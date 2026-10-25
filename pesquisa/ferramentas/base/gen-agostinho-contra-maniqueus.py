"""Santo Agostinho, De Genesi contra Manichaeos I–II (PL 34, 173–220), por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-contra-maniqueus.py <capítulo>   (1, 2 ou 3)

Grava pesquisa/genesis/<ccc>/base/agostinho-de-genesi-contra-manichaeos.md. A primeira obra dele sobre o
Gênesis (388–389), «ad imperitiorum captum»: literal e alegórica, contra as objeções dos maniqueus.
  - Gn 1: livro I, 1, 1 – 21, 32 (até o «bona valde», Gn 1,31);
  - Gn 2: livro I, 22, 33 – 25, 43 (o sétimo dia, Gn 2,2-3, e as seis idades do mundo) e livro II, 1 e 3–19
    (Gn 2,4-25; o II, 1 recita Gn 2);
  - Gn 3: livro II, 2 (a recitação de Gn 3) e 20–43 (Gn 3, a serpente, as penas, a expulsão; 26–29 = epílogo).
Texto: augustinus.it (`latino/genesi_dcm/genesi_dcm_N_libro.htm`); colunas da PL pelo Corpus Corporum, texto 7303.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402

MAPA = {
    1: ([1], lambda lv, r: r[2] <= 32, 'Gn 1,1–31', 'livro I, 1, 1 – 21, 32'),
    2: ([1, 2], lambda lv, r: (lv == 1 and r[2] >= 33) or (lv == 2 and (r[2] == 1 or 3 <= r[2] <= 19)),
        'Gn 2,1–25', 'livro I, 22, 33 – 25, 43; livro II, 1, 1 e 2, 3 – 13, 19'),
    3: ([2], lambda lv, r: r[2] == 2 or r[2] >= 20, 'Gn 3,1–24', 'livro II, 1, 2 e 14, 20 – 29, 43'),
}


def main(cap):
    if cap not in MAPA:
        print(f'De Genesi contra Manichaeos: nada sobre Gn {cap} (a obra cobre Gn 1–3).')
        return
    livros, filtro, cobre, passagem = MAPA[cap]
    A.obra_por_livros(cap, 'gen-agostinho-contra-maniqueus.py', 'agostinho-de-genesi-contra-manichaeos.md',
                      'Santo Agostinho, De Genesi contra Manichaeos', 'De Genesi contra Manichaeos libri duo',
                      'genesi_dcm', 'genesi_dcm_{}_libro.htm', livros, 7303, 'PL 34', cobre, passagem, filtro)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    main(int(sys.argv[1]))
