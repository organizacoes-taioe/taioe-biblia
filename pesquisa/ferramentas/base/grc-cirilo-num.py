"""São Cirilo de Alexandria sobre Números, por capítulo: Glaphyra in Pentateuchum (in Numeros), Fragmenta duo in Numeros e
De adoratione et cultu in spiritu et veritate (os trechos que citam Números).

    python -I -X utf8 pesquisa/ferramentas/base/grc-cirilo-num.py

Baixa UMA vez, da «Ψηφιακή Πατρολογία» (khazarzar, https://khazarzar.skeptik.net/pgm/PG_Migne/Cyril%20of%20Alexandria_PG%2068-77/):
Glaphyra in Pentateuchum.pdf, Fragmenta duo in Numeros.pdf e De adoratione et cultu in spiritu et veritate.pdf (cache:
pesquisa/cache/base/numeros/cirilo-*.pdf) e grava, em numeros/<ccc>/base/: cirilo-glaphyra-in-numeros.md, cirilo-fragmenta-in-numeros.md
e cirilo-de-adoratione-numeros.md.

- Glaphyra (PG 69, 589-641; o texto de Números vai das linhas 10363 a 11292 do texto extraído): cinco seções, «Περὶ Χριστοῦ καὶ τῆς
  Ἰουδαίων Συναγωγῆς» (Nm 12), «Περὶ τῶν κατασκεψαμένων τὴν γῆν» (Nm 13-14), «Ὅτι γέγονεν ἡμῖν ἄρτος ζωῆς ὁ Χριστός» (Nm 15,17-29 com Lv 23),
  «Περὶ τῆς δαμάλεως τῆς πυῤῥᾶς» (Nm 19) e «Περὶ τοῦ ὄφεως τοῦ χαλκοῦ» (Nm 21,6-9). Só as duas últimas caem nos capítulos pedidos.
- Fragmenta duo in Numeros: dois fragmentos curtos de cadeia (Nm 18,26 e Nm 20,8).
- De adoratione (PG 68, 133-1125; diálogo com Paládio, 17 livros): a obra cita Números em dezenas de lugares. O script divide o
  texto nas falas do diálogo ({ΚΥΡ.} e {ΠΑΛΛ.}) e, para cada fala, conta os grupos de 4 palavras (sem acento) que também estão na LXX de
  Números (Rahlfs 1935, github.com/eliranwong/LXX-Rahlfs-1935) em cada capítulo. A fala vai ao capítulo com 8 ou mais grupos em comum
  (ou 5 ou mais, se a fala diz «ἐν τοῖς Ἀριθμοῖς»). Alusões sem citação ficam de fora: a pesquisa do capítulo deve completar.
Os PDFs seguem a PG (colunas «69.592» viram «[PG 69, 592]»).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

PASTA = 'Cyril of Alexandria_PG 68-77'
U_GLA = C.khazarzar_url(PASTA, 'Glaphyra in Pentateuchum.pdf')
U_FRA = C.khazarzar_url(PASTA, 'Fragmenta duo in Numeros.pdf')
U_ADO = C.khazarzar_url(PASTA, 'De adoratione et cultu in spiritu et veritate.pdf')
C.baixar(U_GLA, 'cirilo-glaphyra.pdf', minimo=1000)
C.baixar(U_FRA, 'cirilo-fragmenta-num.pdf', minimo=1000)
C.baixar(U_ADO, 'cirilo-deadoratione.pdf', minimo=1000)

PGM = re.compile(r'\b(6[89])\.(\d{3,4})\b')


def marcar(t):
    return PGM.sub(lambda m: f'[PG {m.group(1)}, {m.group(2)}]', t)


def col_ini(linhas, i, vol):
    """Última coluna «vol.NNN» vista até a linha i (inclusive)."""
    for j in range(i, -1, -1):
        m = re.findall(r'\b%d\.(\d{3,4})\b' % vol, linhas[j])
        if m:
            return int(m[-1])
    return None


def cols(texto, vol):
    return [int(x) for x in re.findall(r'\[PG %d, (\d+)\]' % vol, texto)]


def edicao(texto, vol, c0):
    cs = cols(texto, vol)
    if c0:
        cs.append(c0)
    return f'PG {vol}, {min(cs)}–{max(cs)}' if cs else f'PG {vol}'


# ------------------------------------------------------------------------- Glaphyra
G = C.pdf_linhas('cirilo-glaphyra.pdf')
g_ini = next(i for i, l in enumerate(G) if 'ΓΛΑΦΥΡΩΝ ΕΙΣ ΤΟΥΣ ΑΡΙΘΜΟΥΣ' in C.sem_acento(l).upper())
g_fim = None
for i in range(g_ini, len(G)):
    if 'ΕΙΣ ΤΟ ΔΕΥΤΕΡΟΝΟΜΙΟΝ' in C.sem_acento(G[i]).upper():
        g_fim = i - 2  # as duas linhas anteriores são o cabeçalho «ΤΟΥ ΕΝ ΑΓΙΟΙΣ ΠΑΤΡΟΣ ΗΜΩΝ ΚΥΡΙΛΛΟΥ…»
        break
assert g_fim
secoes = {  # NV -> (rótulo, procura do começo, procura do fim)
    19: ('Περὶ τῆς δαμάλεως τῆς πυῤῥᾶς (Nm 19)', 'Περὶ τῆς δαμάλεως τῆς πυ', 'Περὶ τοῦ ὄφεως τοῦ'),
    21: ('Περὶ τοῦ ὄφεως τοῦ χαλκοῦ (Nm 21,6-9)', 'Περὶ τοῦ ὄφεως τοῦ', None),
}
n_arq = 0
for cap, (rot, a_s, b_s) in secoes.items():
    a = next(i for i in range(g_ini, g_fim + 1) if a_s in G[i])
    b = next((i for i in range(a + 1, g_fim + 1) if b_s and b_s in G[i]), g_fim + 1) if b_s else g_fim + 1
    # a linha de começo traz o fim da seção anterior («… Ἀμήν. Περὶ τῆς δαμάλεως…»): corta a partir do título
    seg = list(G[a:b])
    seg[0] = seg[0][seg[0].index(a_s):]
    if b_s and b < len(G) and b_s in G[b]:
        pass
    # o fim: a linha b (se existir) traz o título da próxima seção no meio: inclui só até o título
    if b_s and b <= g_fim:
        fim_linha = G[b][:G[b].index(b_s)]
        seg.append(fim_linha)
    texto = marcar('\n'.join(seg))
    campos = {
        'Autor': 'São Cirilo de Alexandria (c. 376–444)',
        'Obra': 'Glaphyra in Pentateuchum (Glaphyra in Numeros)',
        'Passagem': f'{C.cap_nm(cap)}; seção «{rot}»',
        'Edição': edicao(texto, 69, col_ini(G, a, 69)),
        'Fonte': U_GLA,
        'Cobre': 'a seção inteira dos Glaphyra sobre este capítulo',
        'Oriental': 'sim',
        'Língua': 'grc',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/grc-cirilo-num.py',
    }
    nota = ('Os Glaphyra («Comentários elegantes») leem Moisés como figura de Cristo; em Números tratam só de cinco episódios (Nm 12; 13–14; 15,17–29; 19; 21,6–9). '
            'Texto da PG 69 (khazarzar), com as colunas «[PG 69, N]»; os números «αʹ.», «βʹ.» são as subdivisões da seção.')
    C.gravar(cap, 'cirilo-glaphyra-in-numeros', 'São Cirilo de Alexandria, Glaphyra in Numeros', campos, texto, nota)
    n_arq += 1
    print(f'Glaphyra Nm {cap}: {len(texto)//1024} KB {campos["Edição"]}')

# ------------------------------------------------------------------------- Fragmenta duo
F = C.pdf_linhas('cirilo-fragmenta-num.pdf')
frs = {18: (1, 5), 20: (5, len(F))}  # linhas: o 1.º fragmento vai até «…ἀλλ' ἐν τῇ ἐσωτέρᾳ καὶ κεκρυμμένῃ.»
i2 = next(i for i, l in enumerate(F) if 'Λαβὲ τὴν ῥάβδον καὶ ἐκκλησίασον' in l)
frs = {18: (F[1:i2 + 0], F[i2][:F[i2].index('Λαβὲ τὴν ῥάβδον καὶ ἐκκλησίασον')]), 20: (F[i2:], '')}
for cap, (linhas, resto) in frs.items():
    if cap == 18:
        corpo = '\n'.join(linhas) + ('\n' + resto if resto.strip() else '')
        rot = 'primeiro fragmento (Nm 18,26: «Ἀφελεῖτε ὑμεῖς ἀπ’ αὐτοῦ ἀφαίρεμα», o dízimo do dízimo)'
    else:
        corpo = '\n'.join(linhas)
        corpo = corpo[corpo.index('Λαβὲ τὴν ῥάβδον καὶ ἐκκλησίασον'):]
        rot = 'segundo fragmento (Nm 20,8: «Λαβὲ τὴν ῥάβδον καὶ ἐκκλησίασον τὴν συναγωγήν», a pedra que é Cristo)'
    campos = {
        'Autor': 'São Cirilo de Alexandria (c. 376–444)',
        'Obra': 'Fragmenta duo in Numeros',
        'Passagem': f'{C.cap_nm(cap)}; {rot}',
        'Edição': 'fragmentos de cadeia (ed. Mai; coluna não indicada no PDF)',
        'Fonte': U_FRA,
        'Cobre': 'só um fragmento curto (quatro a cinco linhas)',
        'Oriental': 'sim',
        'Língua': 'grc',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/grc-cirilo-num.py',
    }
    nota = ('Os dois fragmentos do PDF estão colados num só texto; este arquivo traz o que pertence a este capítulo. '
            'A divisão entre os dois é a do script (o segundo começa em «Λαβὲ τὴν ῥάβδον καὶ ἐκκλησίασον»).')
    C.gravar(cap, 'cirilo-fragmenta-in-numeros', 'São Cirilo de Alexandria, Fragmenta duo in Numeros', campos, corpo, nota)
    n_arq += 1
    print(f'Fragmenta Nm {cap}: {len(corpo)} bytes')

# ------------------------------------------------------------------------- De adoratione
A = C.pdf_linhas('cirilo-deadoratione.pdf')
# juntamos as linhas mantendo as quebras (para a leitura) e dividimos nas falas do diálogo
texto = '\n'.join(A)
cortes = [m.start() for m in re.finditer(r'\{(?:ΚΥΡ|ΠΑΛΛ)\.\}', texto)]
cortes = [0] + cortes + [len(texto)]
unidades = []
for a, b in zip(cortes, cortes[1:]):
    u = texto[a:b]
    if len(u) < 200:
        continue
    unidades.append((a, u))

# coluna da PG vigente no começo de cada unidade
marcas_pg = [(m.start(), int(m.group(2))) for m in re.finditer(r'\b(68)\.(\d{3,4})\b', texto)]
import bisect
pos_pg = [p for p, c in marcas_pg]


def col_em(p):
    k = bisect.bisect_right(pos_pg, p) - 1
    return marcas_pg[k][1] if k >= 0 else None


por = {c: [] for c in C.CAPS}
# palavras que, sozinhas, identificam o episódio (sem acento, minúsculas): ajudam quando Cirilo só alude ou parafraseia
CHAVES = {5: ['ζηλοτυπι'], 6: ['ναζιραι'], 17: ['ραβδοσ του αρων', 'ραβδον του αρων', 'βλαστησασα ραβδ'],
          19: ['δαμαλ'], 20: ['υδωρ αντιλογιασ', 'υδατοσ αντιλογιασ'], 21: ['χαλκουν οφιν', 'οφιν τον χαλκον', 'οφεωσ του χαλκ', 'χαλκου οφεωσ'],
          22: ['βαλααμ', 'βαλακ'], 23: ['βαλααμ'], 24: ['βαλααμ'], 25: ['φινεε', 'βεελφεγωρ'], 27: ['θυγατερεσ σαλπααδ', 'θυγατερων σαλπααδ'],
          31: ['μαδιανιτ'], 35: ['φυγαδ', 'πολεισ καταφυγ', 'πολεων καταφυγ']}
for a, u in unidades:
    sc = C.pontuar(u)
    cita = 'Ἀριθμοῖς' in u.replace('\n', ' ')
    sa = C.sem_acento(u).lower().replace('ς', 'σ')
    for cap, n in sc.items():
        if cap in por and (n >= 8 or (cita and n >= 5)):
            por[cap].append((a, u, n))
    for cap, chs in CHAVES.items():
        if any(c in sa for c in chs) and not any(x[0] == a for x in por[cap]):
            por[cap].append((a, u, 0))
    for cap in por:
        por[cap].sort(key=lambda x: x[0])

for cap in C.CAPS:
    if not por[cap]:
        continue
    partes = por[cap]
    corpo = '\n\n'.join(f'**[De adoratione, PG 68, {col_em(a)}; {(str(n) + ' grupos de 4 palavras em comum com a LXX de Nm ' + str(cap)) if n else 'palavra-chave do episódio, sem citação longa'}]**\n\n' + marcar(u.strip())
                        for a, u, n in partes)
    cs = [col_em(a) for a, u, n in partes] + cols(corpo, 68)
    campos = {
        'Autor': 'São Cirilo de Alexandria (c. 376–444)',
        'Obra': 'De adoratione et cultu in spiritu et veritate (os trechos que citam Números)',
        'Passagem': f'{C.cap_nm(cap)}; {len(partes)} fala(s) do diálogo com Paládio, PG 68, ' + ', '.join(str(x) for x in sorted(set(col_em(a) for a, u, n in partes))),
        'Edição': f'PG 68, {min(cs)}–{max(cs)} (a obra: PG 68, 133–1125)',
        'Fonte': U_ADO,
        'Cobre': 'só as falas que citam este capítulo (ver Nota); não é a obra inteira nem as alusões sem citação',
        'Oriental': 'sim',
        'Língua': 'grc',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/grc-cirilo-num.py',
    }
    nota = ('Seleção automática: o script divide o diálogo nas falas ({ΚΥΡ.} Cirilo, {ΠΑΛΛ.} Paládio) e mantém as falas com 8 ou mais grupos de '
            '4 palavras (sem acento) em comum com a LXX deste capítulo (5 ou mais se dizem «ἐν τοῖς Ἀριθμοῖς»). O rótulo de cada trecho diz a coluna da PG '
            'e o número de grupos. Citações muito curtas, alusões e comentários sem citação não aparecem: conferir a obra no PDF. '
            'Texto da PG 68 (khazarzar), colunas «[PG 68, N]».')
    C.gravar(cap, 'cirilo-de-adoratione-numeros', 'São Cirilo de Alexandria, De adoratione (trechos sobre Números)', campos, corpo, nota)
    n_arq += 1
    print(f'De adoratione Nm {cap:2d}: {len(partes)} falas, {len(corpo)//1024} KB  colunas {sorted(set(col_em(a) for a,u,n in partes))}')
print(n_arq, 'arquivos')
C.finalizar()
