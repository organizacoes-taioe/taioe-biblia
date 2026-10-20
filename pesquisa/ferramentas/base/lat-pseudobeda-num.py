"""pseudo-Beda, Quaestiones super Numeros (PL 93, 395-410), cortado por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/lat-pseudobeda-num.py

Baixa UMA vez o texto 8484 do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.AuInBe.QuSuNu) e grava
numeros/<ccc>/base/pseudobeda-quaestiones-super-numeros.md. A obra é um diálogo (Discipulus/Magister) em 29 capítulos
curtos que copiam as 42 mansões de Isidoro (In Numeros) com títulos por episódio; a tabela MAPA diz a que capítulo(s)
de Números (Nova Vulgata) cada capítulo da obra vai. Nm 33 recebe os caps. I (catálogo das mansões), XXI e XXIX.
Beda autêntico não comentou Números; a atribuição é falsa (PL 93 traz o texto entre os espúrios).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDNO = 8484
URL = 'https://mlat.uzh.ch/browser/cps_2.AuInBe.QuSuNu'
L = C.cc_linhas(IDNO)

ini = {}
for i, l in enumerate(L):
    m = re.match(r'^\s+CAPUT ([IVXL]+|PRIMUM)\b', l)
    if m:
        ini[1 if m.group(1) == 'PRIMUM' else C.romano(m.group(1))] = i
ns = sorted(ini)
fim = {n: (ini[ns[k + 1]] if k + 1 < len(ns) else len(L)) for k, n in enumerate(ns)}

MAPA = {  # capítulo da obra -> capítulos de Números (NV)
    1: [33], 2: [9], 3: [6], 4: [5], 5: [1], 6: [4, 8], 7: [10], 8: [11], 9: [11], 11: [17],
    14: [17], 15: [17], 16: [19], 17: [20], 18: [20], 19: [20, 21], 20: [21], 21: [33],
    22: [22, 23, 24], 23: [25], 24: [26], 25: [27], 26: [28, 29], 27: [31], 28: [32], 29: [33],
}
# (10 = Nm 12; 11 = Nm 13-19 em resumo, 12 = Nm 15, 13 = Nm 16: fora dos capítulos pedidos, exceto o resumo do 11 em Nm 17)


def rom(n):
    t = [(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    r = ''
    for v, sy in ((20, 'XX'), *t):
        while n >= v:
            r += sy
            n -= v
    return r


por = {c: [] for c in C.CAPS}
for cap_o, nms in MAPA.items():
    for nm in nms:
        por[nm].append(cap_o)

TIT = {n: re.sub(r'^\s+CAPUT (?:[IVXL]+|PRIMUM)\.?\s*', '', L[i]).strip() for n, i in ini.items()}
n_arq = 0
for cap in C.CAPS:
    if not por[cap]:
        continue
    partes = []
    for co in sorted(por[cap]):
        partes.append((co, C.cortar(L, ini[co], fim[co])))
    corpo = '\n\n'.join(f'**[pseudo-Beda, Quaestiones super Numeros, cap. {rom(co)}]**\n\n{t}' for co, t in partes)
    rots = '; '.join(f'cap. {rom(co)} ({TIT[co].rstrip(".")})' for co, _ in partes)
    campos = {
        'Autor': 'pseudo-Beda (autor medieval incerto; atribuído a Beda, 672–735)',
        'Obra': 'Quaestiones super Numeros',
        'Passagem': f'{C.cap_nm(cap)}; pseudo-Beda: {rots}',
        'Edição': C.edicao_pl(93, corpo),
        'Fonte': URL,
        'Cobre': 'os capítulos da obra que tratam do episódio (resumo curto, copiado de Isidoro)',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-pseudobeda-num.py',
    }
    nota = ('Obra espúria (PL 93), em forma de diálogo Discipulus/Magister, que copia as «Quaestiones in Numeros» de Isidoro. '
            'Útil só para ver como a tradição resumiu cada episódio. Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]» '
            'e as notas de Migne.')
    C.gravar(cap, 'pseudobeda-quaestiones-super-numeros', 'pseudo-Beda, Quaestiones super Numeros', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {len(corpo)//1024 or 1} KB  {rots[:100]}')
print(n_arq, 'arquivos')
C.finalizar()
