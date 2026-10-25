"""Orígenes no Gênesis, por capítulo: Homiliae in Genesim (latim de Rufino), fragmentos gregos dos Commentarii, Selecta e
Adnotationes (escólios de cadeia).

    python3 -I pesquisa/ferramentas/base/gen-gregos-origenes.py [capítulos]      (padrão: 1; ex.: 1-50)

Fontes (baixadas UMA vez para pesquisa/cache/genesis/gregos/; PDFs apagados depois da conversão):
  - Homiliae in Genesim 1–16, latim de Rufino: OCR do archive.org «origenes-werke.-bd-6-1920» (GCS 29, ed. Baehrens, 1920).
    O OCR lê mal os títulos das homilias: o script corta só a Homilia 1 (Gn 1), de «HOMILIA PRIMA» ao título seguinte;
    para as outras, deixa uma pista com o capítulo (tabela HOMILIAS: 2 = a arca, Gn 6; 3 = a circuncisão, Gn 17; 4 = Mambré,
    Gn 18; 5 = Ló, Gn 19; 6 = Abimelec, Gn 20; 7 = Isaac e Ismael, Gn 21; 8–9 = o sacrifício de Isaac, Gn 22; 10 = Rebeca,
    Gn 24; 11 = Cetura, Gn 25; 12 = Gn 25–26; 13–14 = os poços, Gn 26; 15 = José, Gn 45–46; 16 = o Egito, Gn 47).
    Na PG: 12, 145–262 (Delarue).
  - Commentarii in Genesim (fragmentos gregos dos tomos I e III, PG 12, 45–92, todos sobre Gn 1: o Pai eterno, a criação sem
    matéria eterna, e o longo fragmento da Filocalia 23 sobre Gn 1,14, contra a astrologia; o último, sobre a missão dos
    apóstolos, vem de Eusébio, HE III, 1) e Selecta in Genesim (PG 12, 92–145): khazarzar «Origenes_PG 11-17/…». Os
    Commentarii vão inteiros para Gn 1; nas Selecta, cada coluna da PG vai para os capítulos que cita (grupos de 4 palavras em
    comum com a LXX de Rahlfs, pelo menos 2).
  - Adnotationes in Genesim (PG 17, 12–?): os escólios trazem «ΚΕΦ. Ζʹ. Στίχ. δʹ.» (capítulo e versículo).
  - «Homiliae in Genesim.pdf» da khazarzar só tem um fragmento grego da Homilia 2 (a forma da arca): pista para Gn 6.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
GCS6 = 'https://archive.org/download/origenes-werke.-bd-6-1920/Origenes%20Werke.%20Bd%206%2C%201920_djvu.txt'
GCS6_VER = 'https://archive.org/details/origenes-werke.-bd-6-1920'
URL_COMM = G.khz('Origenes_PG 11-17', 'Commentarii in Genesim.pdf')
URL_SEL = G.khz('Origenes_PG 11-17', 'Selecta in Genesim.pdf')
URL_ADN = G.khz('Origenes_PG 11-17', 'Adnotationes in Genesim.pdf')
URL_HOMG = G.khz('Origenes_PG 11-17', 'Homiliae in Genesim.pdf')
HOMILIAS = {1: [1], 2: [6], 3: [17], 4: [18], 5: [19], 6: [20], 7: [21], 8: [22], 9: [22], 10: [24], 11: [25], 12: [25, 26],
            13: [26], 14: [26], 15: [45, 46], 16: [47]}
VAL = {'Α': 1, 'Β': 2, 'Γ': 3, 'Δ': 4, '∆': 4, 'Ε': 5, 'Ϛ': 6, 'Ζ': 7, 'Η': 8, 'Θ': 9, 'Ι': 10, 'Κ': 20, 'Λ': 30, 'Μ': 40, 'Ν': 50}


def homilia1():
    p = G.baixar(GCS6, 'ia/origenes-gcs6.txt', minimo=100000)
    L = G.ler(p).split('\n')
    a = next(i for i, l in enumerate(L) if re.match(r'^\s*HOMILIA PRIMA\.?\s*$', l))
    b = next(i for i in range(a + 50, len(L)) if re.match(r'^\s*HOMILIA\s+\S+\.?\s*$', L[i]))
    corpo = '\n'.join(l for l in L[a:b] if not re.match(r'^\s*in Genes\. Homilia', l))
    corpo = re.sub(r'-\s*\n\s*', '', corpo)
    corpo = re.sub(r'(?<!\n)\n(?!\n)', ' ', corpo)
    return re.sub(r'[ \t]+', ' ', corpo).strip()


def por_colunas(t, vol):
    """Divide o texto nas viradas de coluna «[PG v, n]» e devolve [(coluna, trecho, {cap: n})]."""
    partes = re.split(r'(\[PG \d+, \d+\])', t)
    out, col = [], None
    for x in partes:
        m = re.match(r'\[PG (\d+), (\d+)\]', x)
        if m:
            col = int(m.group(2))
            continue
        if x.strip():
            out.append((col, x.strip(), G.capitulos_citados(x, minimo=2)))
    return out


def adnotationes():
    t = G.texto_pdf(URL_ADN, 'origenes-adnot-gen')
    pos = [(m.start(), m.group(1)) for m in re.finditer(r'ΚΕΦ\.\s*([Α-ΩΔ∆Ϛ]{1,2})ʹ', t)]
    out = {}
    for k, (a, n) in enumerate(pos):
        b = pos[k + 1][0] if k + 1 < len(pos) else len(t)
        c = sum(VAL.get(ch, 0) for ch in n)
        out.setdefault(c, []).append(t[a:b].strip())
    return out


def main():
    caps = G.capitulos()
    comm_txt = G.texto_pdf(URL_COMM, 'origenes-comm-gen')
    sel = por_colunas(G.texto_pdf(URL_SEL, 'origenes-selecta-gen'), 12)
    adn = adnotationes()
    h1 = homilia1() if 1 in caps else ''
    for cap in caps:
        partes = []
        if cap == 1:
            partes.append('## Homiliae in Genesim, homilia 1 (latim de Rufino; GCS 29, 1–30; PG 12, 145–161)\n\n' + h1)
        if cap == 1:      # os fragmentos que restam são dos tomos I e III, todos sobre Gn 1
            partes.append('## Commentarii in Genesim, fragmentos gregos dos tomos I e III (PG 12, 45–92)\n\n'
                          + G.paragrafos(re.sub(r'^.*?(?=ΤΟΜΟΥ)', '', comm_txt, count=1)))
        for nome, lst in (('Selecta in Genesim (escólios gregos)', sel),):
            pedacos = [f'**[PG 12, {c}]** {x}' for c, x, cs in lst if cap in cs]
            if pedacos:
                partes.append(f'## {nome}\n\n' + '\n\n'.join(pedacos))
        if adn.get(cap):
            partes.append('## Adnotationes in Genesim (PG 17)\n\n' + '\n\n'.join(adn[cap]))
        homs = [h for h, cs in HOMILIAS.items() if cap in cs and h != 1]
        for h in homs:
            G.pista(cap, f'Orígenes, Homiliae in Genesim {h} (latim de Rufino; GCS 29, ed. Baehrens): sobre Gn {cap}; o OCR não '
                         f'separa os títulos das homilias, cortar à mão. {GCS6_VER}')
        if cap == 6:
            G.pista(cap, 'Orígenes, Homilia 2 sobre o Gênesis, fragmento grego (a forma da arca): ' + URL_HOMG)
        if not partes:
            if not homs:
                G.ausente(cap, f'Orígenes: nenhuma homilia, fragmento ou escólio grego achado sobre Gn {cap} (corte automático).')
            continue
        campos = {
            'Autor': 'Orígenes (c. 185–254)',
            'Obra': 'Homiliae in Genesim (Rufino); Commentarii in Genesim e Selecta in Genesim (fragmentos gregos)',
            'Passagem': ('homilia 1; ' if cap == 1 else '') + 'fragmentos e escólios que citam Gn ' + str(cap),
            'Edição': 'PG 12, 45–262 (homilias: GCS 29, ed. Baehrens 1920); escólios: PG 17',
            'Fonte': GCS6_VER + ' ; ' + URL_COMM + ' ; ' + URL_SEL,
            'Cobre': {1: 'o capítulo inteiro (homilia 1, alegórica: o firmamento, as águas, os luzeiros na alma; o homem «à imagem»); '
                         'nos fragmentos, a criação sem matéria eterna e Gn 1,14 contra a astrologia (Filocalia 23)'}.get(cap, 'ver o texto'),
            'Oriental': 'sim',
            'Língua': 'la (homilia, Rufino) e grc (fragmentos)',
        }
        nota = ('Homilia: OCR da GCS (archive.org), com o aparato crítico misturado e erros: para citar, conferir na imagem. '
                'Fragmentos: o corte por coluna da PG e por citação da LXX é automático. Orígenes: escritor eclesiástico, não santo.')
        G.gravar(cap, 'origenes-in-genesim', 'Orígenes, Homilias e fragmentos sobre o Gênesis', campos, '\n\n'.join(partes), nota, SCRIPT)
    G.registrar()


if __name__ == '__main__':
    main()
