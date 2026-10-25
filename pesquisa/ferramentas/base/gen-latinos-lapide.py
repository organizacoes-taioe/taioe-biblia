"""Cornélio a Lápide, Commentaria in Scripturam Sacram: Commentaria in Genesim (ed. Vivès, Paris, 1866, t. I), por capítulo.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-lapide.py 3-50      (ou 4, 1-11, 5 7 9)

Baixa UMA vez, para pesquisa/cache/genesis/latinos/ (fora do git), o OCR do archive.org do t. I da edição Vivès
(https://archive.org/details/commentariainscr01lapi; Princeton Theological Seminary; Gênesis e Êxodo): o texto
lapide_t1_djvu.txt (5 MB) e, para achar a folha da imagem de cada capítulo, lapide_t1_hocr_searchtext.txt.gz e
lapide_t1_hocr_pageindex.json.gz. Grava genesis/<ccc>/base/lapide-commentaria-in-genesim.md.

Como corta (no modelo de lat-lapide-num.py): cada capítulo abre com «CAPUT …» e a «SYNOPSIS CAPITIS» logo abaixo; antes do
Êxodo há exatamente 50 SYNOPSIS de capítulo (a 51.ª, «SYNOPSIS HISTORIAE ET CHRONOLOGIAE TOTIUS GENESEOS», fecha o Gn 50 e
fica de fora). O título «CAPUT …» às vezes some no OCR («CAP», «GESIMUM SEPTIMUM», «—»): o corte começa na linha não vazia
antes da SYNOPSIS, se ela tem «CAP» ou «SIMUM», senão na própria SYNOPSIS. Os cabeçalhos de página
(«238 COMMENTARIA IN GENESIM, cap. XXI.») viram «[pág. 238]» quando o número é legível e cabe na sequência; os outros
são tirados. A folha da imagem (n…) de cada capítulo é a da SYNOPSIS no texto do hOCR (as folhas não seguem as páginas:
há folhas em branco e lâminas). O OCR mistura às vezes as duas colunas, estropia «æ» e perde letras: conferir na imagem.
Gn 1 e 2: o script também os grava, se pedido; a pré-pesquisa de 25/10 rodou só 3-50.
"""
import gzip, importlib.util, json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

SCRIPT = os.path.basename(__file__)
ID = 'commentariainscr01lapi'
URL = f'https://archive.org/details/{ID}'
DL = f'https://archive.org/download/{ID}/{ID}'
PAG = URL + '/page/n{}/mode/1up'
HEAD = re.compile(r'^\W{0,3}(\d{1,3})?\W{0,3}\s*COMMENTARIA\s+IN\s+GENES\S*(.*)$', re.I)


def carregar():
    p = C.baixar(DL + '_djvu.txt', os.path.join(C.CACHE, 'lapide_t1_djvu.txt'))
    L = open(p, encoding='utf-8', errors='replace').read().split('\n')
    ps = C.baixar(DL + '_hocr_searchtext.txt.gz', os.path.join(C.CACHE, 'lapide_t1_hocr_searchtext.txt.gz'))
    pi = C.baixar(DL + '_hocr_pageindex.json.gz', os.path.join(C.CACHE, 'lapide_t1_hocr_pageindex.json.gz'))
    t = gzip.open(ps, 'rt', encoding='utf-8').read()
    idx = json.load(gzip.open(pi, 'rt'))
    return L, t, idx


def cortes(L):
    """{cap: (primeira linha, linha final exclusiva)} dos 50 capítulos."""
    ex = next(i for i, l in enumerate(L) if re.match(r'^\W*ARGUMENTUM IN EXODUM', l.strip()))
    sy = [i for i in range(ex) if re.search(r'SYNOPSIS', L[i], flags=re.I)]
    assert len(sy) == 51 and re.search(r'TOTIUS\s+GENESEOS', ' '.join(L[sy[50]:sy[50] + 12])), len(sy)
    ini = {}
    for k, i in enumerate(sy[:50], start=1):
        j = i - 1
        while j > 0 and not L[j].strip():
            j -= 1
        ini[k] = j if re.search(r'CAP|SIMUM', L[j]) else i
    fim_total = sy[50]
    while not L[fim_total - 1].strip() or len(L[fim_total - 1].strip()) < 6:   # restos de OCR antes da sinopse final
        fim_total -= 1
    return {k: (ini[k], ini[k + 1] if k < 50 else fim_total) for k in range(1, 51)}


def folhas(t, idx):
    """Folha (n do archive.org) da SYNOPSIS de cada capítulo, pelo hOCR (51 = a sinopse cronológica que fecha o Gênesis)."""
    def folha(pos):
        for i, x in enumerate(idx):
            if x[0] <= pos < x[1]:
                return i
    fs = [folha(m.start()) for m in re.finditer(r'SYNOPSIS', t, flags=re.I)]
    return {k: fs[k - 1] for k in range(1, 52)}, folha


def ancoras(L, a, b):
    """Cabeçalhos com número de página legível e crescente: [(linha, página)]."""
    anc, ult = [], 0
    for i in range(a, b):
        m = HEAD.match(L[i])
        if not m:
            continue
        ns = [m.group(1)] if m.group(1) else re.findall(r'\b(\d{2,3})\b', m.group(2))
        if ns and ns[-1]:
            n = int(ns[-1])
            if ult < n <= ult + 6 or (ult == 0 and 30 <= n <= 60):
                anc.append((i, n))
                ult = n
    return anc


def pagina(anc, linha):
    if linha <= anc[0][0]:
        return anc[0][1] - (anc[0][0] - linha) / 176
    for (i0, p0), (i1, p1) in zip(anc, anc[1:]):
        if i0 <= linha <= i1:
            return p0 + (p1 - p0) * (linha - i0) / max(1, i1 - i0)
    i0, p0 = anc[-1]
    return p0 + (linha - i0) / 176


def limpar(L, a, b, boas):
    out = []
    for i in range(a, b):
        if HEAD.match(L[i]):
            if i in boas:
                out.append(f'[pág. {boas[i]}]')
            continue
        out.append(L[i].rstrip())
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip('\n')


def rom(n):
    r = ''
    for v, s in ((50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += s
            n -= v
    return r


def main():
    caps = C.capitulos_args(__doc__)
    L, t, idx = carregar()
    cor = cortes(L)
    fol, _ = folhas(t, idx)
    anc = ancoras(L, cor[1][0] - 300, cor[50][1])
    boas = dict(anc)
    for cap in caps:
        a, b = cor[cap]
        txt = limpar(L, a, b, boas)
        pa, pb = int(pagina(anc, a)), int(pagina(anc, b))
        f1 = fol[cap]
        folhas_txt = f'folhas n{f1}–n{fol[cap + 1]}'
        C.gravar_base(
            cap, 'lapide-commentaria-in-genesim.md', 'Cornélio a Lápide, Commentaria in Genesim',
            'Cornélio a Lápide (1567–1637), jesuíta, exegeta (escritor, não canonizado)',
            'Commentaria in Scripturam Sacram: Commentaria in Pentateuchum, Genesis',
            f'Gn {cap}; Lápide, cap. {rom(cap)}',
            f'ed. Vivès (A. Crampon), Paris, 1866, t. I, pp. ~{pa}–{pb} (estimadas pelos cabeçalhos); {folhas_txt} do archive.org',
            PAG.format(f1), 'o capítulo inteiro, versículo a versículo, com o texto da Vulgata e a SYNOPSIS no começo',
            txt, SCRIPT, leitor=URL,
            nota=('OCR do archive.org (' + DL + '_djvu.txt), sem correção: mistura às vezes as duas colunas, estropia «æ» e perde '
                  'letras; conferir na imagem antes de citar. «[pág. N]» = cabeçalho de página legível. Lápide resume e cita os '
                  'Padres e os exegetas (Orígenes, Crisóstomo, Agostinho, Jerônimo, Ruperto, Tostado, Lira, Pereira): as citações '
                  'dele se conferem no original antes de entrar como dos Padres.'))


if __name__ == '__main__':
    main()
