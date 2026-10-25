"""São João Crisóstomo no Gênesis: Homiliae in Genesim (67) e Sermones in Genesim (9), por capítulo.

    python3 -I pesquisa/ferramentas/base/gen-gregos-crisostomo.py [capítulos]      (padrão: 1; ex.: 1-11)

Fontes (baixadas UMA vez para pesquisa/cache/genesis/gregos/, fora do git):
  - Sermones in Genesim 1–9 (PG 54, 581–630), grego: khazarzar, «John Chrysostom_PG 47-64/In Genesim sermones.pdf»
    («54.587» -> «[PG 54, 587]»; o PDF é apagado depois da conversão). Tabela SERMOES (pela leitura dos títulos):
    1 = Gn 1,1; 2 = 1,26 («Façamos», a imagem); 3 = 1,26–28 (a semelhança, o domínio perdido) e 2,19; 4 = 1,28 e 3,16
    (as três servidões); 5 = Gn 3; 6–8 = Gn 2 (a árvore, o mandamento); 9 = Gn 17,5 e 5,29 (os nomes). O PDF
    «In Genesim sermo 3.pdf» é outro, espúrio (PG 56, 525: Quaresma, o exílio de Adão): só pista.
  - Homiliae in Genesim 1–67 (PG 53, 21–385; PG 54, 385–580): a khazarzar NÃO as tem. O grego só existe aqui no OCR do
    archive.org da PG greco-latina (53 = «patrologiaecurs24migngoog», ilegível para citar); o script guarda o LATIM da PG
    (versão de Montfaucon, domínio público) do OCR legível da edição só latina de 1859 («bim_early-english-books-1641-1700_1859_53»
    e «…_1859_54»), que traz nos cabeçalhos as colunas da PG greco-latina e o capítulo do Gênesis de cada página
    («IN CAP. I. GENES. HOMIL. III»). Cada homilia vai para os capítulos que aparecem nesses cabeçalhos (e nas
    referências «(Gen. 1. 9)» do título). Para citar o grego, conferir na imagem da PG 53/54.
"""
import collections, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
URL_SERM = G.khz('John Chrysostom_PG 47-64', 'In Genesim sermones.pdf')
URL_SERM3SP = G.khz('John Chrysostom_PG 47-64', 'In Genesim sermo 3.pdf')
LAT = {53: 'https://archive.org/download/bim_early-english-books-1641-1700_1859_53/bim_early-english-books-1641-1700_1859_53_djvu.txt',
       54: 'https://archive.org/download/bim_early-english-books-1641-1700_1859_54/bim_early-english-books-1641-1700_1859_54_djvu.txt'}
LAT_VER = {53: 'https://archive.org/details/bim_early-english-books-1641-1700_1859_53',
           54: 'https://archive.org/details/bim_early-english-books-1641-1700_1859_54'}
GRC_PG53 = 'https://archive.org/details/patrologiaecurs24migngoog'
SERMOES = {1: [1], 2: [1], 3: [1, 2], 4: [1, 3], 5: [3], 6: [2], 7: [2], 8: [2], 9: [5, 17]}
ROM = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def romano(s):
    s = s.strip()
    if s in ('U', 'u', 'Il', 'lI', 'll'):      # o OCR lê «II» assim
        s = 'II'
    s = s.upper().replace('1', 'I').replace('Ï', 'I')
    s = re.sub(r'[^IVXLC]', '', s)
    if not s:
        return None
    n = 0
    for i, c in enumerate(s):
        v = ROM[c]
        n += -v if i + 1 < len(s) and ROM[s[i + 1]] > v else v
    return n


def rom(n):
    r = ''
    for v, s in ((50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += s
            n -= v
    return r


# ---------------------------------------------------------------- sermões (grego)
def sermoes():
    t = G.texto_pdf(URL_SERM, 'crisostomo-sermones-in-genesim')
    pos = [m.start() for m in re.finditer(r'ΛΟΓΟΣ [Α-ΩΔ∆ϚΣΤ]{1,2}ʹ', t)]
    assert len(pos) == 9, len(pos)
    out = {}
    for k, a in enumerate(pos):
        b = pos[k + 1] if k + 1 < len(pos) else len(t)
        out[k + 1] = (a, b)
    return t, out


def gravar_sermoes(cap, t, sec):
    quais = [n for n, cs in SERMOES.items() if cap in cs]
    if not quais:
        G.ausente(cap, f'São João Crisóstomo, Sermones in Genesim 1–9: nenhum sobre Gn {cap}.')
        return
    partes = []
    for n in quais:
        a, b = sec[n]
        partes.append(f'## Sermão {n} ({G.colunas(t, a, b, 54)})\n\n' + G.paragrafos(t[a:b]))
    campos = {
        'Autor': 'São João Crisóstomo (c. 349–407)',
        'Obra': 'Sermones in Genesim (Sermões sobre o Gênesis)',
        'Passagem': 'sermões ' + ', '.join(str(n) for n in quais),
        'Edição': 'PG 54, 581–630 («[PG 54, n]» marca a virada de coluna)',
        'Fonte': URL_SERM,
        'Cobre': {1: 'v. 1 (sermão 1); vv. 26–28 (sermões 2–4: «Façamos», a imagem e a semelhança, o domínio sobre os animais)',
                  2: 'Gn 2 (a árvore do conhecimento, o mandamento a Adão)', 3: 'Gn 3 (o castigo, as servidões)'}.get(cap, ''),
        'Oriental': 'sim',
        'Língua': 'grc',
    }
    G.gravar(cap, 'crisostomo-sermones-in-genesim', 'São João Crisóstomo, Sermones in Genesim', campos, '\n\n'.join(partes),
             'Os sermões começam com assunto do dia (Quaresma, jejum, esmola); a exegese vem depois.', SCRIPT)


# ---------------------------------------------------------------- homilias (latim da PG)
def homilias(vol):
    p = G.baixar(LAT[vol], f'ia/pg0{vol}-lat.txt', minimo=100000)
    L = G.ler(p).split('\n')
    primeira = 1 if vol == 53 else 42
    ultima = 41 if vol == 53 else 67
    inicio = next(i for i, l in enumerate(L) if re.match(r'^\s*HOMILIA (PRIMA|I)\.\s*$', l)) if vol == 53 else \
        next(i for i, l in enumerate(L) if re.match(r'^\s*HOMILIA XL[I1l]+\.\s*$', l))
    rx = re.compile(r'^[\s.\-–J]*HOMILIA\s+([IVXLCivxlc1 ]+|PRIMA)\.?\s*(?:\([a-z]\)\.?)?\s*$')
    cands = []
    for i in range(inicio, len(L)):
        m = rx.match(L[i])
        if m:
            n = 1 if m.group(1) == 'PRIMA' else romano(m.group(1))
            cands.append((i, n))
    # sequência crescente: o número lido vale se é o esperado ou um pouco adiante (homilias cujo título o OCR perdeu);
    # um número estranho vale como o esperado se o candidato seguinte é o esperado + 1
    pos, esp = {}, primeira
    for k, (i, n) in enumerate(cands):
        if esp > ultima:
            break
        prox = cands[k + 1][1] if k + 1 < len(cands) else None
        if n is not None and esp <= n <= esp + 3:
            pos[n] = i
            esp = n + 1
        elif prox == esp + 1:
            pos[esp] = i
            esp += 1
    # capítulos do Gênesis por homilia: cabeçalhos «IN CAP. I. GENES. HOMIL. III» e referências «(Gen. 1. 9)» do título
    ordem = sorted(pos.items(), key=lambda kv: kv[1])
    caps, rng = {}, {}
    for k, (h, a) in enumerate(ordem):
        b = ordem[k + 1][1] if k + 1 < len(ordem) else len(L)
        rng[h] = (a, b)
        cont = collections.Counter()
        for l in L[a:b]:
            m = re.search(r'IN CAP[.,]\s*([IVXLl1Uui]+)\.?\s*GENES', l)
            if m:
                c = romano(m.group(1))
                if c and 1 <= c <= 50:
                    cont[c] += 1
        for m in re.finditer(r'\((?:Gen|Cen|Gem)\.\s*(\d{1,2})\.', ' '.join(L[a:a + 12])):
            cont[int(m.group(1))] += 2
        caps[h] = cont
    # capítulo principal de cada homilia, sem recuar (o OCR lê «II» como «1» às vezes); os outros só com 2+ cabeçalhos
    ult = 1
    for h in sorted(caps):
        cont = caps[h]
        bons = {c: n for c, n in cont.items() if ult - 0 <= c <= ult + 3}
        princ = max(bons, key=lambda c: (bons[c], -c)) if bons else ult
        outros = {c for c, n in cont.items() if n >= 2 and abs(c - princ) <= 2 and c >= ult}
        caps[h] = sorted({princ} | outros)
        ult = princ
    return L, rng, caps, pos


def colunas_lat(L, a, b):
    """Colunas pelos cabeçalhos «25 S. JOANNIS CHRYSOSTOMI … 26»: só os números perto da mediana (o OCR lê mal muitos)."""
    ns = []
    for l in L[a:b]:
        if re.search(r'JOANNIS CHRYSOSTOMI|GENES\.\s*HOMIL', l):
            ns += [int(x) for x in re.findall(r'\b(\d{2,3})\b', l)]
    if not ns:
        return ns
    ns.sort()
    med = ns[len(ns) // 2]
    return [n for n in ns if abs(n - med) <= 12]


def limpar_lat(linhas):
    boas = [l for l in linhas if not re.search(r'JOANNIS CHRYSOSTOMI|GENES\.\s*HOMIL|^\s*\d{1,3}\s*$', l)]
    t = '\n'.join(boas)
    t = re.sub(r'-\s*\n\s*', '', t)          # palavra partida com hífen
    t = re.sub(r'\n{2,}', '\n\n', t)
    t = re.sub(r'(?<!\n)\n(?!\n)', ' ', t)
    return re.sub(r'[ \t]+', ' ', t).strip()


def gravar_homilias(cap, dados):
    partes, quais, cols_all = [], [], []
    for vol, (L, rng, caps, pos) in dados.items():
        for h in sorted(rng):
            if cap in caps[h]:
                a, b = rng[h]
                ns = colunas_lat(L, a, b)
                lo, hi = (min(ns), max(ns)) if ns else (None, None)
                ref = f'PG {vol}, {lo}–{hi}' if ns else f'PG {vol}'
                partes.append(f'## Homilia {h} ({ref}, colunas pelo OCR)\n\n' + limpar_lat(L[a:b]))
                quais.append(h)
    if not quais:
        G.ausente(cap, f'São João Crisóstomo, Homiliae in Genesim: nenhuma homilia achada para Gn {cap} (conferir a tabela).')
        return
    vols = sorted(set(53 if h <= 41 else 54 for h in quais))
    campos = {
        'Autor': 'São João Crisóstomo (c. 349–407)',
        'Obra': 'Homiliae in Genesim (67 homilias sobre o Gênesis)',
        'Passagem': 'homilias ' + ', '.join(str(h) for h in quais),
        'Edição': 'PG 53, 21–385 e PG 54, 385–580 (texto aqui: a versão latina da PG, de Montfaucon)',
        'Fonte': ' ; '.join(LAT_VER[v] for v in vols) + f' (grego: {GRC_PG53}, OCR ilegível)',
        'Cobre': 'as homilias que o cabeçalho da PG põe neste capítulo',
        'Oriental': 'sim',
        'Língua': 'la (tradução latina antiga da PG, para conferir; o original grego está na PG 53–54)',
    }
    nota = ('A khazarzar não tem as Homilias sobre o Gênesis; o OCR grego da PG 53 no archive.org é ilegível. Este arquivo traz o '
            'LATIM da PG (Montfaucon, domínio público), do OCR da edição só latina de 1859, que tem erros: para citar, traduzir do '
            'grego conferido na imagem da PG (archive.org, patrologiaecurs24migngoog, PG 53) e dar as colunas da página. '
            'Notas de rodapé de Montfaucon misturadas ao texto.')
    G.gravar(cap, 'crisostomo-homiliae-in-genesim', 'São João Crisóstomo, Homiliae in Genesim (latim da PG)', campos,
             '\n\n'.join(partes), nota, SCRIPT)


def main():
    caps_pedidos = G.capitulos()
    t, sec = sermoes()
    dados = {}
    for vol in (53, 54):
        if vol == 54 and max(caps_pedidos) < 18:
            continue
        dados[vol] = homilias(vol)
        L, rng, caps, pos = dados[vol]
        print(f'  PG {vol}: homilias achadas {sorted(rng)[0]}–{sorted(rng)[-1]} ({len(rng)})')
    for cap in caps_pedidos:
        gravar_sermoes(cap, t, sec)
        gravar_homilias(cap, dados)
        if cap in (2, 3):
            G.pista(cap, 'Pseudo-Crisóstomo, Sermo in Genesim 3 (espúrio; PG 56, 525 ss.): Quaresma, o exílio de Adão, as más mulheres. '
                    + URL_SERM3SP)
    G.registrar()


if __name__ == '__main__':
    main()
