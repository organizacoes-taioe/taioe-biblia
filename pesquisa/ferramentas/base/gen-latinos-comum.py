"""Biblioteca comum dos scripts gen-latinos-<autor>.py (pré-pesquisa do Gênesis, Padres latinos).

Não se roda sozinha: os scripts a carregam com `importlib` (o nome tem hífens). Faz:
  - baixar uma vez (para pesquisa/cache/genesis/latinos/, fora do git) os textos do Corpus Corporum
    (https://mlat.uzh.ch, `download.php?idno=<texto>&type=file-txt`) e a Nova Vulgata do Gênesis
    (vatican.va), que dá a divisão em capítulos e versículos;
  - limpar o texto da PL com `lat_comum.limpar_pl` (marcas de coluna `[col. 225A]`, notas de Migne
    entre parênteses no próprio texto);
  - achar a que capítulo do Gênesis pertence cada parágrafo de um comentário que vai versículo a
    versículo (Beda, Ruperto, Rábano, Hugo, Alcuíno): o começo do parágrafo é comparado, por
    sequências de 4 palavras, com o texto da Vulgata; o parágrafo sem lema herda o capítulo anterior;
  - gravar genesis/<ccc>/base/<autor>-<obra>.md com o cabeçalho de COMO-PESQUISAR.md e as linhas de
    base/_ausentes-latinos.md.
"""
import datetime, html, os, re, sys, time, urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import lat_comum as L  # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))  # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'genesis', 'latinos')
GENESIS = os.environ.get('GEN_LATINOS_SAIDA') or os.path.join(RAIZ, 'genesis')  # a variável serve para testar fora da pasta
HOJE = datetime.date.today().isoformat()
UA = 'Mozilla/5.0 (pesquisa Biblia Taioe; uso gentil, 1 requisicao por vez)'
URL_NV = 'https://www.vatican.va/archive/bible/nova_vulgata/documents/nova-vulgata_vt_genesis_lt.html'
romano = L.romano


# ---------------------------------------------------------------- rede e cache
def baixar(url, destino, tentativas=4):
    if os.path.exists(destino) and os.path.getsize(destino) > 200:
        return destino
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    ult = None
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                dados = r.read()
            with open(destino, 'wb') as f:
                f.write(dados)
            time.sleep(1)
            return destino
        except Exception as e:  # noqa
            ult = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f'falhou {url}: {ult}')


def bruto(idno):
    p = baixar(f'https://mlat.uzh.ch/php_modules/download.php?idno={idno}&type=file-txt',
               os.path.join(CACHE, f'cc_{idno}.txt'))
    with open(p, encoding='utf-8') as f:
        return f.read()


def permalink(texto_bruto):
    m = re.search(r'permalink: (\S+)', texto_bruto)
    return m.group(1) if m else ''


def paragrafos(idno):
    """[{'t': texto, 'tit': bool}] do texto do Corpus Corporum, já limpo."""
    return L.limpar_pl(bruto(idno))


# ---------------------------------------------------------------- Vulgata (Nova Vulgata, divisão oficial)
def norm(s):
    s = s.lower().replace('j', 'i').replace('v', 'u').replace('æ', 'ae').replace('œ', 'oe')
    s = re.sub(r'\[col\. \w+\]', ' ', s)
    s = re.sub(r'\([^)]*\)', ' ', s)          # notas de Migne
    s = s.replace('ae', 'e').replace('oe', 'e')
    s = re.sub(r'[^a-z ]+', ' ', s)
    return s.split()


_VULG = None


def vulgata():
    """{cap: {v: texto}} do Gênesis na Nova Vulgata."""
    global _VULG
    if _VULG:
        return _VULG
    p = baixar(URL_NV, os.path.join(CACHE, 'nv-genesis.html'))
    t = open(p, encoding='utf-8', errors='replace').read()
    caps = {}
    partes = re.split(r'<a name="(\d+)">', t)
    for k in range(1, len(partes), 2):
        cap = int(partes[k])
        corpo = partes[k + 1]
        corpo = re.sub(r'^.*?</a>', '', corpo, count=1, flags=re.S)
        vs, atual = {}, None
        for linha in re.split(r'<br\s*/?>', corpo):
            linha = html.unescape(re.sub(r'<[^>]+>', ' ', linha)).replace('\xad', ' ').strip()
            if not linha:
                continue
            m = re.match(r'^(\d+)\s+(.*)$', linha)
            if m:
                atual = int(m.group(1))
                vs[atual] = m.group(2)
            elif atual:
                vs[atual] += ' ' + linha
        if vs:
            caps[cap] = vs
    _VULG = caps
    return caps


_IDX = None


def indice(n=4):
    global _IDX
    if _IDX:
        return _IDX
    idx = {}
    for cap, vs in vulgata().items():
        for v, txt in vs.items():
            w = norm(txt)
            for i in range(len(w) - n + 1):
                idx.setdefault(tuple(w[i:i + n]), set()).add((cap, v))
    _IDX = idx
    return idx


def lema(texto, n=4, palavras=30, minimo=2):
    """(cap, v) do versículo citado no começo do texto, ou None."""
    w = norm(texto)[:palavras]
    idx = indice(n)
    conta = {}
    for i in range(len(w) - n + 1):
        for cv in idx.get(tuple(w[i:i + n]), ()):
            conta[cv] = conta.get(cv, 0) + 1
    if not conta:
        return None
    melhor = max(conta.items(), key=lambda x: (x[1], -x[0][0], -x[0][1]))
    return melhor[0] if melhor[1] >= minimo else None


def atribuir(pars, ini=0, fim=None, cap0=None, salto=3):
    """Lista (cap, v) por parágrafo de pars[ini:fim]: o lema do começo, ou o do parágrafo anterior.
    Ignora lema que volte para trás ou salte mais de `salto` capítulos (citação de passagem)."""
    fim = len(pars) if fim is None else fim
    out, atual = [], (cap0, 0) if cap0 else None
    for p in pars[ini:fim]:
        cv = None if p['tit'] else lema(p['t'])
        if cv and atual:
            if cv[0] < atual[0] or cv[0] > atual[0] + salto:
                cv = None
        if cv:
            atual = cv
        out.append(atual)
    return out


# ---------------------------------------------------------------- cortes e gravação
def colunas(pars, ini, fim):
    """(primeira, última) coluna da PL de pars[ini:fim] (a primeira é a vigente no começo)."""
    a = L.col_vigente(pars, ini)
    m = L.RX_COL_INI.match(pars[ini]['t']) if ini < len(pars) else None
    if m:
        a = m.group(1)
    cols = [x.group(1) + x.group(2) for p in pars[ini:fim] for x in L.RE_COL.finditer(p['t'])]
    return (a or (cols[0] if cols else '')), (cols[-1] if cols else a)


def faixa_pl(vol, a, b):
    return f'PL {vol}, {a}' + (f'–{b}' if b and b != a else '')


def corpo(pars):
    return '\n\n'.join(('### ' + p['t']) if p['tit'] else p['t'] for p in pars)


def pasta_base(cap):
    return os.path.join(GENESIS, f'{cap:03d}', 'base')


def gravar_base(cap, arquivo, titulo, autor, obra, passagem, edicao, fonte, cobre, texto, script,
                lingua='la', leitor=None, nota=None):
    d = pasta_base(cap)
    os.makedirs(d, exist_ok=True)
    cab = [f'# {titulo}', f'- Autor: {autor}', f'- Obra: {obra}', f'- Passagem: {passagem}',
           f'- Edição: {edicao}', f'- Fonte: {fonte}', f'- Cobre: {cobre}', '- Oriental: não',
           f'- Língua: {lingua}', f'- Baixado: {HOJE}, por pesquisa/ferramentas/base/{script}']
    if leitor:
        cab.append(f'- Leitor: {leitor}')
    if nota:
        cab.append(f'- Nota: {nota}')
    txt = '\n'.join(cab) + '\n\n---\n\n' + texto.strip() + '\n'
    with open(os.path.join(d, arquivo), 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    print(f'  gravado genesis/{cap:03d}/base/{arquivo} ({len(txt.encode()) // 1024} KB)')
    return len(txt.encode('utf-8'))


def registrar_ausente(cap, rotulo, motivo):
    d = pasta_base(cap)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, '_ausentes-latinos.md')
    linhas = []
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            linhas = [x.rstrip('\n') for x in f if x.startswith('- ')]
    linhas = [x for x in linhas if not x.startswith(f'- {rotulo}:')] + [f'- {rotulo}: {motivo}']
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('# Ausentes (latinos)\n\nObras que se conferiu e que não comentam o capítulo.\n\n'
                + '\n'.join(sorted(linhas)) + '\n')


def capitulos_args(uso):
    """Lista de capítulos da linha de comando (`1`, `1-3`, `1 4 6`)."""
    caps = []
    for a in sys.argv[1:]:
        if re.fullmatch(r'\d+-\d+', a):
            x, y = map(int, a.split('-'))
            caps += list(range(x, y + 1))
        elif a.isdigit():
            caps.append(int(a))
    if not caps:
        print(uso)
        sys.exit(1)
    return caps


def por_lema(idno, ini_rx, fim_rx, caps, cfg, cap0=1):
    """Fluxo dos comentários versículo a versículo: corta pars entre os títulos ini_rx e fim_rx,
    atribui capítulos pelos lemas e grava um arquivo base/ por capítulo pedido.
    cfg: arquivo, titulo, autor, obra, pl, fonte, script, rotulo, (nota)."""
    b = bruto(idno)
    pars = L.limpar_pl(b)
    ini = next(i for i, p in enumerate(pars) if re.search(ini_rx, p['t'])) if ini_rx else 0
    fim = next((i for i, p in enumerate(pars) if i > ini and re.search(fim_rx, p['t'])), len(pars)) if fim_rx else len(pars)
    cvs = atribuir(pars, ini, fim, cap0=cap0)
    for cap in caps:
        idx = [ini + k for k, cv in enumerate(cvs) if cv and cv[0] == cap]
        if not idx:
            registrar_ausente(cap, cfg['rotulo'], 'não comenta este capítulo (nenhum lema dele na obra).')
            print(f'  Gn {cap}: nada')
            continue
        a, z = idx[0], idx[-1] + 1
        while z - 1 > a and pars[z - 1]['tit']:      # título do capítulo seguinte
            z -= 1
        while a - 1 >= ini and pars[a - 1]['tit']:   # título que abre este capítulo
            a -= 1
        trecho = pars[a:z]
        vs = sorted({cvs[k - ini][1] for k in idx if cvs[k - ini][1]})
        ca, cb = colunas(pars, a, z)
        passagem = f'Gn {cap}' + (f' (lemas dos vv. {vs[0]}–{vs[-1]})' if vs else '')
        gravar_base(cap, cfg['arquivo'], cfg['titulo'], cfg['autor'], cfg['obra'], passagem,
                    faixa_pl(cfg['pl'], ca, cb), cfg['fonte'], cfg.get('cobre', 'o capítulo, versículo a versículo'),
                    corpo(trecho), cfg['script'], leitor=permalink(b) + ' (abre a obra inteira)',
                    nota=cfg.get('nota'))


def achar(pars, rx, depois=-1):
    """Índice do primeiro parágrafo (depois de `depois`) que casa com rx; None se não houver."""
    return next((i for i, p in enumerate(pars) if i > depois and re.search(rx, p['t'])), None)


def secao(pars, ini_rx, fim_rx=None, depois=-1):
    """(ini, fim) do trecho que começa no parágrafo que casa com ini_rx e acaba antes do que casa com
    fim_rx (ou no fim do texto)."""
    a = achar(pars, ini_rx, depois)
    if a is None:
        raise KeyError(ini_rx)
    z = achar(pars, fim_rx, a) if fim_rx else None
    return a, (z if z is not None else len(pars))


def gravar_partes(cap, arquivo, meta, pars, partes, b=None):
    """Grava num só arquivo base/ vários trechos [(ini, fim, subtítulo ou None)] da mesma obra.
    meta: titulo, autor, obra, passagem, pl, fonte, script, cobre, (nota)."""
    blocos, cols = [], []
    limpas = []
    for ini, fim, sub in partes:
        while fim - 1 > ini and pars[fim - 1]['tit']:   # título do trecho seguinte
            fim -= 1
        limpas.append((ini, fim, sub))
    for ini, fim, sub in limpas:
        a, z = colunas(pars, ini, fim)
        cols.append((a, z))
        blocos.append((f'## {sub}\n\n' if sub else '') + corpo(pars[ini:fim]))
    edicao = '; '.join(faixa_pl(meta['pl'], a, z) for a, z in cols) if meta.get('pl') else meta.get('edicao', '')
    return gravar_base(cap, arquivo, meta['titulo'], meta['autor'], meta['obra'], meta['passagem'], edicao,
                       meta['fonte'], meta['cobre'], '\n\n'.join(blocos), meta['script'],
                       leitor=(permalink(b) + ' (abre a obra inteira)') if b else None, nota=meta.get('nota'))


def url_cc(idno):
    return f'https://mlat.uzh.ch/php_modules/download.php?idno={idno}&type=file-txt'
