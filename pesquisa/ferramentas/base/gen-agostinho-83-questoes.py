"""Santo Agostinho, De diversis quaestionibus LXXXIII (PL 40, 11–100): as questões sobre o Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-83-questoes.py <capítulo>   (1 ou 6)

Grava pesquisa/genesis/<ccc>/base/agostinho-de-diversis-quaestionibus-83.md:
  - Gn 1: q. 51 (o homem feito à imagem e semelhança de Deus) e q. 74 (imagem, igualdade e semelhança, a
    propósito de Cl 1,15);
  - Gn 6: q. 52 («Paenitet me hominem fecisse», Gn 6,6).
Texto: augustinus.it (`latino/ottantatre_questioni/ottantatre_questioni_libro.htm`, uma página só);
colunas pelo Corpus Corporum, texto 7400.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402

MAPA = {1: ((51, 74), 'Gn 1,26-27', 'q. 51 e q. 74'), 6: ((52,), 'Gn 6,6', 'q. 52')}


def main(cap):
    if cap not in MAPA:
        print(f'83 questões: nada sobre Gn {cap}.')
        return
    qs, cobre, passagem = MAPA[cap]
    A.obra_por_livros(cap, 'gen-agostinho-83-questoes.py', 'agostinho-de-diversis-quaestionibus-83.md',
                      'Santo Agostinho, De diversis quaestionibus LXXXIII', 'De diversis quaestionibus octoginta tribus',
                      'ottantatre_questioni', 'ottantatre_questioni_libro.htm', [1], 7400, 'PL 40', cobre, passagem,
                      lambda lv, r: r[1] in qs)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    main(int(sys.argv[1]))
