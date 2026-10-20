"""Cornélio a Lápide e Guilherme Estius, comentários a 2 Coríntios (OCR do Internet Archive): caps. 3 a 13.

    python -I -X utf8 pesquisa/ferramentas/base/ocr-lapide-estius-2cor.py              # as duas obras, caps. 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/ocr-lapide-estius-2cor.py estius 3 4

Não são Padres nem santos (exegetas jesuíta e holandês, séc. XVI–XVII); entram porque reúnem os Padres e os medievais
verso a verso. Domínio público.
  lapide: Commentaria in Scripturam Sacram, ed. Vivès/Crampon, t. XVIII (Paris 1868): Romanos, 1 e 2 Coríntios.
          https://archive.org/details/commentariainscr18lapi ; 2Cor nas pp. 420–516, linhas 68042–83092 do `_djvu.txt`.
          Cada capítulo abre com «CAPUT <ordinal>.» e «SYNOPSIS CAPITIS»; o OCR mistura as colunas e as notas de Crampon
          (numeradas (1), (2), que não são de Lápide).
  estius: In omnes D. Pauli epistolas ... commentarii, ed. J. Holzammer (Mogúncia, Kirchheim, 1858), t. II.
          https://archive.org/details/guilielmiestiiin02estw ; 2Cor nas pp. 1–~200. Cada capítulo abre com «CAPUT <ordinal>.»
          (o OCR escreve CAPOT, CAPDT…), o texto da Vulgata do capítulo, as notas, o «SUMMARIUM CAPITIS» e o comentário.
O script baixa cada `_djvu.txt` UMA vez (pesquisa/cache/base/paulo/) e corta por linhas-âncora conferidas à mão (a numeração
de linhas é a do arquivo com os espaços duplos encolhidos, que é só o que se mexe no texto); confere o padrão da linha e para
se o arquivo mudar. Nenhuma correção de OCR é feita aqui.
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

IA = 'https://archive.org/download/{id}/{id}_djvu.txt'
ID_L, ID_E = 'commentariainscr18lapi', 'guilielmiestiiin02estw'
LAP = {3: (69656, 'TERTIUM'), 4: (70770, 'QUARTUM'), 5: (72133, 'QUINTUM'), 6: (73669, 'SYNOPSIS'), 7: (74765, 'SEPTIMUM'),
       8: (75551, 'OCTAVUM'), 9: (76504, 'NONUM'), 10: (77666, 'DECIMUM'), 11: (78743, 'UNDECIMUM'),
       12: (80534, 'DUODECIMUM'), 13: (82171, 'TERTIUM'), 14: (83092, 'GALATAS')}
EST = {3: (5042, 'CAP'), 4: (6850, 'CAP'), 5: (9066, 'CAP'), 6: (11992, 'CAP'), 7: (13515, 'CAP'), 8: (14710, 'CAP'),
       9: (16423, 'CAP'), 10: (17302, 'CAP'), 11: (18505, 'CAP'), 12: (20792, 'GAP'), 13: (22777, 'CAP'),
       14: (23517, 'IN EPISTOLAM')}


def linhas(id_):
    L = ler(baixar(IA.format(id=id_), f'ocr_{id_}.txt')).split('\n')
    return [re.sub(r' +', ' ', x).rstrip() for x in L]


def achar(L, anc, cap):
    a, pa = anc[cap]
    for k in range(10):
        if pa in L[a - 1 + k]:
            return a + k
    raise AssertionError((cap, a, pa, L[a - 1][:80]))


def lis(v):
    n = len(v)
    if not n:
        return []
    best, prev = [1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if v[j] <= v[i] and best[j] + 1 > best[i]:
                best[i], prev[i] = best[j] + 1, j
    i = max(range(n), key=lambda k: best[k])
    out = []
    while i >= 0:
        out.append(v[i])
        i = prev[i]
    return out[::-1]


def pags_lapide(trecho):
    v = []
    for l in trecho:
        m = re.search(r'COMMENTARIA IN', l)
        if m:
            for n in re.findall(r'\b(4[2-9]\d|5[01]\d)\b', l):
                v.append(int(n))
    return lis(v)


def pags_estius(trecho):
    v = []
    for l in trecho:
        m = re.fullmatch(r'\s*(\d{1,3})\s*', l)
        if m and 1 <= int(m.group(1)) <= 260:
            v.append(int(m.group(1)))
    return lis(v)


def faixa(pg):
    if not pg:
        return 'páginas não lidas no OCR'
    return f'pp. {min(pg)}–{max(pg)}' if max(pg) != min(pg) else f'p. {min(pg)}'


def main():
    args = sys.argv[1:]
    obras = ['lapide', 'estius']
    if args and args[0] in obras:
        obras = [args[0]]
        args = args[1:]
    caps = [int(a) for a in args] or CAPS
    saidas = []
    for obra in obras:
        L = linhas(ID_L if obra == 'lapide' else ID_E)
        anc = LAP if obra == 'lapide' else EST
        for cap in caps:
            a, b = achar(L, anc, cap), achar(L, anc, cap + 1)
            trecho = L[a - 1:b - 1]
            txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(trecho)).strip('\n')
            if obra == 'lapide':
                campos = {
                    'Autor': 'Cornélio a Lápide (1567–1637), jesuíta, exegeta (não é santo)',
                    'Obra': 'Commentaria in Scripturam Sacram: In II Epistolam ad Corinthios',
                    'Passagem': f'2Cor {cap}', 'Edição': 'ed. Vivès (Crampon), t. XVIII (Paris 1868); 2Cor ocupa as pp. 420–516, a página exata do capítulo não se lê no OCR',
                    'Fonte': IA.format(id=ID_L),
                    'Cobre': 'o capítulo inteiro, versículo por versículo (sinopse, comentário e tropologia; reúne Padres e medievais)',
                    'Oriental': 'não', 'Língua': 'la'}
                nota = ('OCR do Internet Archive: boa leitura, mas as colunas se misturam e o título «CAPUT N.» às vezes cai no meio do texto do '
                        'capítulo anterior; as notas numeradas (1), (2) são de Crampon, não de Lápide.')
                arq, tit = 'lapide-commentaria-2cor.md', 'Cornélio a Lápide, Commentaria in II Epistolam ad Corinthios'
            else:
                campos = {
                    'Autor': 'Guilherme Estius (Willem Hessels van Est, 1542–1613), exegeta (não é santo)',
                    'Obra': 'In omnes D. Pauli epistolas ... commentarii: Epistola II ad Corinthios',
                    'Passagem': f'2Cor {cap}', 'Edição': 'ed. J. Holzammer (Mogúncia 1858), t. II, ' + faixa(pags_estius(trecho)),
                    'Fonte': IA.format(id=ID_E),
                    'Cobre': 'o capítulo inteiro (texto da Vulgata, sumário e comentário versículo por versículo; equilibrado, cita os Padres)',
                    'Oriental': 'não', 'Língua': 'la'}
                nota = ('OCR do Internet Archive: boa leitura, com erros de letra (CAPOT/CAPDT por CAPUT, «ffl» por «M»), espaços duplos encolhidos; '
                        'os números soltos são as páginas da edição de 1858.')
                arq, tit = 'estius-commentarii-2cor.md', 'Guilherme Estius, Commentarii in epistolam II ad Corinthios'
            saidas.append(gravar(cap, arq, tit, campos, txt, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
