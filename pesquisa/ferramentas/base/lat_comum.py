"""Biblioteca comum dos scripts lat-*.py (pré-pesquisa dos Salmos, autores latinos).

Não se roda sozinha. Os scripts `lat-<autor>.py` a importam. Faz:
  - baixar (uma vez, para pesquisa/cache/base/, fora do git) e ler os textos do Corpus Corporum
    (https://mlat.uzh.ch, API `download.php?idno=<texto>&type=file-txt`);
  - limpar o texto da Patrologia Latina: as marcas `-----[page 0225A]-----` viram `[col. 225A]` no
    ponto exato do texto, as notas de Migne (`[522]` no texto, `522: (Matth. V, 11)` no rodapé)
    viram parênteses no próprio texto, as linhas quebradas se juntam em parágrafos;
  - a correspondência entre a numeração hebraica (a do nosso site: pasta salmos/<ccc>) e a da
    Vulgata/LXX (a dos autores);
  - gravar `salmos/<ccc>/base/<autor>-<obra>.md` com o cabeçalho de COMO-PESQUISAR.md e
    `salmos/<ccc>/base/_ausentes-latinos.md` (uma linha por obra que não comenta o salmo).
"""
import os, re, sys, time, urllib.request, json

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'base')
SALMOS = os.path.join(RAIZ, 'salmos')
HOJE = '2026-10-20'
EXCLUIDOS = {33, 34, 35, 36}  # hebraicos já feitos ou em andamento
UA = 'Mozilla/5.0 (pesquisa Biblia Taioe; uso gentil, 1 requisicao por vez)'

ROMANOS = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
           (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def romano(n):
    s = ''
    for v, r in ROMANOS:
        while n >= v:
            s += r
            n -= v
    return s


def de_romano(s):
    s = s.upper()
    if not re.fullmatch(r'[IVXLC]+', s):
        return None
    tot, prev = 0, 0
    for ch in reversed(s):
        v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}[ch]
        tot += -v if v < prev else v
        prev = max(prev, v)
    return tot if romano(tot) == s else None


# ---------------------------------------------------------------- numeração
def vulgata_de_hebraico(h):
    """Lista dos números da Vulgata/LXX que correspondem ao salmo hebraico h."""
    if h <= 8: return [h]
    if h in (9, 10): return [9]
    if 11 <= h <= 113: return [h - 1]
    if h in (114, 115): return [113]
    if h == 116: return [114, 115]
    if 117 <= h <= 146: return [h - 1]
    if h == 147: return [146, 147]
    return [h]


def hebraicos_de_vulgata(v):
    return [h for h in range(1, 151) if v in vulgata_de_hebraico(h)]


def nota_numeracao(h):
    """Texto para o campo Passagem."""
    vs = vulgata_de_hebraico(h)
    if len(vs) == 2:
        return f'Sl {vs[0]} e {vs[1]} (Vulgata), que correspondem ao Sl {h} hebr.'
    v = vs[0]
    if h == 9:
        return 'Sl 9 (Vulgata), que reúne os Sl 9 e 10 hebr.'
    if v == h:
        return f'Sl {v} (Vulgata)'
    if h in (114, 115):
        return 'Sl 113 (Vulgata), que reúne os Sl 114 e 115 hebr.'
    if h == 10:
        return 'Sl 9 (Vulgata), que reúne os Sl 9 e 10 hebr.'
    return f'Sl {v} (Vulgata), que corresponde ao Sl {h} hebr.'


def hebraicos_alvo():
    return [h for h in range(1, 151) if h not in EXCLUIDOS]


# ---------------------------------------------------------------- rede
def baixar(url, destino, binario=False, tentativas=4, espera=1.0, codificacao=None):
    """Baixa url para destino (cache); não baixa de novo se já existe."""
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        return destino
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    ult = None
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                dados = r.read()
            with open(destino, 'wb') as f:
                f.write(dados)
            time.sleep(espera)
            return destino
        except Exception as e:  # noqa
            ult = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f'falhou {url}: {ult}')


def corpus_corporum(idno):
    """Devolve o texto bruto do Corpus Corporum (baixa uma vez)."""
    p = os.path.join(CACHE, f'cc_{idno}.txt')
    baixar(f'https://mlat.uzh.ch/php_modules/download.php?idno={idno}&type=file-txt', p)
    with open(p, encoding='utf-8') as f:
        return f.read()


def url_corpus(idno):
    return f'https://mlat.uzh.ch/php_modules/download.php?idno={idno}&type=file-txt'


# ---------------------------------------------------------------- limpeza da PL
RE_MARCA = re.compile(r'^-{5,}\[page (\d+)([A-Za-z]?)\]-{5,}\s*$')
RE_NOTA = re.compile(r'^\s+(\d+): (.*)$')
RE_REF = re.compile(r'\[(\d+)\]')
RE_SEP = re.compile(r'^_{20,}\s*$')


def limpar_pl(bruto):
    """Texto bruto do Corpus Corporum -> lista de parágrafos (strings) com `[col. 225A]` inline.

    Cada parágrafo é um dict: {'t': texto, 'tit': True se for título (linha recuada)}.
    """
    linhas = bruto.split('\n')
    # tira o cabeçalho do download (até a linha de #####)
    for i, l in enumerate(linhas[:40]):
        if l.startswith('#####'):
            linhas = linhas[i + 1:]
            break
    # 1) separa em eventos: marca, bloco de notas, linha de texto
    eventos = []  # ('m', col) | ('n', {num: texto}) | ('l', linha)
    i = 0
    while i < len(linhas):
        l = linhas[i].rstrip('\r')
        m = RE_MARCA.match(l)
        if m:
            eventos.append(('m', str(int(m.group(1))) + m.group(2)))
            i += 1
            continue
        if RE_SEP.match(l):
            notas, ult = {}, None
            i += 1
            while i < len(linhas):
                l2 = linhas[i].rstrip('\r')
                if RE_MARCA.match(l2):
                    break
                mn = RE_NOTA.match(l2)
                if mn and (ult is None or True):
                    ult = int(mn.group(1))
                    notas[ult] = mn.group(2).strip()
                elif l2.strip() == '':
                    # linha em branco dentro do bloco: pode acabar o bloco de notas
                    j = i + 1
                    while j < len(linhas) and linhas[j].strip() == '':
                        j += 1
                    if j < len(linhas) and (RE_MARCA.match(linhas[j].rstrip('\r')) or RE_NOTA.match(linhas[j].rstrip('\r'))):
                        i += 1
                        continue
                    break
                elif ult is not None:
                    notas[ult] += ' ' + l2.strip()
                else:
                    break
                i += 1
            eventos.append(('n', notas))
            continue
        eventos.append(('l', l))
        i += 1
    # 2) resolve as referências [N] com as notas do bloco mais próximo (o do mesmo trecho)
    #    Os blocos de notas vêm no fim do trecho; as referências estão no trecho anterior ao bloco.
    #    Estratégia: percorre; guarda o índice das linhas de texto desde o último bloco de notas;
    #    ao chegar num bloco, substitui nelas.
    saida = []  # itens: ('m', col) | ('l', linha)
    pendentes = []  # posições em `saida` das linhas de texto desde o último bloco de notas
    ultimas = {}
    for ev in eventos:
        if ev[0] == 'l':
            saida.append(['l', ev[1]])
            pendentes.append(len(saida) - 1)
        elif ev[0] == 'm':
            saida.append(['m', ev[1]])
        else:
            notas = ev[1]
            ultimas.update(notas)
            for pos in pendentes:
                saida[pos][1] = RE_REF.sub(lambda m: _nota(notas, m), saida[pos][1])
            pendentes = []
    for pos in pendentes:  # sobras sem bloco de notas
        saida[pos][1] = RE_REF.sub(lambda m: _nota(ultimas, m), saida[pos][1])
    return _paragrafos(saida)


def _nota(notas, m):
    n = int(m.group(1))
    t = notas.get(n)
    if t is None or not t.strip():
        return ''  # nota ausente: só garante o espaço (limpo depois em _paragrafos)
    t = t.strip()
    if not (t.startswith('(') and t.endswith(')')):
        t = '(' + t + ')'
    return ' ' + t


FIM_FRASE = re.compile(r'[.?!:;»"\)\]]$')


def _paragrafos(saida):
    """Junta as linhas em parágrafos e põe as marcas de coluna no ponto certo."""
    pars, atual = [], []
    marca = None
    prev_vazia = False
    prev_sem_espaco = False
    interveio = False

    def fecha():
        nonlocal atual
        if atual:
            t = ' '.join(x.strip() for x in atual)
            t = re.sub(r'(?=[.,;:?!)»\]])', '', t).replace('', ' ')
            t = re.sub(r'[ 	]+', ' ', t).strip()
            pars.append({'t': t, 'tit': False})
        atual = []

    for tipo, v in saida:
        if tipo == 'm':
            marca = v
            interveio = True
            continue
        l = v
        if l.strip() == '':
            prev_vazia = True
            continue
        recuada = bool(re.match(r'^( {4,}|	)\S', l))
        texto = l.strip() if recuada else l
        if marca:
            texto = f'[col. {marca}] ' + texto.lstrip()
            marca = None
        if recuada and l.endswith(' '):
            # primeira linha recuada de um parágrafo que continua nas linhas seguintes
            fecha()
            atual.append(texto)
            prev_vazia = interveio = False
            prev_sem_espaco = False
            continue
        if recuada:
            fecha()
            pars.append({'t': texto.strip(), 'tit': True})
            prev_vazia = prev_sem_espaco = interveio = False
            continue
        ultimo = atual[-1].rstrip() if atual else ''
        quebra = False
        if atual:
            sem_col = re.sub(r'^\[col\. [0-9A-Za-z]+\] ', '', texto.lstrip())
            if prev_vazia and FIM_FRASE.search(ultimo):
                quebra = True
            elif (prev_sem_espaco and not interveio and FIM_FRASE.search(ultimo)
                  and ultimo[-1] not in ':;' and re.match(r'[A-Z0-9"«(\[]', sem_col)):
                quebra = True
        if quebra:
            fecha()
        atual.append(texto)
        prev_vazia = False
        interveio = False
        prev_sem_espaco = not l.endswith(' ')
    fecha()
    return pars


RE_COL = re.compile(r'\[col\. (\d+)([A-Za-z]?)\]')


def faixa_colunas(pars, col_antes):
    """(primeira, ultima) coluna: a em vigor no começo (col_antes) e a última marcada no trecho."""
    cols = []
    for p in pars:
        cols += [m.group(1) + m.group(2) for m in RE_COL.finditer(p['t'])]
    ini = col_antes or (cols[0] if cols else '')
    fim = cols[-1] if cols else ini
    return ini, fim


def col_vigente(pars, idx):
    """Coluna em vigor no começo do parágrafo idx (última marca nos parágrafos anteriores)."""
    for j in range(idx - 1, -1, -1):
        ms = RE_COL.findall(pars[j]['t'])
        if ms:
            return ms[-1][0] + ms[-1][1]
    return ''


def texto_de(pars):
    out = []
    for p in pars:
        out.append(('**' + p['t'] + '**') if False else p['t'])
    return '\n\n'.join(out)


# ---------------------------------------------------------------- gravação
def pasta_base(h):
    return os.path.join(SALMOS, f'{h:03d}', 'base')


def gravar_base(h, nome_arquivo, titulo, autor, obra, passagem, edicao, fonte, cobre, corpo,
                script, lingua='la', oriental='não', nota=None, leitor=None):
    d = pasta_base(h)
    os.makedirs(d, exist_ok=True)
    cab = [f'# {titulo}',
           f'- Autor: {autor}',
           f'- Obra: {obra}',
           f'- Passagem: {passagem}',
           f'- Edição: {edicao}',
           f'- Fonte: {fonte}',
           f'- Cobre: {cobre}',
           f'- Oriental: {oriental}',
           f'- Língua: {lingua}',
           f'- Baixado: {HOJE}, por pesquisa/ferramentas/base/{script}']
    if leitor:
        cab.append(f'- Leitor: {leitor}')
    if nota:
        cab.append(f'- Nota: {nota}')
    txt = '\n'.join(cab) + '\n\n---\n\n' + corpo.strip() + '\n'
    with open(os.path.join(d, nome_arquivo), 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    return len(txt.encode('utf-8'))


def registrar_ausente(h, obra_rotulo, motivo='não comentou este salmo.', script=None):
    """Acrescenta (sem duplicar) uma linha em _ausentes-latinos.md."""
    d = pasta_base(h)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, '_ausentes-latinos.md')
    linha = f'- {obra_rotulo}: {motivo}'
    existentes = []
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            existentes = [x.rstrip('\n') for x in f if x.startswith('- ')]
    # tira linha antiga da mesma obra
    existentes = [x for x in existentes if not x.startswith(f'- {obra_rotulo}:')]
    existentes.append(linha)
    existentes.sort()
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(existentes) + '\n')


def limpar_ausente(h, obra_rotulo):
    p = os.path.join(pasta_base(h), '_ausentes-latinos.md')
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            ex = [x.rstrip('\n') for x in f if x.startswith('- ') and not x.startswith(f'- {obra_rotulo}:')]
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(('\n'.join(ex) + '\n') if ex else '')
        if not ex:
            os.remove(p)


def corpo_de_salmos(h, por_vulgata, func_fmt=None):
    """por_vulgata: {n_vulgata: texto}. Devolve o corpo para o hebraico h (subtítulos se vários)."""
    vs = vulgata_de_hebraico(h)
    if len(vs) == 1:
        return por_vulgata[vs[0]]
    return '\n\n'.join(f'## Salmo {v} (Vulgata)\n\n{por_vulgata[v]}' for v in vs if v in por_vulgata)




# ---------------------------------------------------------------- corte por salmo (PL)
RX_TITULO = re.compile(
    r'^(?:\[col\. \w+\] )?(?:\d+ )?(?:EXPOSITIO IN |TRACTATUS IN |TRACT\. )?(?:IN )?'
    r'PSALM(?:US|UM|I)\.?\s+([IVXLC]+|PRIM(?:US|UM)|SECUND(?:US|UM))\b')
RX_COL_INI = re.compile(r'^\[col\. (\d+[A-Za-z]?)\]')
ORDINAIS = {'PRIMUS': 1, 'PRIMUM': 1, 'SECUNDUS': 2, 'SECUNDUM': 2}


def _n(s):
    return ORDINAIS.get(s) or de_romano(s)


def achar_titulos(pars, extras=(), overrides=None, rx=RX_TITULO):
    """[(indice, n_vulgata)] em ordem. extras: [(regex, n|None)] (n None: o grupo 1 é o romano).
    overrides: {prefixo_do_texto: n} para corrigir erros de numeração do original."""
    out = []
    for i, p in enumerate(pars):
        t = p['t']
        n = None
        if overrides:
            for pref, nn in overrides.items():
                if t.startswith(pref):
                    n = nn
        if n is None:
            m = rx.match(t)
            if m:
                n = _n(m.group(1))
        if n is None:
            for r, nn in extras:
                m = re.match(r, t)
                if m:
                    n = nn if nn is not None else _n(m.group(1))
                    break
        if n is not None:
            out.append((i, n))
    # conserta repetição seguida de salto (115, 115, 117 -> 115, 116, 117)
    for k in range(1, len(out) - 1):
        if out[k][1] == out[k - 1][1] and out[k + 1][1] == out[k][1] + 2:
            out[k] = (out[k][0], out[k][1] + 1)
    return out


def cortar(pars, titulos, fim, aparar=None, extras_secao=()):
    """Devolve {n: [paragrafos]} cortando entre títulos. fim = índice onde termina o último.
    aparar: regex dos parágrafos-título a tirar do fim de cada trecho (ex.: «PARS SECUNDA»).
    extras_secao: [(inicio, fim, n, rotulo)] trechos acrescentados ao salmo n."""
    secoes, ordem = {}, []
    k = 0
    while k < len(titulos):
        i, n = titulos[k]
        j = k + 1
        while j < len(titulos) and titulos[j][1] == n:
            j += 1
        ate = titulos[j][0] if j < len(titulos) else fim
        if n in secoes:
            print(f'  aviso: salmo {n} repetido (idx {i}); ignorando o repetido')
        else:
            trecho = pars[i:ate]
            while aparar and trecho and trecho[-1]['tit'] and re.match(aparar, trecho[-1]['t']):
                trecho = trecho[:-1]
            secoes[n] = (i, trecho)
            ordem.append(n)
        k = j
    for ini, ate, n, rot in extras_secao:
        trecho = [{'t': rot, 'tit': True, 'sub': True}] + pars[ini:ate]
        if n in secoes:
            secoes[n] = (secoes[n][0], secoes[n][1] + trecho)
        else:
            secoes[n] = (ini, trecho)
    # sanidade: ordem estritamente crescente
    for a, b in zip(ordem, ordem[1:]):
        if b <= a:
            print(f'  AVISO: ordem quebrada {a} -> {b}')
    return secoes


def executar_pl(cfg, pars, secoes, so_hebraicos=None):
    """Grava os arquivos base/ e os _ausentes para todos os hebraicos alvo. Devolve (n_arquivos, bytes, lista)."""
    n_arq, tot, feitos = 0, 0, []
    for h in hebraicos_alvo():
        if so_hebraicos and h not in so_hebraicos:
            continue
        vs = vulgata_de_hebraico(h)
        tem = [v for v in vs if v in secoes]
        if not tem:
            if cfg.get('sem_ausente'):
                continue
            registrar_ausente(h, cfg['rotulo'], cfg.get('motivo_ausente', 'não comentou este salmo.'))
            continue
        limpar_ausente(h, cfg['rotulo'])
        blocos, ini_cols, fim_cols = [], [], []
        for v in tem:
            i0, trecho = secoes[v]
            col0 = None
            if trecho:
                m = RX_COL_INI.match(trecho[0]['t'])
                col0 = m.group(1) if m else col_vigente(pars, i0)
            a, b = faixa_colunas(trecho, col0)
            ini_cols.append(a); fim_cols.append(b)
            corpo = '\n\n'.join(p['t'] if not p.get('sub') else '### ' + p['t'] for p in trecho)
            blocos.append((v, corpo))
        if len(vs) == 2 or len(blocos) > 1:
            corpo_final = '\n\n'.join(f'## Salmo {v} (Vulgata)\n\n{c}' for v, c in blocos)
        else:
            corpo_final = blocos[0][1]
        a, b = ini_cols[0], fim_cols[-1]
        pl = f"PL {cfg['pl']}, {a}" + (f'–{b}' if b and b != a else '') if cfg.get('pl') else cfg.get('edicao', '')
        passagem = nota_numeracao(h)
        if len(vs) == 2 and len(tem) < 2:
            passagem += f' (neste comentário só consta o Sl {tem[0]})'
        cobre = cfg.get('cobre', 'o salmo inteiro')
        nota = cfg.get('nota')
        tam = gravar_base(h, cfg['arquivo'], cfg['titulo'], cfg['autor'], cfg['obra'], passagem, pl,
                          cfg['fonte'], cobre, corpo_final, cfg['script'], nota=nota, leitor=cfg.get('leitor'))
        n_arq += 1; tot += tam; feitos.append(h)
    return n_arq, tot, feitos


def rodar_cc(cfg, so_hebraicos=None):
    """Fluxo completo para uma obra do Corpus Corporum (PL): baixa, limpa, corta, grava.
    cfg: idno, pl, titulo, autor, obra, arquivo, rotulo, script, fonte (opcional), extras_titulo,
    overrides, fim (callable pars, titulos -> índice), aparar, extras_secao (callable pars, titulos -> lista),
    cobre, nota, motivo_ausente."""
    cfg = dict(cfg)
    cfg.setdefault('fonte', url_corpus(cfg['idno']))
    bruto = corpus_corporum(cfg['idno'])
    m = re.search(r'permalink: (\S+)', bruto)
    pars = limpar_pl(bruto)
    titulos = achar_titulos(pars, cfg.get('extras_titulo', ()), cfg.get('overrides'))
    fim = cfg['fim'](pars, titulos) if callable(cfg.get('fim')) else len(pars)
    ex = cfg['extras_secao'](pars, titulos) if callable(cfg.get('extras_secao')) else ()
    secoes = cortar(pars, titulos, fim, cfg.get('aparar'), ex)
    cfg['leitor'] = (m.group(1) + ' (abre a obra inteira; procurar o título do salmo)') if m else None
    n, tot, feitos = executar_pl(cfg, pars, secoes, so_hebraicos)
    vul = sorted(secoes)
    print(f"[{cfg['script']}] salmos (Vulgata) achados: {len(vul)}; arquivos gravados: {n}; {tot/1024:.0f} KB")
    falt = [v for v in range(1, 151) if v not in secoes]
    print('  Vulgata sem trecho:', falt if falt else 'nenhum')
    return secoes, pars
