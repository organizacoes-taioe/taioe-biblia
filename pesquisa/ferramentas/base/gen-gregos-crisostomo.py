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
    («IN CAP. I. GENES. HOMIL. III»). Para citar o grego, conferir na imagem da PG 53/54.

Homilias -> capítulos (desde 25/10, para Gn 3–50): a tabela INICIO dá o versículo do lema de cada homilia (lido no OCR e
corrigido à mão: o OCR troca números, ex. «Gen. 25. 5» por 23,5); cada homilia vai do seu lema até o versículo antes do lema
da seguinte, e entra em todos os capítulos desse trecho. Gn 1 e 2 seguem a divisão antiga (1–10 e 11–16; a 16 também vai a
Gn 3, porque comenta 2,25–3,7). Os títulos «HOMILIA XL. V.» se acham com regra frouxa e se numeram em sequência (41 na PG 53,
26 na PG 54); a edição de 1859 repete uma página (o fim da homilia 43 e o começo da 44): a primeira cópia sai.
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
# versículo do lema de cada homilia (17–67); as 1–16 ficam com a divisão antiga (CAPS_ANTIGOS)
INICIO = {17: (3, 8), 18: (3, 20), 19: (4, 8), 20: (4, 16), 21: (5, 1), 22: (5, 32), 23: (6, 9), 24: (6, 10),
          25: (7, 6), 26: (8, 1), 27: (8, 20), 28: (9, 8), 29: (9, 20), 30: (11, 1), 31: (11, 31), 32: (12, 7),
          33: (13, 2), 34: (13, 14), 35: (14, 1), 36: (15, 1), 37: (15, 7), 38: (16, 1), 39: (17, 1), 40: (17, 15),
          41: (18, 1), 42: (18, 16), 43: (19, 1), 44: (19, 27), 45: (20, 1), 46: (21, 7), 47: (22, 1), 48: (23, 5),
          49: (25, 19), 50: (25, 21), 51: (26, 1), 52: (26, 12), 53: (26, 34), 54: (27, 42), 55: (29, 15), 56: (29, 21),
          57: (30, 25), 58: (32, 1), 59: (33, 18), 60: (35, 7), 61: (37, 2), 62: (38, 2), 63: (39, 23), 64: (41, 46),
          65: (45, 25), 66: (47, 29), 67: (48, 21)}
CAPS_ANTIGOS = {h: [1] for h in range(1, 11)} | {h: [2] for h in range(11, 16)} | {16: [2, 3]}
# último versículo de cada capítulo (Vulgata/LXX: o fim do trecho de uma homilia)
FIM_CAP = {1: 31, 2: 25, 3: 24, 4: 26, 5: 32, 6: 22, 7: 24, 8: 22, 9: 29, 10: 32, 11: 32, 12: 20, 13: 18, 14: 24, 15: 21,
           16: 16, 17: 27, 18: 33, 19: 38, 20: 18, 21: 34, 22: 24, 23: 20, 24: 67, 25: 34, 26: 35, 27: 46, 28: 22,
           29: 35, 30: 43, 31: 55, 32: 32, 33: 20, 34: 31, 35: 29, 36: 43, 37: 36, 38: 30, 39: 23, 40: 23, 41: 57,
           42: 38, 43: 34, 44: 34, 45: 28, 46: 34, 47: 31, 48: 22, 49: 33, 50: 26}


def trecho(h):
    """(cap, vers) do começo e do fim do trecho da homilia h (h >= 16), pelo lema dela e o da seguinte."""
    ini = INICIO.get(h, (2, 25))
    if h == 67:
        return ini, (50, 26)
    c, v = INICIO[h + 1]
    fim = (c, v - 1) if v > 1 else (c - 1, FIM_CAP[c - 1])
    return ini, fim


def caps_da_homilia(h):
    if h in CAPS_ANTIGOS:
        return CAPS_ANTIGOS[h]
    (c0, _), (c1, _) = trecho(h)
    return list(range(c0, c1 + 1))


def trecho_txt(h):
    (c0, v0), (c1, v1) = trecho(h)
    return f'Gn {c0},{v0}–{v1}' if c0 == c1 else f'Gn {c0},{v0}–{c1},{v1}'


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
def _lema(L, i):
    """Primeiras letras do lema (a linha não vazia depois do título), para achar a página repetida."""
    for l in L[i + 1:i + 6]:
        if l.strip():
            return re.sub(r'[^a-z]', '', l.lower())[:25]
    return ''


def homilias(vol):
    p = G.baixar(LAT[vol], f'ia/pg0{vol}-lat.txt', minimo=100000)
    L = G.ler(p).split('\n')
    primeira = 1 if vol == 53 else 42
    ultima = 41 if vol == 53 else 67
    fim = next((i for i, l in enumerate(L) if 'FINIS HOMILIARUM' in l), len(L))
    # títulos: regra frouxa («HOMILIA XL. V.», «HNOMILIA XXVI.», «ROMILIA LV.», «| HOMILIA LXVII.»), numerados em sequência
    rx = re.compile(r'^[\s|.\-–J\dRP]{0,6}[HNR]N?OMILIA\s+(\S.{0,14}?)\s*$')
    cands = [i for i, l in enumerate(L[:fim]) if rx.match(l) and not re.search(r'DAVID|SAUL', l)]
    # página repetida no volume (PG 54: o fim da homilia 43 e o começo da 44 aparecem duas vezes): fica a segunda cópia,
    # e a homilia anterior termina na primeira
    lixo = []
    k = 0
    while k + 1 < len(cands):
        if _lema(L, cands[k]) and _lema(L, cands[k]) == _lema(L, cands[k + 1]):
            lixo.append((cands[k], cands[k + 1]))
            del cands[k]
        else:
            k += 1
    assert len(cands) == ultima - primeira + 1, (vol, len(cands))
    pos = {primeira + k: i for k, i in enumerate(cands)}
    caps, rng = {}, {}
    for h, a in pos.items():
        b = pos[h + 1] if h + 1 in pos else fim
        for x, y in lixo:
            if y == b:
                b = x
        rng[h] = (a, b)
        caps[h] = caps_da_homilia(h)
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
                tr = f'{trecho_txt(h)}; ' if cap >= 3 and h >= 16 else ''
                partes.append(f'## Homilia {h} ({tr}{ref}, colunas pelo OCR)\n\n' + limpar_lat(L[a:b]))
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
        'Cobre': 'as homilias que o cabeçalho da PG põe neste capítulo' if cap <= 2 else
                 '; '.join(f'hom. {h}: {trecho_txt(h)}' for h in quais) + ' (do lema de cada homilia ao da seguinte)',
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
