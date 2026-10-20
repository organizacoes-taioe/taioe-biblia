"""Acha, no Digital Syriac Corpus, as citações dos capítulos-alvo (pela Peshitta) e lista os achados.

    python -I -X utf8 pesquisa/ferramentas/base/ori-siriaco-buscar.py                 # alvos padrão
    python -I -X utf8 pesquisa/ferramentas/base/ori-siriaco-buscar.py nm:17-25 sl:37-50 2cor:3-7

Saída: pesquisa/cache/base/ori/siriaco-achados.tsv (texto, autor, título, ref, página, seção, bloco, n-grama) e um
resumo na tela por capítulo e obra. É só o primeiro passo: quem decide o que vira base/ é
ori-siriaco-gravar.py (lista curada). Método: 4-gramas de palavras (sem vogais, sem o ܘ inicial) do versículo
na Peshitta, e 3-gramas raros (que não aparecem em mais de 3 textos do corpus); sem os textos bíblicos.
Numeração dos Salmos: a da Peshitta, que é a hebraica (a mesma das pastas salmos/<ccc>).
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_siriaco_comum as C

# autores que entram (ver pesquisa/fontes/orientais.md, «Quem entra»); hereges e textos bíblicos fora
AUTORES = ['Ephrem', 'Aphrahat', 'Jacob of Serugh', 'Narsai', 'Isaac of Nineveh', 'Philoxenos', 'Dionysius bar',
           'Isaac of Antioch', 'Balai', 'Rabbula', 'John the Solitary', 'Joseph Hazzaya', 'Ishoʿyahb', 'Moshe bar Kepha',
           'Gregorius bar Hebraeus', 'Timothy II', 'Simeon of Beth Arsham', 'Abraham of Nathpar', 'Jacob of Nisibis',
           'Thomas of Edessa', 'Anton of Tagrit', 'Titus of Bostra', 'Papa bar Aggai', 'Barlaha', 'Judah Kyriakos']
LIVRE_GRADUUM = range(188, 219)  # Liber Graduum (anônimo)


def alvos(args):
    if not args:
        args = ['nm:17-25', 'sl:37-50', '2cor:3-7']
    out = []
    for a in args:
        livro, faixa = a.split(':')
        i, j = (int(x) for x in faixa.split('-'))
        out += [(livro, c) for c in range(i, j + 1)]
    return out


def main():
    C.preparar()
    alv = alvos(sys.argv[1:])
    fontes = {'nm': C.peshitta_at('Numbers'), 'sl': C.peshitta_at('Psalms'), '2cor': C.peshitta_2cor()}
    # textos do corpus
    textos = []
    for f in os.listdir(C.SC):
        if not f.endswith('.xml'):
            continue
        n = int(f[:-4])
        meta, blocos = C.ler_tei(n)
        if not (any(a in meta['autor'] for a in AUTORES) or n in LIVRE_GRADUUM):
            continue
        if n in LIVRE_GRADUUM:
            meta['autor'] = 'Liber Graduum'
        toks = []  # (palavra, i_bloco)
        for ib, (pg, tipo, tx, sec) in enumerate(blocos):
            for w in C.palavras(tx):
                toks.append((w, ib))
        textos.append((meta, blocos, toks))
    # frequência dos 3-gramas por texto
    df3 = collections.Counter()
    for meta, blocos, toks in textos:
        ws = [w for w, _ in toks]
        df3.update(set(tuple(ws[i:i + 3]) for i in range(len(ws) - 2)))
    # frequência dos n-gramas na própria Peshitta (fórmulas como «e o Senhor falou a Moisés» ficam fora)
    pf = collections.Counter()
    for vs in fontes.values():
        for tx in vs.values():
            ws = C.palavras(tx)
            pf.update(set(tuple(ws[i:i + k]) for k in (3, 4) for i in range(len(ws) - k + 1)))
    # n-gramas dos versículos-alvo
    idx = collections.defaultdict(set)  # ngrama -> {(livro, cap, vers)}
    for livro, cap in alv:
        for (c, v), tx in fontes[livro].items():
            if c != cap:
                continue
            ws = C.palavras(tx)
            for i in range(len(ws) - 3):
                g = tuple(ws[i:i + 4])
                if pf[g] <= 2 and df3[g[:3]] <= 40:
                    idx[g].add((livro, c, v))
            for i in range(len(ws) - 2):
                g = tuple(ws[i:i + 3])
                if df3[g] <= 3 and pf[g] <= 2 and sum(len(w) for w in g) >= 9:
                    idx[g].add((livro, c, v))
    os.makedirs(os.path.join(C.CACHE, 'ori'), exist_ok=True)
    saida = os.path.join(C.CACHE, 'ori', 'siriaco-achados.tsv')
    resumo = collections.defaultdict(lambda: collections.defaultdict(set))
    with open(saida, 'w', encoding='utf-8', newline='\n') as f:
        for meta, blocos, toks in textos:
            ws = [w for w, _ in toks]
            vistos = set()
            for k in (4, 3):
                for i in range(len(ws) - k + 1):
                    g = tuple(ws[i:i + k])
                    if g not in idx:
                        continue
                    ib = toks[i][1]
                    for ref in idx[g]:
                        if (ref, ib) in vistos:
                            continue
                        vistos.add((ref, ib))
                        livro, c, v = ref
                        f.write(f"{meta['n']}\t{meta['autor']}\t{meta['titulo']}\t{livro} {c},{v}\t{blocos[ib][0]}\t{blocos[ib][3]}\t{ib}\t{' '.join(g)}\n")
                        resumo[(livro, c)][(meta['n'], meta['autor'][:20], meta['titulo'][:60])].add(v)
    for (livro, c) in alv:
        r = resumo.get((livro, c), {})
        print(f'== {livro} {c}: {len(r)} textos')
        for (n, a, t), vs in sorted(r.items(), key=lambda x: -len(x[1])):
            print(f'   {n:>4} {a:20} {t:60} vv. {",".join(map(str, sorted(vs)))}')
    print('achados em', saida)


if __name__ == '__main__':
    main()
