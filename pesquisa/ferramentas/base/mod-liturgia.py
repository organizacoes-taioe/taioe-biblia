"""Liturgia: onde cada salmo é rezado (Liturgia das Horas, Lecionário, Missal e Breviário antigos).

    python -I -X utf8 pesquisa/ferramentas/base/mod-liturgia.py baixar     # catholic-resources (4 páginas) + Divinum Officium (.tar.gz, 140 MB)
    python -I -X utf8 pesquisa/ferramentas/base/mod-liturgia.py construir  # monta cache/base/modernos/liturgia.json (por salmo HEBRAICO)

Fontes:
  - Liturgia das Horas, saltério de 4 semanas (1971): Felix Just, https://catholic-resources.org/LoH/Psalter-Index.html
    (tabela salmo → semana, dia, hora; numeração hebraica). Siglas: OR Ofício das Leituras, MP Laudes, DP Hora Média,
    EP Vésperas (EP1 = I Vésperas, EP2 = II Vésperas), Night Prayer Completas. As antífonas latinas da Liturgia Horarum NÃO
    estão em fonte aberta que se consiga raspar (Universalis bloqueia o curl; brewiarz.katolik.pl/latin só tem dias
    soltos): ficam «a confirmar».
  - Lecionário (Ordo Lectionum Missae, 1981), salmo responsorial: tabelas de Felix Just em
    https://catholic-resources.org/Lectionary/ (1970USL-Sundays, 1998USL-Solemnities, 1970USL-WeekdaysA, 1970USL-WeekdaysB;
    numeração e versículos hebraicos; sem o refrão).
  - Missal e Breviário antigos (latim, domínio público): https://github.com/DivinumOfficium/divinum-officium
    (web/www/missa/Latin/{Tempora,Sancti,Commune}/*.txt: linhas `!Ps N:v` nas seções Introitus, Graduale, Tractus, Offertorium,
    Communio; web/www/horas/Latin/Psalterium/Psalmi/*.txt: distribuição dos salmos, com antífonas). Numeração da Vulgata.
    Matinas do Breviário de Pio V: tiradas da própria *Traduzione* de Afonso (mod-afonso-salmi.py), porque as seções «DayN» do
    Divinum Officium trazem outra distribuição.
Saída: pesquisa/cache/base/modernos/liturgia.json = {hebraico: {lh: [...], lect: [...], missa: [...], oficio: [...]}}.
"""
import html, json, os, re, sys, tarfile, time, urllib.request
from html.parser import HTMLParser

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
MOD = os.path.join(RAIZ, 'cache', 'base', 'modernos')
LIT = os.path.join(MOD, 'liturgia')
DOD = os.path.join(MOD, 'divinum-officium')
UA = {'User-Agent': 'Mozilla/5.0 (pesquisa Biblia Taioe)'}
PAGINAS = {
    'psalter-index.html': 'https://catholic-resources.org/LoH/Psalter-Index.html',
    'sundays.html': 'https://catholic-resources.org/Lectionary/1970USL-Sundays.htm',
    'solemnities.html': 'https://catholic-resources.org/Lectionary/1998USL-Solemnities.htm',
    'weekdaysA.html': 'https://catholic-resources.org/Lectionary/1970USL-WeekdaysA.htm',
    'weekdaysB.html': 'https://catholic-resources.org/Lectionary/1970USL-WeekdaysB.htm',
}
DO_TGZ = 'https://codeload.github.com/DivinumOfficium/divinum-officium/tar.gz/refs/heads/master'


def baixar():
    os.makedirs(LIT, exist_ok=True)
    for nome, url in PAGINAS.items():
        p = os.path.join(LIT, nome)
        if os.path.exists(p):
            continue
        req = urllib.request.Request(url, headers=UA)
        open(p, 'wb').write(urllib.request.urlopen(req, timeout=60).read())
        print('baixado', nome)
        time.sleep(1)
    if not os.path.isdir(os.path.join(DOD, 'divinum-officium-master')):
        os.makedirs(DOD, exist_ok=True)
        tgz = os.path.join(DOD, 'do.tgz')
        req = urllib.request.Request(DO_TGZ, headers=UA)
        open(tgz, 'wb').write(urllib.request.urlopen(req, timeout=600).read())
        with tarfile.open(tgz) as t:
            membros = [m for m in t.getmembers()
                       if '/web/www/missa/Latin/' in m.name or '/web/www/horas/Latin/' in m.name]
            t.extractall(DOD, members=membros)
        print('Divinum Officium extraído')


def vul_para_heb(v):
    if v <= 8 or v >= 148:
        return v
    if v == 9:
        return 9   # a Vulgata 9 cobre os hebr. 9 e 10
    if v == 113:
        return 114  # e 115
    if v in (114, 115):
        return 116
    return v + 1


def hebs_da_vulg(v):
    if v == 9:
        return [9, 10]
    if v == 113:
        return [114, 115]
    if v in (146, 147):
        return [147]
    return [vul_para_heb(v)]


# ---------------------------------------------------------------- tabelas HTML
class Tabelas(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows, self.cur, self.cell = [], None, None

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.cur = []
        elif tag in ('td', 'th') and self.cur is not None:
            self.cell = []
        elif tag == 'br' and self.cell is not None:
            self.cell.append(' ')

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None and self.cur is not None:
            self.cur.append(re.sub(r'\s+', ' ', ''.join(self.cell)).strip())
            self.cell = None
        elif tag == 'tr' and self.cur is not None:
            self.rows.append(self.cur)
            self.cur = None

    def handle_data(self, d):
        if self.cell is not None:
            self.cell.append(d)


def linhas_tabela(nome):
    p = Tabelas()
    p.feed(open(os.path.join(LIT, nome), encoding='utf-8', errors='replace').read())
    return p.rows


# ---------------------------------------------------------------- Liturgia das Horas
DIAS = {'Sunday': 'domingo', 'Sun': 'domingo', 'Monday': 'segunda-feira', 'Tuesday': 'terça-feira',
        'Wednesday': 'quarta-feira', 'Thursday': 'quinta-feira', 'Friday': 'sexta-feira', 'Saturday': 'sábado'}
ROM = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV'}


def traduz_lugar(s):
    s = s.replace('(', ' (').replace(')', ') ')
    s = re.sub(r'\s+', ' ', s).strip()
    def semanas(m):
        nums = [ROM[x] for x in re.findall(r'\d', m.group(1))]
        if len(nums) == 1:
            return 'Semana ' + nums[0] + ', '
        if nums == ['I', 'II', 'III', 'IV']:
            return 'Semanas I a IV, '
        return 'Semanas ' + ', '.join(nums[:-1]) + ' e ' + nums[-1] + ', '
    s = re.sub(r'Weeks? ([\d,&\s]+):\s*', semanas, s)
    for en, pt in DIAS.items():
        s = re.sub(r'\b' + en + r'\b', pt, s)
    troca = [
        ('ORDINARY: INVITATORY Psalm', 'Invitatório (salmo ordinário)'),
        ('also alt. Invitatory Psalm', 'também como invitatório alternativo'),
        ('also alt. Invitatory', 'também como invitatório alternativo'),
        ('EP-II', 'II Vésperas'), ('EP-I', 'I Vésperas'), ('EP1', 'I Vésperas'), ('EP2', 'II Vésperas'),
        ('Night Prayer', 'Completas'), ('after', 'depois das'), (' on ', ' de '),
        ('only in Ordinary Time', 'só no Tempo Comum'),
        ('only in Advent, Christmas, Lent, Easter', 'só no Advento, Natal, Quaresma e Páscoa'),
        ('OMITTED', 'omitido da Liturgia das Horas'),
    ]
    for en, pt in troca:
        s = s.replace(en, pt)
    s = re.sub(r'\bOR\b', 'Ofício das Leituras', s)
    s = re.sub(r'\bMP\b', 'Laudes', s)
    s = re.sub(r'\bDP\b', 'Hora Média', s)
    s = re.sub(r'\bEP\b', 'Vésperas', s)
    s = s.replace(' & ', '; ')
    s = re.sub(r'(feira|domingo|sábado) (Laudes|Hora Média|Vésperas|Ofício|I Vésperas|II Vésperas)', r'\1, \2', s)
    s = s.replace('Completas: ', 'Completas, ')
    return re.sub(r'\s+', ' ', s).strip()


def ler_lh():
    out = {}
    for r in linhas_tabela('psalter-index.html'):
        if len(r) < 2 or not re.match(r'^Ps \d', r[0]):
            continue
        m = re.match(r'^Ps (\d+)\s*(.*)$', r[0])
        n = int(m.group(1))
        sub = m.group(2).strip()
        out.setdefault(n, []).append({'trecho': sub, 'lugar_en': r[1], 'lugar': traduz_lugar(r[1]),
                                      'titulo_en': r[2] if len(r) > 2 else ''})
    return out


# ---------------------------------------------------------------- Lecionário
ORD = {'First': 1, 'Second': 2, 'Third': 3, 'Fourth': 4, 'Fifth': 5, 'Sixth': 6, 'Seventh': 7, 'Eighth': 8}
TEMPO = {'Advent': 'do Advento', 'Lent': 'da Quaresma', 'Easter': 'da Páscoa', 'Christmas': 'do Natal'}
DIA3 = {'Mon': 'segunda-feira', 'Tues': 'terça-feira', 'Wed': 'quarta-feira', 'Thurs': 'quinta-feira', 'Fri': 'sexta-feira',
        'Sat': 'sábado', 'Sun': 'domingo'}


MESES = {'January': 'janeiro', 'February': 'fevereiro', 'March': 'março', 'April': 'abril', 'August': 'agosto',
         'September': 'setembro', 'October': 'outubro', 'November': 'novembro', 'December': 'dezembro',
         'Jan': 'janeiro', 'Feb': 'fevereiro', 'Mar': 'março', 'Apr': 'abril', 'May': 'maio', 'Jun': 'junho', 'June': 'junho',
         'Jul': 'julho', 'July': 'julho', 'Aug': 'agosto', 'Sep': 'setembro', 'Sept': 'setembro', 'Oct': 'outubro', 'Nov': 'novembro',
         'Dec': 'dezembro'}
NOMES = [  # (trecho em inglês, português) — aplicados em ordem
    ('Sunday after Trinity Sunday: Solemnity of the Most Holy Body and Blood of Christ (formerly called “Corpus Christi”)', 'Corpus Christi'),
    ('Thursday after Trinity Sunday: Corpus Christi', 'Corpus Christi'), ('Body & Blood / Corpus Christi', 'Corpus Christi'),
    ('Friday after the Second Sunday after Pentecost: Solemnity of the Most Sacred Heart of Jesus', 'Sagrado Coração de Jesus'),
    ('Friday of the Second Sunday after Pentecost: Sacred Heart', 'Sagrado Coração de Jesus'), ('Sacred Heart', 'Sagrado Coração de Jesus'),
    ('Passion Sunday (Palm Sunday)', 'Domingo de Ramos'), ('Trinity Sunday', 'Santíssima Trindade'),
    ('[34th Sunday] Christ the King', 'Cristo Rei (34º domingo do Tempo Comum)'),
    ('[1st Sunday] Baptism of the Lord', 'Batismo do Senhor'), ('Baptism of Lord', 'Batismo do Senhor'),
    ('Good Friday: The Passion of the Lord', 'Sexta-feira Santa'),
    ('Easter: The Resurrection of the Lord - Easter Vigil', 'Vigília Pascal'), ('Easter Sunday', 'Domingo da Páscoa'),
    ('Ascension', 'Ascensão do Senhor'), ('[Ash Wednesday', 'Quarta-feira de Cinzas'), ('Ash Wednesday', 'Quarta-feira de Cinzas'),
    ('Jan 1: Octave of Christmas - ABC; Solemnity of Mary, Mother of God', '1º de janeiro, Santa Maria, Mãe de Deus'),
    ('Jan. 1 - Mary, Mother of God', '1º de janeiro, Santa Maria, Mãe de Deus'),
    ('Jan 6: Epiphany', 'Epifania do Senhor'), ('Epiphany of the Lord (traditionally on Jan. 6; but now in USA: Sunday after Jan. 1)', 'Epifania do Senhor'),
    ('Christmas Vigil', 'Natal, Vigília'), ('Christmas Mass at Midnight', 'Natal, Missa da Noite'),
    ('Christmas Mass at Dawn', 'Natal, Missa da Aurora'), ('Christmas Mass during Day', 'Natal, Missa do Dia'),
    ('Holy Thursday: Chrism Mass', 'Quinta-feira Santa, Missa do Crisma'),
    ("Holy Thursday: Mass of the Lord's Supper", 'Quinta-feira Santa, Missa da Ceia do Senhor'),
    ('Pentecost: Vigil', 'Vigília de Pentecostes'), ('Pentecost Sunday', 'Domingo de Pentecostes'),
    ('Sunday in the Octave of Christmas: Holy Family', 'Sagrada Família'), ('Second Sunday after Christmas', '2º domingo depois do Natal'),
    ('Dec. 26 - St. Stephen', '26 de dezembro, Santo Estêvão'), ('Dec. 27 - St. John', '27 de dezembro, São João Evangelista'),
    ('Dec. 28 - Holy Innocents', '28 de dezembro, Santos Inocentes'), ('Dec. 24 - morning Mass', '24 de dezembro, Missa da manhã'),
    ('Thursday after Ash Wed.', 'quinta-feira depois das Cinzas'), ('Friday after Ash Wed.', 'sexta-feira depois das Cinzas'),
    ('Saturday after Ash Wed.', 'sábado depois das Cinzas'),
    ('The Presentation of the Lord', 'Apresentação do Senhor'), ('St. Joseph, Spouse of the Blessed Virgin Mary', 'São José, esposo da Virgem Maria'),
    ('The Annunciation of the Lord', 'Anunciação do Senhor'), ('The Nativity of St. John the Baptist', 'Natividade de São João Batista'),
    ('SS. Peter and Paul, Apostles', 'São Pedro e São Paulo, apóstolos'), ('The Transfiguration of the Lord', 'Transfiguração do Senhor'),
    ('The Assumption of the Blessed Virgin Mary', 'Assunção de Nossa Senhora'), ('The Exaltation of the Cross', 'Exaltação da Santa Cruz'),
    ('All Saints', 'Todos os Santos'), ('The Commemoration of All the Faithful Departed (All Souls)', 'Finados'),
    ('The Dedication of the Lateran Basilica', 'Dedicação da Basílica de Latrão'),
    ('The Immaculate Conception of the Blessed Virgin Mary', 'Imaculada Conceição'),
    ('Holy Week', 'Semana Santa'), ('Easter Octave', 'Oitava da Páscoa'), ('opt. Mass', 'missa facultativa'),
    ('Monday after Epiphany, or', 'segunda-feira depois da Epifania, ou'), ('Tuesday after Epiphany, or', 'terça-feira depois da Epifania, ou'),
    ('Wednesday after Epiphany, or', 'quarta-feira depois da Epifania, ou'), ('Thursday after Epiphany, or', 'quinta-feira depois da Epifania, ou'),
    ('Friday after Epiphany, or', 'sexta-feira depois da Epifania, ou'), ('Saturday after Epiphany, or', 'sábado depois da Epifania, ou'),
    ('Vigil', 'vigília'), (': Day', ': dia'),
]
RESIDUO = re.compile(r'\b(the|of|and|Week|Sunday|Mass|St\.|Feast|Solemnity|after|Lent|Easter|Mon|Tues|Wed|Thurs|Fri|Sat)\b')


def traduz_nomeado(lab):
    lab = lab.lstrip('*').strip()
    for corte in (' (transferred', ' (exceptions', ' [new', ' - [new', ' (further'):
        if corte in lab:
            lab = lab[:lab.index(corte)]
    r = lab
    for en, pt in NOMES:
        if en in r:
            r = r.replace(en, pt)
    # datas «Dec. 20», «Jan. 7»
    r = re.sub(r'\b(January|February|March|April|August|September|October|November|December|Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)\.?\s+\[?(\d+)\]?', lambda m: '%s de %s' % (m.group(2), MESES[m.group(1)]), r)
    r = re.sub(r'\s*\(add\)', '', r)
    r = re.sub(r'\s*-\s*ABC\b', '', r)
    r = re.sub(r'\s*-\s*([ABC])\b', r', ano \1', r)
    r = re.sub(r'(Cristo Rei \(34º domingo do Tempo Comum\))\s+([ABC])\b', r'\1, ano \2', r)
    r = re.sub(r'(Batismo do Senhor)\s+([ABC])\b', r'\1, ano \2', r)
    r = re.sub(r'(\w+) Week of (Lent|Easter|Advent)', lambda m: '%dª semana %s' % (ORD[m.group(1)], TEMPO[m.group(2)]) if m.group(1) in ORD else m.group(0), r)
    r = re.sub(r'\b(Mon|Tues|Wed|Thurs|Fri|Sat)\b(?!\.)', lambda m: DIA3[m.group(1)], r)
    r = r.replace('Semana Santa - ', 'Semana Santa, ').replace('Oitava da Páscoa - ', 'Oitava da Páscoa, ')
    return r


def rotulo_pt(lab):
    """Traduz o rótulo da tabela de Felix Just quando segue um padrão conhecido; senão devolve o original em inglês."""
    ano = ''
    m = re.search(r' \(ano (I+)\)$', lab)
    if m:
        ano = ' (ano ' + m.group(1) + ')'
        lab = lab[:m.start()]
    lab = re.sub(r'^\d+ — ', '', lab)
    m = re.match(r'^(\d+)(?:st|nd|rd|th) Sunday of (Advent|Lent|Easter)(?: - ([ABC]+))?', lab)
    if m:
        return '%dº domingo %s%s' % (int(m.group(1)), TEMPO[m.group(2)], (', ano ' + m.group(3)) if m.group(3) else '') + ano
    m = re.match(r'^(\d+)(?:st|nd|rd|th) Sunday of Year ([ABC])', lab)
    if m:
        return '%dº domingo do Tempo Comum, ano %s' % (int(m.group(1)), m.group(2)) + ano
    m = re.match(r'^Week (\d+) - (\w+)$', lab)
    if m and m.group(2) in DIA3:
        return '%s da %dª semana do Tempo Comum' % (DIA3[m.group(2)], int(m.group(1))) + ano
    m = re.match(r'^(\w+) Week of (Advent|Lent|Easter) - (\w+)$', lab)
    if m and m.group(1) in ORD and m.group(3) in DIA3:
        return '%s da %dª semana %s' % (DIA3[m.group(3)], ORD[m.group(1)], TEMPO[m.group(2)]) + ano
    pt = traduz_nomeado(lab)
    return pt + ano + ('' if pt != lab and not RESIDUO.search(pt) else ' [rótulo da tabela, em inglês]')

def ler_lecionario():
    out = {}
    arqs = [('sundays.html', 'Domingos e festas do Senhor'), ('solemnities.html', 'Solenidades e festas'),
            ('weekdaysA.html', 'Dias de semana (tempos fortes)'), ('weekdaysB.html', 'Dias de semana (Tempo Comum)')]
    for nome, grupo in arqs:
        cab = None
        for r in linhas_tabela(nome):
            if any('Responsorial' in c for c in r) and len(r) >= 4:
                cab = r
                continue
            if cab is None or len(r) != len(cab):
                continue
            idx = [i for i, c in enumerate(cab) if 'Responsorial' in c]
            lab_idx = [i for i, c in enumerate(cab) if not any(k in c for k in ('Reading', 'Psalm', 'Gospel', 'Alleluia',
                                                                                  'Years It Falls', 'S/f')) and c.strip() != 'Date']
            # a coluna «Date» das solenidades (5/31/26) não ajuda; o resto forma o rótulo
            lab = ' — '.join(r[i] for i in lab_idx if r[i] and r[i] != '#')
            num = r[0] if re.match(r'^\d+$', r[0]) else ''
            for k, i in enumerate(idx):
                cel = r[i]
                if not cel:
                    continue
                ano = ''
                if len(idx) > 1:
                    ano = ' (ano ' + ('I' if k == 0 else 'II') + ')'
                for m in re.finditer(r'Ps (\d+)\s*:?\s*([^P]*?)(?=\s+or\s+Ps|\s*$|\s*\(diff\))', cel):
                    n = int(m.group(1))
                    out.setdefault(n, []).append({'grupo': grupo, 'celebracao': rotulo_pt(lab + ano), 'celebracao_en': lab + ano, 'olm': num,
                                                  'versos': m.group(2).strip(' ;,'), 'celula': cel})
                # salmos não numerados como «Ps» (cânticos) são ignorados
    return out


# ---------------------------------------------------------------- Missal antigo (Divinum Officium)
def do_raiz():
    return os.path.join(DOD, 'divinum-officium-master', 'web', 'www')


SEC_MISSA = {'Introitus': 'Intróito', 'Graduale': 'Gradual', 'GradualeP': 'Gradual (tempo pascal)', 'Tractus': 'Tracto',
             'Offertorium': 'Ofertório', 'Communio': 'Comunhão', 'GradualeL1': 'Gradual', 'GradualeF': 'Gradual',
             'Sequentia': 'Sequência', 'Prelude': 'Prelúdio', 'Super populum': 'Sobre o povo'}


def ler_missa():
    out = {}
    base = os.path.join(do_raiz(), 'missa', 'Latin')
    for sub in ('Tempora', 'Sancti', 'Commune'):
        pasta = os.path.join(base, sub)
        for f in sorted(os.listdir(pasta)):
            if not f.endswith('.txt'):
                continue
            txt = open(os.path.join(pasta, f), encoding='utf-8').read()
            partes = re.split(r'^\[([^\]]+)\][^\n]*\n', txt, flags=re.M)
            # partes = ['', nome1, corpo1, nome2, corpo2 …]
            titulo = ''
            secs = []
            for i in range(1, len(partes) - 1, 2):
                nome, corpo = partes[i], partes[i + 1]
                if nome == 'Officium' and not titulo:
                    titulo = corpo.strip().split('\n')[0].strip()
                secs.append((nome, corpo))
            for nome, corpo in secs:
                if nome not in SEC_MISSA:
                    continue
                ult = None
                linhas = corpo.split('\n')
                for j, l in enumerate(linhas):
                    m = re.match(r'^!Ps(?:almus)? (.*)$', l)
                    if not m:
                        continue
                    refs = []
                    for r in re.split(r';', m.group(1)):
                        r = r.strip().rstrip('.')
                        mm = re.match(r'(\d+):([\d\-a-z,\.]+)', r)
                        if mm:
                            ult = int(mm.group(1))
                            refs.append((ult, mm.group(2)))
                        else:
                            mi = re.match(r'ibid\.?,?\s*([\d\-a-z,\.]+)', r)
                            if mi and ult:
                                refs.append((ult, mi.group(1)))
                    # texto latino: primeira linha seguinte que não comece por ! ou &
                    texto = ''
                    for l2 in linhas[j + 1:j + 6]:
                        if l2 and not l2.startswith('!') and not l2.startswith('&') and not l2.startswith('@'):
                            texto = re.sub(r'^v\.\s*', '', l2).strip()
                            break
                    for n, v in refs:
                        out.setdefault(n, []).append({'arquivo': '%s/%s' % (sub, f[:-4]), 'titulo': titulo or f[:-4],
                                                      'parte': SEC_MISSA[nome], 'versos': v, 'texto': texto})
    return out


# ---------------------------------------------------------------- Breviário antigo
DIAS_PT = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']
FERIA = {'Dominica': 'domingo', 'Feria II': 'segunda-feira', 'Feria III': 'terça-feira', 'Feria IV': 'quarta-feira',
         'Feria V': 'quinta-feira', 'Feria VI': 'sexta-feira', 'Sabbato': 'sábado', 'Feria': 'féria (dias de semana)',
         'Festis': 'festas'}


def salmos_de(cel):
    """'92;99;62;66' ou '118(1-16),118(17-32)' ou '9(2-11)' → [(num, trecho)] com num<200"""
    res = []
    for tok in re.split(r'[;,]\s*(?![^()]*\))', cel):
        tok = tok.strip().strip('[]')
        m = re.match(r"^(\d+)\s*(\(.*\))?", tok)
        if m and int(m.group(1)) < 200:
            res.append((int(m.group(1)), (m.group(2) or '').strip('()').replace("'", '')))
    return res


def ler_oficio():
    out = {}
    pm = os.path.join(do_raiz(), 'horas', 'Latin', 'Psalterium', 'Psalmi')

    def secoes(arq):
        txt = open(os.path.join(pm, arq), encoding='utf-8').read()
        partes = re.split(r'^\[([^\]]+)\][^\n]*\n', txt, flags=re.M)
        return [(partes[i], partes[i + 1]) for i in range(1, len(partes) - 1, 2)]

    def add(n, dados):
        out.setdefault(n, []).append(dados)

    # Laudes e Vésperas, Pio V (Day0..6) e Pio X (Daya0..6)
    for nome, corpo in secoes('Psalmi major.txt'):
        m = re.match(r'^Day(a?)(\d) (Laudes1|Laudes2|Laudes|Vespera)$', nome)
        if not m:
            continue
        pio = 'Pio X (1911)' if m.group(1) else 'Pio V (Tridentino)'
        dia = DIAS_PT[int(m.group(2))]
        hora = 'Vésperas' if m.group(3) == 'Vespera' else 'Laudes'
        if m.group(3) == 'Laudes2':
            hora += ' (série alternativa, em tempos penitenciais)'
        for l in corpo.strip().split('\n'):
            if ';;' not in l:
                continue
            ant, ps = l.split(';;', 1)
            ant = ant.strip()
            for n, trecho in salmos_de(ps):
                add(n, {'saltério': pio, 'dia': dia, 'hora': hora, 'trecho': trecho, 'antifona': ant})
    # Matinas de Pio X (Daya) — Pio V sai de Afonso
    for nome, corpo in secoes('Psalmi matutinum.txt'):
        m = re.match(r'^Daya(\d)$', nome)
        if not m:
            continue
        dia = DIAS_PT[int(m.group(1))]
        for l in corpo.strip().split('\n'):
            if ';;' not in l:
                continue
            ant, ps = l.split(';;', 1)
            for n, trecho in salmos_de(ps):
                add(n, {'saltério': 'Pio X (1911)', 'dia': dia, 'hora': 'Matinas', 'trecho': trecho, 'antifona': ant.strip()})
    # horas menores: Pio X ([Prima] …) e Pio V ([Tridentinum])
    horas_pt = {'Prima': 'Prima', 'Tertia': 'Terça', 'Sexta': 'Sexta', 'Nona': 'Noa', 'Completorium': 'Completas'}
    for nome, corpo in secoes('Psalmi minor.txt'):
        if nome in horas_pt:
            ant_atual, dia_atual = '', ''
            for l in corpo.strip().split('\n'):
                m = re.match(r'^([A-Za-z ]+?)\s*=\s*(.*)$', l)
                if m and m.group(1).strip() in FERIA:
                    dia_atual, ant_atual = FERIA[m.group(1).strip()], m.group(2).strip()
                    continue
                if dia_atual and re.match(r'^[\d\[\(]', l.strip()):
                    for n, trecho in salmos_de(l.strip()):
                        add(n, {'saltério': 'Pio X (1911)', 'dia': dia_atual, 'hora': horas_pt[nome], 'trecho': trecho, 'antifona': ant_atual})
                    dia_atual = ''
        elif nome == 'Tridentinum':
            for l in corpo.strip().split('\n'):
                m = re.match(r'^(Prima|Tertia|Sexta|Nona|Completorium)\s*([^=]*)=([^;]*);;(.*)$', l)
                if not m:
                    continue
                hora = horas_pt[m.group(1)]
                resto = m.group(2).strip()
                if resto.endswith('SQP'):
                    continue
                dia = FERIA.get(resto.replace('Dominica ', 'Dominica').strip(), '') or FERIA.get(resto, resto) or 'todos os dias'
                if not resto:
                    dia = 'todos os dias'
                for n, trecho in salmos_de(m.group(4)):
                    add(n, {'saltério': 'Pio V (Tridentino)', 'dia': dia, 'hora': hora, 'trecho': trecho, 'antifona': m.group(3).strip()})
    return out


def ler_matinas_pio5():
    """Matinas do Breviário de Pio V a partir da Traduzione de Afonso (seções «MATTUTINO» e «NOTTURNO»)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location('afonso', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mod-afonso-salmi.py'))
    af = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(af)
    res, _ = af.mapa_salmos()
    out = {}
    for n, secs in res.items():
        for s in secs:
            sc = s['secao']
            if 'MATTUTINO' in sc or 'NOTTURNO' in sc:
                if sc in ('PRIMO NOTTURNO', 'SECONDO NOTTURNO', 'TERZO NOTTURNO'):
                    dia = 'domingo'
                    hora = 'Matinas, ' + {'PRIMO': 'I', 'SECONDO': 'II', 'TERZO': 'III'}[sc.split()[0]] + ' noturno'
                else:
                    m = re.match(r'^(FERIA [IVX]+|SABBATO)', sc)
                    dia = {'FERIA II': 'segunda-feira', 'FERIA III': 'terça-feira', 'FERIA IV': 'quarta-feira',
                           'FERIA V': 'quinta-feira', 'FERIA VI': 'sexta-feira', 'SABBATO': 'sábado'}.get(m.group(1), sc) if m else sc
                    hora = 'Matinas'
                out.setdefault(n, []).append({'saltério': 'Pio V (Tridentino)', 'dia': dia, 'hora': hora, 'trecho': '',
                                              'antifona': '', 'pagina_afonso': sorted(p for p in s['pags'] if p)[:1]})
    return out


def dedup_missa(lst):
    """Junta entradas iguais (títulos, parte, versículos, texto) de arquivos que são variantes (Quad3-6, Quad3-6t …)."""
    por = {}
    for x in lst:
        k = (x['titulo'], x['parte'], x['versos'], x['texto'])
        if k in por:
            if x['arquivo'] not in por[k]['arquivo'].split(' + '):
                por[k]['arquivo'] += ' + ' + x['arquivo']
        else:
            por[k] = dict(x)
    return sorted(por.values(), key=lambda x: x['arquivo'])


def construir():
    lh, lect, missa = ler_lh(), ler_lecionario(), ler_missa()
    ofic, mat5 = ler_oficio(), ler_matinas_pio5()
    # Invitatório (Sl 94 da Vulgata) vem de Afonso/DO fora dessas seções: acrescentado à mão no montador
    res = {}
    for h in range(1, 151):
        # a Vulgata correspondente(s) a este hebraico
        vul = {1: [1]}.get(h)
        vs = [v for v in range(1, 151) if h in hebs_da_vulg(v)]
        res[str(h)] = {
            'vulgata': vs,
            'lh': lh.get(h, []),
            'lect': lect.get(h, []),
            'missa': dedup_missa([dict(x, vulg=v) for v in vs for x in missa.get(v, [])]),
            'oficio': [dict(x, vulg=v) for v in vs for x in (ofic.get(v, []) + mat5.get(v, []))],
        }
    json.dump(res, open(os.path.join(MOD, 'liturgia.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('LH:', sum(1 for v in res.values() if v['lh']), 'salmos; lecionário:', sum(1 for v in res.values() if v['lect']),
          '; missal antigo:', sum(1 for v in res.values() if v['missa']), '; oficio antigo:', sum(1 for v in res.values() if v['oficio']))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'baixar':
        baixar()
    elif cmd == 'construir':
        construir()
    else:
        print(__doc__)
