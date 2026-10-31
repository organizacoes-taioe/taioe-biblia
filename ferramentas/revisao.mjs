// Monta as duas páginas de revisão do Gere (só o revisor geral):
// - biblia (em /admin/pendencias/, «Bíblia: tradução»): os capítulos «em revisão», só com perguntas
//   pontuais (escolhas de tradução e notas; a divisão e o registro não vão mais a ele, pedido de
//   24/10) e os estudos de palavra de revisao/estudos/*.json;
// - biblia-comentarios («Bíblia: comentários dos Padres», pedido dele, 19/10): à parte, para não
//   misturar com o que é prioritário. Cada comentário que ele ainda não aprovou (`revisto`) e, no
//   fim do tema, o nome dele, para decidir depois de ler os comentários (31/10; o tema não tem
//   mais resumo). Desde 26/10 só o aprovado vai ao site (gerar.mjs,
//   `publicavel`): o capítulo sem escolha pendente, a nota aprovada e o comentário aprovado.
// Sem textos explicativos nas páginas (ele é o único leitor, 19/10).
//
//   node ferramentas/revisao.mjs     grava ../infra/dados/paginas/biblia.json e biblia-comentarios.json
//
// Depois, no taioe-infra: python dados/paginas/gerar.py dados/paginas/<arquivo>.json, commit, e
// Catálogo (taioe-infra, dados/paginas/<arquivo>.sql) no teste e na produção. As respostas dele
// voltam pelo workflow Respostas (ferramentas/respostas.sh; as dos comentários com `comentarios`).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const C = path.join(RAIZ, 'conteudo');
const PAGINAS = process.env.PAGINAS || path.resolve(RAIZ, '..', 'infra', 'dados', 'paginas');
const livros = JSON.parse(fs.readFileSync(path.join(C, 'livros.json'), 'utf8'));
const letra = (i) => (i < 26 ? String.fromCharCode(97 + i) : letra(Math.floor(i / 26) - 1) + letra(i % 26));
const grego = (n) => (n <= 8 || n >= 148 ? n : n <= 10 ? 9 : n <= 113 ? n - 1 : n <= 115 ? 113 : n === 116 ? '114–115' : n <= 146 ? n - 1 : '146–147');

const capitulos = [], comentarios = [];
for (const l of livros) {
  const dir = path.join(C, l.id);
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json')).sort()) {
    const c = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    paraComentarios(c, l);
    if (c.estado !== 'em revisão') continue;
    const id = `${c.livro}-${c.cap}`;
    const rotulo = c.livro === 'salmos' ? `Salmo ${c.cap}${String(grego(c.cap)) !== String(c.cap) ? ` (${grego(c.cap)})` : ''}` : `${l.nome} ${c.cap}`;
    const abrev = c.livro === 'salmos' ? 'Sl' : l.nome;
    const verso = (v) => { const x = c.texto.find((t) => String(t.v) === String(v)); return x ? (x.l ? x.l.join(' / ') : x.t) : ''; };
    const rv = c.revisao || {};
    const secoes = [];

    if (rv.escolhas && rv.escolhas.length) secoes.push({
      id: 'escolhas', titulo: 'Escolhas de tradução',
      itens: rv.escolhas.map((e) => ({ id: `${id}:escolha:${e.id}`, tipo: 'escolha', titulo: e.titulo, ref: e.ref, contexto: e.contexto, opcoes: e.opcoes })),
    });

    const ordem = new Map(c.texto.filter((v) => v.v !== undefined).map((v, i) => [String(v.v), i]));
    // As notas que ele já aprovou (`revista: true`) vão ao site e saem da página; a letra é a da
    // ordem de todas as notas do capítulo (no site, só as aprovadas têm letra).
    const notas = (c.notas || []).slice().sort((a, b) => ordem.get(String(a.v)) - ordem.get(String(b.v)))
      .map((n, i) => ({ ...n, letra: letra(i) })).filter((n) => !n.revista);
    if (notas.length) secoes.push({
      id: 'notas', titulo: 'Notas',
      itens: notas.map((n) => ({ id: `${id}:nota:${n.id}`, tipo: 'nota', ref: `${abrev} ${c.cap},${n.v}`, letra: n.letra, versiculo: verso(n.v), texto: n.texto })),
    });

    // O Gere, 24/10: «me mostre apenas questões pontuais, para eu decidir uma única coisa em cada
    // pendência». A divisão é decisão nossa e o registro vai direto para o ESCOLHAS.md.
    if (rv.divisao || rv.registro) throw new Error(`${id}: revisao.divisao e revisao.registro não vão mais à revisão (CAPITULO.md, etapas 2 e 5)`);

    if (!secoes.length) continue;
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

// Os comentários: um bloco por tema, com os comentários ainda não aprovados e, no fim, o nome do
// tema, se ainda não foi aprovado (pedido do Gere, 31/10: decidir o nome depois de ler).
// Ids: <livro>-<cap>:tt:<trecho>:<tema> (o nome), <livro>-<cap>:c:<trecho>:<tema>:<item>
// (comentário) e <livro>-<cap>:ca<n>:<trecho>:<tema>:<item> (aviso de corte, rodada n).
function paraComentarios(c, l) {
  const id = `${c.livro}-${c.cap}`;
  const rotulo = c.livro === 'salmos' ? `Salmo ${c.cap}${String(grego(c.cap)) !== String(c.cap) ? ` (${grego(c.cap)})` : ''}` : `${l.nome} ${c.cap}`;
  const umSo = c.trechos.length === 1 && !c.trechos[0].titulo;
  const secoes = [];
  for (const t of c.trechos) {
    const com = c.comentarios && c.comentarios[t.id];
    for (const x of (com && com.temas) || []) {
      const rev = x.revisto || [];
      const itens = [];
      for (const it of x.itens) {
        // Corte dele que muda o sentido: volta com o aviso e a sugestão (fora do site até a resposta).
        // O número da rodada entra no id, para não herdar a resposta anterior.
        const a = it.aviso_corte;
        if (a) itens.push({ id: `${id}:ca${a.n}:${t.id}:${x.id}:${it.id}`, tipo: 'comentario-aviso', autor: it.autor, obra: it.obra, passagem: it.passagem, link: it.link, corte: a.corte, aviso: a.aviso, sugestao: it.texto });
        else if (!it.revisto) itens.push({ id: `${id}:c:${t.id}:${x.id}:${it.id}`, tipo: 'comentario', autor: it.autor, sobre: it.sobre, obra: it.obra, passagem: it.passagem, link: it.link, texto: it.texto });
      }
      if (!rev.includes('titulo')) itens.push({ id: `${id}:tt:${t.id}:${x.id}`, tipo: 'tema-titulo', texto: x.titulo });
      if (!itens.length) continue;
      // O alto do bloco não traz o nome: ele vem no fim, depois dos comentários.
      const vv = (x.versiculos || []).length ? `${x.versiculos.length > 1 ? 'Versículos' : 'Versículo'} ${x.versiculos.join(', ')}` : 'Tema';
      secoes.push({
        id: `${t.id}-${x.id}`, titulo: vv,
        sub: umSo ? '' : t.titulo,
        url: `/biblia/${c.livro}/${c.cap}/comentarios/${umSo ? '' : t.id + '/'}${x.id}/`,
        itens,
      });
    }
  }
  if (secoes.length) comentarios.push({ id, rotulo, url: `/biblia/${c.livro}/${c.cap}/`, secoes });
}

function gravar(arquivo, pagina) {
  const destino = path.join(PAGINAS, arquivo);
  fs.writeFileSync(destino, JSON.stringify(pagina, null, 1) + '\n');
  const n = pagina.capitulos.reduce((s, c) => s + c.secoes.reduce((t, x) => t + x.itens.filter((i) => i.tipo !== 'casos').length, 0), 0);
  console.log(`${destino}: ${pagina.capitulos.length} capítulo(s), ${n} itens`);
}
gravar('biblia.json', { slug: 'biblia', titulo: 'Bíblia Taioé: revisão', capitulos });
gravar('biblia-comentarios.json', { slug: 'biblia-comentarios', titulo: 'Bíblia Taioé: comentários', capitulos: comentarios });
