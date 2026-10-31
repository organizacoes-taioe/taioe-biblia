// Gera o site estático da Bíblia Taioé (public/biblia/) a partir de conteudo/.
//
//   node ferramentas/gerar.mjs            grava as páginas
//   node ferramentas/gerar.mjs --conferir só confere (o CI usa: falha se public/ estiver velho)
//
// Páginas: /biblia/ (início), /biblia/<livro>/ (capítulos), /biblia/<livro>/<cap>/ (texto e
// notas), /biblia/<livro>/<cap>/comentarios/[<trecho>/] (temas), .../<tema>/ (comentários) e
// /biblia/leituras/ (as leituras do leitor, montadas no navegador).
// Node puro, sem dependências. Nada inline (contrato da origem): CSS e JS são arquivos, com o
// hash no endereço.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CONTEUDO = path.join(RAIZ, 'conteudo');
const SAIDA = path.join(RAIZ, 'public', 'biblia');
const CONFERIR = process.argv.includes('--conferir');
const BASE = '/biblia/';

// ---------------------------------------------------------------- utilidades

const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
// Marcação mínima nas notas e comentários: *itálico*.
const inline = (s) => esc(s).replace(/\*([^*]+)\*/g, '<em>$1</em>');
const paragrafos = (s) => String(s).split(/\n\s*\n/).map((p) => `<p>${inline(p.trim())}</p>`).join('');
const hash = (f) => crypto.createHash('sha256').update(fs.readFileSync(path.join(SAIDA, f))).digest('hex').slice(0, 8);
const CSS = `${BASE}css/estilo.css?v=${hash('css/estilo.css')}`;
const JS = `${BASE}js/biblia.js?v=${hash('js/biblia.js')}`;
// As notas: o mesmo arquivo da Biblioteca (o workflow Cópias confere o sha256).
const NOTAS = `${BASE}js/notas.js?v=${hash('js/notas.js')}`;
// Lido antes de desenhar a página (sem defer): tema e tamanho da letra escolhidos, sem piscar.
const PREF = `${BASE}js/preferencias.js?v=${hash('js/preferencias.js')}`;

const LIVROS = JSON.parse(fs.readFileSync(path.join(CONTEUDO, 'livros.json'), 'utf8'));
const livroPorId = Object.fromEntries(LIVROS.map((l) => [l.id, l]));

// Os Salmos têm a numeração hebraica, com a grega e latina (a dos Padres e da liturgia antiga)
// entre parênteses: Sl 9–10 hebraicos são o 9 grego; 114–115 são o 113; 116 é 114–115; 147 é 146–147.
function numeroGrego(n) {
  if (n <= 8 || n >= 148) return String(n);
  if (n === 9 || n === 10) return '9';
  if (n <= 113) return String(n - 1);
  if (n === 114 || n === 115) return '113';
  if (n === 116) return '114–115';
  if (n <= 146) return String(n - 1);
  return '146–147';
}
function rotuloCap(livro, cap) {
  if (livro === 'salmos') {
    const g = numeroGrego(cap);
    return { curto: `Salmo ${cap}`, longo: g === String(cap) ? `Salmo ${cap}` : `Salmo ${cap} (${g})`, grego: g === String(cap) ? '' : g };
  }
  const nome = livroPorId[livro].nome;
  return { curto: `${nome} ${cap}`, longo: `${nome} ${cap}`, grego: '' };
}
const refVers = (livro, cap, vs) => {
  if (!vs || !vs.length) return '';
  const abrev = livro === 'salmos' ? 'Sl' : livroPorId[livro].nome;
  const faixa = vs.length > 1 && vs[vs.length - 1] - vs[0] === vs.length - 1 ? `${vs[0]}–${vs[vs.length - 1]}` : vs.join('.');
  return `${abrev} ${cap},${faixa}`;
};

// ---------------------------------------------------------------- moldura

// Ícones da barra de cima (SVG no HTML, sem estilo inline).
const ICONE_TEMA = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg>';
const ICONE_LEITURA = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="fita" d="M6.5 3.5h11v17l-5.5-4-5.5 4z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>';

function pagina({ titulo, descricao, inicio = false, trilha = [], corpo, classe = '', cap = '' }) {
  const marca = inicio ? '<a class="marca" href="/">Taioé</a>' : `<a class="marca" href="${BASE}">Bíblia</a>`;
  const nav = trilha.length
    ? `<nav class="trilha" aria-label="Trilha de navegação">${trilha.map(([t, h]) => (h ? `<a href="${h}">${esc(t)}</a>` : `<span aria-current="page">${esc(t)}</span>`)).join('<span class="sep">›</span>')}</nav>`
    : '';
  return `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>${esc(titulo)}</title>
<meta name="description" content="${esc(descricao)}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="${BASE}favicon.svg" type="image/svg+xml">
<script src="${PREF}"></script>
<link rel="stylesheet" href="${CSS}">
<script defer src="${JS}"></script>
<script defer src="${NOTAS}"></script>
</head>
<body${classe ? ` class="${classe}"` : ''}${cap ? ` data-cap="${esc(cap)}"` : ''}>
<a class="pular" href="#app">Ir para o conteúdo</a>
<header class="topo">
  <div class="topo-int">
    ${marca}
    ${nav}
    <div class="ferramentas">
      <button type="button" class="ferr so-js" id="letra-menor" aria-label="Letra menor" title="Letra menor"><span class="a-menor">A</span>−</button>
      <button type="button" class="ferr so-js" id="letra-maior" aria-label="Letra maior" title="Letra maior"><span class="a-maior">A</span>+</button>
      <button type="button" class="ferr so-js" id="trocar-tema" aria-label="Modo claro ou escuro" title="Modo claro ou escuro">${ICONE_TEMA}</button>
      <a class="ferr" id="botao-leituras" href="${BASE}leituras/" aria-label="Leituras" title="Leituras">${ICONE_LEITURA}</a>
      <div class="menu-leitura" id="menu-leitura" hidden>
        <p class="menu-titulo">Leitura aberta</p>
        <p class="menu-nome" id="menu-nome"></p>
        <p class="menu-pos" id="menu-pos"></p>
        <a class="menu-item" href="${BASE}leituras/">Ver as leituras</a>
        <button type="button" class="menu-item" id="fechar-leitura">Fechar esta leitura</button>
      </div>
    </div>
  </div>
</header>
<main id="app" tabindex="-1">
${corpo}
</main>
<footer class="rodape">
  <p><a href="/">Taioé</a> · <a href="/privacidade/">Privacidade</a> · <a href="/termos/">Termos de uso</a></p>
</footer>
</body>
</html>
`;
}
const voltar = (h, t) => `<p class="voltar"><a href="${h}">← ${esc(t)}</a></p>`;

// ---------------------------------------------------------------- capítulos

function lerCapitulos() {
  const caps = [];
  for (const l of LIVROS) {
    const dir = path.join(CONTEUDO, l.id);
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir).filter((f) => /^\d{3}\.json$/.test(f)).sort()) {
      const c = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
      if (c.livro !== l.id || c.cap !== Number(f.slice(0, 3))) throw new Error(`${l.id}/${f}: livro ou capítulo não confere`);
      caps.push(c);
    }
  }
  return caps;
}

// O que o leitor vê (o Gere, 26/10: «as notas da bíblia e dos outros livros comentados só
// apareçam para os usuários na medida em que eu os for confirmando»):
// - o capítulo, só sem escolha de tradução esperando a resposta dele (`revisao.escolhas`);
// - a nota, só aprovada: `revista`, ou o capítulo inteiro `revisado`;
// - o comentário, só aprovado (`revisto`), e nunca o que voltou com aviso de corte;
// - o tema, só com o título aprovado e algum comentário aprovado. Desde 31/10 o tema não tem
//   resumo: só um nome bem descritivo (pedido do Gere).
function publicavel(c) {
  if (c.revisao && c.revisao.escolhas && c.revisao.escolhas.length) return null;
  const comentarios = {};
  for (const [tid, com] of Object.entries(c.comentarios || {})) {
    const temas = [];
    for (const x of com.temas || []) {
      const rev = x.revisto || [];
      const itens = x.itens.filter((it) => it.revisto && !it.aviso_corte);
      if (!rev.includes('titulo') || !itens.length) continue;
      temas.push({ ...x, itens });
    }
    comentarios[tid] = { ...com, temas };
  }
  return { ...c, notas: c.notas.filter((n) => c.estado === 'revisado' || n.revista), comentarios };
}

// Letras das notas: a, b, …, z, aa, ab…
const letra = (i) => (i < 26 ? String.fromCharCode(97 + i) : letra(Math.floor(i / 26) - 1) + letra(i % 26));

// Põe as marcas das notas no texto de um versículo. Cada nota tem `apos` (a palavra ou expressão
// depois da qual a marca entra, na 1ª ocorrência dentro do versículo); sem `apos`, a marca fica
// no fim do versículo. Devolve as linhas (verso) ou o texto (prosa) já em HTML.
function marcarNotas(v, notasDoV, contexto) {
  const partes = v.l ? v.l.slice() : [v.t];
  const marcas = partes.map(() => []);   // [posição, html] por linha
  for (const n of notasDoV) {
    const m = `<a class="nota-ref" href="#nota-${n.letra}" id="ref-${n.letra}" data-nota="${n.letra}" aria-label="Nota ${n.letra}">${n.letra}</a>`;
    let feito = false;
    if (n.apos) {
      for (let i = 0; i < partes.length && !feito; i++) {
        const p = partes[i].indexOf(n.apos);
        if (p >= 0) { marcas[i].push([p + n.apos.length, m]); feito = true; }
      }
      if (!feito) throw new Error(`${contexto}, v. ${v.v}: nota ${n.id} — «${n.apos}» não está no versículo`);
    } else {
      marcas[partes.length - 1].push([partes[partes.length - 1].length, m]);
    }
  }
  return partes.map((txt, i) => {
    const ms = marcas[i].sort((a, b) => a[0] - b[0]);
    let h = '', pos = 0;
    for (const [p, m] of ms) { h += esc(txt.slice(pos, p)) + m; pos = p; }
    return h + esc(txt.slice(pos));
  });
}

function montarTexto(c, notasPorV, botaoTrecho) {
  const ctx = `${c.livro} ${c.cap}`;
  let h = '', buf = [], modo = null, trecho = 0;
  const fechar = () => {
    if (buf.length) h += modo === 'poesia' ? `<p class="poesia">${buf.join(' ')}</p>` : `<p class="par">${buf.join(' ')}</p>`;
    buf = []; modo = null;
  };
  for (const v of c.texto) {
    if (v.s) {
      fechar();
      const t = c.trechos[trecho++];
      h += `<h2 class="sub-trecho">${esc(v.s)}</h2>${botaoTrecho(t)}`;
      continue;
    }
    const tipo = v.l ? 'poesia' : 'par';
    if (v.np || modo !== tipo) fechar();
    modo = tipo;
    const num = `<span class="num" id="v${esc(String(v.v).replace(/[^0-9a-z]/gi, ''))}">${esc(v.v)}</span>`;
    const partes = marcarNotas(v, notasPorV[v.v] || [], ctx);
    if (v.l) buf.push(partes.map((ln, i) => `<span class="linha"><span class="calha">${i ? '' : num}</span><span class="txt">${ln}</span></span>`).join(' '));
    else buf.push(num + partes[0]);
  }
  fechar();
  return h;
}

function paginaCapitulo(c, vizinhos) {
  const livro = livroPorId[c.livro], r = rotuloCap(c.livro, c.cap);
  const url = `${BASE}${c.livro}/${c.cap}/`;
  const umSo = c.trechos.length === 1 && !c.trechos[0].titulo;
  const temComent = (t) => c.comentarios && c.comentarios[t.id] && c.comentarios[t.id].temas && c.comentarios[t.id].temas.length;
  const sobre = c.livro === 'salmos' ? 'este salmo' : (umSo ? 'este capítulo' : 'este trecho');
  const botao = (t) => (temComent(t)
    ? `<p class="ver-coment"><a class="botao" href="${url}comentarios/${umSo ? '' : t.id + '/'}">Ver comentários sobre ${umSo ? sobre : 'este trecho'}</a></p>`
    : '');

  // Notas: em ordem de versículo; letra na ordem em que aparecem.
  const ordemV = new Map(c.texto.filter((v) => v.v !== undefined).map((v, i) => [String(v.v), i]));
  const notas = c.notas.slice().sort((a, b) => ordemV.get(String(a.v)) - ordemV.get(String(b.v)));
  notas.forEach((n, i) => { n.letra = letra(i); });
  const notasPorV = {};
  for (const n of notas) (notasPorV[n.v] = notasPorV[n.v] || []).push(n);

  const corpo = `<article class="folha">
${voltar(`${BASE}${c.livro}/`, livro.nome)}
<header class="cab-cap">
  <h1>${esc(r.curto)}${r.grego ? ` <span class="num-grega" title="Na numeração grega e latina">(${esc(r.grego)})</span>` : ''}</h1>
  ${umSo ? botao(c.trechos[0]) : ''}
</header>
<div class="texto">${montarTexto(c, notasPorV, botao)}</div>
${notas.length ? `<section class="notas" aria-labelledby="titulo-notas"><h2 id="titulo-notas">Notas</h2><ol>${notas.map((n) => `<li id="nota-${n.letra}"><a class="nota-letra" href="#ref-${n.letra}" aria-label="Voltar ao texto">${n.letra}</a> <span class="nota-v">v. ${esc(n.v)}</span> <span class="nota-texto">${inline(n.texto)}</span></li>`).join('')}</ol></section>` : ''}
${passos(vizinhos, (x) => rotuloCap(x.livro, x.cap).curto, (x) => `${BASE}${x.livro}/${x.cap}/`, 'Navegação entre capítulos')}
${r.grego ? `<p class="pequeno apagado">A Bíblia Taioé numera os salmos pelo hebraico; entre parênteses vai o número da Bíblia grega e da latina, que é o que os Padres da Igreja e a liturgia antiga usam.</p>` : ''}
</article>
<div class="nota-painel" id="nota-painel" role="dialog" aria-modal="false" aria-labelledby="nota-painel-ref" hidden>
  <p class="nota-painel-ref" id="nota-painel-ref"></p>
  <div class="nota-painel-texto" id="nota-painel-texto"></div>
</div>`;
  return pagina({
    titulo: `${r.longo} · Bíblia Taioé`,
    descricao: `${r.longo}: tradução dos originais, com notas e comentários dos Padres da Igreja e dos santos.`,
    trilha: [[livro.nome, `${BASE}${c.livro}/`], [r.curto, null]],
    corpo, classe: 'pag-capitulo', cap: r.curto,
  });
}

function passos(v, rot, href, rotulo) {
  if (!v.ant && !v.seg) return '';
  return `<nav class="passos" aria-label="${rotulo}">${v.ant ? `<a class="passo ant" href="${href(v.ant)}" rel="prev"><span class="dir">← Anterior</span><span class="alvo">${esc(rot(v.ant))}</span></a>` : '<span></span>'}${v.seg ? `<a class="passo seg" href="${href(v.seg)}" rel="next"><span class="dir">Seguinte →</span><span class="alvo">${esc(rot(v.seg))}</span></a>` : ''}</nav>`;
}

// ---------------------------------------------------------------- comentários

function versosDoTema(c, vs) {
  if (!vs || !vs.length) return '';
  const set = new Set(vs.map(String));
  const linhas = c.texto.filter((v) => v.v !== undefined && set.has(String(v.v)));
  if (!linhas.length) return '';
  return `<blockquote class="versos-tema">${linhas.map((v) => (v.l
    ? `<p class="poesia">${v.l.map((ln, i) => `<span class="linha"><span class="calha">${i ? '' : `<span class="num">${esc(v.v)}</span>`}</span><span class="txt">${esc(ln)}</span></span>`).join(' ')}</p>`
    : `<p class="par"><span class="num">${esc(v.v)}</span>${esc(v.t)}</p>`)).join('')}</blockquote>`;
}

function paginasComentarios(c, gravar) {
  const r = rotuloCap(c.livro, c.cap), livro = livroPorId[c.livro];
  const urlCap = `${BASE}${c.livro}/${c.cap}/`;
  const umSo = c.trechos.length === 1 && !c.trechos[0].titulo;
  for (const t of c.trechos) {
    const com = c.comentarios && c.comentarios[t.id];
    if (!com || !com.temas || !com.temas.length) continue;
    const urlT = `${urlCap}comentarios/${umSo ? '' : t.id + '/'}`;
    const nomeTrecho = umSo ? r.longo : `${r.curto}: ${t.titulo}`;
    const total = com.temas.reduce((s, x) => s + x.itens.length, 0);
    const indice = `<article class="folha">
${voltar(urlCap, r.curto)}
<header class="cab-coment">
  <p class="sobretitulo">Comentários</p>
  <h1>${esc(nomeTrecho)}</h1>
  ${com.intro ? `<div class="intro">${paragrafos(com.intro)}</div>` : ''}
  <p class="apagado pequeno">${com.temas.length} temas · ${total} comentários. Escolha um tema.</p>
</header>
<nav class="temas" aria-label="Temas dos comentários">
${com.temas.map((x) => `<a class="tema" href="${urlT}${x.id}/"><span class="tema-titulo">${esc(x.titulo)}</span>${x.versiculos && x.versiculos.length ? `<span class="tema-ref">${esc(refVers(c.livro, c.cap, x.versiculos))}</span>` : ''}<span class="tema-n">${x.itens.length === 1 ? '1 comentário' : x.itens.length + ' comentários'}</span></a>`).join('\n')}
</nav>
<p class="pequeno apagado aviso-trad">As traduções dos comentários são da Bíblia Taioé, feitas dos originais; cada comentário traz a referência e o link para o texto na língua em que foi escrito.</p>
</article>`;
    gravar(urlT, pagina({
      titulo: `Comentários: ${nomeTrecho} · Bíblia Taioé`,
      descricao: `Comentários dos Padres da Igreja e dos santos sobre ${nomeTrecho}, organizados por tema.`,
      trilha: [[livro.nome, `${BASE}${c.livro}/`], [r.curto, urlCap], ['Comentários', null]],
      corpo: indice, classe: 'pag-temas',
    }));

    com.temas.forEach((x, i) => {
      const viz = { ant: com.temas[i - 1], seg: com.temas[i + 1] };
      const corpo = `<article class="folha">
<p class="voltar"><a href="${urlT}">← Todos os temas</a><span class="sep">·</span><a href="${urlCap}">${esc(r.curto)}</a></p>
<header class="cab-coment">
  <p class="sobretitulo">Comentários · ${esc(nomeTrecho)}</p>
  <h1>${esc(x.titulo)}</h1>
</header>
${versosDoTema(c, x.versiculos)}
<div class="comentarios">
${x.itens.map((it) => `<details class="comentario">
  <summary><span class="abrir" aria-hidden="true"></span><span class="autor">${esc(it.autor)}</span></summary>
  <div class="comentario-texto">${paragrafos(it.texto)}</div>
  <p class="autoria"><span class="autor">${esc(it.autor)}</span>${it.sobre ? `<span class="sobre-autor">, ${esc(it.sobre)}</span>` : ''}<br><span class="obra"><em>${esc(it.obra)}</em>${it.passagem ? `, ${esc(it.passagem)}` : ''}</span>${it.link ? ` · <a href="${esc(it.link)}" rel="noopener">texto original</a>` : ''}</p>
</details>`).join('\n')}
</div>
${passos(viz, (t) => t.titulo, (t) => `${urlT}${t.id}/`, 'Navegação entre temas')}
</article>`;
      gravar(`${urlT}${x.id}/`, pagina({
        titulo: `${x.titulo} · Comentários ao ${r.curto} · Bíblia Taioé`,
        descricao: `${x.titulo}: comentários sobre ${nomeTrecho}.`,
        trilha: [[livro.nome, `${BASE}${c.livro}/`], [r.curto, urlCap], ['Comentários', urlT], [x.titulo, null]],
        corpo, classe: 'pag-tema',
      }));
    });
  }
}

// ---------------------------------------------------------------- índices

// Os 73 livros, por Testamento e pelos grupos de livros.json, numa linha corrida. Livro com
// capítulo pronto vira link para a sua grade; os outros ficam apagados, sem link.
function paginaInicio(caps) {
  const tem = new Set(caps.map((c) => c.livro));
  const testamento = (sigla, nome) => {
    const grupos = [];
    for (const l of LIVROS.filter((x) => x.testamento === sigla)) {
      if (!grupos.length || grupos[grupos.length - 1][0] !== l.grupo) grupos.push([l.grupo, []]);
      grupos[grupos.length - 1][1].push(l);
    }
    return `<section class="testamento" aria-labelledby="t-${sigla}">
<h2 id="t-${sigla}">${nome}</h2>
${grupos.map(([g, ls]) => `<h3>${esc(g)}</h3>
<p class="livros">${ls.map((l) => (tem.has(l.id) ? `<a href="${BASE}${l.id}/">${esc(l.nome)}</a>` : `<span class="vazio">${esc(l.nome)}</span>`)).join('<span class="sep" aria-hidden="true">&nbsp;· </span>')}</p>`).join('\n')}
</section>`;
  };
  const corpo = `<article class="folha capa">
<h1>Bíblia Taioé</h1>
<p class="subtitulo">Sagrada Escritura</p>
<nav class="indice-livros" aria-label="Livros da Bíblia">
${testamento('AT', 'Antigo Testamento')}
${testamento('NT', 'Novo Testamento')}
</nav>
</article>`;
  return pagina({ titulo: 'Bíblia Taioé', descricao: 'A Sagrada Escritura traduzida dos originais, com notas e os comentários dos Padres da Igreja e dos santos.', inicio: true, corpo, classe: 'pag-inicio' });
}

function paginaLivro(l, caps) {
  const tem = new Set(caps.filter((c) => c.livro === l.id).map((c) => c.cap));
  const grade = Array.from({ length: l.capitulos }, (_, i) => i + 1).map((n) => (tem.has(n)
    ? `<a class="cap" href="${BASE}${l.id}/${n}/" aria-label="${esc(rotuloCap(l.id, n).longo)}">${n}</a>`
    : `<span class="cap vazio" aria-hidden="true">${n}</span>`)).join('');
  const corpo = `<article class="folha">
${voltar(BASE, 'Bíblia Taioé')}
<h1>${esc(l.nome)}</h1>
<p class="apagado pequeno">${tem.size === 1 ? 'Por enquanto, 1 capítulo disponível' : `Por enquanto, ${tem.size} capítulos disponíveis`}${l.id === 'salmos' ? '. A numeração é a hebraica; o número da Bíblia grega e da latina aparece em cada salmo, entre parênteses' : ''}.</p>
<nav class="grade-caps" aria-label="Capítulos">${grade}</nav>
</article>`;
  return pagina({ titulo: `${l.nome} · Bíblia Taioé`, descricao: `${l.nome}: capítulos disponíveis na Bíblia Taioé.`, trilha: [[l.nome, null]], corpo, classe: 'pag-livro' });
}

// As leituras: pontos de leitura que acompanham o leitor (ficam no navegador; js/biblia.js
// monta a lista). Sem JavaScript, só o aviso.
function paginaLeituras() {
  const corpo = `<article class="folha">
${voltar(BASE, 'Bíblia Taioé')}
<h1>Leituras</h1>
<div id="leituras" class="leituras"><p class="apagado">As leituras precisam de JavaScript.</p></div>
<form class="nova-leitura so-js" id="nova-leitura">
  <label for="nome-leitura">Nova leitura</label>
  <div class="nova-linha"><input id="nome-leitura" name="nome" maxlength="60" autocomplete="off" placeholder="Nome" required><button type="submit" class="botao">Criar e abrir</button></div>
  <p class="pequeno apagado" id="nova-onde"></p>
</form>
<p class="pequeno apagado">Uma leitura aberta acompanha você: a posição dela muda conforme você lê, e ela volta ao último ponto quando você a abrir de novo. As leituras ficam só neste navegador.</p>
</article>`;
  return pagina({ titulo: 'Leituras · Bíblia Taioé', descricao: 'As suas leituras da Bíblia Taioé.', trilha: [['Leituras', null]], corpo, classe: 'pag-leituras' });
}

// ---------------------------------------------------------------- gravação

const geradas = new Map();   // caminho relativo a public/biblia → conteúdo
const gravar = (url, html) => geradas.set(path.join(...url.slice(BASE.length).split('/').filter(Boolean), 'index.html'), html);

const caps = lerCapitulos().map(publicavel).filter(Boolean);
gravar(BASE, paginaInicio(caps));
gravar(`${BASE}leituras/`, paginaLeituras());
geradas.set('404.html', pagina({ titulo: 'Página não encontrada · Bíblia Taioé', descricao: 'Página não encontrada.', corpo: `<article class="folha">
${voltar(BASE, 'Bíblia Taioé')}
<h1>Página não encontrada</h1>
<p>Este capítulo ainda não está na Bíblia Taioé, ou o endereço mudou.</p>
</article>` }));
for (const l of LIVROS) if (caps.some((c) => c.livro === l.id)) gravar(`${BASE}${l.id}/`, paginaLivro(l, caps));
caps.forEach((c, i) => {
  // Só entre capítulos disponíveis: com um capítulo de cada vez, não há vizinho «vazio».
  gravar(`${BASE}${c.livro}/${c.cap}/`, paginaCapitulo(c, { ant: caps[i - 1], seg: caps[i + 1] }));
  paginasComentarios(c, gravar);
});

// O que foi gerado antes e não é mais (capítulo ou tema que saiu) é apagado.
const FIXOS = new Set(['css', 'js', 'favicon.svg', '404.html']);
function htmlsExistentes(dir, rel = '') {
  const out = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const r = path.join(rel, e.name);
    if (!rel && FIXOS.has(e.name)) continue;
    if (e.isDirectory()) out.push(...htmlsExistentes(path.join(dir, e.name), r));
    else if (e.name === 'index.html') out.push(r);
  }
  return out;
}
const existentes = htmlsExistentes(SAIDA);
let diferencas = 0;
for (const [rel, html] of geradas) {
  const f = path.join(SAIDA, rel);
  const antes = fs.existsSync(f) ? fs.readFileSync(f, 'utf8') : null;
  if (antes === html) continue;
  diferencas++;
  if (CONFERIR) { console.error(`velho: ${rel}`); continue; }
  fs.mkdirSync(path.dirname(f), { recursive: true });
  fs.writeFileSync(f, html);
}
for (const rel of existentes) {
  if (geradas.has(rel)) continue;   // o 404.html nunca entra aqui: está em FIXOS
  diferencas++;
  if (CONFERIR) { console.error(`sobra: ${rel}`); continue; }
  fs.rmSync(path.join(SAIDA, rel));
}
if (CONFERIR && diferencas) { console.error(`public/ está velho em ${diferencas} arquivo(s): rode node ferramentas/gerar.mjs`); process.exit(1); }
console.log(`${geradas.size} páginas${CONFERIR ? ' conferidas' : `, ${diferencas} gravadas ou apagadas`}`);
