"""São Cirilo de Alexandria, fragmentos sobre a 2ª Coríntios (ed. Pusey, 1872): corta por capítulo (3, 4, 5, 10, 13).

    python -I -X utf8 pesquisa/ferramentas/base/grc-cirilo-2cor.py

Baixa o PDF da khazarzar UMA vez (pesquisa/cache/base/paulo/cirilo-2cor.pdf) e converte com gregos-limpar.py.
O texto são fragmentos de cadeia, sem marcador de versículo: cada fragmento abre com o lema bíblico (às vezes
seguido de «κ.τ.λ.»), e os números soltos no meio do texto são as PÁGINAS de Pusey (vol. III; 2Cor 1 = pp. 320 ss.).
Cirilo só tem fragmentos para 2Cor 1–5, 10 e 13 (nada para 6–9, 11 e 12). Os pontos de corte são os lemas:
    cap. 3 = lema 3,2 «Ἡ ἐπιστολὴ ἡμῶν ὑμεῖς ἐστε»    cap. 4 = lema 4,4 «Εἰς τὸ μὴ αὐγάσαι» (o comentário a 3,18 corre até lá)
    cap. 5 = lema 5,1 «Οἴδαμεν γὰρ ὅτι ἐὰν ἡ ἐπίγειος» (o fim de 4,16-18 vai no cap. 4)
    cap. 10 = lema 10,1 «Αὐτὸς δὲ ἐγὼ Παῦλος παρακαλῶ»    cap. 13 = lema 13,3 «Ἐπεὶ δοκιμὴν ζητεῖτε»
O cap. 5 acaba onde começa o 10 (os fragmentos pulam de 5,21 para 10,1). Conferir os cortes olhando o início de cada arquivo.
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

URL = ('https://khazarzar.skeptik.net/pgm/PG_Migne/Cyril%20of%20Alexandria_PG%2068-77/'
       'Fragmenta%20in%20sancti%20Pauli%20epistulam%20ii%20ad%20Corinthios.pdf')
ANCORAS = {3: r'(?:\d{3} )?Ἡ ἐπιστολὴ ἡμῶν ὑμεῖς ἐστε', 4: r'Εἰς τὸ μὴ αὐγάσαι αὐτοῖς τὸν φωτισμὸν',
           5: r'Οἴδαμεν γὰρ ὅτι ἐὰν ἡ ἐπίγειος', 10: r'Αὐτὸς δὲ ἐγὼ Παῦλος παρακαλῶ',
           13: r'Ἐπεὶ δοκιμὴν ζητεῖτε'}
SEQUENCIA = [3, 4, 5, 10, 13]
VERSOS = {3: '3,2-18', 4: '4,4-18', 5: '5,1-21', 10: '10,1-6', 13: '13,3-4'}


def main():
    pdf = baixar(URL, 'cirilo-2cor.pdf')
    txt = ler(pdf_para_texto_grego(pdf, os.path.join(CACHE, 'cirilo-2cor.txt')))
    pos = {}
    for cap, pat in ANCORAS.items():
        m = re.search(pat, txt)
        assert m, cap
        pos[cap] = m.start()
    assert [pos[c] for c in SEQUENCIA] == sorted(pos[c] for c in SEQUENCIA), pos
    saidas = []
    for k, cap in enumerate(SEQUENCIA):
        a = pos[cap]
        b = pos[SEQUENCIA[k + 1]] if k + 1 < len(SEQUENCIA) else len(txt)
        bloco = txt[a:b].strip()
        # o marcador «ΤΟΜΟΣ … ΛΟΓΟΣ …» que precede o lema entra no capítulo seguinte; o que fecha o capítulo, sai
        bloco = re.sub(r'\s*ΤΟΜΟΣ [^\s]+ ΛΟΓΟΣ [^\s]+\s*$', '', bloco)
        paginas = [int(x) for x in re.findall(r'(?<=\s)(3[2-9]\d)(?=\s)', ' ' + bloco + ' ')]
        pag = ('?' if not paginas else f'{min(paginas)}' if min(paginas) == max(paginas) else f'{min(paginas)}–{max(paginas)}')
        # fragmentos: quebra de parágrafo nos marcadores de tomo/discurso e antes de cada «κ.τ.λ.» (fim de lema)
        bloco = re.sub(r'\s(ΤΟΜΟΣ [^\s]+ ΛΟΓΟΣ [^\s]+)\s', r'\n\n## \1\n\n', bloco)
        bloco = re.sub(r'κ\.τ\.λ\.\s', 'κ.τ.λ.\n\n', bloco)
        campos = {
            'Autor': 'São Cirilo de Alexandria (c. 376–444)',
            'Obra': 'Fragmenta in sancti Pauli epistulam II ad Corinthios',
            'Passagem': f'2Cor {VERSOS[cap]} (só os fragmentos que a cadeia conservou)',
            'Edição': f'ed. P. E. Pusey, In D. Joannis Evangelium, vol. III (Oxford 1872), {'p.' if '–' not in pag else 'pp.'} {pag}; PG 74',
            'Fonte': URL, 'Cobre': f'só fragmentos, versículos {VERSOS[cap]} (cada um abre com o lema bíblico)',
            'Oriental': 'sim', 'Língua': 'grc'}
        nota = ('Texto da khazarzar limpo por gregos-limpar.py. Os números soltos (331, 332…) são as páginas de Pusey. '
                'Fragmentos de cadeia: o comentário a um versículo pode correr sem lema novo até o seguinte. '
                'Cirilo não tem fragmentos para 2Cor 6–9, 11 e 12.')
        saidas.append(gravar(cap, 'cirilo-fragmenta-2cor.md', 'São Cirilo de Alexandria, fragmentos sobre a 2ª Coríntios',
                             campos, bloco, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
