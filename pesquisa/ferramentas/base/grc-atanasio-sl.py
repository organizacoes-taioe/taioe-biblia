"""Santo Atanásio, Expositiones in Psalmos (PG 27, 60–545): um arquivo por salmo comentado.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-atanasio-sl.py
PDF do khazarzar (baixado uma vez para cache/base/grc/), limpo com gregos-limpar.py. Cada salmo traz «<título>
ΨΑΛΜΟΣ … Βʹ. Ὑπόθεσις.» (numeração da LXX; o título vem ANTES do número e a palavra ΨΑΛΜΟΣ nem sempre está lá).
Onde o cabeçalho falta ou o OCR o estragou, o começo é achado pelo primeiro versículo citado (régua: o Saltério
da LXX, _grc.lxx()). O texto da Expositio acaba no Sl 146 da LXX (col. 548); o que o PDF traz depois (perguntas atribuídas a Atanásio, PG 27, 549–589) não entra.
O Sl 9 da LXX (hebr. 9 e 10) aparece em dois blocos: «Ἵνα τί, Κύριε, ἀφέστηκας» (Sl 9,22ss) é o Sl 10 hebraico.
Colchetes no texto = acréscimos de cadeia; várias glosas coincidem com as de Teodoreto e de Cirilo, sem colchetes.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-atanasio-sl.py'
URL = _grc.khz('Athanasius the Great of Alexandria_ PG 25-28', 'Expositiones in Psalmos.pdf')
t = _grc.texto(URL, 'atanasio-exp')
# depois do Sl 146 da LXX o PDF segue com perguntas atribuídas a Atanásio (PG 27, 549–589, «Ἀθανάσιος. Διὰ τί δὲ
# οἱ βασιλεῖς…»): não são a Expositio e ficam de fora (ver o mapa)
_fim = t.index('Ἀθανάσιος. Διὰ τί δὲ οἱ βασιλεῖς')
t = t[:_fim]

num = {}
for m in re.finditer(r'ΨΑΛΜΟΣ', t):
    seg = t[m.end():m.end() + 260]
    n = re.search(r'(?:^|[\s.,·])([Α-ΩϚS]{1,5}\s?[Sς]?\s?ʹ)', seg)
    if n:
        num[m.end() + n.start(1)] = (n.group(1), m.start())
for m in re.finditer(r'([Α-ΩϚS]{1,5}\s?[Sς]?\s?ʹ)\.?\s*Ὑπόθεσις', t):
    num.setdefault(m.start(1), (m.group(1), None))
c = [(p, _grc.num_grego(b.replace('S', 'ϛ')), b) for p, (b, _) in sorted(num.items())]
# o bloco «Ἵνα τί, Κύριε» (cabeçalho Ιʹ repetido) é o fim do Sl 9 da LXX
dup = [i for i in range(1, len(c)) if c[i][1] == 10 and c[i - 1][1] == 10][0]
bloco9b = c.pop(dup - 1)
assert 'Ἵνα τί' in t[bloco9b[0]:bloco9b[0] + 200]
fix = {}
for i, (p, v, b) in enumerate(c):
    if b.strip() in ('ΚΛʹ',) and v == 50:
        fix[i] = 24
    if b.strip() in ('ΑΓʹ',) and v == 4:
        fix[i] = 33
starts, probs = _grc.alinhar(c, maxgap=6, fix=fix)
_grc.avisos([p for p in probs if not p.startswith('FALTA')])
starts, achados, nao = _grc.completar(t, starts)
# o Sl 106 da LXX começa como o 105 e o 117 («Ἐξομολογεῖσθε τῷ Κυρίῳ, ὅτι χρηστός»): o acerto de completar() é
# só uma citação dentro do comentário ao Sl 105; Atanásio não tem o Sl 106
for _n in (106,):
    if _n in achados:
        del achados[_n]
        del starts[_n]
print('achados pelo versículo:', sorted(achados), '| sem rastro no texto:', nao)

# posição de começo de cada salmo: recuar do número (ou do versículo) até o título
ini = {}
for n, p in starts.items():
    if n in achados:
        # procura o numeral/ΨΑΛΜΟΣ logo antes do versículo achado
        pre = t[max(0, p - 400):p]
        k = [x for x in re.finditer(r'ΨΑΛΜΟΣ|[Α-ΩϚ]{1,5}ʹ?\.\s(?:Ὑπόθεσις|[Α-Ω][α-ω])', pre)]
        base = p - len(pre) + k[-1].start() if k else p
        ini[n] = _grc.recuar(t, base, voltar=1)
    else:
        pre = t[max(0, p - 300):p]
        k = list(re.finditer(r'ΨΑΛΜΟΣ', pre))
        if k and 'Ὑπόθεσις' not in pre[k[-1].start():]:
            ini[n] = _grc.recuar(t, p - len(pre) + k[-1].start(), voltar=1)
        else:
            ini[n] = _grc.recuar(t, p - 1, voltar=1)
ini[9.5] = _grc.recuar(t, bloco9b[0] - 1, voltar=1)
# o Sl 144 (último) acaba no fim do texto
ordem = sorted(ini.items(), key=lambda kv: kv[1])
limites = {n: (a, ordem[i + 1][1] if i + 1 < len(ordem) else len(t)) for i, (n, a) in enumerate(ordem)}

COBRE = 'o salmo inteiro: Ὑπόθεσις e glosa dos versículos (colchetes = acréscimos de cadeia)'
ausentes, tam, gravados = {}, 0, {}
for h in _grc.conjunto_hebr():
    ls = _grc.lxx_de_hebr(h)
    pres = [9.5] if h == 10 else [n for n in ls if n in limites]
    if not pres:
        ausentes[h] = [f'- Santo Atanásio, Expositiones in Psalmos: não comenta o Sl {h} (hebr.) = Sl '
                       + ' e '.join(str(x) for x in ls) + ' (LXX); o texto da PG 27 vai só até o Sl ' + str(max(limites)) + ' da LXX'
                       + (' ' if False else '') + '.']
        continue
    a, b = limites[pres[0]][0], limites[pres[-1]][1]
    corpo = '\n\n'.join(t[limites[n][0]:limites[n][1]].strip() for n in pres)
    if h == 10:
        pas = 'Sl 10 (hebr.) = Sl 9,22–39 (LXX), bloco «Ἵνα τί, Κύριε, ἀφέστηκας»; o Sl 9 e o Sl 10 do hebraico são um só (Sl 9) na LXX'
    elif h == 9:
        pas = 'Sl 9 (hebr.) = Sl 9,1–21 (LXX); o Sl 9 e o Sl 10 do hebraico são um só (Sl 9) na LXX'
    else:
        pas = _grc.nota_numeracao(h)
        if len(pres) < len(ls):
            pas += f' (neste texto só o Sl {" e ".join(str(x) for x in pres)} da LXX)'
    extra = None
    if any(n in achados for n in pres):
        extra = ('Nota: o cabeçalho deste salmo faltava ou estava estragado no PDF; o começo foi achado pelo primeiro '
                 'versículo citado e pode incluir ou perder uma frase do título.')
    _grc.gravar_base(h, 'atanasio-expositiones-in-psalmos', 'Santo Atanásio, Expositiones in Psalmos',
                     'Santo Atanásio de Alexandria (c. 296–373)', 'Expositiones in Psalmos (Ἑρμηνεία εἰς τοὺς Ψαλμούς)',
                     pas, _grc.titulo_edicao(t, a, b), URL, COBRE, 'sim', 'grc', SCRIPT, corpo, extra)
    gravados[h] = (a, b)
    tam += len(corpo)
_grc.registrar(SCRIPT, 'ausentes', ausentes)
print(f'{SCRIPT}: {len(gravados)} arquivos, {tam // 1024} KB; ausentes {len(ausentes)}: {sorted(ausentes)}')
for h in (1, 15, 23, 50, 90, 10, 118, 135, 145):
    if h in gravados:
        a, b = gravados[h]
        print(f'--- Sl {h} ({b - a} car.)\n  INI: {t[a:a + 100]!r}\n  FIM: {t[b - 100:b]!r}')
