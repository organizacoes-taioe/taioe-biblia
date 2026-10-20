"""Tabela «homilia -> versículos -> colunas da PG» das homilias de Crisóstomo sobre as cartas de Paulo.

    python -I -X utf8 pesquisa/ferramentas/base/grc-crisostomo-paulo-tabela.py              # todas as cartas
    python -I -X utf8 pesquisa/ferramentas/base/grc-crisostomo-paulo-tabela.py 1Cor Rm      # só algumas

Baixa (UMA vez, pausa de 1 s) os PDFs da khazarzar, `https://khazarzar.skeptik.net/pgm/PG_Migne/John%20Chrysostom_PG%2047-64/
<nome>.pdf`, converte com gregos-limpar.py e acha cada «ΟΜΙΛΙΑ» (o PDF às vezes erra o número: aqui se conta pela ordem).
O versículo em que a homilia começa é o do LEMA: compara as 4 primeiras palavras depois do título (sem acentos) com cada
versículo da SBLGNT (MorphGNT em pesquisa/cache/morphgnt/; `python pesquisa/ferramentas/grego.py --baixar` traz os livros).
Uma homilia vai até onde a seguinte começa (a última palavra do versículo final é aproximada: a homilia pode passar um
versículo). Escreve pesquisa/cache/base/paulo/crisostomo-paulo-tabela.md e imprime o mesmo. Resultado em fontes/paulo.md.
"""
import os, re, sys, unicodedata
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

BASE = 'https://khazarzar.skeptik.net/pgm/PG_Migne/John%20Chrysostom_PG%2047-64/{}.pdf'
# sigla, nome do PDF (sem .pdf, com %20), arquivo MorphGNT
LIVROS = [
    ('Rm', 'In%20epistulam%20ad%20Romanos', '66-Ro'),
    ('1Cor', 'In%20epistulam%20i%20ad%20Corinthios', '67-1Co'),
    ('2Cor', 'In%20epistulam%20ii%20ad%20Corinthios', '68-2Co'),
    ('Gl', 'In%20epistulam%20ad%20Galatas%20commentarius', '69-Ga'),
    ('Ef', 'In%20epistulam%20ad%20Ephesios', '70-Eph'),
    ('Fl', 'In%20epistulam%20ad%20Philippenses', '71-Php'),
    ('Cl', 'In%20epistulam%20ad%20Colossenses', '72-Col'),
    ('1Ts', 'In%20epistulam%20i%20ad%20Thessalonicenses', '73-1Th'),
    ('2Ts', 'In%20epistulam%20ii%20ad%20Thessalonicenses', '74-2Th'),
    ('1Tm', 'In%20epistulam%20i%20ad%20Timotheum', '75-1Ti'),
    ('2Tm', 'In%20epistulam%20ii%20ad%20Timotheum', '76-2Ti'),
    ('Tt', 'In%20epistulam%20ad%20Titum', '77-Tit'),
    ('Fm', 'In%20epistulam%20ad%20Philemonem', '78-Phm'),
    ('Hb', 'In%20epistulam%20ad%20Hebraeos', '79-Heb'),
]


def norm(w):
    d = unicodedata.normalize('NFD', w)
    d = ''.join(c for c in d if unicodedata.category(c)[0] == 'L')
    return d.lower().replace('ς', 'σ')


def versos(arq):
    caminho = os.path.join(RAIZ, 'cache', 'morphgnt', f'{arq}-morphgnt.txt')
    v = {}
    for l in ler(caminho).split('\n'):
        p = l.split()
        if len(p) < 5:
            continue
        k = p[0]
        v.setdefault((int(k[2:4]), int(k[4:6])), []).append(norm(p[4]))
    return v


def candidatos(pal, V):
    """Versículos cujo texto aparece nas primeiras palavras da homilia (lema): (cap, ver, razão de bigramas casados)."""
    janela = set(zip(pal[:60], pal[1:61]))
    out = []
    for (c, vs), w in V.items():
        bi = list(zip(w, w[1:]))
        if not bi:
            continue
        ac = sum(1 for x in bi if x in janela)
        if ac >= min(2, len(bi)) and ac / len(bi) >= 0.5:
            out.append((c, vs))
    return sorted(out)


def tabela(sigla, nome, arq):
    pdf = baixar(BASE.format(nome), f'crisostomo-{sigla}.pdf')
    txt = ler(pdf_para_texto_grego(pdf, os.path.join(CACHE, f'crisostomo-{sigla}.txt')))
    V = versos(arq)
    cabecas = [m for m in re.finditer(r'(?:ΟΜΙΛΙΑ|ΛΟΓΟΣ)\s+[^\s.]+[ʹ.]?\.?', txt)]
    marc = [(m.start(), int(m.group(1)), int(m.group(2))) for m in re.finditer(r'\[PG (\d+), (\d+)\]', txt)]

    def col(pos):
        ant = [x for x in marc if x[0] <= pos]
        return (ant[-1][1], ant[-1][2]) if ant else (None, None)

    inicios, ultimo = [], (0, 0)
    for i, m in enumerate(cabecas):
        fim = cabecas[i + 1].start() if i + 1 < len(cabecas) else len(txt)
        corpo = txt[m.end():fim]
        pal = [norm(w) for w in re.findall(r'\S+', corpo[:900]) if norm(w)]
        cand = [x for x in candidatos(pal, V) if x >= ultimo]
        ver = cand[0] if cand else None
        if ver:
            ultimo = ver
        inicios.append((i + 1, m.group(0).strip(), ver, m.start(), fim))
    linhas = []
    for k, (n, rotulo, ver, a, b) in enumerate(inicios):
        c0 = col(a + 1)
        c1 = col(b - 1)
        prox = next((x[2] for x in inicios[k + 1:] if x[2]), None)
        v0 = f'{ver[0]},{ver[1]}' if ver else '?'
        v1 = f'{prox[0]},{prox[1]}' if prox else 'fim'
        linhas.append(f'| {sigla} | {n} | {rotulo} | {v0} até antes de {v1} | PG {c0[0]}, {c0[1]}–{c1[1]} |')
    return linhas


def main():
    quer = sys.argv[1:]
    saida = ['| carta | homilia (ordem) | título no PDF | versículos (pelo lema) | colunas |', '|---|---|---|---|---|']
    for sigla, nome, arq in LIVROS:
        if quer and sigla not in quer:
            continue
        try:
            saida += tabela(sigla, nome, arq)
        except Exception as e:
            saida.append(f'| {sigla} | falhou: {e} | | | |')
    texto = '\n'.join(saida)
    with open(os.path.join(CACHE, 'crisostomo-paulo-tabela.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(texto + '\n')
    print(texto)


if __name__ == '__main__':
    main()
