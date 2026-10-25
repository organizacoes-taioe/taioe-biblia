"""Santo Agostinho, De Genesi ad litteram libri XII (PL 34, 245–486), por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-literal.py <capítulo>   (1, 2 ou 3)

Grava pesquisa/genesis/<ccc>/base/agostinho-de-genesi-ad-litteram.md. O grande comentário literal (401–415):
  - Gn 1: livros I (Gn 1,1-5), II (Gn 1,6-19) e III (Gn 1,20-31), inteiros;
  - Gn 2: livros IV (Gn 2,1-3: o sétimo dia, os seis dias, o conhecimento «da tarde» e «da manhã» dos anjos),
    V (Gn 2,4-6), VI–VII (Gn 2,7: o corpo e a alma), VIII (Gn 2,8-17: o paraíso), IX (Gn 2,18-24: a mulher),
    X (a origem da alma) e XI, 1, 1 – 1, 3 (Gn 2,25). Livros longos: o arquivo passa de 400 KB;
  - Gn 3: livro XI, 2, 4 – 42, 60 (a tentação, a queda, as penas). O livro XII (o paraíso de 2Cor 12,2-4,
    as visões) não comenta o Gênesis.
Texto: augustinus.it (`latino/genesi_lettera/genesi_lettera_NN_libro.htm`); colunas pelo Corpus Corporum, texto 7302.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402

MAPA = {
    1: ([1, 2, 3], None, 'Gn 1,1–31', 'livros I, II e III inteiros'),
    2: ([4, 5, 6, 7, 8, 9, 10, 11], lambda lv, r: lv < 11 or r[2] <= 3, 'Gn 2,1–25',
        'livros IV a X inteiros; XI, 1, 1 – 1, 3'),
    3: ([11], lambda lv, r: r[2] >= 4, 'Gn 3,1–24', 'livro XI, 2, 4 até o fim'),
}


def main(cap):
    if cap not in MAPA:
        print(f'De Genesi ad litteram: nada sobre Gn {cap} (a obra cobre Gn 1–3).')
        return
    livros, filtro, cobre, passagem = MAPA[cap]
    A.obra_por_livros(cap, 'gen-agostinho-literal.py', 'agostinho-de-genesi-ad-litteram.md',
                      'Santo Agostinho, De Genesi ad litteram', 'De Genesi ad litteram libri duodecim',
                      'genesi_lettera', 'genesi_lettera_{:02d}_libro.htm', livros, 7302, 'PL 34', cobre, passagem,
                      filtro)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    main(int(sys.argv[1]))
