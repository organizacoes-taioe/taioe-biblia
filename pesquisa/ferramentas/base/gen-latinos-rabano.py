"""Rábano Mauro, Commentaria in Genesim (4 livros), cortado por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-rabano.py 1        (ou 1-50)

Baixa uma vez o texto 8885 do Corpus Corporum (PL 107, 439–670; https://mlat.uzh.ch/browser/cps_2.RabMau.CoInGe3)
e grava genesis/<ccc>/base/rabano-in-genesim.md. Compilação (Beda, Agostinho, Jerônimo, Isidoro), quase nada
próprio; serve para conferir de quem é uma ideia. O capítulo sai do lema (gen-latinos-comum.py). Em Gn 1, o cap. X
do livro I («Allegorica expositio de sex dierum opere») vem depois de Gn 2,3 e fica em Gn 2.
"""
import importlib.util, os
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

caps = C.capitulos_args(__doc__)
C.por_lema(8885, r'INCIPIUNT COMMENTARIA IN GENESIM', None, caps, {
    'arquivo': 'rabano-in-genesim.md',
    'titulo': 'Rábano Mauro, Commentaria in Genesim',
    'autor': 'Rábano Mauro (c. 780–856)',
    'obra': 'Commentariorum in Genesim libri quatuor',
    'pl': 107, 'fonte': C.url_cc(8885), 'script': 'gen-latinos-rabano.py',
    'rotulo': 'Rábano Mauro, Commentaria in Genesim',
    'nota': 'Compilação; as fontes (Agostinho, Beda, Jerônimo, Isidoro) às vezes vêm nas notas de Migne.',
})
