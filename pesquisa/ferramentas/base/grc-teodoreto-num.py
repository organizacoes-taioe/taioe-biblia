"""Teodoreto de Ciro, Quaestiones in Octateuchum: Quaestiones in Numeros (PG 80, 349-400), por capítulo de Números.

    python -I -X utf8 pesquisa/ferramentas/base/grc-teodoreto-num.py

Baixa UMA vez o PDF da «Ψηφιακή Πατρολογία» (khazarzar):
https://khazarzar.skeptik.net/pgm/PG_Migne/Theodoretus%20of%20Cyrrhus_PG%2080-84/Quaestiones%20in%20Octateuchum.pdf
para pesquisa/cache/base/numeros/teodoreto-qoct.pdf e grava numeros/<ccc>/base/teodoreto-quaestiones-in-numeros.md.

O PDF segue a edição moderna (Fernández Marcos–Sáenz-Badillos, Madri 1979), sem as colunas da PG: os números soltos no texto
(«191», «216») são páginas dessa edição. Texto de Números: das linhas 3391 a 4040 do texto extraído. As 51 perguntas vêm numeradas
no corpo («XXII Τίνα χρὴ νοῆσαι τὴν αἰθιόπισσαν…»); a tabela MAPA diz a que capítulo de Números (Nova Vulgata) cada uma pertence
(pela leitura de cada pergunta). Quando uma pergunta serve a dois capítulos, entra nos dois.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

URL = C.khazarzar_url('Theodoretus of Cyrrhus_PG 80-84', 'Quaestiones in Octateuchum.pdf')
C.baixar(URL, 'teodoreto-qoct.pdf', minimo=1000)
L = C.pdf_linhas('teodoreto-qoct.pdf')

# trecho de Números: da pergunta I de Números à linha «QUAESTIONES IN DEUTERONOMIUM»
fim = next(i for i, l in enumerate(L) if re.match(r'^(?:\d+\s+)?QUAESTIONES IN DEUTERONOMIUM', l))
ini = next(i for i, l in enumerate(L) if i > 2800 and 'Διὰ τί προσέταξεν ἀριθμηθῆναι' in l)
seg = L[ini:fim]
seg[0] = seg[0][seg[0].index('I Διὰ'):]
txt = '\n'.join(seg)

# início de cada pergunta: numeral romano esperado em sequência (I, II, III…)
pat = re.compile(r'(?:(?<=\s)|^)([IVXL]{1,7})(?:[ \t]+|$)', re.M)
pos, esp = [], 1
for m in pat.finditer(txt):
    try:
        n = C.romano(m.group(1))
    except Exception:
        continue
    if n == esp:
        pos.append((n, m.start()))
        esp += 1
assert len(pos) == 51, len(pos)
fins = [p for n, p in pos[1:]] + [len(txt)]
Q = {n: txt[p:f].strip() for (n, p), f in zip(pos, fins)}

MAPA = {1: [1], 2: [1, 3], 3: [1], 4: [3], 5: [3], 6: [4], 7: [5], 8: [5], 9: [5], 10: [5], 11: [6], 12: [8], 13: [8], 14: [9],
        15: [10], 16: [10], 17: [11], 18: [11], 19: [11], 20: [11], 21: [11], 22: [12], 23: [12], 24: [13], 25: [13], 26: [13],
        27: [14], 28: [15], 29: [15], 30: [15], 31: [15], 32: [16], 33: [16], 34: [17, 18], 35: [19], 36: [19], 37: [20], 38: [21],
        39: [22], 40: [22], 41: [22], 42: [22, 23], 43: [23], 44: [24, 25], 45: [26], 46: [26], 47: [27], 48: [31], 49: [33], 50: [35],
        51: [36]}
por = {c: [] for c in C.CAPS}
for q, nms in MAPA.items():
    for nm in nms:
        if nm in por:
            por[nm].append(q)

ROM = lambda n: ''.join(s * (n // v) if False else '' for v, s in [])  # (não usado)


def rom(n):
    r = ''
    for v, sy in ((50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += sy
            n -= v
    return r


n_arq = 0
for cap in C.CAPS:
    if not por[cap]:
        continue
    qs = por[cap]
    corpo = '\n\n'.join(f'**[Teodoreto, Quaestiones in Numeros, pergunta {rom(q)}]**\n\n{Q[q]}' for q in qs)
    campos = {
        'Autor': 'Teodoreto de Ciro (c. 393–c. 460)',
        'Obra': 'Quaestiones in Octateuchum: Quaestiones in Numeros',
        'Passagem': f'{C.cap_nm(cap)}; Quaestiones in Numeros, ' + ('pergunta ' + rom(qs[0]) if len(qs) == 1 else
                    'perguntas ' + ', '.join(rom(q) for q in qs)) + ' (numeração do livro, de I a LI)',
        'Edição': 'PG 80, 349–400 (as colunas não vêm no PDF); texto da ed. Fernández Marcos–Sáenz-Badillos, Madri 1979',
        'Fonte': URL,
        'Cobre': 'as perguntas de Teodoreto sobre este capítulo (cada uma com a resposta curta)',
        'Oriental': 'sim',
        'Língua': 'grc',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/grc-teodoreto-num.py',
    }
    nota = ('O PDF da «Ψηφιακή Πατρολογία» (Univ. do Egeu) segue a edição moderna de Fernández Marcos–Sáenz-Badillos (1979), que pode ter direito '
            'autoral: usar para pesquisa e citar curto; o texto da PG 80 (domínio público) é equivalente. Os números soltos no texto (191, 216…) '
            'são páginas dessa edição, não colunas da PG; os algarismos romanos no começo de cada pergunta são do próprio livro. '
            'Colunas da PG 80: no OCR do archive.org «bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1860_80».')
    C.gravar(cap, 'teodoreto-quaestiones-in-numeros', 'Teodoreto de Ciro, Quaestiones in Octateuchum: Quaestiones in Numeros', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: perguntas {[rom(q) for q in qs]}  {len(corpo)//1024 or 1} KB')
print(n_arq, 'arquivos')
C.finalizar()
