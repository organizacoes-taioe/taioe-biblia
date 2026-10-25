"""Severiano de Gábala no Gênesis: o sermão sobre «Viu Deus tudo o que tinha feito, e eis que era muito bom» (Gn 1,31),
que a PG dá entre os espúrios de Crisóstomo (PG 56, 519–522) e a khazarzar põe sob Severiano.

    python3 -I pesquisa/ferramentas/base/gen-gregos-severiano.py [capítulos]      (padrão: 1)

Baixa UMA vez o PDF «Severianus_PG 65/In Genesim.pdf» (texto da PG; «56.520» -> «[PG 56, 520]»; apagado depois da conversão).
As seis homilias de Severiano sobre a criação (In mundi creationem, PG 56, 429–500, também entre os espúrios de Crisóstomo)
NÃO estão na khazarzar: ficam como pista para Gn 1 (procurar a PG 56 no archive.org).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
URL = G.khz('Severianus_PG 65', 'In Genesim.pdf')


def main():
    for cap in G.capitulos():
        if cap != 1:
            G.ausente(cap, 'Severiano de Gábala, sermão sobre «muito bom» (PG 56, 519–522): só Gn 1,31.')
            continue
        t = G.texto_pdf(URL, 'severiano-in-genesim')
        campos = {
            'Autor': 'Severiano de Gábala (fl. c. 400), atribuído (na PG, entre os espúrios de São João Crisóstomo)',
            'Obra': 'Sermão sobre «Viu Deus tudo o que tinha feito, e eis que era muito bom» (In Genesim sermo 1)',
            'Passagem': 'o sermão inteiro',
            'Edição': 'PG 56, 519–522',
            'Fonte': URL,
            'Cobre': 'v. 31 (nada mau saiu de Deus; os animais não são maus, o homem é que se rebaixa imitando a fera)',
            'Oriental': 'sim',
            'Língua': 'grc',
        }
        G.gravar(1, 'severiano-sermo-valde-bona', 'Severiano de Gábala (atribuído), sermão sobre «muito bom»', campos,
                 G.paragrafos(t), None, SCRIPT)
        G.pista(1, 'Severiano de Gábala, In mundi creationem orationes 1–6 (PG 56, 429–500, entre os espúrios de Crisóstomo): as '
                   'homilias dele sobre os seis dias; não estão na khazarzar (procurar a PG 56 no archive.org, '
                   'https://archive.org/details/patrologiaecursu0056mign).')
    G.registrar()


if __name__ == '__main__':
    main()
