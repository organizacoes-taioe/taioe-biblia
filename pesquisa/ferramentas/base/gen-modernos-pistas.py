"""Pré-pesquisa do Gênesis, grupo modernos: pistas por capítulo no Catecismo, em São Josemaria Escrivá e na liturgia da Missa.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-modernos-pistas.py baixar     # Catecismo e tabelas do Lecionário (cache)
    python3 -I -X utf8 pesquisa/ferramentas/base/gen-modernos-pistas.py 3-50       # grava genesis/<ccc>/base/_pistas-modernos.md
    python3 -I -X utf8 pesquisa/ferramentas/base/gen-modernos-pistas.py --ver 22   # só mostra na tela o que acharia para Gn 22

Só pistas (número do parágrafo ou do ponto, a citação bíblica e o link): o Catecismo e as obras de Escrivá têm direito
autoral e não se copiam aqui. O que o script escreve fica entre «<!-- automático -->» e «<!-- fim do automático -->»;
o que a pesquisa do capítulo escrever à mão fora dos marcadores é mantido (num arquivo antigo sem marcadores, a parte
automática vai para o fim). Não rodar para Gn 1 e 2 sem conferir: os dois têm pistas feitas à mão.

Fontes (cache em pesquisa/cache/genesis/modernos/, fora do git; uma requisição por vez, pausa de 1 s):
  - Catecismo da Igreja Católica, texto oficial em português (europeu) no vatican.va
    (https://www.vatican.va/archive/cathechism_po/index_new/prima-pagina-cic_po.html; 27 páginas, ISO-8859-1), em
    catecismo/. Liga cada nota «(N)» ao parágrafo que a chama, como o mod-catecismo.py (que só lê os Salmos), e lê as
    citações «Gn 3, 15», «Gn 2, 7; 3, 19», «Gn 8, 20 – 9, 17» nas notas e no texto («(Gn 6, 9)»).
  - São Josemaria Escrivá: o índice bíblico pesquisa/fontes/escriva-indice.md (gerado pelo mod-escriva.py, que junta o
    índice do escriva.org, as notas e as referências no texto; o cache das obras não está nesta máquina).
  - Lecionário da Missa (USA 1998/2002, = Ordo Lectionum Missae 1981), tabelas de Felix Just em
    https://catholic-resources.org/Lectionary/, em liturgia/: Index-Sundays.htm (domingos, solenidades, Vigília Pascal),
    Index-Weekdays.htm (dias de semana, anos I e II), 2002USL-Sanctoral.htm (santos), 2002USL-Masses-{Commons,Rituals,
    Various,Votives}.htm (comuns, missas rituais, por várias necessidades, votivas). Números do Lecionário entre parênteses.
"""
import importlib.util, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))          # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'genesis', 'modernos')
CIC = os.path.join(CACHE, 'catecismo')
LIT = os.path.join(CACHE, 'liturgia')
CIC_URL = 'https://www.vatican.va/archive/cathechism_po/index_new/'
LECT_URL = 'https://catholic-resources.org/Lectionary/'
LECT = ['Index-Sundays.htm', 'Index-Weekdays.htm', '2002USL-Sanctoral.htm', '2002USL-Masses-Commons.htm',
        '2002USL-Masses-Rituals.htm', '2002USL-Masses-Various.htm', '2002USL-Masses-Votives.htm']
ESCRIVA = os.path.join(RAIZ, 'fontes', 'escriva-indice.md')
UA = {'User-Agent': 'Mozilla/5.0 (pesquisa Biblia Taioe)'}
HOJE = '2026-10-25'
SCRIPT = 'pesquisa/ferramentas/base/gen-modernos-pistas.py'
INI, FIM = '<!-- automático -->', '<!-- fim do automático -->'


def _modulo(nome):
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_'), os.path.join(HERE, nome + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MC = _modulo('mod-catecismo')      # limpa(), arquivos(), baixar() (com CACHE trocado)
ML = _modulo('mod-liturgia')       # Tabelas (leitor das tabelas HTML)
MC.CACHE = CIC


def baixar():
    MC.baixar()
    os.makedirs(LIT, exist_ok=True)
    for nome in LECT:
        p = os.path.join(LIT, nome)
        if os.path.exists(p) and os.path.getsize(p) > 2000:
            continue
        req = urllib.request.Request(LECT_URL + nome, headers=UA)
        dados = urllib.request.urlopen(req, timeout=60).read()
        if len(dados) < 2000:
            raise RuntimeError(f'{nome}: resposta curta (página de erro?)')
        open(p, 'wb').write(dados)
        print('baixado', nome)
        time.sleep(1)


# ---------------------------------------------------------------- citações do Gênesis
def _caps_de(corpo):
    """«12, 4» / «8, 20 – 9, 17» / «2, 7; 3, 19» / «1 – 3» -> lista de (capítulos, texto normalizado «12,4»)."""
    out = []
    corpo = corpo.replace('\u2011', '-')
    for parte in corpo.split(';'):
        p = parte.strip(' .,')
        if not p:
            continue
        p = re.sub(r'^(\d{1,2})\.\s*(?=\d)', r'\1, ', p)      # «Gn 18. 14» = 18, 14
        m = re.match(r'^(\d{1,2})\s*,\s*([\dabc]+(?:\s*[-–]\s*[\dabc]+)?)\s*[-–]\s*(\d{1,2})\s*,\s*([\dabc]+)$', p)
        if m:                                   # 8, 20 – 9, 17
            a, b = int(m.group(1)), int(m.group(3))
            if 1 <= a <= b <= 50:
                out.append((list(range(a, b + 1)), f'{a},{m.group(2)}–{b},{m.group(4)}'))
            continue
        m = re.match(r'^(\d{1,2})\s*,\s*(.+)$', p)
        if m:                                   # 12, 4  /  1, 26-27.31
            c = int(m.group(1))
            vs = re.sub(r'\s+', '', m.group(2)).replace('–', '-')
            if 1 <= c <= 50:
                out.append(([c], f'{c},{vs}'))
            continue
        m = re.match(r'^(\d{1,2})(?:\s*[-–]\s*(\d{1,2}))?$', p)
        if m:                                   # 3  /  1 – 11 (capítulos inteiros)
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
            if 1 <= a <= b <= 50:
                out.append((list(range(a, b + 1)), f'{a}' if a == b else f'{a}–{b}'))
    return out


# último versículo de cada capítulo (para marcar erro de digitação da fonte, como «Gn 9, 5-61» no § 2260)
FIM_CAP = {1: 31, 2: 25, 3: 24, 4: 26, 5: 32, 6: 22, 7: 24, 8: 22, 9: 29, 10: 32, 11: 32, 12: 20, 13: 18, 14: 24, 15: 21,
           16: 16, 17: 27, 18: 33, 19: 38, 20: 18, 21: 34, 22: 24, 23: 20, 24: 67, 25: 34, 26: 35, 27: 46, 28: 22,
           29: 35, 30: 43, 31: 55, 32: 33, 33: 20, 34: 31, 35: 29, 36: 43, 37: 36, 38: 30, 39: 23, 40: 23, 41: 57,
           42: 38, 43: 34, 44: 34, 45: 28, 46: 34, 47: 31, 48: 22, 49: 33, 50: 26}


def sic(ref):
    """«Gn 9,5-61» -> «Gn 9,5-61 [sic: Gn 9 tem 29 versículos]» (só confere referências de um capítulo)."""
    m = re.match(r'^Gn (\d+),([\d.,\-abc]+)$', ref)
    if m and int(m.group(1)) in FIM_CAP:
        c = int(m.group(1))
        if any(int(v) > FIM_CAP[c] for v in re.findall(r'\d+', m.group(2))):
            return f'{ref} [sic: Gn {c} tem {FIM_CAP[c]} versículos]'
    return ref


RE_GN = re.compile(r'\b(?:Gn|Gén|Gen)\b\.?\s*((?:[\s\d,;.\-–\u2011]|(?<=\d)[abc](?![A-Za-zÀ-ÿ]))+)')


def refs_gn(txt):
    res = []
    for m in RE_GN.finditer(txt):
        corpo = m.group(1)
        if re.match(r'\s*[A-Za-zÀ-ÿ]', txt[m.end():]):      # «Gn 4, 3-8; 1 Rs 21»: o «1» é do livro seguinte
            corpo = re.sub(r'[;,]\s*[1-3]\s*$', '', corpo)
        res.extend(_caps_de(corpo))
    return res


# ---------------------------------------------------------------- Catecismo
def catecismo():
    """{cap: {par: {'vs': [..], 'via': set(), 'arquivo': f}}}"""
    out = {}
    for f in sorted(os.listdir(CIC)):
        if not f.endswith('_po.html') or f.startswith('prima'):
            continue
        t = MC.limpa(open(os.path.join(CIC, f), 'rb').read())
        linhas = [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n') if l.strip()]
        ini = None
        for i, l in enumerate(linhas[:-1]):
            if re.match(r'^1(?:\.\s?|\s)(?!\d)', l) and re.match(r'^2(?:\.\s?|\s)(?!\d)', linhas[i + 1]):
                ini = i
        if ini is None:
            print('  sem notas?', f)
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
            if par is None:
                continue
            for c in re.finditer(r'\((\d{1,3})\)', l):
                chamada.setdefault(int(c.group(1)), par)
            textos[par] = textos.get(par, '') + ' ' + l

        def anota(caps_txt, p, via):
            for caps, txt in caps_txt:
                for c in caps:
                    d = out.setdefault(c, {}).setdefault(p, {'vs': [], 'via': set(), 'arquivo': f})
                    if f'Gn {txt}' not in d['vs']:
                        d['vs'].append(f'Gn {txt}')
                    d['via'].add(via)
        for n, txt in notas.items():
            p = chamada.get(n)
            if p is not None:
                anota(refs_gn(txt), p, f'nota {n}')
        for p, l in textos.items():
            anota(refs_gn(re.sub(r'\(\d{1,3}\)', '', l)), p, 'texto')
    return out


def url_cic(f):
    return CIC_URL + f.replace('prologo_', 'prologo%20')


# ---------------------------------------------------------------- Escrivá
def escriva():
    """{cap: [(versos, rótulo, url, origem)]} do índice pesquisa/fontes/escriva-indice.md (seção Gênesis)."""
    out, cap, dentro = {}, None, False
    for l in open(ESCRIVA, encoding='utf-8'):
        if l.startswith('## '):
            dentro = l.strip() == '## Gênesis'
            continue
        if not dentro:
            continue
        m = re.match(r'^### Gênesis (\d+)', l)
        if m:
            cap = int(m.group(1))
            continue
        m = re.match(r'^- (.+?): \[(.+?)\]\((\S+?)\) \((.+?)\)', l)
        if m and cap:
            out.setdefault(cap, []).append(m.groups())
    return out


# ---------------------------------------------------------------- Lecionário
VERSO = r'[\dab:,;\s\-–—]'
RE_LECT = re.compile(r'Gen\s+(\d+:' + VERSO + r'*?(?:\s+or\s+\d+:' + VERSO + r'*?)*)(?=\s+\d+[A-E]?\)|\s+or\s+[A-Z]|\s*$|[^\dab:,;\s\-–—])')
DIA = {'Mon': 'segunda-feira', 'Tues': 'terça-feira', 'Wed': 'quarta-feira', 'Thurs': 'quinta-feira', 'Fri': 'sexta-feira',
       'Sat': 'sábado', 'Sun': 'domingo'}
ANO_FER = {'1': 'ano I', '2': 'ano II', '1+2': 'anos I e II'}
NOMES = {   # rótulos das tabelas -> português
    'Easter Vigil (1st Reading)': 'Vigília Pascal, 1ª leitura',
    'Easter Vigil (2nd Reading)': 'Vigília Pascal, 2ª leitura',
    'Dec 8: Immaculate Conception of the BVMary': '8 de dezembro, Imaculada Conceição de Nossa Senhora',
    'Dec 8: Solemnity: Immaculate Conception of the BVMary': '8 de dezembro, Imaculada Conceição de Nossa Senhora',
    'Pentecost Sunday: Vigil Mass (Option 1)': 'Vigília de Pentecostes (1ª leitura à escolha)',
    'Sunday after Trinity Sun: Body & Blood of Christ': 'Santíssimo Corpo e Sangue de Cristo',
    'Sunday in Octave of Christmas: Holy Family (Opt. B)': 'Sagrada Família (leituras à escolha no ano B)',
    'Mon after Pentecost: BVMary, Mother of the Church (option 1)': 'segunda-feira depois de Pentecostes, Santa Maria, Mãe da Igreja (1ª à escolha)',
    'Advent, Dec. 17': '17 de dezembro (Advento)',
    'Common of the Blessed Virgin Mary': 'Comum de Nossa Senhora',
    'Common of Holy Men and Women': 'Comum dos santos e santas',
    'Entrance into the Order of Catechumens': 'Missas rituais: entrada no catecumenato',
    'Christian Initiation apart from the Easter Vigil': 'Missas rituais: iniciação cristã fora da Vigília Pascal',
    'Institution of Acolytes': 'Missas rituais: instituição dos acólitos',
    'For the Conferral of the Sacrament of Marriage': 'Missas rituais: celebração do Matrimônio',
    'For the Consecration of Virgins and Religious Profession': 'Missas rituais: consagração das virgens e profissão religiosa',
    'Dedication of an Altar': 'Missas rituais: dedicação de um altar',
    'For Vocations to Holy Orders or Religious Life': 'Missas por várias necessidades: pelas vocações às ordens sacras e à vida religiosa',
    'For the Country or a City': 'Missas por várias necessidades: pela pátria ou pela cidade (e pelos governantes)',
    'In Time of War or Civil Disturbance': 'Missas por várias necessidades: em tempo de guerra ou de desordem',
    'For the Beginning of the Civil Year': 'Missas por várias necessidades: no começo do ano civil',
    'For the Blessing of Human Labor': 'Missas por várias necessidades: pela santificação do trabalho humano',
    'For Productive Land': 'Missas por várias necessidades: pelos frutos da terra',
    'For Giving Thanks to God for the Gift of Human Life': 'Missas por várias necessidades: ação de graças pelo dom da vida humana',
    'The Most Holy Eucharist': 'Missas votivas: Santíssima Eucaristia',
    'The Blessed Virgin Mary, Mother of the Church': 'Missas votivas: Santa Maria, Mãe da Igreja',
    'St. Joseph the Worker': '1º de maio, São José Operário',
    'Blessed Virgin Mary, Mother of the Church': 'segunda-feira depois de Pentecostes, Santa Maria, Mãe da Igreja',
    'The Immaculate Conception of the Blessed Virgin Mary': '8 de dezembro, Imaculada Conceição de Nossa Senhora',
}


def ordinal(n):
    return f'{int(n)}º'


def rotulo(lab):
    lab = re.sub(r'\s+', ' ', lab).strip()
    for en, pt in NOMES.items():
        if en in lab:
            return pt
    m = re.match(r'^(\d+)(?:st|nd|rd|th) Sunday of (Lent|Advent|Easter)$', lab)
    if m:
        return f'{ordinal(m.group(1))} domingo ' + {'Lent': 'da Quaresma', 'Advent': 'do Advento', 'Easter': 'da Páscoa'}[m.group(2)]
    m = re.match(r'^(\d+)(?:st|nd|rd|th) Sunday in Ordinary Time$', lab)
    if m:
        return f'{ordinal(m.group(1))} domingo do Tempo Comum'
    m = re.match(r'^Ord\. Time, Week (\d+), (\w+)$', lab)
    if m and m.group(2) in DIA:
        return f'{DIA[m.group(2)]} da {int(m.group(1))}ª semana do Tempo Comum'
    m = re.match(r'^(Lent|Easter|Advent), Week (\d+), (\w+)$', lab)
    if m and m.group(3) in DIA:
        return f'{DIA[m.group(3)]} da {int(m.group(2))}ª semana ' + {'Lent': 'da Quaresma', 'Advent': 'do Advento', 'Easter': 'da Páscoa'}[m.group(1)]
    return lab + ' [rótulo da tabela, em inglês]'


def br(ref):
    """«22:1-2, 9a, 10-13» -> «22,1-2.9a.10-13»; «1:20—2:4a» -> «1,20–2,4a»; «or» -> «ou»."""
    r = re.sub(r'\s+', ' ', ref).strip(' ,;')
    r = r.replace(', ', '.').replace(':', ',').replace('—', '–').replace(' or ', ' ou ')
    return 'Gn ' + r


def caps_lect(ref):
    cs = set()
    for alt in re.split(r'\s+or\s+', ref):
        for parte in alt.split(';'):
            for a, b in re.findall(r'(\d+):[\dab,\s\-]*?(?:[—–]\s*(\d+):)?', parte):
                a = int(a)
                cs.update(range(a, (int(b) if b else a) + 1))
    return sorted(c for c in cs if 1 <= c <= 50)


def lecionario():
    """{cap: [(rótulo pt, número do Lecionário, ano, referência br)]}"""
    out, vistos = {}, set()

    def poe(caps, lab, num, ano, ref):
        for c in caps:
            k = (c, num, ref)
            if k in vistos:
                continue
            vistos.add(k)
            out.setdefault(c, []).append((lab, num, ano, ref))
    for nome in LECT:
        p = os.path.join(LIT, nome)
        if not os.path.exists(p):
            print('  falta', nome, '(rodar «baixar»)')
            continue
        tb = ML.Tabelas()
        tb.feed(open(p, encoding='utf-8', errors='replace').read())
        for r in tb.rows:
            r = [re.sub(r'\s+', ' ', c).strip() for c in r]
            if nome == 'Index-Sundays.htm':
                if len(r) >= 3 and r[0].startswith('Gen '):
                    num, _, anos = r[1].partition('-')
                    ano = '' if not anos else ('anos A, B e C' if anos == 'ABC' else f'ano {anos}')
                    ref = r[0][4:]
                    poe(caps_lect(ref), rotulo(r[2]), num, ano, br(ref))
            elif nome == 'Index-Weekdays.htm':
                if len(r) >= 4 and r[0].startswith('Gen '):
                    ref = r[0][4:]
                    poe(caps_lect(ref), rotulo(r[1]), r[3], ANO_FER.get(r[2], r[2]), br(ref))
            elif nome == '2002USL-Sanctoral.htm':
                if len(r) >= 6:
                    for k, cel in enumerate(r[4:], start=4):
                        for m in RE_LECT.finditer(cel):
                            poe(caps_lect(m.group(1)), rotulo(r[2]), r[0], '', br(m.group(1)))
            else:
                if len(r) < 2:
                    continue
                for cel in r[1:]:
                    for m in RE_LECT.finditer(cel):
                        antes = cel[:m.start()]
                        nums = re.findall(r'(\d{3}[A-E]?):', antes)
                        num = nums[-1] if nums else (re.match(r'\D*(\d{3}[A-E]?)', r[0]) or [None, ''])[1]
                        poe(caps_lect(m.group(1)), rotulo(r[0]), num, '', br(m.group(1)))
    return out


# ---------------------------------------------------------------- saída
def montar(cap, cic, esc, lect):
    L = [INI, '',
         f'Pistas geradas por script em {HOJE} (`{SCRIPT}`): só endereços e números, sem o texto (o Catecismo e as obras de',
         'Escrivá têm direito autoral). Conferir cada uma antes de usar; a pesquisa do capítulo escreve à mão fora dos marcadores.', '',
         '## Catecismo', '']
    pars = cic.get(cap, {})
    if not pars:
        L.append('- nada achado (nenhuma nota nem citação no texto com «Gn ' + str(cap) + '»).')
    for p in sorted(pars):
        d = pars[p]
        via = ', '.join(sorted(d['via'], key=lambda v: (v != 'texto', int(re.sub(r'\D', '', v) or 0))))
        L.append(f"- § {p}: {'; '.join(sic(v) for v in d['vs'])} ({via}). {url_cic(d['arquivo'])}")
    if pars:
        L.append('')
        L.append('(Texto oficial em português europeu; as notas «Cf.» só remetem. Ler o parágrafo inteiro antes de usar.)')
    L += ['', '## São Josemaria Escrivá', '']
    itens = esc.get(cap, [])
    if not itens:
        L.append('- nada achado no índice `pesquisa/fontes/escriva-indice.md` (índice do escriva.org, notas e referências '
                 'no texto; citação sem referência não entra).')
    for vs, rot, url, ori in itens:
        ref = f'Gn {cap}' if vs.startswith('(') else f'Gn {cap},{vs.replace(", ", ".").replace("–", "-")}'
        L.append(f'- {ref}: {rot}. {url} (referência: {ori})')
    L += ['', '## Liturgia da Missa', '']
    ls = lect.get(cap, [])
    if not ls:
        L.append('- nada achado (o Lecionário não lê este capítulo nos domingos, dias de semana, santos, comuns, missas '
                 'rituais, votivas e por várias necessidades).')
    def chave(x):
        lab, num, ano, ref = x
        n = int(re.sub(r'\D', '', num) or 9999)
        return (n, lab)
    for lab, num, ano, ref in sorted(ls, key=chave):
        extra = ', '.join(x for x in (ano, f'Lecionário {num}' if num else '') if x)
        L.append(f'- {lab}' + (f' ({extra})' if extra else '') + f': {ref}')
    if ls:
        L.append('')
        L.append('(Tabelas de Felix Just, catholic-resources.org/Lectionary/: Index-Sundays.htm, Index-Weekdays.htm e as de '
                 'santos e missas rituais; numeração do Ordo Lectionum Missae, 1981. Conferir o lecionário brasileiro.)')
    L += ['', FIM]
    return '\n'.join(L)


def gravar(cap, auto):
    pasta = os.path.join(RAIZ, 'genesis', f'{cap:03d}', 'base')
    os.makedirs(pasta, exist_ok=True)
    p = os.path.join(pasta, '_pistas-modernos.md')
    titulo = f'# Pistas modernas: Gênesis {cap}'
    if os.path.exists(p):
        velho = open(p, encoding='utf-8').read()
        if INI in velho and FIM in velho:
            txt = re.sub(re.escape(INI) + r'.*?' + re.escape(FIM), lambda m: auto, velho, flags=re.S)
        else:
            txt = velho.rstrip('\n') + '\n\n' + auto + '\n'
    else:
        txt = titulo + '\n\n' + auto + '\n'
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    return p


def capitulos(arg):
    out = []
    for parte in arg.split(','):
        if '-' in parte:
            a, b = parte.split('-', 1)
            out.extend(range(int(a), int(b) + 1))
        elif parte:
            out.append(int(parte))
    return sorted(set(c for c in out if 1 <= c <= 50))


def main():
    a = sys.argv[1:]
    if a[:1] == ['baixar']:
        baixar()
        return
    ver = a[:1] == ['--ver']
    if ver:
        a = a[1:]
    if not a or not re.match(r'^[\d,\-]+$', a[0]):
        print(__doc__)
        sys.exit(1)
    cic, esc, lect = catecismo(), escriva(), lecionario()
    tot = {'cic': 0, 'esc': 0, 'lect': 0}
    for cap in capitulos(a[0]):
        auto = montar(cap, cic, esc, lect)
        n = (len(cic.get(cap, {})), len(esc.get(cap, [])), len(lect.get(cap, [])))
        tot['cic'] += n[0]
        tot['esc'] += n[1]
        tot['lect'] += n[2]
        if ver:
            print(auto)
        else:
            gravar(cap, auto)
            print(f'  gravado genesis/{cap:03d}/base/_pistas-modernos.md (Catecismo {n[0]}, Escrivá {n[1]}, liturgia {n[2]})')
    print('total:', tot)


if __name__ == '__main__':
    main()
