"""Biblioteca comum dos scripts grc-*.py (pré-pesquisa dos Padres gregos nos Salmos).

Não se executa sozinha; os scripts fazem `sys.path.insert(0, <esta pasta>)` e `import _grc`
(com `python -I` a pasta do script não entra sozinha no caminho).

O que faz:
  - baixa o PDF UMA vez para pesquisa/cache/base/grc/ (fora do git; pausa de 1 s antes de cada pedido);
  - converte com ferramentas/gregos-limpar.py para pesquisa/cache/base/grc/txt/<nome>.txt (uma vez);
  - acha o começo de cada salmo (numeração da LXX) e corta;
  - converte a numeração (hebraica -> LXX) e grava base/<autor>-<obra>.md com o cabeçalho do COMO-PESQUISAR.
"""
import os, re, subprocess, sys, time, unicodedata, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))          # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'base', 'grc')
TXT = os.path.join(CACHE, 'txt')
SALMOS = os.path.join(RAIZ, 'salmos')
LIMPAR = os.path.join(RAIZ, 'ferramentas', 'gregos-limpar.py')
KHZ = 'https://khazarzar.skeptik.net/pgm/PG_Migne/'
HOJE = '2026-10-20'
EXCLUIDOS = {33, 34, 35, 36}      # salmos hebraicos feitos à mão em outra frente


def khz(pasta, arquivo):
    """URL https exata de um PDF do khazarzar."""
    return KHZ + urllib.parse.quote(pasta) + '/' + urllib.parse.quote(arquivo)


def baixar(url, nome):
    """Baixa url para cache/base/grc/<nome> se ainda não estiver lá."""
    os.makedirs(CACHE, exist_ok=True)
    dest = os.path.join(CACHE, nome)
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return dest
    time.sleep(1)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (pesquisa Biblia Taioe)'})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest + '.tmp', 'wb') as f:
        f.write(r.read())
    os.replace(dest + '.tmp', dest)
    return dest


def texto(url, nome):
    """PDF -> texto limpo (cache). Devolve o texto."""
    pdf = baixar(url, nome + '.pdf')
    os.makedirs(TXT, exist_ok=True)
    t = os.path.join(TXT, nome + '.txt')
    if not (os.path.exists(t) and os.path.getsize(t) > 100):
        subprocess.run([sys.executable, '-I', '-X', 'utf8', LIMPAR, pdf, t], check=True,
                       stdout=subprocess.DEVNULL)
    return open(t, encoding='utf-8').read()


# ---------- numeração ----------
VAL = {'Α': 1, 'Β': 2, 'Γ': 3, 'Δ': 4, 'Ε': 5, 'Ϛ': 6, 'Ϝ': 6, 'Σ': 6, 'Ζ': 7, 'Η': 8, 'Θ': 9, 'Ι': 10, 'Κ': 20,
       'Λ': 30, 'Μ': 40, 'Ν': 50, 'Ξ': 60, 'Ο': 70, 'Π': 80, 'Ϟ': 90, 'Ϙ': 90, 'Ρ': 100}


def num_grego(s):
    """'ΛΒʹ' -> 32; 'ϛʹ' -> 6; devolve None se não for numeral."""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('ς', 'Ϛ').replace('ϛ', 'Ϛ').replace('ϟ', 'Ϟ')
    s = re.sub(r"[ʹ'’´΄\s.,·]", '', s).upper()
    if not s:
        return None
    n = 0
    for c in s:
        if c not in VAL:
            return None
        n += VAL[c]
    return n


def lxx_de_hebr(h):
    """Números LXX (lista) que correspondem ao salmo hebraico h."""
    if h <= 8 or h >= 148:
        return [h]
    if h in (9, 10):
        return [9]
    if h in (114, 115):
        return [113]
    if h == 116:
        return [114, 115]
    if h == 147:
        return [146, 147]
    return [h - 1]


def nota_numeracao(h):
    ls = lxx_de_hebr(h)
    if h == 9:
        return 'Sl 9 (hebr.) = Sl 9 (LXX); o Sl 9 e o Sl 10 do hebraico são um só (Sl 9) na LXX, e o mesmo texto serve aos dois'
    if ls == [h]:
        return f'Sl {h} (hebr. e LXX)'
    lx = ' + '.join(str(x) for x in ls)
    extra = ''
    if h in (9, 10):
        extra = '; o Sl 9 e o 10 do hebraico são um só (Sl 9) na LXX, e o mesmo texto serve aos dois'
    if h in (114, 115):
        extra = '; o Sl 114 e o 115 do hebraico são um só (Sl 113) na LXX, e o mesmo texto serve aos dois'
    if h == 116:
        extra = '; o Sl 116 do hebraico é o 114 e o 115 da LXX'
    if h == 147:
        extra = '; o Sl 147 do hebraico é o 146 e o 147 da LXX'
    return f'Sl {h} (hebr.) = Sl {lx} (LXX){extra}'


def alinhar(cands, total=150, maxgap=3, fix=None, pular_falta=False, inicio=1):
    """cands: lista [(pos, valor_ou_None, bruto)] em ordem de posição.
    Devolve (dict salmo->pos, problemas[list de str]). Segue a sequência 1..total. O OCR costuma
    perder o «ϛ» (6) e a koppa (90): «Ν ʹ» no lugar de «Νϛʹ» (56) e «Αʹ» no lugar de «ϞΑʹ» (91);
    os dois casos são aceitos. Um valor maior que o esperado em até `maxgap` vira «FALTA o salmo k»;
    qualquer outro valor estranho (OCR) é tomado pelo esperado e assinalado.
    fix: {índice do candidato (0..): salmo} para corrigir à mão o que o OCR errou.
    pular_falta: obras que não comentam todos os salmos (não lista as faltas como problema)."""
    fix = fix or {}
    res, probs = {}, []
    esperado = inicio
    for i, (pos, v, bruto) in enumerate(cands):
        if esperado > total:
            probs.append(f'sobrou cabeçalho depois do {total}: «{bruto}»')
            continue
        if i in fix:
            interp = [fix[i]]
        elif v is None:
            interp = []
        else:
            interp = [v]
            if v % 10 == 0:
                interp.append(v + 6)       # «Ν ʹ» por «Νϛʹ»
            if v < 10:
                interp.append(v + 90)      # «Αʹ» por «ϞΑʹ»
            if v == 6:
                interp.append(90)          # a koppa (90) sai como «ς»
        if esperado in interp:
            escolhido = esperado
        else:
            mais = [x for x in interp if esperado < x <= esperado + maxgap and x <= total and not (x == v + 6 and i not in fix and not re.search(r'\s\s*ʹ', bruto))]
            escolhido = min(mais) if mais else None
        if escolhido is None and v is not None and i not in fix and (max(1, esperado - 4) <= v < esperado) and not (v % 10 == 0 and re.search(r'\s\s*ʹ', bruto) and esperado <= v + 6 <= esperado + maxgap):
            probs.append(f'#{i} número «{bruto}» ({v}) repete um já visto: ignorado')
            continue
        if escolhido is None:
            probs.append(f'#{i} número «{bruto}» ({v}) no lugar do {esperado}: assumido {esperado}')
            escolhido = esperado
        elif escolhido > esperado and not pular_falta:
            for k in range(esperado, escolhido):
                probs.append(f'FALTA o cabeçalho do salmo {k}')
        res[escolhido] = pos
        esperado = escolhido + 1
    if not pular_falta:
        for k in range(esperado, total + 1):
            probs.append(f'FALTA o cabeçalho do salmo {k}')
    return res, probs


def colunas(t, ini, fim, vol=None):
    """Colunas da PG tocadas pelo trecho t[ini:fim] -> (vol, primeira, última) ou None. Se não há marcador antes do
    começo, a primeira coluna é a anterior ao primeiro marcador de dentro (o marcador vem na virada de coluna)."""
    ant = [m for m in re.finditer(r'\[PG (\d+), (\d+)\]', t[:ini])]
    dentro = list(re.finditer(r'\[PG (\d+), (\d+)\]', t[ini:fim]))
    if not dentro and not ant:
        return None
    if ant:
        a = ant[-1]
        vol0, c0 = a.group(1), int(a.group(2))
    else:
        d0 = dentro[0]
        vol0, c0 = d0.group(1), int(d0.group(2))
        if d0.start() > 12:
            c0 -= 1
    boas = [int(m.group(2)) for m in dentro if m.group(1) == vol0 and c0 - 1 <= int(m.group(2)) <= c0 + 250]
    c1 = max(boas) if boas else c0
    return (vol0, str(c0), str(c1))


def titulo_edicao(t, ini, fim, rotulo='PG'):
    c = colunas(t, ini, fim)
    if not c:
        return ''
    vol, a, b = c
    return f'{rotulo} {vol}, {a}' + ('' if a == b else f'–{b}')


def gravar_base(h, nome_arquivo, titulo, autor, obra, passagem, edicao, fonte, cobre, oriental, lingua, script,
                corpo, extra=None):
    """Grava salmos/<ccc>/base/<nome_arquivo>.md. extra: linhas adicionais depois do cabeçalho."""
    pasta = os.path.join(SALMOS, f'{h:03d}', 'base')
    os.makedirs(pasta, exist_ok=True)
    cab = [f'# {titulo}',
           f'- Autor: {autor}',
           f'- Obra: {obra}',
           f'- Passagem: {passagem}',
           f'- Edição: {edicao}',
           f'- Fonte: {fonte}',
           f'- Cobre: {cobre}',
           f'- Oriental: {oriental}',
           f'- Língua: {lingua}',
           f'- Baixado: {HOJE}, por pesquisa/ferramentas/base/{script}',
           '']
    if extra:
        cab += [extra, '']
    corpo = quebrar(corpo)
    p = os.path.join(pasta, nome_arquivo + '.md')
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(cab) + '\n' + corpo.strip() + '\n')
    return p


def quebrar(t):
    """Parágrafos: quebra de linha antes de cada marcador de versículo grego (αʹ., βʹ., ...)."""
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'(?<=[.·;:"»”]) (?=(?:[α-ωϛ]{1,3}ʹ|[α-ωϛ]{1,3}ʹ, [α-ωϛ]{1,3}ʹ)\.)', '\n\n', t)
    return t


def registrar(script, tipo, dados):
    """Guarda em cache/base/grc/<tipo>/<script>.json {hebr: [linhas]} (tipo: ausentes | pistas).
    O grc-fechar.py junta tudo em base/_ausentes-gregos.md e base/_pistas-gregos.md."""
    import json
    d = os.path.join(CACHE, tipo)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, script + '.json'), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in dados.items()}, f, ensure_ascii=False, indent=0)


def conjunto_hebr():
    return [h for h in range(1, 151) if h not in EXCLUIDOS]


AMOSTRAS = (1, 23, 50, 88, 118, 136, 150)


def produzir(script, nome_arq, titulo, autor, obra, fonte, t, starts, fim_texto=None, edicao_fn=None,
             cobre_fn=None, oriental='sim', lingua='grc', rotulo_ed='PG', fonte_fn=None, passagem_fn=None,
             extra_fn=None, nome_ausente=None, motivo_ausente=None, excluir_hebr=EXCLUIDOS, amostras=True):
    """Corta e grava. starts: {n_LXX: posição inicial}; cada trecho vai até o começo do próximo da lista
    (ou fim_texto / fim do texto). Devolve {hebr: (ini, fim)} dos gravados e a lista dos ausentes."""
    ordem = sorted(starts.items(), key=lambda kv: kv[1])
    limites = {}
    for i, (n, ini) in enumerate(ordem):
        fim = ordem[i + 1][1] if i + 1 < len(ordem) else (fim_texto or len(t))
        limites[n] = (ini, fim)
    gravados, ausentes, tamanho = {}, {}, 0
    nome_ausente = nome_ausente or f'{autor}, {obra}'
    dividido = 9.5 in limites          # o comentário divide o Sl 9 da LXX em dois blocos (Sl 9 e Sl 10 hebraicos)
    for h in conjunto_hebr():
        ls = lxx_de_hebr(h)
        pres = [n for n in ls if n in limites]
        if dividido and h == 10:
            pres = [9.5]
        if not pres:
            lx = ' e '.join(str(x) for x in ls)
            ausentes[h] = [f'- {nome_ausente}: não comenta o Sl {h} (hebr.) = Sl {lx} (LXX)'
                           + (f'; {motivo_ausente(h)}' if motivo_ausente and motivo_ausente(h) else '') + '.']
            continue
        ini, fim = limites[pres[0]][0], limites[pres[-1]][1]
        partes = [t[limites[n][0]:limites[n][1]].strip() for n in pres]
        corpo = '\n\n'.join(partes)
        ed = edicao_fn(h, pres, ini, fim) if edicao_fn else titulo_edicao(t, ini, fim, rotulo_ed)
        passagem = passagem_fn(h, pres) if passagem_fn else nota_numeracao(h)
        if dividido and h == 10:
            passagem = ('Sl 10 (hebr.) = Sl 9,22–39 (LXX), bloco «Ἵνα τί, Κύριε, ἀφέστηκας»; o Sl 9 e o Sl 10 do hebraico '
                        'são um só (Sl 9) na LXX')
        elif dividido and h == 9:
            passagem = 'Sl 9 (hebr.) = Sl 9,1–21 (LXX); o Sl 9 e o Sl 10 do hebraico são um só (Sl 9) na LXX'
        elif len(pres) < len(ls):
            passagem += f' (neste texto só o Sl {" e ".join(str(x) for x in pres)} da LXX)'
        cobre = cobre_fn(h, pres, corpo) if cobre_fn else 'o salmo inteiro'
        extra = extra_fn(h, pres) if extra_fn else None
        gravar_base(h, nome_arq, titulo, autor, obra, passagem, ed, fonte_fn(h, pres) if fonte_fn else fonte,
                    cobre, oriental, lingua, script, corpo, extra)
        gravados[h] = (ini, fim)
        tamanho += len(corpo)
    registrar(script, 'ausentes', ausentes)
    print(f'{script}: {len(gravados)} arquivos, {tamanho // 1024} KB de texto; ausentes {len(ausentes)}: '
          f'{sorted(ausentes)}')
    if amostras:
        for h in AMOSTRAS:
            if h in gravados and h not in EXCLUIDOS:
                a, b = gravados[h]
                print(f'--- Sl {h} ({b - a} car.)\n  INI: {t[a:a + 110]!r}\n  FIM: {t[b - 110:b]!r}')
    return gravados, ausentes


def semacento(t):
    """Texto sem acentos, minúsculo, ς->σ, com o MESMO comprimento (posições valem no original)."""
    cache = {}
    out = []
    for ch in t:
        r = cache.get(ch)
        if r is None:
            d = unicodedata.normalize('NFD', ch)
            d = ''.join(c for c in d if not unicodedata.combining(c)).lower().replace('ς', 'σ')
            r = d[0] if d else ' '
            cache[ch] = r
        out.append(r)
    return ''.join(out)


# ---------- o Saltério da LXX (Rahlfs 1935), só para achar onde cada salmo começa ----------
LXX_URL_TEXTO = 'https://raw.githubusercontent.com/eliranwong/LXX-Rahlfs-1935/master/01_wordlist_unicode/text_accented.csv'
LXX_URL_VERSOS = 'https://raw.githubusercontent.com/eliranwong/LXX-Rahlfs-1935/master/01_wordlist_unicode/alignment_with_OSSP/E-verse.csv'
_LXX = None


def lxx():
    """{salmo(int): {verso(int): texto}} do Saltério da LXX (Rahlfs), construído uma vez (cache).
    Serve só de régua: os cabeçalhos dos comentários às vezes faltam no PDF e o primeiro versículo
    citado marca o começo do salmo."""
    global _LXX
    if _LXX is not None:
        return _LXX
    import json
    caminho = os.path.join(CACHE, 'lxx_salmos.json')
    if not os.path.exists(caminho):
        ptxt = baixar(LXX_URL_TEXTO, 'lxx_text_accented.csv')
        pver = baixar(LXX_URL_VERSOS, 'lxx_E-verse.csv')
        palavras = {}
        for l in open(ptxt, encoding='utf-8'):
            a = l.rstrip('\n').split('\t')
            if len(a) >= 3:
                palavras[int(a[0])] = a[2]
        vs = []
        for l in open(pver, encoding='utf-8'):
            a = l.rstrip('\n').split('\t')
            m = re.search(r'「(\S+) (\d+):(\d+)', a[2])
            if m:
                vs.append((int(a[0]), m.group(1), int(m.group(2)), int(m.group(3))))
        out = {}
        for i, (s, livro, c, v) in enumerate(vs):
            if livro != 'Ps':
                continue
            e = vs[i + 1][0] if i + 1 < len(vs) else max(palavras) + 1
            out.setdefault(c, {})[v] = ' '.join(palavras[w] for w in range(s, e) if w in palavras)
        json.dump({str(c): {str(v): t for v, t in d.items()} for c, d in out.items()},
                  open(caminho, 'w', encoding='utf-8'), ensure_ascii=False)
    import json
    d = json.load(open(caminho, encoding='utf-8'))
    _LXX = {int(c): {int(v): t for v, t in vv.items()} for c, vv in d.items()}
    return _LXX


def _palavras(s):
    return re.findall(r'[α-ω]+', semacento(s))


_ANC = {}


def ancoras(n, k=4, versos=None):
    """Expressões regulares (sobre texto sem acentos): janelas de k palavras dos versículos 1 a 3 do salmo n
    que NÃO se repetem em nenhum outro lugar do Saltério (assim «ψαλμοσ τω δαυιδ ο» e as aberturas iguais,
    como «Ἐξομολογεῖσθε τῷ Κυρίῳ ὅτι χρηστός», não dão acerto falso). O título conta: pode ser tudo que o comentário cita."""
    chave = (n, k)
    if chave in _ANC:
        return _ANC[chave]
    L = lxx()
    if not hasattr(ancoras, 'cont'):
        cont = {}
        for c, vv in L.items():
            for v, txt in vv.items():
                w = _palavras(txt)
                for kk in (3, 4):
                    for i in range(len(w) - kk + 1):
                        cont.setdefault(tuple(w[i:i + kk]), set()).add(c)
        ancoras.cont = cont
    cont = ancoras.cont
    pats = []
    for v in (1, 2, 3):
        w = _palavras(L[n].get(v, ''))
        for i in range(len(w) - k + 1):
            j = tuple(w[i:i + k])
            if len(cont.get(j, ())) == 1:
                pats.append(r'\W{0,6}'.join(re.escape(x) for x in j))
    res = [re.compile(p) for p in pats]
    _ANC[chave] = res
    return res


def achar_incipit(tt, n, de, ate, k=4, versos=None):
    """Menor posição, em tt (semacento) entre de e ate, onde aparece um dos inícios do salmo n; ou None."""
    melhor = None
    for rx in ancoras(n, k, versos):
        m = rx.search(tt, de, ate)
        if m and (melhor is None or m.start() < melhor):
            melhor = m.start()
    return melhor


def avisos(probs, max=14):
    for p in probs[:max]:
        print('AVISO:', p)
    if len(probs) > max:
        print(f'AVISO: ... e mais {len(probs) - max}')


def completar(t, starts, total=150, so_estes=None, k=4, margem=400):
    """Para os salmos que faltam em starts, procura o primeiro versículo citado (régua da LXX) entre o
    começo do salmo anterior conhecido e o do seguinte. Devolve (starts novo, achados{n:pos}, nao_achados[n])."""
    tt = semacento(t)
    novo = dict(starts)
    achados, nao = {}, []
    for n in range(1, total + 1):
        if n in novo or (so_estes is not None and n not in so_estes):
            continue
        ant = max([p for m, p in novo.items() if m < n], default=0)
        dep = min([p for m, p in novo.items() if m > n], default=len(t))
        pos = achar_incipit(tt, n, ant + margem, dep, k)
        if pos is None:      # segunda tentativa: três palavras, e os versículos 1 a 4
            pos = achar_incipit(tt, n, ant + margem, dep, 3)
        if pos is None:
            nao.append(n)
        else:
            novo[n] = pos
            achados[n] = pos
    return novo, achados, nao


def recuar(t, pos, janela=300, voltar=1):
    """Recua do pos até o começo da `voltar`-ésima frase anterior (fim de frase: «. », «· », «; », «] »)."""
    pre = t[max(0, pos - janela):pos]
    ks = list(re.finditer(r'[.·;\]] ', pre))
    if len(ks) >= voltar:
        return pos - len(pre) + ks[-voltar].end()
    return pos


def verificar(t, starts, alcance=5000, so_estes=None):
    """Confere se o primeiro versículo do salmo n (régua da LXX) aparece logo depois do começo achado.
    Devolve a lista dos salmos em que NÃO aparece (para olhar à mão). Não corrige nada."""
    tt = semacento(t)
    ordem = sorted(starts.items(), key=lambda kv: kv[1])
    falhas = []
    for i, (n, p) in enumerate(ordem):
        if so_estes is not None and n not in so_estes:
            continue
        if n not in lxx():
            continue
        fim = ordem[i + 1][1] if i + 1 < len(ordem) else len(t)
        lim = min(fim, p + alcance)
        if achar_incipit(tt, n, p, lim, 4) is None and achar_incipit(tt, n, p, lim, 3) is None:
            falhas.append(n)
    return falhas


def sequencial(t, total, de=0, ate=None, margem=200, conhecidos=None, k=4):
    """Acha o começo dos salmos 1..total só pelo primeiro versículo citado (régua da LXX), em ordem: cada salmo
    é procurado depois do anterior. `conhecidos` {n: pos} (cabeçalhos seguros) valem como fixos.
    Devolve ({n: pos}, [n sem rastro])."""
    tt = semacento(t)
    ate = ate if ate is not None else len(t)
    conhecidos = conhecidos or {}
    achados, nao = dict(conhecidos), []
    ultimo = de
    for n in range(1, total + 1):
        if n in conhecidos:
            ultimo = conhecidos[n]
            continue
        dep = min([p for m, p in conhecidos.items() if m > n], default=ate)
        pos = achar_incipit(tt, n, ultimo + margem if ultimo > de else de, dep, k)
        if pos is None:
            pos = achar_incipit(tt, n, ultimo + margem if ultimo > de else de, dep, 3)
        if pos is None:
            nao.append(n)
            continue
        achados[n] = pos
        ultimo = pos
    return achados, nao


def cabeca_maiuscula(t, p, janela=360):
    """Recua de p (onde está o primeiro versículo citado) até o começo do cabeçalho em MAIÚSCULAS que o precede
    (título + número, ex.: «ΕΙΣ ΤΟ ΤΕΛΟΣ ΕΝ ΥΜΝΟΙΣ, ΤΩ ΔΑΥΙΔ Ξʹ. «»). Aceita no cabeçalho números em minúsculas
    (βʹ) e as palavras «Ἐξήγησις ψαλμοῦ»/«Ἑρμηνεία». Sem cabeçalho em maiúsculas, devolve p."""
    pre = t[max(0, p - janela):p]
    toks = list(re.finditer(r'\S+', pre))
    ini = len(pre)
    for m in reversed(toks):
        tok = m.group(0)
        w = re.sub(r'[«»"“”.,;:·()\[\]ʹ\d\-—]', '', tok)
        pgm = re.fullmatch(r'\[PG|\d+,|\d+\]', tok)
        if (w == '' or not re.search(r'[α-ω]', w) or re.fullmatch(r'[α-ωϛ]{1,3}ʹ[.,]?', tok)
                or re.fullmatch(r'(?:Ἐξήγησις|Ἑρμηνεία|ψαλμοῦ|ψαλμός)[α-ωϛ]{0,3}ʹ?[.,]?', tok)):
            ini = m.start()
            continue
        break
    return p - len(pre) + ini


def inicio_do_cabecalho(t, p):
    """Começo do trecho cujo primeiro versículo citado está em p: o cabeçalho em maiúsculas que o precede, se houver;
    senão o começo da frase."""
    q = cabeca_maiuscula(t, p)
    return q if q < p else recuar(t, p, voltar=1)


def _confere(v, n):
    if v is None:
        return False
    return v == n or (v % 10 == 0 and v + 6 == n) or (90 <= n <= 99 and v < 10 and v + 90 == n)


def refinar(t, starts, antes=2500, depois=250, rx=r'([Α-ΩϚ]{1,5}\s?ʹ)'):
    """Para cada começo achado pelo versículo, procura um cabeçalho com o número do salmo (numeral em MAIÚSCULAS com ʹ)
    entre o começo do salmo anterior e um pouco depois do ponto achado e recua até o título em maiúsculas.
    Devolve {n: novo começo}. Sem cabeçalho numerado, usa inicio_do_cabecalho()."""
    novo = {}
    ordem = sorted(starts.items(), key=lambda kv: kv[1])
    ant = 0
    for n, p in ordem:
        lo = max(ant + 100, p - antes)
        achou = None
        cand = [m for m in re.finditer(rx, t[lo:p + depois]) if _confere(num_grego(m.group(1)), n)]
        if cand:
            antes_p = [m for m in cand if lo + m.start() <= p]
            m = antes_p[-1] if antes_p else cand[0]
            achou = cabeca_maiuscula(t, lo + m.end())
            if achou <= ant:
                achou = None
        novo[n] = achou if achou is not None else inicio_do_cabecalho(t, p)
        if novo[n] <= ant:
            novo[n] = p
        ant = novo[n]
    return novo


def descobrir(t, rx_cab, total=150, inicio=1, maxgap=25, fix=None, completar_lacunas=True, bloco9b_rx=None,
              tratar=None, margem=400):
    r"""Acha o começo dos salmos de um comentário.
    rx_cab: expressão regular cujo grupo 1 é o numeral grego do cabeçalho (ex.: r'ΨΑΛΜΟΣ\s+([Α-ΩϚ]{1,5}\s?ʹ)').
    bloco9b_rx: se dado e o cabeçalho do Sl 10 aparece duas vezes seguidas, a primeira ocorrência cujo texto
      logo depois casa com esta expressão é o fim do Sl 9 da LXX (= Sl 10 hebraico) e sai da lista.
    tratar: função bruto->bruto para consertar o numeral do OCR (ex.: trocar 'S' por 'ϛ').
    Devolve dict com: starts {n: pos do cabeçalho}, achados [n achados só pelo versículo], nao [n sem rastro],
    bloco9b (pos ou None), avisos, ini {n: começo recuado ao título}."""
    cands = []
    for m in re.finditer(rx_cab, t):
        b = m.group(1)
        b2 = tratar(b) if tratar else b
        v = num_grego(b2)
        if v is not None and 1 <= v <= 150:
            cands.append((m.start(), v, b))
    bloco9b = None
    for i in range(len(cands) - 1):
        if cands[i][1] == 10 and cands[i + 1][1] == 10:
            if bloco9b_rx is None or re.search(bloco9b_rx, t[cands[i][0]:cands[i][0] + 400]):
                bloco9b = cands.pop(i)[0]
            break
    starts, probs = alinhar(cands, total=total, maxgap=maxgap, fix=fix, pular_falta=True, inicio=inicio)
    achados, nao = [], []
    if completar_lacunas:
        starts, ach, nao = completar(t, starts, total=total, margem=margem)
        achados = sorted(ach)
        nao = [n for n in nao if n >= inicio]
    ini = {}
    for n, p in starts.items():
        ini[n] = p if n not in achados else inicio_do_cabecalho(t, p)
    return dict(starts=starts, achados=achados, nao=nao, bloco9b=bloco9b, avisos=probs, ini=ini)
