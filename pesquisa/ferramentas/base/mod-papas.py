"""Audiências gerais dos Papas (vatican.va, em italiano) que comentam um salmo: só um ÍNDICE, sem guardar o texto.

    python -I -X utf8 pesquisa/ferramentas/base/mod-papas.py baixar      # índices anuais + cada audiência (cache, fora do git)
    python -I -X utf8 pesquisa/ferramentas/base/mod-papas.py baixar-docs # encíclicas, exortações e cartas apostólicas (JP II, Bento XVI, Francisco, Leão XIV)
    python -I -X utf8 pesquisa/ferramentas/base/mod-papas.py analisar    # monta cache/base/modernos/papas/indice.json
    python -I -X utf8 pesquisa/ferramentas/base/mod-papas.py pt          # títulos oficiais em português das catequeses do ciclo

Varre as audiências de São João Paulo II (2001–2005), Bento XVI (2005–2013), Francisco (2013–2025) e
Leão XIV (2025–2026). Para cada uma, guarda no cache o texto limpo e conta quantas vezes cada salmo é
citado («Sal 32», «Salmo 143 [144]»). Duas categorias saem no índice:
  - **ciclo**: as catequeses de 2001–2006 sobre os salmos e cânticos de Laudes e Vésperas, cujo título é
    «Salmo N - …» (João Paulo II, depois Bento XVI) e a «Escola de oração» de 2011 (Sl 3, 22, 23, 126, 136, 119, 110);
  - **cita**: as outras audiências em que o salmo aparece 3 vezes ou mais (provável comentário).
Numeração: nas catequeses de 2001–fev. 2006 o número sem colchetes é o da Vulgata; com colchetes, o primeiro
é a Vulgata e o segundo, o hebraico. Fora disso, sem colchetes vale o hebraico; com colchetes, vale a ordem
que for coerente (hebr = vulg + 1 na faixa 10–147). O índice guarda tudo em número HEBRAICO.
Uma requisição por vez, pausa de 1 s; o que já está no cache não se baixa de novo.
Direito autoral da LEV: o texto fica só no cache local; os arquivos de base/ levam título, data e URL.
"""
import html, json, os, re, sys, time, urllib.request, urllib.error

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CACHE = os.path.join(RAIZ, 'cache', 'base', 'modernos', 'papas')
UA = {'User-Agent': 'Mozilla/5.0 (pesquisa Biblia Taioe)'}
SITE = 'https://www.vatican.va'

ALVOS = [  # (slug, anos)
    ('john-paul-ii', range(2001, 2006)),
    ('benedict-xvi', range(2005, 2014)),
    ('francesco', range(2013, 2026)),
    ('leo-xiv', range(2025, 2027)),
]
NOME = {'john-paul-ii': 'São João Paulo II', 'benedict-xvi': 'Bento XVI', 'francesco': 'Papa Francisco', 'leo-xiv': 'Leão XIV'}


def pega(url, tent=3):
    for i in range(tent):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode('utf-8', errors='replace')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3)
        except Exception:
            time.sleep(3)
    return None


def texto(h):
    h = re.sub(r'<script.*?</script>|<style.*?</style>', '', h, flags=re.S)
    h = re.sub(r'</p>|<br\s*/?>|</div>|</h\d>', '\n', h, flags=re.I)
    h = re.sub(r'<[^>]+>', '', h)
    h = html.unescape(h).replace('\xa0', ' ')
    return re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n', h)).strip()


def baixar():
    os.makedirs(CACHE, exist_ok=True)
    for slug, anos in ALVOS:
        for ano in anos:
            ip = os.path.join(CACHE, slug, '%d.index.html' % ano)
            os.makedirs(os.path.dirname(ip), exist_ok=True)
            if not os.path.exists(ip):
                h = pega('%s/content/%s/it/audiences/%d.index.html' % (SITE, slug, ano))
                time.sleep(1)
                if h is None:
                    print('SEM ÍNDICE', slug, ano)
                    continue
                open(ip, 'w', encoding='utf-8').write(h)
            h = open(ip, encoding='utf-8').read()
            links = sorted(set(re.findall(r'href="(/content/%s/it/audiences/\d+/documents/[^"]+\.html)"' % slug, h)))
            n = 0
            for l in links:
                nome = l.rsplit('/', 1)[1][:-5]
                ano_doc = l.split('/')[-3]
                p = os.path.join(CACHE, slug, ano_doc, nome + '.txt')
                if os.path.exists(p):
                    continue
                os.makedirs(os.path.dirname(p), exist_ok=True)
                d = pega(SITE + l)
                time.sleep(1)
                if d is None:
                    open(p, 'w', encoding='utf-8').write('')
                    print('404', l)
                    continue
                open(p, 'w', encoding='utf-8').write(texto(d))
                n += 1
            print(slug, ano, len(links), 'documentos;', n, 'novos', flush=True)


DOCS = [(slug, tipo) for slug in ('john-paul-ii', 'benedict-xvi', 'francesco', 'leo-xiv')
        for tipo in ('encyclicals', 'apost_exhortations', 'apost_letters')]


def baixar_docs():
    """Encíclicas, exortações e cartas apostólicas (índices sem ano)."""
    for slug, tipo in DOCS:
        ip = os.path.join(CACHE, slug, '_docs', tipo + '.index.html')
        os.makedirs(os.path.dirname(ip), exist_ok=True)
        if not os.path.exists(ip):
            h = pega('%s/content/%s/it/%s.index.html' % (SITE, slug, tipo))
            time.sleep(1)
            if h is None:
                print('SEM ÍNDICE', slug, tipo)
                continue
            open(ip, 'w', encoding='utf-8').write(h)
        h = open(ip, encoding='utf-8').read()
        links = sorted(set(re.findall(r'href="(/content/%s/it/%s/(?:\d+/)?documents/[^"]+\.html)"' % (slug, tipo), h)))
        n = 0
        for l in links:
            nome = l.rsplit('/', 1)[1][:-5]
            p = os.path.join(CACHE, slug, '_docs', tipo, nome + '.txt')
            if os.path.exists(p):
                continue
            os.makedirs(os.path.dirname(p), exist_ok=True)
            d = pega(SITE + l)
            time.sleep(1)
            open(p, 'w', encoding='utf-8').write(texto(d) if d else '')
            n += 1
        print(slug, tipo, len(links), 'documentos;', n, 'novos', flush=True)


def baixar_cartas_jp2(anos=range(1995, 2006)):
    """As cartas apostólicas de João Paulo II estão em índices anuais (apost_letters/<ano>.index.html)."""
    slug, tipo = 'john-paul-ii', 'apost_letters'
    for ano in anos:
        h = pega('%s/content/%s/it/%s/%d.index.html' % (SITE, slug, tipo, ano))
        time.sleep(1)
        if not h:
            print('sem índice', ano)
            continue
        links = sorted(set(re.findall(r'href="(/content/%s/it/%s/\d+/documents/[^"]+\.html)"' % (slug, tipo), h)))
        n = 0
        for l in links:
            nome = l.rsplit('/', 1)[1][:-5]
            p = os.path.join(CACHE, slug, '_docs', tipo, nome + '.txt')
            if os.path.exists(p):
                continue
            os.makedirs(os.path.dirname(p), exist_ok=True)
            d = pega(SITE + l)
            time.sleep(1)
            open(p, 'w', encoding='utf-8').write(texto(d) if d else '')
            n += 1
        print('cartas JP II', ano, len(links), 'documentos;', n, 'novos', flush=True)


def vul_para_heb(v):
    if v <= 8 or v >= 148:
        return v
    if v == 9:
        return 9
    if v == 113:
        return 114
    if v in (114, 115):
        return 116
    return v + 1


def heb_do_par(a, b, ciclo):
    """a = número antes, b = número entre colchetes (ou None). Devolve o número hebraico."""
    if b is None:
        return vul_para_heb(a) if ciclo else a
    # escolhe a leitura coerente
    if vul_para_heb(a) == b:
        return b           # a = Vulgata, b = hebraico
    if vul_para_heb(b) == a:
        return a           # a = hebraico, b = Vulgata
    return a if not ciclo else b


def ciclo_heb(a, suf, b):
    """Número hebraico de um salmo do ciclo (Vulgata a, sufixo A/B do Sl 113, colchete b)."""
    if a == 113 and suf == 'A':
        return 114
    if a == 113 and suf == 'B':
        return 115
    return heb_do_par(a, b, True)


RE_SAL = re.compile(r'\b(?:Sal|Salmo|Salmi|Sl)\b\.?\s*(\d{1,3})(?:\s*[A-B]\b)?(?:\s*[\[\(]\s*(\d{1,3})\s*[\]\)])?')


def data_do_nome(nome):
    m = re.search(r'(\d{8})', nome)
    if not m:
        return ''
    d = m.group(1)
    if 1900 <= int(d[:4]) <= 2035:
        return '%s-%s-%s' % (d[:4], d[4:6], d[6:])
    return '%s-%s-%s' % (d[4:], d[2:4], d[:2])  # ddmmaaaa


DATA_RE = re.compile(r'(Luned|Marted|Mercoled|Gioved|Venerd|Sabato|Domenica)\w*,?\s+\d+\s+\w+\s+\d{4}')


def cabecalho(t):
    """Título e «Lettura» do documento: as linhas depois da barra de línguas (DE - EN - … PT) e antes do 1º parágrafo."""
    linhas = [l.strip() for l in t.split('\n')]
    ini = 0
    for i, l in enumerate(linhas[:80]):
        if re.match(r'^-?\s*PT\s*$', l):
            ini = i + 1
    cab = []
    for l in linhas[ini:ini + 14]:
        if re.match(r'^\d+\.\s', l) or l.startswith('Cari ') or l.startswith('Carissimi'):
            break
        if l:
            cab.append(l)
    h = ' '.join(cab)
    m = re.search(r'\(Lettura:\s*([^)]*)\)', h)
    leitura = m.group(1).strip() if m else None
    h = re.sub(r'\(Lettura:[^)]*\)', '', h)
    h = DATA_RE.sub('', h)
    h = re.sub(r'\b(UDIENZA GENERALE|GIOVANNI PAOLO II|BENEDETTO XVI|FRANCESCO|LEONE XIV|Piazza San Pietro|Aula Paolo VI|Sala Nervi)\b', '', h)
    return re.sub(r'\s+', ' ', h).strip(' "-')[:200], leitura


def analisar():
    docs = []
    for slug, anos in ALVOS:
        for raiz, dirs, files in os.walk(os.path.join(CACHE, slug)):
            for f in sorted(files):
                if not f.endswith('.txt'):
                    continue
                t = open(os.path.join(raiz, f), encoding='utf-8').read()
                if not t:
                    continue
                ano = os.path.basename(raiz)
                nome = f[:-4]
                data = data_do_nome(nome)
                if '_docs' in raiz.split(os.sep):
                    tipo = ano
                    url = '%s/content/%s/it/%s/documents/%s.html' % (SITE, slug, tipo, nome)
                else:
                    tipo = 'audiences'
                    url = '%s/content/%s/it/audiences/%s/documents/%s.html' % (SITE, slug, ano, nome)
                flat = re.sub(r'\s+', ' ', t)
                titulo, leitura = cabecalho(t)
                ciclo_epoca = '2001-03-28' <= data <= '2006-02-16' and slug in ('john-paul-ii', 'benedict-xvi')
                ciclo_salmos = []
                if leitura and ciclo_epoca:
                    for mm in re.finditer(r'Sal(?:mo)?\s*(\d{1,3})\s*([AB])?(?:\s*[\[\(]\s*(\d{1,3})\s*[\]\)])?', leitura):
                        h = ciclo_heb(int(mm.group(1)), mm.group(2), int(mm.group(3)) if mm.group(3) else None)
                        if h not in ciclo_salmos:
                            ciclo_salmos.append(h)
                if not ciclo_salmos and ciclo_epoca and titulo:
                    mm = re.search(r'Salm[oi]\s*(\d{1,3})\s*([AB])?\b(?:\s*[\[\(]\s*(\d{1,3})\s*[\]\)])?', titulo) or \
                        re.search(r'\((?:Sal|Lettura:? Sal)\s*(\d{1,3})()()', titulo)
                    if mm:
                        ciclo_salmos = [ciclo_heb(int(mm.group(1)), mm.group(2) or None, int(mm.group(3)) if mm.group(3) else None)]
                if not ciclo_salmos and ciclo_epoca:
                    for l in t.splitlines()[:140]:
                        mm = re.match(r'^Salm[oi]\s*(\d{1,3})\s*([AB])?\b', l.strip())
                        if mm:
                            ciclo_salmos = [ciclo_heb(int(mm.group(1)), mm.group(2), None)]
                            break
                if not ciclo_salmos and ciclo_epoca and re.search(r'Lodi|Vespri|Salm|Lettura|cura di', titulo + ' ' + flat[:900]):
                    # sem título numerado (ex.: 2001-06-13, Sl 28; 2003-09-24, lida pelo Card. Sodano): 1º salmo citado no início do corpo
                    corpo = flat[flat.find(' 1. ') if flat.find(' 1. ') > 0 else 0:][:1800]
                    ms = [(int(m.group(1)), m.group(2)) for m in RE_SAL.finditer(corpo)]
                    if ms:
                        a0 = ms[0][0]
                        if sum(1 for x in ms if x[0] == a0) >= 2 and 'Ordine' not in titulo:
                            ciclo_salmos = [ciclo_heb(a0, None, None)]
                cont = {}
                for mm in RE_SAL.finditer(flat):
                    a = int(mm.group(1))
                    b = int(mm.group(2)) if mm.group(2) else None
                    if not (1 <= a <= 150):
                        continue
                    if b is not None and not (1 <= b <= 150):
                        b = None
                    h = heb_do_par(a, b, ciclo_epoca)
                    cont[h] = cont.get(h, 0) + 1
                docs.append({'papa': slug, 'tipo': tipo, 'data': data, 'url': url, 'arquivo': nome, 'titulo': titulo,
                             'leitura': leitura, 'ciclo_salmos': ciclo_salmos, 'cita': cont})
    docs.sort(key=lambda d: (d['data'], d['papa']))
    json.dump(docs, open(os.path.join(CACHE, 'indice.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(len(docs), 'documentos no índice;', sum(1 for d in docs if d['ciclo_salmos']), 'catequeses de ciclo sobre salmos')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'baixar':
        baixar()
    elif cmd == 'baixar-docs':
        baixar_docs()
        baixar_cartas_jp2()
    elif cmd == 'analisar':
        analisar()
    else:
        print(__doc__)
