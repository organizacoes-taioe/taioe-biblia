"""Pré-pesquisa do Gênesis, grupo orientais: acha, no Digital Syriac Corpus, as citações de um capítulo do Gênesis
(pela Peshitta) e, com --kw, procura palavras sem vogais em todo o corpus.

Uso (da pasta biblia/):
    python3 -I pesquisa/ferramentas/base/gen-orientais-corpus.py 1                 # n-gramas raros de Gn 1
    python3 -I pesquisa/ferramentas/base/gen-orientais-corpus.py --kw 'ܡܪܚܦ' Ephrem  # palavra (regex sem vogais),
                                                                                 # filtro opcional de autor/título
    python3 -I pesquisa/ferramentas/base/gen-orientais-corpus.py --bloco 530 20 22  # imprime blocos de um texto (com vogais)

O que faz: na primeira vez, clona o corpus (github.com/srophe/syriac-corpus, ~50 MB) em
pesquisa/cache/genesis/orientais/sc e baixa o Gênesis da Peshitta (ETCBC, plain/0.2) para peshitta/. A busca usa
3-gramas do versículo que não sejam fórmula (aparecem no máximo 3 vezes no Gênesis da Peshitta) e que sejam raros no
corpus (no máximo 8 textos). Saída: tabela na tela (texto, autor, título, versículos, página, seção, bloco, n-grama)
e cache/genesis/orientais/gn<ccc>-corpus.tsv. Os textos bíblicos do corpus ficam de fora.
Lembrete: só o primeiro passo. Os Padres parafraseiam o Gênesis; procurar também as palavras-chave do capítulo com
--kw (em Gn 1: ܡܪܚܦ «pairar», ܒܨܠܡܢ «à nossa imagem», ܢܗܝܪ̈ܐ «luzeiros», ܬܢܝܢܐ «monstros»). Siríacos fora da
comunhão com Roma (Dionísio bar Salibi, Filoxeno, Narsai, Isho`dad, Teodoro bar Koni, Timóteo II, Jacó de Edessa):
só pista. Link de cada texto: https://syriaccorpus.org/<n>.
"""
import collections, os, re, subprocess, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ori_siriaco_comum as C  # noqa: E402  (palavras, ler_tei, SINAIS)

RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))
CACHE = os.path.join(RAIZ, 'cache', 'genesis', 'orientais')
C.SC = os.path.join(CACHE, 'sc', 'data', 'tei')
C.PESH = os.path.join(CACHE, 'peshitta')


def preparar():
    if not os.path.isdir(C.SC):
        os.makedirs(CACHE, exist_ok=True)
        subprocess.run(['git', 'clone', '--depth', '1', '-q', 'https://github.com/srophe/syriac-corpus.git',
                        os.path.join(CACHE, 'sc')], check=True)
    os.makedirs(C.PESH, exist_ok=True)
    p = os.path.join(C.PESH, 'Genesis.txt')
    if not os.path.exists(p):
        urllib.request.urlretrieve('https://raw.githubusercontent.com/ETCBC/peshitta/master/plain/0.2/Genesis.txt', p)


def textos():
    for f in sorted(os.listdir(C.SC), key=lambda x: int(re.sub(r'\D', '', x) or 0)):
        if not f.endswith('.xml'):
            continue
        n = int(f[:-4])
        meta, blocos = C.ler_tei(n)
        if re.search(r'Apostle|Evangelist', meta['autor']) or 'Peshitta' in meta['titulo']:
            continue
        yield n, meta, blocos


def buscar(cap):
    preparar()
    pesh = C.peshitta_at('Genesis')
    pdf = collections.Counter()
    for ws in (C.palavras(v) for v in pesh.values()):
        pdf.update(set(tuple(ws[i:i + 3]) for i in range(len(ws) - 2)))
    alvo = {}
    for (c, v), tx in pesh.items():
        if c != cap:
            continue
        ws = C.palavras(tx)
        for i in range(len(ws) - 2):
            g = tuple(ws[i:i + 3])
            if sum(len(w) > 2 for w in g) >= 2 and pdf[g] <= 3:
                alvo.setdefault(g, set()).add(v)
    todos = []
    df = collections.Counter()
    for n, meta, blocos in textos():
        toks = [(w, ib) for ib, b in enumerate(blocos) for w in C.palavras(b[2])]
        df.update(set(tuple(w for w, _ in toks[i:i + 3]) for i in range(len(toks) - 2)))
        todos.append((n, meta, blocos, toks))
    linhas, vistos = [], set()
    for n, meta, blocos, toks in todos:
        ws = [w for w, _ in toks]
        for i in range(len(ws) - 2):
            g = tuple(ws[i:i + 3])
            if g in alvo and df[g] <= 8:
                ib = toks[i][1]
                if (n, ib) in vistos:
                    continue
                vistos.add((n, ib))
                linhas.append([n, meta['autor'], meta['titulo'][:60], ','.join(map(str, sorted(alvo[g]))),
                               blocos[ib][0], blocos[ib][3], ib, ' '.join(g)])
    saida = os.path.join(CACHE, f'gn{cap:03d}-corpus.tsv')
    with open(saida, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('texto\tautor\ttitulo\tversiculos\tpagina\tsecao\tbloco\tngrama\n')
        for l in linhas:
            fh.write('\t'.join(map(str, l)) + '\n')
    for l in linhas:
        print('\t'.join(map(str, l)))
    print(f'\n{len(linhas)} blocos; tabela em {saida}')


def kw(padrao, filtro=''):
    preparar()
    pat, aut = re.compile(padrao), re.compile(filtro)
    for n, meta, blocos in textos():
        if not aut.search(meta['autor'] + ' ' + meta['titulo']):
            continue
        for ib, (pg, tipo, tx, sec) in enumerate(blocos):
            s = C.SINAIS.sub('', tx)
            for m in pat.finditer(s):
                print(f"[{n}] {meta['autor'][:22]} | {meta['titulo'][:45]} | p.{pg} §{sec} b{ib}: "
                      f"…{s[max(0, m.start() - 120):m.end() + 120]}…")


def bloco(n, a, b):
    preparar()
    meta, blocos = C.ler_tei(n)
    print(meta)
    for i in range(a, min(b + 1, len(blocos))):
        pg, tipo, tx, sec = blocos[i]
        print(f'b{i} p.{pg} §{sec} [{tipo}] {tx}')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0].isdigit():
        buscar(int(a[0]))
    elif a[:1] == ['--kw'] and len(a) >= 2:
        kw(a[1], a[2] if len(a) > 2 else '')
    elif a[:1] == ['--bloco'] and len(a) == 4:
        bloco(int(a[1]), int(a[2]), int(a[3]))
    else:
        print(__doc__)
