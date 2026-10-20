"""Arnóbio, o Jovem, Commentarii in Psalmos (PL 53, 327-570): todos os salmos, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-arnobio.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 21351 (cache em pesquisa/cache/base/cc_21351.txt). Títulos «PSALMUS N.»;
o Sl 118 vem em três partes («PSALMUS CXVIII (vers. 1-48)» etc.), reunidas num só trecho.
Cada salmo traz o texto bíblico e depois o «COMMENTARIUM».
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-arnobio.py', idno=21351, pl=53,
    titulo='Arnóbio, o Jovem, Commentarii in Psalmos', autor='Arnóbio, o Jovem (séc. V)',
    obra='Commentarii in Psalmos', arquivo='arnobio-commentarii-in-psalmos.md',
    rotulo='Arnóbio, o Jovem, Commentarii in Psalmos',
    nota='Semipelagiano (ver fontes/latinos.md): usar com cuidado.',
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
