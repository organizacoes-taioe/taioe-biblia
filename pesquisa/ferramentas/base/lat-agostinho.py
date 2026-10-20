"""Santo Agostinho, Enarrationes in Psalmos (PL 36-37): todos os salmos, em latim, do augustinus.it.

    python -I -X utf8 pesquisa/ferramentas/base/lat-agostinho.py [--so 32 37 ...]   (números hebraicos)
    python -I -X utf8 pesquisa/ferramentas/base/lat-agostinho.py --baixar            (só baixa os 208 arquivos)

Texto: augustinus.it (Nuova Biblioteca Agostiniana, texto dos Maurinos = PL). Padrão
`https://www.augustinus.it/latino/esposizioni_salmi/esposizione_salmo_NNN_testo.htm`, em que NNN é a ordem do
arquivo, não o número do salmo (tabela em fontes/agostinho.md § 1.1: salmos com várias enarrationes
ocupam vários arquivos; o Sl 118 tem o prólogo no 144 e os sermões I-XXXII nos 145-176). Quando o site
responde 503 (o caso em 2026-10-20), o script usa a cópia do web.archive.org (`.../web/2016id_/...`).
Cache: pesquisa/cache/base/aug/NNN.htm (uma requisição por vez, pausa de 1 s).

Colunas da PL: o augustinus.it não as tem. O script baixa o texto da PL do Corpus Corporum (idno 7329 =
Sl 1-79, PL 36; idno 21385 = Sl 80-150, PL 37), tira as notas, e ancora cada marca `[page NNNN]` no
augustinus.it pelas quatro palavras seguintes (letras sem acento, j=i, v=u), sempre avançando. Marcas que
não acham âncora ficam de fora (o «Edição» sai das que acharam). O OCR do Corpus erra; o augustinus.it
também tem raros erros de digitação (conferir no PL quando estranho).
As notas do augustinus.it (referências bíblicas da NBA, arquivos `_note.htm`) não estão no web.archive.org: os
sobrescritos de nota são descartados.
Numeração: sempre a da Vulgata; lat_comum.py converte para a hebraica (pasta salmos/<ccc>).
"""
import sys, os, re, html, time, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

SEGMENTOS = [  # (primeiro salmo, último salmo, primeiro arquivo, arquivos por salmo)
    (1, 17, 1, 1), (18, 18, 18, 2), (19, 20, 20, 1), (21, 21, 22, 2), (22, 24, 24, 1), (25, 25, 27, 2),
    (26, 26, 29, 2), (27, 28, 31, 1), (29, 29, 33, 2), (30, 30, 35, 4), (31, 31, 39, 2), (32, 32, 41, 3),
    (33, 33, 44, 2), (34, 34, 46, 2), (35, 35, 48, 1), (36, 36, 49, 3), (37, 47, 52, 1), (48, 48, 63, 2),
    (49, 57, 65, 1), (58, 58, 74, 2), (59, 67, 76, 1), (68, 68, 85, 2), (69, 69, 87, 1), (70, 70, 88, 2),
    (71, 87, 90, 1), (88, 88, 107, 2), (89, 89, 109, 1), (90, 90, 110, 2), (91, 100, 112, 1), (101, 101, 122, 2),
    (102, 102, 124, 1), (103, 103, 125, 4), (104, 112, 129, 1), (113, 113, 138, 2), (114, 117, 140, 1),
    (118, 118, 144, 33), (119, 150, 177, 1),
]


def arquivos_por_salmo():
    m = {}
    for a, b, f0, k in SEGMENTOS:
        f = f0
        for v in range(a, b + 1):
            m[v] = list(range(f, f + k))
            f += k
    return m


POR_SALMO = arquivos_por_salmo()
TOTAL_ARQ = 208
ARQ = os.path.join(L.CACHE, 'aug')
LIVE = 'https://www.augustinus.it/latino/esposizioni_salmi/esposizione_salmo_{:03d}_testo.htm'
WAY = 'http://web.archive.org/web/2016id_/http://www.augustinus.it/latino/esposizioni_salmi/esposizione_salmo_{:03d}_testo.htm'
_modo = {'live': None}


def url_live(n):
    return LIVE.format(n)


def url_way(n):
    return WAY.format(n)


def obter(n):
    """HTML do arquivo n (cache; tenta o site e, se cair, a cópia do web.archive.org)."""
    p = os.path.join(ARQ, f'{n:03d}.htm')
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        return open(p, 'rb').read().decode('cp1252', 'replace')
    import urllib.request
    os.makedirs(ARQ, exist_ok=True)
    dados = None
    if _modo['live'] is not False:
        try:
            req = urllib.request.Request(url_live(n), headers={'User-Agent': L.UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                dados = r.read()
            _modo['live'] = True
        except Exception as e:  # noqa
            if _modo['live'] is None:
                print('  site fora do ar (', str(e)[:60], '): usando o web.archive.org')
            _modo['live'] = False
    if dados is None:
        ult = None
        for i in range(5):
            try:
                req = urllib.request.Request(url_way(n), headers={'User-Agent': L.UA})
                with urllib.request.urlopen(req, timeout=90) as r:
                    dados = r.read()
                if b'Augustinus Hipponensis' not in dados[:2000]:
                    raise RuntimeError('resposta sem o texto esperado')
                break
            except Exception as e:  # noqa
                ult = e
                dados = None
                time.sleep(4 * (i + 1))
        if dados is None:
            raise RuntimeError(f'arquivo {n}: {ult}')
    with open(p, 'wb') as f:
        f.write(dados)
    time.sleep(1.0)
    return dados.decode('cp1252', 'replace')


def baixar_todos():
    for n in range(1, TOTAL_ARQ + 1):
        obter(n)
        if n % 20 == 0:
            print('  baixados até', n, flush=True)


# ---------------------------------------------------------------- HTML -> texto
def html_para_pars(h):
    """Devolve (titulo_pagina, subtitulo, resumo, [paragrafos])."""
    t = re.search(r'<TITLE>(.*?)</TITLE>', h, re.S | re.I)
    titulo_pag = html.unescape(t.group(1)).strip() if t else ''
    corpo = h[h.lower().find('<body'):]
    h3 = re.search(r'<H3[^>]*>(.*?)</H3>', corpo, re.S | re.I)
    cab = re.sub(r'<[^>]+>', '', h3.group(1)).strip() if h3 else ''
    sub = ''
    m = re.search(r'</H3>\s*(?:<B>)?\s*<P[^>]*>(.*?)</P>', corpo, re.S | re.I)
    if m:
        sub = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    resumo = re.search(r'<H5[^>]*>(.*?)</H5>', corpo, re.S | re.I)
    resumo = re.sub(r'<[^>]+>', '', resumo.group(1)).strip() if resumo else ''
    pars = []
    for m in re.finditer(r'<P ALIGN="JUSTIFY"[^>]*>(.*?)</P>', corpo, re.S | re.I):
        x = m.group(1)
        x = re.sub(r'<A HREF="[^"]*_note\.htm[^"]*">.*?</A>', '', x, flags=re.S | re.I)  # sobrescritos de nota
        x = re.sub(r'</I>\s*<I>', '', x, flags=re.I)
        x = re.sub(r'</I>(\s*)<I>', r'\1', x, flags=re.I)
        x = re.sub(r'<I>(.*?)</I>', lambda mm: '*' + mm.group(1).strip() + '*' + (' ' if mm.group(1).endswith(' ') else ''), x, flags=re.S | re.I)
        x = re.sub(r'<BR\s*/?>', ' ', x, flags=re.I)
        x = re.sub(r'<[^>]+>', '', x)
        x = html.unescape(x).replace('\xa0', ' ')
        x = re.sub(r'\*\s*\*', ' ', x)  # *..*  *..*  -> junta
        x = re.sub(r'\s+', ' ', x).strip()
        if x:
            pars.append(x)
    return titulo_pag, cab, sub, resumo, pars


def psalmo_do_titulo(cab):
    m = re.search(r'PSALMUM\s+(\d+)', cab, re.I)
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------- colunas da PL (âncoras)
def norm(tok):
    s = unicodedata.normalize('NFD', tok.lower())
    s = ''.join(c for c in s if c.isalpha() and unicodedata.category(c)[0] == 'L')
    s = s.replace('j', 'i').replace('v', 'u').replace('æ', 'e').replace('œ', 'e')
    s = re.sub(r'[^a-z]', '', s)
    return s


def tokens_cc(bruto):
    """(lista de palavras normalizadas, lista de (posição_na_lista, coluna)) do texto da PL, sem notas."""
    linhas = bruto.split('\n')
    for i, l in enumerate(linhas[:40]):
        if l.startswith('#####'):
            linhas = linhas[i + 1:]
            break
    palavras, marcas = [], []
    dentro_notas = False
    for l in linhas:
        m = L.RE_MARCA.match(l)
        if m:
            marcas.append((len(palavras), str(int(m.group(1))) + m.group(2)))
            dentro_notas = False
            continue
        if L.RE_SEP.match(l):
            dentro_notas = True
            continue
        if dentro_notas:
            continue
        for tk in l.split():
            n = norm(re.sub(r'\[\d+\]', '', tk))
            if n:
                palavras.append(n)
    return palavras, marcas


def ancorar(aug_norm, cc_pal, cc_marcas, inicio_cc=0):
    """Para cada marca do CC acha a posição em aug_norm (lista de palavras). Devolve [(pos_aug, coluna)]."""
    achados = []
    p = 0
    for pos, col in cc_marcas:
        seg = cc_pal[pos:pos + 12]
        achou = None
        for k in (5, 4, 3):
            alvo = seg[:k]
            if len(alvo) < k:
                continue
            janela = 6000 if k >= 4 else 800
            fim = min(len(aug_norm) - k, p + janela)
            for j in range(p, fim + 1):
                if aug_norm[j] == alvo[0] and aug_norm[j:j + k] == alvo:
                    achou = j
                    break
            if achou is not None:
                break
        if achou is not None:
            achados.append((achou, col, pos))
            p = achou
    return achados


def gerar(so=None):
    # 1) baixa tudo e lê
    textos = {}
    for n in range(1, TOTAL_ARQ + 1):
        textos[n] = html_para_pars(obter(n))
    # confere a tabela arquivo -> salmo
    erros = []
    for v, fs in POR_SALMO.items():
        for f in fs:
            pv = psalmo_do_titulo(textos[f][1])
            if pv != v:
                erros.append((f, v, pv, textos[f][1]))
    if erros:
        print('ERRO: tabela arquivo->salmo não confere:', erros[:10])
        sys.exit(1)
    # 2) colunas da PL
    marcas_por_arquivo = {}  # n -> [(idx_par, idx_tok, col)]
    col_ini, col_fim = {}, {}
    if True:
        for idno, vol, v_ini, v_fim in ((7329, 36, 1, 79), (21385, 37, 80, 150)):
            bruto = L.corpus_corporum(idno)
            cc_pal, cc_marcas = tokens_cc(bruto)
            # fluxo do augustinus.it para esses salmos
            fluxo, norm_list, pos_map = [], [], []
            arqs = [f for v in range(v_ini, v_fim + 1) for f in POR_SALMO[v]]
            for f in arqs:
                for ip, par in enumerate(textos[f][4]):
                    for it, tk in enumerate(par.split(' ')):
                        n = norm(re.sub(r'[*]', '', tk))
                        if n:
                            norm_list.append(n)
                            pos_map.append((f, ip, it))
            ach = ancorar(norm_list, cc_pal, cc_marcas)
            print(f'  PL {vol}: {len(ach)} de {len(cc_marcas)} marcas de coluna ancoradas')
            for pos, col, _ in ach:
                f, ip, it = pos_map[pos]
                marcas_por_arquivo.setdefault(f, []).append((ip, it, col, vol))
            # colunas do começo e do fim de cada arquivo (interpolando entre as âncoras, para não depender
            # de a marca vizinha ter sido ancorada)
            import bisect
            a_aug = [x[0] for x in ach]
            a_cc = [x[2] for x in ach]
            m_pos = [x[0] for x in cc_marcas]

            def col_em(p):
                k = bisect.bisect_right(a_aug, p)
                if k == 0:
                    c = a_cc[0] - (a_aug[0] - p)
                elif k >= len(a_aug):
                    c = a_cc[-1] + (p - a_aug[-1])
                else:
                    c = a_cc[k - 1] + (p - a_aug[k - 1]) * (a_cc[k] - a_cc[k - 1]) / max(1, a_aug[k] - a_aug[k - 1])
                j = bisect.bisect_right(m_pos, c) - 1
                return cc_marcas[max(j, 0)][1]
            for f in arqs:
                idx = [i for i, (ff, _, _) in enumerate(pos_map) if ff == f]
                if idx:
                    col_ini[f] = (col_em(idx[0]), vol)
                    col_fim[f] = (col_em(idx[-1]), vol)
    todas = sorted((f, ip, it, col, vl) for f, ms in marcas_por_arquivo.items() for (ip, it, col, vl) in ms)
    # 3) monta os arquivos
    n_arq, tot = 0, 0
    for h in L.hebraicos_alvo():
        if so and h not in so:
            continue
        vs = L.vulgata_de_hebraico(h)
        blocos, cols, subs = [], [], []
        vol = None
        for v in vs:
            for f in POR_SALMO[v]:
                titulo_pag, cab, sub, resumo, pars = textos[f]
                mk = {}
                for ip, it, col, vl in sorted(marcas_por_arquivo.get(f, [])):
                    mk.setdefault((ip, it), []).append(col)
                    vol = vl
                    cols.append(col)
                corpo_pars = []
                for ip, par in enumerate(pars):
                    toks = par.split(' ')
                    for it in range(len(toks)):
                        for col in mk.get((ip, it), []):
                            toks[it] = f'[col. {col}] ' + toks[it]
                    corpo_pars.append(' '.join(toks))
                rot = re.sub(r'^Augustinus Hipponensis - In Psalmum \d+\s*', '', titulo_pag, flags=re.I).strip() or 'enarratio'
                if resumo == 'Prooemium':
                    rot = 'prooemium'
                elif sub.lower().startswith('sermo'):
                    rot += f' ({sub.lower()})'
                subs.append(rot)
                cab_blk = f'## Salmo {v} (Vulgata): {rot} (arquivo {f:03d} do augustinus.it)'
                if resumo:
                    cab_blk += f'\n\n{resumo}'
                blocos.append(cab_blk + '\n\n' + '\n\n'.join(corpo_pars))
        vol = vol or (36 if vs[0] <= 79 else 37)
        pl = f'PL {vol}'
        arqs_h = [f for v in vs for f in POR_SALMO[v]]
        if arqs_h[0] in col_ini:
            a, vol = col_ini[arqs_h[0]]
            b = col_fim[arqs_h[-1]][0]
            pl = f'PL {vol}, {a}–{b}' if a != b else f'PL {vol}, {a}'
            pl += ' (colunas deduzidas do Corpus Corporum)'
        arqs_h = [f for v in vs for f in POR_SALMO[v]]
        fonte = url_live(arqs_h[0]) if len(arqs_h) == 1 else ' ; '.join(url_live(f) for f in arqs_h)
        copia = ' ; '.join(url_way(f) for f in arqs_h)
        if len(subs) > 6:
            desc = 'prólogo e 32 sermões (enarrationes I–XXXII)'
        elif len(subs) == 1:
            desc = 'uma enarratio'
        else:
            desc = 'enarrationes ' + ', '.join(re.sub(r'^enarratio\s*', '', x) or '(única)' for x in subs)
            if len({L.vulgata_de_hebraico(h)[0]}) and len(vs) == 2:
                desc = '; '.join(f'Sl {v}: {x}' for v, x in zip(vs, subs))
        passagem = L.nota_numeracao(h) + '; ' + desc
        corpo = '\n\n'.join(blocos)
        tam = L.gravar_base(h, 'agostinho-enarrationes-in-psalmos.md', 'Santo Agostinho, Enarrationes in Psalmos',
                            'Santo Agostinho (354–430)', 'Enarrationes in Psalmos', passagem, pl, fonte,
                            'o salmo inteiro (todas as enarrationes e sermões)', corpo,
                            'lat-agostinho.py', nota='Texto dos Maurinos (= PL) pelo augustinus.it; itálico (*...*) = citação bíblica; [v N.] = versículo comentado. '
                            'Cópia usada: ' + copia)
        n_arq += 1
        tot += tam
    print(f'[lat-agostinho.py] arquivos gravados: {n_arq}; {tot/1024:.0f} KB')


if __name__ == '__main__':
    if '--baixar' in sys.argv:
        baixar_todos()
    else:
        so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
        gerar(so)
