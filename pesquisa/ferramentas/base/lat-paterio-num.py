"""Paterius, Liber testimoniorum (Expositio Veteris ac Novi Testamenti), livro IV «De Testimoniis libri Numerorum»
(PL 79, 761-?): excertos de São Gregório Magno (Moralia, Regra pastoral, Homilias) organizados por versículo.

    python -I -X utf8 pesquisa/ferramentas/base/lat-paterio-num.py

Baixa UMA vez o texto 8106 do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.PaNoGrI.ExVeAcN) e grava
numeros/<ccc>/base/paterio-expositio-numeros.md. Cada capítulo («CAP. n.--») traz o versículo no título e, numa nota de
Migne, a referência «Num. X, Y» e a obra de Gregório de onde veio. Os «Item unde supra» continuam o excerto anterior.
O livro IV salta do cap. 11 ao 16 de Números (nada sobre Nm 12-15) e acaba em Nm 35.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

IDNO = 8106
URL = 'https://mlat.uzh.ch/browser/cps_2.PaNoGrI.ExVeAcN'
L = C.cc_linhas(IDNO)
a0 = next(i for i, l in enumerate(L) if re.match(r'^\s+LIBER QUARTUS\. De Testimoniis libri Numerorum', l))
a1 = next(i for i, l in enumerate(L) if i > a0 and re.match(r'^\s+LIBER QUINTUS\. De Testimoniis in Deuteronomium', l))

heads = [i for i in range(a0, a1) if re.match(r'^\s+(CAPUT PRIMUM|CAP\. [IVXLC]+)\.-+', L[i])]
fim = heads[1:] + [a1]
# cap. da obra -> capítulo de Números (NV), conforme a nota de Migne do título
MAPA = {1: 6, 2: 7, 3: 8, 4: 8, 5: 9, 6: 10, 7: 10, 8: 11, 9: 11, 10: 11, 11: 17, 12: 17, 13: 19, 14: 19, 15: 19,
        16: 22, 17: 23, 18: 23, 19: 23, 20: 24, 21: 24, 22: 24, 23: 32, 24: 35}
ref = {}
txt = '\n'.join(L[a0:a1])
notas = dict((int(a), b) for a, b in re.findall(r'^\s+(\d+): \((.*?)\)\s*$', txt, flags=re.M))
por = {c: [] for c in C.CAPS}
for k, (a, b) in enumerate(zip(heads, fim), start=1):
    seg = C.cortar(L, a, b)
    titulo = ' '.join(x.strip() for x in L[a:a + 3] if x.strip())
    m = re.search(r'\[(\d+)\]', titulo)
    r = notas.get(int(m.group(1))) if m else None
    nm = MAPA[k]
    por[nm].append((k, r, seg))

ROM = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII',
       'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV']
n_arq = 0
for cap in C.CAPS:
    if not por[cap]:
        continue
    corpo = '\n\n'.join(f'**[Paterius, livro IV, cap. {ROM[k]}' + (f'; Migne: {r}' if r else '') + ']**\n\n' + seg for k, r, seg in por[cap])
    rots = ', '.join(f'cap. {ROM[k]}' for k, r, s in por[cap])
    campos = {
        'Autor': 'Paterius, notário de São Gregório Magno (séc. VI–VII)',
        'Obra': 'Liber testimoniorum (Expositio Veteris ac Novi Testamenti), livro IV: Números',
        'Passagem': f'{C.cap_nm(cap)}; Paterius IV, {rots}',
        'Edição': C.edicao_pl(79, corpo),
        'Fonte': URL,
        'Cobre': 'os excertos de Gregório sobre versículos deste capítulo (só os que Paterius escolheu)',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-paterio-num.py',
    }
    nota = ('Os excertos são de Gregório Magno (Moralia, Regra pastoral, Homilias sobre Ezequiel e sobre os Evangelhos); a nota de Migne '
            'no título dá o versículo de Números e, depois, a obra de Gregório. Os títulos «Item unde supra» continuam o excerto anterior. '
            'Texto da PL revisto no Corpus Corporum, com as colunas «[col. …]» e as notas de Migne.')
    C.gravar(cap, 'paterio-expositio-numeros', 'Paterius, Expositio Veteris ac Novi Testamenti, livro IV (Números)', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap}: {rots}  ({len(corpo)//1024 or 1} KB)')
print(n_arq, 'arquivos')
C.finalizar()
