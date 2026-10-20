"""Cornélio a Lápide, Commentaria in Pentateuchum: Commentaria in Numeros (ed. Vivès, Paris, 1866-1868, t. II), por capítulo.

    python -I -X utf8 pesquisa/ferramentas/base/lat-lapide-num.py

Baixa UMA vez o OCR do archive.org (https://archive.org/details/commentariainscr02lapi_0; texto em
.../download/commentariainscr02lapi_0/commentariainscr02lapi_0_djvu.txt, 3,4 MB, t. II = Levítico, Números, Deuteronômio)
e grava numeros/<ccc>/base/lapide-commentaria-in-numeros.md. Cada capítulo traz o título «CAPUT …» e uma «SYNOPSIS
CAPITIS» logo abaixo; é isso que marca o começo de cada um dos 36 capítulos. Lápide segue a Vulgata: o cap. XVI tem 50
versículos (os turíbulos, Vulg. 16,37-40 = NV 17,2-5, começam na linha «37. TOLLAT THURIBULA»), e o cap. XVII é a vara de Aarão:
Nm 17 (NV) = do «37. TOLLAT THURIBULA» do cap. XVI ao fim do cap. XVII. O cap. XXIX, cujo título o OCR estragou
(«CAFULI VIGUESIMUM NONUM»), é achado pela SYNOPSIS. Os cabeçalhos de página («COMMENTARIA IN NUMEROS, cap. XVI. 273»)
viram «[pág. 273]»; os números de página que o OCR estropia são descartados. Para o intervalo de páginas de cada capítulo
(no campo Edição), o script interpola entre os cabeçalhos bem lidos (~150 linhas de OCR por página): é estimativa.
O OCR mistura às vezes as duas colunas e a coluna estreita dos números de versículo («Vers. 35.»), estropia «æ» e perde letras:
conferir na imagem (página P = imagem n(P+31): https://archive.org/download/commentariainscr02lapi_0/page/n<P+31>.jpg) antes de citar.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

URL = 'https://archive.org/details/commentariainscr02lapi_0'
OCR = 'https://archive.org/download/commentariainscr02lapi_0/commentariainscr02lapi_0_djvu.txt'
p = C.baixar(OCR, 'lapide_t2_djvu.txt', minimo=100000)
L = C.ler(p).split('\n')

sy = [i for i in range(30800, 60300) if re.search(r'SYNOPSIS', L[i], flags=re.I)]
assert len(sy) == 36, len(sy)
ini = {}
for k, i in enumerate(sy, start=1):
    j = i - 1
    while j > 0 and not L[j].strip():
        j -= 1
    ini[k] = j
fim_total = next(i for i in range(ini[36], len(L)) if re.match(r'^\s*ARGUMENTUM', L[i]))
fim = {k: (ini[k + 1] if k < 36 else fim_total) for k in range(1, 37)}
a17 = next(i for i in range(ini[16], fim[16]) if re.match(r'^\s*37\.\s*TOLLAT THURIBULA', L[i]))

HEAD = re.compile(r'^\s*COMMENTARIA\s+IN\s+N\S*ROS\b(.*)$', re.I)


def limpar(linhas):
    """Tira os cabeçalhos de página (guarda o número, quando bem lido) e compacta as linhas em branco."""
    out = []
    for l in linhas:
        m = HEAD.match(l)
        if m:
            n = re.findall(r'\b(\d{3})\b', m.group(1))
            if n and 190 <= int(n[-1]) <= 370:
                out.append(f'[pág. {n[-1]}]')
            continue
        out.append(l.rstrip())
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip('\n')


def rom(n):
    r = ''
    for v, sy_ in ((50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += sy_
            n -= v
    return r


# âncoras de página: cabeçalhos que o OCR leu bem (pág. entre 190 e 370, em ordem crescente)
anc = []
ult = 0
for i in range(30800, 60300):
    m = HEAD.match(L[i])
    if m:
        n = re.findall(r'\b(\d{3})\b', m.group(1))
        if n and 190 <= int(n[-1]) <= 370 and int(n[-1]) >= ult:
            anc.append((i, int(n[-1])))
            ult = int(n[-1])


def pagina(linha):
    """Página impressa estimada (interpolação entre as âncoras; ~150 linhas de OCR por página)."""
    if linha <= anc[0][0]:
        return anc[0][1] - (anc[0][0] - linha) / 150
    for (i0, p0), (i1, p1) in zip(anc, anc[1:]):
        if i0 <= linha <= i1:
            return p0 + (p1 - p0) * (linha - i0) / max(1, i1 - i0)
    i0, p0 = anc[-1]
    return p0 + (linha - i0) / 150


n_arq = 0
for cap in C.CAPS:
    if cap == 17:
        a, b = a17, fim[17]
        txt = limpar(L[a17:fim[16]]) + '\n\n' + limpar(L[ini[17]:fim[17]])
        rotulo = 'cap. XVI (a partir do v. 37, «TOLLAT THURIBULA») e cap. XVII'
    else:
        a, b = ini[cap], fim[cap]
        txt = limpar(L[a:b])
        rotulo = f'cap. {rom(cap)}'
    pa, pb = int(pagina(a)), int(pagina(b))
    pg = f'pp. ~{pa}–{pb} (estimadas)'
    campos = {
        'Autor': 'Cornélio a Lápide (1567–1637), jesuíta (escritor, não canonizado)',
        'Obra': 'Commentaria in Scripturam Sacram: Commentaria in Pentateuchum, Numeri',
        'Passagem': f'{C.cap_nm(cap)}; Lápide, {rotulo}',
        'Edição': f'ed. Vivès, Paris, 1866–1868 (ed. A. Crampon), t. II, {pg}',
        'Fonte': URL,
        'Cobre': 'o capítulo inteiro, versículo a versículo, com o texto da Vulgata no começo e a SYNOPSIS',
        'Oriental': 'não',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/lat-lapide-num.py',
    }
    nota = ('OCR do archive.org (' + OCR + '): mistura às vezes as duas colunas e a coluna dos números de versículo, estropia «æ» e '
            'perde letras. Conferir na imagem (página P = imagem n(P+31)) antes de citar. Os cabeçalhos de página viram «[pág. N]»; '
            'o intervalo de páginas do campo Edição é estimado. Lápide cita os Padres e os exegetas (Orígenes, Agostinho, Jerônimo, Ruperto, '
            'Tostado/Abulense, Lira): as citações dele se conferem no original antes de entrar como dos Padres.')
    C.gravar(cap, 'lapide-commentaria-in-numeros', 'Cornélio a Lápide, Commentaria in Numeros', campos, txt, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {len(txt)//1024:3d} KB  {pg}')
print(n_arq, 'arquivos')
C.finalizar()
