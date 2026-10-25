"""Santo Agostinho, De civitate Dei XI–XIV (PL 41, 315–436), por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-cidade.py <capítulo>   (1, 2 ou 3)
    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-cidade.py 4-50         (livros XV–XVI, por capítulo)

Grava pesquisa/genesis/<ccc>/base/agostinho-de-civitate-dei.md. A segunda parte da obra começa pela origem
das duas cidades, isto é, pela criação:
  - Gn 1: livros XI (a criação, o tempo, a luz = os anjos, os dias, «viu Deus que era bom», a queda dos anjos)
    e XII (a vontade má, a idade do mundo, a criação do homem, 21–28), inteiros;
  - Gn 2 e Gn 3: livros XIII (a morte, o paraíso, o corpo de Adão; Gn 2,7.17) e XIV (o pecado, as duas
    cidades), inteiros (separar à mão o que é de cada capítulo).
  - Gn 4–49 (desde 25/10): os livros XV (de Caim e Abel ao dilúvio) e XVI (de Noé a Jacó e José; o cap. 43 já é Moisés)
    seguem a história do Gênesis; a tabela CAPS_XV_XVI diz que capítulos do Gênesis cada capítulo de Agostinho comenta
    (pelos títulos da NBA e pelas citações; conferir). Os capítulos sem nada (XV, 4 e 6; XVI, 8, 9, 17 e 43) ficam de fora;
    o Gn sem capítulo de Agostinho (23, 31, 33–45, 47, 50) não ganha arquivo.
Texto: augustinus.it (`latino/cdd/cdd_NN_libro.htm`); colunas pelo Corpus Corporum, texto 21364.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402

MAPA = {
    1: ([11, 12], 'Gn 1,1–31 (e a queda dos anjos)', 'livros XI e XII inteiros'),
    2: ([13, 14], 'Gn 2 (com Gn 3: separar à mão)', 'livros XIII e XIV inteiros'),
    3: ([13, 14], 'Gn 3 (com Gn 2: separar à mão)', 'livros XIII e XIV inteiros'),
}


# (livro, capítulo de Agostinho) -> capítulos do Gênesis
CAPS_XV_XVI = {
    (15, 1): [4], (15, 2): [16, 21], (15, 3): [16, 21], (15, 5): [4], (15, 7): [4], (15, 8): [4], (15, 9): [5, 6],
    (15, 10): [5], (15, 11): [5], (15, 12): [5], (15, 13): [5], (15, 14): [5], (15, 15): [5], (15, 16): [4, 5],
    (15, 17): [4, 5], (15, 18): [4], (15, 19): [5], (15, 20): [4, 5], (15, 21): [4, 5], (15, 22): [6], (15, 23): [6],
    (15, 24): [6], (15, 25): [6], (15, 26): [6], (15, 27): [6, 7, 8],
    (16, 1): [9, 10, 11], (16, 2): [9], (16, 3): [10], (16, 4): [10, 11], (16, 5): [11], (16, 6): [11], (16, 7): [7, 8],
    (16, 10): [11], (16, 11): [10, 11], (16, 12): [11], (16, 13): [11], (16, 14): [11], (16, 15): [12], (16, 16): [12],
    (16, 18): [12], (16, 19): [12], (16, 20): [13], (16, 21): [13], (16, 22): [14], (16, 23): [15], (16, 24): [15],
    (16, 25): [16], (16, 26): [17], (16, 27): [17], (16, 28): [17], (16, 29): [18, 19], (16, 30): [19, 20],
    (16, 31): [18, 21], (16, 32): [22], (16, 33): [24], (16, 34): [25], (16, 35): [25], (16, 36): [26], (16, 37): [27],
    (16, 38): [28, 29, 30], (16, 39): [32], (16, 40): [46], (16, 41): [49], (16, 42): [48],
}


def main_xv_xvi(cap):
    sel = sorted(k for k, cs in CAPS_XV_XVI.items() if cap in cs)
    if not sel:
        print(f'De civitate Dei XV–XVI: nada sobre Gn {cap}.')
        return
    livros = sorted({lv for lv, c in sel})
    passagem = '; '.join(f'livro {"XV" if lv == 15 else "XVI"}, ' + ', '.join(str(c) for l, c in sel if l == lv) for lv in livros)
    A.obra_por_livros(cap, 'gen-agostinho-cidade.py', 'agostinho-de-civitate-dei.md',
                      'Santo Agostinho, De civitate Dei', 'De civitate Dei', 'cdd', 'cdd_{:02d}_libro.htm',
                      livros, 21364, 'PL 41', f'Gn {cap}: os capítulos de Agostinho que o comentam (tabela CAPS_XV_XVI; conferir)',
                      passagem, lambda lv, r: (lv, r[1]) in sel)


def main(cap):
    if cap >= 4:
        return main_xv_xvi(cap)
    if cap not in MAPA:
        print(f'De civitate Dei XI–XIV: nada próprio sobre Gn {cap} (os livros XV–XVI seguem a história de Caim a Abraão).')
        return
    livros, cobre, passagem = MAPA[cap]
    A.obra_por_livros(cap, 'gen-agostinho-cidade.py', 'agostinho-de-civitate-dei.md',
                      'Santo Agostinho, De civitate Dei', 'De civitate Dei', 'cdd', 'cdd_{:02d}_libro.htm',
                      livros, 21364, 'PL 41', cobre, passagem)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not re.fullmatch(r'\d+(-\d+)?', sys.argv[1]):
        print(__doc__)
        sys.exit(1)
    a, _, b = sys.argv[1].partition('-')
    for c in range(int(a), int(b or a) + 1):
        main(c)
