// Aplica no conteudo/ as respostas do Gere na página dos comentários (/admin/biblia-comentarios/).
//
//   bash ferramentas/respostas.sh comentarios exportar      → caminho do JSON
//   node ferramentas/aplicar-comentarios.mjs <respostas.json>
//
// - título ou resumo de tema aprovado: entra em `revisto` do tema; alterado: troca o texto e entra;
// - comentário aprovado: `revisto: true`; excluído: sai (e o tema sem comentários sai também);
// - comentário alterado (ele só corta): o texto novo entra com `revisto: true`, e cada corte é
//   listado no fim, com o antes e o depois, para conferir se o sentido ficou fiel ao original.
//   Corte que muda o sentido: acertar à mão e dizer a ele.
// Grava <respostas>.aplicadas.json (o que entrou), para `respostas.sh comentarios marcar`.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const arquivo = process.argv[2];
if (!arquivo) { console.error('uso: node ferramentas/aplicar-comentarios.mjs <respostas.json>'); process.exit(1); }
const respostas = (JSON.parse(fs.readFileSync(arquivo, 'utf8')).respostas || []).filter((r) => !r.lida);

const caps = new Map();   // "<livro>-<cap>" → { arquivo, dados }
function capitulo(id) {
  if (!caps.has(id)) {
    const m = id.match(/^(.+)-(\d+)$/);
    const f = m && path.join(RAIZ, 'conteudo', m[1], String(m[2]).padStart(3, '0') + '.json');
    caps.set(id, f && fs.existsSync(f) ? { arquivo: f, dados: JSON.parse(fs.readFileSync(f, 'utf8')) } : null);
  }
  return caps.get(id);
}

const aplicadas = [], cortes = [], avisos = [];
for (const r of respostas) {
  const [capId, tipo, trecho, temaId, itemId] = r.item.split(':');
  const c = capitulo(capId);
  const tema = c && c.dados.comentarios && c.dados.comentarios[trecho] && c.dados.comentarios[trecho].temas.find((t) => t.id === temaId);
  if (!tema) { avisos.push(`${r.item}: tema não encontrado`); continue; }
  const revisto = (campo) => { tema.revisto = [...new Set([...(tema.revisto || []), campo])]; };
  if (tipo === 'tt' || tipo === 'tr') {
    const campo = tipo === 'tt' ? 'titulo' : 'resumo';
    if (r.decisao === 'alterar' && r.texto) tema[campo] = r.texto.trim();
    else if (r.decisao !== 'aprovar') { avisos.push(`${r.item}: decisão inesperada (${r.decisao})`); continue; }
    revisto(campo);
  } else if (tipo === 'c') {
    const i = tema.itens.findIndex((x) => x.id === itemId);
    if (i < 0) { avisos.push(`${r.item}: comentário não encontrado`); continue; }
    const it = tema.itens[i];
    if (r.decisao === 'excluir') {
      tema.itens.splice(i, 1);
      if (!tema.itens.length) {
        const temas = c.dados.comentarios[trecho].temas;
        temas.splice(temas.indexOf(tema), 1);
        avisos.push(`${r.item}: era o último comentário; o tema «${tema.titulo}» saiu`);
      }
    } else if (r.decisao === 'alterar' && r.texto) {
      cortes.push({ item: r.item, autor: it.autor, antes: it.texto, depois: r.texto.trim(), explicacao: r.explicacao });
      it.texto = r.texto.trim();
      it.revisto = true;
    } else if (r.decisao === 'aprovar') it.revisto = true;
    else { avisos.push(`${r.item}: decisão inesperada (${r.decisao})`); continue; }
  } else { avisos.push(`${r.item}: item desconhecido`); continue; }
  aplicadas.push({ item: r.item, atualizado_em: r.atualizado_em });
}

const mudados = [];
for (const c of caps.values()) {
  if (!c) continue;
  fs.writeFileSync(c.arquivo, JSON.stringify(c.dados));
  mudados.push(c.arquivo);
}
if (mudados.length) execFileSync('python', [path.join(RAIZ, 'ferramentas', 'formato.py'), ...mudados], { stdio: 'inherit' });
fs.writeFileSync(arquivo.replace(/\.json$/, '') + '.aplicadas.json', JSON.stringify({ lidas: aplicadas }, null, 1));

console.log(`${aplicadas.length} de ${respostas.length} respostas aplicadas em ${mudados.length} capítulo(s)`);
for (const a of avisos) console.log(`AVISO ${a}`);
if (cortes.length) {
  console.log(`\n${cortes.length} corte(s) para conferir o sentido:`);
  for (const k of cortes) console.log(`\n## ${k.item} (${k.autor})${k.explicacao ? `\nExplicação: ${k.explicacao}` : ''}\nANTES: ${k.antes}\nDEPOIS: ${k.depois}`);
}
