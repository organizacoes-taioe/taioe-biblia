"""Procópio de Gaza, Commentarii in Genesin (catena; PG 87/1, 21–512), por capítulo do Gênesis.

    python3 -I pesquisa/ferramentas/base/gen-gregos-procopio.py [capítulos]      (padrão: 1; ex.: 1-50)

Baixa UMA vez o OCR do archive.org «patrologiaecurs267unkngoog» (PG 87/1; texto em
https://archive.org/download/patrologiaecurs267unkngoog/patrologiaecurs267unkngoog_djvu.txt, 5 MB; o servidor às vezes
responde 500: rodar de novo) para pesquisa/cache/genesis/gregos/ia/pg087a.txt e grava genesis/<ccc>/base/procopio-commentarii-in-genesim.md.

Como é: Procópio compila trechos de Basílio, Nissa, Cirilo, Teodoreto, Orígenes, Dídimo (quase sempre sem dizer de quem); a PG
imprime o grego e o latim de Clauser em duas colunas, e o OCR intercala as linhas dos dois (o latim sai legível; o grego, ruim).
O comentário ao Gênesis vai do começo do livro até «COMMENTARII IN EXODUM»; o OCR marca os capítulos («CAPUT PRIMUM.»,
«CAPUT II.», «CAP. VII.»…), mas perde alguns títulos: o trecho de um título vai até o seguinte e vale para todos os capítulos
entre os dois números. Para Gn 3–50 vale a lista ORDEM dos títulos lidos à mão (ver main): o «CAP. Il.» (= III) era lido
como 49, e os arquivos de Gn 3–48 saíam com o trecho de Gn 2; Gn 1 e 2 seguem a regra antiga (o de Gn 2 diz «cobre Gn 2–48»,
mas o texto é só o de Gn 2). Colunas: números dos
cabeçalhos de página («21 COMMENTARII IN GENESIM. | 22»), interpolados. Para citar, ler na imagem da página (o grego da PG).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
OCR = 'https://archive.org/download/patrologiaecurs267unkngoog/patrologiaecurs267unkngoog_djvu.txt'
VER = 'https://archive.org/details/patrologiaecurs267unkngoog'
ROM = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def romano(s):
    s = s.upper().replace('Y', 'I').replace('1', 'I').replace('PRIMUM', 'I')
    s = re.sub(r'[^IVXLC]', '', s)
    if not s:
        return None
    n = 0
    for i, c in enumerate(s):
        v = ROM[c]
        n += -v if i + 1 < len(s) and ROM[s[i + 1]] > v else v
    return n


def main():
    caps = G.capitulos()
    L = G.ler(G.baixar(OCR, 'ia/pg087a.txt', minimo=1000000)).split('\n')
    fim = next(i for i, l in enumerate(L) if re.search(r'COMMENTARII IN EXODUM', l))
    heads = []
    for i in range(fim):
        m = re.match(r'^\s*CAP(?:UT|\.)\s+([IVXLYl1]+|PRIMUM)\.?\s*$', L[i])
        if m:
            n = romano(m.group(1))
            if n and (not heads or n > heads[-1][1]) and n <= 50:
                heads.append((i, n))
    # Gn 3–50 (desde 25/10): o romano() lê «CAP. Il.» como 49 e a regra acima perde todos os títulos depois dele (o Gn 2 ficava
    # «Gn 2–48» e o Gn 49 levava o resto). Os títulos curtos «CAP…» do OCR vão aqui na ordem, com o capítulo lido no texto que
    # segue cada um («CAP. Il.» = III, Serpens callidior; «CAPUT VY.» = V, Liber generationis; «CAP.» = XXII; «ΧΧΧΗ» = XXXII;
    # o 2.º «CAP. XXXI.» = XXXIII, Gn 33,10; «XXXIX - XLYII» = 39 a 47 juntos; «ΧΙ ΤΗ» = XLVIII). Capítulo sem título no
    # OCR (4, 15, 20, 29–30) fica no trecho do título anterior. Gn 1 e 2 continuam com a regra antiga (arquivos iguais).
    ordem = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35,
             36, 37, 38, 39, 48, 49, 50]
    cand = [i for i in range(fim) if re.match(r'^\s*CAP(?:UT|\.)?(?:\s.{0,25})?$', L[i]) and len(L[i].strip()) < 30]
    assert len(cand) == len(ordem), (len(cand), len(ordem))
    heads3 = list(zip(cand, ordem))
    # colunas: «21 COMMENTARII IN GENESIM. | 22»
    anc = [(0, 21)]
    for i in range(fim):
        if 'COMMENTAR' in L[i] and 'GENES' in L[i]:
            ns = [int(x) for x in re.findall(r'\b(\d{2,3})\b', L[i]) if anc[-1][1] < int(x) <= anc[-1][1] + 6 + (i - anc[-1][0]) // 60]
            if ns:
                anc.append((i, max(ns)))

    def col(i):
        ante = [a for a in anc if a[0] <= i]
        return ante[-1][1] if ante else 21
    for cap in caps:
        trechos = []
        hs = heads if cap <= 2 else heads3
        for k, (i, n) in enumerate(hs):
            j, prox = (hs[k + 1] if k + 1 < len(hs) else (fim, 51))
            if n <= cap < prox:
                trechos.append((i, j, n, prox - 1))
        if not trechos:
            G.ausente(cap, f'Procópio de Gaza, Commentarii in Genesin: trecho de Gn {cap} não achado no OCR.')
            continue
        partes = []
        for i, j, a, b in trechos:
            corpo = '\n'.join(l for l in L[i:j] if not re.search(r'COMMENTAR\S* IN', l))
            corpo = re.sub(r'-\s*\n\s*', '', corpo)
            corpo = re.sub(r'\n{2,}', '\n\n', corpo)
            partes.append(f'## Gn {a}' + (f'–{b}' if b > a else '') + f' (PG 87/1, c. {col(i)}–{col(j)})\n\n' + corpo.strip())
        campos = {
            'Autor': 'Procópio de Gaza (c. 465–c. 528)',
            'Obra': 'Commentarii in Genesin (Comentário ao Gênesis, catena)',
            'Passagem': f'Gn {cap}' + ('' if trechos[0][3] == trechos[0][2] else f' (o trecho do OCR cobre Gn {trechos[0][2]}–{trechos[0][3]})'),
            'Edição': 'PG 87/1, 21–512 (o capítulo: colunas no título da seção, interpoladas)',
            'Fonte': VER,
            'Cobre': 'o capítulo inteiro (grego e latim de Clauser misturados pelo OCR)',
            'Oriental': 'sim',
            'Língua': 'la e grc (OCR)',
        }
        nota = ('OCR de página com duas colunas (grego e latim) intercaladas: o latim de Clauser se lê; o grego quase não. Procópio '
                'copia outros Padres sem nomeá-los: antes de citar, achar a fonte (Basílio, Nissa, Cirilo, Teodoreto, Orígenes) e '
                'citar o autor.')
        G.gravar(cap, 'procopio-commentarii-in-genesim', 'Procópio de Gaza, Commentarii in Genesin', campos, '\n\n'.join(partes), nota, SCRIPT)
    G.registrar()


if __name__ == '__main__':
    main()
