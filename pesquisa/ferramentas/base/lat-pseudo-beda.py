"""pseudo-Beda, De Psalmorum libro exegesis (PL 93, 477-1098): todos os salmos, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-pseudo-beda.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 8477 (cache em pesquisa/cache/base/cc_8477.txt). Títulos «IN PSALMUM N.»,
cada salmo com ARGUMENTUM, EXPLANATIO e COMMENTARIUM. O original traz «IN PSALMUM CXI» no lugar do XCI
(corrigido pelo script). Depois do Sl 150 vem um «ARGUMENTUM PSALMI» do salmo 151 (fora de numeração),
que fica de fora.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-pseudo-beda.py', idno=8477, pl=93,
    titulo='pseudo-Beda, De Psalmorum libro exegesis', autor='pseudo-Beda (autor incerto; compilação medieval)',
    obra='De Psalmorum libro exegesis', arquivo='pseudo-beda-de-psalmorum-libro.md',
    rotulo='pseudo-Beda, De Psalmorum libro exegesis',
    overrides={'IN PSALMUM CXI. Laus cantici in die Sabbati': 91},
    fim=lambda pars, tit: max(i for i, p in enumerate(pars) if p['t'].startswith('ARGUMENTUM PSALMI')),
    nota='Coleção de glosas (argumento, explanação, comentário) atribuída a Beda sem fundamento; citar como «pseudo-Beda».',
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
