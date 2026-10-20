"""Dídimo, o Cego: só PISTAS (o texto é edição moderna e não se guarda) para cada salmo.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-didimo-pistas.py
- Comentário do papiro de Tura (ed. Gronewald, PTA 4–8, 1968–70): cobre os Sl 20–44 da LXX, com lacunas; PDF do
  khazarzar «Didymus the Blind_PG 39/Commentarii in Psalmos.pdf».
- Fragmentos de cadeia (ed. Mühlenberg, PTA 15–16, 1975–78): marcadores «N Ps c,v» = fragmento N sobre o salmo c,
  versículo v (LXX); «Fragmenta in Psalmos.pdf» na mesma pasta. Os números dos fragmentos vêm do texto limpo.
Grava, em cache/base/grc/pistas/, o que grc-fechar.py junta em base/_pistas-gregos.md. Não grava textos em base/.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-didimo-pistas.py'
PASTA = 'Didymus the Blind_PG 39'
U_TURA = _grc.khz(PASTA, 'Commentarii in Psalmos.pdf')
U_FRAG = _grc.khz(PASTA, 'Fragmenta in Psalmos.pdf')
_grc.texto(U_TURA, 'didimo-tura')
f = _grc.texto(U_FRAG, 'didimo-frag')

frag = {}
for m in re.finditer(r'\b(\d{1,4}) Ps (\d{1,3}),(\d{1,3})', f):
    frag.setdefault(int(m.group(2)), []).append((int(m.group(1)), int(m.group(3))))

pistas = {}
for h in _grc.conjunto_hebr():
    linhas = []
    for n in _grc.lxx_de_hebr(h):
        if 20 <= n <= 44:
            linhas.append(f'- Dídimo, o Cego, Comentário aos Salmos (papiro de Tura; ed. Gronewald, PTA 4–8): cobre o Sl {n} da LXX '
                          f'(com lacunas); edição moderna, não guardada. {U_TURA}')
        if n in frag:
            ns = [a for a, _ in frag[n]]
            vs = sorted(set(b for _, b in frag[n]))
            linhas.append(f'- Dídimo, o Cego, fragmentos de cadeia sobre os Salmos (ed. Mühlenberg, PTA 15–16): frgs. '
                          f'{min(ns)}–{max(ns)} sobre o Sl {n} da LXX (vv. {vs[0]}–{vs[-1]}); edição moderna, não guardada. {U_FRAG}')
    if linhas:
        pistas[h] = linhas
_grc.registrar(SCRIPT, 'pistas', pistas)
print(f'{SCRIPT}: pistas para {len(pistas)} salmos hebraicos')
