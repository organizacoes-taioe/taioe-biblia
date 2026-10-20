"""São Gregório de Nissa, Vida de Moisés (De vita Mosis), os trechos que tratam de Números, por capítulo.

    python -I -X utf8 pesquisa/ferramentas/base/grc-nissa-num.py

Baixa UMA vez o PDF da «Ψηφιακή Πατρολογία» (khazarzar):
https://khazarzar.skeptik.net/pgm/PG_Migne/Gregory%20of%20Nyssa_PG%2044-46/De%20vita%20Mosis.pdf
para pesquisa/cache/base/numeros/nissa-vita-mosis.pdf e grava numeros/<ccc>/base/nissa-vida-de-moises.md.

A obra (PG 44, 297-430) segue a ed. Musurillo (GNO VII/1, 1964): o texto vem dividido em seções «livro.seção» (1.1…1.78 = livro I,
a história; 2.1…2.321 = livro II, a contemplação). Gregório não comenta Números versículo a versículo: o livro I resume a vida de Moisés
(§§ 61-76 passam por Números) e o livro II lê os episódios como etapas da subida da alma (II, 256-321 cobrem Nm 12-25). A tabela MAPA
diz, seção por seção, a que capítulos de Números (Nova Vulgata) cada trecho vai (alguns vão a mais de um). Os marcadores de seção
às vezes perdem o «2.10»: o script aceita saltos de 1.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

URL = C.khazarzar_url('Gregory of Nyssa_PG 44-46', 'De vita Mosis.pdf')
C.baixar(URL, 'nissa-vita-mosis.pdf', minimo=1000)
L = C.pdf_linhas('nissa-vita-mosis.pdf')
txt = '\n'.join(L)

marcas = []
cur = (1, 0)
for m in re.finditer(r'(?<![\w.])([12])\.(\d{1,3})(?=\s)', txt):
    b, s = int(m.group(1)), int(m.group(2))
    if (b == cur[0] and cur[1] < s <= cur[1] + 2) or (b == 2 and cur[0] == 1 and s == 1 and cur[1] >= 60):
        marcas.append((m.start(), b, s))
        cur = (b, s)
pos = {(b, s): p for p, b, s in marcas}
ordem = [(b, s) for p, b, s in marcas]


def trecho(b0, s0, b1, s1):
    """Texto da seção b0.s0 até o fim da seção b1.s1 (inclusive)."""
    a = pos[(b0, s0)]
    k = ordem.index((b1, s1))
    fim = pos[ordem[k + 1]] if k + 1 < len(ordem) else len(txt)
    return txt[a:fim].strip()


# (livro, seção inicial, livro, seção final, rótulo, capítulos de Números)
MAPA = [
    (1, 63, 1, 64, 'I, 63–64: o povo se farta de carne', [11]),
    (1, 66, 1, 66, 'I, 66: falta de água', [20]),
    (1, 67, 1, 68, 'I, 67–68: a saudade do Egito, as serpentes e a serpente de bronze', [21]),
    (1, 69, 1, 71, 'I, 69–71: a revolta pelo sacerdócio e as varas', [17]),
    (1, 72, 1, 72, 'I, 72: a passagem proibida pelas terras vizinhas', [20, 21]),
    (1, 73, 1, 74, 'I, 73–74: Balac, Balaão e a jumenta', [22]),
    (1, 75, 1, 75, 'I, 75: o fim do povo estrangeiro e a queda de Israel na impureza', [25]),
    (2, 269, 2, 270, 'II, 269–270: a sede e a rocha', [20]),
    (2, 271, 2, 283, 'II, 271–283: a serpente de bronze e o madeiro', [21]),
    (2, 284, 2, 286, 'II, 284–286: o sacerdócio e a vara que floresce', [17]),
    (2, 287, 2, 291, 'II, 287–291: a vida entre os estrangeiros', [21]),
    (2, 292, 2, 297, 'II, 292–297: Balaão e a maldição contra quem vive na virtude', [22, 23, 24]),
    (2, 298, 2, 304, 'II, 298–304: Finéias e a queda no prazer', [25]),
]
por = {c: [] for c in C.CAPS}
for b0, s0, b1, s1, rot, nms in MAPA:
    for nm in nms:
        por[nm].append((rot, trecho(b0, s0, b1, s1)))

n_arq = 0
for cap in C.CAPS:
    if not por[cap]:
        continue
    corpo = '\n\n'.join(f'**[Gregório de Nissa, Vida de Moisés {r}]**\n\n{t}' for r, t in por[cap])
    campos = {
        'Autor': 'São Gregório de Nissa (c. 335–c. 395)',
        'Obra': 'Vida de Moisés (De vita Mosis)',
        'Passagem': f'{C.cap_nm(cap)}; ' + '; '.join(r.split(':')[0] for r, t in por[cap]),
        'Edição': 'PG 44, 297–430 (colunas não indicadas no PDF); texto da ed. Musurillo, GNO VII/1 (1964); seções «livro.seção»',
        'Fonte': URL,
        'Cobre': 'só os trechos que tratam deste capítulo (a obra lê os episódios como etapas da alma)',
        'Oriental': 'sim',
        'Língua': 'grc',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/grc-nissa-num.py',
    }
    nota = ('O PDF da «Ψηφιακή Πατρολογία» segue a edição crítica moderna (GNO VII/1, Musurillo 1964), com possível direito autoral: usar para pesquisa e '
            'citar curto; o texto da PG 44 é equivalente e de domínio público (colunas: OCR «patrologiaecursu44mignuoft» do archive.org). '
            'A numeração «2.292» é livro.seção da GNO. Os trechos foram escolhidos pela leitura do episódio, não por citação literal '
            '(Gregório parafraseia a LXX).')
    C.gravar(cap, 'nissa-vida-de-moises', 'São Gregório de Nissa, Vida de Moisés', campos, corpo, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {[r.split(":")[0] for r, t in por[cap]]}  {len(corpo)//1024 or 1} KB')
print(n_arq, 'arquivos')
C.finalizar()
