"""Pedro Lombardo, Commentaria in Psalmos («Magna glosatura», PL 191, 55-1296): todos os salmos.

    python -I -X utf8 pesquisa/ferramentas/base/lat-lombardo.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 11455 (cache em pesquisa/cache/base/cc_11455.txt). Títulos «PSALMUS N.»
(duas linhas seguidas: o número e o «PSALMI TITULUS»). No fim de cada salmo a PL traz uma
«COLLATIO IN PSALMUM N» (variantes do hebraico e do grego, notas de editor do séc. XVI: Pratensis,
Munsterus etc.); fica no trecho, mas não é de Lombardo. As siglas [Aug.], [Cassiod.], [Hier.]... no
texto indicam a fonte de cada glosa.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-lombardo.py', idno=11455, pl=191,
    titulo='Pedro Lombardo, Commentaria in Psalmos', autor='Pedro Lombardo (c. 1100–1160)',
    obra='Commentaria in Psalmos (Magna glosatura)', arquivo='pedro-lombardo-commentaria-in-psalmos.md',
    rotulo='Pedro Lombardo, Commentaria in Psalmos',
    nota='No fim do trecho vem a «COLLATIO IN PSALMUM» do editor da PL (variantes hebraicas e gregas): não é de Lombardo.',
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
