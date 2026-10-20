"""Funções comuns dos scripts ori-*.py do grupo «Padres orientais gregos não clássicos» (ascetas,
Máximo, bizantinos, hinografia). Não se roda sozinho; os scripts fazem

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ori_gregos_comum as O

O que faz:
- baixar(url, nome): baixa UMA vez para pesquisa/cache/base/ori/grc/<nome> (fora do git), com pausa de 1 s.
- norm_tabela(texto) / normal(texto): texto sem acentos, minúsculo, com σ no lugar de ς; cada caractere vira
  exatamente um, então as posições do texto normalizado valem no original (busca rápida de gregos.md).
- lxx(livro): {(cap, vers): texto} da LXX (texto grego da ed. Brenton, ebible.org, domínio público), baixado
  só para buscar citações (não vai para base/). Salmos na numeração da LXX; Números na da LXX
  (16,36-50 LXX = 17,1-15 hebr.; 17,1-13 LXX = 17,16-28 hebr.).
- nt(livro, cap): {(cap, vers): texto} do NT (MorphGNT/SBLGNT do cache de grego.py), só para busca.
- buscar(alvos, arquivos, n=4): procura n-gramas dos versículos-alvo nos arquivos de texto.
- gravar(livro, ccc, arquivo, titulo, campos, corpo): grava <livro>/<ccc>/base/<arquivo>.md com o cabeçalho
  do COMO-PESQUISAR (seção «Pré-pesquisa»).
- linha_lista(livro, ccc, tipo, linha): acrescenta uma linha (sem repetir) a base/_pistas-orientais-gregos.md
  ou base/_ausentes-orientais-gregos.md.
"""
import os, re, time, unicodedata, urllib.request, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))          # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'base', 'ori', 'grc')
HOJE = '2026-10-20'
UA = 'Mozilla/5.0 (pesquisa Biblia Taioe)'
KHZ = 'https://khazarzar.skeptik.net/pgm/PG_Migne/'
_ult = [0.0]


def baixar(url, nome, minimo=500):
    os.makedirs(os.path.dirname(os.path.join(CACHE, nome)), exist_ok=True)
    dest = os.path.join(CACHE, nome)
    if os.path.exists(dest) and os.path.getsize(dest) >= minimo:
        return dest
    d = time.time() - _ult[0]
    if d < 1:
        time.sleep(1 - d)
    _ult[0] = time.time()
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=240) as r:
        dados = r.read()
    if len(dados) < minimo:
        raise RuntimeError(f'resposta curta de {url}')
    with open(dest + '.tmp', 'wb') as f:
        f.write(dados)
    os.replace(dest + '.tmp', dest)
    return dest


# ---------- normalização ----------
_TAB = {}


def _base(c):
    if c in _TAB:
        return _TAB[c]
    d = unicodedata.normalize('NFD', c)
    b = d[0].lower() if d else ' '
    if b == 'ς':
        b = 'σ'
    if not ('α' <= b <= 'ω' or 'a' <= b <= 'z'):
        b = ' '
    _TAB[c] = b
    return b


def normal(t):
    return ''.join(_base(c) for c in t)


PALAVRA = re.compile(r'[α-ωa-z]+')


def palavras(t):
    """[(palavra_normalizada, início, fim)] do texto original."""
    n = normal(t)
    return [(m.group(), m.start(), m.end()) for m in PALAVRA.finditer(n)]


VAZIAS = set('και ο η το του τησ των τω τη τον την τοισ ταισ τουσ τασ τα οι αι εν εισ εκ εξ επι προσ απο δια κατα μετα '
             'περι υπο υπερ παρα δε γαρ ουν μη ου ουκ ουχ οτι ωσ αυτοσ αυτου αυτησ αυτω αυτον αυτην αυτων αυτοισ αυτουσ '
             'μου σου μοι σοι με σε ημων υμων ημιν υμιν ημασ υμασ εγω συ τισ τι οσ ην εστι εστιν ειναι ουτοσ τουτο '
             'αλλα αλλ ινα εαν αν'.split())


# ---------- textos bíblicos (só para busca) ----------
def lxx(livro):
    """livro: 'NUM' ou 'PSA'. Devolve {(cap, vers): texto}."""
    z = baixar('https://ebible.org/Scriptures/grcbrent_usfm.zip', 'lxx/grcbrent_usfm.zip')
    nome = {'NUM': '05-NUMgrcbrent.usfm', 'PSA': '20-PSAgrcbrent.usfm'}[livro]
    with zipfile.ZipFile(z) as zf:
        t = zf.read(nome).decode('utf-8')
    out, cap = {}, 0
    for linha in t.splitlines():
        m = re.match(r'\\c (\d+)', linha)
        if m:
            cap = int(m.group(1))
            continue
        for v, txt in re.findall(r'\\v (\d+) ([^\\]*)', linha):
            out[(cap, int(v))] = txt.strip()
    return out


def nt(arquivo='68-2Co-morphgnt.txt'):
    p = os.path.join(RAIZ, 'cache', 'morphgnt', arquivo)
    out = {}
    for l in open(p, encoding='utf-8'):
        c = l.split()
        if len(c) < 4:
            continue
        ref = c[0]
        cap, v = int(ref[2:4]), int(ref[4:6])
        out.setdefault((cap, v), []).append(c[3])
    return {k: ' '.join(w) for k, w in out.items()}


def ngramas(texto, n):
    ws = [w for w, _, _ in palavras(texto)]
    for i in range(len(ws) - n + 1):
        g = tuple(ws[i:i + n])
        if all(w in VAZIAS for w in g):
            continue
        if sum(1 for w in g if w not in VAZIAS and len(w) > 3) < 2:
            continue
        yield g


def buscar(alvos, arquivos, n=4):
    """alvos: {rótulo: texto}. arquivos: [caminho]. Devolve [(arquivo, pos_ini, pos_fim, rótulo, ngrama)]."""
    idx = {}
    for rot, txt in alvos.items():
        for g in ngramas(txt, n):
            idx.setdefault(g, set()).add(rot)
    achados = []
    for arq in arquivos:
        t = open(arq, encoding='utf-8', errors='replace').read()
        ws = palavras(t)
        for i in range(len(ws) - n + 1):
            g = tuple(w for w, _, _ in ws[i:i + n])
            if g in idx:
                for rot in idx[g]:
                    achados.append((arq, ws[i][1], ws[i + n - 1][2], rot, ' '.join(g)))
    return achados


# ---------- gravação ----------
def pasta_base(livro, ccc):
    p = os.path.join(RAIZ, livro, f'{ccc:03d}', 'base')
    os.makedirs(p, exist_ok=True)
    return p


def gravar(livro, ccc, arquivo, titulo, campos, corpo):
    """campos: lista de (nome, valor) na ordem do cabeçalho."""
    linhas = [f'# {titulo}'] + [f'- {k}: {v}' for k, v in campos] + ['', corpo.strip(), '']
    p = os.path.join(pasta_base(livro, ccc), arquivo + '.md')
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(linhas))
    return p


def linha_lista(livro, ccc, tipo, linha):
    """tipo: 'pistas' ou 'ausentes'."""
    p = os.path.join(pasta_base(livro, ccc), f'_{tipo}-orientais-gregos.md')
    tit = {'pistas': '# Pistas: Padres orientais gregos (ascetas, Máximo, bizantinos, hinografia)',
           'ausentes': '# Ausentes: Padres orientais gregos (ascetas, Máximo, bizantinos, hinografia)'}[tipo]
    atual = open(p, encoding='utf-8').read().splitlines() if os.path.exists(p) else [tit, '']
    item = f'- {linha}'
    if item not in atual:
        atual.append(item)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(atual).rstrip('\n') + '\n')
    return p
