"""Rábano Mauro, Enarrationes in librum Numerorum (PL 108, 587-?), cortado por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/lat-rabano-num.py

Baixa UMA vez o texto 8898 do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.RabMau.EnInLiN) para
pesquisa/cache/base/numeros/cc_8898.txt e grava numeros/<ccc>/base/rabano-enarrationes-numeros.md (capítulos
1-11 e 17-36 da Nova Vulgata).

Como corta: o Corpus Corporum conserva as notas de Migne («245: (CAP. XVI.)»), que marcam onde começa cada
capítulo da Vulgata no texto («[245]Ecce autem Chore…»). O capítulo N da Nova Vulgata vai da marca do capítulo
N à marca do N+1; um título «CAPUT …» colado antes da marca entra no capítulo. Exceção: Nm 17 (NV) = Nm 16,36-50
e 17,1-13 da Vulgata: começa no título «CAPUT XVIII. De thuribulis seditiosorum ab incendio sublatis» (livro II).
Rábano é compilação (Orígenes na versão de Rufino, Agostinho, Jerônimo, Isidoro); as fontes vêm indicadas
às vezes («Ex Augustino») nas notas de Migne, mantidas no texto.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDNO = 8898
URL = 'https://mlat.uzh.ch/browser/cps_2.RabMau.EnInLiN'
linhas = C.cc_linhas(IDNO)
txt = '\n'.join(linhas)

# 1. início de cada capítulo da Vulgata, pelas notas de Migne
inicio = {}
for m in re.finditer(r'^\s+(\d+): \(CAP\. ([IVXL]+)\.?\)', txt, flags=re.M):
    n = C.romano(m.group(2))
    if n not in inicio:
        inicio[n] = int(m.group(1))


def linha_do_marcador(num):
    pat = re.compile(r'\[%d\]' % num)
    for i, l in enumerate(linhas):
        if pat.search(l) and not re.match(r'^\s+%d: ' % num, l):
            return i
    raise KeyError(num)


def com_titulo(i):
    """Sobe até o título «CAPUT …» (e «LIBER …») colado antes da linha i."""
    j = i - 1
    vistos = 0
    while j >= 0 and vistos < 6:
        l = linhas[j]
        if re.match(r'^\s+CAPUT', l):
            k = j - 1
            while k >= 0 and (not linhas[k].strip()):
                k -= 1
            if k >= 0 and re.match(r'^\s+LIBER', linhas[k]):
                return k
            return j
        if l.strip() and not C.COL_RE.match(l.strip()):
            vistos += 1
        j -= 1
    return i


pos = {n: com_titulo(linha_do_marcador(m)) for n, m in inicio.items()}
# Nm 17 (NV): começa no título do livro II, cap. XVIII
i17 = next(i for i, l in enumerate(linhas) if re.match(r'^\s+CAPUT XVIII\. De thuribulis', l))
pos[17] = i17
pos[16] = pos[16]
pos['fim'] = len(linhas)
# a numeração da Vulgata: NV 18 = Vulg 18; o Vulg 17 já está incluído no NV 17 (de i17 até a marca do cap. 18)
ordem = {}
for cap in range(1, 37):
    a = pos[cap] if cap != 1 else next(i for i, l in enumerate(linhas) if 'INCIPIUNT ENARRATIONES IN NUMEROS' in l)
    b = pos[cap + 1] if cap < 36 else pos['fim']
    if cap == 16:
        b = i17
    if cap == 17:
        b = pos[18]
    ordem[cap] = (a, b)

n_ok = 0
for cap in C.CAPS:
    a, b = ordem[cap]
    seg = C.cortar(linhas, a, b)
    caps_tit = re.findall(r'^\s+(CAPUT [IVXL]+|CAPUT PRIMUM)\.', seg, flags=re.M)
    livros = [i for i in re.findall(r'^\s+LIBER (\w+)\.', seg, flags=re.M)]
    nomes = C.estrutura(linhas, a, b)
    campos = {
        'Autor': 'Rábano Mauro (c. 780–856)',
        'Obra': 'Enarrationes in librum Numerorum',
        'Passagem': f'{C.cap_nm(cap)}; Rábano, {nomes}',
        'Edição': C.edicao_pl(108, seg),
        'Fonte': URL,
        'Cobre': 'o capítulo inteiro (compilação: Orígenes/Rufino, Agostinho, Jerônimo, Isidoro; as fontes aparecem nas notas de Migne)',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-rabano-num.py',
    }
    nota = ('Texto da PL (Migne) revisto no Corpus Corporum, com as colunas «[col. …]» e as notas de Migne no rodapé de cada página '
            '(«N: (CAP. X.)»). O lema bíblico vem no corpo do texto; as chamadas «[N]» remetem às notas de Migne. Rábano copia Orígenes quase palavra por palavra.')
    C.gravar(cap, 'rabano-enarrationes-numeros', 'Rábano Mauro, Enarrationes in librum Numerorum', campos, seg, nota)
    n_ok += 1
    print(f'Nm {cap:2d}: linhas {a}-{b} ({len(seg)//1024} KB) {nomes}')
print(n_ok, 'arquivos')
C.finalizar()
