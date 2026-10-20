"""Cassiodoro, Expositio Psalmorum (PL 70, 9-1056): todos os salmos, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-cassiodoro.py [--so 32 37 ...]   (números hebraicos)

Baixa UMA vez o texto do Corpus Corporum (idno 21404) para pesquisa/cache/base/cc_21404.txt e corta
por salmo (numeração da Vulgata -> hebraica pela tabela de lat_comum.py). Grava
salmos/<ccc>/base/cassiodoro-expositio-psalmorum.md. Os títulos são «EXPOSITIO IN PSALMUM N.»;
os Sl 51 e 101 vêm como «TITULUS PSALMI N» (depois de «PARS SECUNDA/TERTIA», que se descarta) e o
Sl 71 começa em «EXPOSITIO IN OCTO DECADAS...» (com um prefácio às oito décadas, que fica no Sl 71).
O trecho do Sl 150 acaba antes da «ORATIO» final de toda a obra.
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-cassiodoro.py', idno=21404, pl=70,
    titulo='Cassiodoro, Expositio Psalmorum', autor='Cassiodoro (c. 485–c. 580)',
    obra='Expositio Psalmorum (Expositio in Psalterium)', arquivo='cassiodoro-expositio-psalmorum.md',
    rotulo='Cassiodoro, Expositio Psalmorum',
    extras_titulo=[(r'^(?:\[col\. \w+\] )?(?:\d+ )?TITULUS PSALMI ([IVXLC]+)\b', None),
                   (r'^(?:\[col\. \w+\] )?(?:\d+ )?EXPOSITIO IN OCTO DECADAS', 71)],
    aparar=r'^(?:\[col\. \w+\] )?(?:\d+ )?PARS (SECUNDA|TERTIA)\.?$',
    fim=lambda pars, tit: next(i for i, p in enumerate(pars) if i > tit[-1][0] and re.match(r'^ORATIO\.?$', p['t'])),
    nota='Texto da PL (Migne, reproduz Garet, 1679); os números soltos no texto (ex.: «107») são as páginas da edição de Garet.',
)

if __name__ == '__main__':
    so = None
    if '--so' in sys.argv:
        so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]}
    L.rodar_cc(CFG, so)
