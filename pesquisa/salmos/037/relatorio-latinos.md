# Salmo 37 (36): relatório da pesquisa nos Padres latinos e nos autores medievais

Pesquisa de 2026-10-20/21. Grupo: Padres latinos (menos Santo Agostinho e Santo Ambrósio, cobertos à
parte), autores medievais, Tomás de Kempis e São Roberto Belarmino. Nos autores é o «Psalmus XXXVI»
(«Noli aemulari in malignantibus»). Resultado: **28 excertos** em `achados-latinos.json` (15 de
relevância 3, 13 de relevância 2), de 12 autores, cobrindo os vv. 1, 3–5, 7, 11–16, 20–21, 23–26, 29,
31, 34–37, 39–40 e o salmo inteiro (conclusão de Cassiodoro). Textos novos guardados em `textos/`.
Onde achar cada obra: `../../fontes/latinos.md`.

## Numeração

- Os `versiculos` estão na numeração hebraica, que neste salmo coincide com a da Vulgata Clementina
  (o título «Psalmus ipsi David» está dentro do v. 1; 40 versículos). As notas de Migne usam a mesma.
- **Cassiodoro e Belarmino** contam 42 versículos: o v. 7 é dividido em dois (Vers. 7 = 7a, Vers. 8 =
  7b «In homine faciente iniquitatem») e o v. 28 também (Vers. 29 = 28ab, Vers. 30 = 28c «Injusti
  punientur…»). Logo: Vers. 1–7 = vv. 1–7; Vers. 9–29 = v. N−1; Vers. 31–42 = v. N−2. A `passagem`
  dá a numeração deles; os `versiculos`, a nossa.
- Tomás não numera (os n. 1–25 do Corpus Thomisticum seguem o texto).

## Conferência dos originais

Todo `original` foi conferido por script (`p-latinos/bin/build.py`, no scratchpad) com o texto
baixado: cada trecho entre «(...)» é substring exata, depois de tirar as notas bíblicas de Migne, as
marcas de coluna, os números de página da edição anterior e os números de parágrafo. Correções
deliberadas, todas de OCR ou digitação: Belarmino «quodest» → «quod est», «obediasin» → «obedias in»;
Bernardo, *Qui habitat* 2, «injustis?Nam» → «injustis? Nam». No Kempis da The Latin Library ficou
«perserveratus» como está no site (deve ser «perseveraturus»). **Belarmino vem de OCR**: conferir com
as imagens de Vivès, t. X, pp. 229–237, antes de publicar; as páginas dadas nos achados são aproximadas.

## O que se achou

| autor | obra e passagem | edição | excertos |
|---|---|---|---|
| São Bernardo | Advento 3, 3; Cântico 11, 2; *Qui habitat* 2, 1–2 e 9, 6 | PL 183 | 4 |
| Cassiodoro | *Expositio*, Vers. 26, 39, 41 e conclusão | PL 70 | 4 |
| São Tomás de Aquino | *Postilla*, n. 2, 8, 11, 12 | Parma t. 14 | 4 |
| São Roberto Belarmino | *Explanatio*, vv. 1, 4, 7 | Vivès t. X | 3 |
| São Gregório Magno | *Moralia* XV, 68; Registrum I, 5; *Hom. in Ez.* II, 9, 8 | PL 75–77 | 3 |
| São Bruno de Segni | *Expositio*, vv. 5, 21, 34 | PL 164 | 3 |
| São Cipriano | *De zelo et livore* 7–8; *De opere et eleemosynis* 19 | PL 4 | 2 |
| São Bento | Regra 7, 44–46 | PL 66 | 1 |
| Tomás de Kempis | *Imitação* I, 25, 2–3 | The Latin Library | 1 |
| Bem-av. Isaac de Stella | Sermão 2 | PL 194 | 1 |
| São Leão Magno | Sermão 71, 6 | PL 54 | 1 |
| São Pedro Damião | *De divina omnipotentia* 4 | PL 145 | 1 |

Por versículo: v. 1 não invejar, compadecer-se e rezar pelos maus (Bernardo) e a «emulação» como
rivalidade de estádio (Belarmino); v. 3 as quatro terras (Tomás) e o «faze agora o que farias»
(Kempis); v. 4 mel no absinto (Bernardo, Cânt. 11) e Deus nega o pequeno para dar o grande
(Belarmino, o espinho de Paulo); v. 5 o quinto grau da humildade (Bento) e começar o bem desejado
(Bruno de Segni); v. 7 «cala-te diante do Senhor» (Belarmino); vv. 11 e 29 a terra = a face de Deus
(Isaac) e as quatro guerras que cessam (Tomás); vv. 12–13 o retrato do invejoso (Cipriano); vv. 14–15
a espada que enferruja na bainha (Tomás); v. 16 os bens como remédio (Tomás); v. 20 a fumaça, na carta
de Gregório recém-eleito papa; v. 21 «mutuum = meum tuum» (Bruno de Segni); vv. 23–24 o chão
movediço (Leão) e o justo que cai sobre a mão de Deus (Bernardo); vv. 25–26 a esmola como herança
dos filhos (Cipriano) e a Igreja que fala de Adão ao fim (Cassiodoro); v. 31 o coração como altar de
pedras quadradas (Gregório); v. 34 Deus vem julgar a teu favor (Bruno de Segni); vv. 35–36 o viajante
que passa (Gregório) e o nada ontológico do ímpio (Pedro Damião); v. 37 guardar a Verdade (Cassiodoro);
v. 39 tribulações que mordem e não devoram (Cassiodoro); v. 40 «porque esperaram nele» (Bernardo);
o salmo como túnica de Cristo tecida de versos (Cassiodoro).

Sem excerto: vv. 2, 6, 8–10, 17–19, 22, 27–28, 30, 32–33, 38 (há material nos comentários, mas
repetido de Agostinho ou fraco).

## Reservas (bons, deixados fora para não repetir; textos em `textos/` ou `base/`)

- São Bernardo, Quaresma 5, 6–7 (PL 183, 180B–D): «Delectare in Domino» não é afeto, é exercício; o
  pai que parte o pão em vez de dar a faca ao filho. Muito bom; ficou fora só porque o v. 4 já tem dois.
- São Bernardo, Cântico 70, 6 (v. 37: o lírio da mansidão, «odor da esperança»); Vida de São
  Malaquias (v. 31: «a lei no coração, e não no códice»).
- João Cassiano, *Coll.* XII, 6 (PL 49, 877A–878B; vv. 11 e 34): a terra que os mansos possuem é o
  próprio corpo; «não diz paz, mas abundância de paz». Bom, mas toca a 4.ª terra de Tomás.
- Santo Hilário, *Tract. in Ps.* 128, 12 (PL 9, 717B; vv. 35–36): a mesma ideia de Gregório
  (o «passei» de Moisés, peregrino do mundo); Gregório é mais claro.
- São Jerônimo, *In Amos* III (PL 25, 1085A; v. 25): mártires morreram de fome, o pão é o do céu;
  *In Amos* I (1009C; vv. 35–36).
- São Máximo de Turim, Sermão 76 (PL 57, 686B–D; vv. 30–31), aplicados a São Cipriano.
- Ricardo de São Vítor, *Benjamin minor* 23–24 (PL 196, 28D; v. 11): «nela não se trabalha, mas
  sem trabalho não se chega a ela».
- Tomás de Kempis, *Imitação* III, 12, 3–4 (vv. 4 e 20) e I, 6, 1 (v. 11).
- Tomás, *Postilla* n. 3 («delitiare»: não te contentes com o necessário, procura as delícias, v. 4),
  n. 16 (os doutores como cambistas da palavra, v. 21), n. 17 («é próprio do viajante cair às vezes»,
  v. 24), n. 19 («inhabita = intus habita», v. 27), n. 23 («a espera é para os males, a guarda para os
  bens», v. 34), n. 24 («por isso os santos são tidos por soberbos», v. 36).
- Belarmino: v. 13 («o pecador mata a própria alma antes de matar o corpo do justo»), v. 15 («ao
  despojar o justo do manto, despoja-se da fé»), vv. 35–36 («onde estão os impérios da Assíria, da
  Pérsia, da Grécia e de Roma?»).
- Bruno, o Cartuxo (v. 15): pede que o arco se quebre, mas não a espada, que coroa os mártires.
  Arnóbio (v. 3): «habita a terra, isto é, o teu corpo: os olhos, os ouvidos, a boca, as mãos…».
- Cassiodoro: v. 3 («alimento que, quanto mais sacia, mais aumenta a fome feliz»), v. 20 (a fumaça),
  v. 21, v. 24 (a queda é cair nas mãos dos perseguidores), v. 26 («não deixa de dar quem está
  acostumado a receber de Cristo»), v. 36 (os dois modos de passar o mundo).
- Haimo (v. 4): no começo o Senhor parece duro; depois que se acostuma, é a maior delícia.
- São Gregório, *Moralia* (PL 75, 793A; v. 10, de passagem) e Paterius (PL 79, 840D, que só traz o trecho dos vv. 35–36).

## O que não existe ou não se achou (não procurar de novo)

- **Santo Hilário não comentou o Sl 36** (só a citação do *Tract. in Ps.* 128, acima). **São Gregório
  Magno** não comentou os Salmos (as *Expositio in VII psalmos poenitentiales* são espúrias; citam o
  v. 6). **São Jerônimo**: nenhum *Tractatus* sobre o Sl 36 nas séries de Morin; em *In Isaiam* XVI
  (PL 24, 586C) diz que o Sl 36 «pede um volume próprio», que não escreveu.
- **São Leão Magno**: só o Sermão 71. **São Cesário de Arles**: os sermões estão na PL 39 como
  «Sermones supposititii» de Agostinho (textos 7336–7340, varridos): só citações soltas (vv. 1–2, 9,
  20, 35–36), nenhuma explicação. **Valeriano de Cimiez**, **Zenão de Verona**, **Fausto de Riez**,
  **Columbano**, **Ildefonso**, **Eucherio**: citações de passagem.
- **São Bento**: só a Regra 7 (v. 5); o comentário de Smaragdo à Regra (PL 102, 821B) explica o mesmo
  versículo (confissão ao abade), guardado em `textos/outros-citacoes.md`.
- **São Beda**: nenhuma explicação (o *De Psalmorum libro* é espúrio e está em `base/`).
- **Santo Anselmo**: só o v. 39 na lista dos bens do céu (*Proslogion* 25, *Meditationes*), e o
  *Tractatus asceticus* (PL 158, 1033A), que copia Cassiano.
- **São Boaventura**: varridos os tomos 5–9 de Quaracchi (archive.org `doctorisseraphic0Nbona`, OCR):
  só citações de passagem (vv. 1–2, 20, 25, 30, 34, 39), nenhuma explicação aproveitável.
- **Tomás de Kempis**: varrida a *Imitação* inteira; achados acima. Outras obras não varridas.
- **Santa Catarina de Sena**: não varrida nesta rodada (fica para o grupo dos modernos, que já tem o
  *Diálogo* em italiano).
- **Gerhoh de Reichersberg** (PL 193, 1355C–1366A) e **Remígio de Auxerre** (*Enarrationes*, PL 131,
  330C–): comentários inteiros ao salmo, guardados em `textos/`, sem excertos: compilam Agostinho,
  Cassiodoro e pseudo-Beda (a imagem do ouro e da palha na fornalha, v. 10, é de Agostinho).
- **Pedro Lombardo, pseudo-Beda, *Breviarium*, «Haimo»**: lidos, sem excertos (compilações).
- **Hildeberto de Lavardin** (sermão 108 «De operibus misericordiae», PL 171, 835D–837B, comenta os
  vv. 1–19 seguidos), **Pedro de Blois**, **Rábano**, **Honório**, **Ivo**, **Werner**: só citações
  ou glosa sem nada novo; Hildeberto é em parte espúrio.
- Varredura feita: ~1100 textos da PL (os 655 já baixados em conversas anteriores, mais ~600 novos de
  50 autores, em `p-latinos/dl/`), com as notas de Migne reinseridas e 70 padrões das palavras dos
  versículos; resultados em `p-latinos/hits1.tsv` e `hits2.tsv`.

## Avisos para a seleção

- **Autor novo**: «São Leão Magno», sobre sugerido: «papa (c. 400–461), Doutor da Igreja».
  Os outros já estão em `ferramentas/autores.json` (Isaac como «Bem-aventurado Isaac de Stella»).
- **Não são santos**: Tomás de Kempis (sem culto oficial); Isaac de Stella é bem-aventurado de culto
  local.
- **Repetições possíveis com outros grupos**: a fumaça (v. 20) e o «transivi» (vv. 35–36) estão também
  em Agostinho; Cassiodoro, v. 26 (a Igreja que fala desde Adão), é de Agostinho, mas acrescenta a
  resposta sobre o Justo abandonado na cruz.
- **Cipriano, *De zelo***: o texto bíblico dele é a Vetus Latina («Noli zelare bene ambulantem in via
  sua»), diferente da Vulgata no v. 7.
- **Bento**: a PL dá «Revela Domino viam tuam»; a edição crítica da Regra lê «Revela ad Dominum».
  O «Confitemini Domino» foi traduzido «Confessai ao Senhor» porque Bento o lê como confissão.
- **Kempis**: o excerto começa pela história e termina no versículo (a citação vem no fim, no texto).
- Links do Corpus Corporum abrem a obra inteira, não o parágrafo: citar a coluna da PL.
