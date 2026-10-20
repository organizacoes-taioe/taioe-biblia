"""Orígenes, Homiliae in Numeros (latim de Rufino; GCS 30 = Origenes Werke VII, ed. Baehrens, 1921), cortadas por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/lat-origenes-num.py

Baixa UMA vez o OCR do archive.org (https://archive.org/details/origenes-werke.-bd-7-1921; texto em
https://archive.org/download/origenes-werke.-bd-7-1921/Origenes%20Werke.%20Bd%207%2C%201921_djvu.txt, 1,9 MB; as homilias sobre
Números ocupam os primeiros 840 KB, depois vêm as de Josué e Juízes) para pesquisa/cache/base/numeros/origenes_gcs7_djvu.txt e grava
numeros/<ccc>/base/origenes-homilias-in-numeros.md.

O OCR mistura o aparato crítico (variantes, «vgl.», números de linha de 5 em 5) e perde linhas inteiras; o cabeçalho de algumas homilias saiu
estragado. Por isso as 28 homilias (H1…H28) são achadas por posição, conferida por uma frase do começo de cada uma (a frase tem de aparecer
perto da posição; senão o script para). As margens trazem as páginas de Delarue («Del.», = PG 12) e de Lommatzsch («Lomm.»). Para citar,
transcrever da imagem da página (leaf = página + 36).
Mapa das homilias em Números (numeração da Nova Vulgata; Orígenes segue a Vulgata/LXX): H1 Nm 1; H2 Nm 2; H3-H4 Nm 3 (H4 também Nm 4); H5 Nm 4;
H6 Nm 11 e 12,1; H7 Nm 12-13; H8 Nm 13-14; H9 Nm 16,36-50 e 17 (Vulg.) = NV 17; H10-H11 Nm 18; H12 Nm 21 (o poço e o cântico);
H13 Nm 21 e 22; H14 Nm 22; H15-H16 Nm 23; H17-H19 Nm 24; H20 Nm 25; H21 Nm 26; H22 Nm 27; H23-H24 Nm 28-29; H24 também Nm 30; H25 Nm 31;
H26 Nm 31 e 32; H27 Nm 33; H28 Nm 34. Orígenes não tem homilia sobre Nm 5-10, 19-20, 35 e 36.
Alguns cortes dentro de uma homilia (H6, H13, H23, H24, H26) são nos parágrafos que mudam de capítulo, conferidos pelas referências «Num. N, V»
do aparato. As homilias que cobrem dois capítulos aparecem inteiras nos dois quando não se achou um ponto de corte limpo (H4).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

URL = 'https://archive.org/details/origenes-werke.-bd-7-1921'
OCR = 'https://archive.org/download/origenes-werke.-bd-7-1921/Origenes%20Werke.%20Bd%207%2C%201921_djvu.txt'
p = C.baixar(OCR, 'origenes_gcs7_djvu.txt', minimo=100000)
T = C.ler(p)


def alfa(s):
    return re.sub(r'[^a-z]', '', C.sem_acento(s).lower())


# H<n>: (posição do começo no OCR, frase do começo para conferir)
H = {
    1: (76839, 'Divinis Numeris non omnes digni sunt'),
    2: (91254, 'Prima Numerorum lectio docuit'),
    3: (103686, 'Scriptum est de manna'),
    4: (120667, 'Numerorum liber est'),
    5: (133972, 'Responsa dans Dominus ad Moysen'),
    6: (151074, 'Plura nobis simul'),
    7: (167367, 'Apostolus dicit'),
    8: (199166, 'Duodecim missi sunt'),
    9: (210531, 'Apud Deum, ut intelligi'),
    10: (249141, 'Qui meliores sunt'),
    11: (267093, 'Primitias omnium frugum'),
    12: (316643, 'Lectio nobis putei'),
    13: (353382, 'Hesterno die'),
    14: (386559, 'Plura sunt, quae nobis'),
    15: (409538, 'Licet nos ordo lectionum'),
    16: (433779, 'Priore tractatu'),
    17: (476938, 'Tertiam nunc prophetiam'),
    18: (515667, 'Quartam nunc prophetiam'),
    19: (540535, 'Quinta haec'),
    20: (563135, 'Lectio hodie recitata est'),
    21: (601022, 'Numeri sunt, quos legimus'),
    22: (613517, 'Quinque filiae fuerunt'),
    23: (631399, 'observatio sacrificiorum'),
    24: (666953, 'Omnes, qui imbuendi sunt'),
    25: (691412, 'In superioribus fornicati sunt'),
    26: (718300, 'Differentias esse'),
    27: (752550, 'Cum conderet Deus mundum'),
    28: (821348, 'Ultima in libro Numerorum'),
}
FIM = 838361  # começa a homilia 1 sobre Josué
for n, (pos, frase) in H.items():
    janela = alfa(T[max(0, pos - 100): pos + 1500])
    af = alfa(frase)
    if af[:9] not in janela and af[-9:] not in janela:  # o OCR estropia letras: basta um dos dois pedaços
        raise SystemExit(f'H{n}: a frase «{frase}» não está perto da posição {pos}: o OCR mudou? Refazer as posições.')
ini = {n: pos for n, (pos, f) in H.items()}
fim = {n: (ini[n + 1] if n < 28 else FIM) for n in H}


def H_(n, a=0, b=None):
    """Texto da homilia n, do deslocamento a ao b (relativos ao começo)."""
    return (n, ini[n] + a, ini[n] + (b if b is not None else fim[n] - ini[n]))


# cada item: (homilia, deslocamento inicial, deslocamento final ou None, rótulo)
MAPA = {
    1: [(1, 0, None, 'H1 (Nm 1)')],
    2: [(2, 0, None, 'H2 (Nm 2)')],
    3: [(3, 0, None, 'H3 (Nm 3,12 ss.: os levitas no lugar dos primogênitos)'), (4, 0, None, 'H4 (Nm 3,39 e 4)')],
    4: [(4, 0, None, 'H4 (Nm 3,39 e 4)'), (5, 0, None, 'H5 (Nm 4,18)')],
    11: [(6, 0, 12577, 'H6, §§1–3 (Nm 11,24-29: os setenta anciãos)')],
    17: [(9, 0, None, 'H9 (Nm 16,36–17,13 Vulg.: os turíbulos e a vara de Aarão)')],
    18: [(10, 0, None, 'H10 (Nm 18,1: «tu e teus filhos levareis os pecados do santuário»)'), (11, 0, None, 'H11 (Nm 18: as primícias e os dízimos)')],
    21: [(12, 0, None, 'H12 (Nm 21,16-18: o poço e o cântico)'), (13, 0, 7879, 'H13, §§1–2 (Nm 21,21-35: Seon e Og)')],
    22: [(13, 7879, None, 'H13, §3 ss. (Nm 22: Balaão e a jumenta)'), (14, 0, None, 'H14 (Nm 22: Balaão e a jumenta, continuação)')],
    23: [(15, 0, None, 'H15 (Nm 23,7-10: a primeira profecia)'), (16, 0, None, 'H16 (Nm 23,18-24: a segunda profecia)')],
    24: [(17, 0, None, 'H17 (Nm 24,3-9: a terceira profecia)'), (18, 0, None, 'H18 (Nm 24,15-19: a quarta profecia)'),
         (19, 0, 22600, 'H19, até o §4 (Nm 24,20-24: Amalec e o cineu)')],
    25: [(20, 0, None, 'H20 (Nm 25: Baal-Fegor e Finéias)')],
    26: [(21, 0, None, 'H21 (Nm 26: o segundo recenseamento)')],
    27: [(22, 0, None, 'H22 (Nm 27: as filhas de Salfaad e o sucessor de Moisés)')],
    28: [(23, 0, 27042, 'H23, §§1–8 (Nm 28: as festas, do sacrifício perpétuo aos novos frutos)'), (24, 0, 10920, 'H24, §1 (Nm 28–29: os sacrifícios de cada festa)')],
    29: [(23, 27042, None, 'H23, §§9–10 (Nm 29: o sétimo mês, o jejum)'), (24, 0, 10920, 'H24, §1 (Nm 28–29: os sacrifícios de cada festa)')],
    30: [(24, 10920, None, 'H24, §§2–3 (Nm 30: os votos)')],
    31: [(25, 0, None, 'H25 (Nm 31: a vingança contra Madiã)'), (26, 0, 10358, 'H26, §§1–2 (Nm 31,25-54: a partilha da presa)')],
    32: [(26, 10358, 34250 - 130, 'H26, §3 ss. (Nm 32: Rúben, Gad e meia tribo de Manassés)')],
    33: [(27, 0, None, 'H27 (Nm 33: as quarenta e duas mansões)')],
    34: [(28, 0, None, 'H28 (Nm 34: a descrição da terra santa)')],
}

LIMPAR_NUM = re.compile(r'^\s*\d{1,3}\s*$')
CAB = re.compile(r'^\s*Origenes( VII\.?)?\s*\.?\s*$')


def limpar(txt):
    out = []
    for l in txt.split('\n'):
        if LIMPAR_NUM.match(l) or CAB.match(l):
            continue
        out.append(l.rstrip())
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip('\n')


n_arq = 0
for cap in C.CAPS:
    if cap not in MAPA:
        continue
    partes = []
    for n, a, b, rot in MAPA[cap]:
        fim_h = fim[n] - ini[n]
        txt = limpar(T[ini[n] + a: ini[n] + (b if b is not None else fim_h)])
        partes.append((rot, txt))
    corpo = '\n\n'.join(f'**[Orígenes, Homiliae in Numeros, {r}]**\n\n{t}' for r, t in partes)
    campos = {
        'Autor': 'Orígenes (c. 185–c. 253)',
        'Obra': 'Homiliae in Numeros (versão latina de Rufino)',
        'Passagem': f'{C.cap_nm(cap)}; ' + '; '.join(r.split(' (')[0] for r, t in partes),
        'Edição': 'GCS 30 (Origenes Werke VII), Baehrens, Leipzig 1921; PG 12 e Lommatzsch t. 10 (páginas «Del.» e «Lomm.» nas margens do texto)',
        'Fonte': URL,
        'Cobre': 'a(s) homilia(s) que comentam este capítulo, inteiras ou no trecho indicado',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-origenes-num.py',
    }
    nota = ('OCR do archive.org (' + OCR + '): traz o aparato crítico (variantes «BCE», «vgl.», referências «Num. N, V» no pé da página) e os números de linha, '
            'perde linhas inteiras e estropia letras (c/e, n/u, i/l). Serve para achar o trecho; para citar, transcrever da imagem (página P = imagem n(P+36)). '
            'Orígenes não é santo: citar como «Orígenes», na versão latina de Rufino. As referências «Num. N, V» do aparato são da Vulgata. '
            'Os cortes dentro de uma homilia estão indicados no rótulo de cada trecho.')
    C.gravar(cap, 'origenes-homilias-in-numeros', 'Orígenes, Homiliae in Numeros (Rufino)', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: ' + '; '.join(r.split(' (')[0] for r, t in partes) + f'  {len(corpo)//1024} KB')
print(n_arq, 'arquivos')
C.finalizar()
