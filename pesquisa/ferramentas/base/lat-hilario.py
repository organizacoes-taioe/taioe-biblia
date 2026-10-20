"""Santo Hilário de Poitiers, Tractatus super Psalmos (PL 9, 231-908): só os salmos que ele comentou.

    python -I -X utf8 pesquisa/ferramentas/base/lat-hilario.py [--so 32 37 ...]   (números hebraicos)

Corpus Corporum, texto 21450 (cache em pesquisa/cache/base/cc_21450.txt). Comentou os Sl 1, 2, 9,
13, 14, 51-69, 91, 118 e 119-150 (Vulgata); o resto vai para _ausentes-latinos.md. Títulos
«PSALMUS N.» e, no Sl 118, «TRACT. PSALMI CXVIII». O «PROLOGUS IN CANTICA QUINDECIM GRADUUM»
(prólogo geral aos salmos graduais) fica no começo do Sl 119 (Vulgata) = Sl 120 hebr.
O prólogo geral da obra (antes do Sl 1) não entra em nenhum salmo.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

CFG = dict(
    script='lat-hilario.py', idno=21450, pl=9,
    titulo='Santo Hilário de Poitiers, Tractatus super Psalmos', autor='Santo Hilário de Poitiers (c. 315–367)',
    obra='Tractatus super Psalmos', arquivo='hilario-tractatus-super-psalmos.md',
    rotulo='Santo Hilário, Tractatus super Psalmos',
    extras_titulo=[(r'^(?:\[col\. \w+\] )?(?:\d+ )?PROLOGUS IN CANTICA QUINDECIM GRADUUM', 119)],
    nota='Hilário só comentou parte do Saltério (ver fontes/salmos.md). Os números soltos no texto são páginas da edição antiga.',
)

if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    L.rodar_cc(CFG, so)
