"""Orígenes, Fragmenta in Psalmos 1–150 (cadeias; ed. Pitra, *Analecta sacra* III): um arquivo por salmo.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-origenes-fragmenta-sl.py
PDF do khazarzar «Origenes_PG 11-17/Fragmenta in Psalmos.pdf». Os marcadores «[PG 32, 6]» do texto limpo NÃO são colunas
da PG: são salmo 32, versículo 6 (LXX), e vêm antes do texto do versículo. O texto do v. 1 (e do 2) fica antes do primeiro
marcador do salmo, então o começo de cada salmo é achado pelo primeiro versículo citado entre o último marcador do salmo
anterior e o primeiro do salmo (se não achar, vale o primeiro marcador). OCR ruim (palavras partidas, letras trocadas).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-origenes-fragmenta-sl.py'
URL = _grc.khz('Origenes_PG 11-17', 'Fragmenta in Psalmos.pdf')
t = _grc.texto(URL, 'origenes-frag')
tt = _grc.semacento(t)
mar = [(m.start(), int(m.group(1)), int(m.group(2))) for m in re.finditer(r'\[PG (\d+), (\d+)\]', t)]
primeiro, ultimo = {}, {}
for p, a, b in mar:
    primeiro.setdefault(a, p)
    ultimo[a] = p
presentes = sorted(primeiro)
print('salmos com marcador:', len(presentes), '| sem marcador:', [n for n in range(1, 151) if n not in primeiro])

ini, achados, so_marcador = {}, [], []
for n in presentes:
    pm = primeiro[n]
    lo = ultimo.get(max([x for x in presentes if x < n], default=0), 0)
    pos = None
    if n > 1:
        pos = _grc.achar_incipit(tt, n, lo + 20, pm, 4) or _grc.achar_incipit(tt, n, lo + 20, pm, 3)
    if pos is not None:
        ini[n] = _grc.recuar(t, pos, voltar=1)
        if ini[n] <= lo:
            ini[n] = pos
        achados.append(n)
    else:
        ini[n] = 0 if n == 1 else pm
        if n > 1:
            so_marcador.append(n)
print('começo pelo 1º versículo:', len(achados), '| só pelo primeiro marcador:', so_marcador)

_grc.produzir(
    SCRIPT, 'origenes-fragmenta-in-psalmos', 'Orígenes, Fragmenta in Psalmos 1–150 (Pitra)',
    'Orígenes de Alexandria (c. 185–254)', 'Fragmenta in Psalmos (cadeias; ed. Pitra, Analecta sacra III)', URL, t, ini,
    edicao_fn=lambda h, pres, a, b: 'Pitra, Analecta sacra III (marcadores «[PG n, m]» = salmo n, versículo m; não há colunas da PG)',
    cobre_fn=lambda h, pres, corpo: ('fragmentos de cadeia sobre versículos do salmo (nem todos); marcadores [PG n, m] = salmo, '
                                    'versículo; OCR ruim'),
    extra_fn=lambda h, pres: ('Nota: os marcadores «[PG n, m]» deste arquivo são salmo n, versículo m (LXX), não colunas da PG.'
                              + (' O começo foi tomado do primeiro marcador do salmo: o texto dos primeiros versículos pode estar no fim do arquivo do salmo anterior.'
                                 if any(n in so_marcador for n in pres) else '')),
    motivo_ausente=lambda h: 'a coleção não tem marcador para este salmo')
