"""Santo Agostinho, Confessiones XI–XIII (PL 32, 809–868): o comentário do começo do Gênesis, por capítulo.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-confissoes.py <capítulo do Gênesis>   (ex.: 1)

Grava pesquisa/genesis/<ccc>/base/agostinho-confissoes.md. Só os capítulos 1 e 2 têm comentário:
  - Gn 1: XI inteiro (Gn 1,1, «no princípio», e o tempo), XII inteiro (Gn 1,1-2: o céu do céu e a matéria
    informe) e XIII, 1–49 (os seis dias lidos como a Igreja: o firmamento = a Escritura, as águas, os
    luzeiros, os peixes, o homem à imagem, o «muito bom»);
  - Gn 2: XIII, 50–53 (o sétimo dia, o descanso de Deus, Gn 2,2-3).
Texto: augustinus.it (`latino/confessioni/conf_NN_libro.htm`); colunas da PL pelo Corpus Corporum, texto 7270.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402

MAPA = {
    1: ([11, 12, 13], lambda lv, r: lv in (11, 12) or (lv == 13 and r[2] <= 49),
        'Gn 1,1–31: livros XI, XII e XIII, 1–49', 'XI e XII inteiros; XIII, 1, 1 – 34, 49'),
    2: ([13], lambda lv, r: r[2] >= 50, 'Gn 2,2-3: livro XIII, 50–53 (o sétimo dia)', 'XIII, 35, 50 – 38, 53'),
}


def main(cap):
    if cap not in MAPA:
        print(f'Confissões: nada sobre Gn {cap} (só os livros XI–XIII comentam Gn 1–2,3).')
        return
    livros, filtro, cobre, passagem = MAPA[cap]
    A.obra_por_livros(cap, 'gen-agostinho-confissoes.py', 'agostinho-confissoes.md',
                      'Santo Agostinho, Confessiones', 'Confessiones', 'confessioni', 'conf_{:02d}_libro.htm',
                      livros, 7270, 'PL 32', cobre, passagem, filtro)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    main(int(sys.argv[1]))
