"""Santo Agostinho, De Trinitate VII, XII e XIV (PL 42): o homem à imagem de Deus (Gn 1,26-27).

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-trindade.py <capítulo>   (só 1)

Grava pesquisa/genesis/<ccc>/base/agostinho-de-trinitate.md com:
  - VII, 6, 12 («Faciamus… nostram»: o plural e a Trindade; o homem «ad imaginem», o Filho «imago»);
  - XII, 4, 4 – 8, 13 (a imagem não está no casal; está na mente; o homem e a mulher, 1Cor 11,7);
  - XIV inteiro (a imagem na memória, na inteligência e no amor de Deus; a imagem que não se perde e se renova).
Texto: augustinus.it (`latino/trinita/trinita_NN_libro.htm`); colunas pelo Corpus Corporum, texto 7441.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402


def filtro(lv, r):
    if lv == 7:
        return r[2] >= 12 or r == (7, 0, 0)
    if lv == 12:
        return 4 <= r[2] <= 13 or r == (12, 0, 0)
    return True


def main(cap):
    if cap != 1:
        print(f'De Trinitate: nada próprio sobre Gn {cap} (as citações de Gn 2–3 estão no livro XII, 12–13: pista).')
        return
    A.obra_por_livros(cap, 'gen-agostinho-trindade.py', 'agostinho-de-trinitate.md', 'Santo Agostinho, De Trinitate',
                      'De Trinitate libri quindecim', 'trinita', 'trinita_{:02d}_libro.htm', [7, 12, 14], 7441,
                      'PL 42', 'Gn 1,26-27 (a imagem e a semelhança; homem e mulher)',
                      'VII, 6, 12; XII, 4, 4 – 8, 13; XIV inteiro', filtro)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    main(int(sys.argv[1]))
