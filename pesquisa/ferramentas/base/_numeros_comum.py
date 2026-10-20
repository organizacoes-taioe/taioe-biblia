"""Funções comuns dos scripts de pré-pesquisa de Números (pesquisa/ferramentas/base/).

Não se roda sozinho; cada script de obra de Números (lat-*-num.py, grc-*-num.py, ...) o importa:

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import _numeros_comum as C

- baixar(url, nome): baixa UMA vez para pesquisa/cache/base/numeros/<nome> (fora do git), com pausa de 1 s
  entre requisições à rede e novas tentativas; devolve o caminho.
- cc_texto(idno): texto do Corpus Corporum (mlat.uzh.ch) pelo idno do texto.
- gravar(cap, arquivo, titulo, campos, corpo, nota=None): grava numeros/<ccc>/base/<arquivo>.md com o
  cabeçalho do COMO-PESQUISAR (seção «Pré-pesquisa»).
- ausente(cap, grupo, linha) / pista(cap, grupo, linha): acumulam linhas para base/_ausentes-<grupo>.md e
  base/_pistas-<grupo>.md (o script que as grava as zera antes, para poder rodar de novo).
Capítulos: os da Nova Vulgata (numeração hebraica). Os Padres usam a Vulgata de Jerônimo/LXX:
Nm 16,36-50 deles = 17,1-15 nossos; o 17 deles = 17,16-28 nossos.
"""
import os, re, sys, time, urllib.request, urllib.error

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # .../pesquisa
CACHE = os.path.join(RAIZ, 'cache', 'base', 'numeros')
NUM = os.path.join(RAIZ, 'numeros')
DATA = '2026-10-20'
CAPS = list(range(1, 12)) + [15] + list(range(17, 37))
UA = 'Mozilla/5.0 (pesquisa-biblia-taioe; contato: taioe.com.br)'
_ultimo = [0.0]


def _pausa():
    d = time.time() - _ultimo[0]
    if d < 1.0:
        time.sleep(1.0 - d)
    _ultimo[0] = time.time()


def baixar(url, nome, minimo=200, tentativas=4, timeout=240):
    """Baixa url para CACHE/nome se ainda não existir. Devolve o caminho."""
    os.makedirs(os.path.dirname(os.path.join(CACHE, nome)), exist_ok=True)
    p = os.path.join(CACHE, nome)
    if os.path.exists(p) and os.path.getsize(p) >= minimo:
        return p
    ultimo = None
    for i in range(tentativas):
        _pausa()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                dados = r.read()
            if len(dados) < minimo:
                raise RuntimeError(f'resposta curta ({len(dados)} bytes)')
            with open(p + '.parte', 'wb') as f:
                f.write(dados)
            os.replace(p + '.parte', p)
            return p
        except Exception as e:  # noqa
            ultimo = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f'falhou {url}: {ultimo}')


def ler(p, enc='utf-8'):
    with open(p, encoding=enc, errors='replace') as f:
        return f.read()


def cc_texto(idno):
    p = baixar(f'https://mlat.uzh.ch/php_modules/download.php?idno={idno}&type=file-txt', f'cc_{idno}.txt', minimo=500)
    return ler(p)


def cc_corpo(txt):
    """Tira o cabeçalho do Corpus Corporum (até a linha de #####)."""
    i = txt.find('######')
    if i >= 0:
        j = txt.find('\n', i)
        txt = txt[j + 1:]
    return txt


def cc_limpo(txt):
    """Corpo do Corpus Corporum com as marcas de coluna da PL viradas em [col. 0587A] numa linha própria
    e as notas de Migne no rodapé mantidas. Remove linhas em branco repetidas."""
    txt = cc_corpo(txt)
    txt = re.sub(r'^-{5,}\[page (\w+)\]-{5,}\s*$', lambda m: f'[col. {m.group(1)}]', txt, flags=re.M)
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    return txt.strip('\n')


def cabecalho(titulo, campos):
    ordem = ['Autor', 'Obra', 'Passagem', 'Edição', 'Fonte', 'Cobre', 'Oriental', 'Língua', 'Baixado']
    linhas = [f'# {titulo}']
    for k in ordem:
        linhas.append(f'- {k}: {campos[k]}')
    return '\n'.join(linhas)


def pasta_base(cap):
    p = os.path.join(NUM, f'{cap:03d}', 'base')
    os.makedirs(p, exist_ok=True)
    return p


def gravar(cap, arquivo, titulo, campos, corpo, nota=None):
    """campos: dict com Autor, Obra, Passagem, Edição, Fonte, Cobre, Oriental, Língua, Baixado."""
    campos = dict(campos)
    campos.setdefault('Baixado', None)
    if not campos['Baixado']:
        campos['Baixado'] = f"{DATA}, por pesquisa/ferramentas/base/{os.path.basename(sys.argv[0])}"
    txt = cabecalho(titulo, campos) + '\n\n'
    if nota:
        txt += '> ' + nota.replace('\n', '\n> ') + '\n\n'
    txt += corpo.strip('\n') + '\n'
    nome = arquivo if arquivo.endswith('.md') else arquivo + '.md'
    p = os.path.join(pasta_base(cap), nome)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    _ESCRITOS.setdefault(nome, set()).add(cap)
    return p


_ESCRITOS = {}


def finalizar():
    """Apaga os arquivos que uma rodada anterior deste script gravou e esta não gravou mais (capítulos que deixaram de ter texto).
    Chamar no fim de cada script, depois de todos os `gravar`."""
    for nome, caps in _ESCRITOS.items():
        for cap in CAPS:
            p = os.path.join(NUM, f'{cap:03d}', 'base', nome)
            if cap not in caps and os.path.exists(p):
                os.remove(p)
                print(f'  (apagado o arquivo obsoleto {cap:03d}/base/{nome})')


_extras = {}


def _extra(tipo, cap, grupo, linha):
    _extras.setdefault((tipo, cap, grupo), []).append(linha)


def ausente(cap, grupo, linha):
    _extra('ausentes', cap, grupo, linha)


def pista(cap, grupo, linha):
    _extra('pistas', cap, grupo, linha)


def gravar_extras(grupo):
    """Grava base/_ausentes-<grupo>.md e base/_pistas-<grupo>.md de todos os capítulos (sobrescreve)."""
    for tipo, tit in (('ausentes', 'Ausentes'), ('pistas', 'Pistas')):
        for cap in CAPS:
            linhas = _extras.get((tipo, cap, grupo), [])
            p = os.path.join(pasta_base(cap), f'_{tipo}-{grupo}.md')
            if linhas:
                with open(p, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(f'# {tit} ({grupo})\n\n' + '\n'.join(f'- {l}' for l in linhas) + '\n')
            elif os.path.exists(p):
                os.remove(p)


# ---------------------------------------------------------------- cortes em textos do Corpus Corporum
ROM = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def romano(s):
    s = s.upper().replace('.', '').strip()
    n = 0
    for i, c in enumerate(s):
        v = ROM[c]
        if i + 1 < len(s) and ROM[s[i + 1]] > v:
            n -= v
        else:
            n += v
    return n


def cc_linhas(idno):
    return cc_limpo(cc_texto(idno)).split('\n')


COL_RE = re.compile(r'^\[col\. (\w+)\]$')


def ultima_col(linhas, i):
    """Última marca [col. X] antes (ou na) linha i."""
    for j in range(i, -1, -1):
        m = COL_RE.match(linhas[j].strip())
        if m:
            return m.group(1)
    return None


def cortar(linhas, a, b):
    """Linhas a..b-1, com a marca de coluna em vigor no começo, sem brancos nas pontas."""
    seg = list(linhas[a:b])
    while seg and not seg[0].strip():
        seg.pop(0)
    while seg and not seg[-1].strip():
        seg.pop()
    if seg and not COL_RE.match(seg[0].strip()):
        c = ultima_col(linhas, a)
        if c:
            seg.insert(0, f'[col. {c}]')
    return '\n'.join(seg)


def colunas(texto):
    """Lista de colunas ('0587A', ...) que aparecem no texto, em ordem."""
    return [m.group(1) for m in re.finditer(r'^\[col\. (\w+)\]$', texto, flags=re.M)]


def edicao_pl(vol, texto, sigla='PL'):
    cs = colunas(texto)
    if not cs:
        return f'{sigla} {vol}'
    nums = [int(re.match(r'\d+', c).group(0)) for c in cs]
    a, b = min(nums), max(nums)
    return f'{sigla} {vol}, {a}' + (f'–{b}' if b != a else '')


def tam(texto):
    return len(texto)


DIV = {
    17: ' = Nm 16,36-50 e 17,1-13 na Vulgata de Jerônimo e nas edições antigas da LXX (a de Rahlfs já segue o hebraico)',
    25: ' (o v. 19 hebraico é o 26,1 da Vulgata)',
    26: ' (a Vulgata põe no v. 1 o que o hebraico tem em 25,19)',
    29: ' (o v. 40 da Vulgata é o 30,1 hebraico)',
    30: ' (o v. 1 hebraico é o 29,40 da Vulgata, e o 30,2 hebraico é o 30,1 dela)',
}


def cap_nm(cap):
    """Nm <cap> na numeração da Nova Vulgata (hebraica), com a divisão da Vulgata/LXX quando difere."""
    return f'Nm {cap}' + DIV.get(cap, '')


def estrutura(linhas, a, b, liber_re=r'^\s*(?:\S.*?)?LIBER (PRIMUS|SECUNDUS|TERTIUS|QUARTUS|QUINTUS)\b',
              caput_re=r'^\s*CAPUT[ -]([IVXL]+|PRIMUM)\b', livro_unico=None):
    """Texto tipo «livro I: cap. XVII (a partir do meio); livro II: caps. I–III» para as linhas a..b."""
    ords = {'PRIMUS': 'I', 'SECUNDUS': 'II', 'TERTIUS': 'III', 'QUARTUS': 'IV', 'QUINTUS': 'V'}
    liv, cap = livro_unico, None
    for k in range(0, a):
        m = re.match(liber_re, linhas[k])
        if m and livro_unico is None:
            liv = ords[m.group(1)]
        m = re.match(caput_re, linhas[k])
        if m:
            cap = m.group(1)
    grupos = []  # [livro, [caps]]
    # o corte já começa num título?
    f = a
    while f < b and not linhas[f].strip():
        f += 1
    g = f
    if g < b and re.match(liber_re, linhas[g]) and livro_unico is None:
        g += 1
        while g < b and not linhas[g].strip():
            g += 1
    comeca_em_titulo = g < b and re.match(caput_re, linhas[g]) is not None
    if cap and not comeca_em_titulo:
        grupos.append([liv, [(cap if cap != 'PRIMUM' else 'I') + ' (a partir do meio)']])
    for k in range(a, b):
        m = re.match(liber_re, linhas[k])
        if m and livro_unico is None:
            liv = ords[m.group(1)]
            if not grupos or grupos[-1][0] != liv:
                grupos.append([liv, []])
        m = re.match(caput_re, linhas[k])
        if m:
            c = 'I' if m.group(1) == 'PRIMUM' else m.group(1)
            if not grupos or grupos[-1][0] != liv:
                grupos.append([liv, []])
            grupos[-1][1].append(c)
    saida = []
    for lv, cs in grupos:
        if not cs:
            continue
        pre = (f'livro {lv}: ' if lv else '')
        saida.append(pre + ('cap. ' if len(cs) == 1 else 'caps. ') + ', '.join(cs))
    return '; '.join(saida)


# ---------------------------------------------------------------- PDFs da «Ψηφιακή Πατρολογία» (khazarzar) e do archive.org
RODAPE_KH = ('Ερευνητικό έργο', 'Χρηµατοδότηση', 'Εργαστήριο ∆ιαχείρισης', 'Πανεπιστήµιο Αιγαίου', 'Επιτρέπεται η ελεύθερη')
KHAZARZAR = 'https://khazarzar.skeptik.net/pgm/PG_Migne/'


def khazarzar_url(pasta, arquivo):
    import urllib.parse as up
    return KHAZARZAR + up.quote(pasta) + '/' + up.quote(arquivo)


def pdf_linhas(nome):
    """Linhas do PDF baixado em CACHE/nome, sem o rodapé do projeto, sem o número de página sozinho e com ∆/µ normalizados."""
    import fitz
    doc = fitz.open(os.path.join(CACHE, nome))
    out = []
    for pg in doc:
        for l in pg.get_text().split('\n'):
            s = l.replace('\xa0', ' ').strip()
            if not s:
                continue
            if any(s.startswith(r) for r in RODAPE_KH):
                continue
            if re.fullmatch(r'\d{1,4}', s):
                continue
            s = s.replace('∆', 'Δ').replace('µ', 'μ')
            import unicodedata
            out.append(unicodedata.normalize('NFC', s))
    return out


def sem_acento(s):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))


# ---------------------------------------------------------------- LXX de Números (Rahlfs 1935) para achar a que capítulo um trecho grego remete
def _norm_gr(s):
    s = sem_acento(s).lower().replace('ς', 'σ')
    return re.findall(r'[α-ω]+', s)


_LXX = {}
_OUTRO = set()  # 4-gramas que também estão em Gn, Êx, Lv ou Dt: não servem para provar que o trecho cita Números


def lxx_numeros():
    """{(cap_LXX, verso): [palavras sem acento]} de Números (Rahlfs 1935, github.com/eliranwong/LXX-Rahlfs-1935)."""
    if _LXX:
        return _LXX
    pv = baixar('https://raw.githubusercontent.com/eliranwong/LXX-Rahlfs-1935/master/01_wordlist_unicode/alignment_with_OSSP/E-verse.csv',
                'lxx_E-verse.csv', minimo=1000)
    pt = baixar('https://raw.githubusercontent.com/eliranwong/LXX-Rahlfs-1935/master/01_wordlist_unicode/text_accented.csv',
                'lxx_text_accented.csv', minimo=100000)
    palavras = {}
    for l in ler(pt).split('\n'):
        p = l.split('\t')
        if len(p) == 3:
            palavras[int(p[0])] = p[2]
    marcas = []
    for l in ler(pv).split('\n'):
        p = l.split('\t')
        if len(p) == 3:
            m = re.match(r'「(\w+) (\d+):(\d+)', p[2])
            if m:
                marcas.append((int(p[0]), m.group(1), int(m.group(2)), int(m.group(3))))
    for k, (i, liv, c, v) in enumerate(marcas):
        j = marcas[k + 1][0] if k + 1 < len(marcas) else i + 1
        if liv in ('Gen', 'Exod', 'Lev', 'Deut'):
            pal = _norm_gr(' '.join(palavras[x] for x in range(i, j) if x in palavras))
            for q in range(len(pal) - 3):
                _OUTRO.add(tuple(pal[q:q + 4]))
        if liv != 'Num':
            continue
        _LXX[(c, v)] = _norm_gr(' '.join(palavras[x] for x in range(i, j) if x in palavras))
    return _LXX


def cap_nv_de_lxx(c, v):
    """Capítulo da Nova Vulgata de um (cap, verso) da LXX/Vulgata: Vulg. 16,36-50 → 17; 17 → 17."""
    return 17 if (c == 16 and v >= 36) or c == 17 else c


_IDX = {}


def _indice_4gramas():
    if _IDX:
        return _IDX
    for (c, v), pal in lxx_numeros().items():
        cap = cap_nv_de_lxx(c, v)
        for k in range(len(pal) - 3):
            g = tuple(pal[k:k + 4])
            if g in _OUTRO:
                continue
            _IDX.setdefault(g, set()).add(cap)
    return _IDX


def pontuar(texto, minimo_comum=0):
    """{cap_NV: n.º de 4-gramas distintos do texto (sem acento) que também estão na LXX de Números nesse capítulo}.
    4-gramas que aparecem em muitos capítulos (fórmulas como «καὶ ἐλάλησε κύριος πρὸς μωυσῆν») contam para todos: filtrados
    se estiverem em mais de 5 capítulos."""
    idx = _indice_4gramas()
    pal = _norm_gr(texto)
    vistos = set()
    pont = {}
    for k in range(len(pal) - 3):
        g = tuple(pal[k:k + 4])
        if g in vistos:
            continue
        vistos.add(g)
        caps = idx.get(g)
        if caps and len(caps) <= 5:
            for c in caps:
                pont[c] = pont.get(c, 0) + 1
    return pont


# ---------------------------------------------------------------- atribuição de trechos latinos corridos a capítulos de Números
# palavras-chave por capítulo da Vulgata (latim de Clauser, de Assemani e nomes), em minúsculas, sem acento, u/v e i/j unificados
KW_LAT = {
    1: ['recensi', 'a viginti annis', 'numerat', 'tribus levi', 'primogenit'], 2: ['castrametat', 'vexill', 'signa', 'castra'],
    3: ['primogenit', 'levit', 'gerson', 'merari', 'nadab', 'abiu'], 4: ['caath', 'involv', 'ministeri', 'arca'],
    5: ['leprosum', 'zelotyp', 'adulter', 'aqua amara', 'maledict'], 6: ['nazar', 'capill', 'abstin', 'benedict'],
    7: ['plaustr', 'dedicat', 'oblationes', 'principes'], 8: ['candelabr', 'lucern', 'purific', 'viginti quinque'],
    9: ['pascha', 'secundo mense', 'nubes', 'columna'], 10: ['tubae', 'tubas', 'hobab', 'raguel', 'surge domine'],
    11: ['coturnic', 'cucumer', 'septuaginta', 'eldad', 'carnes', 'murmur'], 12: ['maria', 'aethiop', 'lepra', 'mitissim'],
    13: ['explorator', 'botrus', 'caleb', 'gigant', 'locust', 'josue'], 14: ['caleb', 'decem', 'quadraginta annos', 'amalec', 'horma'],
    15: ['ligna', 'fimbri', 'primiti', 'ignorantia', 'sabbat'], 16: ['core', 'dathan', 'abiron'],
    17: ['virga', 'virgam', 'germinav', 'amygdal', 'thuribul', 'plaga', 'florui'], 18: ['decimas', 'primitias', 'iniquitatem', 'sacerdotium'],
    19: ['vacca', 'rufa', 'cinis', 'hyssop', 'cedr', 'aspersion', 'cadaver'],
    20: ['cades', 'meriba', 'contradictionis', 'petram', 'edom', 'aaron mortu'],
    21: ['serpent', 'aeneus', 'seon', 'arnon', 'puteus', 'arad'], 22: ['balaam', 'balac', 'asina', 'angelus'],
    23: ['balaam', 'leo', 'rhinocer', 'monocer'], 24: ['balaam', 'stella', 'amalec', 'cinaeus', 'parabol'],
    25: ['phinees', 'beelphegor', 'fornicati', 'zambri', 'madianit'], 26: ['secunda numeratio', 'recensi', 'sorte'],
    27: ['salphaad', 'josue', 'abarim', 'filiae'], 28: ['holocaust', 'quotidian', 'sacrific', 'agni'],
    29: ['tubarum', 'expiati', 'scenopeg', 'festiv'], 30: ['votum', 'vota', 'juramen', 'juram'],
    31: ['madian', 'praed', 'vindict'], 32: ['ruben', 'gad', 'manasse', 'galaad'],
    33: ['mansion', 'stationes', 'ramesse'], 34: ['termin', 'finibus', 'chanaan'],
    35: ['urbes', 'civitat', 'refugi', 'homicid'], 36: ['salphaad', 'nubant', 'tribu'],
}


def norm_lat(s, longo_s=False):
    s = sem_acento(s).lower().replace('v', 'u').replace('j', 'i')
    if longo_s:
        s = s.replace('f', 's')
    return s


def atribuir_dp(textos, longo_s=False, kw=None, primeiro=None):
    """Capítulo (1..36) de cada texto de uma sequência, por programação dinâmica: o capítulo nunca recua e a soma dos pontos
    (ocorrências de palavras-chave, no máximo 4 por palavra) é a maior possível. Devolve uma lista de inteiros.
    Se `primeiro` for dado, o primeiro texto é desse capítulo."""
    kw = kw or KW_LAT
    nk = {c: [norm_lat(k, longo_s) for k in ks] for c, ks in kw.items()}
    S = []
    for t in textos:
        nt = norm_lat(t, longo_s)
        S.append([sum(min(nt.count(k), 4) for k in nk.get(c, [])) for c in range(1, 37)])
    n = len(S)
    NEG = -10 ** 9
    dp = [[NEG] * 36 for _ in range(n)]
    bp = [[0] * 36 for _ in range(n)]
    for c in range(36):
        dp[0][c] = S[0][c] if (primeiro is None or c + 1 == primeiro) else NEG
    for b in range(1, n):
        melhor, arg = NEG, 0
        for c in range(36):
            if dp[b - 1][c] - 0 > melhor:
                melhor, arg = dp[b - 1][c], c
            dp[b][c] = melhor + S[b][c]
            bp[b][c] = arg
    c = max(range(36), key=lambda x: dp[n - 1][x])
    cadeia = [0] * n
    for b in range(n - 1, -1, -1):
        cadeia[b] = c
        c = bp[b][c]
    return [x + 1 for x in cadeia]
