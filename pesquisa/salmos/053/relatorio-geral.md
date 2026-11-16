# Salmo 53 (52 da Vulgata e da LXX): relatório da pesquisa (p53)

Pesquisa de 2026-11-16. Todos os grupos. Resultado: **18 excertos** em `achados-geral.json`
(9 de relevância 3, 9 de relevância 2), de 10 autores, cobrindo os vv. 2, 3, 4, 5, 6 e 7. O v. 1 (título)
não tem excerto. O salmo é quase igual ao Sl 14 (13 na Vulgata); por isso os Padres o remetem a ele.

## Numeração

- Os `versiculos` seguem a numeração hebraica (a do nosso texto, em que o título é o v. 1). A Vulgata
  tem um a menos: Vg 1 = hebr. 2 (o insensato), Vg 5 = hebr. 5, Vg 6 = hebr. 5c–6a («ibi timuerunt»),
  Vg 7 = hebr. 6b («ossa»), Vg 8 = hebr. 7. A `passagem` dos achados dá a numeração do autor.
- O título é «pro Maeleth» (Vg: «pro Amalech» em Cassiodoro e Bruno de Segni).

## O que entrou

| autor | obra e passagem | v. | tema |
|---|---|---|---|
| Santo Anselmo | *Proslogion* 2 | 2 | até o insensato entende «aquilo de que nada maior se pode pensar» |
| Santo Anselmo | *Proslogion* 3 | 2 | Deus existe de tal modo que não se pode pensar que não exista |
| Santo Anselmo | *Proslogion* 4 | 2 | dizer no coração (a palavra) × entender o que Deus é; a ação de graças |
| São Tomás | *Postilla* n. 1 | 2 | Deus é evidente em si, não para nós; nega Deus quem nega a providência |
| Santo Agostinho | *Enarr.* 52, 2 | 2 | quem pensa que Deus aprova o seu pecado nega Deus |
| Santo Agostinho | *Enarr.* 52, 7 | 5 | o pão: devorar o povo sem trégua |
| Santo Agostinho | *Enarr.* 52, 8 | 5 | invocar = chamar para dentro de si; Deus enche o peito, não o cofre |
| Santo Hilário | *Tract.* 52, 2 | 2 | o insensato diz só no coração porque teria vergonha de dizê-lo |
| Santo Hilário | *Tract.* 52, 5 | 3 | o olhar de Deus do céu: Noé, Abraão, Isaac, Jacó, Moisés, os profetas |
| Santo Hilário | *Tract.* 52, 8 | 4 | primeiro inúteis, depois desviados; Adão se esconde |
| Santo Hilário | *Tract.* 52, 14 | 6 | temer o que não se deve: os reis, o ladrão e a febre |
| Cassiodoro | *Expositio*, Vg 7 | 6 | o justo desagrada a si mesmo; o pecador ama o que o perde |
| São Tomás | *Postilla* n. 7 | 6 | agradar aos homens: quando é mau e quando é bom |
| São Gregório de Nissa | *In inscr. Ps.* II, 12 (a) | 2, 4 | a corrupção como queda do ser; o vaso rejeitado |
| São Gregório de Nissa | *In inscr. Ps.* II, 12 (b) | 6, 7 | o medo dos que têm horror à água |
| Eusébio de Cesareia | *Comm. in Ps.* 52 | 2 | as sementes do conhecimento de Deus nas noções comuns |
| Teodoreto de Ciro | *Interp. in Ps.* 52, v. 7 | 7 | alegria plena só com a volta dos outros cativos; chorar com os que choram |
| São Bruno de Segni | *Expositio*, Vg 8–9 | 7 | Jacó (esta vida) e Israel (a outra: ver a Deus) |

Agostinho tem 3 dos 18 (17%).

## Conferência dos originais

Todo `original` foi extraído por script (`~/.cache/taioe-sl48-57/p53/lib.py`, `sl53.py`) dos textos
de `base/` e do *Proslogion* baixado: cada trecho é substring exata do texto guardado, depois de tirar
as marcas de coluna (`[col. 325A]`), de página (`[PG 80, 1264]`), os asteriscos de itálico e as quebras
de linha. Correções deliberadas, só de digitação ou OCR da fonte:
- Anselmo: «alium intelligere rem esse» → «aliud»; omitida a referência editorial «[Ps 13,1; 52,1]».
- Agostinho: «si iustus est displicet, ei iniustitia» → «si iustus est, displicet ei iniustitia».
- Hilário: «praeficitet» → «praeficit et».
- Gregório de Nissa: «διέφθει ρενἔξω» → «διέφθειρεν ἔξω» (OCR partido).
- Bruno de Segni: «exsulvabit» → «exsultabit»; tirado o número de página «407», o «»» solto e o «« » do
  versículo de João.
Os de Hilário, Cassiodoro, Bruno de Segni e Tomás vêm de textos já guardados em `base/` (mlat.uzh.ch e
Corpus Thomisticum); Anselmo está em `textos/anselmo-proslogion-02-04.md`.

## Observações para a seleção

- **Cassiodoro** lê «ossa hominum sibi placentium» («os que agradam a si mesmos»), diferente do nosso texto
  («os que agradam aos homens», que é o da LXX e o de Tomás e Hilário). O excerto fala da leitura dele.
- **Gregório de Nissa**, **Eusébio** e **Teodoreto** são orientais (Eusébio é escritor eclesiástico, não é santo).
- **Tomás** n. 1 responde a Anselmo (a «objeção» do *Proslogion*): os dois excertos conversam.

## O que não existe ou não se achou (não procurar de novo)

- **Basílio, Crisóstomo, Ambrósio** e as catequeses de João Paulo II e Bento XVI: nada sobre o Sl 53
  (`base/_ausentes-*.md`). Catecismo e Josemaria Escrivá: nenhum ponto cita o salmo.
- Bruno, o Cartuxo, Belarmino, Afonso, Atanásio e Cirilo foram lidos: comentam o salmo pelo Sl 14 ou
  ficam no esquema de Agostinho e Cassiodoro; sem excerto próprio. Arnóbio, Haimo, Pedro Lombardo,
  pseudo-Beda, pseudo-Jerônimo e Orígenes (*Selecta*) só foram folheados (compilações, pelo catálogo). Belarmino explica o «ossa… qui hominibus placent» pelo hebraico
  («os que te sitiavam», de *chonach*, lido como *chonaph*, «hipócrita»), interessante mas técnico.
- Atanásio, glosa do v. 4 («não é exagero: nada na Escritura se diz por exagero, mas tudo com verdade»):
  boa frase, curta demais para entrar sozinha.

## Para outros capítulos

- O Sl 14 (13 da Vulgata) tem o mesmo texto e os mesmos comentários: o *Proslogion*, Tomás n. 1 e Hilário
  (Tract. 13) podem servir lá, mas **os excertos de Anselmo, Tomás e Hilário aqui são o que o `conferir`
  tomará como repetidos**: usar outros trechos no Sl 14.
- Hilário, *Tract.* 52, 12 (a «bonitas» do homem é mutável, a de Deus não; Moisés, Aarão, Pedro): uma
  página sobre «não há quem faça o bem», útil ao Sl 14 ou a Rm 3.
