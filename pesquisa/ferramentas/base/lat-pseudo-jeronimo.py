"""pseudo-Jerônimo, Breviarium in Psalmos (PL 26, 821-1270): todos os salmos, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-pseudo-jeronimo.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 7183 (cache em pesquisa/cache/base/cc_7183.txt). Títulos «PSALMUS N.» (o
Sl 106 vem como «PSALMUS. CVI.»). No fim da obra há uma «SECUNDA EXPOSITIO SUPER PSALMUM CXIX»
(Vulgata), anexada ao Sl 119 (Vulgata) = Sl 120 hebr. Citar como «autor antigo», não como Jerônimo.
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

RX_SEGUNDA = re.compile(r'^SECUNDA EXPOSITIO SUPER PSALMUM CXIX')


def _inicio_segunda(pars):
    return next(i for i, p in enumerate(pars) if RX_SEGUNDA.match(p['t']))


CFG = dict(
    script='lat-pseudo-jeronimo.py', idno=7183, pl=26,
    titulo='pseudo-Jerônimo, Breviarium in Psalmos', autor='pseudo-Jerônimo (autor incerto, séc. VII–VIII?)',
    obra='Breviarium in Psalmos', arquivo='pseudo-jeronimo-breviarium-in-psalmos.md',
    rotulo='pseudo-Jerônimo, Breviarium in Psalmos',
    fim=lambda pars, tit: _inicio_segunda(pars),
    extras_secao=lambda pars, tit: [(_inicio_segunda(pars), len(pars), 119,
                                     'Secunda expositio super psalmum CXIX (anexada ao fim da obra)')],
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
