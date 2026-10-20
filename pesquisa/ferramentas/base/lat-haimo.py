"""«Haimo de Halberstadt», Commentaria in Psalmos (PL 116, 193-696): todos os salmos, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-haimo.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 9073 (cache em pesquisa/cache/base/cc_9073.txt). Títulos «IN PSALMUM N.»
(o Sl 1 é «IN PRIMUM PSALMUM»). Atribuição incerta (talvez Haimo de Auxerre ou Remígio): citar como «Haimo (?)».
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-haimo.py', idno=9073, pl=116,
    titulo='«Haimo de Halberstadt», Commentaria in Psalmos', autor='«Haimo de Halberstadt» (séc. IX; autoria incerta)',
    obra='Commentaria in Psalmos', arquivo='haimo-commentaria-in-psalmos.md',
    rotulo='«Haimo de Halberstadt», Commentaria in Psalmos',
    extras_titulo=[(r'^(?:\[col\. \w+\] )?IN PRIMUM PSALMUM\b', 1)],
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
