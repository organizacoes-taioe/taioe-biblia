"""São João Damasceno, Commentarii in epistulas Pauli (PG 95), parte sobre 2 Coríntios: corta por capítulo (3 a 13).

    python -I -X utf8 pesquisa/ferramentas/base/grc-damasceno-2cor.py            # capítulos 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/grc-damasceno-2cor.py 3 4

Baixa o PDF da khazarzar (todas as cartas de Paulo, ~2 MB) UMA vez para pesquisa/cache/base/paulo/, converte
com pesquisa/ferramentas/gregos-limpar.py ([PG 95, n] = começo da coluna n) e corta pelos títulos
«ΚΕΦΑΛ. Γʹ.» etc. (a obra repete a divisão em capítulos das cartas). A parte de 2 Coríntios vai do título
«ΕΙΣ ΕΠΙΣΤΟΛΗΝ ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ Βʹ.» (PG 95, 705) até «ΕΙΣ ΕΠΙΣΤΟΛΗΝ ΠΡΟΣ ΓΑΛΑΤΑΣ».
Atenção: Damasceno resume Crisóstomo quase palavra por palavra; vale para registro.
Para as outras cartas basta trocar o título de início e fim (1 Cor: «ΕΙΣ ΕΠΙΣΤΟΛΗΝ Αʹ ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ», col. 569).
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

URL = ('https://khazarzar.skeptik.net/pgm/PG_Migne/John%20of%20Damascus_PG%2094-96/'
       'Commentarii%20in%20epistulas%20Pauli.pdf')
GREGO = {1: 'Αʹ', 2: 'Βʹ', 3: 'Γʹ', 4: 'Δʹ', 5: 'Εʹ', 6: 'ςʹ', 7: 'Ζʹ', 8: 'Ηʹ', 9: 'Θʹ', 10: 'Ιʹ',
         11: 'ΙΑʹ', 12: 'ΙΒʹ', 13: 'ΙΓʹ'}


def main():
    caps = [int(a) for a in sys.argv[1:]] or CAPS
    pdf = baixar(URL, 'damasceno-paulo.pdf')
    txt = ler(pdf_para_texto_grego(pdf, os.path.join(CACHE, 'damasceno-paulo.txt')))
    ini = txt.index('ΕΙΣ ΕΠΙΣΤΟΛΗΝ ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ Βʹ.')
    fim = txt.index('ΕΙΣ ΕΠΙΣΤΟΛΗΝ ΠΡΟΣ ΓΑΛΑΤΑΣ')
    parte = txt[ini:fim]
    pos = {}
    for cap in range(2, 14):
        m = re.search(r'ΚΕΦΑΛ\.\s*' + GREGO[cap].replace('ς', '[ςϛ]') + r'\.', parte)
        assert m, cap
        pos[cap] = m.start()
    pos[14] = len(parte)
    saidas = []
    for cap in caps:
        a, b = pos[cap], pos[cap + 1]
        bloco = parte[a:b].strip()
        c0 = re.findall(r'\[PG 95, (\d+)\]', txt[:ini + a])
        c0 = c0[-1] if c0 else '?'
        cs = re.findall(r'\[PG 95, (\d+)\]', bloco)
        c1 = cs[-1] if cs else c0
        corpo = f'[PG 95, {c0}]\n\n' + bloco
        campos = {
            'Autor': 'São João Damasceno (c. 675–749)',
            'Obra': 'Commentarii in epistulas Pauli (Ad Corinthios II)',
            'Passagem': f'2Cor {cap}',
            'Edição': f'PG 95, {c0}' + (f'–{c1}' if c1 != c0 else ''),
            'Fonte': URL, 'Cobre': 'o capítulo inteiro (resumo quase literal das homilias de Crisóstomo; só para registro)',
            'Oriental': 'sim', 'Língua': 'grc'}
        nota = ('Texto da «Ψηφιακή Πατρολογία» (khazarzar), limpo por gregos-limpar.py; [PG 95, n] marca o começo da '
                'coluna n. Junções de palavras automáticas: conferir na leitura.')
        saidas.append(gravar(cap, 'damasceno-in-2cor.md', 'São João Damasceno, Commentarii in epistulas Pauli (2 Coríntios)',
                             campos, corpo, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
