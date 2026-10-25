"""São Basílio Magno no Gênesis: Homiliae in Hexaemeron (9 homilias, só Gn 1) e as duas homilias atribuídas
Sobre a origem do homem (De hominis structura / De creatione hominis, Gn 1,26–28; a 2ª passa a Gn 2,7).

    python3 -I pesquisa/ferramentas/base/gen-gregos-basilio.py [capítulos]      (padrão: 1; ex.: 1-3)

Fontes (baixadas UMA vez para pesquisa/cache/genesis/gregos/, fora do git; o PDF é apagado depois da conversão):
  - Hexaémeron: khazarzar (Ψηφιακή Πατρολογία), «Basilius Caesariensis_PG 29-32/Homiliae in hexaemeron.pdf». O PDF segue a
    ed. Giet (SC 26, 1949, que reimprime o texto de Garnier/PG com poucas mudanças): os marcadores «2.6» são homilia e
    parágrafo, não colunas. As colunas da PG 29 (4–208) saem do OCR do archive.org «patrologicursus22migngoog»: os números
    dos cabeçalhos de página, interpolados pela linha onde cada parágrafo começa (aproximação de ±1 coluna).
  - Sobre a origem do homem I e II: khazarzar, «Gregory of Nyssa_PG 44-46/De creatione hominis sermo primus.pdf» e
    «… sermo alter.pdf» (texto da ed. Hörner, GNO Suppl., 1972; os números soltos no texto são páginas dessa edição).
    Na PG: 44, 257–298 (entre as obras de Nissa) e 30, 9–61 (entre as de Basílio). Autoria discutida (Basílio, Nissa ou
    outro capadócio); a SC 160 (Smets–van Esbroeck, 1970) as dá a Basílio.

Gn 1 recebe tudo; os outros capítulos só entram nas listas de ausentes/pistas (o Hexaémeron para no v. 26; a homilia II
comenta Gn 2,7 e o paraíso: pista para Gn 2).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
URL_HEX = G.khz('Basilius Caesariensis_PG 29-32', 'Homiliae in hexaemeron.pdf')
URL_S1 = G.khz('Gregory of Nyssa_PG 44-46', 'De creatione hominis sermo primus.pdf')
URL_S2 = G.khz('Gregory of Nyssa_PG 44-46', 'De creatione hominis sermo alter.pdf')
OCR29 = 'https://archive.org/download/patrologicursus22migngoog/patrologicursus22migngoog_djvu.txt'

# o que cada homilia comenta (Gn 1, numeração da LXX = Vulgata = hebraica neste capítulo)
HOMILIAS = {1: 'Gn 1,1', 2: 'Gn 1,2–5', 3: 'Gn 1,6–8 (o firmamento)', 4: 'Gn 1,9–10 (o ajuntamento das águas)',
            5: 'Gn 1,11–13 (a vegetação)', 6: 'Gn 1,14–19 (os luzeiros)', 7: 'Gn 1,20–23 (os seres das águas)',
            8: 'Gn 1,24 e 1,20–23 (os animais da terra; as aves)', 9: 'Gn 1,24–26 (os animais da terra; «Façamos o homem»)'}


def secoes_hex(t):
    """Posições dos parágrafos «h.s» do PDF (em ordem: 1.1, 1.2, …, 9.6)."""
    pos, esp_h, esp_s = [], 1, 1
    for m in re.finditer(r'(?<![\d.])(\d)\.(\d{1,2})(?=\s)', t):
        h, s = int(m.group(1)), int(m.group(2))
        if (h, s) == (esp_h, esp_s) or (h == esp_h + 1 and s == 1):
            pos.append((h, s, m.start(), m.end()))
            esp_h, esp_s = h, s + 1
    return pos


def _esqueleto(s):
    """Letras gregas sem acento, com as trocas comuns do OCR igualadas (κ/χ, β/δ, ο/ω, ε/η, ι/υ…)."""
    s = G.sem_acento(s)
    s = s.translate(str.maketrans('χδωηυφθ', 'κβοειπτ'))
    return re.sub(r'[^α-ω]', '', s)


def _parecido(a, b):
    import difflib
    return difflib.SequenceMatcher(None, a, b).ratio()


def colunas_pg29(inicios):
    """{(h, s): coluna aproximada da PG 29}. inicios: {(h, s): primeiras palavras do parágrafo no PDF}.
    No OCR do archive.org, acha o começo de cada parágrafo («N. <grego>») pelo parecido das primeiras letras, em ordem, e
    interpola a coluna pelos números dos cabeçalhos de página que formam uma sequência crescente plausível."""
    p = G.baixar(OCR29, 'ia/pg029.txt', minimo=100000)
    L = G.ler(p).split('\n')
    a = next(i for i in range(50000, 56000) if re.match(r'^\s*IN HEXAEMERON\.\s*$', L[i]))
    fim = next(i for i in range(a, a + 25000) if 'Γραφὴ θεόπνευστος' in L[i])
    brutos = []
    for i in range(a, fim):
        if re.search(r'S\. BASILII MAGNI|HOMILIA [IVXl1]+ IN HEX', L[i]):
            ns = [int(x) for x in re.findall(r'\b(\d{1,3})\b', L[i]) if 4 <= int(x) <= 210]
            if ns:
                brutos.append((i, max(ns)))
    lin = lambda i: 4 + (i - a) / (fim - a) * (208 - 4)
    brutos = [(i, n) for i, n in brutos if abs(n - lin(i)) <= 20]
    # maior subsequência crescente (os números mal lidos saem)
    melhor = []
    for k, (i, n) in enumerate(brutos):
        cand = [m for m in melhor if m[-1][1] < n]
        nova = (max(cand, key=len) if cand else []) + [(i, n)]
        melhor.append(nova)
    anc = [(a, 4)] + (max(melhor, key=len) if melhor else []) + [(fim, 208)]

    def interp(i):
        for (i0, c0), (i1, c1) in zip(anc, anc[1:]):
            if i0 <= i <= i1:
                return round(c0 + (c1 - c0) * (i - i0) / max(1, i1 - i0))
        return None
    cands = []
    for i in range(a, fim):
        m = re.match(r'^\s*(\d{1,2})\.\s+(.*)$', L[i])
        if m and re.search(r'[\u0370-\u03ff\u1f00-\u1fff]', m.group(2)[:6]):
            cands.append((i, _esqueleto(m.group(2) + ' ' + (L[i + 1] if i + 1 < len(L) else ''))[:28]))
    chaves = sorted(inicios)
    escolha = {}
    for chave in chaves:
        alvo = _esqueleto(inicios[chave][1])[:28]
        best = max(((_parecido(alvo, c[1]), k) for k, c in enumerate(cands)), default=None)
        if best and best[0] >= 0.6:
            escolha[chave] = best[1]
    # maior subsequência crescente dos índices, na ordem dos parágrafos (casamentos fora de ordem saem)
    seq = [(ch, escolha[ch]) for ch in chaves if ch in escolha]
    cadeias = []
    for ch, k in seq:
        ant = [c for c in cadeias if c[-1][1] < k]
        cadeias.append((max(ant, key=len) if ant else []) + [(ch, k)])
    fixos = {ch: cands[k][0] for ch, k in (max(cadeias, key=len) if cadeias else [])}
    # os que faltam: linha interpolada pela posição do parágrafo no PDF, entre os vizinhos achados
    pts = sorted((inicios[ch][0], ln) for ch, ln in fixos.items())
    out = {}
    for ch in chaves:
        if ch in fixos:
            ln = fixos[ch]
        else:
            x = inicios[ch][0]
            ante = [q for q in pts if q[0] <= x]
            depo = [q for q in pts if q[0] > x]
            if not ante or not depo:
                continue
            (x0, l0), (x1, l1) = ante[-1], depo[0]
            ln = l0 + (l1 - l0) * (x - x0) / max(1, x1 - x0)
        out[ch] = interp(int(ln))
    return out


def hexaemeron():
    t = G.texto_pdf(URL_HEX, 'basilio-hexaemeron', colunas_pg=False)
    pos = secoes_hex(t)
    assert len(pos) > 60, len(pos)
    inicios = {(h, s): (a, t[b:b + 80]) for (h, s, a, b) in pos}
    cols = colunas_pg29(inicios)
    partes, ult_h = [], 0
    for k, (h, s, a, b) in enumerate(pos):
        fim = pos[k + 1][2] if k + 1 < len(pos) else len(t)
        corpo = t[b:fim].strip()
        if h != ult_h:
            partes.append(f'## Homilia {h} ({HOMILIAS[h]})')
            ult_h = h
        c = cols.get((h, s))
        partes.append(f'**[{h}, {s}' + (f' · PG 29, c. {c}' if c else '') + ']** ' + corpo)
    # o título de cada homilia (ΟΜΙΛΙΑ …) fica colado ao fim do parágrafo anterior: tira-se
    corpo = '\n\n'.join(re.sub(r'\s*ΟΜΙΛΙΑ [α-ωϛw]{1,2}ʹ\.?\s*(Περὶ [^.]*\.?)?\s*$', '', p) for p in partes)
    ult = max(c for c in cols.values() if c)
    campos = {
        'Autor': 'São Basílio Magno (c. 330–379)',
        'Obra': 'Homiliae in Hexaemeron (Homilias sobre os seis dias)',
        'Passagem': 'Gn 1,1–26: homilias 1–9 inteiras (a 9 para em «Façamos o homem»)',
        'Edição': f'PG 29, 4–208 (as colunas de cada parágrafo, aproximadas, vêm entre colchetes); texto da ed. Giet, SC 26 (1949)',
        'Fonte': URL_HEX,
        'Cobre': 'o capítulo inteiro até o v. 26 (o v. 26–31 só no começo; ver as homilias Sobre a origem do homem)',
        'Oriental': 'sim',
        'Língua': 'grc',
    }
    nota = ('Marcadores: **[homilia, parágrafo · PG 29, c. N]**; a coluna é estimada pelos cabeçalhos do OCR da PG 29 '
            '(archive.org, patrologicursus22migngoog) e pode errar por uma. A divisão em parágrafos é a de Garnier, que a PG e a '
            'SC 26 seguem. As palavras partidas na quebra de linha do PDF foram coladas por heurística: conferir na leitura.')
    G.gravar(1, 'basilio-hexaemeron', 'São Basílio Magno, Homiliae in Hexaemeron', campos, corpo, nota, SCRIPT)
    print(f'  Hexaémeron: {len(pos)} parágrafos; colunas achadas para {len(cols)} (última {ult})')


def sermoes():
    partes = []
    for n, url, nome, pg in ((1, URL_S1, 'basilio-origem-homem-1', 'PG 44, 257–277'),
                             (2, URL_S2, 'basilio-origem-homem-2', 'PG 44, 277–298')):
        t = G.texto_pdf(url, nome, colunas_pg=False)
        t = re.sub(r'^\S.*?(?=ΟΜΙΛΙΑ)', '', t, count=1)
        partes.append(f'## Homilia {"I" if n == 1 else "II"} ({pg})\n\n' + t.strip())
    campos = {
        'Autor': 'São Basílio Magno (c. 330–379), atribuído (também dado a São Gregório de Nissa)',
        'Obra': 'Sobre a origem do homem, homilias I e II (De hominis structura; In verba «Faciamus hominem»)',
        'Passagem': 'Gn 1,26–28 (a homilia II passa a Gn 2,7 e ao paraíso)',
        'Edição': 'PG 44, 257–298 (entre as obras de Nissa) e PG 30, 9–61 (entre as de Basílio); texto da ed. Hörner, GNO Suppl. (1972)',
        'Fonte': URL_S1 + ' ; ' + URL_S2,
        'Cobre': 'vv. 26–28 (imagem e semelhança, homem e mulher, «crescei e multiplicai-vos», o domínio)',
        'Oriental': 'sim',
        'Língua': 'grc',
    }
    nota = ('Os números soltos no texto são páginas da ed. Hörner (GNO Suppl.). A PG lê em I (PG 44, 273–276) '
            '«καθ\' ὁμοίωσιν δὲ γίνομαι ἐν τῷ Χριστιανὸς γενέσθαι», onde Hörner tem «χρηστὸς». Edição moderna: '
            'para citar, conferir com a PG (OCR em archive.org/details/patrologiaecursu44mignuoft).')
    G.gravar(1, 'basilio-origem-homem', 'São Basílio Magno (atribuído), Sobre a origem do homem I–II', campos,
             '\n\n'.join(partes), nota, SCRIPT)


def main():
    caps = G.capitulos()
    for cap in caps:
        if cap == 1:
            hexaemeron()
            sermoes()
        else:
            G.ausente(cap, 'São Basílio, Homiliae in Hexaemeron: só comenta Gn 1 (para em 1,26).')
            if cap == 2:
                G.pista(cap, 'São Basílio (atribuído), Sobre a origem do homem II (PG 44, 277–298; GNO Suppl.): Gn 2,7 '
                             '(«o pó da terra»), o paraíso; já em genesis/001/base/basilio-origem-homem.md, homilia II. '
                             + URL_S2)
            else:
                G.ausente(cap, 'São Basílio (atribuído), Sobre a origem do homem I–II: só Gn 1,26–28 e 2,7.')
    G.registrar()


if __name__ == '__main__':
    main()
