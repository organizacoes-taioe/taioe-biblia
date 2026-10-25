"""Santo Agostinho, De civitate Dei XI–XIV (PL 41, 315–436), por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-cidade.py <capítulo>   (1, 2 ou 3)

Grava pesquisa/genesis/<ccc>/base/agostinho-de-civitate-dei.md. A segunda parte da obra começa pela origem
das duas cidades, isto é, pela criação:
  - Gn 1: livros XI (a criação, o tempo, a luz = os anjos, os dias, «viu Deus que era bom», a queda dos anjos)
    e XII (a vontade má, a idade do mundo, a criação do homem, 21–28), inteiros;
  - Gn 2 e Gn 3: livros XIII (a morte, o paraíso, o corpo de Adão; Gn 2,7.17) e XIV (o pecado, as duas
    cidades), inteiros (separar à mão o que é de cada capítulo).
Texto: augustinus.it (`latino/cdd/cdd_NN_libro.htm`); colunas pelo Corpus Corporum, texto 21364.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402

MAPA = {
    1: ([11, 12], 'Gn 1,1–31 (e a queda dos anjos)', 'livros XI e XII inteiros'),
    2: ([13, 14], 'Gn 2 (com Gn 3: separar à mão)', 'livros XIII e XIV inteiros'),
    3: ([13, 14], 'Gn 3 (com Gn 2: separar à mão)', 'livros XIII e XIV inteiros'),
}


def main(cap):
    if cap not in MAPA:
        print(f'De civitate Dei XI–XIV: nada próprio sobre Gn {cap} (os livros XV–XVI seguem a história de Caim a Abraão).')
        return
    livros, cobre, passagem = MAPA[cap]
    A.obra_por_livros(cap, 'gen-agostinho-cidade.py', 'agostinho-de-civitate-dei.md',
                      'Santo Agostinho, De civitate Dei', 'De civitate Dei', 'cdd', 'cdd_{:02d}_libro.htm',
                      livros, 21364, 'PL 41', cobre, passagem)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    main(int(sys.argv[1]))
