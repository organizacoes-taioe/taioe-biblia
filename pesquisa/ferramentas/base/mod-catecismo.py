"""Catecismo da Igreja Católica: em que parágrafos cada salmo é citado (pelas notas de rodapé).

    python -I -X utf8 pesquisa/ferramentas/base/mod-catecismo.py baixar     # os 34 arquivos em português (cache, fora do git)
    python -I -X utf8 pesquisa/ferramentas/base/mod-catecismo.py indice     # monta cache/base/modernos/catecismo/indice.json
    python -I -X utf8 pesquisa/ferramentas/base/mod-catecismo.py mostrar 22 # parágrafos que citam o Sl 22 (hebraico)

Fonte: https://www.vatican.va/archive/cathechism_po/index_new/prima-pagina-cic_po.html (texto oficial, português
europeu, ISO-8859-1). O arquivo traz o texto com as chamadas de nota «(N)» e, no fim, as notas «(N) Sl 8, 2; …».
O script associa cada nota ao último número de parágrafo que a precede e lê as siglas «Sl», «Sal».
Numeração: o Catecismo usa a HEBRAICA (Sl 33 = Vulgata 32), mas as notas citam também «Sl 22; 32; 35» em listas
e, nas citações antigas, a Vulgata; por isso o índice guarda o texto da nota ao lado, para conferir.
Uma requisição por vez, pausa de 1 s.
"""
import html, json, os, re, sys, time, urllib.request

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CACHE = os.path.join(RAIZ, 'cache', 'base', 'modernos', 'catecismo')
BASE = 'https://www.vatican.va/archive/cathechism_po/index_new/'
UA = {'User-Agent': 'Mozilla/5.0 (pesquisa Biblia Taioe)'}


def arquivos():
    p = os.path.join(CACHE, 'prima-pagina.html')
    if not os.path.exists(p):
        os.makedirs(CACHE, exist_ok=True)
        req = urllib.request.Request(BASE + 'prima-pagina-cic_po.html', headers=UA)
        open(p, 'wb').write(urllib.request.urlopen(req, timeout=60).read())
        time.sleep(1)
    h = open(p, encoding='latin-1').read()
    return sorted(set(x for x in re.findall(r'href="([^"/]+_po\.html)"', h)
                      if re.match(r'(p\d|prologo)', x)), key=lambda x: x)


def baixar():
    os.makedirs(CACHE, exist_ok=True)
    for a in arquivos():
        p = os.path.join(CACHE, a.replace('%20', '_'))
        if os.path.exists(p) and os.path.getsize(p) > 2000:
            continue
        req = urllib.request.Request(BASE + a, headers=UA)
        open(p, 'wb').write(urllib.request.urlopen(req, timeout=60).read())
        print('baixado', a)
        time.sleep(1)


def limpa(b):
    h = b.decode('latin-1')
    h = re.sub(r'<script.*?</script>|<style.*?</style>', '', h, flags=re.S)
    h = re.sub(r'</p>|<br\s*/?>|</div>|</h\d>|</tr>|</li>', '\n', h, flags=re.I)
    h = re.sub(r'<[^>]+>', '', h)
    return html.unescape(h).replace('\xa0', ' ')


def indice():
    """Parágrafos: «<b>2587.</b> texto … (38) …»; notas no fim do arquivo, «38. Cf. Sl 1, 2.» (a numeração das
    notas recomeça em cada arquivo). Liga cada chamada «(N)» ao parágrafo em que está e lê a nota N."""
    out = {}
    for f in sorted(os.listdir(CACHE)):
        if not f.endswith('_po.html') or f.startswith('prima'):
            continue
        t = limpa(open(os.path.join(CACHE, f), 'rb').read())
        linhas = [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n') if l.strip()]
        ini = None  # início das notas: a última linha «1. …» seguida de «2. …»
        for i, l in enumerate(linhas[:-1]):
            if re.match(r'^1\.\s', l) and re.match(r'^2\.?\s', linhas[i + 1]):
                ini = i
        if ini is None:
            print('sem notas?', f)
            continue
        notas = {}
        for l in linhas[ini:]:
            m = re.match(r'^(\d{1,3})\.?\s*(.*)', l)
            if m and m.group(2):
                notas.setdefault(int(m.group(1)), m.group(2))
        par, chamada, textos = None, {}, {}
        for l in linhas[:ini]:
            m = re.match(r'^(\d{1,4})\.\s', l)
            if m and 1 <= int(m.group(1)) <= 2865:
                par = int(m.group(1))
                textos[par] = l
            for c in re.finditer(r'\((\d{1,3})\)', l):
                chamada.setdefault(int(c.group(1)), par)
            if par is not None and not m:
                textos[par] = textos.get(par, '') + ' ' + l
        for n, txt in notas.items():
            par = chamada.get(n)
            if par is None:
                continue
            for h, ver in refs_salmo(txt):
                out.setdefault(str(h), []).append({'par': par, 'nota': n, 'texto': txt, 'ver': ver, 'via': 'nota'})
        for par, l in textos.items():  # «Salmo 51», «(Sl 130, 1)» no próprio texto
            l2 = re.sub(r'\(\d{1,3}\)', '', l)
            for h, ver in refs_salmo(l2):
                out.setdefault(str(h), []).append({'par': par, 'nota': None, 'texto': l2[:0], 'ver': ver, 'via': 'texto'})
            for m in re.finditer(r'[Ss]almos?\s+(\d{1,3})', l2):
                h = int(m.group(1))
                if 1 <= h <= 150:
                    out.setdefault(str(h), []).append({'par': par, 'nota': None, 'texto': l2[max(0, m.start() - 60):m.end() + 40],
                                                       'ver': '', 'via': 'texto'})
    json.dump(out, open(os.path.join(CACHE, 'indice.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('salmos citados:', len(out), '; citações:', sum(len(v) for v in out.values()))


def indice_velho():
    out = {}  # n_hebraico -> lista de dicts(par, nota, arquivo)
    for f in sorted(os.listdir(CACHE)):
        if not f.endswith('_po.html') or f.startswith('prima'):
            continue
        t = limpa(open(os.path.join(CACHE, f), 'rb').read())
        linhas = [l.strip() for l in t.split('\n') if l.strip()]
        # 1) parágrafos: linha que começa com o número (3–4 dígitos) do parágrafo
        # 2) notas: linhas «(N) …» ou «N …» depois do texto; chamadas «(N)» dentro do texto
        # estratégia: percorre as linhas; mantém o último parágrafo visto; ao achar chamadas (N) no texto,
        # associa N → parágrafo; ao achar a nota N no fim, lê o texto da nota.
        par_atual = None
        chamada = {}   # N -> parágrafo
        notas = {}     # N -> texto
        for l in linhas:
            m = re.match(r'^(\d{1,4})\s+\S', l)
            # linha de nota: «(12) Sl 33, 9» ou «12. Sl 33, 9» (o formato é conferido abaixo)
            mn = re.match(r'^\(?(\d{1,4})\)\s+(.*)', l) or re.match(r'^\[(\d{1,4})\]\s+(.*)', l)
            if mn and (mn.group(2)[:2].isupper() or mn.group(2)[:3] in ('Cf ', 'Cf.')) and len(mn.group(2)) < 600 and not m:
                notas.setdefault(int(mn.group(1)), mn.group(2))
                continue
            if m and 1 <= int(m.group(1)) <= 2865:
                par_atual = int(m.group(1))
            for c in re.finditer(r'\((\d{1,4})\)', l):
                chamada.setdefault(int(c.group(1)), par_atual)
        for n, txt in notas.items():
            par = chamada.get(n)
            if par is None:
                continue
            for h, ver in refs_salmo(txt):
                out.setdefault(h, []).append({'par': par, 'nota': n, 'texto': txt, 'ver': ver, 'arquivo': f})
    json.dump(out, open(os.path.join(CACHE, 'indice.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('salmos citados:', len(out), '; citações:', sum(len(v) for v in out.values()))


RE_SL = re.compile(r'\bSl\b\.?\s*([\d][\d,\.\-;\s]*)')


def refs_salmo(txt):
    """Lê «Sl 22, 2; 32, 4; 35» e devolve [(salmo_hebraico, 'versículos' ou '')].
    Devolve só o que vem depois de «Sl»/«Sal» até a próxima sigla de livro."""
    res = []
    for m in re.finditer(r'\b(?:Sl|Sal)\b\.?\s*([^A-Za-zÀ-ÿ]*(?:\d[^A-Za-zÀ-ÿ]*)*)', txt):
        corpo = m.group(1)
        for part in re.split(r';', corpo):
            part = part.strip(' .')
            mm = re.match(r'(\d{1,3})(?:\s*[,\.:]\s*(.*))?', part)
            if mm:
                n = int(mm.group(1))
                if 1 <= n <= 150:
                    res.append((n, (re.match(r'[\d,\.\-\s]*', mm.group(2) or '').group(0)).strip(' ,.-')))
    return res


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'baixar':
        baixar()
    elif cmd == 'indice':
        indice()
    elif cmd == 'mostrar':
        d = json.load(open(os.path.join(CACHE, 'indice.json'), encoding='utf-8'))
        for x in d.get(sys.argv[2], []):
            print(x['par'], x['ver'], '|', x['texto'][:100])
    else:
        print(__doc__)
