# Salmo 40 (39): relatório da pesquisa geral (Padres, medievais, gregos, modernos)

Pesquisa de 2026-11-15 (pesquisador p40, lote dos Sl 38–47). Todos os grupos juntos, a partir de `base/`.
Resultado: **28 excertos** em `achados-geral.json` (16 de relevância 3, 12 de relevância 2), cobrindo os vv. 2–14, 17 e 18.
Textos novos guardados em `textos/`.

## Numeração

- O título é o v. 1 (hebraico = Nova Vulgata). A Vulgata e a LXX leem o Sl 39; os versículos dos Padres vão um abaixo
  (Vulgata v. 1 = «Exspectans exspectavi» = v. 2 nosso), até o v. 6, que Cassiodoro e Belarmino dividem em dois
  («Multa fecisti» e «Annuntiavi et locutus sum»): a partir daí «Vers. N» de Cassiodoro = v. N−1 nosso
  (Vers. 8 = v. 7, Vers. 17 = v. 14, Vers. 21 = v. 17, Vers. 22 = v. 18). A `passagem` dá a numeração do autor; os `versiculos`, a nossa.
- Agostinho numera por parágrafos (n.); Tomás também (n. e [número] do Corpus Thomisticum).
- Os Padres leem «corpus autem perfecisti mihi» (LXX, Hb 10,5); o nosso texto traz «abriste-me os ouvidos» (hebraico, Vulgata
  latina). As traduções seguem o texto que cada Padre leu.

## O que se achou

| autor | obra e passagem | excertos |
|---|---|---|
| Santo Agostinho | *Enarrationes* n. 2, 3, 4, 9, 12, 15 (PL 36) | 6 |
| Cassiodoro | *Expositio*, Vers. 1, 2, 4, 17, 21, 22 (PL 70) | 6 |
| São Tomás de Aquino | *Postilla* n. 2, 5, 6 e *Super Hebraeos* 10, lição 1 | 4 |
| Teodoreto de Ciro | *Interpretatio*, vv. 3-4, 7-9, 13 (PG 80) | 3 |
| São Bruno de Segni | *Expositio*, vv. 6, 10 e 13 (PL 164) | 3 |
| São Josemaria Escrivá | *Amigos de Deus* 133 e *Via-Sacra* II | 2 |
| Santo Ambrósio | *Enarrationes* n. 3 (v. 4) | 1 |
| Santo Atanásio | *Exposições* (cadeia), v. 9 | 1 |
| São Cirilo de Alexandria | *Expositio*, vv. 7-9 | 1 |
| São João Crisóstomo | *In Hebraeos* hom. 18 (Hb 10,5-9) | 1 |

Por versículo:
- v. 2: Agostinho (esperar do Senhor, que adia, não tira a promessa) e Cassiodoro (a paciência no «esperei, esperei»).
- v. 3: Agostinho (o abismo e o clamor que já levanta), Cassiodoro (lodo e rocha), Escrivá (agradecer e pedir perdão).
- v. 4: Teodoreto (cântico novo, hino em vez de lamento), Agostinho («invoca louvando, não repreendendo»), Ambrósio (o cântico novo é o Evangelho, amar os inimigos).
- v. 5: Cassiodoro (a esperança, «pé estável») e Tomás (ver, temer e esperar).
- v. 6: Agostinho (Pedro «andamar» × o artista da corda) e Bruno de Segni (a maior das maravilhas é a humilhação do Verbo).
- vv. 7-9 (Hb 10): Agostinho (sacrifícios como palavras de promessa), Teodoreto (oferecer os membros), Cirilo (o corpo formado na Virgem), Atanásio (a lei escrita no coração), Tomás sobre Hb 10, Crisóstomo sobre Hb 10, Escrivá (Via-Sacra, a vontade do Pai).
- vv. 10-11: Agostinho (lábios e coração), Bruno de Segni (só tenho os lábios), Tomás (o que anunciar).
- v. 12: Tomás (misericórdia e verdade).
- v. 13: Bruno de Segni (o justo acusa a si mesmo) e Teodoreto (a Igreja confessa pecados, como os santos).
- v. 14: Cassiodoro (o olhar de Deus, Pedro olhado por Jesus).
- v. 17: Cassiodoro («Grande é o Senhor», Jó).
- v. 18: Cassiodoro (a pobreza mais rica que todos os tesouros).

## Como se procurou

- Tudo o que está em `base/` foi lido (Agostinho, Ambrósio, Cassiodoro, Tomás, Teodoreto, Atanásio, Cirilo, Bruno de Segni, Bruno Cartuxo,
  Belarmino; Arnóbio, Haimo, Lombardo, pseudo-Beda, pseudo-Jerônimo, Eusébio e Orígenes só por amostragem: compilam os anteriores).
- Os `original` foram extraídos por script das fontes (`/home/geremias/.cache/taioe-sl38-47/p40/`, `lib.py` e `build.py`): cada trecho é
  substring exata do texto de `base/` ou de `textos/`, depois de tirar as marcas de coluna, os asteriscos de citação e os números de
  página; o grego em forma NFC. Correções declaradas: Teodoreto «ἐπέχου σαδρόμον» → «ἐπέχουσα δρόμον» (espaço da conversão do PDF);
  Atanásio «ἐν δοτάτοις» → «ἐνδοτάτοις»; Escrivá, sem a marca de nota `[^16]`; Ambrósio, sem o número de página `872`.
  Nenhuma conferida na imagem da página (os gregos vêm do texto digital do khazarzar, sem OCR; Belarmino, que é OCR, não entrou).
- Fora de `base/`, baixados e guardados em `textos/`: Tomás, *Super Epistolam ad Hebraeos*, cap. 10, lição 1
  (https://www.corpusthomisticum.org/che07.html) e Crisóstomo, *In Hebraeos*, hom. 18 (khazarzar, PG 63).

## O que não existe ou não se achou (não procurar de novo)

- Basílio, Crisóstomo (Salmos), Gregório de Nissa e Hilário não comentaram este salmo (ver `base/_ausentes-*.md`).
- Nenhuma catequese de João Paulo II ou Bento XVI (ciclo de Laudes e Vésperas) trata este salmo; nenhum Papa recente o cita 3 vezes ou mais.
- Escrivá: `Camino` 92 não é do Sl 40 (cita «in meditatione mea exardescit ignis», Sl 38,4); `Es Cristo que pasa` 164 só remete ao v. 9 em nota.
- Orientais siríacos: só pistas, sem leitura (Liber Graduum, Tito de Bostra, Narsai; Dionísio bar Salibi e Isho`dad são proibidos no site).

## Avisos para a seleção

- **Atanásio**: o comentário dado como dele, nesta cadeia, tem a *Hypothesis* marcada «incerto auctore» (PG 27); as glosas dos versículos, no corpo do texto, são de cadeia e de autoria também discutida.
- **Cirilo** e **Teodoreto** dizem coisas próximas nos vv. 7-9 (o Espírito sobre a Virgem; Rm 12,1); ficaram os dois porque as ênfases diferem.
- **Tomás** sobre Hb 10: texto de reportatio (Marietti); o trecho em «cap. 10, lição 1».
- **Escrivá**: «autorizado pelo Opus Dei», com o link do escriva.org.
- Cassiodoro, v. 18 (`pobreza mais rica`), é o mais forte do salmo para a vida cristã; Agostinho, n. 12 («palavras de promessa»), para Hb 10.

## Para outros capítulos

- Tomás, *Hb* 10 e Crisóstomo, *Hb* 18: servem também a Hb 10,5-9 (se houver Bíblia nas Cartas).
- Ambrósio, n. 17 (Judas, osculo, vulnera amici, o bom ladrão) e Agostinho, n. 11 (Cristo esperou em Judas «nos seus membros») estão em `base/` e cabem no Sl 41,10.
- Cassiodoro, Vers. 10 (v. 9: o desejo de fazer a vontade, Sl 1 recolhido); Belarmino, v. 4 («antes cantava cantos velhos dos amores do mundo»; OCR, conferir em Vivès t. X pp. 262ss.).
