// Monta a página de revisão do Gere (/admin/biblia/, só o revisor geral) a partir dos capítulos
// «em revisão» (escolhas de tradução, notas, divisão e o que entra no registro de escolhas da Bíblia
// inteira) e dos estudos de palavra de revisao/estudos/*.json. Os comentários dos Padres não entram:
// o Gere não os aprova um por um; lê no site e pede as mudanças na conversa (17/10).
//
//   node ferramentas/revisao.mjs     grava ../infra/dados/paginas/biblia.json
//
// Depois, no taioe-infra: python dados/paginas/gerar.py dados/paginas/biblia.json, commit, e
// Catálogo (taioe-infra, dados/paginas/biblia.sql) no teste e na produção. As respostas dele
// voltam pelo workflow Respostas (ferramentas/respostas.sh).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const C = path.join(RAIZ, 'conteudo');
const DESTINO = path.resolve(RAIZ, '..', 'infra', 'dados', 'paginas', 'biblia.json');
const livros = JSON.parse(fs.readFileSync(path.join(C, 'livros.json'), 'utf8'));
const letra = (i) => (i < 26 ? String.fromCharCode(97 + i) : letra(Math.floor(i / 26) - 1) + letra(i % 26));
const grego = (n) => (n <= 8 || n >= 148 ? n : n <= 10 ? 9 : n <= 113 ? n - 1 : n <= 115 ? 113 : n === 116 ? '114–115' : n <= 146 ? n - 1 : '146–147');

const capitulos = [];
for (const l of livros) {
  const dir = path.join(C, l.id);
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json')).sort()) {
    const c = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    if (c.estado !== 'em revisão') continue;
    const id = `${c.livro}-${c.cap}`;
    const rotulo = c.livro === 'salmos' ? `Salmo ${c.cap}${String(grego(c.cap)) !== String(c.cap) ? ` (${grego(c.cap)})` : ''}` : `${l.nome} ${c.cap}`;
    const abrev = c.livro === 'salmos' ? 'Sl' : l.nome;
    const verso = (v) => { const x = c.texto.find((t) => String(t.v) === String(v)); return x ? (x.l ? x.l.join(' / ') : x.t) : ''; };
    const rv = c.revisao || {};
    const secoes = [];

    if (rv.escolhas && rv.escolhas.length) secoes.push({
      id: 'escolhas', titulo: 'Escolhas de tradução',
      texto: 'O texto do site já está com a opção recomendada. Se você escolher outra, eu troco no texto e registro a regra para os capítulos seguintes.',
      itens: rv.escolhas.map((e) => ({ id: `${id}:escolha:${e.id}`, tipo: 'escolha', titulo: e.titulo, ref: e.ref, contexto: e.contexto, opcoes: e.opcoes })),
    });

    const ordem = new Map(c.texto.filter((v) => v.v !== undefined).map((v, i) => [String(v.v), i]));
    const notas = (c.notas || []).slice().sort((a, b) => ordem.get(String(a.v)) - ordem.get(String(b.v)));
    if (notas.length) secoes.push({
      id: 'notas', titulo: 'Notas',
      texto: 'Uma por uma: aprovar, alterar o texto ou excluir. A explicação me ajuda a acertar o tom das próximas.',
      itens: notas.map((n, i) => ({ id: `${id}:nota:${n.id}`, tipo: 'nota', ref: `${abrev} ${c.cap},${n.v}`, letra: letra(i), versiculo: verso(n.v), texto: n.texto, origem: n.origem ? `Origem: ${n.origem}.` : '' })),
    });

    if (rv.divisao) secoes.push({
      id: 'divisao', titulo: 'Divisão do texto',
      itens: [{ id: `${id}:divisao`, tipo: 'avaliacao', titulo: rv.divisao.titulo || 'Trechos e estrofes', texto: rv.divisao.texto }],
    });

    if (rv.registro && rv.registro.length) secoes.push({
      id: 'registro', titulo: 'Para a Bíblia inteira',
      texto: 'Escolhas que este capítulo fixou e que passam a valer nos capítulos seguintes (ficam no ESCOLHAS.md do repositório).',
      itens: rv.registro.map((r) => ({ id: `${id}:registro:${r.id}`, tipo: 'avaliacao', titulo: r.titulo, texto: r.texto })),
    });

    secoes.push({ id: 'geral', titulo: 'Observações gerais', itens: [{ id: `${id}:geral`, tipo: 'avaliacao', titulo: 'Sobre o capítulo como um todo', texto: 'Qualquer outra coisa: o tom das notas, a tradução, o que faltou. Os comentários dos Padres ficam no site; quando quiser mudar algum, é só pedir na conversa.', rotuloAprovar: 'Nada a acrescentar' }] });

    capitulos.push({ id, rotulo, url: `/biblia/${c.livro}/${c.cap}/`, estado: `${c.estado}, atualizado em ${c.atualizado.split('-').reverse().join('/')}`, secoes });
  }
}

// Estudos de uma palavra (ex.: nefesh): o resumo, os casos (cada versículo em cada opção) e a decisão.
const ESTUDOS = path.join(RAIZ, 'revisao', 'estudos');
if (fs.existsSync(ESTUDOS)) {
  for (const f of fs.readdirSync(ESTUDOS).filter((x) => x.endsWith('.json')).sort()) {
    const e = JSON.parse(fs.readFileSync(path.join(ESTUDOS, f), 'utf8'));
    if (e.estado !== 'em revisão') continue;
    const id = `estudo-${e.id}`;
    const opcoes = e.escolha.opcoes.map((o) => ({ id: o.id, rotulo: `Opção ${o.id.toUpperCase()}` }));
    capitulos.push({
      id, rotulo: e.titulo.replace(/\*/g, ''),
      url: `https://github.com/organizacoes-taioe/taioe-biblia/blob/main/revisao/estudos/${f.replace(/\.json$/, '.md')}`,
      rotuloUrl: 'Ler o estudo inteiro',
      estado: `${e.estado}, atualizado em ${e.atualizado.split('-').reverse().join('/')}`,
      secoes: [
        { id: 'casos', titulo: 'Os casos', texto: e.resumo, itens: [{ id: `${id}:casos`, tipo: 'casos', casos: e.casos, opcoes }] },
        { id: 'escolha', titulo: 'A decisão', itens: [{ id: `${id}:escolha:${e.id}`, tipo: 'escolha', titulo: e.escolha.titulo, contexto: e.escolha.contexto,
          opcoes: e.escolha.opcoes.map((o) => ({ ...o, texto: `${o.id.toUpperCase()}. ${o.texto}` })) }] },
      ],
    });
  }
}

const pagina = {
  slug: 'biblia',
  titulo: 'Bíblia Taioé: revisão',
  intro: 'Os capítulos e os estudos que esperam a sua avaliação. Cada resposta grava sozinha, assim que você clica ou para de digitar; pode mudar quando quiser. Eu leio as respostas, aplico no texto e uso as explicações nos capítulos seguintes.',
  capitulos,
};
fs.writeFileSync(DESTINO, JSON.stringify(pagina, null, 1) + '\n');
const n = capitulos.reduce((s, c) => s + c.secoes.reduce((t, x) => t + x.itens.filter((i) => i.tipo !== 'casos').length, 0), 0);
console.log(`${DESTINO}: ${capitulos.length} capítulo(s), ${n} itens`);
