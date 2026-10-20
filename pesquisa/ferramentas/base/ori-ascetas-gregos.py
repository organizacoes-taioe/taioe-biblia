"""Pré-pesquisa: ascetas e São Máximo Confessor (texto grego da PG via khazarzar) nos capítulos-alvo.
Grava <livro>/<ccc>/base/<autor>-<obra>.md.

Uso (da pasta biblia/):
    python -I -X utf8 pesquisa/ferramentas/base/ori-ascetas-gregos.py [--txt PASTA_DOS_TXT]

Os textos vêm dos PDFs do khazarzar já convertidos por gregos-limpar.py (ver fontes/gregos.md, «Textos já
convertidos»): Maximu__PG_91AGI.txt (Mistagogia, Capítulos), Maximu__PG_91A_2.txt (Ad Thalassium),
Macari__Homiliae spirituales 50.txt. Se a pasta temporária tiver sumido, baixar de novo:
  khazarzar «Maximus Confessor_PG 90-91/PG_91AGI.pdf», «PG_91A_2.pdf»; «Macarius of Egypt_PG 34/Homiliae spirituales 50.pdf».
Os achados vieram de ori-buscar-gregos.py (n-gramas dos versículos). Cada corte vai de uma frase de
início a uma frase de fim, conferidas à mão; as colunas da PG foram conferidas no OCR do archive.org
(PG 90 = bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1860_90; PG 34 = …_1860_34).
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_gregos_comum as O

TXT_PADRAO = os.path.normpath(os.path.join(O.RAIZ, '..', '..', '..', '..', '94b210f9-de88-4ff1-a06d-f01e9346d6d5',
                                           'scratchpad', 'g12', 'txt'))
SCRIPT = 'pesquisa/ferramentas/base/ori-ascetas-gregos.py'
KHZ_MAX = 'https://khazarzar.skeptik.net/pgm/PG_Migne/Maximus%20Confessor_PG%2090-91/'
KHZ_MAC = 'https://khazarzar.skeptik.net/pgm/PG_Migne/Macarius%20of%20Egypt_PG%2034/'

MAXIMO = 'São Máximo, o Confessor (c. 580–662), monge, santo'
MACARIO = ('São Macário, o Egípcio (c. 300–391), sob cujo nome correm as Homilias espirituais; o autor é um '
           'monge sírio dos séc. IV–V («Pseudo-Macário»), lido no Oriente como São Macário')

ITENS = [
    dict(livro='2corintios', cap=4, arquivo='maximo-ad-thalassium', fonte_txt='Maximu__PG_91A_2.txt',
         titulo='São Máximo, o Confessor, Quaestiones ad Thalassium',
         ini='Ὅπερ ἐκ τοῦ παθεῖν τῇ πείρᾳ μαθὼν', fim='ἡ πρὸς τὰ ἔθνη χάρις τῆς προφητείας', ate_ponto=True,
         campos=[('Autor', MAXIMO), ('Obra', 'Quaestiones ad Thalassium (Perguntas a Talássio), q. 64, sobre Jonas'),
                 ('Passagem', 'q. 64: Paulo e Jonas, «tesouro em vasos de barro» e «a morte de Jesus no corpo»'),
                 ('Edição', 'PG 90, 693–785 (q. 64 começa na c. 697; o trecho fica na segunda metade; coluna exata não conferida). '
                  'Texto digital da PG (khazarzar, «ΑΠΑΝΤΑ ΜΑΞΙΜΟΥ»; os marcadores «14Γ_314» são páginas dessa edição grega)'),
                 ('Fonte', KHZ_MAX + 'PG_91A_2.pdf'),
                 ('Cobre', '2Cor 4,7–12 (citados e lidos: o tesouro = a palavra da graça; o vaso de barro = o corpo passível '
                  'ou a fala simples do Apóstolo; a morte que age nos pregadores e a vida nos gentios, prefigurada em Jonas)')]),
    dict(livro='2corintios', cap=4, arquivo='maximo-mistagogia', fonte_txt='Maximu__PG_91AGI.txt',
         titulo='São Máximo, o Confessor, Mistagogia',
         ini='S. Πῶς καὶ ποίῳ τρόπῳ ἄνθρωπος λέγεται', fim='μηδεμίαν πρὸς αὐτὰ σχετικῆς δυνάμεως τὴν οἱανοῦν ἔμφασιν ἔχων.',
         campos=[('Autor', MAXIMO), ('Obra', 'Mystagogia (Mistagogia), cap. 6: «Como e de que modo também a santa Escritura se chama homem»'),
                 ('Passagem', 'cap. 6 inteiro'),
                 ('Edição', 'PG 91, 684–685 (colunas pela ordem da Mistagogia na PG 91, 657–717; não conferidas no OCR). '
                  'Texto digital da PG (khazarzar, «ΑΠΑΝΤΑ ΜΑΞΙΜΟΥ»; «14__086» = página dessa edição grega)'),
                 ('Fonte', KHZ_MAX + 'PG_91AGI.pdf'),
                 ('Cobre', '2Cor 4,16 («o homem exterior se corrompe, o interior se renova»), aplicado à Escritura: a letra '
                  'passa, o espírito cresce')]),
    dict(livro='salmos', cap=42, arquivo='maximo-capitulos-teologicos', fonte_txt='Maximu__PG_91AGI.txt',
         titulo='São Máximo, o Confessor, Capítulos teológicos e econômicos',
         ini='[PG 2, 77] (οζ΄) Ἕως ἡ ψυχή', fim='κατά σύγκρασιν γινομένη διηνεκής μυστική δοξολογία.', depois=330000,
         campos=[('Autor', MAXIMO), ('Obra', 'Capita theologica et oeconomica (Capítulos sobre a teologia e a economia), centúria II, 77–78'),
                 ('Passagem', 'II, 77–78 (o marcador «[PG 2, 77]» do texto limpo é centúria e capítulo, não coluna)'),
                 ('Edição', 'PG 90, 1161–1164 (conferido no OCR do archive.org; latim de Combefis ao lado)'),
                 ('Fonte', KHZ_MAX + 'PG_91AGI.pdf'),
                 ('Cobre', 'Sl 41(42),5 LXX («passarei ao lugar da tenda admirável, até a casa de Deus, com voz de júbilo e '
                  'louvor, ruído de festa»), versículo por versículo; II, 77 junta Sl 119,6 e 2Cor 3,18 («de glória em glória»)')]),
    dict(livro='2corintios', cap=5, arquivo='macario-homilias-espirituais', fonte_txt='Macari__Homiliae%20spirituales%2050.txt',
         titulo='São Macário, o Egípcio, Homilias espirituais',
         ini='ὁ γὰρ μακάριος ἀπόστολος Παῦλος περὶ τούτου τοῦ ἐπουρανίου θησαυροῦ', fim='ἀγαλλίασις, χαρά, εἰρήνη, ἄμφιον, ζωὴ αἰώνιος.',
         campos=[('Autor', MACARIO), ('Obra', 'Homiliae spirituales 50 (Homilias espirituais), homilia 5'),
                 ('Passagem', 'hom. 5, no fim (a casa não feita por mãos; o «mês Xântico» da ressurreição)'),
                 ('Edição', 'PG 34, c. 512–516 (hom. V; colunas pelo OCR do archive.org, aproximadas). O texto digital do '
                  'khazarzar segue a ed. Dörries–Klostermann–Kroeger (PTS 4, 1964), muito próxima da PG: antes de publicar, '
                  'conferir com a PG 34 (domínio público)'),
                 ('Fonte', KHZ_MAC + 'Homiliae%20spirituales%2050.pdf'),
                 ('Cobre', '2Cor 5,1–4 (a tenda terrestre, a casa eterna, «revestidos, não nus», «o mortal absorvido pela vida»), '
                  'com 2Cor 4,11 e Rm 8,11')]),
]


def cortar(t, it):
    i = t.find(it['ini'], it.get('depois', 0))
    if i < 0:
        raise SystemExit(f'início não achado: {it["arquivo"]}')
    j = t.find(it['fim'], i)
    if j < 0:
        raise SystemExit(f'fim não achado: {it["arquivo"]}')
    j += len(it['fim'])
    if it.get('ate_ponto'):
        j = t.find('.', j) + 1
    return t[i:j].strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--txt', default=TXT_PADRAO)
    a = ap.parse_args()
    for it in ITENS:
        t = open(os.path.join(a.txt, it['fonte_txt']), encoding='utf-8').read()
        corpo = cortar(t, it)
        campos = it['campos'] + [('Oriental', 'sim'), ('Língua', 'grc'), ('Baixado', f'{O.HOJE}, por {SCRIPT}')]
        p = O.gravar(it['livro'], it['cap'], it['arquivo'], it['titulo'], campos, corpo)
        print('gravado', p, len(corpo), 'caracteres')


if __name__ == '__main__':
    main()
