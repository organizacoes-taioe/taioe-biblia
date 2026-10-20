"""Comentários bizantinos a 2 Coríntios na PG de Migne, só em OCR do Internet Archive: Teodoreto, Ecumênio, Teofilato.

    python -I -X utf8 pesquisa/ferramentas/base/ocr-pg-2cor.py               # as três obras, caps. 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/ocr-pg-2cor.py teodoreto 3 4

Nenhuma das três está no khazarzar (texto digital da PG); só existe o OCR do Internet Archive, com a PG em duas
colunas (grego | latim de Migne), então as linhas vêm misturadas. O script baixa cada `_djvu.txt` UMA vez para
pesquisa/cache/base/paulo/ e corta por capítulo a partir de LINHAS-ÂNCORA conferidas à mão (cada âncora é a
linha do título do capítulo, ou do primeiro versículo, no OCR; o script confere o padrão da linha e para se o
arquivo mudar). Nada é corrigido: o texto é o do OCR.

  teodoreto (PG 82, Interpretatio in xiv epistolas S. Pauli, 2Cor = cols. 377–460): dois OCR da mesma PG:
      grego legível, com κ→χ, β→δ/θ e o latim em letras gregas:  patrologiae_cursus_completus_gr_vol_082
      latim legível, grego ilegível:                              bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1859_82
  ecumenio  (PG 118, Oecumenii Commentaria; 2Cor = cols. c. 899–1090): patrologicursus21migngoog (vol. 118, Google). O grego do OCR
      perde o fim das linhas; a numeração «CAPUT» do Ecumênio NÃO é a dos capítulos (usa capítulos bizantinos): o corte segue
      os marcadores «III, 16-18.» (capítulo, versículos) do latim de Migne.
  teofilato (PG 124, Expositio in epistolam II ad Corinthios, cols. 791–?): patrologicursus37migngoog (vol. 124, Google). Grego e latim
      legíveis; corte pelos títulos «CAPUT III.» do latim.
O número da coluna da PG vem dos cabeçalhos de página do OCR (números soltos), por isso é aproximado.
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

IA = 'https://archive.org/download/{id}/{id}_djvu.txt'
GR82 = 'patrologiae_cursus_completus_gr_vol_082'
LA82 = 'bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1859_82'
G118 = 'patrologicursus21migngoog'
G124 = 'patrologicursus37migngoog'

# capítulo -> (linha, padrão que a linha tem de conter); a chave 14 é o fim da carta
TEO_GR = {3: (29181, 'ΚΕΦ'), 4: (29820, 'ΚΕΦΑΛ'), 5: (30260, 'ΚΕΦΑΛ'), 6: (30855, 'ΚΕΦΑΛ'), 7: (31180, 'ΚΕΦΑΛ'),
          8: (31565, 'ΚΕΦΑΛ'), 9: (32163, 'ΚΕΦΑΛ'), 10: (32809, 'ΚΕΦΑΛ'), 11: (33235, 'ΚΕΦΑΛ'),
          12: (33930, 'ΚΕΦΑΛ'), 13: (34431, 'ΚΕΦΑΛ'), 14: (34870, 'ΥΠΟΘΕΣΙΣ')}
TEO_LA = {3: (31591, 'CAP'), 4: (32280, 'CAP. IV'), 5: (32788, 'CAP'), 6: (33220, 'CAP. VI'), 7: (33583, 'CAP'),
          8: (34121, 'TOMUS'), 9: (34666, 'CAPUT'), 10: (35028, 'X'), 11: (35415, 'CAPUT'), 12: (36224, 'CAPUT'),
          13: (36819, 'CAPUT XIII'), 14: (37455, 'GALATAS')}
OEC = {3: (66668, 'III, 1-3'), 4: (67323, 'ἔχοντες'), 5: (68087, 'V, 1'), 6: (69158, 'VI, 1-3'), 7: (69847, 'VII, 1'),
       8: (71008, 'VIII, 1-2'), 9: (71949, 'IX, 1-2'), 10: (72348, 'X, 1-3'), 11: (72926, ''), 12: (74137, ''),
       13: (75032, 'XIII, 1'), 14: (75621, 'GALATAS')}
TFL = {3: (60236, 'CAPUT'), 4: (60959, 'CAPUT IV'), 5: (61789, 'CAPUT V'), 6: (62652, 'CAPUT VI'), 7: (63390, 'CAPUT VII'),
       8: (64211, 'CAPUT VIII'), 9: (65139, 'CAPUT'), 10: (65740, 'CAPUT X'), 11: (66450, 'CAPUT XI'),
       12: (68005, 'CAPUT XII'), 13: (69195, 'CAPUT XIII'), 14: (69880, 'GALATAS')}


def linhas(id_):
    return ler(baixar(IA.format(id=id_), f'ocr_{id_}.txt')).split('\n')


def achar(L, anc, cap):
    """Linha (1-based) da âncora: a indicada ou, se o padrão não estiver nela, a primeira das 8 seguintes que o tenha."""
    a, pa = anc[cap]
    for k in range(8):
        if pa in L[a - 1 + k]:
            return a + k
    raise AssertionError((cap, a, pa, L[a - 1][:80]))


def corte(L, anc, cap):
    a = achar(L, anc, cap)
    b = achar(L, anc, cap + 1)
    trecho = [x.rstrip() for x in L[a - 1:b - 1]]
    # tira linhas vazias em excesso
    txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(trecho)).strip('\n')
    return txt, trecho


def lis(v):
    """Maior subsequência não decrescente (descarta os números lidos errado pelo OCR)."""
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


def colunas(trecho, lo, hi):
    nums = []
    for l in trecho:
        s = l.strip()
        m = re.fullmatch(r'\D{0,3}(\d{3,4})\D{0,3}', s)
        if m and lo <= int(m.group(1)) <= hi:
            nums.append(int(m.group(1)))
        for m in re.finditer(r'^(\d{3,4}) (?:INTERPRETATIO|EXPOSITIO|OECUMENII|THEOPHYL)|(?:INTERPRETATIO|EXPOSITIO)[^\d]{0,60}(\d{3,4}) *$', s):
            n = int(m.group(1) or m.group(2))
            if lo <= n <= hi:
                nums.append(n)
    nums = lis(nums)
    return (min(nums), max(nums)) if nums else (None, None)


def faixa(pg, lo, hi, trecho):
    a, b = colunas(trecho, lo, hi)
    if a is None:
        return f'PG {pg}, colunas não lidas no OCR'
    return f'PG {pg}, c. {a}–{b} (lidas dos cabeçalhos do OCR)' if a != b else f'PG {pg}, c. {a} (lida dos cabeçalhos do OCR)'


def main():
    args = sys.argv[1:]
    obras = ['teodoreto', 'ecumenio', 'teofilato']
    if args and args[0] in obras:
        obras = [args[0]]
        args = args[1:]
    caps = [int(a) for a in args] or CAPS
    saidas = []
    for obra in obras:
        for cap in caps:
            if obra == 'teodoreto':
                tg, trg = corte(linhas(GR82), TEO_GR, cap)
                tl, trl = corte(linhas(LA82), TEO_LA, cap)
                corpo = ('## Grego (OCR de patrologiae_cursus_completus_gr_vol_082; o latim de Migne sai misturado, em letras gregas)\n\n'
                         + tg + '\n\n## Latim de Migne (OCR de ..._1859_82; o grego sai ilegível, em letras latinas)\n\n' + tl)
                campos = {
                    'Autor': 'Teodoreto de Ciro (c. 393–c. 460)', 'Obra': 'Interpretatio in xiv epistolas sancti Pauli (Ad Corinthios II)',
                    'Passagem': f'2Cor {cap}', 'Edição': faixa(82, 370, 470, trl + trg),
                    'Fonte': IA.format(id=GR82) + ' (grego) e ' + IA.format(id=LA82) + ' (latim)',
                    'Cobre': 'o capítulo inteiro, versículo por versículo (OCR bruto, grego e latim de Migne)', 'Oriental': 'sim', 'Língua': 'grc'}
                nota = ('OCR BRUTO do Internet Archive: a PG 82 tem grego e latim em colunas paralelas e o OCR mistura as linhas. '
                        'Serve para achar o trecho e ler o latim de Migne; para citar o grego, conferir a imagem da coluna. '
                        'O corte é por linhas-âncora (ver o topo do script). Teodoreto lê 1,9 «τῷ ἐγείραντι».')
                saidas.append(gravar(cap, 'teodoreto-interpretatio-2cor.md', 'Teodoreto de Ciro, Interpretatio in epistolam II ad Corinthios',
                                     campos, corpo, nota))
            elif obra == 'ecumenio':
                t, tr = corte(linhas(G118), OEC, cap)
                campos = {
                    'Autor': 'Ecumênio de Trica (escritor bizantino, séc. VI–X; atribuição discutida)',
                    'Obra': 'Commentaria in epistolas Pauli (Ad Corinthios II)', 'Passagem': f'2Cor {cap}',
                    'Edição': 'PG 118, 2Cor ocupa as cols. c. 899–1090; a coluna exata do capítulo não se lê no OCR', 'Fonte': IA.format(id=G118),
                    'Cobre': 'o capítulo, por pericopes «cap., vers.» (OCR bruto; o grego perde o fim das linhas)',
                    'Oriental': 'sim', 'Língua': 'grc'}
                nota = ('OCR BRUTO (digitalização Google da PG 118): grego e latim de Migne em colunas paralelas, linhas misturadas e '
                        'grego incompleto; o latim ao lado é legível. A numeração «CAPUT» do OCR é a dos capítulos bizantinos do Ecumênio '
                        '(não a do texto bíblico): o corte segue as pericopes «III, 16-18.».')
                saidas.append(gravar(cap, 'ecumenio-commentaria-2cor.md', 'Ecumênio de Trica, Commentaria in epistolam II ad Corinthios',
                                     campos, t, nota))
            else:
                t, tr = corte(linhas(G124), TFL, cap)
                campos = {
                    'Autor': 'Teofilato de Ocrida (c. 1055–c. 1107, arcebispo da Bulgária)',
                    'Obra': 'Expositio in epistolam II ad Corinthios', 'Passagem': f'2Cor {cap}',
                    'Edição': 'PG 124, 2Cor ocupa as cols. c. 791–952; a coluna exata do capítulo não se lê no OCR', 'Fonte': IA.format(id=G124),
                    'Cobre': 'o capítulo inteiro, versículo por versículo (grego e latim de Migne; resume Crisóstomo)',
                    'Oriental': 'sim', 'Língua': 'grc'}
                nota = ('OCR do Internet Archive (digitalização Google da PG 124): grego e latim de Migne em colunas paralelas, as linhas '
                        'chegam em blocos alternados. O corte é pelo título «CAPUT N.» do latim.')
                saidas.append(gravar(cap, 'teofilato-expositio-2cor.md', 'Teofilato de Ocrida, Expositio in epistolam II ad Corinthios',
                                     campos, t, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
