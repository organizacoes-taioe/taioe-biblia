"""São Basílio Magno, Homiliae super Psalmos (PG 29, 209–494) e as homilias espúrias aos Salmos (PG 30).

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-basilio-sl.py
Autênticas (um PDF, «Homiliae super Psalmos.pdf»): Sl 1, 7, 14, 28, 29, 32, 33, 44, 45, 48, 59, 61, 114 (LXX), cada
uma começa em «ΕΙΣ ΤΟΝ <numeral> ΨΑΛΜΟΝ». Espúrias (PDFs à parte, PG 30; arquivos «pseudo-basilio-…»): Sl 28 (outra
homilia), 37, 115 e 132 (LXX; o PDF se chama «CXXII»). Numeração da LXX; o hebraico h vem de _grc.lxx_de_hebr.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-basilio-sl.py'
PASTA = 'Basilius Caesariensis_PG 29-32'
URL = _grc.khz(PASTA, 'Homiliae super Psalmos.pdf')
t = _grc.texto(URL, 'basilio-hps')

starts = {}
for m in re.finditer(r'(?:ΤΟΥ ΑΥΤΟΥ\s+)?(?:ΟΜΙΛΙΑ\s+)?ΕΙΣ\s+ΤΟΝ\s+(ΠΡΩΤΟΝ|[Α-ΩϚ]{1,5}ʹ?)\s+ΨΑΛΜΟΝ', t):
    n = 1 if m.group(1) == 'ΠΡΩΤΟΝ' else _grc.num_grego(m.group(1))
    starts[n] = m.start()
print('homilias autênticas achadas (LXX):', sorted(starts))
assert sorted(starts) == [1, 7, 14, 28, 29, 32, 33, 44, 45, 48, 59, 61, 114], sorted(starts)

_grc.produzir(
    SCRIPT, 'basilio-homiliae-super-psalmos', 'São Basílio Magno, Homiliae in Psalmos',
    'São Basílio Magno (c. 330–379)', 'Homiliae super Psalmos (Ὁμιλίαι εἰς τοὺς Ψαλμούς)', URL, t, starts,
    cobre_fn=lambda h, pres, corpo: 'o salmo inteiro (homilia contínua)',
    nome_ausente='São Basílio, Homiliae in Psalmos',
    motivo_ausente=lambda h: ('Basílio só comentou os Sl 1, 7, 14, 28, 29, 32, 33, 44, 45, 48, 59, 61 e 114 da LXX'
                              + (' (há homilia ESPÚRIA atribuída a ele sobre este salmo: «pseudo-basilio-…» nesta pasta)'
                                 if h in (38, 133) else '')))

# ---- espúrias (PG 30) ----
ESP = [  # (arquivo no khazarzar, nome em cache, salmo LXX, nota)
    ('In Psalmum XXVIII.pdf', 'basilio-28', 28, 'segunda homilia sobre o Sl 28, atribuída a Basílio'),
    ('Homilia in Psalmum XXXVII 1.pdf', 'basilio-37', 37, 'homilia sobre o Sl 37, atribuída a Basílio'),
    ('Homilia in Psalmum CXV.pdf', 'basilio-115', 115, 'homilia sobre o Sl 115, atribuída a Basílio'),
    ('Homilia in Psalmum CXXII.pdf', 'basilio-122', 132, 'homilia sobre o Sl 132 (o PDF se chama «CXXII»), atribuída a Basílio'),
]
for arq, nome, n, nota in ESP:
    u = _grc.khz(PASTA, arq)
    tx = _grc.texto(u, nome)
    corpo = re.sub(r'^\s*(?:In|Homilia in) Psalmum \S+( \d)?\s*', '', tx).strip()
    hs = [h for h in _grc.conjunto_hebr() if n in _grc.lxx_de_hebr(h)]
    for h in hs:
        pas = _grc.nota_numeracao(h)
        if len(_grc.lxx_de_hebr(h)) > 1:
            pas += f' (neste texto só o Sl {n} da LXX)'
        _grc.gravar_base(
            h, f'pseudo-basilio-homilia-in-psalmum-{n}', f'Pseudo-Basílio, Homilia sobre o Sl {n} (LXX; espúria)',
            'Pseudo-Basílio (atribuída a São Basílio Magno; espúria)', f'Homilia in Psalmum {n} (PG 30; {nota})',
            pas, _grc.titulo_edicao(tx, 0, len(tx)), u, 'o salmo inteiro (homilia espúria; não citar como de Basílio)',
            'sim', 'grc', SCRIPT, corpo)
    print(f'espúria Sl {n} (LXX) -> hebr {hs}: {len(corpo)} car.')
