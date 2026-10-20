"""Grava, por capítulo de Números, base/_ausentes-numeros.md (quem não comenta o capítulo) e base/_pistas-numeros.md (onde ainda procurar).

    python -I -X utf8 pesquisa/ferramentas/base/pistas-ausentes-num.py       (rodar DEPOIS dos scripts lat-*-num.py, grc-*-num.py, sir-*-num.py)

- Ausentes: (a) afirmações gerais que os relatórios de Nm 12–15 confirmaram (Crisóstomo não comentou Números etc.); (b) para cada obra da
  lista do pedido, a falta de um arquivo `base/<obra>.md` no capítulo, com o motivo (a obra não tem trecho sobre ele: conferido no texto baixado
  em 2026-10-20; para as obras cortadas por palavras-chave — De adoratione, Procópio, Efrém —, «o corte automático não achou», o que é menos firme).
- Pistas: o que os catálogos por grupo (`pesquisa/fontes/*.md`) e os relatórios de Nm 12–15 apontam para o capítulo e ainda não está em `base/`;
  o texto da pista diz de onde veio. O método geral de busca (Corpus Thomisticum, Index scripturaire etc.) está em `pesquisa/fontes/numeros.md`.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C

GERAIS = [
    'Crisóstomo: não comentou Números nem Êxodo (só o Gênesis, homilias e sermões); só citações de passagem (relatório de Nm 12, gregos).',
    'Santo Efrém: não há comentário autêntico a Números (só Gênesis e Êxodo); o «comentário» da ed. romana de Assemani vem de cadeias siríacas (ver base/efrem-in-numeros.md onde houver).',
    'Beda: não comentou Números; o «In Pentateuchum» (PL 91) e as «Quaestiones super Numeros» (PL 93) são espúrios (relatório de Nm 12, latinos).',
    'São Gregório Magno: nenhum comentário a Números; só citações (Moralia, homilias) e os excertos de Paterius (ver base/paterio-expositio-numeros.md onde houver).',
    'São Tomás de Aquino e São Roberto Belarmino: não comentaram Números (só citações em outras obras; relatórios de Nm 12–14, modernos).',
    'Basílio, Nazianzeno, Atanásio, Dídimo, Epifânio, Macário, Máximo, Damasceno: sem comentário a Números (relatórios de Nm 13–14, gregos).',
    'Fílon (não cristão) e Apolinário (herético): não usar (relatórios de Nm 12, gregos).',
]

# obra -> (nome, nome do arquivo em base/, motivo da ausência)
OBRAS = [
    ('Rábano Mauro, Enarrationes in librum Numerorum', 'rabano-enarrationes-numeros', 'a obra cobre todos os capítulos; se falta, o corte falhou'),
    ('Santo Isidoro, Quaestiones in VT, In Numeros', 'isidoro-quaestiones-in-numeros',
     'o In Numeros de Isidoro é a Praefatio e as 42 mansões de Nm 33; só alguns capítulos de Números têm parágrafo (a mansão XII cobre Nm 1–10, a XV Nm 13–19, a XLII Nm 22–36); sobre este capítulo não há trecho'),
    ('pseudo-Beda, Quaestiones super Numeros', 'pseudobeda-quaestiones-super-numeros', 'a obra tem 29 capítulos curtos, copiados de Isidoro, sem episódio deste capítulo'),
    ('Ruperto de Deutz, De Trinitate: In Numeros', 'ruperto-in-numeros', 'Ruperto não tem capítulo sobre este capítulo de Números'),
    ('São Bruno de Segni, Expositio in Numeros', 'bruno-expositio-in-numeros', 'Bruno não comenta este capítulo (Nm 26 não tem capítulo; Nm 32, 34 e 36: «omittitur» no texto)'),
    ('Hugo de São Vítor, Adnotationes in Pentateuchon', 'hugo-adnotationes-in-pentateuchon', 'Hugo deixou só quatro notas sobre Números (Nm 14, 18, 21 e 24); o texto acaba com «Reliqua enim desideramus»'),
    ('Paterius, Expositio (excertos de Gregório)', 'paterio-expositio-numeros', 'Paterius não tem excerto de Gregório sobre este capítulo (o livro IV salta de Nm 11 a 16 e acaba em Nm 35)'),
    ('Santo Agostinho, Quaestiones in Heptateuchum IV', 'agostinho-quaestiones-in-heptateuchum-4', 'Agostinho não tem questão sobre este capítulo nas Quaestiones IV'),
    ('Santo Agostinho, Locutiones in Heptateuchum IV', 'agostinho-locutiones-in-heptateuchum-4', 'sem entrada sobre este capítulo nas Locutiones IV (só gramática)'),
    ('Orígenes, Homiliae in Numeros', 'origenes-homilias-in-numeros', 'Orígenes não tem homilia sobre este capítulo (28 homilias; saltam Nm 5–10, 19–20, 35 e 36)'),
    ('Cornélio a Lápide, Commentaria in Numeros', 'lapide-commentaria-in-numeros', 'a obra cobre todos os capítulos; se falta, o corte falhou'),
    ('Teodoreto, Quaestiones in Numeros', 'teodoreto-quaestiones-in-numeros', 'Teodoreto não tem pergunta sobre este capítulo (51 perguntas, de Nm 1 a 36, com lacunas)'),
    ('São Cirilo de Alexandria, Glaphyra in Numeros', 'cirilo-glaphyra-in-numeros', 'os Glaphyra tratam em Números só de Nm 12, 13–14, 15,17–29, 19 e 21,6–9'),
    ('São Cirilo de Alexandria, De adoratione', 'cirilo-de-adoratione-numeros', 'o corte automático (4-gramas da LXX + palavras-chave) não achou fala do diálogo que cite este capítulo; alusões podem existir'),
    ('Procópio de Gaza, Commentarii in Numeros', 'procopio-commentarii-in-numeros', 'o corte por palavras-chave não atribuiu texto da catena a este capítulo (atribuição aproximada)'),
    ('Santo Efrém (atribuído), Explanatio in Numeros', 'efrem-in-numeros', 'o corte por palavras-chave não atribuiu texto da explicação a este capítulo (atribuição aproximada)'),
    ('São Gregório de Nissa, Vida de Moisés', 'nissa-vida-de-moises', 'a Vida de Moisés não trata deste capítulo (I, 61–76 e II, 256–304 passam só por Nm 11–25)'),
]
EXTRAS = {}
# Nm 1: Bruno, Rábano… todos presentes; Nm 12–16 não são deste levantamento.

PISTAS_GERAL = ('Método para o que não está em base/: ver `pesquisa/fontes/numeros.md` (Corpus Thomisticum «Num. N», Index scripturaire de Francisco de Sales, Clerus, '
                'Lecionário e Ofício das Leituras, varredura dos Papas, Santo Antônio de Pádua, Glosa Ordinária).')

PISTAS = {
    1: ['Catecismo da Igreja Católica: cita Nm 1 (o CIC só cita Números nos caps. 1, 7, 11, 12, 21, 24 e 28; conferir o § no índice de citações bíblicas; relatório de Nm 13, modernos).'],
    6: ['Liturgia: Nm 6,22-27 é a 1ª leitura da Missa de 1º de janeiro (Santa Maria, Mãe de Deus) (catholic-resources.org, Index-Pentateuch.htm; relatório de Nm 15, liturgia).',
        'Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 6 (relatório de Nm 15, modernos; as referências vêm como «(Num 6, …)»).'],
    7: ['Catecismo da Igreja Católica: cita Nm 7 (relatório de Nm 13, modernos).'],
    8: ['Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 8 (relatório de Nm 15, modernos).'],
    9: ['«Νόμος εἷς ἔσται» (Nm 9,14, a Páscoa e o prosélito): Cirilo, De adoratione XVII (PG 68, 1081); Pseudo-Crisóstomo, In sanctum pascha sermo 6 (espúrio, não usar) (relatório de Nm 15, gregos).'],
    10: ['Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 10 (relatório de Nm 15, modernos).'],
    11: ['Liturgia: Nm 11,4b-15 e 11,25-29 na Missa (Lecionário de 1981); Ofício das Leituras (ciclo anual): Nm 11,4-6.10-30 na quarta-feira da 4ª semana da Quaresma (relatórios de Nm 14–15, liturgia).',
         'Papa Francisco: a «nostalgia do Egito» e a murmuração aparecem em Santa Marta de 24/03/2015, 20/03/2018 e 09/04/2019 e no Te Deum de 31/12/2014 (com Nm 11,5), sempre sobre Nm 11 e Nm 21 (relatório de Nm 14, modernos; textos no vatican.va em italiano).',
         'São João da Cruz (obras completas em espanhol, DCO): cita Nm 11 (relatório de Nm 14, modernos).',
         'Catecismo da Igreja Católica: cita Nm 11 (relatório de Nm 13, modernos).',
         'Teodoreto, Interpretatio in Psalmos, Sl 77, 94 e 105 (LXX): relembram o deserto; procurar ali os episódios de Nm 11, 14, 20, 21 e 25 (acréscimos de Nm 14, gregos).'],
    17: ['Seção «Para Nm 17» do pedido de Nm 16: o que os Padres dizem de Nm 16,36–50 (Vulgata e LXX) é do nosso capítulo 17: os turíbulos batidos em lâminas para o altar, a murmuração do dia seguinte, a praga e Aarão entre os mortos e os vivos com o turíbulo (16,46-48 Vulg. = 17,11-13); o cap. 17 deles (a vara que floresce) é o nosso 17,16-28 (pedido de Nm 16).',
         'Pedido de Nm 16, «pistas fortes» que valem também para Nm 17: Cipriano, De unitate 18 e Ep. 3, 67, 69, 73; Firmiliano (Ep. 75 do epistolário de Cipriano); Optato I; Ambrósio (De officiis II; Expositio in Ps. 118); Jerônimo (Dialogus contra Luciferianos); Gregório Magno (Regula pastoralis, Moralia, Hom. in Ez.); Clemente Romano 1 Cor 4,12 e 51,3–4; Ireneu IV, 26, 2 e IV, 18, 3; Nazianzeno Or. 2 e 32; Constituições Apostólicas II e VI; Didascalia.',
         'São João da Cruz (obras completas em espanhol, DCO): cita Nm 17 (relatório de Nm 14, modernos).',
         'Liturgia: o Ofício das Leituras (ciclo anual) salta os caps. 15–19 de Números (relatório de Nm 15, liturgia); Hb 5,4 («ninguém se atribui essa honra, senão quem é chamado por Deus, como Aarão») e Sl 106,16–18 (pedido de Nm 16).'],
    18: ['Francisco de Sales, Index scripturaire (t. XXVII): conferir a entrada «Nombres XVIII» (o índice dá o tomo e a página de cada citação; método em fontes/modernos.md § 11).'],
    19: ['Liturgia: o Ofício das Leituras (ciclo anual) salta os caps. 15–19 de Números (relatório de Nm 15, liturgia).'],
    20: ['Missal antigo (1570–1962): Nm 20 é a única perícope de Números da Missa (sexta-feira da 3ª semana da Quaresma, `Tempora/Quad3-5` do Divinum Officium); Lecionário de 1981: Nm 20,1-13 (relatórios de Nm 12 e 15, modernos e liturgia).',
         'Ofício das Leituras (ciclo anual): Nm 20,1-13 e 21,4-9 no sábado da 4ª semana da Quaresma (relatório de Nm 15, liturgia).',
         'Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 20 (relatório de Nm 15, modernos).',
         'São Jerônimo, Ep. 78 a Fabíola (De XLII mansionibus, PL 22, 698–724): as mansões Cades e monte Hor (fontes/latinos.md § 4).'],
    21: ['Liturgia: Nm 21,4b-9 na Missa (Lecionário de 1981) e no Ofício das Leituras (sábado da 4ª semana da Quaresma) (relatórios de Nm 14–15, liturgia).',
         'Papa Francisco: Santa Marta (24/03/2015, 20/03/2018, 09/04/2019) sobre a murmuração e a serpente (relatório de Nm 14, modernos).',
         'Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 21 (relatório de Nm 15, modernos).',
         'Catecismo da Igreja Católica: cita Nm 21 (relatório de Nm 13, modernos).',
         'Eusébio, Onomasticon (khazarzar, pasta de Eusébio): verbetes com a referência bíblica, úteis para os lugares de Nm 21 e 33 (acréscimos de Nm 13, gregos).',
         'Teodoreto, Interpretatio in Psalmos, Sl 77, 94 e 105 (LXX): o deserto (acréscimos de Nm 14, gregos).'],
    22: ['São João da Cruz (obras completas em espanhol, DCO): cita Nm 22 (relatório de Nm 14, modernos).'],
    23: ['Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 23 (relatório de Nm 15, modernos).'],
    24: ['Liturgia: Nm 24,2-7.15-17 na Missa (Lecionário de 1981; Advento) (relatório de Nm 15, liturgia).',
         'Catecismo da Igreja Católica: cita Nm 24 (relatório de Nm 13, modernos).',
         'Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 24 (relatório de Nm 15, modernos).',
         'Orígenes, Adnotationes in Numeros (PG 17, 24): os mágicos de Balaão e a estrela (já em base/origenes-escolios-gregos-numeros.md).'],
    25: ['Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 25 (relatório de Nm 15, modernos).',
         'Teodoreto, Interpretatio in Psalmos, Sl 105 (LXX): Baal-Fegor (acréscimos de Nm 14, gregos).'],
    26: ['Nm 26,11: os filhos de Coré não morreram, e deles vêm os «filhos de Coré» dos Salmos (pedido de Nm 16).'],
    27: ['Nm 27,16 («Deus dos espíritos de toda carne»; Hb 12,9): Deus autor das almas, a origem da alma nos Padres (pedido de Nm 16).'],
    28: ['Catecismo da Igreja Católica: cita Nm 28 (relatório de Nm 13, modernos).',
         'Cirilo, De adoratione XVII (PG 68, 1081 ss.): as medidas «τέταρτον τοῦ ἵν» e «οἶνον εἰς σπονδήν» são de Nm 28–29 (relatório de Nm 15, gregos).',
         'Pseudo-Atanásio, De sabbatis et circumcisione (PG 28, 136): cita Nm 28 (relatório de Nm 15, gregos).'],
    29: ['Cirilo, De adoratione XVII (PG 68, 1081 ss.): Nm 28–29 (relatório de Nm 15, gregos).'],
    32: ['Orígenes hom. 26 sobre Números (Nm 32: «os dez que foram enviados com Jesus e Caleb»; relatório de Nm 13, Orígenes e Agostinho), já em base/origenes-homilias-in-numeros.md.'],
    33: ['São Jerônimo, Ep. 78 a Fabíola, De XLII mansionibus (PL 22, 698–724; Corpus Corporum, Jerônimo, Epistolae, texto 7132): fonte de Isidoro, Rábano e da Glosa para Nm 33 (fontes/latinos.md § 4).',
         'São Pedro Damião, De quadragesima et XLII mansionibus (Corpus Corporum, texto 10104; PL 145) (fontes/latinos.md § 7).',
         'Orígenes hom. 27 (Nm 33): já em base/origenes-homilias-in-numeros.md; relatório de Nm 14, Orígenes e Agostinho: §§ 4 e 7 (GCS 262, 265).'],
    36: ['Santo Antônio de Pádua, sermões latinos (DCO): cita Nm 36 (relatório de Nm 15, modernos).'],
}

n = 0
for cap in C.CAPS:
    base = os.path.join(C.NUM, f'{cap:03d}', 'base')
    os.makedirs(base, exist_ok=True)
    existentes = {f[:-3] for f in os.listdir(base) if f.endswith('.md') and not f.startswith('_')}
    aus = list(GERAIS)
    for nome, arq, motivo in OBRAS:
        if arq not in existentes:
            aus.append(f'{nome}: {motivo}.')
    with open(os.path.join(base, '_ausentes-numeros.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Ausentes (numeros)\n\nConferido em {C.DATA} (obras da lista do pedido; ver `pesquisa/fontes/numeros.md`).\n\n' + '\n'.join(f'- {l}' for l in aus) + '\n')
    pis = [PISTAS_GERAL] + PISTAS.get(cap, [])
    with open(os.path.join(base, '_pistas-numeros.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('# Pistas (numeros)\n\nCitações do capítulo em outras obras que os catálogos e os relatórios de Nm 12–15 apontam e que ainda não estão em base/.\n\n'
                + '\n'.join(f'- {l}' for l in pis) + '\n')
    n += 1
print(n, 'capítulos')
