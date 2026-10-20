"""Orígenes, escólios gregos de cadeia sobre Números (Adnotationes in Numeros, PG 17, 21; Selecta in Numeros, PG 12, 576-584), por capítulo.

    python -I -X utf8 pesquisa/ferramentas/base/grc-origenes-num.py

Baixa UMA vez, da «Ψηφιακή Πατρολογία» (khazarzar, https://khazarzar.skeptik.net/pgm/PG_Migne/Origenes_PG%2011-17/):
Adnotationes in Numeros.pdf e Selecta in Numeros.pdf, e grava numeros/<ccc>/base/origenes-escolios-gregos-numeros.md.

- Adnotationes: quatro a seis notas curtas, cada uma com o título «ΚΕΦ. ΚΒʹ. Στίχ. βʹ.» (capítulo e versículo da LXX): o capítulo vem do título.
- Selecta: glosas de cadeia (Procópio, Nicéforo), sem título de capítulo; o script corta o texto em unidades de ~350 caracteres e atribui cada uma
  a um capítulo por palavras-chave gregas, em ordem (programação dinâmica): aproximado.
A atribuição a Orígenes dessas glosas é incerta (cadeia); no site, tratar como «escólio atribuído a Orígenes».
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

PASTA = 'Origenes_PG 11-17'
U_ADN = C.khazarzar_url(PASTA, 'Adnotationes in Numeros.pdf')
U_SEL = C.khazarzar_url(PASTA, 'Selecta in Numeros.pdf')
C.baixar(U_ADN, 'origenes-adnotationes-num.pdf', minimo=1000)
C.baixar(U_SEL, 'origenes-selecta-num.pdf', minimo=1000)

GN = {'ΙΑ': 11, 'ΙΒ': 12, 'ΙΓ': 13, 'ΙΔ': 14, 'ΙΕ': 15, 'ΙϚ': 16, 'ΙΖ': 17, 'ΙΗ': 18, 'ΙΘ': 19, 'Κ': 20, 'ΚΑ': 21, 'ΚΒ': 22, 'ΚΓ': 23, 'ΚΔ': 24,
      'ΚΕ': 25, 'ΚϚ': 26, 'ΚΖ': 27, 'ΚΗ': 28, 'ΚΘ': 29, 'Λ': 30, 'ΛΑ': 31, 'ΛΒ': 32, 'ΛΓ': 33, 'ΛΔ': 34, 'ΛΕ': 35, 'ΛϚ': 36}
partes_por_cap = {c: [] for c in C.CAPS}

# --- Adnotationes
A = C.pdf_linhas('origenes-adnotationes-num.pdf')
ta = ' '.join(A[2:])
ta = re.sub(r'\b17\.(\d+)\b', r'[PG 17, \1]', ta)
marcas = [(m.start(), m.group(1)) for m in re.finditer(r'ΚΕΦ\.\s+([Α-ΩϚ]+)ʹ\.', ta)]
for k, (p, num) in enumerate(marcas):
    fim = marcas[k + 1][0] if k + 1 < len(marcas) else len(ta)
    cap = GN.get(num)
    if cap in partes_por_cap:
        partes_por_cap[cap].append(('Adnotationes (PG 17, 21)', ta[p:fim].strip()))

# --- Selecta
S = C.pdf_linhas('origenes-selecta-num.pdf')
ts = ' '.join(S[3:])
ts = re.sub(r'\b12\.(\d{3})\b', r'[PG 12, \1]', ts)
unid, buf = [], ''
for fr in re.split(r'(?<=[.;·]) ', ts):
    buf += fr + ' '
    if len(buf) >= 350:
        unid.append(buf.strip())
        buf = ''
if buf.strip():
    unid.append(buf.strip())
KWG = {
    11: ['μαννα', 'ορτυγ', 'κοριο', 'προφητευ', 'εβδομηκοντα', 'επιθυμ'], 12: ['μαριαμ', 'αιθιοπ', 'λεπρ'],
    13: ['κατασκοπ', 'αυση', 'χαλεβ', 'γιγαντ', 'βοτρυ', 'αποστειλον'], 14: ['χαλεβ', 'εικοσαετ', 'μετεμελ', 'παιδι'],
    15: ['ξυλα', 'σαββατ', 'κρασπεδ'], 16: ['κορε', 'δαθαν', 'αβειρων'], 17: ['ραβδ', 'θυμιαμα', 'πυρεια', 'θυμιατηρ'],
    18: ['λευι', 'κληρον', 'δεκατ', 'απαρχ'], 19: ['δαμαλ', 'πυρρ', 'σποδ'], 20: ['πετρα', 'μεριβα', 'αντιλογ', 'εδωμ'],
    21: ['οφεισ', 'οφεωσ', 'χαλκ', 'σηων', 'ωγ'], 22: ['βαλααμ', 'βαλακ', 'ονοσ', 'μαντι', 'μαγει', 'αγγελον'], 23: ['βαλααμ', 'παραβολ', 'ευλογ'],
    24: ['βαλααμ', 'αστρον', 'αμαληκ', 'κιναι', 'κυριευσ'], 25: ['βεελφεγωρ', 'φινεεσ', 'πορνε'], 26: ['απαριθμ', 'κληρω'],
    27: ['σαλπααδ', 'χειρασ', 'ιησουν'], 28: ['θυσι', 'ολοκαυτ', 'νεομην'], 29: ['σαλπιγγ', 'εορτ'], 30: ['ευχη', 'ορκ'],
    31: ['μαδιαν', 'λαφυρ'], 32: ['ρουβην', 'γαδ', 'μανασση'], 33: ['σταθμ', 'μανσι'], 34: ['οριο', 'γη χαναναν'], 35: ['φυγαδ', 'πολεισ'],
    36: ['κληρονομ', 'θυγατερ'],
}
cap_de = C.atribuir_dp(unid, kw=KWG, primeiro=11)
for t, cap in zip(unid, cap_de):
    if cap in partes_por_cap:
        partes_por_cap[cap].append(('Selecta (PG 12, 576–584; atribuição de capítulo aproximada)', t))
    if cap == 22:  # a Selecta comenta a história de Balaão (Nm 22–24) de uma vez: as glosas valem para os três capítulos
        for outro in (23, 24):
            partes_por_cap[outro].append(('Selecta (PG 12, 576–584; glosa sobre Balaão, Nm 22–24)', t))

n_arq = 0
for cap in C.CAPS:
    ps = partes_por_cap[cap]
    if not ps:
        continue
    corpo = '\n\n'.join(f'**[Orígenes (cadeia), {r}]**\n\n{t}' for r, t in ps)
    campos = {
        'Autor': 'Orígenes (c. 185–c. 253), escólios de cadeia',
        'Obra': 'Adnotationes in Numeros e Selecta in Numeros',
        'Passagem': f'{C.cap_nm(cap)}; ' + ', '.join(sorted(set(r.split(' (')[0] for r, t in ps))),
        'Edição': 'PG 17, 21 (Adnotationes); PG 12, 576–584 (Selecta)',
        'Fonte': U_SEL if any(r.startswith('Selecta') for r, t in ps) and not any(r.startswith('Adnot') for r, t in ps) else U_ADN,
        'Cobre': 'só as notas e glosas que a cadeia grega liga a este capítulo (poucas linhas)',
        'Oriental': 'sim',
        'Língua': 'grc',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/grc-origenes-num.py',
    }
    nota = ('Escólios gregos de cadeia atribuídos a Orígenes (Procópio, Nicéforo): atribuição incerta, não são as homilias (essas só existem no latim de Rufino: ver '
            'origenes-homilias-in-numeros.md). Adnotationes: ' + U_ADN + ' ; Selecta: ' + U_SEL + '. Os capítulos das Adnotationes vêm do título («ΚΕΦ. ΚΒʹ.» = 22); os da '
            'Selecta são atribuídos por palavras-chave, em ordem. Texto da PG (khazarzar), colunas «[PG n, N]».')
    C.gravar(cap, 'origenes-escolios-gregos-numeros', 'Orígenes, escólios gregos sobre Números (Adnotationes e Selecta)', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {[r.split(" (")[0] for r, t in ps]}  {len(corpo)} bytes')
print(n_arq, 'arquivos')
C.finalizar()
