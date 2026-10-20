"""São Gregório de Nissa, In inscriptiones Psalmorum (GNO V, ed. McDonough): os trechos de cada salmo.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-nissa-sl.py
PDF do khazarzar (cache/base/grc/). A obra é um tratado sobre a ordem do Saltério e os títulos dos salmos, não um
comentário seguido: no Livro II (a partir do cap. A, col. 66352 do texto limpo) Gregório cita o título ou o primeiro
versículo de alguns salmos e comenta. Para cada salmo da LXX, os trechos são os parágrafos em que aparece uma sequência de
5 palavras do v. 1 (título) ou do v. 2 que não se repete em nenhum outro salmo (régua: Saltério da LXX, _grc.lxx());
trechos próximos são juntados e vão separados por «[…]». Heurística: conferir a leitura. Os marcadores «[PG 5, 119]» do
texto limpo são páginas da GNO V (volume 5), não colunas da PG. Hebraico h -> LXX por _grc.lxx_de_hebr.
"""
import collections, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-nissa-sl.py'
URL = _grc.khz('Gregory of Nyssa_PG 44-46', 'In inscriptiones Psalmorum.pdf')
t = _grc.texto(URL, 'nissa-inscr')
tt = _grc.semacento(t)
L = _grc.lxx()
LIVRO2 = t.index('ΚΕΦΑΛΑΙΟΝ Αʹ Τούτων οὖν οὕτως')

cont = collections.defaultdict(set)
for c, vv in L.items():
    for v, tx in vv.items():
        w = _grc._palavras(tx)
        for i in range(len(w) - 4):
            cont[tuple(w[i:i + 5])].add(c)

hits = collections.defaultdict(list)
for n in range(1, 151):
    for v in (1, 2):
        w = _grc._palavras(L[n].get(v, ''))
        for i in range(len(w) - 4):
            j = tuple(w[i:i + 5])
            if len(cont[j]) != 1:
                continue
            for m in re.finditer(r'\W{0,6}'.join(map(re.escape, j)), tt):
                if m.start() > LIVRO2:
                    hits[n].append(m.start())


def frase_ini(p):
    pre = t[max(0, p - 400):p]
    ks = list(re.finditer(r'[.;·] ', pre))
    return p - len(pre) + ks[0].end() if ks else p


def frase_fim(p):
    m = re.search(r'[.;·] ', t[p:p + 500])
    return p + m.end() if m else p


trechos = {}
for n, ps in hits.items():
    ps = sorted(set(ps))
    grupos = []
    for p in ps:
        if grupos and p - grupos[-1][-1] < 2500:
            grupos[-1].append(p)
        else:
            grupos.append([p])
    tr = []
    for g in grupos[:6]:
        a = frase_ini(max(0, g[0] - 700))
        b = frase_fim(min(len(t) - 1, g[-1] + 1800))
        if tr and a <= tr[-1][1]:
            tr[-1] = (tr[-1][0], b)
        else:
            tr.append((a, b))
    trechos[n] = tr
print('salmos com trechos (LXX):', sorted(trechos))


def gno(a, b):
    c = _grc.colunas(t, a, b)
    if not c:
        return 'GNO V'
    return f'GNO V (McDonough), pp. {c[1]}–{c[2]}' if c[1] != c[2] else f'GNO V (McDonough), p. {c[1]}'


ausentes, tam, grav = {}, 0, 0
for h in _grc.conjunto_hebr():
    ls = _grc.lxx_de_hebr(h)
    pres = [n for n in ls if n in trechos]
    if not pres:
        ausentes[h] = [f'- São Gregório de Nissa, In inscriptiones Psalmorum: nenhum trecho sobre o Sl {h} (hebr.) = Sl '
                       + ' e '.join(str(x) for x in ls) + ' (LXX): o tratado só cita o título ou o v. 1 de uns 25 salmos.']
        continue
    partes, ini, fim = [], None, None
    for n in pres:
        for a, b in trechos[n]:
            partes.append(t[a:b].strip())
            ini = a if ini is None else min(ini, a)
            fim = b if fim is None else max(fim, b)
    corpo = '\n\n[…]\n\n'.join(partes)
    pas = _grc.nota_numeracao(h)
    if len(pres) < len(ls):
        pas += f' (neste texto só o Sl {" e ".join(str(x) for x in pres)} da LXX)'
    _grc.gravar_base(h, 'gregorio-nissa-in-inscriptiones-psalmorum', 'São Gregório de Nissa, In inscriptiones Psalmorum',
                     'São Gregório de Nissa (c. 335–c. 395)', 'In inscriptiones Psalmorum (Εἰς τὰς ἐπιγραφὰς τῶν Ψαλμῶν)',
                     pas, gno(ini, fim), URL,
                     'só os trechos em que Gregório cita o título ou o primeiro versículo do salmo e comenta (não é comentário seguido)',
                     'sim', 'grc', SCRIPT, corpo,
                     'Nota: trechos achados por busca do título/1º versículo; os marcadores «[PG 5, n]» são páginas da GNO V.')
    tam += len(corpo)
    grav += 1
_grc.registrar(SCRIPT, 'ausentes', ausentes)
print(f'{SCRIPT}: {grav} arquivos, {tam // 1024} KB; ausentes {len(ausentes)}')
