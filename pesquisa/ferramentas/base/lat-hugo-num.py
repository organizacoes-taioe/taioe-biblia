"""Hugo de São Vítor, Adnotationes in Pentateuchon: «Adnotatiunculae elucidatoriae in Numeros» (PL 175, 29-86).

    python -I -X utf8 pesquisa/ferramentas/base/lat-hugo-num.py

Baixa UMA vez o texto 11054 do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.HuDeSVi.AdInPe) e grava
numeros/<ccc>/base/hugo-adnotationes-in-pentateuchon.md para os capítulos de Números em que há nota: o trecho de
Números (CAP. XIV da obra) é curtíssimo: quatro notas, às marcas «NUM. XIV», «NUM. XVIII», «NUM. XXI», «NUM. XXIV»
de Migne. Para os capítulos pedidos só há Nm 18, 21 e 24 (a nota de Nm 14 fica fora do pedido).
O texto termina com «Et haec in Numeros. Reliqua enim desideramus.»
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDNO = 11054
URL = 'https://mlat.uzh.ch/browser/cps_2.HuDeSVi.AdInPe'
L = C.cc_linhas(IDNO)

a_num = next(i for i, l in enumerate(L) if re.match(r'^\s+CAP\. XIV\.-- Adnotatiunculae elucidatoriae in Numeros', l))
a_fim = next(i for i, l in enumerate(L) if 'Et haec in Numeros' in l) + 1


def marca(n):
    for i in range(a_num, a_fim):
        if re.match(r'^\[%d\]' % n, L[i]):
            return i
    raise KeyError(n)


# as notas de Migne dizem a que capítulo (Vulgata) cada trecho pertence
notas = dict((int(a), b) for a, b in re.findall(r'^\s+(\d+): \((NUM\. [IVXL]+)\.\)', '\n'.join(L[a_num:a_fim]), flags=re.M))
marcas = sorted(notas)
cap_de = {n: C.romano(notas[n].split()[1]) for n in marcas}

n_arq = 0
for k, n in enumerate(marcas):
    cap = cap_de[n]
    if cap not in C.CAPS:
        continue
    a = marca(n)
    b = marca(marcas[k + 1]) if k + 1 < len(marcas) else a_fim
    seg = C.cortar(L, a, b)
    campos = {
        'Autor': 'Hugo de São Vítor (1096–1141)',
        'Obra': 'Adnotationes in Pentateuchon (Adnotatiunculae elucidatoriae in Numeros)',
        'Passagem': f'{C.cap_nm(cap)}; capítulo XIV da obra, nota «{notas[n]}.» de Migne',
        'Edição': C.edicao_pl(175, seg),
        'Fonte': URL,
        'Cobre': 'só a nota deste capítulo (a obra tem quatro notas curtas sobre Números)',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-hugo-num.py',
    }
    nota = ('Hugo (ou um discípulo) deixou só notas literais, soltas, sobre Números (o texto acaba com «Reliqua enim desideramus»). '
            'A nota vem sem o lema bíblico; o capítulo é o indicado pela nota de Migne. '
            'Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]».')
    C.gravar(cap, 'hugo-adnotationes-in-pentateuchon', 'Hugo de São Vítor, Adnotationes in Pentateuchon', campos, seg, nota)
    n_arq += 1
    print(f'Nm {cap}: {len(seg)} bytes')
print(n_arq, 'arquivos')
C.finalizar()
