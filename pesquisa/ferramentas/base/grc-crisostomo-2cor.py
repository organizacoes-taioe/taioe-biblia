"""São João Crisóstomo, Homilias sobre a 2ª Coríntios (PG 61, 381–610): corta por capítulo (3 a 13).

    python -I -X utf8 pesquisa/ferramentas/base/grc-crisostomo-2cor.py            # capítulos 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/grc-crisostomo-2cor.py 3 4        # só alguns

Baixa o PDF da «Ψηφιακή Πατρολογία» (espelho khazarzar) UMA vez para pesquisa/cache/base/paulo/,
converte com pesquisa/ferramentas/gregos-limpar.py (texto com marcadores [PG 61, n] = começo da coluna n)
e grava pesquisa/2corintios/<ccc>/base/crisostomo-in-2cor.md.

Homilia -> versículos (pelo lema com que cada homilia abre; a homilia pode terminar um versículo depois):
 1: 1,1-5   2: 1,6-11   3: 1,12-22   4: 1,23-2,11   5: 2,12-17   6: 3,1-6    7: 3,7-18   8: 4,1-7
 9: 4,8-18  10: 5,1-10  11: 5,11-21  12: 6,1-10    13: 6,11-7,1  14: 7,2-7   15: 7,8-12  16: 7,13-8,6
 17: 8,7-15 18: 8,16-24 19: 9,1-9    20: 9,10-15   21: 10,1-6    22: 10,7-18 23: 11,1-12 24: 11,13-20
 25: 11,21-33 26: 12,1-10 27: 12,11-15 28: 12,16-21 29: 13,1-9  30: 13,10-13
As homilias 13 e 16 passam de um capítulo ao outro: são cortadas no lema («Ταύτας οὖν ἔχοντες» = 7,1;
«Γνωρίζω δὲ ὑμῖν» = 8,1), e cada pedaço vai para o seu capítulo.
Limites conhecidos: o PDF às vezes erra o número da homilia (a 3 sai «Ιʹ», a 16 sai «Ι» + «ς.») e põe um
marcador de coluna adiantado no fim de uma homilia.
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

URL = ('https://khazarzar.skeptik.net/pgm/PG_Migne/John%20Chrysostom_PG%2047-64/'
       'In%20epistulam%20ii%20ad%20Corinthios.pdf')

# capítulo -> lista de (homilia, parte) ; parte: 'tudo', 'ate13', 'de13', 'ate16', 'de16'
PLANO = {
    3: [(6, 'tudo'), (7, 'tudo')],
    4: [(8, 'tudo'), (9, 'tudo')],
    5: [(10, 'tudo'), (11, 'tudo')],
    6: [(12, 'tudo'), (13, 'ate13')],
    7: [(13, 'de13'), (14, 'tudo'), (15, 'tudo'), (16, 'ate16')],
    8: [(16, 'de16'), (17, 'tudo'), (18, 'tudo')],
    9: [(19, 'tudo'), (20, 'tudo')],
    10: [(21, 'tudo'), (22, 'tudo')],
    11: [(23, 'tudo'), (24, 'tudo'), (25, 'tudo')],
    12: [(26, 'tudo'), (27, 'tudo'), (28, 'tudo')],
    13: [(29, 'tudo'), (30, 'tudo')],
}
VERS = {  # versículos de cada homilia (pelo lema)
    6: '3,1-6', 7: '3,7-18', 8: '4,1-7', 9: '4,8-18', 10: '5,1-10', 11: '5,11-21', 12: '6,1-10',
    13: '6,11-7,1', 14: '7,2-7', 15: '7,8-12', 16: '7,13-8,6', 17: '8,7-15', 18: '8,16-24', 19: '9,1-9',
    20: '9,10-15', 21: '10,1-6', 22: '10,7-18', 23: '11,1-12', 24: '11,13-20', 25: '11,21-33',
    26: '12,1-10', 27: '12,11-15', 28: '12,16-21', 29: '13,1-9', 30: '13,10-13'}
PASSAGEM = {3: '3,1-18', 4: '4,1-18', 5: '5,1-21', 6: '6,1-18 (e 7,1)', 7: '7,1-16', 8: '8,1-24',
            9: '9,1-15', 10: '10,1-18', 11: '11,1-33', 12: '12,1-21', 13: '13,1-13'}


def homilias(txt):
    marcas = [m.start() for m in re.finditer('ΟΜΙΛΙΑ ', txt)]
    assert len(marcas) == 30, len(marcas)
    marcas.append(len(txt))
    out = {}
    for i in range(30):
        bloco = txt[marcas[i]:marcas[i + 1]]
        bloco = re.sub(r'^ΟΜΙΛΙΑ [^\s]*\s*', '', bloco)        # tira «ΟΜΙΛΙΑ Δʹ.»
        bloco = re.sub(r'^[\sʹς.]+', '', bloco)               # restos de «Ις.» e «ΚΣΤ ʹ.»
        out[i + 1] = (marcas[i], bloco)
    return out


def col_antes(txt, pos):
    achados = re.findall(r'\[PG 61, (\d+)\]', txt[:pos])
    return int(achados[-1]) if achados else 381


def paragrafar(bloco):
    # cada seção da homilia (αʹ., βʹ., …) começa em parágrafo novo
    return re.sub(r'\s([α-θ]ʹ|ϛʹ)\. ', r'\n\n\1. ', bloco)


def main():
    caps = [int(a) for a in sys.argv[1:]] or CAPS
    pdf = baixar(URL, 'crisostomo-2cor.pdf')
    txt = ler(pdf_para_texto_grego(pdf, os.path.join(CACHE, 'crisostomo-2cor.txt')))
    hom = homilias(txt)
    cortes = {}
    h13 = hom[13][1]
    i13 = h13.index('Ταύτας οὖν ἔχοντες τὰς ἐπαγγελίας')
    h16 = hom[16][1]
    i16 = re.search(r'Γνωρίζω δὲ ὑμῖν, ἀδελφοὶ', h16).start()
    saidas = []
    for cap in caps:
        partes, col_ini, col_fim, cobertas = [], None, None, []
        for n, parte in PLANO[cap]:
            ini, bloco = hom[n]
            deslocamento = 0
            if parte == 'ate13': bloco = bloco[:i13]
            elif parte == 'de13': deslocamento, bloco = i13, bloco[i13:]
            elif parte == 'ate16': bloco = bloco[:i16]
            elif parte == 'de16': deslocamento, bloco = i16, bloco[i16:]
            c0 = col_antes(txt, ini + 14 + deslocamento)
            c1 = col_antes(txt, ini + 14 + deslocamento + len(bloco))
            col_ini = c0 if col_ini is None else col_ini
            col_fim = c1
            sufixo = {'tudo': '', 'ate13': ' (até 7,1, que a homilia começa a comentar)',
                      'de13': ' (a partir de 7,1)', 'ate16': ' (até 8,1)', 'de16': ' (a partir de 8,1)'}[parte]
            partes.append(f'## Homilia {n}: 2Cor {VERS[n]}{sufixo}\n\n[PG 61, {c0}]\n\n' + paragrafar(bloco))
            cobertas.append(f'{n}')
        corpo = '\n\n'.join(partes)
        homs = ' e '.join(cobertas) if len(cobertas) <= 2 else ', '.join(cobertas[:-1]) + ' e ' + cobertas[-1]
        campos = {
            'Autor': 'São João Crisóstomo (c. 349–407)',
            'Obra': 'In epistulam II ad Corinthios homiliae',
            'Passagem': f'2Cor {PASSAGEM[cap]} (homilias ' + '; '.join(f'{n}: {VERS[n]}' for n, _ in PLANO[cap]) + ')',
            'Edição': f'PG 61, {col_ini}–{col_fim}',
            'Fonte': URL,
            'Cobre': 'o capítulo inteiro, versículo por versículo (cada homilia termina numa exortação moral longa)',
            'Oriental': 'sim', 'Língua': 'grc'}
        nota = ('Texto da «Ψηφιακή Πατρολογία» (khazarzar), limpo por gregos-limpar.py; [PG 61, n] marca o começo da '
                'coluna n. Junções de palavras automáticas: conferir na leitura. Tradução antiga: NPNF I/12.')
        saidas.append(gravar(cap, 'crisostomo-in-2cor.md', 'São João Crisóstomo, In epistulam II ad Corinthios homiliae',
                             campos, corpo, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
