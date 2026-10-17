# Salmo 33 (LXX 32): relatório da pesquisa nos Padres gregos e orientais

Pesquisa de 2026-10-17. Resultado: 40 excertos em `achados-gregos.json` (20 com relevância 3), textos
em `textos/` e o catálogo para os próximos capítulos em `../../fontes/gregos.md`.

## Onde se procurou

- **Fonte principal**: os PDFs da «Ψηφιακή Πατρολογία» (Universidade do Egeu, 2006, «livre uso com menção
  da fonte»), espelhados em http://khazarzar.skeptik.net/pgm/PG_Migne/ (uma pasta por autor, um PDF por
  obra). São texto digital (não imagem): a maioria segue a PG e traz as colunas («29.325» = PG 29, 325).
  Convertidos com `../../ferramentas/gregos-limpar.py` e varridos com `../../ferramentas/gregos-buscar.py`
  (busca sem acentos por uma expressão de cada versículo).
- **Conferência**: OCR da PG 29 no Internet Archive (https://archive.org/details/patrologicursus22migngoog),
  para os números das seções de Basílio; edição de Basílio, *Sobre o Espírito Santo*, por C. F. H. Johnston
  (Oxford 1892, https://archive.org/details/bookofsaintbasil00basi); Irineu na edição de Harvey (1857).
- O documentacatholicaomnia.eu tem a PG em PDF de imagem (pesado, sem texto); o OCR grego da PG no
  archive.org é ruim e o latim da PG 7 saiu ilegível. O First1KGreek (GitHub) não tem Basílio nem os
  comentários aos Salmos de Teodoreto, Eusébio ou Atanásio. Uma busca na web por frases gregas não deu nada.

## O que se achou

| Autor, obra | Onde | Situação |
|---|---|---|
| **São Basílio, Homilia sobre o Sl 32** | PG 29, 324–349 | **Texto grego inteiro**, seções 1–10, em `textos/basilio-homilia-salmo-32.md`. É o principal: 23 excertos. Não há tradução antiga em língua moderna (a de A. C. Way, 1963, tem direito autoral). |
| Teodoreto, *Interpretatio in Psalmos* | PG 80, 1093–1101 | Inteiro. Leitura histórica (Ezequias e Senaquerib) e espiritual; cita Áquila e Símaco. 2 excertos. |
| Eusébio, *Commentaria in Psalmos* | PG 23, 280–288 | Inteiro (até o v. 19). Profecia da Igreja dos gentios e das perseguições. 2 excertos. |
| Santo Atanásio, *Expositiones in Psalmos* | PG 27, 164–165 | Inteiro: glosas de uma frase; nada para excerto. Os trechos entre colchetes são de Basílio e Teodoreto (acréscimos de cadeia). |
| Santo Atanásio, *Carta a Marcelino* | PG 27, 16, 28, 32 | Diz que o Sl 32 é «exortativo» e que é o salmo para cantar **com muitos, reunindo os justos** (excerto). |
| São Cirilo de Alexandria, *Expositio in Psalmos* | PG 69, 869–884 | Inteiro (cadeias, ed. Mai). Leitura cristológica. 1 excerto. |
| Orígenes, *Selecta in Psalmos* | PG 12, 1304–1305 | Glosas curtas; várias são de Evágrio. Nenhum excerto (fraco e de autoria incerta). |
| Orígenes, fragmento de Pitra ao v. 6 | *Analecta sacra* | É, na segunda metade, o texto de Basílio sobre os anjos. |
| Dídimo, comentário do papiro de Tura | pp. 177–184 do códice (Gronewald, PTA 8) | Cobre os v. 13–22 (os v. 1–12 se perderam). Guardados os v. 13–19. 1 excerto, como citação curta. |
| Dídimo, fragmentos de cadeia | Mühlenberg, frags. 290–297 | V. 1–7; texto digital estragado (sem espíritos). Não copiado. |
| Apolinário, fragmento ao v. 6 | Mühlenberg, frag. 9 | Guardado só para registro: autor herético, não serve para o site. |
| São Gregório de Nissa, *Sobre os títulos dos Salmos* II, 13 | GNO V, 94–95 | Por que o Sl 32 não tem título no hebraico. Guardado; sem excerto. |
| São João Crisóstomo | — | **Não comentou o Sl 32** (as *Expositiones* cobrem Sl 4–12, 41, 43–49, 108–117, 119–150). Cita o salmo em várias homilias (ver abaixo). |

**Citações em outras obras** (todas em `textos/citacoes-gregas-avulsas.md`):

- v. 3 «cântico novo»: Clemente, *Protréptico* 1 (Cristo é o cântico novo; não cita o Sl 32 pelo nome).
- v. 4: Atanásio, *Contra os arianos* II (PG 26, 300).
- v. 6 (o Verbo e o Espírito na criação): Teófilo, *A Autólico* I, 7 (o uso mais antigo); Irineu, *Contra as
  heresias* I, 22, 1 (latim); Clemente, *Protréptico* 4, 63; Atanásio, *Contra os arianos* II, 31, *Cartas a
  Serapião* I, 31 e III, *Carta a Marcelino*; Basílio, *Sobre o Espírito Santo* 16, 38 e 19, 49; Gregório de
  Nissa, *Grande catequese* 4 e *Refutação de Eunômio*; Gregório Nazianzeno, *Discurso 41*, 14; João
  Damasceno, *Exposição da fé* I, 7 (copia Nissa) e IV, 13 (Eucaristia).
- v. 9: Cirilo de Jerusalém, *Catequese* 11, 16 e 11, 23; Gregório de Nissa (várias vezes, contra Eunômio).
- v. 15 («formou um a um os corações»): Crisóstomo, homilias sobre 1 Coríntios 11, João 24, Colossenses 2,
  Romanos 26; Dídimo (Tura).
- v. 16–17 (o rei, o gigante, o cavalo): Crisóstomo, *Exposição do Sl 143* e do Sl 7, *Homilia 28 sobre Romanos*.
- v. 22: Crisóstomo, *Homilia 3 sobre Filipenses*.

## Problemas e cuidados

- **Atribuições das cadeias**: o trecho de Basílio sobre os anjos santificados pelo Espírito (§ 4) aparece
  também sob Eusébio (PG 23, 281), Orígenes (Pitra) e, em parte, Cirilo; o trecho sobre γῆ e κατοικοῦντες
  (§ 6) aparece em Cirilo (PG 69, 876). Sempre citar Basílio, cuja homilia é a fonte.
- **Texto digital**: as palavras partidas no fim de linha foram coladas por programa; os erros vistos foram
  corrigidos à mão (lista no topo de cada arquivo). Não houve conferência completa com a PG impressa:
  antes de publicar um excerto, vale olhar a coluna na PG.
- **Colunas aproximadas**: Gregório de Nissa (*Grande catequese*), Teófilo, Damasceno e Cirilo de Jerusalém
  estão em PDFs que seguem edições modernas (sem colunas da PG); a coluna dada no JSON é aproximada e está
  marcada «aprox.». Clemente vai pela numeração de Stählin.
- **Basílio, *Sobre o Espírito Santo***: não está nos PDFs; o grego de 16, 38 e 19, 49 foi reconstruído do OCR
  de Johnston (1892), conferindo o aparato; no último membro adotou-se a lição da PG (τὸ στερεοῦν Πνεῦμα).
- **Direitos**: os textos antigos são de domínio público. O papiro de Tura de Dídimo e os fragmentos de
  Mühlenberg vêm de edições modernas (1969 e 1975): no JSON, Dídimo vai como «citação curta». O Gere decide
  se o trecho guardado em `textos/` pode ficar (o texto é do séc. IV; a edição alemã já passou dos 25 anos
  da proteção de edições científicas, mas isso não foi verificado com advogado).
- **ἐξομολογεῖσθε** (v. 2): Basílio explora o duplo sentido «louvar / confessar»; na tradução do excerto
  ficou «louvar», com nota no resumo.
- **κατὰ μόνας** (v. 15): os Padres leem de três modos: «um a um, cada coração à parte» (Eusébio, Dídimo,
  Crisóstomo), «só ele, que os formou, os conhece» (Orígenes/Evágrio) e «simples, a sós» (Basílio). Bom tema
  para nota.

## O que não existe ou não se achou

- Basílio, Teodoreto, Eusébio, Cirilo de Alexandria: nada além do que está aqui sobre o Sl 32.
- **Crisóstomo** não tem homilia nem exposição do Sl 32.
- **Hesíquio de Jerusalém**: o comentário breve (ed. Antonelli, 1746, como «Pseudo-Atanásio, *De titulis
  Psalmorum*», PG 27, 649–1344) e os fragmentos maiores (PG 93) não estão no khazarzar (lá só há homilias).
  Não verificado.
- **Eutímio Zigabeno**, *Commentarius in Psalterium* (PG 128, 41–1326): não está no khazarzar; não verificado
  (procurar a PG 128 no archive.org).
- **Diodoro de Tarso** (Sl 1–50, CCSG 6, 1980) e **Teodoro de Mopsuéstia** (Sl 1–80, ed. Devreesse 1939):
  edições modernas, não consultadas; Teodoro foi condenado (553) e não serve para o site.
- **Cirilo de Jerusalém** não cita o v. 6 nas *Catequeses* (as ocorrências de «πνεύματι τοῦ στόματος αὐτοῦ»
  são de 2 Ts 2,8); cita o v. 9.
- **Irineu**: o grego de *Contra as heresias* I, 22 se perdeu; só o latim. A *Demonstração* (armênio) não foi vista.
- Sem tradução antiga de domínio público, em língua moderna, para a homilia de Basílio sobre o Sl 32, para
  Teodoreto ou para Eusébio. Há para *Sobre o Espírito Santo* (NPNF II/8) e para Irineu (ANF 1).
