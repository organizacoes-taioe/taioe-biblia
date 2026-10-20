"""São Roberto Belarmino, Explanatio in Psalmos (1611): todos os salmos, em latim (OCR do archive.org).

    python -I -X utf8 pesquisa/ferramentas/base/lat-belarmino.py [--so 32 37 ...]   (números hebraicos)

Fonte: *Opera omnia*, ed. J. Fèvre, Paris, Vivès, 1870-1874; t. X (Sl 1-75 da Vulgata) = archive.org
`operaomnia10bell` e t. XI (Sl 76-150) = `operaomnia11bell`; texto OCR em
`https://archive.org/download/<id>/<id>_djvu.txt` (cache em pesquisa/cache/base/bel10.txt e bel11.txt).

O que o script faz (e os limites do OCR):
  - cada salmo da edição Fèvre traz ANTES um «Commentaria» do editor (versão do hebraico, «secundum
    Hebraeos», notas de Maurer, Ewald, Rosenmüller): isso fica de fora. O trecho de Belarmino começa em
    «BELLARMINI EXPLANATIO. / PSALMUS N. / (TITULUS ET) ARGUMENTUM» e acaba no começo do «Commentaria»
    do salmo seguinte (ou no «INDEX» / fim do volume);
  - o OCR erra os números romanos (G por C, Y por V, 1 por I...): os 150 começos são achados por três
    sinais (linha «PSALMUS» com «ARGUMENTUM» logo depois; linha «ARGUMENTUM»; «EXPLANATIO» seguida de
    «PSALMUS») e numerados em sequência, conferindo com o romano lido;
  - saem os cabeçalhos correntes («BELLARMINI EXPLANATIO.», «PSALMUS N. 123») e as quebras de sílaba
    (`¬`); as notas de margem do original ficam misturadas ao texto, no ponto onde o OCR as pôs, e
    erros de OCR permanecem (conferir a imagem em caso de dúvida: archive.org/details/operaomnia10bell);
  - não há marcas de página: o OCR dos números de página é pouco confiável (o campo Edição traz só o tomo).
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

VOLS = {10: 'operaomnia10bell', 11: 'operaomnia11bell'}
ROTULO = 'São Roberto Belarmino, Explanatio in Psalmos'


def url(vol):
    i = VOLS[vol]
    return f'https://archive.org/download/{i}/{i}_djvu.txt'


def linhas(vol):
    p = os.path.join(L.CACHE, f'bel{vol}.txt')
    L.baixar(url(vol), p)
    return open(p, encoding='utf-8').read().split('\n')


def fix(s):
    s = s.upper().strip(" .’'*")
    s = s.replace('G', 'C').replace('Y', 'V').replace('1', 'I').replace('H', 'II').replace('O', 'C')
    return s.replace('.', '')


RX_ARG = re.compile(r'^\s*(?:T\s*i\s*T\s*U\s*L\s*U\S*\s+ET\s+|TITULUS\s+ET\s+)?A\s?R\s?G\s?U\s?M\s?E?N?T?U?M?\W*\s*$')
RX_PS = re.compile(r'^\s*\S?[SA]ALMUS\s+(\S{1,9})\W{0,2}\s*\d{0,3}\W{0,2}\s*$')
RX_EXPL = re.compile(r'(B[A-Z0-9]{1,3}L[A-Z0-9]{0,3}\s*A?R?[A-Z0-9]{0,3}M?[A-Z0-9]{0,3}N?[A-Z0-9]?\s*)?[A-Z]{0,2}XPL[A-Z]{0,4}ATIO\W*$')


def proximo(Ls, i, n=1):
    out = []
    for j in range(i + 1, min(len(Ls), i + 12)):
        if Ls[j].strip():
            out.append((j, Ls[j]))
            if len(out) == n:
                break
    return out


def achar_inicios(Ls):
    c = set()
    for i, l in enumerate(Ls):
        if RX_PS.match(l) and not re.search(r'\d', l.strip().split(None, 1)[-1] if len(l.split()) > 1 else ''):
            nx = proximo(Ls, i, 2)
            if any(re.search(r'ARGUM|TITULUS', x) for _, x in nx):
                c.add(i)
        if l.strip() and RX_ARG.match(l):
            ps = [j for j in range(max(0, i - 6), i) if re.match(r'^\s*\S?[SA]ALMUS', Ls[j])]
            c.add(ps[-1] if ps else i)
        s = l.strip()
        if s and len(s) < 40 and RX_EXPL.search(s):
            nx = proximo(Ls, i, 1)
            if nx and re.match(r'^\s*\S?[SA]ALMUS\s+\S+\s*\W?\s*$', nx[0][1]):
                c.add(nx[0][0])
    out = []
    for x in sorted(c):
        if out and x - out[-1] < 25:
            continue
        out.append(x)
    return out


def rotulo_linha(l):
    m = re.match(r'^\s*\S?[SA]ALMUS\s+(\S+)', l)
    return m.group(1) if m else None


def numerar():
    """[(n, vol, indice_da_linha)] dos 150 começos."""
    res, n = [], 0
    dados = {v: linhas(v) for v in VOLS}
    for v in sorted(VOLS):
        Ls = dados[v]
        for i in achar_inicios(Ls):
            lab = rotulo_linha(Ls[i])
            r = L.de_romano(fix(lab)) if lab else None
            if r and n + 1 <= r <= n + 1:
                n = r
            else:
                n = n + 1
            res.append((n, v, i))
    return res, dados


RX_EDITOR = re.compile(r'SECUNDUM|HEBR|^\s*V\.\s*[vyd]\b|^\s*V\.\s*v')


def fim_do_trecho(Ls, ini, limite):
    """Índice onde acaba o trecho de Belarmino que começa em ini (limite: próximo começo ou fim do volume)."""
    for j in range(ini + 3, limite):
        l = Ls[j]
        if re.match(r'^\s*\S?[SA]ALMUS\s+\S{1,9}\W{0,2}\s*$', l):
            nx = proximo(Ls, j, 3)
            # «Commentaria» do editor: a linha PSALMUS é seguida de «SECUNDUM HEBRAEOS» / «V. v.»
            if nx and any(RX_EDITOR.search(x) for _, x in nx[:2]):
                # sobe sobre eventuais cabeçalhos próprios (página)
                return j
        if re.match(r'^\s*PSALMORUM\s*$', l):
            nx = proximo(Ls, j, 1)
            if nx and re.match(r'^\s*LIBER', nx[0][1]):
                return j
    return limite


def eh_cabecalho(s):
    up = s.upper()
    if len(s) > 46:
        return False
    if re.search(r'XPL[A-Z]{0,5}ATIO', up):
        return True
    if re.match(r'^(\d{1,3}\s+)?\S?[SA]ALMUS\s+\S{1,9}\W{0,2}(\s*\d{1,3}\W{0,2})?$', up):
        return True
    if 'COMMENTARIA IN' in up or up.startswith('COMMENTARIA'):
        return True
    return False


def limpar_trecho(Ls, ini, fim, n, pag_ant):
    """Devolve (paragrafos, ultima_pagina)."""
    paras, cur = [], ''
    ultimo = pag_ant
    pend_vazia = False
    primeira = True

    def flush():
        nonlocal cur
        t = re.sub(r'\s{2,}', ' ', cur).strip()
        if t:
            paras.append(t)
        cur = ''

    for j in range(ini, fim):
        s = Ls[j].strip()
        if not s:
            pend_vazia = True
            continue
        if primeira:
            primeira = False
            paras.append(f'PSALMUS {L.romano(n)}. (Belarmino, Explanatio)')
            pend_vazia = False
            continue
        # número de página solto ou no cabeçalho
        mp = re.match(r'^(\d{1,3})$', s) or re.match(r'^(?:\S?[SA]ALMUS\s+\S{1,9}\W{0,2}\s+)(\d{1,3})\W{0,2}$', s) \
            or re.match(r'^(\d{1,3})\s+\S?[SA]ALMUS\s+\S{1,9}\W{0,2}$', s) or re.match(r'^(\d{1,3})\s+\S*XPL\S*\W*$', s.upper()) \
            or re.match(r'^(?:[A-Z0-9 ]*XPL[A-Z]*\W*)\s+(\d{1,3})$', s.upper())
        if mp and re.match(r'^\d{1,3}$', s):
            continue
        if eh_cabecalho(s):
            continue
        if re.match(r'^\d{1,3}$', s):
            continue
        # junta linhas; une sílabas partidas
        if cur and pend_vazia:
            if re.search(r'[.:;?!»"”]\s*(\[p\. \d+\])?$', cur) or cur.isupper():
                flush()
        pend_vazia = False
        if cur.endswith('¬'):
            cur = cur[:-1] + s
        elif re.search(r'[A-Za-z]-$', cur) and s[:1].islower():
            cur = cur[:-1] + s
        else:
            cur = (cur + ' ' + s) if cur else s
    flush()
    return paras, ultimo


def main(so=None):
    inicios, dados = numerar()
    ns = [x[0] for x in inicios]
    assert ns == list(range(1, 151)), 'numeração dos começos não fecha 1..150'
    # limites
    fins = {}
    for k, (n, v, i) in enumerate(inicios):
        Ls = dados[v]
        prox = next((x for x in inicios[k + 1:] if x[1] == v), None)
        if prox:
            limite = prox[2]
        else:
            if v == 10:
                limite = next((j for j, l in enumerate(Ls) if j > i and re.search(r'Date\s+Due', l)), len(Ls))
            else:
                limite = next((j for j, l in enumerate(Ls) if j > i and re.match(r'^\s*INDEX\b', l)), len(Ls))
        fim = fim_do_trecho(Ls, i, limite)
        # tira o cabeçalho «BELLARMINI EXPLANATIO.» que precede o próximo começo
        while fim > i + 3 and (not Ls[fim - 1].strip() or eh_cabecalho(Ls[fim - 1].strip())):
            fim -= 1
        fins[n] = (v, i, fim)
    # páginas: percorre em ordem para a coerência
    secoes, pag = {}, {10: None, 11: None}
    for n in range(1, 151):
        v, i, fim = fins[n]
        paras, pag[v] = limpar_trecho(dados[v], i, fim, n, pag[v])
        secoes[n] = (v, paras)
    n_arq, tot = 0, 0
    for h in L.hebraicos_alvo():
        if so and h not in so:
            continue
        vs = L.vulgata_de_hebraico(h)
        blocos, vol = [], None
        for v in vs:
            vol, paras = secoes[v]
            corpo = '\n\n'.join(paras)
            blocos.append(corpo if len(vs) == 1 else f'## Salmo {v} (Vulgata)\n\n{corpo}')
        ed = f'Opera omnia, ed. J. Fèvre, Paris, Vivès, 1870–1874, t. {"X" if vol == 10 else "XI"}'
        tam = L.gravar_base(h, 'belarmino-explanatio-in-psalmos.md', ROTULO, 'São Roberto Belarmino (1542–1621)',
                            'Explanatio in Psalmos (1611)', L.nota_numeracao(h), ed, url(vol), 'o salmo inteiro',
                            '\n\n'.join(blocos), 'lat-belarmino.py',
                            nota='OCR do archive.org: pode haver erros de leitura e notas de margem do original misturadas ao texto; '
                                 'o «Commentaria» do editor (Fèvre) que precede cada salmo na edição foi omitido.',
                            leitor=f'https://archive.org/details/{VOLS[vol]}')
        n_arq += 1
        tot += tam
    print(f'[lat-belarmino.py] arquivos gravados: {n_arq}; {tot/1024:.0f} KB')


if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    main(so)
