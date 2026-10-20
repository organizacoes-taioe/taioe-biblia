"""Santo Afonso Maria de Ligório, *Traduzione de' Salmi e de' Cantici* (1774), por salmo.

    python -I -X utf8 pesquisa/ferramentas/base/mod-afonso-salmi.py baixar     # as páginas do IntraText (uma vez)
    python -I -X utf8 pesquisa/ferramentas/base/mod-afonso-salmi.py cortar     # grava base/afonso-salmi.md de cada salmo
    python -I -X utf8 pesquisa/ferramentas/base/mod-afonso-salmi.py cortar 37 119   # só estes (numeração HEBRAICA)
    python -I -X utf8 pesquisa/ferramentas/base/mod-afonso-salmi.py mapa       # mostra a tabela salmo → página (conferência)

Fonte: IntraText, https://www.intratext.com/IXT/ITASA0000/_IDX150.HTM (páginas `_P36G` a `_P37H`, em ordem).
O cache fica em pesquisa/cache/base/modernos/afonso/ (fora do git). Uma requisição por vez, pausa de 1 s.

Como corta: a obra segue a ordem do Breviário tridentino, não a do Saltério. Cada salmo começa com um
parágrafo «Salmo N. (M. del salterio.)» (o M, quando existe, é o número da Vulgata, com alguns erros de
impressão), depois o «argomento» e, versículo por versículo, o latim da Vulgata seguido da paráfrase
italiana. O script identifica o salmo pelo latim do 1º versículo (comparado com o Saltério da Vulgata do
Divinum Officium, em cache/base/modernos/divinum-officium/) e usa o M só para conferir. Afonso numera os
versículos sem o título do salmo. Sl hebraico → Vulgata: 1–8 igual; 9–10 = 9; 11–113 = −1; 114–115 = 113;
116 = 114–115; 117–146 = −1; 147 = 146–147; 148–150 igual. Hebr. 9 e 10 e hebr. 114 e 115 saem no mesmo
arquivo, porque Afonso os trata como um salmo só (o 9 e o 113 da Vulgata); hebr. 116 junta os 114 e 115
da Vulgata (dois salmos de Afonso, em duas seções) e hebr. 147, os 146 e 147.
"""
import html, os, re, sys, time, unicodedata, urllib.request

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CACHE = os.path.join(RAIZ, 'cache', 'base', 'modernos', 'afonso')
DO = os.path.join(RAIZ, 'cache', 'base', 'modernos', 'divinum-officium')
BASEURL = 'https://www.intratext.com/IXT/ITASA0000/'
INDICE = BASEURL + '_IDX150.HTM'
UA = {'User-Agent': 'Mozilla/5.0 (pesquisa Biblia Taioe)'}
SCRIPT = 'pesquisa/ferramentas/base/mod-afonso-salmi.py'


def b36(n):
    d = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    while n:
        n, r = divmod(n, 36)
        s = d[r] + s
    return s


def paginas():
    # _P36G … _P37H, as do texto da obra (o índice lista todas)
    a, b = int('36G', 36), int('37H', 36)
    return ['_P' + b36(i) for i in range(a, b + 1)]


def baixar():
    os.makedirs(CACHE, exist_ok=True)
    for cod in paginas():
        p = os.path.join(CACHE, cod + '.HTM')
        if os.path.exists(p) and os.path.getsize(p) > 5000:
            continue
        req = urllib.request.Request(BASEURL + cod + '.HTM', headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r:
            dados = r.read()
        open(p, 'wb').write(dados)
        print('baixado', cod, len(dados))
        time.sleep(1)


NOTAS = {}  # id da nota → (número na página, texto); preenchido por texto_pagina


def texto_pagina(cod):
    s = open(os.path.join(CACHE, cod + '.HTM'), encoding='latin-1').read()
    i = s.find('<!--UTM:IT0-->')
    s = s[i:] if i >= 0 else s
    j = s.find('<!--UTM:FT0-->')
    s = s[:j] if j >= 0 else s
    s = re.sub(r'\s*\r?\n\s*', ' ', s)  # quebras de linha do HTML não são de parágrafo
    # notas de rodapé: ficam no fim da página, depois de <hr width=30%>; a chamada no texto é <sup><a href=#$ID>
    k = s.find('<hr size=1 width=30%')
    if k >= 0:
        notas_html, s = s[k:], s[:k]
        for m in re.finditer(r'<a name=\$(\w+) href=#-\w+>(\d+)</a>(.*?)</p>', notas_html):
            t = html.unescape(re.sub(r'<[^>]+>', '', m.group(3))).replace('\xa0', ' ')
            NOTAS[m.group(1)] = (m.group(2), re.sub(r'\s+', ' ', t).strip())
    s = re.sub(r'<sup><a name=-(\w+) href=#\$\w+>(.*?)</a></sup>', lambda m: '⟦' + m.group(1) + '⟧', s)
    s = re.sub(r'</p>|<br\s*/?>', '\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = s.replace('\xa0', ' ')
    linhas = []
    for l in s.split('\n'):
        l = re.sub(r'\s+', ' ', l).strip()
        if l:
            linhas.append(l)
    return linhas


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    s = s.replace('j', 'i').replace('v', 'u').replace('æ', 'ae').replace('œ', 'oe')
    return re.sub(r'[^a-z]', '', s)


def vulgata_incipits():
    """{n: [versículos latinos normalizados]} do Saltério da Vulgata (Gallicanum) do Divinum Officium."""
    pasta = None
    for raiz, dirs, files in os.walk(DO):
        if os.path.basename(raiz) == 'Psalmorum' and 'Latin' in raiz.split(os.sep) and 'horas' in raiz.split(os.sep):
            pasta = raiz
            break
    if not pasta:
        raise SystemExit('Falta o Divinum Officium em ' + DO + ' (veja mod-liturgia.py baixar)')
    out = {}
    for n in range(1, 151):
        p = os.path.join(pasta, f'Psalm{n}.txt')
        if not os.path.exists(p):
            continue
        vs = []
        for l in open(p, encoding='utf-8'):
            l = l.strip()
            m = re.match(r'(\d+):(\d+)[a-z]?\s+(.*)', l)
            if m:
                vs.append((int(m.group(2)), m.group(3)))
        out[n] = vs
    return out


def secoes():
    """Lê as páginas em ordem: lista de ('PAG', n) e ('L', parágrafo). O número de página da edição
    (« - 690 - ») aparece entre parágrafos ou no meio de uma frase; sai do texto e vira marcador."""
    todas = []
    for cod in paginas():
        todas.append(('COD', cod))
        for l in texto_pagina(cod):
            partes = re.split(r'-\s*(\d{3})\s*-', l)
            # partes: texto, nº, texto, nº, texto …
            for i, p in enumerate(partes):
                if i % 2 == 1:
                    todas.append(('PAG', int(p)))
                elif p.strip():
                    todas.append(('LJ' if i > 0 else 'L', p.strip()))  # LJ: continua a frase antes da quebra de página
    return todas


RE_CAB = re.compile(r'^(?:Salmo|Salmi)\b.*$')


def separar():
    """Divide em salmos. Retorna lista de dict(titulo, M, linhas, pags, cods, secao)"""
    itens = secoes()
    out, atual, secao, pag, cod, pag_recente = [], None, '', None, None, False
    for tipo, v in itens:
        if tipo == 'COD':
            cod = v
            if atual:
                atual['cods'].append(cod)
            continue
        if tipo == 'PAG':
            pag = v
            pag_recente = True
            if atual:
                atual['pags'].add(pag)
            continue
        if tipo == 'LJ' or (tipo == 'L' and pag_recente and atual is not None and atual['linhas']
                            and (not re.search(r'[.!?;:)»]$', atual['linhas'][-1]) or v[:1].islower())):
            if atual is not None and atual['linhas']:
                atual['linhas'][-1] += ' ' + v
                pag_recente = False
                continue
        pag_recente = False
        l = v
        # cabeçalho de seção (maiúsculas): FERIA II. - A MATTUTINO, DOMENICA - ALLE LAUDI …
        if re.match(r'^(DOMENICA|FERIA|SABBATO|NELLE FERIE|PRIMO NOTTURNO|SECONDO NOTTURNO|TERZO NOTTURNO|A TERZA|A SESTA|A NONA|ALLA COMPIETA|A COMPIETA|ALLE COMPIETE)\b', l) and l == l.upper():
            secao = l
            if atual:
                out.append(atual)
                atual = None
            continue
        m = re.match(r'^(Salmo|Cantico|Invitatorio)\b(.*)', l)
        if m and len(l) < 120 and re.search(r'(salterio|ed ultimo|^Salmo \d+\.?$|Cantico|Invitatorio|Miserere|Salmo (primo|secondo|terzo))', l):
            if atual:
                out.append(atual)
            mm = re.search(r'\((\d+)\.?\s*del\s+salterio', l)
            atual = {'titulo': l, 'M': int(mm.group(1)) if mm else None, 'linhas': [], 'secao': secao,
                     'pags': {pag} if pag else set(), 'cods': [cod]}
            continue
        if atual is not None:
            atual['linhas'].append(l)
    if atual:
        out.append(atual)
    return out


def lcp(a, b):
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def mapa_salmos():
    """Identifica cada seção pelo latim do 1º versículo (maior prefixo comum com os versículos 1–3 de
    cada salmo da Vulgata; o M do cabeçalho só desempata). Retorna ({n_vulgata: [secao,...]}, [não identificadas])"""
    vulg = vulgata_incipits()
    chaves = [(n, norm(v), num) for n, vs in vulg.items() for num, v in vs[:3]]
    res, nao = {}, []
    for s in separar():
        if s['titulo'].startswith('Cantico'):
            continue  # cânticos (Is 12, Benedictus…) têm incipits iguais aos de alguns salmos
        melhor = (0, None)
        for l in s['linhas'][:6]:
            k = norm(l)
            for n, kv, num in chaves:
                c = lcp(k, kv)
                if c >= 18:
                    pontos = c * 10 + (5 if s['M'] == n else 0) - (abs(n - s['M']) / 1000 if s['M'] else 0)
                    if pontos > melhor[0]:
                        melhor = (pontos, n)
            if melhor[1]:
                break
        s['n'] = melhor[1]
        if melhor[1] is None:
            nao.append(s)
        else:
            res.setdefault(melhor[1], []).append(s)
    return res, nao


# --- hebraico → Vulgata -----------------------------------------------------------------------
def vulgata_de(h):
    if h <= 8 or h >= 148:
        return [h]
    if h in (9, 10):
        return [9]
    if h == 116:
        return [114, 115]
    if h in (114, 115):
        return [113]
    if h == 147:
        return [146, 147]
    return [h - 1]


def cabec_arquivo(h, vul, pags, fonte):
    nums = '–'.join(str(x) for x in vul) if len(vul) > 1 else str(vul[0])
    pg = ('pp. %d–%d' % (min(pags), max(pags))) if pags else ''
    return [
        '# Santo Afonso Maria de Ligório, Traduzione de\' Salmi e de\' Cantici',
        '- Autor: Santo Afonso Maria de Ligório (1696–1787)',
        '- Obra: Traduzione de\' Salmi e de\' Cantici che si contengono nell\'Officio Divino (1774)',
        '- Passagem: Sl %d (hebraico) = Sl %s (Vulgata, numeração de Afonso)%s' % (h, nums, ('; ' + pg + ' da edição-base do IntraText') if pg else ''),
        '- Edição: Napoli/Bassano 1774–1775; texto do IntraText (EuloTech), ortografia modernizada',
        '- Fonte: ' + fonte,
        '- Cobre: o salmo inteiro (argomento e, versículo a versículo, latim da Vulgata e paráfrase italiana)',
        '- Oriental: não',
        '- Língua: it',
        '- Baixado: %s, por %s' % (time.strftime('%Y-%m-%d'), SCRIPT),
    ]


def pagina_de(cod_pag_secao):
    return cod_pag_secao


def cortar(alvos):
    res, nao = mapa_salmos()
    ausentes, ok = [], 0
    for h in alvos:
        if h in (33, 34, 35, 36):
            continue
        vul = vulgata_de(h)
        blocos, pags, urls = [], set(), []
        for n in vul:
            if n not in res:
                ausentes.append((h, n))
                continue
            for s in res[n]:
                blocos.append((n, s))
                pags |= {p for p in s['pags'] if p}
                for c in dict.fromkeys(s['cods']):
                    u = BASEURL + c + '.HTM'
                    if u not in urls:
                        urls.append(u)
        if not blocos:
            continue
        corpo = []
        for n, s in blocos:
            corpo += ['', '## Sl %d da Vulgata — %s (%s)' % (n, s['titulo'], s['secao']), '']
            ids = []
            for l in s['linhas']:
                for m in re.finditer('⟦(\\w+)⟧', l):
                    if m.group(1) in NOTAS and m.group(1) not in ids:
                        ids.append(m.group(1))
                l = re.sub('⟦(\\w+)⟧', lambda m: '[n. %s]' % NOTAS[m.group(1)][0] if m.group(1) in NOTAS else '', l)
                corpo += [l, '']
            if ids:
                corpo += ['Notas de Afonso (rodapé da edição):', ''] + ['- [n. %s] %s' % NOTAS[i] for i in ids] + ['']
        cab = cabec_arquivo(h, vul, pags, ' ; '.join(urls))
        if h in (9, 10):
            cab[6] = '- Cobre: o salmo inteiro (Afonso trata os hebr. 9 e 10 como um salmo só, o 9 da Vulgata)'
        if h in (114, 115):
            cab[6] = '- Cobre: o salmo inteiro (Afonso trata os hebr. 114 e 115 como um salmo só, o 113 da Vulgata)'
        if h == 116:
            cab[6] = '- Cobre: os dois salmos (114 e 115 da Vulgata = hebr. 116,1-9 e 116,10-19), cada um numa seção'
        if h == 147:
            cab[6] = '- Cobre: os dois salmos (146 e 147 da Vulgata = hebr. 147,1-11 e 147,12-20), cada um numa seção'
        if len(blocos) > 1 and h not in (9, 10, 114, 115, 116, 147):
            cab[6] = '- Cobre: o salmo inteiro, em ' + str(len(blocos)) + ' seções do Breviário (o salmo volta em outra hora; o trecho repetido vem de novo)'
        d = os.path.join(RAIZ, 'salmos', '%03d' % h, 'base')
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'afonso-salmi.md'), 'w', encoding='utf-8').write(chr(10).join(cab + corpo).rstrip() + chr(10))
        ok += 1
    print('gravados:', ok)
    if ausentes:
        print('sem texto de Afonso (hebr, vulg):', ausentes)
    return ausentes


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'baixar':
        baixar()
    elif cmd == 'mapa':
        res, nao = mapa_salmos()
        for n in sorted(res):
            for s in res[n]:
                print(n, '|', s['titulo'], '|', s['secao'], '|', sorted(s['pags']), '| versos', len(s['linhas']))
        print('NÃO IDENTIFICADOS:')
        for s in nao:
            print(' ', s['titulo'], '|', s['secao'], '|', s['linhas'][:2])
        print('Faltam da Vulgata:', [n for n in range(1, 151) if n not in res])
    elif cmd == 'cortar':
        alvos = [int(x) for x in sys.argv[2:]] or list(range(1, 151))
        cortar(alvos)
    else:
        print(__doc__)
