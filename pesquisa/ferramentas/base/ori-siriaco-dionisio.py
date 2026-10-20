"""Dionísio bar Salibi, comentário literal a Números e aos Salmos (siríaco): corta por capítulo e grava em base/.

    python -I -X utf8 pesquisa/ferramentas/base/ori-siriaco-dionisio.py --ver nm 17-25   # só mostra os cortes
    python -I -X utf8 pesquisa/ferramentas/base/ori-siriaco-dionisio.py nm 17-36 sl 37-60 # grava (feito em 2026-10-20)

Só grava o capítulo com 2 lemas reconhecidos ou mais (ou, nos Salmos, com o título do salmo) e 200 letras ou mais.

Texto: Digital Syriac Corpus n.º 231 (Números) e 238 (Salmos), transcrição do ms. Homs, Arquidiocese
siro-ortodoxa, MS 13 (SOAH 00013), sem edição impressa; texto siríaco de domínio público, TEI CC BY 4.0.
O comentário é um bloco corrido, sem divisão de capítulos: o corte sai dos lemas (as palavras da Peshitta que
Dionísio cita antes de explicar) e, nos Salmos, também dos títulos «ܡܙܡܘܪܐ ܕ…» quando ele os põe. Cada corte vai do
fim da frase anterior ao primeiro lema do capítulo até o fim da frase anterior ao primeiro lema do capítulo seguinte;
por isso pode levar uma ou duas frases do vizinho. Conferir antes de citar.
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_siriaco_comum as C

OBRAS = {
    'nm': dict(n=231, livro='numeros', fonte='Numbers', nome='Números', arquivo='dionisio-bar-salibi-comentario-numeros.md',
               obra='Comentário literal a Números (ܦܘܫܩܐ ܕܣܦܪܐ ܕܡܢܝܢܐ)'),
    'sl': dict(n=238, livro='salmos', fonte='Psalms', nome='Sl', arquivo='dionisio-bar-salibi-comentario-salmos.md',
               obra='Comentário literal aos Salmos (ܦܘܫܩܐ ܣܘܥܪܢܝܐ ܕܟܬܒܐ ܕܡܙܡܘܪܐ)'),
}
VAL = dict(zip('ܐܒܓܕܗܘܙܚܛܝܟܠܡܢܣܥܦܨܩܪܫܬ', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400]))
PALAVRA = {'ܩܕܡܝܐ': 1, 'ܬܪܝܢ': 2, 'ܬܠܬܐ': 3, 'ܐܪܒܥܐ': 4, 'ܚܡܫܐ': 5, 'ܫܬܐ': 6, 'ܫܒܥܐ': 7, 'ܬܡܢܝܐ': 8, 'ܬܫܥܐ': 9,
           'ܥܣܪܐ': 10, 'ܥܣܪܝܢ': 20, 'ܬܠܬܝܢ': 30, 'ܐܪܒܥܝܢ': 40, 'ܚܡܫܝܢ': 50, 'ܫܬܝܢ': 60, 'ܫܒܥܝܢ': 70,
           'ܬܡܢܝܢ': 80, 'ܬܫܥܝܢ': 90, 'ܡܐܐ': 100}
STATUS = ('Dionísio bar Salibi (†1171), bispo de Amida, da Igreja siro-ortodoxa (miafisita, fora da comunhão '
          'católica): escritor eclesiástico, usar com essa indicação')


def titulos_salmos(raw):
    """Posições (no texto bruto) dos títulos «ܡܙܡܘܪܐ ܕ<número>» (ou «ܡܙ̄ܡ ܕ…») → número do salmo."""
    out = []
    for m in re.finditer(r'ܡܙ(?:ܡܘܪܐ|̄ܡ|ܡܘܪܝܐ)\s+ܕ(\S+)(?:\s+(\S+))?', raw):
        bruto = m.group(1)
        w = C.SINAIS.sub('', bruto).strip('.:܀܇')
        num = None
        if '̄' in bruto:  # letras-número com traço (ܠ̄ܚ = 38)
            letras = re.sub('[^ܐ-ܯ]', '', C.SINAIS.sub('', bruto))
            if letras and all(c in VAL for c in letras):
                num = sum(VAL[c] for c in letras)
        elif w in PALAVRA:
            num = PALAVRA[w]
            w2 = C.SINAIS.sub('', m.group(2) or '').strip('.:܀܇')
            if w2.startswith('ܘ') and w2[1:] in PALAVRA and PALAVRA[w2[1:]] < 10:
                num += PALAVRA[w2[1:]]
        if num and 1 <= num <= 150:
            out.append((m.start(), num))
    return out


def crescente(hits):
    """Maior subsequência de capítulos não decrescentes (descarta citações cruzadas e lemas mal reconhecidos)."""
    import bisect
    caudas, idx_caudas, ant = [], [], [-1] * len(hits)
    for i, (p, c, v) in enumerate(hits):
        k = bisect.bisect_right(caudas, c)
        if k > 0:
            ant[i] = idx_caudas[k - 1]
        if k == len(caudas):
            caudas.append(c); idx_caudas.append(i)
        else:
            caudas[k] = c; idx_caudas[k] = i
    i = idx_caudas[-1] if idx_caudas else -1
    seq = []
    while i >= 0:
        seq.append(hits[i]); i = ant[i]
    return seq[::-1]


def cortar(chave, caps):
    o = OBRAS[chave]
    meta, blocos = C.ler_tei(o['n'])
    raw = ' '.join(b[2] for b in blocos)
    # palavras com a posição no texto bruto
    toks = [(m.start(), w) for m in re.finditer(r'\S+', raw) for w in [C.palavras(m.group(0))] if w]
    pos = [p for p, _ in toks]
    ws = [w[0] for _, w in toks]
    pesh = C.peshitta_at(o['fonte'])
    pf = collections.Counter()
    for tx in pesh.values():
        v = C.palavras(tx)
        pf.update(set(tuple(v[i:i + 3]) for i in range(len(v) - 2)))
    idx = collections.defaultdict(set)
    for (c, v), tx in pesh.items():
        p = C.palavras(tx)
        for i in range(len(p) - 2):
            g = tuple(p[i:i + 3])
            if pf[g] == 1 and sum(len(x) for x in g) >= 8:
                idx[g].add((c, v))
    hits = []  # (posição bruta, cap, vers)
    for i in range(len(ws) - 2):
        for c, v in idx.get(tuple(ws[i:i + 3]), ()):
            hits.append((pos[i], c, v))
    if chave == 'sl':
        hits += [(p, n, 0) for p, n in titulos_salmos(raw)]
    hits.sort()
    seq = crescente(hits)
    primeiro = {}
    for p, c, v in seq:
        primeiro.setdefault(c, p)
    fim_frase = [m.end() for m in re.finditer(r'[܀:.܁܂]', raw)]

    def recua(p):
        antes = [f for f in fim_frase if f <= p]
        return antes[-1] if antes else 0
    cortes = {}
    ordem = sorted(primeiro)
    for k, c in enumerate(ordem):
        if c not in caps:
            continue
        ini = recua(primeiro[c])
        fim = recua(primeiro[ordem[k + 1]]) if k + 1 < len(ordem) else len(raw)
        vs = sorted(set(v for p, cc, v in seq if cc == c and v))
        cortes[c] = (ini, fim, vs)
    return meta, blocos, raw, cortes


def paginas(blocos, raw, ini, fim):
    """Fólios do manuscrito que o trecho atravessa (pelo marcador de página do TEI)."""
    # o texto de 231/238 é um bloco só; os <pb> estão dentro dele: reler do XML
    return ''


def main():
    args = sys.argv[1:]
    ver = '--ver' in args
    args = [a for a in args if a != '--ver']
    for chave, faixa in zip(args[::2], args[1::2]):
        i, j = (int(x) for x in faixa.split('-'))
        caps = set(range(i, j + 1))
        o = OBRAS[chave]
        meta, blocos, raw, cortes = cortar(chave, caps)
        for c in sorted(caps):
            if c not in cortes:
                print(f"{chave} {c}: sem lemas reconhecidos (não gravado)")
                continue
            ini, fim, vs = cortes[c]
            trecho = raw[ini:fim].strip()
            print(f"{chave} {c}: {len(trecho)} letras, lemas vv. {vs[:12]}{'…' if len(vs) > 12 else ''} | {trecho[:70]} … {trecho[-50:]}")
            titulo_achado = chave == 'sl' and re.match(r'ܡܙ', C.SINAIS.sub('', trecho[:12]))
            if len(trecho) < 200 or (len(vs) < 2 and not titulo_achado):
                print('   (poucos lemas ou trecho curto: não gravado)')
                continue
            if ver:
                continue
            ref = f"{o['nome']} {c}" if chave == 'nm' else f"Sl {c} (Peshitta e hebraico; Sl {c - 1 if 10 <= c <= 147 else c} da LXX/Vulgata, aproximado)"
            campos = {
                'Autor': STATUS,
                'Obra': o['obra'],
                'Passagem': ref + f"; lemas reconhecidos: vv. {', '.join(map(str, vs)) or '—'}",
                'Edição': 'sem edição impressa: ms. Homs, Arquidiocese siro-ortodoxa, MS 13 (SOAH 00013), transcrito no Digital Syriac Corpus',
                'Fonte': f"https://syriaccorpus.org/{o['n']} (XML: https://raw.githubusercontent.com/srophe/syriac-corpus/main/data/tei/{o['n']}.xml)",
                'Cobre': 'o capítulo inteiro, em glosas literais curtas (corte automático pelos lemas; conferir as bordas)' if chave == 'nm'
                         else 'o salmo, em glosas literais curtas (corte automático pelos lemas e títulos; conferir as bordas)',
                'Língua': 'syr',
            }
            nota = ('Corte automático: começa na frase anterior ao primeiro lema reconhecido deste capítulo e vai até a frase '
                    'anterior ao primeiro lema do seguinte. Texto siríaco de domínio público; edição digital CC BY 4.0 '
                    '(Digital Syriac Corpus, James E. Walters et al.): citar a fonte.')
            C.gravar(o['livro'], c, o['arquivo'], f"Dionísio bar Salibi, {o['obra'].split(' (')[0]}: {o['nome'] if chave == 'nm' else 'Sl'} {c}",
                     campos, trecho, nota=nota, script='ori-siriaco-dionisio.py')


if __name__ == '__main__':
    main()
