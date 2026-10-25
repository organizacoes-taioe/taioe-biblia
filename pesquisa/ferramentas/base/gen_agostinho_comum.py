"""Biblioteca comum dos scripts gen-agostinho-*.py (pré-pesquisa do Gênesis, Santo Agostinho).

Não se roda sozinha. Os scripts `gen-agostinho-<obra>.py` a importam. Faz:
  - baixar (uma vez, para pesquisa/cache/genesis/agostinho/, fora do git) as páginas de texto do
    augustinus.it (Nuova Biblioteca Agostiniana; texto dos Maurinos = PL), uma por vez. O site recusa
    (HTTP 999) o user-agent curto: usar um de navegador. Quando cai (503), usa a cópia do Internet
    Archive (`http://web.archive.org/web/2016id_/http://www.augustinus.it/latino/...`);
  - converter o HTML em blocos: títulos (os resumos H4/H5 da NBA, que não são de Agostinho) e
    parágrafos, com a referência da âncora (`NAME="GL_001_002_004"` = livro 1, capítulo 2, parágrafo 4);
  - pôr as colunas da PL (`[col. 175]`) no texto, ancorando as marcas `-----[page 0175]-----` do texto
    da PL do Corpus Corporum (https://mlat.uzh.ch, `download.php?idno=<texto>&type=file-txt`) pelas
    palavras que as seguem (letras sem acento, j=i, v=u), sempre avançando;
  - gravar `genesis/<ccc>/base/agostinho-<obra>.md` com o cabeçalho de COMO-PESQUISAR.md.
"""
import html as _html
import os
import re
import time
import unicodedata
import urllib.request

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'genesis', 'agostinho')
HOJE = time.strftime('%Y-%m-%d')
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/130.0 Safari/537.36')
AUG = 'https://www.augustinus.it/latino/'
WAY = 'http://web.archive.org/web/2016id_/http://www.augustinus.it/latino/'

ROMANOS = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
           (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def romano(n):
    s = ''
    for v, r in ROMANOS:
        while n >= v:
            s += r
            n -= v
    return s


# ---------------------------------------------------------------- rede
def _get(url, tentativas=4):
    ult = None
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:  # noqa
            ult = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f'falhou {url}: {ult}')


def obter_aug(caminho):
    """HTML (str) de https://www.augustinus.it/latino/<caminho> (cache; cópia do Internet Archive se o site cair)."""
    p = os.path.join(CACHE, 'aug', caminho.replace('/', '_'))
    if not (os.path.exists(p) and os.path.getsize(p) > 1000):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        try:
            dados = _get(AUG + caminho, tentativas=2)
            if b'<P ALIGN' not in dados.upper():
                raise RuntimeError('página sem texto (erro do site?)')
        except Exception as e:  # noqa
            print('  augustinus.it falhou (', str(e)[:60], '): usando o web.archive.org')
            dados = _get(WAY + caminho)
        with open(p, 'wb') as f:
            f.write(dados)
        time.sleep(1.0)
    return open(p, 'rb').read().decode('cp1252', 'replace')


def obter_cc(idno):
    """Texto bruto da PL no Corpus Corporum (baixa uma vez)."""
    p = os.path.join(CACHE, 'cc', f'cc_{idno}.txt')
    if not (os.path.exists(p) and os.path.getsize(p) > 1000):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        dados = _get(f'https://mlat.uzh.ch/php_modules/download.php?idno={idno}&type=file-txt')
        with open(p, 'wb') as f:
            f.write(dados)
    return open(p, encoding='utf-8', errors='replace').read()


# ---------------------------------------------------------------- HTML -> blocos
RE_NOTA = re.compile(r'<A HREF="[^"]*_note\.htm[^"]*">.*?</A>', re.S | re.I)


def _texto(x):
    x = RE_NOTA.sub('', x)
    x = re.sub(r'<FONT SIZE=1>\s*</FONT>', '', x, flags=re.I)
    x = re.sub(r'<img[^>]*>', ' [grego] ', x, flags=re.I)
    x = re.sub(r'</I>(\s*)<I>', r'\1', x, flags=re.I)
    x = re.sub(r'<I>(.*?)</I>', lambda m: (' ' if m.group(1)[:1].isspace() else '') + '*' + m.group(1).strip() + '*'
               + (' ' if m.group(1)[-1:].isspace() else ''), x, flags=re.S | re.I)
    x = re.sub(r'<BR\s*/?>', ' ', x, flags=re.I)
    x = re.sub(r'<[^>]+>', '', x)
    x = _html.unescape(x).replace('\xa0', ' ')
    x = x.replace('**', '')
    x = re.sub(r'\s+', ' ', x).strip()
    x = re.sub(r'\*\s+([,.;:?!])', r'*\1', x)
    x = re.sub(r'(?<=[\w*»"\)])\s+([,.;:?!])(?=[\s*]|$)', r'\1', x)  # espaço deixado pela nota tirada
    x = re.sub(r'(?<=\S)\s+\*(?=[\s,.;:?!)]|$)', '*', x)
    return x


def blocos(h):
    """Lista de dicts {'tipo': 'tit'|'par', 'ref': (a, b, c) ou None, 'texto': str} do corpo da página."""
    corpo = h[h.lower().find('<body'):]
    corpo = re.sub(r'<B>\s*<FONT SIZE=2>\s*<P[^>]*>(.*?)</(?:P|H5)>', r'<H5>\1</H5>', corpo, flags=re.S | re.I)
    partes = re.split(r'(?=<P[ >])|(?=<H[345][ >])', corpo, flags=re.I)
    out = []
    for raw in partes:
        mtag = re.match(r'<(P|H[345])', raw, re.I)
        if not mtag:
            continue
        a = re.search(r'NAME="[A-Z]+_(\d+)_(\d+)_(\d+)"', raw)
        ref = tuple(int(g) for g in a.groups()) if a else None
        t = _texto(raw)
        if not t or not re.search(r'[A-Za-z]', t):
            continue
        tipo = 'tit' if mtag.group(1).upper().startswith('H') or re.match(r'<P ALIGN="?CENTER', raw, re.I) else 'par'
        out.append({'tipo': tipo, 'ref': ref, 'texto': t})
    # resumo da NBA num <P> comum (sem âncora, curto, sem número, antes de um parágrafo com âncora): é título
    for i, b in enumerate(out[:-1]):
        if (b['tipo'] == 'par' and b['ref'] is None and len(b['texto']) < 200 and not re.match(r'\d', b['texto'])
                and out[i + 1]['ref'] is not None):
            b['tipo'] = 'tit'
    # referência herdada: o parágrafo sem âncora fica com a do anterior; o título, com a do parágrafo seguinte
    atual = None
    for b in out:
        if b['ref'] is not None:
            atual = b['ref']
        b['ref_h'] = b['ref'] or atual
    prox = None
    for b in reversed(out):
        if b['tipo'] == 'tit' and b['ref'] is None:
            b['ref_h'] = prox or b['ref_h']
        elif b['ref_h'] is not None:
            prox = b['ref_h']
    return out


def rotulo(texto):
    """Tira o rótulo «5. 7.» do começo do parágrafo; devolve (rótulo, resto)."""
    m = re.match(r'^\s*(\d+)\.\s*(\d+)\.\s*', texto)
    if m:
        return f'{m.group(1)}, {m.group(2)}', texto[m.end():]
    m = re.match(r'^\s*(\d+)\.\s*', texto)
    if m:
        return m.group(1), texto[m.end():]
    return None, texto


# ---------------------------------------------------------------- colunas da PL
RE_MARCA = re.compile(r'^-{5,}\[page (\d+)([A-Za-z]?)\]-{5,}\s*$')
RE_SEP = re.compile(r'^_{20,}\s*$')


def norm(tok):
    s = unicodedata.normalize('NFD', tok.lower())
    s = ''.join(c for c in s if unicodedata.category(c)[0] == 'L')
    s = s.replace('j', 'i').replace('v', 'u').replace('æ', 'ae').replace('œ', 'oe')
    return re.sub(r'[^a-z]', '', s)


def tokens_cc(bruto):
    """(palavras normalizadas, [(posição, coluna)]) do texto da PL, sem as notas de rodapé de Migne."""
    linhas = bruto.split('\n')
    for i, l in enumerate(linhas[:40]):
        if l.startswith('#####'):
            linhas = linhas[i + 1:]
            break
    pal, marcas, notas = [], [], False
    for l in linhas:
        m = RE_MARCA.match(l)
        if m:
            marcas.append((len(pal), str(int(m.group(1))) + m.group(2)))
            notas = False
            continue
        if RE_SEP.match(l):
            notas = True
            continue
        if notas:
            continue
        for tk in l.split():
            n = norm(re.sub(r'\[\d+\]', '', tk))
            if n:
                pal.append(n)
    return pal, marcas


def _achar(seq, alvo, ini=0, fim=None):
    fim = len(seq) - len(alvo) if fim is None else min(fim, len(seq) - len(alvo))
    a0 = alvo[0]
    for j in range(max(ini, 0), fim + 1):
        if seq[j] == a0 and seq[j:j + len(alvo)] == alvo:
            return j
    return None


def localizar(cc_pal, aug_pal, de_tras=False, ini=0):
    """Posição em cc_pal do começo (ou do fim) da sequência aug_pal, tolerando erros de OCR."""
    k = 7
    n = len(aug_pal)
    for off in range(0, min(n - k, 400), 5):
        o = (n - k - off) if de_tras else off
        if o < 0:
            break
        j = _achar(cc_pal, aug_pal[o:o + k], ini)
        if j is not None:
            return (j + (n - o)) if de_tras else (j - o)
    return None


def _num(col):
    return int(re.sub(r'\D', '', col) or 0)


def colunas(sel, idno):
    """Põe `[col. N]` nos parágrafos de `sel` (lista de blocos, alterada no lugar). Devolve (col_ini, col_fim)."""
    cc_pal, cc_marcas = tokens_cc(obter_cc(idno))
    fluxo, mapa = [], []
    for ib, b in enumerate(sel):
        if b['tipo'] != 'par':
            continue
        for it, tk in enumerate(b['texto'].split(' ')):
            n = norm(tk.replace('*', ''))
            if n:
                fluxo.append(n)
                mapa.append((ib, it))
    if not fluxo:
        return None, None
    c0 = localizar(cc_pal, fluxo)
    c1 = localizar(cc_pal, fluxo, de_tras=True, ini=c0 or 0)
    if c0 is None or c1 is None:
        print('  aviso: não achei o trecho no texto da PL; sem colunas')
        return None, None
    antes = [c for p, c in cc_marcas if p <= c0]
    # sem marca antes: o trecho começa na primeira coluna da obra (a marca do Corpus vem depois do título)
    col_ini = antes[-1] if antes else (cc_marcas[0][1] if cc_marcas else None)
    depois = [c for p, c in cc_marcas if c0 < p < c0 + 60]
    if antes and depois and _num(depois[0]) < _num(antes[-1]):  # numeração que volta: vale a marca seguinte
        col_ini = depois[0]
    col_fim = col_ini
    p = 0
    insercoes = {}
    for pos, col in cc_marcas:
        if pos <= c0 or pos >= c1:
            continue
        seg = cc_pal[pos:pos + 90]
        achou = None
        for k in (5, 4, 3):
            if len(seg) < k:
                continue
            achou = _achar(fluxo, seg[:k], p, p + (6000 if k >= 4 else 800))
            if achou is not None:
                break
        if achou is None:
            # depois da marca vem um título de Migne (que o augustinus.it não tem) ou um erro de OCR: procura
            # as palavras seguintes; se as puladas estão no augustinus.it, era OCR (volta), senão era título
            for d in range(1, 80):
                alvo = seg[d:d + 5]
                if len(alvo) < 5:
                    break
                j = _achar(fluxo, alvo, p, p + 3000)
                if j is not None:
                    pul = seg[:d]
                    viz = set(fluxo[max(0, j - d - 3):j])
                    achou = j - d if sum(1 for t in pul if t in viz) >= 0.5 * d else j
                    achou = max(achou, p)
                    break
        col_fim = col
        if achou is not None:
            insercoes.setdefault(mapa[achou], []).append(col)
            p = achou
    for ib, b in enumerate(sel):
        if b['tipo'] != 'par':
            continue
        toks = b['texto'].split(' ')
        for it in range(len(toks)):
            for col in insercoes.get((ib, it), []):
                toks[it] = f'[col. {col}] ' + toks[it]
        b['texto'] = ' '.join(toks)
    return col_ini, col_fim


# ---------------------------------------------------------------- saída
def markdown(sel, rot_livro=None):
    """Blocos -> Markdown. Títulos da NBA em itálico; parágrafos com o rótulo «**cap, par.**»."""
    linhas = []
    for b in sel:
        if b['tipo'] == 'tit':
            t = b['texto'].strip('* ')
            if re.match(r'^LIBER\b', t):
                linhas.append(f'## {t}')
            else:
                linhas.append(f'_{t}_')
        else:
            r, resto = rotulo(b['texto'])
            if r and rot_livro:
                r = f'{rot_livro}, {r}'
            linhas.append(f'**{r}.** {resto}' if r else resto)
    return '\n\n'.join(linhas)


def gravar(cap, arquivo, titulo, obra, passagem, edicao, fonte, cobre, corpo, script, nota=''):
    pasta = os.path.join(RAIZ, 'genesis', f'{cap:03d}', 'base')
    os.makedirs(pasta, exist_ok=True)
    cab = [f'# {titulo}',
           '- Autor: Santo Agostinho (354–430)',
           f'- Obra: {obra}',
           f'- Passagem: {passagem}',
           f'- Edição: {edicao}',
           f'- Fonte: {fonte}',
           f'- Cobre: {cobre}',
           '- Oriental: não',
           '- Língua: la',
           f'- Baixado: {HOJE}, por pesquisa/ferramentas/base/{script}']
    if nota:
        cab.append(f'- Nota: {nota}')
    txt = '\n'.join(cab) + '\n\n---\n\n' + corpo.strip() + '\n'
    p = os.path.join(pasta, arquivo)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    print(f'  gravado {os.path.relpath(p, RAIZ)} ({len(txt) / 1024:.0f} KB)')
    return p


NOTA_PADRAO = ('Texto dos Maurinos (= PL) pelo augustinus.it; itálico (*...*) = citação bíblica; as linhas em '
               '_itálico_ entre os parágrafos são os resumos da Nuova Biblioteca Agostiniana, não de Agostinho; '
               '[col. N] = coluna da PL, ancorada pelo texto do Corpus Corporum (conferir quando importar).')


def obra_por_livros(cap, script, arquivo, titulo, obra, pasta, pagina_fmt, livros, idno, pl, cobre, passagem,
                    filtro=None, nota=NOTA_PADRAO):
    """Caso comum: uma página do augustinus.it por livro (ex. conf_11_libro.htm).

    livros: lista de números de livro; filtro(livro, ref) -> bool decide se o bloco entra (ref = (livro, cap, par)).
    """
    sel_total, fontes = [], []
    for lv in livros:
        pag = pagina_fmt.format(lv)
        bl = blocos(obter_aug(f'{pasta}/{pag}'))
        sel = [b for b in bl if filtro is None or filtro(lv, b['ref_h'] or (lv, 0, 0))]
        if not sel:
            continue
        if not sel[0]['texto'].startswith('LIBER'):
            sel.insert(0, {'tipo': 'tit', 'ref': None, 'ref_h': None, 'texto': f'LIBER {romano(lv)}'})
        fontes.append(AUG + f'{pasta}/{pag}')
        sel_total.append((lv, sel))
    cols = []
    for lv, sel in sel_total:
        a, b = colunas(sel, idno)
        cols += [c for c in (a, b) if c]
    corpo = '\n\n'.join(markdown(sel, romano(lv) if len(livros) > 1 else None) for lv, sel in sel_total)
    if cols:
        ns = [int(re.sub(r'\D', '', c)) for c in cols]
        edicao = f'{pl}, {min(ns)}–{max(ns)} (colunas deduzidas do Corpus Corporum, texto {idno})'
    else:
        edicao = pl
    return gravar(cap, arquivo, titulo, obra, passagem, edicao, ' ; '.join(fontes), cobre, corpo, script, nota)
