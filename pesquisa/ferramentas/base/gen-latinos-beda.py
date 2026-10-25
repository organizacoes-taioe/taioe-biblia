"""São Beda, In principium Genesis (Hexaemeron), livros I–IV (Gn 1,1–21,10), cortado por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-beda.py 1        (ou 1-21, ou 2 3 4)

Baixa uma vez o texto 8466 do Corpus Corporum (PL 91, 9–190; https://mlat.uzh.ch/browser/cps_2.Beda.Hexaem2)
para pesquisa/cache/genesis/latinos/ e grava genesis/<ccc>/base/beda-in-principium-genesis.md. Beda vai lema a
lema; o capítulo de cada parágrafo sai do lema (comparado com a Nova Vulgata, gen-latinos-comum.py). O livro I acaba
em Gn 2,3 e traz no fim a leitura alegórica dos seis dias como as seis idades do mundo: ela fica em Gn 2 (vem depois
do lema de 2,3). A edição crítica (Jones, CCSL 118A, 1967) tem direitos: não guardar.
"""
import importlib.util, os
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

USO = __doc__
caps = C.capitulos_args(USO)
C.por_lema(8466, r'INCIPIT LIBER PRIMUS', None, caps, {
    'arquivo': 'beda-in-principium-genesis.md',
    'titulo': 'São Beda, In principium Genesis (Hexaemeron)',
    'autor': 'São Beda, o Venerável (c. 673–735)',
    'obra': 'In principium Genesis usque ad nativitatem Isaac (Hexaemeron), livros I–IV',
    'pl': 91, 'fonte': C.url_cc(8466), 'script': 'gen-latinos-beda.py',
    'rotulo': 'São Beda, In principium Genesis',
    'nota': 'Texto da PL (Giles); a edição crítica é a de Jones, CCSL 118A (1967), com direitos.',
})
