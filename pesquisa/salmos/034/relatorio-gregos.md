# Salmo 34 (LXX 33): relatório da pesquisa nos Padres gregos e orientais

Pesquisa de 2026-10-17. Resultado: 44 excertos em `achados-gregos.json` (23 com relevância 3; todos os versículos cobertos), textos em `textos/`
e o que serve para os próximos salmos em `../../fontes/gregos.md`. Numeração dos versículos: título = v. 1,
Εὐλογήσω = v. 2 … Λυτρώσεται = v. 23 (a da LXX coincide com a nossa neste salmo).

## Onde se procurou

- **Texto grego**: PDFs da «Ψηφιακή Πατρολογία» (Univ. do Egeu, 2006) no espelho http://khazarzar.skeptik.net/pgm/PG_Migne/,
  convertidos com `../../ferramentas/gregos-limpar.py`. Para os usos fora dos comentários, foram baixadas e convertidas as pastas
  inteiras de Basílio, Gregório Nazianzeno, Gregório de Nissa, Atanásio, Orígenes, João Damasceno, Macário e Crisóstomo (~400 PDFs;
  a conversão do Crisóstomo ficou em 285 dos 398 PDFs; a de Cirilo de Alexandria em 30 de 70 e a de Teodoreto em 23), e varridas
  com uma cópia de `gregos-buscar.py` com uma expressão de cada versículo (23 padrões, sem acentos).
- **Conferência das seções de Basílio**: OCR da PG 29 no Internet Archive (https://archive.org/details/patrologicursus22migngoog).

## O que se achou

| Autor, obra | Onde | Situação |
|---|---|---|
| **São Basílio, Homilia sobre o Sl 33** | PG 29, 349–388 | **Texto grego inteiro**, seções 1–14, em `textos/basilio-homilia-salmo-33.md`. Comenta todos os versículos; é a fonte principal: 26 excertos. A seção 3 caiu no OCR (início provável no v. 4). Sem tradução antiga em língua moderna (a de A. C. Way, 1963, tem direito autoral). |
| Eusébio, *Commentaria in Psalmos* | PG 23, 288–296 | Inteiro, mas só até o v. 10. Longa discussão do título: Abimelec = o sacerdote Aquimelec de Nob; Áquila traduz «mudou o seu **gosto**», que Eusébio liga aos pães da proposição e ao v. 9. 1 excerto. |
| Teodoreto, *Interpretatio in Psalmos* | PG 80, 1101–1109 | Inteiro. Título em Nob (pães sagrados = prefiguração da Eucaristia aberta a todos); **v. 6 = batismo, v. 9 = Eucaristia**. 3 excertos. |
| São Cirilo de Alexandria, *Expositio in Psalmos* | PG 69, 884–893 | Inteiro (cadeias, ed. Mai). Mistura trechos de Basílio (v. 4, 6, 13) e a glosa dos v. 12–14 de Atanásio. 2 excertos próprios (v. 16–17; v. 23). |
| Santo Atanásio, *Expositiones in Psalmos* | PG 27, 165–169 | Inteiro: glosas de uma frase. Várias são iguais às de Teodoreto (cadeia, sem colchetes no PDF). 1 excerto (v. 15, também em Orígenes). |
| Santo Atanásio, *Carta a Marcelino* | PG 27, 28 e 32 | O Sl 33 está entre os salmos «de ação de graças»; **uso**: cantá-lo com os mansos depois de escapar dos inimigos. 1 excerto. |
| Orígenes, *Selecta in Psalmos* | PG 12, 1308–1309 | Glosas curtas, em boa parte de Evágrio. Nenhum excerto. O fragmento de Pitra traz só a mesma glosa do v. 9. |
| Dídimo, comentário do papiro de Tura | págs. 184–203 do códice (Gronewald, PTA 8, 1969) | **Cobre o salmo inteiro.** Leitura cristológica do título (Cristo «mudou o rosto» ao assumir a forma de servo; o rei de Gat é o diabo, que não pôde retê-lo). 1 excerto, como citação curta; trechos em `textos/didimo-comentario-tura-salmo-33.md`. |
| Dídimo, fragmentos de cadeia; Apolinário | Mühlenberg, frags. 302–316; frags. 10–12 | Texto digital estragado (Dídimo); Apolinário é herege. Não copiados. |
| São Gregório de Nissa, *Sobre os títulos dos Salmos* | GNO V, 70 | Só cita o título entre os «históricos»; não comenta o Sl 33 (só trata em detalhe os títulos com «para o fim»). Sem excerto. |
| São João Crisóstomo | — | **Não comentou o Sl 33.** Usos nas homilias: abaixo. |

**Usos fora dos comentários** (trechos em `textos/citacoes-gregas-avulsas.md`):

- **Liturgia, o salmo da comunhão**: São Cirilo de Jerusalém, *Mistagógica* 5, 20 (o v. 9 cantado durante a comunhão: «não provais pão e
  vinho, mas o corpo e o sangue de Cristo») e 5, 6 (o v. 4 no prefácio); *Constituições Apostólicas* VIII, 13, 16 (obra anônima síria,
  c. 380): «enquanto todos comungam, cante-se o Salmo 33».
- v. 2: Gregório de Nissa, *Sobre o mártir Teodoro* (o mártir canta o v. 2 enquanto o torturam) — excelente; Basílio, *Regras longas*;
  Nazianzeno, *Discurso 32*, 20.
- v. 6 (**batismo, «iluminação»**): Nazianzeno, *Discurso 40*, 24 e *Discurso 39*, 2; Nissa, *No dia das Luzes* e *Contra os que adiam o
  batismo*; Basílio, *Homilia 13, exortação ao batismo*; Teodoreto (comentário).
- v. 8 (o anjo que acampa): Orígenes, *Sobre a oração* 31, 5 (na assembleia há «duas Igrejas, a dos homens e a dos anjos»), *Contra Celso*
  VIII, 34 e 36, *Homilias sobre Jó*; Nissa, *Cântico*; Crisóstomo, *Homilia 9 sobre Efésios*; Basílio, *Hexaémeron* 5 e *Contra Eunômio*.
- v. 9: Basílio, *Homilia sobre o começo dos Provérbios* (o paladar da alma) e *Homilia 13*; Pseudo-Atanásio, *Homilia sobre a paixão*
  (PG 28, 228); Orígenes, *Comentário a João* e *Diálogo com Heráclides* (sentidos espirituais; edição moderna); Crisóstomo, *Sobre a negação
  de Pedro*.
- v. 12–15: Crisóstomo, *Homilia 8 sobre Hebreus* (o temor de Deus se aprende); Orígenes, *Contra Celso* VI, 54, *Comentário a Mateus*.
- v. 19: Crisóstomo, *Homilia 47 sobre Mateus*. v. 20: Orígenes, *Sobre a oração* 29–30, *Exortação ao martírio*; Crisóstomo, *Sobre Romanos*.
- v. 22: Crisóstomo, *Homilia 5 ao povo de Antioquia* (morte má não é a violenta, mas a que chega no pecado) e *Sobre a mártir Drósis*.

## O que não existe ou não se achou

- **v. 21 e Jo 19,36**: nenhum comentário grego aplica o v. 21 a Cristo na cruz. Basílio, Atanásio, Teodoreto, Cirilo e Dídimo leem os
  «ossos» como as forças da alma (Basílio, também os fortes da Igreja). Quando comentam Jo 19,36 (Cirilo, *Comentário a João* XII e *De
  adoratione* X; Crisóstomo, *Homilia 15 sobre 1 Coríntios*), ligam o versículo ao cordeiro pascal (Ex 12,46), não ao salmo.
- **Crisóstomo** não tem homilia nem exposição do Sl 33 (as *Expositiones* cobrem Sl 4–12, 41, 43–49, 108–117, 119–150). Nada achado nas
  homilias sobre o v. 19 que vá além de uma citação.
- **Cirilo de Jerusalém** só usa o salmo nas *Mistagógicas*; nas *Catequeses* e na *Procatequese* não há citação dele.
- **Efrém**: não se achou texto siríaco de domínio público com comentário a este salmo; não incluído.
- **Gregório de Nissa** não explica o título «mudou o rosto»; quem o faz é Basílio (§ 1), Eusébio, Teodoreto, Cirilo e Dídimo.
- **Hesíquio** e **Eutímio Zigabeno**: não estão no khazarzar; não verificados (como no Sl 33).

## Problemas e cuidados

- **Atribuições das cadeias**: os trechos de Basílio sobre o v. 4 («uma só mente não basta»), o v. 6 («aos que estão sentados nas trevas»)
  e o v. 13 («não esta vida comum») aparecem sob Cirilo de Alexandria; citar Basílio. A glosa do v. 15 («afastar-se do mal, o temor o
  ensina; fazer o bem, o amor») está em Atanásio e em Orígenes (talvez Evágrio). As glosas de Atanásio aos v. 3, 4, 7 e 8 são as de Teodoreto.
- **Colunas aproximadas**: Cirilo de Jerusalém, *Constituições Apostólicas*, Orígenes (*Sobre a oração*, *Contra Celso*) e Nissa (GNO) estão em
  PDFs de edições modernas; a coluna da PG dada no JSON leva «aprox.».
- **Texto digital**: palavras partidas na quebra de linha foram coladas por programa; as correções à mão estão no topo de cada arquivo.
  Antes de publicar, olhar a coluna na PG impressa.
- **Direitos**: Dídimo (papiro de Tura) vem de edição de 1969: no JSON, «citação curta»; os trechos guardados em `textos/` esperam a
  decisão do Gere, como no Sl 33. *Diálogo com Heráclides* (Orígenes) também é edição moderna: não usado.
- **Orígenes** (*Sobre a oração*) não é santo; está no JSON por ser o testemunho mais bonito do v. 8 sobre os anjos na assembleia.
- **ἀντίτυπον** em Cirilo de Jerusalém (Myst. 5, 20): «figura» no sentido sacramental, não «mero símbolo»; ver a nota no JSON.
