"""Santo Ambrósio: Enarrationes in XII psalmos (PL 14, 921-1180) e Expositio in Psalmum CXVIII (PL 15, 1197-1526).

    python -I -X utf8 pesquisa/ferramentas/base/lat-ambrosio.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, textos 6956 (as doze: Sl 1, 35-40, 43, 45, 47, 48, 61 da Vulgata) e 6966 (o Sl 118,
em 22 sermões, um por letra do alfabeto hebraico; vai inteiro para o Sl 119 hebr.). Cache em
pesquisa/cache/base/cc_6956.txt e cc_6966.txt. Os salmos que ele não comentou vão para _ausentes.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG12 = dict(
    script='lat-ambrosio.py', idno=6956, pl=14,
    titulo='Santo Ambrósio, Enarrationes in XII psalmos', autor='Santo Ambrósio de Milão (c. 340–397)',
    obra='Enarrationes in XII psalmos Davidicos', arquivo='ambrosio-enarrationes-in-xii-psalmos.md',
    rotulo='Santo Ambrósio, Enarrationes in XII psalmos',
    motivo_ausente='não comentou este salmo (as Enarrationes tratam só dos Sl 1, 35–40, 43, 45, 47, 48 e 61 da Vulgata).',
    fim=lambda pars, tit: next((i for i, p in enumerate(pars) if i > tit[-1][0] and p['t'].startswith('Explicit Tomi')), len(pars)),
)
CFG118 = dict(
    script='lat-ambrosio.py', idno=6966, pl=15,
    titulo='Santo Ambrósio, Expositio in Psalmum CXVIII', autor='Santo Ambrósio de Milão (c. 340–397)',
    obra='Expositio in Psalmum David CXVIII', arquivo='ambrosio-expositio-in-psalmum-118.md',
    rotulo='Santo Ambrósio, Expositio in Psalmum CXVIII',
    sem_ausente=True,  # a ausência já consta da linha das Enarrationes
    extras_titulo=[(r'^PROLOGUS\.?$', 118)],
    nota='22 sermões, um por letra do alfabeto hebraico (Aleph...Tau); os números soltos são páginas da edição antiga.',
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG12, so)
    L.rodar_cc(CFG118, so)
