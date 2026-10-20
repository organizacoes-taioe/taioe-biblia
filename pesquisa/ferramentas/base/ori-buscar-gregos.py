"""Busca citações dos capítulos-alvo (Sl 37-50 hebr. = 36-49 LXX; Nm 17-25 hebr.; 2Cor 3-7) em textos gregos
já convertidos (txt), por n-gramas de palavras sem acentos.

Uso (da pasta biblia/):
    python -I -X utf8 pesquisa/ferramentas/base/ori-buscar-gregos.py --saida achados.tsv <arquivo.txt|pasta> ...
    opções: --n 4 (tamanho do n-grama), --so "2Cor" (só um livro), --minimo 1

Saída TSV: arquivo, posição, rótulo (ex. «2Cor 3,18», «Sl 41(42),2», «Nm 21,9 [LXX 21,9]»), n-grama, contexto.
Agrupa os n-gramas vizinhos (menos de 300 caracteres) do mesmo versículo num achado só.
"""
import argparse, glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_gregos_comum as O


def alvos(so=None):
    a = {}
    if so in (None, 'Sl'):
        for (c, v), t in O.lxx('PSA').items():
            if 36 <= c <= 49:
                a[f'Sl {c + 1}({c} LXX),{v}'] = t
    if so in (None, 'Nm'):
        for (c, v), t in O.lxx('NUM').items():
            if c == 16 and v >= 36:
                a[f'Nm 17,{v - 35} [LXX 16,{v}]'] = t
            elif c == 17:
                a[f'Nm 17,{v + 15} [LXX 17,{v}]'] = t
            elif 18 <= c <= 25:
                a[f'Nm {c},{v}'] = t
    if so in (None, '2Cor'):
        for (c, v), t in O.nt().items():
            if 3 <= c <= 7:
                a[f'2Cor {c},{v}'] = t
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('fontes', nargs='+')
    ap.add_argument('--saida', required=True)
    ap.add_argument('--n', type=int, default=4)
    ap.add_argument('--so')
    a = ap.parse_args()
    arqs = []
    for f in a.fontes:
        arqs += sorted(glob.glob(os.path.join(f, '*.txt'))) if os.path.isdir(f) else glob.glob(f)
    hits = O.buscar(alvos(a.so), arqs, a.n)
    hits.sort(key=lambda h: (h[0], h[3], h[1]))
    grupos = []
    for h in hits:
        if grupos and grupos[-1][0] == h[0] and grupos[-1][3] == h[3] and h[1] - grupos[-1][2] < 300:
            g = grupos[-1]
            grupos[-1] = (g[0], g[1], max(g[2], h[2]), g[3], g[4] + ' | ' + h[4], g[5] + 1)
        else:
            grupos.append(h + (1,))
    cache = {}
    with open(a.saida, 'w', encoding='utf-8', newline='\n') as f:
        for arq, i, j, rot, gr, k in sorted(grupos, key=lambda g: (g[3], g[0], g[1])):
            if arq not in cache:
                cache = {arq: open(arq, encoding='utf-8', errors='replace').read()}
            t = cache[arq]
            ctx = t[max(0, i - 150):j + 150].replace('\n', ' ').replace('\t', ' ')
            f.write(f'{os.path.basename(arq)}\t{i}\t{rot}\t{k}\t{gr}\t{ctx}\n')
    print(len(grupos), 'achados em', len(arqs), 'arquivos ->', a.saida)


if __name__ == '__main__':
    main()
