"""Alcuíno, Interrogationes et responsiones in Genesin (280 perguntas a Sigulfo), por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-alcuino.py 1        (ou 1-50)

Baixa uma vez o texto 21416 do Corpus Corporum (PL 100, 515–570; https://mlat.uzh.ch/browser/cps_2.Alcuin.InEtReI)
e grava genesis/<ccc>/base/alcuino-interrogationes-in-genesin.md. Cada pergunta («Inter. N.») é independente: o
capítulo sai da nota de Migne «(Gen. I, 26)» ou do lema citado; as primeiras (1–25), gerais, ficam sem capítulo,
menos as que citam um versículo. As perguntas não seguem sempre a ordem do livro: junta todas as do capítulo.
A última pergunta (Gn 49, as bênçãos dos patriarcas) vai até «DICTA BEATI ALBINI».
"""
import importlib.util, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

caps = C.capitulos_args(__doc__)
IDNO = 21416
b = C.bruto(IDNO)
pars = C.L.limpar_pl(b)
ini, fim = C.secao(pars, r'PRAEFATIO ALCUINI', r'DICTA BEATI ALBINI')
RX_Q = re.compile(r'^(?:\[col\. \w+\] )?(?:\d+ )?Inter(?:rogatio)?\.? ?(\d+)')
RX_NOTA = re.compile(r'\(Gen(?:es)?\.?\s*([IVXL]+)[,.]')
qs = []  # (ini, fim, cap, n)
i = ini
ant = None
while i < fim:
    m = RX_Q.match(pars[i]['t'])
    if not m:
        i += 1
        continue
    j = i + 1
    while j < fim and not RX_Q.match(pars[j]['t']) and not re.search(r'DE BENEDICTIONIBUS PATRIARCHARUM', pars[j]['t']):
        j += 1
    t = ' '.join(p['t'] for p in pars[i:j])
    cap = None
    n = RX_NOTA.search(t)
    if n:
        cap = C.L.de_romano(n.group(1))
    if cap is None and re.search(r'\((?:vers\.|Ibid)', t):
        cap = ant                      # «(vers. 3)», «(Ibid.)»: o capítulo da pergunta anterior
    if cap is None:
        q = re.split(r'--\s*Resp', t)[0]
        cv = C.lema(q, minimo=2)
        cap = cv[0] if cv else None
    qs.append((i, j, cap, int(m.group(1))))
    ant = cap if cap else ant
    i = j
# pergunta sem citação entre duas do mesmo capítulo (ou logo depois de uma com «Faciamus», «Fiat»…) fica nele
for k in range(1, len(qs)):
    if qs[k][2] is None:
        prox = next((q[2] for q in qs[k + 1:] if q[2] is not None), None)
        if qs[k - 1][2] is not None and qs[k - 1][2] == prox:
            qs[k] = (qs[k][0], qs[k][1], prox, qs[k][3])
for cap in caps:
    sel = [(a, z, n) for a, z, c, n in qs if c == cap]
    if cap == 49:
        a, z = C.secao(pars, r'DE BENEDICTIONIBUS PATRIARCHARUM', r'DICTA BEATI ALBINI')
        sel.append((a, z, 'bênçãos'))
    if not sel:
        C.registrar_ausente(cap, 'Alcuíno, Interrogationes in Genesin', 'nenhuma pergunta sobre este capítulo.')
        print(f'  Gn {cap}: nada')
        continue
    nums = [str(n) for _, _, n in sel]
    juntos = []                        # perguntas seguidas viram um trecho só
    for a, z, n in sel:
        if juntos and juntos[-1][1] == a:
            juntos[-1] = (juntos[-1][0], z, None)
        else:
            juntos.append((a, z, None))
    sel = juntos
    C.gravar_partes(cap, 'alcuino-interrogationes-in-genesin.md', {
        'titulo': 'Alcuíno, Interrogationes et responsiones in Genesin',
        'autor': 'Alcuíno de York (c. 735–804)',
        'obra': 'Interrogationes et responsiones in Genesin',
        'passagem': f'Gn {cap}: perguntas {", ".join(nums)}',
        'pl': 100, 'fonte': C.url_cc(IDNO), 'script': 'gen-latinos-alcuino.py',
        'cobre': 'só as perguntas que citam o capítulo',
    }, pars, sel, b)
