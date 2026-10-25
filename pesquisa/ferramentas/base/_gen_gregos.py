"""Biblioteca comum dos scripts gen-gregos-*.py (pré-pesquisa dos Padres gregos no Gênesis).

Não se roda sozinha; cada script faz:

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import _gen_gregos as G

O que oferece:
  - baixar(url, nome): baixa UMA vez para pesquisa/cache/genesis/gregos/<nome> (fora do git), com pausa de 1 s e novas tentativas;
  - texto_pdf(url, nome): baixa o PDF, converte com o pdftotext (poppler-utils), limpa (tira o rodapé da «Ψηφιακή Πατρολογία»,
    os números de página soltos, cola as palavras partidas na quebra de linha, como o gregos-limpar.py, e vira «29.325» em
    «[PG 29, 325]»), guarda o texto em cache/genesis/gregos/txt/<nome>.txt e APAGA o PDF (o /tmp e o disco são curtos);
  - gravar(cap, arquivo, titulo, campos, corpo, nota): grava genesis/<ccc>/base/<arquivo>.md com o cabeçalho do COMO-PESQUISAR;
  - ausente(cap, linha) / pista(cap, linha): acumulam linhas; registrar(script) as guarda em cache/genesis/gregos/extras/<script>.json,
    e o gen-gregos-fechar.py junta tudo em base/_ausentes-gregos.md e base/_pistas-gregos.md;
  - capitulos(argv): lê os capítulos pedidos na linha de comando («1», «1-3», «1,2,5»; padrão: 1).

O Python dos scripts é o python3 do sistema; rodar com -I (os arquivos baixados são dados, não código).
O pdftotext vem do pacote poppler-utils (no Ubuntu já instalado). O PyMuPDF (fitz) do gregos-limpar.py não é preciso.
"""
import collections, json, os, re, subprocess, sys, time, unicodedata, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))          # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'genesis', 'gregos')
GEN = os.path.join(RAIZ, 'genesis')
KHZ = 'https://khazarzar.skeptik.net/pgm/PG_Migne/'
UA = 'Mozilla/5.0 (pesquisa Biblia Taioe)'
HOJE = time.strftime('%Y-%m-%d')
_ultimo = [0.0]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def capitulos(argv=None):
    """Capítulos do Gênesis pedidos: «1», «1-3», «1,2,5». Sem argumento: [1]."""
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        return [1]
    out = []
    for parte in ','.join(argv).split(','):
        parte = parte.strip()
        if not parte:
            continue
        if '-' in parte:
            a, b = parte.split('-', 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(parte))
    return sorted(set(c for c in out if 1 <= c <= 50))


def khz(pasta, arquivo):
    """URL https exata de um PDF do khazarzar (espelho da «Ψηφιακή Πατρολογία»)."""
    return KHZ + urllib.parse.quote(pasta) + '/' + urllib.parse.quote(arquivo)


def _pausa():
    d = time.time() - _ultimo[0]
    if d < 1.0:
        time.sleep(1.0 - d)
    _ultimo[0] = time.time()


def baixar(url, nome, minimo=500, tentativas=4, timeout=300):
    """Baixa url para CACHE/nome, se ainda não estiver lá. Devolve o caminho."""
    p = os.path.join(CACHE, nome)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if os.path.exists(p) and os.path.getsize(p) >= minimo:
        return p
    erro = None
    for i in range(tentativas):
        _pausa()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=timeout) as r, open(p + '.parte', 'wb') as f:
                while True:
                    bloco = r.read(1 << 16)
                    if not bloco:
                        break
                    f.write(bloco)
            if os.path.getsize(p + '.parte') < minimo:
                raise RuntimeError('resposta curta')
            os.replace(p + '.parte', p)
            return p
        except Exception as e:  # noqa
            erro = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f'falhou {url}: {erro}')


def ler(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()


# ---------------------------------------------------------------- PDF -> texto limpo
RODAPE = ('Ερευνητικό έργο', 'Χρηµατοδότηση', 'Χρηματοδότηση', 'Εργαστήριο ∆ιαχείρισης', 'Εργαστήριο Διαχείρισης',
          'Πανεπιστήµιο Αιγαίου', 'Πανεπιστήμιο Αιγαίου', 'Επιτρέπεται η ελεύθερη')
CLITICOS = set('''ἐν εἰς ἐς ἐκ ἐξ οὐ οὐκ οὐχ ὁ ἡ οἱ αἱ ὡς εἰ μου μοι με σου σοι σε τις τι τινος τινι τινα
τινες τινων τισι τισιν τινας του τῳ που πως ποτε πω πῃ γε τε τοι περ νυν ἐστι ἐστιν εἰσι εἰσιν φημι
φησι φησιν ἐσμεν ἐστε εἰμι φασι φασιν ποθεν ποι μιν νιν'''.split())
FIM = ('αι', 'ος', 'ον', 'ων', 'ης', 'ας', 'ειν', 'ιν', 'ου', 'ους', 'ην', 'αν', 'ες', 'ως', 'ει',
       'ται', 'ναι', 'σι', 'μεν', 'τε', 'το', 'ντο', 'σαν', 'οις', 'αις', 'ις', 'ιας', 'ιαν')
APOS = "’'ʼ᾿"


def _nfd(w):
    return unicodedata.normalize('NFD', w)


def _nucleo(w):
    return unicodedata.normalize('NFC', re.sub(r'[^\ẁ-ͯ]', '', _nfd(w)))


def _tem_acento(w):
    return any(c in _nfd(w) for c in '́̀͂')


def _tem_espirito(w):
    return any(c in _nfd(w) for c in '̓̔')


def _grego_min(w):
    return bool(w) and 'α' <= _nfd(w)[0] <= 'ω'


def _fragmento(t):
    n = _nucleo(t)
    if not n or not re.match('[Ͱ-Ͽἀ-῿]', n[0]):
        return False
    d0 = _nfd(n)
    if d0[0] in 'αεηιουω' and not _tem_espirito(n[:2]) and '̈' not in d0[:3]:
        return 'vogal'
    if not _tem_acento(n) and n.lower() not in CLITICOS:
        return 'sem_acento'
    return False


def _pode(a, t):
    na, nb = _nucleo(a), _nucleo(t)
    if not (na and nb and _grego_min(nb)):
        return False
    if a[-1] in '.,;·:!)]' + APOS or any(c in a for c in APOS) or any(c in t for c in APOS):
        return False
    if not re.match(r'\w', _nfd(t)[0]) or not re.match(r'\w', _nfd(a[-1])[0]):
        return False
    return True


def juntar_palavras(txt):
    """Cola as palavras gregas partidas na quebra de linha («συγγρα φέα» -> «συγγραφέα»): a mesma heurística do
    ferramentas/gregos-limpar.py (fragmento sem acento ou que começa por vogal sem espírito; na dúvida, a junção mais
    frequente no texto). Os marcadores de coluna «29.337» que caem no meio da palavra vão para antes dela."""
    freq = collections.Counter(_nucleo(w).lower() for w in txt.split(' '))
    toks, pres, pend = [], [], []
    for w in txt.split(' '):
        if re.fullmatch(r'\d{1,3}\.\d{1,4}', w):
            pend.append(w)
            continue
        m = re.match(r'^(\d{1,3}\.\d{1,4})(\S+)$', w)
        if m:
            pend.append(m.group(1))
            w = m.group(2)
        toks.append(w)
        pres.append(pend)
        pend = []
    i, res, rpre, depois = 0, [], [], []
    while i < len(toks):
        t = toks[i]
        f = _fragmento(t)
        if f:
            prev_ok = bool(res) and _pode(res[-1], t)
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            next_ok = f == 'sem_acento' and nxt is not None and _pode(t, nxt)
            escolha = None
            if prev_ok and not next_ok:
                escolha = 'prev'
            elif next_ok and not prev_ok:
                escolha = 'next'
            elif prev_ok and next_ok:
                fp = freq[(_nucleo(res[-1]) + _nucleo(t)).lower()]
                fn = freq[(_nucleo(t) + _nucleo(nxt)).lower()]
                escolha = 'prev' if fp > fn else 'next' if fn > fp else ('prev' if _nucleo(t).endswith(FIM) else 'next')
            if escolha == 'prev':
                res[-1] = res[-1] + t
                depois.extend(pres[i])
                i += 1
                continue
            if escolha == 'next':
                toks[i + 1] = t + nxt
                pres[i + 1] = pres[i] + pres[i + 1]
                i += 1
                continue
        res.append(t)
        rpre.append(depois + pres[i])
        depois = []
        i += 1
    saida = []
    for w, ms in zip(res, rpre):
        saida.extend(ms)
        saida.append(w)
    saida.extend(depois)
    return ' '.join(saida)


def limpar(bruto, colunas_pg=True, juntar=True, colunas_nuas=None):
    """Texto do pdftotext -> texto corrido: sem rodapé, sem número de página sozinho, palavras partidas coladas,
    «29.325» -> «[PG 29, 325]» (só se colunas_pg; nos PDFs que seguem edição moderna o número não é coluna da PG).
    colunas_nuas=(vol, de, até): PDFs em que a coluna vem só como número solto no meio do texto («ἀλλοτριώ 132 σῃ»);
    os números nessa faixa que crescem em sequência viram «[PG vol, n]»."""
    boas = []
    for l in bruto.replace('\f', '\n').split('\n'):
        s = l.replace('\xa0', ' ').strip()
        if not s or any(s.startswith(r) for r in RODAPE) or re.fullmatch(r'\d{1,4}', s):
            continue
        boas.append(s)
    t = re.sub(r'\s+', ' ', ' '.join(boas))
    t = t.replace('∆', 'Δ').replace('µ', 'μ')
    t = unicodedata.normalize('NFC', t)
    if colunas_nuas:          # «ἀλλοτριώ 132 σῃ» -> «ἀλλοτριώ 44.132 σῃ» (a junção abaixo o tira de dentro da palavra)
        vol, de, ate = colunas_nuas
        colunas_pg = True
        ult = [de - 1]

        def troca(m):
            n = int(m.group(1))
            if de <= n <= ate and ult[0] < n <= ult[0] + 12:
                ult[0] = n
                return f'{vol}.{n}'
            return m.group(0)
        t = re.sub(r'(?<=\s)(\d{2,4})(?=\s)', troca, t)
    if juntar:
        t = juntar_palavras(t)
    if colunas_pg:
        t = re.sub(r'(?<![\d.,])\b(\d{1,3})\.(\d{1,4})\b(?![.,]\d)', r'[PG \1, \2]', t)
    return unicodedata.normalize('NFC', t)


def texto_pdf(url, nome, colunas_pg=True, juntar=True, colunas_nuas=None):
    """PDF da internet -> texto limpo, com cache em CACHE/txt/<nome>.txt. O PDF é apagado logo depois da conversão."""
    os.makedirs(os.path.join(CACHE, 'txt'), exist_ok=True)
    tp = os.path.join(CACHE, 'txt', nome + '.txt')
    if os.path.exists(tp) and os.path.getsize(tp) > 100:
        return ler(tp)
    pdf = baixar(url, os.path.join('pdf', nome + '.pdf'), minimo=1000)
    try:
        bruto = subprocess.run(['pdftotext', '-enc', 'UTF-8', pdf, '-'], check=True, capture_output=True).stdout.decode('utf-8', 'replace')
    finally:
        os.remove(pdf)
    t = limpar(bruto, colunas_pg=colunas_pg, juntar=juntar, colunas_nuas=colunas_nuas)
    with open(tp, 'w', encoding='utf-8') as f:
        f.write(t)
    return t


def sem_acento(s):
    """Minúsculo, sem acentos, ς->σ, MESMO comprimento (as posições valem no original)."""
    tab = {}
    out = []
    for ch in s:
        r = tab.get(ch)
        if r is None:
            d = ''.join(c for c in unicodedata.normalize('NFD', ch) if not unicodedata.combining(c)).lower().replace('ς', 'σ')
            r = d[0] if d else ' '
            tab[ch] = r
        out.append(r)
    return ''.join(out)


def colunas(t, ini, fim, vol=None):
    """Colunas da PG tocadas por t[ini:fim] -> 'PG v, a–b' (ou '' sem marcadores). Sem marcador antes, a primeira coluna
    é a anterior ao primeiro marcador de dentro (o marcador fica na virada de coluna)."""
    ant = list(re.finditer(r'\[PG (\d+), (\d+)\]', t[:ini]))
    dentro = list(re.finditer(r'\[PG (\d+), (\d+)\]', t[ini:fim]))
    if vol is not None:
        ant = [m for m in ant if m.group(1) == str(vol)]
        dentro = [m for m in dentro if m.group(1) == str(vol)]
    if not ant and not dentro:
        return ''
    if ant:
        v, c0 = ant[-1].group(1), int(ant[-1].group(2))
    else:
        v, c0 = dentro[0].group(1), int(dentro[0].group(2)) - 1
    boas = [int(m.group(2)) for m in dentro if c0 - 1 <= int(m.group(2)) <= c0 + 300]
    c1 = max(boas) if boas else c0
    return f'PG {v}, {c0}' + ('' if c1 == c0 else f'–{c1}')


# ---------------------------------------------------------------- gravação
CAMPOS = ['Autor', 'Obra', 'Passagem', 'Edição', 'Fonte', 'Cobre', 'Oriental', 'Língua', 'Baixado']
_escritos = {}


def pasta_base(cap):
    p = os.path.join(GEN, f'{cap:03d}', 'base')
    os.makedirs(p, exist_ok=True)
    return p


def paragrafos(t, largura=0):
    """Quebra o texto corrido em parágrafos antes dos números de seção («αʹ.», «1.2», «[§ 3]») e dos títulos."""
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r' (?=(?:[α-ωϛ]{1,3}ʹ\.|\d{1,2}\.\d{1,2} |\[§ |ΚΕΦΑΛΑΙΟΝ |ΟΜΙΛΙΑ |ΛΟΓΟΣ |\*\*\[))', '\n\n', t)
    return t


def gravar(cap, arquivo, titulo, campos, corpo, nota=None, script=None):
    """Grava genesis/<ccc>/base/<arquivo>.md. campos: dict com as chaves de CAMPOS (Baixado é preenchido se faltar)."""
    campos = dict(campos)
    if not campos.get('Baixado'):
        campos['Baixado'] = f'{HOJE}, por pesquisa/ferramentas/base/{script or os.path.basename(sys.argv[0])}'
    linhas = [f'# {titulo}'] + [f'- {k}: {campos[k]}' for k in CAMPOS]
    txt = '\n'.join(linhas) + '\n\n'
    if nota:
        txt += '> ' + nota.strip().replace('\n', '\n> ') + '\n\n'
    txt += corpo.strip('\n') + '\n'
    nome = arquivo if arquivo.endswith('.md') else arquivo + '.md'
    p = os.path.join(pasta_base(cap), nome)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    _escritos.setdefault(nome, set()).add(cap)
    print(f'  gravado genesis/{cap:03d}/base/{nome} ({len(corpo) // 1024 or 1} KB)')
    return p


_extras = {'ausentes': {}, 'pistas': {}}


def ausente(cap, linha):
    _extras['ausentes'].setdefault(cap, []).append(linha)


def pista(cap, linha):
    _extras['pistas'].setdefault(cap, []).append(linha)


def registrar(script=None):
    """Guarda as linhas de ausentes/pistas deste script em CACHE/extras/<script>.json (o gen-gregos-fechar.py junta)."""
    script = script or os.path.splitext(os.path.basename(sys.argv[0]))[0]
    d = os.path.join(CACHE, 'extras')
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, script + '.json')
    velho = {}
    if os.path.exists(p):
        velho = json.load(open(p, encoding='utf-8'))
    for tipo in ('ausentes', 'pistas'):
        velho.setdefault(tipo, {})
        for cap in set(capitulos()) | set(_extras[tipo]):     # os capítulos desta rodada são refeitos (vazios saem)
            linhas = _extras[tipo].get(cap, [])
            if linhas:
                velho[tipo][str(cap)] = linhas
            else:
                velho[tipo].pop(str(cap), None)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(velho, f, ensure_ascii=False, indent=1)


# ---------------------------------------------------------------- LXX do Gênesis (Rahlfs 1935), para achar o capítulo de um trecho
LXX_TEXTO = 'https://raw.githubusercontent.com/eliranwong/LXX-Rahlfs-1935/master/01_wordlist_unicode/text_accented.csv'
LXX_VERSOS = 'https://raw.githubusercontent.com/eliranwong/LXX-Rahlfs-1935/master/01_wordlist_unicode/alignment_with_OSSP/E-verse.csv'
_LXX = None


def lxx_genesis():
    """{(cap, vers): texto} do Gênesis da LXX (Rahlfs), construído uma vez (cache em CACHE/lxx_genesis.json)."""
    global _LXX
    if _LXX is not None:
        return _LXX
    cj = os.path.join(CACHE, 'lxx_genesis.json')
    if not os.path.exists(cj):
        ptxt = baixar(LXX_TEXTO, 'lxx_text_accented.csv', minimo=100000)
        pver = baixar(LXX_VERSOS, 'lxx_E-verse.csv', minimo=10000)
        vs = []
        for l in open(pver, encoding='utf-8'):
            a = l.rstrip('\n').split('\t')
            m = re.search(r'「(\S+) (\d+):(\d+)', a[2]) if len(a) > 2 else None
            if m:
                vs.append((int(a[0]), m.group(1), int(m.group(2)), int(m.group(3))))
        ini_gen = [x for x in vs if x[1] == 'Gen']
        prim, ult = ini_gen[0][0], None
        idx = vs.index(ini_gen[-1])
        ult = vs[idx + 1][0] if idx + 1 < len(vs) else None
        palavras = {}
        for l in open(ptxt, encoding='utf-8'):
            a = l.rstrip('\n').split('\t')
            if len(a) >= 3 and a[0].isdigit():
                n = int(a[0])
                if n >= prim and (ult is None or n < ult):
                    palavras[n] = a[2]
        out = {}
        for i, (s, livro, c, v) in enumerate(vs):
            if livro != 'Gen':
                continue
            e = vs[i + 1][0] if i + 1 < len(vs) else max(palavras) + 1
            out[f'{c}:{v}'] = ' '.join(palavras[w] for w in range(s, e) if w in palavras)
        with open(cj, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False)
        for nome in ('lxx_text_accented.csv', 'lxx_E-verse.csv'):
            os.remove(os.path.join(CACHE, nome))
    d = json.load(open(cj, encoding='utf-8'))
    _LXX = {tuple(int(x) for x in k.split(':')): v for k, v in d.items()}
    return _LXX


def _palavras(s):
    return re.findall(r'[α-ω]+', sem_acento(s))


_IDX = {}


def indice_gramas(k=4):
    """{tupla de k palavras: set(capítulos)} sobre a LXX do Gênesis."""
    if k in _IDX:
        return _IDX[k]
    idx = {}
    for (c, v), txt in lxx_genesis().items():
        w = _palavras(txt)
        for i in range(len(w) - k + 1):
            idx.setdefault(tuple(w[i:i + k]), set()).add(c)
    _IDX[k] = idx
    return idx


def capitulos_citados(texto, k=4, minimo=1):
    """Contagem {capítulo: nº de grupos de k palavras em comum com aquele capítulo da LXX} (grupos de um capítulo só)."""
    idx = indice_gramas(k)
    w = _palavras(texto)
    cont = collections.Counter()
    for i in range(len(w) - k + 1):
        cs = idx.get(tuple(w[i:i + k]))
        if cs and len(cs) == 1:
            cont[next(iter(cs))] += 1
    return {c: n for c, n in cont.items() if n >= minimo}
