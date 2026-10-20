"""Santo Efrém, comentário às cartas de Paulo (tradução latina dos Mequitaristas, Veneza 1893): 2 Coríntios, caps. 3 a 13.

    python -I -X utf8 pesquisa/ferramentas/base/ocr-efrem-2cor.py            # capítulos 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/ocr-efrem-2cor.py 3 4

O comentário só existe em armênio (a versão siríaca se perdeu); a tradução latina, «Commentarii in epistolas D. Pauli
nunc primum ex armeno in latinum sermonem a patribus Mekhitaristis translati» (Veneza, São Lázaro, 1893), está no
Internet Archive: https://archive.org/details/commentariiinepi00ephruoft . O script baixa o `_djvu.txt` UMA vez
(pesquisa/cache/base/paulo/ocr_commentariiinepi00ephruoft.txt) e corta pelos algarismos romanos soltos que abrem cada
capítulo no OCR (linhas-âncora conferidas à mão; o capítulo 5 aparece como «Y.» e o 3 como «IIT.»). A parte de 2 Coríntios
vai da linha «AD CORINTHIOS SECUNDA» (OCR: «AD CORDTIIIOS SECODi», linha 4046) até «OBSERVATIO INTERPRETIS» (linha 5407,
antes de 3 Coríntios, apócrifa). O OCR é ruim (letras trocadas, palavras partidas): o script só encolhe os espaços duplos;
não corrige nada. O capítulo 2 já foi corrigido à mão em pesquisa/2corintios/002/textos/efrem-commentarii-2cor-2.md.
Os números de página soltos («94», «95») são as páginas da edição de 1893.
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

ID = 'commentariiinepi00ephruoft'
URL = f'https://archive.org/download/{ID}/{ID}_djvu.txt'
ANC = {3: (4285, 'IIT'), 4: (4389, 'IV'), 5: (4484, 'Y'), 6: (4578, 'VI'), 7: (4665, 'VII'), 8: (4781, 'VIII'),
       9: (4878, 'IX'), 10: (4928, 'X'), 11: (5049, 'XI'), 12: (5217, 'XI'), 13: (5344, 'XIII'),
       14: (5407, 'OBSERVATIO')}


def paginas(trecho):
    v = []
    for l in trecho:
        m = re.fullmatch(r'\s*(\d{2,3})\s*', l)
        if m and 80 <= int(m.group(1)) <= 130:
            v.append(int(m.group(1)))
    return v


def main():
    caps = [int(a) for a in sys.argv[1:]] or CAPS
    L = ler(baixar(URL, f'ocr_{ID}.txt')).split('\n')
    for c, (n, pa) in ANC.items():
        assert pa in L[n - 1], (c, n, L[n - 1])
    saidas = []
    for cap in caps:
        a, b = ANC[cap][0], ANC[cap + 1][0]
        trecho = L[a - 1:b - 1]
        txt = '\n'.join(re.sub(r'  +', ' ', x).rstrip() for x in trecho)
        txt = re.sub(r'\n{3,}', '\n\n', txt).strip('\n')
        pg = paginas(trecho)
        ed = ('Mequitaristas, Veneza 1893' + ((f', p. {min(pg)}' if min(pg) == max(pg) else f', pp. {min(pg)}–{max(pg)}') + ' (números de página lidos no OCR)' if pg else ''))
        campos = {
            'Autor': 'Santo Efrém, o Sírio (c. 306–373)',
            'Obra': 'Commentarii in epistolas D. Pauli (ad Corinthios secunda), tradução latina do armênio',
            'Passagem': f'2Cor {cap}', 'Edição': ed, 'Fonte': URL,
            'Cobre': 'o capítulo inteiro, em glosas breves (OCR bruto da tradução latina; o original é armênio)',
            'Oriental': 'sim', 'Língua': 'la'}
        nota = ('OCR BRUTO do Internet Archive (letras trocadas, palavras partidas, espaços duplos encolhidos): reconstituir à mão antes de '
                'citar, como se fez com o cap. 2 (002/textos/efrem-commentarii-2cor-2.md). O comentário só sobrevive em armênio; o latim é a '
                'tradução dos Mequitaristas (1893). O algarismo romano do começo é o do capítulo da carta.')
        saidas.append(gravar(cap, 'efrem-commentarii-2cor.md', 'Santo Efrém, Commentarii in epistolas Pauli (2 Coríntios)',
                             campos, txt, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
