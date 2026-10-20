"""São Bruno de Segni, Expositio in Pentateuchum: Expositio in Numeros (PL 164, 435-?), cortado por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/lat-bruno-num.py

Baixa UMA vez o texto 21403 do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.BruAst.ExInPe; o Pentateuco de Bruno
inteiro) e grava numeros/<ccc>/base/bruno-expositio-in-numeros.md. A obra tem 36 capítulos que acompanham os da Vulgata,
com estas diferenças: o cap. XVI (Nm 16) inclui os turíbulos batidos em lâminas (Vulg. 16,36-40 = NV 17,1-5) e o XVII é a vara
de Aarão; os caps. XXVI-XXVII tratam de Nm 27,22-23 (Josué sucede a Moisés; o XXVII só diz que a exposição falta); os
caps. XXXII, XXXIV e XXXVI só dizem «omittitur». Nm 26 não tem capítulo. Bruno resume e passa ao moral/alegórico;
«haec una sit omnium expositio» aparece várias vezes.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDNO = 21403
URL = 'https://mlat.uzh.ch/browser/cps_2.BruAst.ExInPe'
L = C.cc_linhas(IDNO)
a_num = next(i for i, l in enumerate(L) if 'INCIPIT EXPOSITIO IN NUMEROS' in l)
a_deu = next(i for i, l in enumerate(L) if 'INCIPIT EXPOSITIO IN DEUTERONOMIUM' in l)
ini = {}
for i in range(a_num, a_deu):
    m = re.match(r'^\s+CAPUT (PRIMUM|[IVXL]+)\.?\s*$', L[i])
    if m:
        ini[1 if m.group(1) == 'PRIMUM' else C.romano(m.group(1))] = i
ns = sorted(ini)
fim = {n: (ini[ns[k + 1]] if k + 1 < len(ns) else a_deu) for k, n in enumerate(ns)}

# Nm 17 (NV): do «Deinde praecepit Dominus ut Eleazar…» (cap. XVI) até o fim do cap. XVII
i17 = next(i for i in range(ini[16], fim[16]) if 'Deinde praecepit Dominus ut Eleazar' in L[i])

MAPA = {c: [c] for c in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 33, 35)}
MAPA[17] = ['16b', 17]
MAPA[27] = [26, 27]


def rom(n):
    r = ''
    for v, sy in ((50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += sy
            n -= v
    return r


n_arq = 0
for cap in C.CAPS:
    if cap not in MAPA:
        continue
    partes = []
    for co in MAPA[cap]:
        if co == '16b':
            a, b = i17, fim[16]
            partes.append(('XVI (a partir de «Deinde praecepit Dominus ut Eleazar»)', C.cortar(L, a, b)))
        else:
            partes.append((rom(co), C.cortar(L, ini[co], fim[co])))
    corpo = '\n\n'.join(f'**[Bruno de Segni, Expositio in Numeros, cap. {r}]**\n\n{t}' for r, t in partes)
    rots = '; '.join('cap. ' + r.split(' (')[0] for r, t in partes)
    campos = {
        'Autor': 'São Bruno de Segni (c. 1045–1123)',
        'Obra': 'Expositio in Pentateuchum: Expositio in Numeros',
        'Passagem': f'{C.cap_nm(cap)}; Bruno, Expositio in Numeros, {rots}',
        'Edição': C.edicao_pl(164, corpo),
        'Fonte': URL,
        'Cobre': 'o capítulo inteiro, resumido (Bruno cita o texto e comenta só o que serve à alegoria e à moral)',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-bruno-num.py',
    }
    nota = ('Os capítulos de Bruno acompanham os da Vulgata; a divisão desta obra está na Passagem. Bruno cita o lema entre «…» e comenta; '
            'onde lhe parece repetido, passa adiante. Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]» e as notas de Migne.')
    C.gravar(cap, 'bruno-expositio-in-numeros', 'São Bruno de Segni, Expositio in Numeros', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {len(corpo)//1024 or 1:3d} KB  {rots}')
print(n_arq, 'arquivos')
C.finalizar()
