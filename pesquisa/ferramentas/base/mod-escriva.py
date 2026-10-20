"""Obras de São Josemaria Escrivá no escriva.org (original espanhol): download, índice bíblico e pistas por capítulo.

    python -I -X utf8 pesquisa/ferramentas/base/mod-escriva.py baixar     # índices das obras + páginas de capítulo (cache, fora do git)
    python -I -X utf8 pesquisa/ferramentas/base/mod-escriva.py analisar   # monta cache/base/escriva/pontos.json e citacoes.json
    python -I -X utf8 pesquisa/ferramentas/base/mod-escriva.py indice     # grava pesquisa/fontes/escriva-indice.md
    python -I -X utf8 pesquisa/ferramentas/base/mod-escriva.py pistas salmos 33 35 numeros 12 16 2corintios 1 2
                     # grava <livro>/<ccc>/base/_pistas-escriva.md (sem números: todos os capítulos que já têm base/)
    python -I -X utf8 pesquisa/ferramentas/base/mod-escriva.py texto "Sl 36"   # mostra os pontos que citam um capítulo (conferência)
    python -I -X utf8 pesquisa/ferramentas/base/mod-escriva.py sem-ref salmos 33 36 numeros 12 16
                     # latim da Vulgata (drbo.org, cache) achado em pontos SEM referência ao capítulo: lista para conferir à mão

Como o site funciona (ver pesquisa/fontes/escriva.md):
  - /es/<obra>/ é o índice da obra; cada capítulo (/es/<obra>/<capitulo>/) traz TODOS os pontos ou
    parágrafos dele, com o número, o texto, as notas e o bloco «Referencias a la Sagrada Escritura»
    (os links /es/scriptural-reference/<livro>/#...). Por isso baixam-se só os capítulos (~300 páginas),
    não os ~5000 pontos.
  - O endereço de cada ponto é /es/<obra>/<n>/ (nas Cartas, <n> é a ordem global no volume, e o rótulo
    é «Carta nº 2, 20»). Ele vem no próprio capítulo (<a href="/es/<obra>/<n>/" id="ref-<n>">).
  - O site exige cabeçalhos de navegador comuns (User-Agent e Accept); sem eles responde 403.

Citações: 1) o bloco do site (numeração dos Salmos como Escrivá cita, isto é, Vulgata); 2) as notas de
rodapé («Ps XXXV, 10», «Num XXI, 8», «2 Cor IV, 7»), que cobrem livros que o índice do site omite (Números,
Josué, Juízes…); 3) referências entre parênteses no corpo do texto. Tudo vai para o número HEBRAICO nos
Salmos (Vulgata 10–112 e 116–145 = hebraico + 1; 9 = 9–10; 113 = 114–115; 114+115 = 116; 146+147 = 147).
Uma requisição por vez, pausa de 1 s; o que já está no cache não se baixa de novo.
"""
import html, json, os, re, sys, time, urllib.request, urllib.error

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CACHE = os.path.join(RAIZ, 'cache', 'base', 'escriva')
SITE = 'https://escriva.org'
UA = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'es-ES,es;q=0.9',
}

# slug → (título espanhol, título português, sigla)
OBRAS = {
    'camino': ('Camino', 'Caminho', 'C'),
    'surco': ('Surco', 'Sulco', 'S'),
    'forja': ('Forja', 'Forja', 'F'),
    'es-cristo-que-pasa': ('Es Cristo que pasa', 'É Cristo que passa', 'ECP'),
    'amigos-de-dios': ('Amigos de Dios', 'Amigos de Deus', 'AD'),
    'amar-a-la-iglesia': ('Amar a la Iglesia', 'Amar a Igreja', 'AI'),
    'conversaciones': ('Conversaciones', 'Questões atuais do cristianismo (Conversaciones con Mons. Escrivá de Balaguer)', 'Conv'),
    'santo-rosario': ('Santo Rosario', 'Santo Rosário', 'SR'),
    'via-crucis': ('Via Crucis', 'Via-Sacra', 'VC'),
    'en-dialogo-con-el-se%C3%B1or': ('En diálogo con el Señor', 'Em diálogo com o Senhor', 'EDS'),
    'cartas-1': ('Cartas I', 'Cartas I', 'Cartas I'),
    'cartas-2': ('Cartas II', 'Cartas II', 'Cartas II'),
    'carta-29': ('Carta 29', 'Carta 29', 'Carta 29'),
    'josemaria-escriva-de-balaguer-y-la-universidad': ('Josemaría Escrivá de Balaguer y la Universidad', 'Josemaria Escrivá de Balaguer e a Universidade', 'Univ'),
    'la-abadesa-de-las-huelgas': ('La Abadesa de las Huelgas', 'A Abadessa de Las Huelgas', 'Abadesa'),
}

_ultimo = [0.0]


def pega(url, tent=3):
    for i in range(tent):
        espera = 1.0 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                dados = r.read().decode('utf-8', 'replace')
            _ultimo[0] = time.time()
            return dados
        except urllib.error.HTTPError as e:
            _ultimo[0] = time.time()
            if e.code == 404:
                return None
            print('  erro', e.code, url, file=sys.stderr)
            time.sleep(5 * (i + 1))
        except Exception as e:
            _ultimo[0] = time.time()
            print('  erro', e, url, file=sys.stderr)
            time.sleep(5 * (i + 1))
    return None


def arq(caminho):
    """Caminho do site (/es/camino/caracter/) → arquivo do cache."""
    nome = caminho.strip('/').replace('/', '__').replace('%', '_')
    return os.path.join(CACHE, 'html', nome + '.html')


def baixa(caminho):
    p = arq(caminho)
    if os.path.exists(p):
        return open(p, encoding='utf-8').read()
    print('baixando', caminho, flush=True)
    s = pega(SITE + caminho)
    if s is None:
        return None
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)
    return s


def artigo(s):
    a, b = s.find('<article'), s.find('</article>')
    return s[a:b] if a >= 0 else ''


def capitulos(slug):
    s = baixa(f'/es/{slug}/')
    if not s:
        return []
    m = artigo(s)
    return re.findall(r'<a class="([^"]*)" href="(/es/[^"]*)"', m)


def baixar():
    lista = {}
    for slug in OBRAS:
        caps = capitulos(slug)
        lista[slug] = caps
        for classe, cam in caps:
            baixa(cam)
    with open(os.path.join(CACHE, 'capitulos.json'), 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=1)
    print('capítulos:', sum(len(v) for v in lista.values()))


# ---------------------------------------------------------------- análise

def limpa(t):
    t = re.sub(r'<a [^>]*class="note"[^>]*>.*?</a>', lambda m: '[^' + re.sub(r'\D', '', re.sub('<[^>]+>', '', m.group(0))) + ']', t, flags=re.S)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'</p>|</h[1-6]>|</li>|</blockquote>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t).replace('﻿', '').replace('\xa0', ' ')
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r' *\n *', '\n', t)
    return re.sub(r'\n{2,}', '\n', t).strip()


def paragrafos(t):
    """HTML de um ponto → lista de parágrafos limpos."""
    ps = re.findall(r'<(p|h[2-6]|li|blockquote)[^>]*>(.*?)</\1>', t, flags=re.S)
    out = []
    for tag, x in ps:
        x = limpa(x)
        if x:
            out.append(('## ' if tag.startswith('h') else '') + x)
    if not out:
        x = limpa(t)
        if x:
            out = x.split('\n')
    return out


def pontos_da_pagina(slug, cam, s):
    """Divide a página de capítulo em pontos: [{n, url, rotulo, paragrafos, notas, refs_site}]."""
    m = artigo(s)
    titulo = limpa((re.search(r'<h1 class="title">(.*?)</h1>', m, flags=re.S) or re.search(r'<h1[^>]*>(.*?)</h1>', m, flags=re.S) or [None, ''])[1] if re.search(r'<h1', m) else '')
    desc = re.search(r'<div class="chapter-description">(.*?)</div>', m, flags=re.S)
    desc = limpa(desc.group(1)) if desc else ''
    corpo_fim = m.find('<div class="bottom-block">')
    corpo = m[:corpo_fim] if corpo_fim >= 0 else m
    rodape = m[corpo_fim:] if corpo_fim >= 0 else ''
    # notas: id _ftnN → texto
    notas = {}
    for n, t in re.findall(r'id="_ftn(\d+)" class="note">.*?</a><span>(.*?)</span></div>', rodape, flags=re.S):
        notas[n] = limpa(t)
    # blocos de rodapé por ponto: «Punto N» … refs do site
    refs_site = {}
    blocos = re.split(r'<div class="notespoint"><a href="#ref-([^"]+)"', rodape)
    for i in range(1, len(blocos), 2):
        rid = blocos[i]
        refs = re.findall(r'href="/es/scriptural-reference/(\d+)/#([^"]*)"><span>(.*?)</span>', blocos[i + 1])
        refs_site[rid] = [(lv, anc, limpa(rot)) for lv, anc, rot in refs]
    # páginas sem «Punto N» (um ponto só): refs soltas
    if not refs_site:
        refs = re.findall(r'href="/es/scriptural-reference/(\d+)/#([^"]*)"><span>(.*?)</span>', rodape)
        if refs:
            refs_site['*'] = [(lv, anc, limpa(rot)) for lv, anc, rot in refs]
    # pontos
    marcas = list(re.finditer(r'<div class="point-number[^"]*"><h2><a href="(/es/[^"]+)" id="ref-([^"]+)"[^>]*>(.*?)</a></h2>', corpo))
    pontos = []
    if not marcas:
        # capítulo sem pontos numerados (intros, Abadesa): um bloco só
        txt = corpo[corpo.find('</h1>') + 5:] if '</h1>' in corpo else corpo
        pontos.append({'n': '', 'url': SITE + cam, 'rotulo': titulo, 'html': txt, 'rid': '*'})
    else:
        for i, mk in enumerate(marcas):
            fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(corpo)
            pontos.append({'n': limpa(mk.group(3)), 'url': SITE + mk.group(1), 'rotulo': limpa(mk.group(3)), 'html': corpo[mk.end():fim], 'rid': mk.group(2)})
    out = []
    for p in pontos:
        h = p.pop('html')
        ns = re.findall(r'href="#_ftn(\d+)" class="note"', h)
        p['paragrafos'] = paragrafos(h)
        p['notas'] = {n: notas.get(n, '') for n in ns}
        p['refs_site'] = refs_site.get(p.pop('rid'), refs_site.get('*', []))
        p['capitulo'] = titulo
        p['descricao'] = desc
        p['pagina'] = SITE + cam
        out.append(p)
    return out


# --- livros: siglas das notas (latinas e espanholas) → (id, nome pt)
LIVROS = [
    ('gn', 'Gênesis', 'Gen Gn Génesis Genesis'), ('ex', 'Êxodo', 'Ex Exod Éxodo Exodo'),
    ('lv', 'Levítico', 'Lev Lv Levítico'), ('nm', 'Números', 'Num Nm Núm Numeri Números'),
    ('dt', 'Deuteronômio', 'Deut Dt Deuteronomio'), ('js', 'Josué', 'Ios Jos Josue Josué Iosue'),
    ('jz', 'Juízes', 'Iud Jud Jue Iudic Jueces Judic'), ('rt', 'Rute', 'Ruth Rut Rt'),
    ('1sm', '1 Samuel', '1 Sam|1 Sm|1 S|1 Reg|I Reg|I Sam|1 Samuel'), ('2sm', '2 Samuel', '2 Sam|2 Sm|2 S|2 Reg|II Reg|II Sam|2 Samuel'),
    ('1rs', '1 Reis', '1 Re|1 R|1 Rg|3 Reg|III Reg|1 Reyes|I Re|1 Reg_'), ('2rs', '2 Reis', '2 Re|2 R|2 Rg|4 Reg|IV Reg|2 Reyes|II Re'),
    ('1cr', '1 Crônicas', '1 Par|1 Cro|1 Cr|I Par|1 Crónicas|1 Chr'), ('2cr', '2 Crônicas', '2 Par|2 Cro|2 Cr|II Par|2 Crónicas|2 Chr'),
    ('esd', 'Esdras', 'Esd Esdr Esdras'), ('ne', 'Neemias', 'Neh Ne Nehemías|2 Esd|II Esd'), ('tb', 'Tobias', 'Tob Tb Tobías'),
    ('jt', 'Judite', 'Iudith Idt Jdt Judit'), ('est', 'Ester', 'Est Esth Ester'),
    ('1mc', '1 Macabeus', '1 Mac|1 Mach|I Mach|1 Macabeos'), ('2mc', '2 Macabeus', '2 Mac|2 Mach|II Mach|2 Macabeos'),
    ('jo', 'Jó', 'Iob Job Jb'), ('sl', 'Salmos', 'Ps Sal Salmo Salmos Psalm Psal Sl'), ('pr', 'Provérbios', 'Prov Pr Prv Proverbios'),
    ('ecl', 'Eclesiastes', 'Eccl Eccle Ecl Qo Coh Eclesiastés Ecle'), ('ct', 'Cântico dos Cânticos', 'Cant Can Ct Cantar'),
    ('sb', 'Sabedoria', 'Sap Sab Sb Sabiduría'), ('eclo', 'Eclesiástico', 'Eccli Ecclo Eclo Sir Si Eclesiástico Ecclus'),
    ('is', 'Isaías', 'Is Isai Isa Isaías'), ('jr', 'Jeremias', 'Ier Jer Jr Ierem Jeremías'), ('lm', 'Lamentações', 'Lam Lm Thren Lamentaciones'),
    ('br', 'Baruc', 'Bar Ba Baruc'), ('ez', 'Ezequiel', 'Ez Ezech Ezeq Ezequiel'), ('dn', 'Daniel', 'Dan Dn Daniel'),
    ('os', 'Oseias', 'Os Hos Oseas'), ('jl', 'Joel', 'Ioel Joel Jl'), ('am', 'Amós', 'Am Amos Amós'), ('ab', 'Abdias', 'Abd Ab'),
    ('jn', 'Jonas', 'Ion Jon Jonás'), ('mq', 'Miqueias', 'Mich Mi Miq Miqueas'), ('na', 'Naum', 'Nah Na Nahum'),
    ('hab', 'Habacuc', 'Hab Ha Habacuc'), ('sf', 'Sofonias', 'Soph Sof Sophon Sofonías'), ('ag', 'Ageu', 'Agg Ag Hag Ageo'),
    ('zc', 'Zacarias', 'Zach Za Zac Zacarías'), ('ml', 'Malaquias', 'Mal Ml Malaquías'),
    ('mt', 'Mateus', 'Mt Matth Mat Mateo'), ('mc', 'Marcos', 'Mc Mk Mar Marc Marcos'), ('lc', 'Lucas', 'Lc Lk Luc Lucas'),
    ('jo4', 'João', 'Ioh Io Ioan Jn Joh Ioann Juan'), ('at', 'Atos', 'Act Hch Hech Hechos Acta'), ('rm', 'Romanos', 'Rom Rm Romanos'),
    ('1cor', '1 Coríntios', '1 Cor|I Cor|1 Co|1 Corintios'), ('2cor', '2 Coríntios', '2 Cor|II Cor|2 Co|2 Corintios'),
    ('gl', 'Gálatas', 'Gal Galat Ga Gálatas'), ('ef', 'Efésios', 'Eph Ephes Ef Efesios'), ('fl', 'Filipenses', 'Phil Philip Flp Fil Filipenses Philipp'),
    ('cl', 'Colossenses', 'Col Colosenses'), ('1ts', '1 Tessalonicenses', '1 Thes|1 Thess|I Thes|1 Tes|1 Ts|1 Tesalonicenses'),
    ('2ts', '2 Tessalonicenses', '2 Thes|2 Thess|II Thes|2 Tes|2 Ts|2 Tesalonicenses'), ('1tm', '1 Timóteo', '1 Tim|I Tim|1 Tm|1 Timoteo'),
    ('2tm', '2 Timóteo', '2 Tim|II Tim|2 Tm|2 Timoteo'), ('tt', 'Tito', 'Tit Tt Tito'), ('fm', 'Filêmon', 'Philem Flm Phlm Filemón'),
    ('hb', 'Hebreus', 'Hebr Heb Hb Hebreos'), ('tg', 'Tiago', 'Iac Sant St Jac Iacob Santiago Jas'),
    ('1pd', '1 Pedro', '1 Pet|1 Petr|I Petr|I Pet|1 Pe|1 P|1 Pedro'), ('2pd', '2 Pedro', '2 Pet|2 Petr|II Petr|II Pet|2 Pe|2 P|2 Pedro'),
    ('1jo', '1 João', '1 Ioh|1 Io|I Ioh|1 Jn|1 Joh|1 Juan|I Io'), ('2jo', '2 João', '2 Ioh|2 Io|II Ioh|2 Jn|2 Juan'),
    ('3jo', '3 João', '3 Ioh|3 Io|III Ioh|3 Jn|3 Juan'), ('jd', 'Judas', 'Iud_|Jds Judas Iudae'), ('ap', 'Apocalipse', 'Apoc Ap Apc Rev Apocalipsis'),
]
ORDEM = {lid: i for i, (lid, _, _) in enumerate(LIVROS)}
# número de capítulos (Nova Vulgata; Salmos até 150), para descartar números que não são referência
NCAP = dict(zip('gn ex lv nm dt js jz rt 1sm 2sm 1rs 2rs 1cr 2cr esd ne tb jt est 1mc 2mc jo sl pr ecl ct sb eclo is jr lm br ez dn '
                'os jl am ab jn mq na hab sf ag zc ml mt mc lc jo4 at rm 1cor 2cor gl ef fl cl 1ts 2ts 1tm 2tm tt fm hb tg 1pd 2pd '
                '1jo 2jo 3jo jd ap'.split(),
                [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 14, 16, 10, 16, 15, 42, 150, 31, 12, 8, 19, 51, 66,
                 52, 5, 6, 48, 14, 14, 4, 9, 1, 4, 7, 3, 3, 3, 2, 14, 3, 28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3,
                 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]))
NOME = {lid: nome for lid, nome, _ in LIVROS}
# nome da pasta de pesquisa
PASTA = {'sl': 'salmos', 'nm': 'numeros', '2cor': '2corintios'}
ABREV = {'sl': 'Sl', 'nm': 'Nm', '2cor': '2Cor'}

SIGLAS, FORMAS = {}, set()
for lid, _, s in LIVROS:
    partes = []
    for bloco in s.split('|'):
        if re.match(r'(\d|I{1,3}|IV)\s', bloco):
            partes.append(bloco)  # sigla de duas palavras («1 Sam», «II Reg»)
        else:
            partes.extend(bloco.split())
    for p in partes:
        p = p.strip().rstrip('_')
        if p:
            SIGLAS.setdefault(p.lower().replace('.', ''), lid)
            FORMAS.add(p)
# a sigla tem de vir com maiúscula, como nas notas («Num», «Sal»): assim «números 809» ou «sal» não contam
SIG_RE = '|'.join(sorted((re.escape(k) for k in FORMAS), key=len, reverse=True))

ROM = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def rom(s):
    s = s.upper()
    if not s or any(c not in ROM for c in s):
        return None
    tot = 0
    for i, c in enumerate(s):
        v = ROM[c]
        if i + 1 < len(s) and ROM[s[i + 1]] > v:
            tot -= v
        else:
            tot += v
    return tot


def num(s):
    s = s.strip().rstrip('.')
    if s.isdigit():
        return int(s)
    return rom(s)


def sl_versos(vulg, hebr, vs):
    """Versículos que mudam de número com a divisão dos salmos (Vulg. 9 → Sl 10; 113 → 115; 115 → 116; 147 → 147)."""
    if vulg == 9 and hebr == 10:
        return [v - 21 for v in vs if v > 21]
    if vulg == 113 and hebr == 115:
        return [v - 8 for v in vs if v > 8]
    if vulg == 115:
        return [v + 9 for v in vs]
    if vulg == 147:
        return [v + 11 for v in vs]
    return vs


def sl_hebr(vulg, v=None):
    """Salmo da Vulgata → hebraico (versículo conservado; diferenças de versículo dos títulos não se corrigem)."""
    if vulg <= 8 or vulg >= 148:
        return vulg
    if vulg == 9:
        return 9 if (v is None or v <= 21) else 10
    if vulg <= 112:
        return vulg + 1
    if vulg == 113:
        return 114 if (v is None or v <= 8) else 115
    if vulg in (114, 115):
        return 116
    if vulg <= 145:
        return vulg + 1
    if vulg in (146, 147):
        return 147
    return vulg


CAP_RE = r'([IVXLC]+|\d+)'
REF_RE = re.compile(r'(?<![A-Za-zÁ-ú])(' + SIG_RE + r')\.?\s+' + CAP_RE + r'(?:\s*[\[(](\d+)[\])])?\s*(?:,|:)\s*(\d+[a-z]?(?:\s*[-–]\s*\d+)?(?:\s*\.\s*\d+(?:\s*[-–]\s*\d+)?)*)')


def versos(txt):
    out = []
    for parte in re.split(r'\s*\.\s*', txt):
        m = re.match(r'(\d+)[a-z]?(?:\s*[-–]\s*(\d+))?', parte)
        if m:
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
            if b < a or b - a > 60:
                b = a
            out.extend(range(a, b + 1))
    return out


def refs_de_texto(t, numeracao_sl='vulg'):
    """Acha referências numa nota ou num parêntese. Segue «Mt XIV, 31; XVI, 8» (capítulos seguintes do mesmo livro).
    Devolve [(livro, cap_hebr, [versos], 'Ps XXXV, 10' original)]."""
    out = []
    t = t.replace('–', '-').replace('—', '-')
    pos = 0
    for m in REF_RE.finditer(t):
        sig = m.group(1).lower().replace('.', '')
        lid = SIGLAS.get(sig)
        if not lid:
            continue
        cap = num(m.group(2))
        if not cap or cap > NCAP.get(lid, 150):
            continue
        vs = versos(m.group(4))
        alt = int(m.group(3)) if m.group(3) else None
        if lid == 'sl' and alt and alt == cap - 1:
            cap = -cap  # «Sal 43[42]»: o primeiro número já é o hebraico (marcado com sinal negativo)
        out.append((lid, cap, vs, m.group(0)))
        # continuações: «; XVI, 8; XVII, 19»
        resto = t[m.end():]
        while True:
            c = re.match(r'\s*;\s*' + CAP_RE + r'\s*,\s*(\d+[a-z]?(?:\s*[-–]\s*\d+)?(?:\s*\.\s*\d+(?:\s*[-–]\s*\d+)?)*)', resto)
            if not c:
                break
            cap2 = num(c.group(1))
            if not cap2:
                break
            out.append((lid, cap2, versos(c.group(2)), c.group(0).strip('; ')))
            resto = resto[c.end():]
    res = []
    for lid, cap, vs, orig in out:
        if lid == 'sl' and cap < 0:
            res.append((lid, -cap, vs, orig, sl_hebr_inv(-cap)))
        elif lid == 'sl':
            hebr = cap if numeracao_sl == 'hebr' else sl_hebr(cap, vs[0] if vs else None)
            res.append((lid, hebr, sl_versos(cap, hebr, vs), orig, cap))
        else:
            res.append((lid, cap, vs, orig, None))
    return res


# livros do índice do site: id numérico → nosso id (ordem da Nova Vulgata, 0 = Gênesis)
SITE_LIVRO = {i: lid for i, lid in enumerate(
    'gn ex lv nm dt js jz rt 1sm 2sm 1rs 2rs 1cr 2cr esd ne tb jt est 1mc 2mc jo sl pr ecl ct sb eclo is jr lm br ez dn os jl am ab jn mq na hab sf ag zc ml '
    'mt mc lc jo4 at rm 1cor 2cor gl ef fl cl 1ts 2ts 1tm 2tm tt fm hb tg 1pd 2pd 1jo 2jo 3jo jd ap'.split())}


def refs_do_site(refs, conv='vulg'):
    """Bloco «Referencias a la Sagrada Escritura» do site. O rótulo («Salmos 56, 2–3») dá capítulo e versículos.
    A numeração dos Salmos no site segue a da edição de cada obra: Vulgata nas que citam «Ps XXXV»
    (e em «En diálogo con el Señor»), hebraica nas Cartas («Sal 56[55]»). `conv` diz qual (ver CONV_SITE)."""
    out = []
    for lv, anc, rot in refs:
        lid = SITE_LIVRO.get(int(lv))
        m = re.search(r'(\d+)(?:\s*,\s*(\d+)(?:\s*[-–]\s*(\d+))?)?\s*$', rot)
        if not lid or not m:
            continue
        cap = int(m.group(1))
        a = int(m.group(2)) if m.group(2) else None
        b = int(m.group(3)) if m.group(3) else a
        vs = list(range(a, (b or a) + 1)) if a and b and b >= a and b - a <= 60 else ([a] if a else [])
        if lid == 'sl' and conv == 'vulg':
            h = sl_hebr(cap, a)
            out.append((lid, h, sl_versos(cap, h, vs), 'site: ' + rot, cap))
        elif lid == 'sl':
            out.append((lid, cap, vs, 'site: ' + rot, sl_hebr_inv(cap)))
        else:
            out.append((lid, cap, vs, 'site: ' + rot, None))
    return out


# numeração dos Salmos no índice do site, por obra (conferida em 2026-10-20 com as notas e o texto)
CONV_SITE = {'cartas-1': 'hebr', 'cartas-2': 'hebr', 'carta-29': 'hebr'}


# citações sem referência (nem nota, nem índice do site), achadas pelo `sem-ref` e por busca de frases
# em espanhol; conferidas à mão. URL do ponto → [(livro, capítulo hebraico, versículos, o que diz o texto)]
MANUAIS = {
    SITE + '/es/camino/842/': [('2cor', 2, [15], '«Es el buen olor de Cristo» (sem referência)')],
    SITE + '/es/cartas-2/230/': [('2cor', 2, [15], '«bonus odor Christi» (sem referência)')],
}


def analisar():
    lista = json.load(open(os.path.join(CACHE, 'capitulos.json'), encoding='utf-8'))
    pontos = []
    for slug, caps in lista.items():
        for classe, cam in caps:
            s = open(arq(cam), encoding='utf-8').read() if os.path.exists(arq(cam)) else None
            if not s:
                print('falta', cam)
                continue
            intro = '/intro/' in cam
            for p in pontos_da_pagina(slug, cam, s):
                p['obra'] = slug
                p['intro'] = intro
                pontos.append(p)
    # citações
    cits = []
    for i, p in enumerate(pontos):
        achou = {}
        for lid, cap, vs, orig, vulg in refs_do_site(p['refs_site'], CONV_SITE.get(p['obra'], 'vulg')):
            achou.setdefault((lid, cap, tuple(vs)), {'origem': set(), 'orig': [], 'vulg': vulg})
            achou[(lid, cap, tuple(vs))]['origem'].add('site')
            achou[(lid, cap, tuple(vs))]['orig'].append(orig)
        for n, nt in p['notas'].items():
            for lid, cap, vs, orig, vulg in refs_de_texto(nt):
                k = (lid, cap, tuple(vs))
                achou.setdefault(k, {'origem': set(), 'orig': [], 'vulg': vulg})
                achou[k]['origem'].add('nota ' + n)
                achou[k]['orig'].append(orig)
        corpo = '\n'.join(p['paragrafos'])
        for par in re.findall(r'\(([^()]{3,80})\)', corpo):
            for lid, cap, vs, orig, vulg in refs_de_texto(par):
                k = (lid, cap, tuple(vs))
                achou.setdefault(k, {'origem': set(), 'orig': [], 'vulg': vulg})
                achou[k]['origem'].add('texto')
                achou[k]['orig'].append(orig)
        for lid, cap, vs, orig in MANUAIS.get(p['url'], []):
            k = (lid, cap, tuple(vs))
            achou.setdefault(k, {'origem': set(), 'orig': [], 'vulg': sl_hebr_inv(cap) if lid == 'sl' else None})
            achou[k]['origem'].add('sem ref.')
            achou[k]['orig'].append(orig)
        for (lid, cap, vs), d in achou.items():
            cits.append({'p': i, 'livro': lid, 'cap': cap, 'versos': list(vs), 'vulg': d['vulg'],
                         'origem': sorted(d['origem']), 'orig': sorted(set(d['orig']))})
    os.makedirs(CACHE, exist_ok=True)
    json.dump(pontos, open(os.path.join(CACHE, 'pontos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    json.dump(cits, open(os.path.join(CACHE, 'citacoes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('pontos:', len(pontos), 'citações:', len(cits))
    por_livro = {}
    for c in cits:
        por_livro[c['livro']] = por_livro.get(c['livro'], 0) + 1
    print(sorted(por_livro.items(), key=lambda x: ORDEM[x[0]]))


def carrega():
    pontos = json.load(open(os.path.join(CACHE, 'pontos.json'), encoding='utf-8'))
    cits = json.load(open(os.path.join(CACHE, 'citacoes.json'), encoding='utf-8'))
    return pontos, cits


def juntar(cits):
    """Junta as citações do mesmo ponto e capítulo: versos unidos, origens unidas.
    Uma citação só do site sem versículo é absorvida pela da nota."""
    grupos = {}
    for c in cits:
        k = (c['p'], c['livro'], c['cap'])
        g = grupos.setdefault(k, {'p': c['p'], 'livro': c['livro'], 'cap': c['cap'], 'versos': set(), 'origem': set(), 'orig': set(), 'vulg': c['vulg']})
        g['versos'].update(c['versos'])
        g['origem'].update(c['origem'])
        g['orig'].update(c['orig'])
    # erro de digitação na nota («Jn 26,23») corrigido pelo índice do site (mesmo ponto, livro e versículos,
    # capítulo diferente): vale o do site, que é revisado
    lst = list(grupos.values())
    fora = set()
    for a in lst:
        if a['origem'] != {'site'}:
            continue
        for b in lst:
            if b is not a and b['p'] == a['p'] and b['livro'] == a['livro'] and 'site' not in b['origem'] \
                    and b['versos'] and b['versos'] == a['versos']:
                a['origem'] |= {o + ' (cap. corrigido)' for o in b['origem']}
                a['orig'] |= b['orig']
                fora.add(id(b))
    return [g for g in lst if id(g) not in fora]


def rotulo_ponto(p):
    t, _, sig = OBRAS[p['obra']]
    if p['obra'].startswith('carta'):
        # rótulo das Cartas: «Carta nº 2, 20» vem do capítulo («Carta nº 2») + número
        cap = p['capitulo']
        return f"{t}, {cap}, n. {p['n']}" if p['n'] else f"{t}, {cap}"
    if p['intro']:
        return f"{t}, {p['capitulo']} (introdução)"
    if not p['n']:
        return f"{t}, {p['capitulo']}"
    return f"{t}, n. {p['n']}"


def fmt_vs(vs):
    vs = sorted(vs)
    if not vs:
        return ''
    out, a, b = [], vs[0], vs[0]
    for v in vs[1:]:
        if v == b + 1:
            b = v
        else:
            out.append(f'{a}' if a == b else f'{a}–{b}')
            a = b = v
    out.append(f'{a}' if a == b else f'{a}–{b}')
    return ', '.join(out)


def indice():
    pontos, cits = carrega()
    gs = [g for g in juntar(cits) if not pontos[g['p']]['intro'] or 'autor' in pontos[g['p']]['capitulo'].lower()]
    por = {}
    for g in gs:
        por.setdefault(g['livro'], {}).setdefault(g['cap'], []).append(g)
    L = ['# São Josemaria Escrivá: índice bíblico (escriva.org, espanhol)', '',
         'Gerado por `pesquisa/ferramentas/base/mod-escriva.py indice`; não editar à mão. Método e obras em `escriva.md`.',
         'Salmos na numeração **hebraica** (Escrivá cita pela Vulgata: «Ps XXXV» = Sl 36; o número dele vai entre',
         'colchetes). Cada linha: versículos → obra, ponto (link) e de onde veio a referência (nota, site, texto).', '']
    total = 0
    for lid in sorted(por, key=lambda x: ORDEM[x]):
        L.append(f'## {NOME[lid]}')
        L.append('')
        for cap in sorted(por[lid]):
            itens = sorted(por[lid][cap], key=lambda g: (min(g['versos']) if g['versos'] else 0, list(OBRAS).index(pontos[g['p']]['obra']), g['p']))
            L.append(f'### {NOME[lid]} {cap}')
            for g in itens:
                p = pontos[g['p']]
                v = fmt_vs(g['versos']) or '(capítulo)'
                vul = f" [Vulg. {g['vulg']}]" if lid == 'sl' and g['vulg'] and g['vulg'] != cap else ''
                ori = ', '.join(sorted({o.split()[0] for o in g['origem']}))
                L.append(f"- {v}{vul}: [{rotulo_ponto(p)}]({p['url']}) ({ori})")
                total += 1
            L.append('')
    L.insert(5, f'{total} entradas (ponto × capítulo bíblico), {len(por)} livros.')
    L.insert(6, '')
    with open(os.path.join(RAIZ, 'fontes', 'escriva-indice.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    print('índice:', total, 'entradas')


def trecho(p, g):
    """Texto a guardar: o ponto inteiro; se for longo (homilia, carta), só os parágrafos com a nota ou a referência."""
    pars = p['paragrafos']
    tot = sum(len(x) for x in pars)
    if tot <= 2500:
        return pars, False
    marcas = set()
    for o in g['origem']:
        if o.startswith('nota '):
            marcas.add('[^' + o.split()[1] + ']')
    escolhidos = []
    for i, x in enumerate(pars):
        if any(m in x for m in marcas):
            escolhidos.append(i)
        elif 'texto' in g['origem'] and any(o in x for o in g['orig']):
            escolhidos.append(i)
    if not escolhidos:
        return pars, False
    return [pars[i] for i in sorted(set(escolhidos))], True


def pistas(alvos):
    pontos, cits = carrega()
    gs = juntar(cits)
    for livro_pasta, cap in alvos:
        lid = {v: k for k, v in PASTA.items()}[livro_pasta]
        itens = [g for g in gs if g['livro'] == lid and g['cap'] == cap]
        itens.sort(key=lambda g: (min(g['versos']) if g['versos'] else 0, list(OBRAS).index(pontos[g['p']]['obra']), g['p']))
        base = os.path.join(RAIZ, livro_pasta, f'{cap:03d}', 'base')
        os.makedirs(base, exist_ok=True)
        ab = ABREV[lid]
        if lid == 'sl':
            vul = sl_hebr_inv(cap)
            tit = f'# Pistas de São Josemaria Escrivá: {ab} {cap} (hebraico) = Sl {vul} (Vulgata, como ele cita)'
        else:
            tit = f'# Pistas de São Josemaria Escrivá: {ab} {cap}'
        L = [tit, '',
             'Obras de São Josemaria no escriva.org, original espanhol. O Gere tem autorização do Opus Dei para usar os textos,',
             'com o link do escriva.org. Gerado por `pesquisa/ferramentas/base/mod-escriva.py pistas` (2026-10-20); índice geral',
             'em `pesquisa/fontes/escriva-indice.md`. «nota» = nota de rodapé da edição; «site» = índice bíblico do escriva.org;',
             '«texto» = referência no corpo. Nos pontos longos (homilias, cartas) vão só os parágrafos onde está a citação.', '']
        if not itens:
            L.append('- Nenhum ponto cita este capítulo (nem nas notas, nem no índice do site, nem no texto).')
        for g in itens:
            p = pontos[g['p']]
            v = fmt_vs(g['versos']) or 'o capítulo, sem versículo'
            L.append(f"## {rotulo_ponto(p)}: {ab} {cap},{v}" if g['versos'] else f"## {rotulo_ponto(p)}: {ab} {cap} ({v})")
            L.append(f"- Obra: {OBRAS[p['obra']][1]} ({OBRAS[p['obra']][0]}); capítulo «{p['capitulo']}»" + (f"; {p['descricao']}" if p['descricao'] else ''))
            L.append(f"- Ponto: {p['rotulo'] or '(sem número)'}; URL: {p['url']}")
            L.append(f"- Referência: {'; '.join(g['orig'])} ({', '.join(g['origem'])})")
            pars, cortado = trecho(p, g)
            notas_usadas = {}
            L.append('')
            if cortado:
                L.append('*(parágrafos do ponto que trazem a citação)*')
                L.append('')
            for x in pars:
                L.append('> ' + x)
                L.append('>')
                for n in re.findall(r'\[\^(\d+)\]', x):
                    notas_usadas[n] = p['notas'].get(n, '')
            if L[-1] == '>':
                L.pop()
            if notas_usadas:
                L.append('')
                for n, t in notas_usadas.items():
                    L.append(f'[^{n}]: {t}')
            L.append('')
        with open(os.path.join(base, '_pistas-escriva.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(L).rstrip() + '\n')
        print(livro_pasta, cap, len(itens), 'pontos')


def sl_hebr_inv(h):
    for v in range(1, 151):
        if sl_hebr(v) == h:
            return v
    return h


def texto(ref):
    m = re.match(r'(\w+)\s+(\d+)', ref)
    lid = {'Sl': 'sl', 'Nm': 'nm', '2Cor': '2cor'}.get(m.group(1), m.group(1).lower())
    cap = int(m.group(2))
    pontos, cits = carrega()
    for g in juntar(cits):
        if g['livro'] == lid and g['cap'] == cap:
            p = pontos[g['p']]
            print('==', rotulo_ponto(p), fmt_vs(g['versos']), p['url'], g['orig'])


# ---------------------------------------------------------------- citações sem referência (latim da Vulgata)
# Vulgata Clementina (a que Escrivá cita) em drbo.org: lvb/chapter/<livro 2 díg.><cap 3 díg.>.htm
DRBO_LIVRO = {'sl': 21, 'nm': 4, '2cor': 54}
PARAR = set('et in ad a ab de ex e cum non est sunt qui quae quod ut me mihi te tibi se sibi eius eum ea nos vos meus mea tuus tua '
            'sicut super sub per pro quia enim autem sed vel aut nec neque si dominus domini domino deus dei deo'.split())


def vulgata(lid, cap_vulg):
    cam = f'/lvb/chapter/{DRBO_LIVRO[lid]:02d}{cap_vulg:03d}.htm'
    p = os.path.join(CACHE, 'vulgata', cam.strip('/').replace('/', '__'))
    if os.path.exists(p):
        s = open(p, encoding='utf-8').read()
    else:
        print('baixando drbo', cam, flush=True)
        s = pega('https://www.drbo.org' + cam)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(s)
    vs = {}
    for n, t in re.findall(r'<a class=vn [^>]*>&nbsp;\s*(\d+)&nbsp;</a>(.*?)(?=<a class=vn|</td>|<p class=desc|$)', s, flags=re.S):
        vs[int(n)] = limpa(t)
    return vs


def norm_lat(t):
    t = t.lower().replace('j', 'i').replace('v', 'u').replace('æ', 'ae').replace('œ', 'oe')
    t = re.sub(r'[áàâ]', 'a', t); t = re.sub(r'[éèê]', 'e', t); t = re.sub(r'[íìî]', 'i', t)
    t = re.sub(r'[óòô]', 'o', t); t = re.sub(r'[úùû]', 'u', t)
    return re.findall(r'[a-z]+', t)


def sem_ref(alvos):
    """Procura no corpus trechos latinos da Vulgata dos capítulos-alvo (4 palavras seguidas, ao menos 2 não triviais)
    em pontos que NÃO têm referência a esse capítulo. Só lista: a conferência é manual."""
    pontos, cits = carrega()
    ja = {(g['p'], g['livro'], g['cap']) for g in juntar(cits)}
    for livro_pasta, cap in alvos:
        lid = {v: k for k, v in PASTA.items()}[livro_pasta]
        cv = sl_hebr_inv(cap) if lid == 'sl' else cap
        vs = vulgata(lid, cv)
        grams = {}
        for v, t in vs.items():
            w = norm_lat(t)
            for i in range(len(w) - 3):
                g = tuple(w[i:i + 4])
                if sum(1 for x in g if x not in PARAR and len(x) > 3) >= 2:
                    grams.setdefault(g, v)
        for i, p in enumerate(pontos):
            if (i, lid, cap) in ja:
                continue
            w = norm_lat(' '.join(p['paragrafos']))
            hits = {}
            for j in range(len(w) - 3):
                g = tuple(w[j:j + 4])
                if g in grams:
                    hits.setdefault(grams[g], ' '.join(g))
            if hits:
                print(f'{livro_pasta} {cap} | {rotulo_ponto(p)} | {p["url"]} | ' + '; '.join(f'v{v}: {h}' for v, h in sorted(hits.items())))


def alvos_padrao():
    out = []
    for pasta in sorted(set(PASTA.values())):
        d = os.path.join(RAIZ, pasta)
        for c in sorted(os.listdir(d)):
            if c.isdigit() and os.path.isdir(os.path.join(d, c, 'base')):
                out.append((pasta, int(c)))
    return out


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'baixar':
        baixar()
    elif cmd == 'analisar':
        analisar()
    elif cmd == 'indice':
        indice()
    elif cmd == 'pistas':
        args = sys.argv[2:]
        alvos = []
        i = 0
        while i < len(args):
            pasta = args[i]
            a, b = int(args[i + 1]), int(args[i + 2])
            alvos += [(pasta, c) for c in range(a, b + 1)]
            i += 3
        if not alvos:
            alvos = alvos_padrao()
        pistas(alvos)
    elif cmd == 'texto':
        texto(sys.argv[2])
    elif cmd == 'sem-ref':
        args = sys.argv[2:]
        alvos = [(args[i], c) for i in range(0, len(args), 3) for c in range(int(args[i + 1]), int(args[i + 2]) + 1)]
        sem_ref(alvos)
    else:
        print(__doc__)
