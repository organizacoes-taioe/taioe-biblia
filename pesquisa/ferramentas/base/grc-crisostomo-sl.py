"""São João Crisóstomo, Expositiones in Psalmos (PG 55, 35–498) e os PDFs à parte sobre salmos (PG 55).

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-crisostomo-sl.py
1) «Expositiones in Psalmos.pdf» (autêntico): comenta só os Sl 4–12, 41, 43–49, 108–117, 119–150 da LXX; cada um
   começa em «ΕΙΣ ΤΟΝ <numeral> ΨΑΛΜΟΝ». No PDF os Sl 8–12 aparecem DUAS vezes (duas redações seguidas, ambas com o
   mesmo cabeçalho): o arquivo do salmo junta as duas, separadas por uma linha.
2) PDFs à parte (khazarzar, mesma pasta): Sl 50 (sem marca de espúrio), 145 (idem) e os marcados «[Sp.]» (espúrios,
   arquivos «pseudo-crisostomo-…»): Sl 50 (duas homilias), 75, 92, 94, 100, 101–107 (um PDF só), 118 (3 homilias), 139.
Numeração da LXX; o hebraico h vem de _grc.lxx_de_hebr. O «Prooemia in Psalmos» (introdução geral) não entra.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-crisostomo-sl.py'
PASTA = 'John Chrysostom_PG 47-64'
URL = _grc.khz(PASTA, 'Expositiones in Psalmos.pdf')
t = _grc.texto(URL, 'crisostomo-ps')

# ---- 1) obra principal ----
blocos = []          # (n, pos)
prev = 3
for m in re.finditer(r'ΕΙΣ\s+ΤΟΝ\s*([Α-Ωςϛ Ϛʹ]{1,7})\s*ΨΑΛΜΟΝ', t):
    v = _grc.num_grego(m.group(1))
    if v is None:
        v = prev + 1                                  # numeral perdido (o ϛ de «ʹ» = 6)
    elif v % 10 == 0 and prev == v + 5:
        v += 6                                        # «ΡΚ ʹ» por «ΡΚϛʹ»
    blocos.append((v, m.start()))
    prev = v
nums = sorted(set(n for n, _ in blocos))
ESPERADO = list(range(4, 13)) + [41] + list(range(43, 50)) + list(range(108, 118)) + list(range(119, 151))
assert nums == ESPERADO, (nums, [n for n in ESPERADO if n not in nums])
rep = sorted(set(n for n in nums if [x for x, _ in blocos].count(n) > 1))
print('obra principal: salmos achados =', len(nums), '| repetidos no PDF:', rep)

SEP = '\n\n[segunda redação do mesmo salmo, repetida no PDF]\n\n'
corpo_n, faixa_n = {}, {}
for i, (n, ini) in enumerate(blocos):
    fim = blocos[i + 1][1] if i + 1 < len(blocos) else len(t)
    corpo_n[n] = (corpo_n[n] + SEP if n in corpo_n else '') + t[ini:fim].strip()
    a, b = faixa_n.get(n, (ini, fim))
    faixa_n[n] = (min(a, ini), max(b, fim))

ausentes, tam, grav = {}, 0, 0
for h in _grc.conjunto_hebr():
    ls = _grc.lxx_de_hebr(h)
    pres = [n for n in ls if n in corpo_n]
    if not pres:
        ausentes[h] = [f'- São João Crisóstomo, Expositiones in Psalmos: não comentou o Sl {h} (hebr.) = Sl '
                       + ' e '.join(str(x) for x in ls)
                       + ' (LXX); a obra cobre só os Sl 4–12, 41, 43–49, 108–117 e 119–150 da LXX.'
                       + (' Há PDF(s) à parte sobre este salmo, ver os arquivos «crisostomo-in-psalmum-…» e '
                          '«pseudo-crisostomo-…» (espúrios) desta pasta.'
                          if any(x in (50, 75, 92, 94, 100, 101, 102, 103, 104, 105, 106, 107, 118, 139, 145) for x in ls)
                          else '')]
        continue
    corpo = '\n\n'.join(corpo_n[n] for n in pres)
    a, b = faixa_n[pres[0]][0], faixa_n[pres[-1]][1]
    pas = _grc.nota_numeracao(h)
    if len(pres) < len(ls):
        pas += f' (neste texto só o Sl {" e ".join(str(x) for x in pres)} da LXX)'
    extra = None
    if any(n in rep for n in pres):
        extra = 'Nota: o PDF traz duas redações seguidas deste comentário; ficam juntas, separadas por uma linha.'
    _grc.gravar_base(h, 'crisostomo-expositiones-in-psalmos', 'São João Crisóstomo, Expositiones in Psalmos',
                     'São João Crisóstomo (c. 349–407)', 'Expositiones in Psalmos (Ἑρμηνεία εἰς τοὺς Ψαλμούς)', pas,
                     _grc.titulo_edicao(t, a, b), URL, 'o salmo inteiro (homilias contínuas)', 'sim', 'grc', SCRIPT,
                     corpo, extra)
    tam += len(corpo)
    grav += 1
_grc.registrar(SCRIPT, 'ausentes', ausentes)
print(f'{SCRIPT}: obra principal {grav} arquivos, {tam // 1024} KB; ausentes {len(ausentes)}')

# ---- 2) PDFs à parte ----
EXTRAS = [  # (arquivo, cache, salmo LXX, espúrio?, nome do arquivo, título/obra, nota)
    ('In Psalmum 50.pdf', 'crisostomo-sl50', 50, False, 'crisostomo-in-psalmum-50', 'In Psalmum 50',
     'PDF à parte, sem marca de espúrio no khazarzar; autoria a conferir na PG 55, 527–532'),
    ('In Psalmum 145.pdf', 'crisostomo-sl145', 145, False, 'crisostomo-in-psalmum-145', 'In Psalmum 145',
     'homilia dita na Semana Santa; PDF à parte, sem marca de espúrio no khazarzar'),
    ('In Psalmum 50 homilia 1.pdf', 'crisostomo-sl50h1', 50, True, 'pseudo-crisostomo-in-psalmum-50-homilia-1',
     'In Psalmum 50, homilia 1', 'espúria [Sp.]'),
    ('In Psalmum 50 homilia 2.pdf', 'crisostomo-sl50h2', 50, True, 'pseudo-crisostomo-in-psalmum-50-homilia-2',
     'In Psalmum 50, homilia 2', 'espúria [Sp.]'),
    ('In Psalmum 75.pdf', 'crisostomo-sl75', 75, True, 'pseudo-crisostomo-in-psalmum-75', 'In Psalmum 75',
     'espúria [Sp.]'),
    ('In Psalmum 92.pdf', 'crisostomo-sl92', 92, True, 'pseudo-crisostomo-in-psalmum-92', 'In Psalmum 92',
     'espúria [Sp.]'),
    ('In Psalmum 94.pdf', 'crisostomo-sl94', 94, True, 'pseudo-crisostomo-in-psalmum-94', 'In Psalmum 94',
     'espúria [Sp.]'),
    ('In Psalmum 100.pdf', 'crisostomo-sl100', 100, True, 'pseudo-crisostomo-in-psalmum-100', 'In Psalmum 100',
     'espúria [Sp.]'),
    ('In Psalmum 118.pdf', 'crisostomo-sl118', 118, True, 'pseudo-crisostomo-in-psalmum-118',
     'In Psalmum 118 (homilias 1–3)', 'espúria [Sp.]; três homilias seguidas sobre o Sl 118 da LXX'),
    ('In Psalmum 139.pdf', 'crisostomo-sl139', 139, True, 'pseudo-crisostomo-in-psalmum-139', 'In Psalmum 139',
     'espúria [Sp.]'),
]


def limpa_titulo(tx):
    """Tira a linha de título que o khazarzar põe no começo («In Psalmum 75 [Sp.] …»)."""
    return re.sub(r'^\s*In Psalm\S*\s+[\d_\-]+(?:\s*\([^)]*\))?(?:\s*\[Sp\.\])?\s*', '', tx).strip()


def grava_extra(h, n, nome, rotulo_obra, tx, corpo, u, espurio, nota):
    pas = _grc.nota_numeracao(h)
    if len(_grc.lxx_de_hebr(h)) > 1:
        pas += f' (neste texto só o Sl {n} da LXX)'
    autor = ('Pseudo-Crisóstomo (atribuído a São João Crisóstomo; espúrio)' if espurio
             else 'São João Crisóstomo (c. 349–407)')
    titulo = f'Pseudo-Crisóstomo, {rotulo_obra} (espúrio)' if espurio else f'São João Crisóstomo, {rotulo_obra}'
    cobre = 'o salmo inteiro (' + ('homilia espúria; não citar como de Crisóstomo' if espurio else 'homilia') + ')'
    _grc.gravar_base(h, nome, titulo, autor, f'{rotulo_obra} (PG 55; {nota})', pas,
                     _grc.titulo_edicao(tx, 0, len(tx)), u, cobre, 'sim', 'grc', SCRIPT, corpo)


for arq, cache, n, esp, nome, rot, nota in EXTRAS:
    u = _grc.khz(PASTA, arq)
    tx = _grc.texto(u, cache)
    corpo = limpa_titulo(tx)
    hs = [h for h in _grc.conjunto_hebr() if n in _grc.lxx_de_hebr(h)]
    for h in hs:
        grava_extra(h, n, nome, rot, tx, corpo, u, esp, nota)
    print(f'extra Sl {n} (LXX) -> hebr {hs}: {len(corpo)} car. ({"espúrio" if esp else "sem marca"})')

# Sl 101–107: um PDF só, espúrio
u = _grc.khz(PASTA, 'In Psalmos 101_107.pdf')
tx = _grc.texto(u, 'crisostomo-101_107')
cs = []
for m in re.finditer(r'ΨΑΛΜ\.\s*([Α-Ωςϛ Ϛʹ]{1,6})\.', tx):
    v = _grc.num_grego(m.group(1))
    if v and 101 <= v <= 107:
        cs.append((v, m.start()))
vals = [v for v, _ in cs]
assert vals == list(range(101, 108)), vals
for i, (n, ini) in enumerate(cs):
    fim = cs[i + 1][1] if i + 1 < len(cs) else len(tx)
    corpo = tx[ini:fim].strip()
    for h in [h for h in _grc.conjunto_hebr() if n in _grc.lxx_de_hebr(h)]:
        grava_extra(h, n, 'pseudo-crisostomo-in-psalmos-101-107', f'In Psalmos 101–107 (o Sl {n})', tx, corpo, u, True,
                    'espúria [Sp.]')
print('extra Sl 101–107 (LXX) -> hebr 102–108 gravados')
