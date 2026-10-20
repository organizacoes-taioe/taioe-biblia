"""Hesíquio de Jerusalém (PG 93) e Eutímio Zigabeno (PG 128): só PISTAS, porque o OCR do archive.org não serve para cortar.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-ia-pistas.py
- Hesíquio, «Fragmenta in Psalmos» (PG 93, 1179–1340; catena em grego com a tradução latina de Corderius em colunas
  intercaladas): o OCR mistura as duas colunas e o grego sai quebrado; não se guarda texto.
- Eutímio Zigabeno, «Commentarius in Psalterium» (PG 128, 41–1326): o latim sai legível, o grego sai com letras latinas
  («xai» por καὶ) e precisa ser refeito à mão; não se guarda texto. Cabeçalhos «PSALMUS <romano>.» (numeração da LXX).
Grava só as pistas (cache/base/grc/pistas/), que grc-fechar.py junta em base/_pistas-gregos.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-ia-pistas.py'
U93 = 'https://archive.org/details/patrologiaecursu93mignuoft'
U128 = 'https://archive.org/details/patrologiaecurs261unkngoog'


def romano(n):
    r = ''
    for v, s in ((100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += s
            n -= v
    return r


pistas = {}
for h in _grc.conjunto_hebr():
    ls = _grc.lxx_de_hebr(h)
    linhas = []
    for n in ls:
        linhas.append(f'- Hesíquio de Jerusalém, Fragmenta in Psalmos (PG 93, 1179–1340), «PSALMUS {romano(n)}» (Sl {n} da LXX): '
                      f'OCR do archive.org sem condições de corte (colunas grego/latim misturadas), não guardado. {U93}')
        linhas.append(f'- Eutímio Zigabeno, Commentarius in Psalterium (PG 128, 41–1326), «PSALMUS {romano(n)}» (Sl {n} da LXX): '
                      f'compila sobretudo Teodoreto; latim legível, grego do OCR quebrado (letras latinas), não guardado. {U128}')
    pistas[h] = linhas
_grc.registrar(SCRIPT, 'pistas', pistas)
print(f'{SCRIPT}: pistas para {len(pistas)} salmos hebraicos')
