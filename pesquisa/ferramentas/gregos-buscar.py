# Procura citações de versículos nos textos limpos (saída de gregos-limpar.py), sem depender de acentos.
# uso: python -I -X utf8 gregos-buscar.py arquivos... > achados.txt
# PADROES abaixo são os do Sl 32 (LXX): trocar pelos do capítulo novo (texto grego sem acentos, σ no lugar de ς).
import sys, re, unicodedata

def tira(s):
    d = unicodedata.normalize('NFD', s)
    d = ''.join(c for c in d if not unicodedata.combining(c))
    return d.lower().replace('ς', 'σ')

PADROES = {
    'v1': r'αγαλλιασθε,? δικαιοι',
    'v1b': r'τοισ ευθεσι πρεπει αινεσισ',
    'v2': r'ψαλτηριω δεκαχορδω',
    'v3': r'ασατε αυτω ασμα καινον|ασμα καινον',
    'v4': r'ευθ[υη]σ ο λογοσ του κυριου',
    'v5': r'του ελεουσ (του )?κυριου πληρησ η γη',
    'v6': r'λογω (του )?κυριου οι ουρανοι εστερεωθησαν|πνευματι του στοματοσ αυτου',
    'v7': r'ωσ(ει)? ασκον υδατα|τιθεισ εν θησαυροισ αβυσσουσ',
    'v9': r'αυτοσ ειπε,? και εγενηθησαν|αυτοσ ενετειλατο,? και εκτισθησαν',
    'v10': r'διασκεδαζει βουλασ εθνων',
    'v11': r'βουλη (δε )?του κυριου εισ τον αιωνα μενει',
    'v12': r'μακαριον το εθνοσ',
    'v15': r'πλασα[σσ]? κατα ?μονασ|κατα ?μονασ τασ καρδιασ',
    'v16': r'ου σωζεται βασιλευσ|γιγασ ου σωθησεται',
    'v17': r'ψευδησ ιπποσ',
    'v19': r'διαθρεψαι αυτουσ εν λιμω',
    'v22': r'γενοιτο,? κυριε,? το ελεοσ σου|καθαπερ ηλπισαμεν επι σε',
}

for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    tt = tira(t)
    # tira() preserva o comprimento? NFD + remoção de combinantes muda posições; mapear por índice
    # reconstruir mapa de posições
    mapa = []
    out = []
    for i, ch in enumerate(t):
        d = unicodedata.normalize('NFD', ch)
        d = ''.join(c for c in d if not unicodedata.combining(c)).lower().replace('ς', 'σ')
        for c in d:
            out.append(c)
            mapa.append(i)
    tt = ''.join(out)
    for k, p in PADROES.items():
        for m in re.finditer(p, tt):
            i = mapa[m.start()]
            # PG mais próxima antes
            pg = re.findall(r'\[PG \d+, \d+\]', t[:i])
            print(f'{f}\t{k}\t{i}\t{pg[-1] if pg else ""}\t{t[max(0, i-150):i+200]}')
            print()
