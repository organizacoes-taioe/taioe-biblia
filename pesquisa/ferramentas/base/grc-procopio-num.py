"""Procópio de Gaza, Commentarii in Octateuchum: Commentarii in Numeros (PG 87/1, 793-897), por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/grc-procopio-num.py

Baixa UMA vez o OCR do archive.org «patrologiaecurs267unkngoog» (Patrologiae cursus completus, t. 87; texto em
https://archive.org/download/patrologiaecurs267unkngoog/patrologiaecurs267unkngoog_djvu.txt) e grava
numeros/<ccc>/base/procopio-commentarii-in-numeros.md.

Como é: o comentário de Procópio é uma catena (Cirilo, Teodoreto, Orígenes, Nissa…) que a PG imprime com o latim de Clauser e, em
alguns trechos, os escólios gregos em duas colunas; o OCR intercala as linhas dos dois idiomas (o latim sai bem; o grego, mal, com acentos
trocados). Não há título de capítulo nem número de versículo: o texto de Números vai das linhas ~47340 a ~52874 do OCR e é cortado em blocos
em unidades de ~1500 caracteres (as colunas do OCR são curtas). O script dá a cada unidade o capítulo de Números (Nova Vulgata) que mais bate com as
palavras-chave (nomes e termos do episódio) mantendo a ordem do livro (programação dinâmica: o capítulo nunca recua). Resultado aproximado:
as fronteiras podem errar por um bloco (~2 colunas). As colunas da PG saem dos números dos cabeçalhos, interpolados.
Para o grego dos escólios, ver o OCR «patrologiae_cursus_completus_gr_vol_087_1», que lê melhor o grego.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

URL = 'https://archive.org/details/patrologiaecurs267unkngoog'
OCR = 'https://archive.org/download/patrologiaecurs267unkngoog/patrologiaecurs267unkngoog_djvu.txt'
p = C.baixar(OCR, 'proc_lat_djvu.txt', minimo=100000)
L = C.ler(p).split('\n')

HEAD = re.compile(r'COMMENTAR\S*\s+IN\s+N\S*ROS', re.I)
a0 = next(i for i in range(47000, 48000) if HEAD.search(L[i]))
a1 = next(i for i in range(a0, len(L)) if re.search(r'^\s*IN DEUTERONOMIUM\.?\s*$', L[i]))
cab = [i for i in range(a0, a1) if HEAD.search(L[i])]
# unidades de ~1500 caracteres, cortadas em linhas em branco (o OCR intercala grego e latim em colunas: unidades menores seriam fragmentos)
blocos, ini, acum = [], a0, 0
for i in range(a0, a1):
    acum += len(L[i]) + 1
    if acum >= 1500 and not L[i].strip():
        blocos.append((ini, i + 1))
        ini, acum = i + 1, 0
if ini < a1:
    blocos.append((ini, a1))

# capítulo de cada unidade: palavras-chave + programação dinâmica (_numeros_comum.atribuir_dp)
nB = len(blocos)
cap_de = C.atribuir_dp(['\n'.join(L[a:b]) for a, b in blocos], primeiro=1)

# âncoras de coluna
anc = []
for i in cab:
    nums = [int(x) for x in re.findall(r'\b(\d{3})\b', L[i]) if 790 <= int(x) <= 900]
    if nums:
        anc.append((i, max(nums)))
def linear(linha):
    return 793 + (linha - a0) / (a1 - a0) * (897 - 793)


mono = []
ult = 0
for i, n in anc:
    if n >= ult and abs(n - linear(i)) <= 8:  # descarta números mal lidos pelo OCR
        mono.append((i, n))
        ult = n
anc = [(a0, 793)] + mono + [(a1, 897)]


def col(linha):
    for (i0, n0), (i1, n1) in zip(anc, anc[1:]):
        if i0 <= linha <= i1 and i1 > i0:
            return n0 + (n1 - n0) * (linha - i0) / (i1 - i0)
    return linear(linha)


por = {}
for (a, b), cap in zip(blocos, cap_de):
    por.setdefault(cap, []).append((a, b))

n_arq = 0
for cap in C.CAPS:
    if cap not in por:
        continue
    trechos = por[cap]
    a, b = trechos[0][0], trechos[-1][1]
    txt = '\n'.join(L[a:b]).strip()
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    campos = {
        'Autor': 'Procópio de Gaza (c. 465–528)',
        'Obra': 'Commentarii in Octateuchum: Commentarii in Numeros',
        'Passagem': f'{C.cap_nm(cap)}; {len(trechos)} unidade(s) de ~1500 caracteres do OCR (atribuição aproximada, ver Nota)',
        'Edição': f'PG 87/1, c. ~{int(col(a))}–{int(col(b))} (estimadas; o comentário a Números ocupa c. 793–897)',
        'Fonte': URL,
        'Cobre': 'as unidades de texto atribuídas a este capítulo; pode faltar ou sobrar meia página nas pontas',
        'Oriental': 'sim',
        'Língua': 'grc',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/grc-procopio-num.py',
    }
    nota = ('OCR do archive.org (' + OCR + '): grego (escólios) e latim (Clauser) intercalados linha a linha; o latim sai legível, o grego com acentos '
            'trocados e letras latinas. Procópio é catena: copia Cirilo (Glaphyra), Teodoreto, Orígenes e Nissa: citar o autor original quando for o mesmo trecho. '
            'A divisão por capítulo é heurística (palavras-chave por unidade de ~1500 caracteres, em ordem); conferir os limites nas imagens do archive.org. '
            'Para ler o grego, comparar com o OCR «patrologiae_cursus_completus_gr_vol_087_1». As edições do latim: Clauser (1555).')
    C.gravar(cap, 'procopio-commentarii-in-numeros', 'Procópio de Gaza, Commentarii in Numeros', campos, txt, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {len(trechos)} unid., linhas {a}-{b}, c. ~{int(col(a))}–{int(col(b))}, {len(txt)//1024} KB')
print(n_arq, 'arquivos;', 'blocos:', nB)
print('capítulos sem bloco:', [c for c in C.CAPS if c not in por])
C.finalizar()
