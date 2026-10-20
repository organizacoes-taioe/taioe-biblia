"""Funções comuns dos scripts siríacos da pré-pesquisa oriental (ori-siriaco-*.py). Não se roda sozinho.

Fontes (tudo fora do git, em pesquisa/cache/base/):
- sc/: o Digital Syriac Corpus (https://syriaccorpus.org; GitHub srophe/syriac-corpus), ~630 textos TEI.
  O texto siríaco de base é de domínio público (edições do séc. XIX e manuscritos); o TEI é CC BY 4.0
  (James E. Walters et al.). Cada texto abre em https://syriaccorpus.org/<n> e o XML em
  https://raw.githubusercontent.com/srophe/syriac-corpus/main/data/tei/<n>.xml.
- peshitta/: Números e Salmos da Peshitta (ETCBC, https://github.com/ETCBC/peshitta, plain/0.2), só para
  achar citações; 2 Coríntios vem do próprio corpus (sc/data/tei/126.xml).
"""
import os, re, subprocess, sys, urllib.request

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # .../pesquisa
CACHE = os.path.join(RAIZ, 'cache', 'base')
SC = os.path.join(CACHE, 'sc', 'data', 'tei')
PESH = os.path.join(CACHE, 'peshitta')
DATA = '2026-10-20'


def preparar():
    if not os.path.isdir(SC):
        os.makedirs(CACHE, exist_ok=True)
        subprocess.run(['git', '-c', 'core.longpaths=true', 'clone', '--depth', '1', '-q',
                        'https://github.com/srophe/syriac-corpus.git', os.path.join(CACHE, 'sc')], check=True)
    os.makedirs(PESH, exist_ok=True)
    for livro in ('Numbers', 'Psalms'):
        p = os.path.join(PESH, livro + '.txt')
        if not os.path.exists(p):
            u = f'https://raw.githubusercontent.com/ETCBC/peshitta/master/plain/0.2/{livro}.txt'
            urllib.request.urlretrieve(u, p)


LETRAS = re.compile('[ܐ-ܯ]+')
SINAIS = re.compile('[̀-ͯܰ-ݏـ‌‍]')  # vogais, qushshaya, seyame…


def palavras(txt):
    """Só as letras siríacas, sem vogais nem sinais; tira o ܘ («e») do começo da palavra."""
    out = []
    for w in LETRAS.findall(SINAIS.sub('', txt)):
        if len(w) > 1 and w[0] == 'ܘ':
            w = w[1:]
        out.append(w)
    return out


def peshitta_at(livro):
    """{(cap, vers): texto} da Peshitta (ETCBC plain)."""
    txt = open(os.path.join(PESH, livro + '.txt'), encoding='utf-8').read()
    vers, cap, atual = {}, 0, None
    for linha in txt.splitlines():
        m = re.match(r'Chapter (\d+)', linha)
        if m:
            cap = int(m.group(1)); atual = None; continue
        m = re.match(r'(\d+) (.*)', linha)
        if m:
            atual = (cap, int(m.group(1))); vers[atual] = m.group(2)
        elif atual and linha.strip():
            vers[atual] += ' ' + linha.strip()
    return vers


def peshitta_2cor():
    t = open(os.path.join(SC, '126.xml'), encoding='utf-8').read()
    vers = {}
    for cap, corpo in re.findall(r'<div type="chapter" n="(\d+)"[^>]*>(.*?)</div>', t, re.S):
        for v, tx in re.findall(r'<ab type="verse" n="(\d+)">(.*?)</ab>', corpo, re.S):
            vers[(int(cap), int(v))] = re.sub(r'<[^>]+>', '', tx)
    return vers


def limpa(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()


def ler_tei(n):
    """Devolve (meta, blocos). blocos = [(pagina, tipo, texto, seção)] na ordem do texto; notas de rodapé fora."""
    t = open(os.path.join(SC, f'{n}.xml'), encoding='utf-8').read()
    meta = {'n': n}
    m = re.search(r'<titleStmt>\s*<title[^>]*>(.*?)</title>', t, re.S); meta['titulo'] = limpa(m.group(1)) if m else ''
    m = re.search(r'<author[^>]*>(.*?)</author>', t, re.S); meta['autor'] = limpa(m.group(1)) if m else ''
    sd = t[t.find('<sourceDesc'):t.find('</sourceDesc>')]
    ed = re.search(r'<title[^>]*>(.*?)</title>', sd, re.S)
    meta['edicao'] = limpa(ed.group(1)) if ed else ''
    m = re.search(r'<editor[^>]*>(.*?)</editor>', sd, re.S); meta['editor'] = limpa(m.group(1)) if m else ''
    m = re.search(r'<date>(.*?)</date>', sd); meta['data'] = m.group(1) if m else ''
    m = re.search(r'<biblScope unit="vol">(.*?)</biblScope>', sd); meta['vol'] = m.group(1) if m else ''
    m = re.search(r'<ref target="(http[^"]+archive[^"]+)"', sd); meta['archive'] = m.group(1) if m else ''
    m = re.search(r'<msIdentifier>.*?<idno[^>]*>(.*?)</idno>', sd, re.S); meta['ms'] = limpa(m.group(1)) if m else ''
    corpo = t[t.find('<body'):]
    corpo = re.sub(r'<note\b.*?</note>', '', corpo, flags=re.S)
    blocos, pag, sec = [], '', ''
    padrao = r'<pb[^>]*\bn="([^"]+)"[^>]*/>|<div\b[^>]*\btype="(?:section|chapter|stanza|part)"[^>]*\bn="([^"]+)"[^>]*>|<(l|p|ab|head)\b[^>]*>(.*?)</\3>'
    for m in re.finditer(padrao, corpo, re.S):
        if m.group(1):
            pag = limpa(m.group(1)); continue
        if m.group(2):
            sec = m.group(2); continue
        tx = m.group(4)
        partes = re.split(r'<pb[^>]*\bn="([^"]+)"[^>]*/>', tx)  # páginas que mudam dentro do bloco
        primeira = pag
        for i in range(1, len(partes), 2):
            pag = limpa(partes[i])
        blocos.append((primeira, m.group(3), limpa(''.join(partes[::2])), sec))
    return meta, blocos


# Decisão do Gere (20/10/2026): os siríacos fora da comunhão com Roma ficam só como pista.
FORA_DA_COMUNHAO = r'Salibi|Filoxeno|Narsai|Isho|bar Koni'
USO_PISTA = 'só pista: fora da comunhão com Roma; não entra no site (decisão do Gere, 20/10/2026)'


def cabecalho(titulo, campos):
    ordem = ['Autor', 'Obra', 'Passagem', 'Edição', 'Fonte', 'Cobre', 'Oriental', 'Língua', 'Baixado']
    return '\n'.join([f'# {titulo}'] + [f'- {k}: {campos[k]}' for k in ordem])


def gravar(livro, cap, arquivo, titulo, campos, corpo, nota=None, script=None):
    campos = dict(campos)
    campos.setdefault('Oriental', 'sim')
    if re.search(FORA_DA_COMUNHAO, campos.get('Autor', '')):
        campos['Uso'] = USO_PISTA
    campos.setdefault('Baixado', f'{DATA}, por pesquisa/ferramentas/base/{script or os.path.basename(sys.argv[0])}')
    pasta = os.path.join(RAIZ, livro, f'{cap:03d}', 'base')
    os.makedirs(pasta, exist_ok=True)
    txt = cabecalho(titulo, campos) + '\n\n'
    if nota:
        txt += '> ' + nota.strip().replace('\n', '\n> ') + '\n\n'
    txt += corpo.strip('\n') + '\n'
    p = os.path.join(pasta, arquivo)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    return p
