"""Santo Agostinho, Quaestiones in Heptateuchum IV (Números) e Locutiones in Heptateuchum IV (PL 34), por capítulo.

    python -I -X utf8 pesquisa/ferramentas/base/lat-agostinho-num.py

Baixa UMA vez os textos 7312 (Quaestiones) e 7311 (Locutiones) do Corpus Corporum
(https://mlat.uzh.ch/browser/cps_2.AugHip.QuInHe e https://mlat.uzh.ch/browser/cps_2.AugHip.LoInHe) e grava, em
numeros/<ccc>/base/, agostinho-quaestiones-in-heptateuchum-4.md e agostinho-locutiones-in-heptateuchum-4.md.

Por que o Corpus Corporum e não o augustinus.it: o texto é o mesmo dos Maurinos, mas o augustinus.it (fora do ar em 20/10/2026,
HTTP 503; há cópia no Wayback Machine) troca as palavras gregas por imagens, e o Corpus traz as colunas da PL.
Como corta: cada questão (65 no livro IV) começa com «[Num. cap. I, v. 1-44.]» ou «[Ib. XII, 1.]»: referência da Vulgata
(capítulo em algarismo romano, versículos). O capítulo vale o da Nova Vulgata, exceto Vulg. 16,36-50 = NV 17,1-15 e Vulg. 17
= NV 17,16-28 (a q. 30, «XVI, 36-40», os turíbulos, vai para Nm 17). Nas Locutiones, uma entrada «[Ib. 9.]» sem capítulo
continua no último capítulo citado.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDQ, IDL = 7312, 7311
URLQ = 'https://mlat.uzh.ch/browser/cps_2.AugHip.QuInHe'
URLL = 'https://mlat.uzh.ch/browser/cps_2.AugHip.LoInHe'
REF = re.compile(r'\[(?:Num\. cap\. |Ib\. )?(?:([IVXLC]+)[,.]\s*(?:V\\\s*)?)?(\d+)')


def nv(cap_vulg, verso):
    if cap_vulg == 16 and verso is not None and verso >= 36:
        return 17
    return cap_vulg


def quest():
    L = C.cc_linhas(IDQ)
    a0 = next(i for i, l in enumerate(L) if re.match(r'^\s+LIBER QUARTUS\. Quaestiones in Numeros', l))
    a1 = next(i for i, l in enumerate(L) if i > a0 and re.match(r'^\s+LIBER QUINTUS\.', l))
    ini = []
    for i in range(a0, a1):
        m = re.search(r'\[(?:Num\. cap\. |Ib\. )?([IVXLC]+)[,.]\s*([^\]]*)\]', L[i])
        if m and (re.match(r'^\s+\[', L[i]) or 'QUAEST.' in L[i]):
            c = i
            for j in range(i - 1, i - 4, -1):
                if re.match(r'^\s+[IVXLC]+\.\s*$', L[j]):
                    c = j
                    break
            v = re.match(r'\s*(\d+)', m.group(2).replace('V\\', ''))
            ini.append((c, C.romano(m.group(1)), int(v.group(1)) if v else None, m.group(1) + ', ' + m.group(2).strip()))
    por = {c: [] for c in C.CAPS}
    fins = [x[0] for x in ini[1:]] + [a1]
    for k, ((c, cv, v, ref), fim) in enumerate(zip(ini, fins), start=1):
        n = nv(cv, v)
        if n in por:
            por[n].append((k, ref, C.cortar(L, c, fim)))
    return por


def locut():
    L = C.cc_linhas(IDL)
    a0 = next(i for i, l in enumerate(L) if re.match(r'^\s+LIBER QUARTUS\. Locutiones de Numeris', l))
    a1 = next(i for i, l in enumerate(L) if i > a0 and re.match(r'^\s+LIBER QUINTUS\.', l))
    ini = []
    cap = None
    for i in range(a0, a1):
        m = REF.match(L[i].strip()) if L[i].strip().startswith('[') else None
        if m:
            if m.group(1):
                cap = C.romano(m.group(1))
            ini.append((i, cap, int(m.group(2))))
    por = {c: [] for c in C.CAPS}
    fins = [x[0] for x in ini[1:]] + [a1]
    blocos = {}  # NV -> [primeira linha, última linha (exclusiva), n.º de entradas]
    for (i, cv, v), fim in zip(ini, fins):
        n = nv(cv, v)
        if n in por:
            if n not in blocos:
                blocos[n] = [i, fim, 0]
            blocos[n][1] = fim
            blocos[n][2] += 1
    for n, (a, b, k) in blocos.items():
        por[n] = [(a, None, k, C.cortar(L, a, b))]
    return por


def rom(n):
    r = ''
    for v, sy in ((40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += sy
            n -= v
    return r


nq = nl = 0
Q = quest()
for cap in C.CAPS:
    if not Q[cap]:
        continue
    corpo = '\n\n'.join(f'**[Quaestiones in Heptateuchum IV, q. {k}: Num. {ref}]**\n\n{t}' for k, ref, t in Q[cap])
    ks = [k for k, r, t in Q[cap]]
    campos = {
        'Autor': 'Santo Agostinho (354–430)',
        'Obra': 'Quaestiones in Heptateuchum, livro IV (Quaestiones in Numeros)',
        'Passagem': f'{C.cap_nm(cap)}; Quaest. in Hept. IV, ' + ('q. ' + str(ks[0]) if len(ks) == 1 else f'qq. {ks[0]}–{ks[-1]}'),
        'Edição': C.edicao_pl(34, corpo) + '; CSEL 28/1 (Zycha, 1895)',
        'Fonte': URLQ,
        'Cobre': 'todas as questões de Agostinho sobre este capítulo (as referências entre colchetes são da Vulgata)',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-agostinho-num.py',
    }
    nota = ('As questões são curtas e literais; as referências «[Ib. XII, 1.]» são capítulo (romano) e versículos da Vulgata. '
            'A numeração das questões segue a ordem do livro IV (a edição do Corpus imprime um número errado na q. 32). '
            'Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]»; versão italiana no augustinus.it '
            '(latino/questioni_ettateuco/quest_ettateuco_4_libro.htm).')
    C.gravar(cap, 'agostinho-quaestiones-in-heptateuchum-4', 'Santo Agostinho, Quaestiones in Heptateuchum IV (Números)', campos, corpo, nota)
    nq += 1
LL = locut()
for cap in C.CAPS:
    if not LL[cap]:
        continue
    corpo = LL[cap][0][3]
    nent = LL[cap][0][2]
    campos = {
        'Autor': 'Santo Agostinho (354–430)',
        'Obra': 'Locutiones in Heptateuchum, livro IV (Locutiones de Numeris)',
        'Passagem': f'{C.cap_nm(cap)}; Locutiones in Hept. IV, ' + (f'{nent} entradas'),
        'Edição': C.edicao_pl(34, corpo) + '; CSEL 28/1 (Zycha, 1895)',
        'Fonte': URLL,
        'Cobre': 'todas as entradas deste capítulo (só gramática e idiomatismos da Vetus Latina)',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-agostinho-num.py',
    }
    nota = ('As «Locutiones» são notas de gramática sobre as expressões estranhas da versão latina que Agostinho tinha (a Vetus Latina); '
            'só servem para ver como ele lia o versículo. Cada entrada começa com a referência da Vulgata entre colchetes; as «[Ib. 9.]» '
            'sem capítulo continuam no último capítulo citado. Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]».')
    C.gravar(cap, 'agostinho-locutiones-in-heptateuchum-4', 'Santo Agostinho, Locutiones in Heptateuchum IV (Números)', campos, corpo, nota)
    nl += 1
print(nq, 'arquivos Quaestiones;', nl, 'arquivos Locutiones')
for cap in C.CAPS:
    print(f'Nm {cap:2d}: Q {[k for k,r,t in Q[cap]]}  L {LL[cap][0][2] if LL[cap] else 0}')
C.finalizar()
