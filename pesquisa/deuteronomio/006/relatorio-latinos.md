# Dt 6, grupo latinos: relatório

18 achados em `achados-latinos.json` (Agostinho 5, Tomás 4, Bernardo 3, Hilário, Gregório Magno, Crisólogo, Jerônimo, Beda, Leão Magno 1 cada). Excertos montados por script a partir dos textos do cache (Corpus Corporum, Corpus Thomisticum); original não reescrito.

## O que entrou
- T1 (vv. 1–3): Tomás II-II q.44 a.1 (o fim do preceito é a caridade); Bernardo, SC 28,6 (Audi, Israel = escuta que obedece).
- T2 (vv. 4–9): Hilário, De Trin. IV,15 (o «Senhor é um» contra os ídolos); Agostinho DDC I,22, Serm. 34,7-8, Ep. 137,17 (v. 5); Gregório Hom. Ev. 38,10; Crisólogo Serm. 62; Tomás q.44 a.5 e a.6; Bernardo De dil. Deo V,15 e SC 20,4; Leão Serm. 95,6 (relevância 1); Jerônimo In Mt IV (filactérios, vv. 8–9).
- T3 (vv. 10–19): Agostinho QH V,12 (v. 13, jurar) e Enarr. Ps 90 s.2,7 (v. 16); Tomás q.97 a.1 (v. 16); Beda In Lc 4,8 (v. 13, latria e dulia).

## Lacunas
- T4 (vv. 20–25) sem achado, e vv. 10–12 (esquecer na fartura) sem achado em Dt 6: os Padres citam esses temas por Dt 8,11-14. Nenhum Padre latino do cache comenta Dt 6,20-25; Rábano e Hugo (In Dt) pulam o trecho.
- v. 2 («temer», «prolongar os dias»), v. 3 e v. 15 (Deus zeloso) sem achado próprio.

## Como se procurou
`grep` (/usr/bin/grep) em todos os caches `pesquisa/cache/**` por frases da Vulgata e notas «Deut. VI»; leitura de Rábano, In Dt (cap. XI–XII dele = Dt 5–6, só compila Agostinho e Jerônimo), Lápide (só para achar pistas). Baixado: Corpus Thomisticum sth3044 (`cache/deuteronomio/dt6-latinos/`).

## Não entram / pistas
- Ambrósio, Enarr. in Ps 1, 65 (Dt 6,7: falar do Senhor em casa e no caminho): já usado em Salmos 37 (excerto repetido); serve a Dt 6 só se for tirado de lá.
- Ep. 170 de Agostinho (latria, Dt 6,13) e Ep. 238,18 (Shemá e Trindade); Ruperto, De glorificatione Trinitatis XIV (Dt 6,4-5 lido como Trindade; alegórico); Leão, Sermo 95; Crisólogo, Sermo 11 (Mt 4, Dt 6,16); Ambrósio, Exp. Lc IV,26 (Non tentabis); Gregório, Hom. Ev. 38 (já entrou); Cassiano, Coll. XIV (Audi, Israel como sentido simples); Agostinho Enarr. Ps 98,9 (Dt 6,13 e «adorai o escabelo»).
- Hilário IV,15 e Gregório Moralia: o que sobrou do Shemá contra arianos é repetitivo.

## Autores novos
Nenhum fora de `autores.json`. `autor_id` novos (slugs): `pedro-crisologo`, `leao-magno`, `jeronimo`, `beda`. Nenhum é oriental.

## Problemas
- Fórmula de Beda em `cc_8470` (In Lc); a cópia nas Homiliae difere em pontos.
- Corpus Corporum traz pequenos erros (ex. «Moysesut» em Jerônimo, evitado cortando).
- A tradução de Bernardo SC 28 usa «Ouve, Israel» citado como Dt 6,3.
