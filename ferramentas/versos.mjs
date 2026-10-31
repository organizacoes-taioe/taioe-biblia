// Passa os versos de um capítulo (as linhas `l` do texto) pelo medidor de verso livre do
// Versificador (Solar/producao/versificador/ferramentas/verso-livre.mjs), para que soem bem em
// português (pedido do Gere, 17/10). A fidelidade ao original vem antes: um verso marcado só se
// reescreve se a nova forma disser o mesmo que o hebraico (ou o grego).
//
//   node ferramentas/versos.mjs salmos 34                 todos os versos, com a medida de cada um
//   node ferramentas/versos.mjs salmos 34 --so-problemas  só os marcados
//   node ferramentas/versos.mjs --verso "Cantai-lhe um cântico novo,"   um verso avulso
//
// Marcas: ralo (mais de 3,5 sílabas por acento), vazio (5 átonas seguidas ou mais), choques (3
// pares de tônicas vizinhas ou mais). No fim, o perfil do capítulo contra as metas do estudo do
// ritmo (sílabas por acento 2,4–2,8; intervalos dos mestres ~15/30/29/16/5 %).
// O Versificador não é repositório: o caminho é relativo a esta pasta (até 2026-10-31,
// Solar/Editora/Versificador, que ainda serve se o novo não existir).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const VERSIFICADOR = [['Solar', 'producao', 'versificador'], ['Solar', 'Editora', 'Versificador']]
  .map((p) => path.resolve(RAIZ, '..', '..', '..', ...p))
  .find((p) => fs.existsSync(p)) ?? path.resolve(RAIZ, '..', '..', '..', 'Solar', 'producao', 'versificador');
const medidor = path.join(VERSIFICADOR, 'ferramentas', 'verso-livre.mjs');
if (!fs.existsSync(medidor)) { console.error(`não achei o Versificador em ${VERSIFICADOR}`); process.exit(1); }
const { medirVerso, perfil } = await import(pathToFileURL(medidor).href);

function linha(ref, m) {
  if (m.vazio) return `${ref.padEnd(8)}   ${m.verso}  [sem leitura]`;
  const extra = [m.ancora && `âncora: ${m.ancora}`, m.marcas.length && m.marcas.join(', ')].filter(Boolean).join(' | ');
  return `${ref.padEnd(8)} ${m.marcas.length ? '✗' : '✓'} ${m.verso}\n${' '.repeat(11)}${m.medida} síl., ${m.acentos.length} acentos (${m.silPorAcento}) | ${m.acentos.join('-')}${extra ? ' | ' + extra : ''}`;
}

const args = process.argv.slice(2);
if (args[0] === '--verso') {
  console.log(linha('', medirVerso(args[1] || '')));
  process.exit(0);
}
const [livro, cap] = args;
if (!livro || !cap) { console.error('uso: node ferramentas/versos.mjs <livro> <capítulo> [--so-problemas] | --verso "..."'); process.exit(1); }
const arq = path.join(RAIZ, 'conteudo', livro, `${String(cap).padStart(3, '0')}.json`);
const c = JSON.parse(fs.readFileSync(arq, 'utf8'));
const so = args.includes('--so-problemas');
const todos = [];
for (const v of c.texto) {
  if (!v.l) continue;
  v.l.forEach((l, i) => {
    const m = medirVerso(l);
    todos.push(m);
    if (!so || (m.marcas && m.marcas.length)) console.log(linha(`${v.v}${v.l.length > 1 ? String.fromCharCode(97 + i) : ''}`, m));
  });
}
if (!todos.length) { console.log('este capítulo não tem versos (só prosa)'); process.exit(0); }
const p = perfil(todos);
console.log(`\n${p.versos} versos, média ${p.mediaSilabas} sílabas | sílabas por acento ${p.silPorAcento} (meta 2,4–2,8)`);
console.log(`intervalos: 1 → ${p.i1}%  2 → ${p.i2}%  3 → ${p.i3}%  4 → ${p.i4}%  5+ → ${p.i5}%   (mestres: ~15 / 30 / 29 / 16 / 5)`);
console.log(`marcados: ${todos.filter((m) => m.marcas && m.marcas.length).length}`);
