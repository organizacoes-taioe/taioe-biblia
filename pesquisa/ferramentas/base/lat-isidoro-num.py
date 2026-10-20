"""Santo Isidoro, Quaestiones in Vetus Testamentum, In Numeros (PL 83, 339-?), cortado por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/lat-isidoro-num.py

Baixa UMA vez o texto 21433 do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.IsiHis.QuInVeT) para
pesquisa/cache/base/numeros/cc_21433.txt e grava numeros/<ccc>/base/isidoro-quaestiones-in-numeros.md.

Como corta: o «In Numeros» de Isidoro é a Praefatio mais 42 capítulos, um por «mansão» de Nm 33 (Jerônimo, Ep. 78);
cada mansão traz, de passagem, os episódios de Números que aconteceram ali. O capítulo XII (Sinai) cobre Nm 1-10;
o XIII, Nm 11; o XV (Rethma), Nm 13-19; o XXXIII-XXXIV (Cades, Hor), Nm 20; XXXVI e XXXIX, Nm 21; o XLII (campos de
Moab), Nm 22-36. Para os demais capítulos de Números só há o nome da mansão. A tabela MAPA diz, parágrafo por parágrafo,
a que capítulos de Números (Nova Vulgata) cada trecho vai (alguns vão a mais de um). Nm 33 recebe a Praefatio e os 42
capítulos inteiros. Isidoro segue Jerônimo, Ep. 78 e Ambrósio; o pseudo-Beda, Rábano e a Glosa o copiam.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDNO = 21433
URL = 'https://mlat.uzh.ch/browser/cps_2.IsiHis.QuInVeT'
L = C.cc_linhas(IDNO)

# onde começa o «IN NUMEROS» e onde termina (começa o Deuteronômio)
a_num = next(i for i, l in enumerate(L) if re.match(r'^\s*(?:\d+\s+)?IN NUMEROS\.', l))
a_deu = next(i for i, l in enumerate(L) if re.match(r'^\s*IN DEUTERONOMIUM', l))

# capítulos (romanos) e parágrafos
cap_ini = {}  # n -> índice da linha do título
for i in range(a_num, a_deu):
    m = re.match(r'^\s+CAPUT ([IVXL]+)\.\s*(?:\d+: \(.*)?$', L[i])
    if m:
        cap_ini[C.romano(m.group(1))] = i
caps = sorted(cap_ini)
cap_fim = {n: (cap_ini[caps[k + 1]] if k + 1 < len(caps) else a_deu) for k, n in enumerate(caps)}


def paragrafos(n):
    """[(num, a, b)] — linhas de cada parágrafo «N. …» do capítulo n (o título vai junto com o §1)."""
    a, b = cap_ini[n], cap_fim[n]
    marcas = [(a, 0)]
    for i in range(a + 1, b):
        m = re.match(r'^(\d+)\. ', L[i])
        if m:
            marcas.append((i, int(m.group(1))))
    out = []
    for k, (i, p) in enumerate(marcas):
        j = marcas[k + 1][0] if k + 1 < len(marcas) else b
        if p == 0:
            continue
        ini = a if p == 1 else i  # o título do capítulo entra com o §1
        out.append((p, ini, j))
    return out


# MAPA: (capítulo de Isidoro, [parágrafos]) -> capítulos de Números (Nova Vulgata)
MAPA = [
    (12, [1], [1]),
    (12, [2], [1, 3, 7, 10]),
    (12, [3], [9]),
    (12, [4, 5, 6], [6]),
    (12, [7], [5]),
    (12, [8], [1]),
    (12, [9, 10], [4, 8]),
    (12, [11, 12], [8]),
    (12, [13, 14, 15], [10]),
    (13, [1, 2, 3], [11]),
    (15, [3, 4], [17]),
    (15, [16, 17, 18, 19], [17]),
    (15, list(range(20, 29)), [19]),
    (33, [1, 2, 3, 4, 5, 6], [20]),
    (34, [1], [20]),
    (34, [2], [21]),
    (36, [1, 2, 3, 4], [21]),
    (39, [1, 2, 3], [21]),
    (41, [1, 2], [27]),
    (42, [2, 3, 4, 5], [22]),
    (42, [2], [23, 24]),
    (42, [6, 7, 8], [25]),
    (42, [9, 10], [26]),
    (42, [11, 12], [27]),
    (42, [13], [28, 29]),
    (42, [14], [31]),
    (42, [15], [32]),
    (42, [16], [33]),
]

def rom(n):
    t = [(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    r = ''
    for v, sy in t:
        while n >= v:
            r += sy
            n -= v
    return r


por_cap = {c: [] for c in C.CAPS}
for cap_is, pars, nms in MAPA:
    tabela = {p: (a, b) for p, a, b in paragrafos(cap_is)}
    for nm in nms:
        por_cap[nm].append((cap_is, pars, [tabela[p] for p in pars]))


def montar(cap):
    partes, rotulos = [], []
    if cap in (1, 33):
        # Praefatio: antes do CAPUT I
        a = a_num
        b = cap_ini[1]
        partes.append(('Praefatio', C.cortar(L, a, b)))
        rotulos.append('Praefatio')
    if cap == 33:
        a, b = cap_ini[1], a_deu
        partes.append(('capítulos I–XLII (as 42 mansões)', C.cortar(L, a, b)))
        rotulos.append('caps. I–XLII (as 42 mansões, com os episódios de cada uma)')
        return partes, rotulos
    for cap_is, pars, spans in por_cap[cap]:
        a, b = spans[0][0], spans[-1][1]
        # parágrafos contíguos?
        txt = C.cortar(L, a, b)
        rot = f'cap. {rom(cap_is)}, §' + (f'{pars[0]}' if len(pars) == 1 else f'§{pars[0]}–{pars[-1]}')
        partes.append((rot, txt))
        rotulos.append(rot)
    return partes, rotulos


n = 0
for cap in C.CAPS:
    partes, rotulos = montar(cap)
    if not partes:
        continue
    corpo = '\n\n'.join(f'**[Isidoro, In Numeros, {r}]**\n\n{t}' for r, t in partes)
    campos = {
        'Autor': 'Santo Isidoro de Sevilha (c. 560–636)',
        'Obra': 'Quaestiones in Vetus Testamentum, In Numeros (também Mysticorum expositiones sacramentorum)',
        'Passagem': f'{C.cap_nm(cap)}; Isidoro, In Numeros: ' + '; '.join(rotulos),
        'Edição': C.edicao_pl(83, corpo),
        'Fonte': URL,
        'Cobre': ('o livro inteiro: Praefatio e as 42 mansões de Nm 33' if cap == 33 else
                  'só os trechos que tratam deste capítulo (o In Numeros de Isidoro é uma alegoria das 42 mansões; ver Nota)'),
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-isidoro-num.py',
    }
    nota = ('O «In Numeros» de Isidoro (PL 83, 339 ss.) não comenta Números versículo a versículo: segue as 42 mansões de Nm 33 '
            '(Jerônimo, Ep. 78), e em cada mansão resume o episódio que ali aconteceu. Os trechos abaixo são os parágrafos que tratam '
            'deste capítulo; os mesmos parágrafos aparecem em mais de um capítulo quando cobrem vários. '
            'Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]» e as notas de Migne («N: (Mt. I)»).')
    C.gravar(cap, 'isidoro-quaestiones-in-numeros', 'Santo Isidoro, Quaestiones in Vetus Testamentum, In Numeros', campos, corpo, nota)
    n += 1
    print(f'Nm {cap:2d}: {len(corpo)//1024 or 1} KB  {"; ".join(rotulos)[:110]}')
print(n, 'arquivos')
C.finalizar()
