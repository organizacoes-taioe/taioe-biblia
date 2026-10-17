// Traz um capítulo do projeto antigo (Software MEU/biblia, a tradução de partida) para
// conteudo/<livro>/<cap>.json, no formato da Bíblia Taioé. Só cria: não sobrescreve um capítulo
// que já exista, porque a partir daqui o texto vivo é o da Taioé (decisão do Gere, 17/10/2026).
//
//   node ferramentas/importar.mjs salmos 33
//
// Na primeira vez, cria conteudo/livros.json (o registro dos livros, na ordem do cânon); depois
// ele é da Taioé (os Evangelhos, que no projeto antigo são só a harmonia, entram aqui como livros).
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const ANTIGO = path.resolve(RAIZ, '..', '..', 'biblia');   // taioe/biblia → Software MEU/biblia
const [livro, capTxt] = process.argv.slice(2);
const cap = Number(capTxt);
if (!livro || !Number.isInteger(cap) || cap < 1) {
  console.error('uso: node ferramentas/importar.mjs <livro> <capítulo>');
  process.exit(1);
}

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(ANTIGO, 'dados-livros.js'), 'utf8'), ctx);
const LIVROS = ctx.window.LIVROS_SEED;
if (!LIVROS[livro]) { console.error(`livro desconhecido: ${livro}`); process.exit(1); }
ctx.window.TEXTOS_SEED = ctx.window.TEXTOS_SEED || {};
vm.runInContext(fs.readFileSync(path.join(ANTIGO, 'livros', `${livro}.js`), 'utf8'), ctx);
const versos = (ctx.window.TEXTOS_SEED[livro] || {})[cap];
if (!versos) { console.error(`${livro} ${cap} não existe no projeto antigo`); process.exit(1); }

// Registro dos livros: id, nome, grupo, capítulos. Só na primeira vez: depois ele é da Taioé
// (73 livros, com o testamento e os quatro Evangelhos) e não se sobrescreve.
const arqLivros = path.join(RAIZ, 'conteudo', 'livros.json');
if (!fs.existsSync(arqLivros)) {
  const registro = Object.entries(LIVROS).map(([id, l]) => ({ id, nome: l.nome, grupo: l.grupo, capitulos: l.capitulos }));
  fs.writeFileSync(arqLivros, JSON.stringify(registro, null, 1) + '\n');
}

const destino = path.join(RAIZ, 'conteudo', livro, String(cap).padStart(3, '0') + '.json');
if (fs.existsSync(destino)) { console.error(`${destino} já existe: o texto vivo é o da Taioé`); process.exit(1); }

// As notas saem do versículo e vão para a lista de notas (uma por item, com id estável).
const notas = [];
const texto = versos.map((v) => {
  const o = { ...v };
  if (o.n) { notas.push({ id: `n${String(notas.length + 1).padStart(2, '0')}`, v: o.v, texto: o.n, origem: 'projeto antigo' }); delete o.n; }
  return o;
});
// Trechos: cada subtítulo abre um; sem subtítulo, o capítulo é um trecho só.
const trechos = [];
texto.forEach((v, i) => {
  if (v.s) trechos.push({ id: String(trechos.length + 1), titulo: v.s, de: texto[i + 1] ? texto[i + 1].v : null });
});
if (!trechos.length) trechos.push({ id: '1', titulo: null, de: texto[0].v });

const capitulo = {
  livro, cap,
  estado: 'em preparo',
  atualizado: new Date().toISOString().slice(0, 10),
  trechos, texto, notas,
  comentarios: {},
};
fs.mkdirSync(path.dirname(destino), { recursive: true });
fs.writeFileSync(destino, JSON.stringify(capitulo, null, 1) + '\n');
console.log(`${destino}: ${texto.length} itens, ${notas.length} notas`);
