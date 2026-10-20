"""Ruperto de Deutz, De Trinitate et operibus eius: In Numeros, livros I e II (PL 167, 835-?), cortado por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/lat-ruperto-num.py

Baixa UMA vez o texto 10873 do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.RupTui.DeTrEtO; 5,6 MB, a Bíblia
inteira de Ruperto) e grava numeros/<ccc>/base/ruperto-in-numeros.md. O In Numeros tem 40 capítulos no livro I (Nm 1-14)
e 32 no livro II (Nm 15-36); cada capítulo traz um título que diz o versículo comentado. A tabela MAPA1/MAPA2 dá o
capítulo de Números (Nova Vulgata) de cada capítulo de Ruperto. O cap. XXXII do livro II, «Brevis narratio» do que
aconteceu na última mansão, resume Nm 24-36 (com notas de Migne «Num. XXV», «Num. XXVI»…): entra nos capítulos de Números
sobre os quais Ruperto não tem capítulo próprio (27, 28, 29, 31, 32, 34, 35, 36) e em Nm 33.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDNO = 10873
URL = 'https://mlat.uzh.ch/browser/cps_2.RupTui.DeTrEtO'
L = C.cc_linhas(IDNO)
a_num = next(i for i, l in enumerate(L) if re.match(r'^\s+IN NUMEROS COMMENTARIORUM', l))
a_l2 = next(i for i, l in enumerate(L) if i > a_num and re.match(r'^\s+IN NUMEROS LIBER SECUNDUS', l))
a_deu = next(i for i, l in enumerate(L) if i > a_l2 and re.match(r'^\s+IN DEUTERONOMIUM\s*$', l))


def caps_de(a, b):
    ini = {}
    for i in range(a, b):
        m = re.match(r'^\s+(?:IN NUMEROS LIBER SECUNDUS\.\S*\s+)?CAPUT (PRIMUM|[IVXL]+)\b', L[i])
        if m:
            ini[1 if m.group(1) == 'PRIMUM' else C.romano(m.group(1))] = i
    return ini


# o título do cap. I do livro II vem depois de «IN NUMEROS LIBER SECUNDUS.[2640]» numa linha; ajusta
ini1 = caps_de(a_num, a_l2)
ini2 = caps_de(a_l2, a_deu)
ns1, ns2 = sorted(ini1), sorted(ini2)
fim1 = {n: (ini1[ns1[k + 1]] if k + 1 < len(ns1) else a_l2) for k, n in enumerate(ns1)}
fim2 = {n: (ini2[ns2[k + 1]] if k + 1 < len(ns2) else a_deu) for k, n in enumerate(ns2)}

MAPA1 = {1: [1], 2: [1], 3: [2], 4: [1], 5: [3], 6: [3], 7: [4], 8: [4], 9: [5], 10: [5],
         11: [6], 12: [6], 13: [6], 14: [6], 15: [6], 16: [6], 17: [7], 18: [7], 19: [7],
         20: [8], 21: [8], 22: [8], 23: [9], 24: [9], 25: [10], 26: [10], 27: [10], 28: [10], 29: [10],
         30: [11], 31: [11], 32: [11]}
MAPA2 = {4: [17], 5: [18], 6: [19], 7: [20], 8: [20], 9: [20], 10: [21], 11: [21], 12: [21], 13: [21], 14: [21], 15: [21],
         16: [22], 17: [22], 18: [23], 19: [23], 20: [23], 21: [24], 22: [24], 23: [24], 24: [24], 25: [24],
         26: [25], 27: [25], 28: [25], 29: [26], 30: [30], 31: [33], 32: [27, 28, 29, 31, 32, 33, 34, 35, 36]}

por = {c: [] for c in C.CAPS}
for n, nms in MAPA1.items():
    for nm in nms:
        por[nm].append((1, n))
for n, nms in MAPA2.items():
    for nm in nms:
        por[nm].append((2, n))


def rom(n):
    r = ''
    for v, sy in ((40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += sy
            n -= v
    return r


def trecho(liv, n):
    ini, fim = (ini1, fim1) if liv == 1 else (ini2, fim2)
    a = ini[n]
    # título do cap. I do livro II: a linha do LIBER SECUNDUS não faz parte do capítulo anterior
    return C.cortar(L, a, fim[n])


def titulo(liv, n):
    ini = ini1 if liv == 1 else ini2
    t = ' '.join(x.strip() for x in L[ini[n]:ini[n] + 3] if x.strip() and not x.strip().startswith(('---', '___')))
    t = re.sub(r'^.*?CAPUT (PRIMUM|[IVXL]+)\.?\s*(\d+\s+)?', '', t)
    t = re.sub(r'\[\d+\].*$', '', t)
    return t.strip()


n_arq = 0
for cap in C.CAPS:
    if not por[cap]:
        continue
    partes = [(liv, n, trecho(liv, n)) for liv, n in por[cap]]
    corpo = '\n\n'.join(f'**[Ruperto, In Numeros, livro {"I" if liv == 1 else "II"}, cap. {rom(n)}: {titulo(liv, n)[:90].rstrip(" .,")}]**\n\n{t}' for liv, n, t in partes)
    rots = []
    for liv in (1, 2):
        ns = [n for l, n, t in partes if l == liv]
        if ns:
            rots.append(f'livro {"I" if liv == 1 else "II"}, ' + ('cap. ' if len(ns) == 1 else 'caps. ') + (rom(ns[0]) if len(ns) == 1 else f'{rom(ns[0])}–{rom(ns[-1])}'))
    rots = '; '.join(rots)
    resumo = cap in (27, 28, 29, 31, 32, 34, 35, 36)
    campos = {
        'Autor': 'Ruperto de Deutz (c. 1075–1129)',
        'Obra': 'De Trinitate et operibus eius: In Numeros (livros I e II)',
        'Passagem': f'{C.cap_nm(cap)}; Ruperto, In Numeros, {rots}',
        'Edição': C.edicao_pl(167, corpo),
        'Fonte': URL,
        'Cobre': ('só o resumo final do livro II (cap. XXXII, «Brevis narratio»): Ruperto não tem capítulo próprio sobre este capítulo de Números'
                  if resumo else 'a lista das 42 mansões (cap. XXXI) e o resumo final (cap. XXXII)' if cap == 33
                  else 'o capítulo inteiro, versículo a versículo'),
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-ruperto-num.py',
    }
    nota = ('Comentário contínuo de Ruperto: sentido literal e depois alegórico, com títulos de capítulo que dizem o versículo. '
            'As chamadas «[N]» remetem às notas de Migne (referência bíblica), no rodapé de cada coluna. '
            'Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]».')
    C.gravar(cap, 'ruperto-in-numeros', 'Ruperto de Deutz, De Trinitate et operibus eius: In Numeros', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {len(corpo)//1024 or 1:3d} KB  {rots[:120]}')
print(n_arq, 'arquivos')
C.finalizar()
