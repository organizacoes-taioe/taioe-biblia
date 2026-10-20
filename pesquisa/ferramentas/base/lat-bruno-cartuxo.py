"""São Bruno, o Cartuxo, Expositio in Psalmos (PL 152, 637-1420): todos os salmos, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-bruno-cartuxo.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 10473 (cache em pesquisa/cache/base/cc_10473.txt). Títulos «IN PSALMUM N.»;
o Sl 150 acaba antes da linha final do editor («Finis tomi primi Operum...»).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-bruno-cartuxo.py', idno=10473, pl=152,
    titulo='São Bruno, o Cartuxo, Expositio in Psalmos', autor='São Bruno, o Cartuxo (c. 1030–1101)',
    obra='Expositio in Psalmos', arquivo='bruno-cartuxo-expositio-in-psalmos.md',
    rotulo='São Bruno, o Cartuxo, Expositio in Psalmos',
    fim=lambda pars, tit: next((i for i, p in enumerate(pars) if i > tit[-1][0] and 'Finis tomi primi' in p['t']), len(pars)),
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
