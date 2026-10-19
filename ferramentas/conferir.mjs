// Confere os capítulos de conteudo/ antes do commit (e no CI):
//   node ferramentas/conferir.mjs
// - nenhuma mesóclise, nenhum pronome contraído, nada de uso europeu (texto, notas, comentários);
// - versículos em ordem, sem lacuna nem duplicata; nenhum `np` logo depois de subtítulo;
// - notas com âncora que existe no versículo; ids únicos e no formato da revisão;
// - comentários com autor, obra, passagem, texto e link https; tema com id, título e itens.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const C = path.join(RAIZ, 'conteudo');
const erros = [];
const erro = (onde, msg) => erros.push(`${onde}: ${msg}`);

// Sem \b no fim: depois de vogal acentuada ele falha (regra geral do Gere).
const MESOCLISE = /[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)/;
const EUROPEU = [/\bfacto\b/i, /\bregist(ar|ou|ei|o)\b/i, /\bGénesis\b/, /\bcrónica/i, /\b(está|estão|estava|estavam|estou|estar) a [a-zà-ÿ]+(ar|er|ir)\b/i, /\bnoutr[oa]s?\b/i, /\bnalgu(m|ma|ns|mas)\b/i, /\bmais pequen[oa]s?\b/i, /\bpormenor/i, /\bconnosco\b/i, /\bactual/i, /\bóptim/i];

function texto(onde, s) {
  if (typeof s !== 'string') return;
  if (MESOCLISE.test(s)) erro(onde, `mesóclise: «${s.match(MESOCLISE)[0]}»`);
  // «mas» e «ta(s)» só valem como pronome depois de hífen; isolados são conjunção, etc.
  const m = s.match(/-(mo|ma|mos|mas|to|ta|tos|tas|lho|lha|lhos|lhas)([^A-Za-zÀ-ÿ]|$)/);
  if (m) erro(onde, `pronome contraído: «${m[0]}»`);
  for (const r of EUROPEU) if (r.test(s)) erro(onde, `uso europeu: «${s.match(r)[0]}»`);
}

const ID = /^[a-z0-9][a-z0-9._-]{0,60}$/;
const livros = JSON.parse(fs.readFileSync(path.join(C, 'livros.json'), 'utf8'));
let ncaps = 0;
for (const l of livros) {
  const dir = path.join(C, l.id);
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json')).sort()) {
    ncaps++;
    const onde = `${l.id}/${f}`;
    let c;
    try { c = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')); } catch (e) { erro(onde, `JSON inválido: ${e.message}`); continue; }
    // versículos
    let ant = 0, depoisDeSub = false;
    const vistos = new Set();
    for (const v of c.texto) {
      if (v.s) { texto(`${onde} subtítulo`, v.s); depoisDeSub = true; continue; }
      const n = parseInt(v.v, 10);
      if (vistos.has(String(v.v))) erro(onde, `v. ${v.v} duplicado`);
      vistos.add(String(v.v));
      if (Number.isInteger(n) && n !== ant + 1 && String(n) === String(v.v)) erro(onde, `depois do v. ${ant} vem o v. ${n}`);
      if (Number.isInteger(n)) ant = n;
      if (depoisDeSub && v.np) erro(onde, `v. ${v.v}: np logo depois de subtítulo`);
      depoisDeSub = false;
      (v.l || [v.t]).forEach((s) => texto(`${onde} v. ${v.v}`, s));
    }
    // notas
    const ids = new Set();
    for (const n of c.notas || []) {
      if (!ID.test(n.id) || ids.has(n.id)) erro(onde, `nota com id ruim ou repetido: ${n.id}`);
      ids.add(n.id);
      const v = c.texto.find((x) => String(x.v) === String(n.v));
      if (!v) { erro(onde, `nota ${n.id}: v. ${n.v} não existe`); continue; }
      if (n.apos && !(v.l || [v.t]).some((s) => s.includes(n.apos))) erro(onde, `nota ${n.id}: «${n.apos}» não está no v. ${n.v}`);
      texto(`${onde} nota ${n.id}`, n.texto);
    }
    // comentários
    for (const [tid, com] of Object.entries(c.comentarios || {})) {
      if (!c.trechos.some((t) => t.id === tid)) erro(onde, `comentários de um trecho que não existe: ${tid}`);
      const temas = new Set(), itens = new Set();
      texto(`${onde} intro dos comentários`, com.intro);
      for (const t of com.temas || []) {
        if (!ID.test(t.id) || temas.has(t.id)) erro(onde, `tema com id ruim ou repetido: ${t.id}`);
        temas.add(t.id);
        if (!t.titulo || !t.itens || !t.itens.length) erro(onde, `tema ${t.id} sem título ou sem comentários`);
        texto(`${onde} tema ${t.id}`, t.titulo); texto(`${onde} tema ${t.id}`, t.resumo);
        for (const it of t.itens || []) {
          if (!ID.test(it.id) || itens.has(it.id)) erro(onde, `comentário com id ruim ou repetido: ${it.id}`);
          itens.add(it.id);
          for (const k of ['autor', 'obra', 'passagem', 'texto']) if (!it[k]) erro(onde, `comentário ${it.id} sem ${k}`);
          if (!/^https:\/\//.test(it.link || '')) erro(onde, `comentário ${it.id} sem link https`);
          texto(`${onde} comentário ${it.id}`, it.texto);
          if (it.aviso_corte) {
            const a = it.aviso_corte;
            if (!Number.isInteger(a.n) || a.n < 1 || !a.corte || !a.aviso) erro(onde, `comentário ${it.id}: aviso_corte precisa de n, corte e aviso`);
            texto(`${onde} aviso de corte ${it.id}`, a.aviso);
          }
        }
      }
    }
    // revisão
    for (const e of (c.revisao && c.revisao.escolhas) || []) {
      if (!ID.test(e.id)) erro(onde, `escolha com id ruim: ${e.id}`);
      if (!e.opcoes || e.opcoes.filter((o) => o.recomendada).length !== 1) erro(onde, `escolha ${e.id}: tem de ter exatamente uma opção recomendada`);
    }
  }
}
if (erros.length) { console.error(erros.join('\n')); console.error(`${erros.length} problema(s)`); process.exit(1); }
console.log(`ok: ${ncaps} capítulo(s) conferido(s)`);
