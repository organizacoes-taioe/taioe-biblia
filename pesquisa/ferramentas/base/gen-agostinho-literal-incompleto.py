"""Santo Agostinho, De Genesi ad litteram imperfectus liber (PL 34, 219–246), por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-literal-incompleto.py <capítulo>   (só 1)

Grava pesquisa/genesis/<ccc>/base/agostinho-de-genesi-ad-litteram-imperfectus.md. Tentativa de comentário
literal (393–394), largada em Gn 1,26; ele a deixou como estava e lhe acrescentou o fim (16, 55–62) ao reler
(Retractationes I, 18). Cobre só Gn 1,1-26: o livro inteiro vai para Gn 1.
Texto: augustinus.it (`latino/genesi_incompiuto/genesi_incompiuto_libro.htm`); colunas pelo Corpus Corporum, texto 7310.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402


def main(cap):
    if cap != 1:
        print(f'De Genesi ad litteram imperfectus liber: nada sobre Gn {cap} (cobre só Gn 1,1-26).')
        return
    A.obra_por_livros(cap, 'gen-agostinho-literal-incompleto.py', 'agostinho-de-genesi-ad-litteram-imperfectus.md',
                      'Santo Agostinho, De Genesi ad litteram imperfectus liber',
                      'De Genesi ad litteram imperfectus liber', 'genesi_incompiuto', 'genesi_incompiuto_libro.htm',
                      [1], 7310, 'PL 34', 'Gn 1,1–26 (o livro inteiro)', 'o livro inteiro, 1, 1 – 16, 62')


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(__doc__)
        sys.exit(1)
    main(int(sys.argv[1]))
