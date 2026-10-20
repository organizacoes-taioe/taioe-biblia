"""Cramer, Catenae Graecorum Patrum in Novum Testamentum, t. V (Oxford 1844): catena sobre 2 Coríntios, caps. 3 a 13.

    python -I -X utf8 pesquisa/ferramentas/base/ocr-cramer-2cor.py            # capítulos 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/ocr-cramer-2cor.py 3 4

Edição de domínio público (J. A. Cramer, Oxford, 1844; a folha de rosto das cartas aos Coríntios diz 1841). Cada versículo
vem em lema, seguido dos fragmentos de cadeia de Crisóstomo, Severiano, Teodoreto, Cirilo, Dídimo, Ecumênio, Teofilato etc.
(as siglas dos autores se perdem no OCR). O OCR bom é o da digitalização Google `bub_gb_6enzBCMGxM8C` (grego legível, com
acentos e espíritos perdidos aqui e ali); o da Universidade de Toronto (`catenaegraecorum05cramuoft`), que as pesquisas de
2Cor 1 e 2 tinham tentado, sai em letras latinas e não serve.
O script baixa o `_djvu.txt` UMA vez e corta pelo lema do primeiro versículo de cada capítulo (linhas-âncora conferidas à
mão; o script confere o padrão e para se o arquivo mudar). A catena de 2Cor vai da linha 27544 («ΚΕΦ. Α΄.») à 36237
(«SCHOLIA E COD. 216»); o que vem depois (variantes do Cod. 216, adições do Cod. Roe 16 e índices) não é cortado por capítulo.
O cabeçalho de página «NNN ΕΞΗΓΗΣΙΣ … IV. 1.» dá a página de Cramer e o capítulo.verso.
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

ID = 'bub_gb_6enzBCMGxM8C'
URL = f'https://archive.org/download/{ID}/{ID}_djvu.txt'
ANC = {3: (29000, 'ρχόμεθα πάλιν'), 4: (30150, 'ΚΕΦ'), 5: (30686, 'ἐπίγειος'), 6: (31290, 'Συνεργοῦντες'),
       7: (31772, 'Ταύτας οὖν ἔχοντες'), 8: (32173, 'Γνωρίζομεν'), 9: (32718, 'Περὶ μὲν γὰρ τῆς διακονίας'),
       10: (33046, 'Αὐτὸς δὲ ἐγὼ Παῦλος'), 11: (33534, 'ἀνείχεσθέ μου μικρόν'), 12: (34388, 'Καυχᾶσθαι δὴ'),
       13: (34974, 'Τρίτον τοῦτο ἔρχομαι'), 14: (36237, 'SCHOLIA')}


def achar(L, cap):
    a, pa = ANC[cap]
    for k in range(8):
        if pa in L[a - 1 + k]:
            return a + k
    raise AssertionError((cap, a, pa, L[a - 1][:80]))


def paginas(trecho):
    v = []
    for l in trecho:
        if re.search(r'ΕΞΗΓΗΣΙΣ|EIIIZTOAHN|EIITZETOAHN|EHIXTOAHN|ΕΠΙΣΤΟΛΗΝ', l):
            for m in re.finditer(r'\b(3[6-9]\d|4[0-4]\d)\b', l):
                v.append(int(m.group(1)))
    # maior subsequência não decrescente (descarta leituras erradas do OCR)
    n = len(v)
    if not n:
        return v
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


def main():
    caps = [int(a) for a in sys.argv[1:]] or CAPS
    L = ler(baixar(URL, f'ocr_{ID}.txt')).split('\n')
    saidas = []
    for cap in caps:
        a, b = achar(L, cap), achar(L, cap + 1)
        trecho = [x.rstrip() for x in L[a - 1:b - 1]]
        txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(trecho)).strip('\n')
        pg = paginas(trecho)
        ed = 'ed. J. A. Cramer, Catenae Graecorum Patrum in N. T., t. V (Oxford 1844)'
        if pg:
            ed += f', c. p. {min(pg)}' + (f'–{max(pg)}' if max(pg) != min(pg) else '') + ' (lidas dos cabeçalhos do OCR)'
        campos = {
            'Autor': 'Catena (Cramer) sobre 2 Coríntios: Crisóstomo, Severiano, Teodoreto, Cirilo, Dídimo, Ecumênio e outros',
            'Obra': 'Catenae Graecorum Patrum in Novum Testamentum, t. V: Catenae in S. Pauli epistolas ad Corinthios',
            'Passagem': f'2Cor {cap}', 'Edição': ed, 'Fonte': URL,
            'Cobre': 'o capítulo inteiro, versículo por versículo (lema + fragmentos de cadeia; OCR do grego legível mas imperfeito)',
            'Oriental': 'sim', 'Língua': 'grc'}
        nota = ('OCR do Internet Archive (digitalização Google de 1844): grego legível, com acentos, espíritos e letras perdidos aqui e ali; '
                'números e letras soltas nas margens são as linhas e as siglas de Cramer. As atribuições a cada Padre não aparecem no OCR: '
                'conferir na imagem antes de atribuir (a cadeia mistura Crisóstomo, Severiano, Teodoreto, Cirilo e Dídimo).')
        saidas.append(gravar(cap, 'cramer-catena-2cor.md', 'Cramer, Catena em Paulo: 2 Coríntios (Crisóstomo, Severiano, Teodoreto, Cirilo, Dídimo e outros)',
                             campos, txt, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
