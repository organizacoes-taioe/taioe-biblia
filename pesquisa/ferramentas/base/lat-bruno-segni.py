"""São Bruno de Segni, Expositio in Psalmos (PL 164, 695-1228): todos os salmos, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-bruno-segni.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 10806 (cache em pesquisa/cache/base/cc_10806.txt). Títulos «PSALMUS N.»
(às vezes com um número de página no meio: «PSALMUS V. 307 IN FINEM...»). O original repete «PSALMUS CXV»
no lugar do CXVI; lat_comum.achar_titulos conserta (repetição seguida de salto de dois).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-bruno-segni.py', idno=10806, pl=164,
    titulo='São Bruno de Segni, Expositio in Psalmos', autor='São Bruno de Segni (c. 1045–1123)',
    obra='Expositio in Psalmos', arquivo='bruno-segni-expositio-in-psalmos.md',
    rotulo='São Bruno de Segni, Expositio in Psalmos',
    nota='O Sl 116 (Vulgata) aparece no original com o título «PSALMUS CXV» repetido; o corte o conserta.',
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
