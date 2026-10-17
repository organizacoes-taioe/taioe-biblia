# Limpa o texto extraído dos PDFs da "Ψηφιακή Πατρολογία" (Univ. do Egeu, via khazarzar):
# tira rodapés e números de página, une as linhas, cola palavras partidas na quebra de linha
# e transforma os marcadores de coluna "29.325" em "[PG 29, 325]".
# uso: python -I -X utf8 gregos-limpar.py entrada.pdf saida.txt [inicio_regex] [fim_regex]
# Precisa do PyMuPDF (fitz). Atenção: em PDFs que seguem edição moderna (GNO, Kotter, Stählin, Reischl-Rupp)
# o marcador "n.m" não é coluna da PG, e o "[PG n, m]" que sai daqui é só o número da edição.
# As junções de palavras são automáticas: conferir na leitura (ver relatorio-gregos.md do Sl 33).
import sys, re, unicodedata, fitz

src, out = sys.argv[1], sys.argv[2]
ini = sys.argv[3] if len(sys.argv) > 3 else None
fim = sys.argv[4] if len(sys.argv) > 4 else None

doc = fitz.open(src)
linhas = []
for p in doc:
    linhas.extend(p.get_text().split('\n'))

RODAPE = ('Ερευνητικό έργο', 'Χρηµατοδότηση', 'Εργαστήριο ∆ιαχείρισης', 'Πανεπιστήµιο Αιγαίου',
          'Επιτρέπεται η ελεύθερη')
boas = []
for l in linhas:
    s = l.strip()
    if any(s.startswith(r) for r in RODAPE):
        continue
    if re.fullmatch(r'\d{1,4}', s):
        continue
    boas.append(s)
txt = ' '.join(boas)
txt = re.sub(r'\s+', ' ', txt)
txt = txt.replace('∆', 'Δ').replace('µ', 'μ').replace('Ω', 'Ω')

todo = txt
if ini:
    m = re.search(ini, txt)
    if m:
        txt = txt[m.start():]
if fim:
    m = re.search(fim, txt)
    if m:
        txt = txt[:m.start()]

CLITICOS = set('''ἐν εἰς ἐς ἐκ ἐξ οὐ οὐκ οὐχ ὁ ἡ οἱ αἱ ὡς εἰ μου μοι με σου σοι σε τις τι τινος τινι τινα
τινες τινων τισι τισιν τινας του τῳ που πως ποτε πω πῃ γε τε τοι περ νυν ἐστι ἐστιν εἰσι εἰσιν φημι
φησι φησιν ἐσμεν ἐστε εἰμι φασι φασιν ποθεν ποι μιν νιν'''.split())


def nfd(w):
    return unicodedata.normalize('NFD', w)


def tem_acento(w):
    d = nfd(w)
    return any(c in d for c in '́̀͂')


def tem_espirito(w):
    d = nfd(w)
    return any(c in d for c in '̓̔')


def nucleo(w):
    return unicodedata.normalize('NFC', re.sub(r'[^\ẁ-ͯ]', '', nfd(w)))


def eh_grego_min(w):
    if not w:
        return False
    c = nfd(w)[0]
    return 'α' <= c <= 'ω'


APOS = "’'ʼ᾿"


def podejuntar(a, t):
    na, nb = nucleo(a), nucleo(t)
    if not (na and nb and eh_grego_min(nb)):
        return None
    if a[-1] in '.,;·:!)]' + APOS or any(c in t for c in APOS):
        return None
    if not re.match(r'\w', nfd(t)[0]):
        return None
    return na, nb


FIM = ('αι', 'ος', 'ον', 'ων', 'ης', 'ας', 'ειν', 'ιν', 'ου', 'ους', 'ην', 'αν', 'ες', 'ως', 'ει',
       'ται', 'ναι', 'σι', 'μεν', 'τε', 'το', 'ντο', 'σαν', 'οις', 'αις', 'ις', 'ιας', 'ιαν')

# frequência das palavras no texto inteiro, para escolher a junção atestada
import collections
freq = collections.Counter(nucleo(w).lower() for w in todo.split(' '))


def fragmento(t):
    n = nucleo(t)
    if not n or not re.match('[Ͱ-Ͽἀ-῿]', n[0]):
        return False
    d0 = nfd(n)
    if d0[0] in 'αεηιουω' and not tem_espirito(n[:2]) and '̈' not in d0[:3]:
        return 'vogal'
    if not tem_acento(n) and n.lower() not in CLITICOS:
        return 'sem_acento'
    return False


def pode(a, t, a_maiusc=False):
    """a + t podem ser uma palavra só (t em minúscula, sem pontuação no meio)."""
    na, nb = nucleo(a), nucleo(t)
    if not (na and nb and eh_grego_min(nb)):
        return False
    if a[-1] in '.,;·:!)]' + APOS or any(c in a for c in APOS) or any(c in t for c in APOS):
        return False
    if not re.match(r'\w', nfd(t)[0]) or not re.match(r'\w', nfd(a[-1])[0]):
        return False
    return True


# os marcadores de coluna da PG ("29.337") às vezes caem no meio de uma palavra:
# tiro-os da sequência e os recoloco antes da palavra seguinte já inteira.
brutos = txt.split(' ')
toks, pres, pend = [], [], []
for w in brutos:
    if re.fullmatch(r'\d{1,3}\.\d{1,4}', w):
        pend.append(w)
        continue
    m = re.match(r'^(\d{1,3}\.\d{1,4})(\S+)$', w)
    if m:
        pend.append(m.group(1))
        w = m.group(2)
    toks.append(w)
    pres.append(pend)
    pend = []

i = 0
res, rpre, depois = [], [], []
while i < len(toks):
    t = toks[i]
    f = fragmento(t)
    if f:
        prev_ok = bool(res) and pode(res[-1], t)
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        next_ok = f == 'sem_acento' and nxt is not None and pode(t, nxt)
        escolha = None
        if prev_ok and not next_ok:
            escolha = 'prev'
        elif next_ok and not prev_ok:
            escolha = 'next'
        elif prev_ok and next_ok:
            fp = freq[(nucleo(res[-1]) + nucleo(t)).lower()]
            fn = freq[(nucleo(t) + nucleo(nxt)).lower()]
            if fp > fn:
                escolha = 'prev'
            elif fn > fp:
                escolha = 'next'
            else:
                escolha = 'prev' if nucleo(t).endswith(FIM) else 'next'
        if escolha == 'prev':
            res[-1] = res[-1] + t
            depois.extend(pres[i])
            i += 1
            continue
        if escolha == 'next':
            toks[i + 1] = t + nxt
            pres[i + 1] = pres[i] + pres[i + 1]
            i += 1
            continue
    res.append(t)
    rpre.append(depois + pres[i])
    depois = []
    i += 1
saida = []
for w, ms in zip(res, rpre):
    saida.extend(ms)
    saida.append(w)
saida.extend(depois)
txt = ' '.join(saida)
txt = re.sub(r'\b(\d{1,3})\.(\d{1,4})\b', r'[PG \1, \2]', txt)
txt = unicodedata.normalize('NFC', txt)
open(out, 'w', encoding='utf-8').write(txt)
print(len(txt))
