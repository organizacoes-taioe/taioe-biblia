# Gênesis 3: relatório da pesquisa nos orientais não gregos e na liturgia oriental

Pesquisa de 2026-10-26. **16 achados** em `achados-orientais.json` (trecho 1: 4; trecho 2: 2; trecho 3: 5; trecho 4: 5).
Textos novos em `base/` (cabeçalho do `COMO-PESQUISAR.md`), gravados à mão: `afraates-demonstracao-6.md` (§ 6),
`afraates-demonstracao-7.md` (§ 8), `efrem-hino-natividade-17.md`, `efrem-hino-natividade-22.md`, `liber-graduum-memra-21.md`
(§ 20), `jaco-de-sarug-querubim-e-ladrao.md` (Bedjan V, memra 177, transcrito da imagem), `triodio-1876-domingo-do-perdao.md`,
`menaion-1889-proeortia-natal.md`, `romano-natividade-2.md`; mais linhas no fim de `_pistas-orientais.md` e o
`_ausentes-orientais.md`. Já estavam em base: `efrem-comentario-genesis.md` (aqui) e, em `../001/base/`,
`efrem-hino-natividade-26.md`. Scripts e rascunhos em `~/.cache/taioe-gn3/orientais/` (nenhum script do repositório foi tocado).

## Ponto para a conversa principal: o siríaco do *Comentário* de Efrém

O pedido manda traduzir do siríaco, com o latim de Assemani só para conferir. Para os **6 achados do *Comentário ao
Gênesis*** isso não deu inteiro: o siríaco só existe na imagem de Assemani (serto miúdo de 1737; a edição de Tonneau,
CSCO 152, é de empréstimo restrito no archive.org e tem direito autoral). Testei a leitura em quatro páginas (p. 34, 38, 39
e um trecho da 32): dá para ler, mas cada linha pede várias ampliações e sobram palavras duvidosas, e o `original` deixaria
de ser «o trecho exato». Por isso, **nesses 6 o `original` é o latim de Benedetti** (conferido na imagem palavra por
palavra, como no Gn 2, cujo comentário de Efrém já saiu assim), e a tradução segue o latim, conferida no siríaco nos pontos
que li:

- p. 34, «Onde estás?»: ܐܝܟܐ ܐܢܬ ܐܕܡ: ܒܥܘܒܗ ܕܐܠܗܘܬܐ ܕܡܠܟ ܠܟ ܚܘܝܐ. ܐܘ ܒܠܥܘܣܗ ܕܡܘܬܐ («no seio da divindade que a serpente
  te aconselhou? ou nas mandíbulas da morte?»): confere com o latim (*in sinu Divinitatis… intra mortis fauces*).
- p. 38–39, a árvore da vida: ܘܗܫܐ ܠܡ ܕܠܡܐ ܢܘܫܛ ܐܝܕܗ ܘܢܣܒ ܐܦ ܡܢ ܐܝܠܢܐ ܕܚܝܐ… ܐܢ … ܡܢ ܐܝܠܢܐ ܕܐܬܦܩܕ ܕܠܐ ܢܐܟܘܠ ܐܡܪܚ («se ousou comer
  da árvore de que lhe foi mandado não comer»), e mais adiante … ܡܫܒܩܝܢ ܗܘܘ ܡܢ ܠܘܛܬܐ ܘܡܠܒܫܝܢ ܫܘܒܚܐ ܢܬܠܝܘܗܝ ܠܗܘܢ ܐܬܚܫܒ ܗܘܐ
  («quando estivessem livres da maldição e vestidos de glória, ele pensava dá-la a eles»): confere com *quam eisdem a
  maledicto liberis, gloriaeque stola amictis concedere proposuerat*. O meio da frase seguinte (*ne gratia supplicium
  perpetuaret*) eu não li com segurança no siríaco.

Se a regra do siríaco tiver de valer também aqui, o caminho é transcrever, na imagem, só as linhas de cada excerto (uns 6 a
10 versos de serto por achado, com `recorte.py`/`faixas.py` da minha pasta, a partir das folhas w4000 do archive.org) e
mandar as dúvidas para o Gere; recomendo deixar como está, no padrão do Gn 2, e marcar no `lingua` que é a tradução latina.

## Onde se procurou

- **Efrém, *Comentário ao Gênesis*** (Assemani I, p. 27–39): lido inteiro no `base/`; os trechos usados conferidos na imagem
  (folhas n50, n52, n53, n54, n55–56, n57, n58–59; regra: n = p. + 20). O OCR só erra letras («Sigo» = *ergo* na p. 32,
  «fictus» na p. 37).
- **Digital Syriac Corpus** (clone em `cache/genesis/orientais/sc`): a tabela automática de `_pistas-orientais.md` (3-gramas da
  Peshitta), lida bloco a bloco, e palavras-chave (`--kw`): ܚܘܐ em Efrém (achou Natividade 1, 17, 21, 22), ܬܐܢܬܐ, ܛܪܦܐ ܕܬܐܢ,
  ܟܘܬܝܢܝܬܐ, ܫܢܢܐ ܕܚܪܒܐ (achou Afraates, Dem. 6, 6), ܓܝܣܐ junto de ܦܪܕܝܣܐ. Script próprio `janela.py` para ler o contexto.
- **Jacó de Sarug, Bedjan I–V**: OCR siríaco (djvu.txt) baixado dos cinco volumes; a busca por ܟܪܘܒܐ ܘܓܝܣܐ achou o memra 177 de
  Bedjan V, «Sobre o querubim e o ladrão» (p. 659–686). Índice de páginas do OCR baixado (`b5_pageindex`, `b5_search`,
  `b5_page_numbers`); a imagem fica uma folha atrás do índice do OCR (p. 677 = imagem n702 = OCR n703).
- **Liturgia bizantina**: AGES (cache) para achar os textos; conferidos nas edições de Veneza: Triódio de 1876, p. 58
  (Domingo do Perdão, folha n66, já baixada pelo Gn 2) e Menaion de dezembro de 1889, p. 138 (item
  `menaion-tou-ianouariou-etc-2`, que é o vol. 12, dezembro; índice do OCR baixado como `men12_*`).
- **Romano**: Pitra, *Analecta sacra* I (folha n615, já baixada pelo Gn 2), kontákion da Natividade II.
- **Parisot** (OCR `ps1_*` do cache) e **Kmosko** (`kmosko_djvu.txt`) para as colunas e o latim de conferência.
- **Efrém, *Hinos sobre o Paraíso*** (Assemani III): OCR latino lido nas folhas n636–676; achados os trechos sobre Gn 3
  (pistas), mas o siríaco é verso em serto miúdo (testei a estr. IV, 5 na folha n648, em alta resolução: não dá leitura segura)
  e o latim é paráfrase em prosa: ficaram fora.

## Achados (16)

| # | id | autor, obra, onde | vv. | rel. | nota |
|---|---|---|---|---|---|
| 1 | `efrem-coment-gn-3-4-6-a-serpente-se-calou` | Efrém, *Comentário*, Assemani I, p. 30 (latim) | 4–6 | 3 | Eva podia ter respondido à serpente com as palavras dela («meus olhos não estão fechados»); tirou os olhos da serpente e os pôs na árvore, e «a serpente se calou». Cena viva, que ninguém mais dá |
| 2 | `efrem-coment-gn-3-5-7-prometendo-a-divindade` | Efrém, *Comentário*, p. 32 (latim) | 5, 7 | 3 | «Prometendo a divindade, excluiu-os da divindade»: os bens prometidos já estavam destinados à obediência. É o «ser como Deus sem Deus» que o pedido atribui a Máximo (grupo gregos): ver qual fica mais claro |
| 3 | `efrem-hino-nat-26-9-o-veneno-e-o-remedio` | Efrém, *Natividade* 26, estr. 9 (siríaco, Beck pelo corpus) | 1, 6 | 3 | A inveja do diabo, o veneno no alimento, e Cristo, o «Remédio da vida», que se dá a comer. Era pista de `proximos.md` |
| 4 | `efrem-hino-nat-17-folhas-de-vergonha` | Efrém, *Natividade* 17, estr. 4 e 6 (siríaco) | 7, 14 | 3 | As folhas da vergonha de Eva e a veste de glória de Maria; a serpente que come pó comeu Eva tornada pó; Cristo, nosso pão e veste de glória. **A veste de glória** está também no Gn 2 (Efrém, sobre 2,25): aqui é o par Eva–Maria |
| 5 | `efrem-coment-gn-3-8-9-os-passos-e-a-voz` | Efrém, *Comentário*, p. 33–34 (latim) | 8–9 | 3 | Deus demora e faz ouvir os passos para dar tempo ao arrependimento; «Onde estás? No seio da divindade, ou nas fauces da morte?» |
| 6 | `afraates-dem-7-8-onde-estas-chamado-a-penitencia` | Afraates, Dem. 7, 8 (siríaco; Parisot col. 322–325) | 9–12 | 3 | «Onde estás?» é o chamado à penitência; Adão escondeu o pecado e culpou Eva. **Diz o que Teófilo II, 26 e Crisóstomo dizem** (grupo gregos); o próprio de Afraates: ele fala aos sacerdotes que acolhem os penitentes («médicos»), e liga a morte à falta de confissão. Fica um dos dois, ou o 5 |
| 7 | `efrem-coment-gn-3-13-15-a-serpente-sem-pergunta` | Efrém, *Comentário*, p. 35–36 (latim) | 13–15 | 3 | Deus pergunta a quem pode se arrepender; à serpente, só a sentença; e começa por ela para que Adão e Eva corressem à penitência |
| 8 | `efrem-hino-nat-22-31-o-pe-de-maria` | Efrém, *Natividade* 22, estr. 31 (siríaco) | 15 | 2 | O pé de Maria pisa o soberbo que feriu Eva no calcanhar (cita a Peshitta de 3,15). Curto; o tema do protoevangelho terá Ireneu e Justino (gregos) e Montfort (modernos) |
| 9 | `romano-natividade-2-4-eva-ouve-maria` | Romano, kontákion da Natividade II, estr. 4 (grego, Pitra I, p. 515) | 15–16, 20 | 3 | Eva, que deu à luz entre dores, ouve o canto de Maria e chama Adão; o filho dela «amarrou quem me feriu». **Autor novo**: «São Romano, o Melodista» não está em `ferramentas/autores.json` |
| 10 | `afraates-dem-6-6-pela-vinda-do-filho-de-maria` | Afraates, Dem. 6, 6 (siríaco; Parisot col. 265–268) | 16–19, 24 | 3 | Cada pena de Gn 3 desfeita pela vinda do Filho de Maria: espinhos arrancados, suor enxugado, maldição pregada na cruz, espada afastada da árvore da vida. Cortei o começo do § 6 (a mulher como arma do adversário), que fora do contexto soa mal; o excerto começa em «por causa de Eva». Serve também a um tema final sobre o capítulo inteiro |
| 11 | `efrem-coment-gn-3-17-19-o-suor-e-o-po` | Efrém, *Comentário*, p. 37 (latim) | 17–19 | 3 | Cada pena responde a uma escolha; «voltarás à tua terra, para te conheceres pelo teu barro» |
| 12 | `liber-graduum-21-20-tunicas-por-misericordia` | *Liber Graduum*, memra 21, 20 (siríaco; Kmosko col. 631–634) | 21 | 2 | As túnicas, começo da compaixão: Deus não tratou Adão segundo a sua loucura. **Diz o que Francisco diz** (audiência de 22/04/2015, grupo modernos); cortei antes da tese da obra (Adão escolheu o trabalho que o prende à terra) |
| 13 | `efrem-coment-gn-3-22-a-arvore-da-vida-negada` | Efrém, *Comentário*, p. 38–39 (latim) | 22 | 3 | A árvore da vida negada por misericórdia: «para que a graça não tornasse perpétuo o castigo»; ela teria «sepultado os vivos». **Toca Nazianzeno, *Or.* 38, 12** («para que o mal não fosse imortal», gregos): Efrém é mais concreto; ficam bem lado a lado |
| 14 | `liturgia-triodio-domingo-do-perdao-adao-expulso` | Triódio (Veneza 1876, p. 58), Domingo do Perdão, Vésperas, «Ἐξεβλήθη Ἀδάμ» | 23–24 | 3 | Adão sentado diante do paraíso; e a resposta do Salvador (1Tm 2,4; Jo 6,37). Escolhi este, e não o mais conhecido «Ἐκάθισεν Ἀδάμ» (mesma página, em base), porque tem a resposta de Deus |
| 15 | `jaco-sarug-querubim-e-ladrao-o-ferrolho-de-adao` | Jacó de Sarug, memra 177 de Bedjan V, p. 676–677 e 685 (siríaco, transcrito da imagem) | 24 | 3 | O bom ladrão com a chave da cruz diante do querubim: «o ferrolho fechado na saída de Adão só se abre quando vier o Senhor de Adão»; e o querubim recolhe a espada. **Diz o que Crisóstomo, *De cruce et latrone*, e Cirilo de Jerusalém dizem** (gregos), mas como cena |
| 16 | `liturgia-proeortia-natal-a-arvore-da-vida-floresceu` | Menaion de dezembro (Veneza 1889, p. 138), apolitíquio da Proeórtia do Natal | 22, 24 | 3 | «O Éden se abriu; a árvore da vida floresceu da Virgem; comendo dela, viveremos, e não morreremos como Adão». **Toca o prefácio da Santa Cruz** (modernos): a árvore da vida, aqui no Natal |

Os três mais fortes: o querubim e o ladrão de Jacó (15), a árvore da vida negada por misericórdia (13) e Afraates, Dem. 6, 6
(10); logo depois, a serpente que se calou (1), «prometendo a divindade, excluiu-os dela» (2) e Eva que ouve Maria (9).

Efrém tem 9 dos 16 (6 do *Comentário*, 3 dos hinos). Se for preciso cortar: 8 (curto, tema cheio), 6 ou 5 (o mesmo «Onde
estás?» como convite), 12 (perto de Francisco), 4 (veste de glória já no Gn 2).

## Para a conversa principal

- **Autores para `ferramentas/autores.json`**: «São Romano, o Melodista» (novo; «sobre» sugerido: «diácono em Constantinopla
  (séc. VI), o maior hinógrafo bizantino», `autor_id` `romano-melodista`, oriental) e «Liber Graduum (Livro dos Degraus)»
  (proposto desde 2Cor 3, Nm 17 e Gn 2; não entrou: «obra ascética siríaca anônima (séc. IV–V), sobre os degraus da vida
  cristã»). Os outros já existem.
- **Siríaco a conferir antes de publicar**: Jacó (15) foi lido na imagem de Bedjan, sem vogais; as palavras duvidosas estão
  marcadas com (?) em `base/jaco-de-sarug-querubim-e-ladrao.md` e ficaram fora do excerto. Conferir sobretudo «ܡܪܗ ܕܐܕܡ»
  (p. 677, linha 1: li «o Senhor de Adão»; o OCR dá «ܡܕܗ»; a outra leitura possível, «ܒܪܗ ܕܐܕܡ», «o Filho de Adão», muda pouco o
  sentido) e «ܕܐܚܝܕ» (p. 676, última linha). Na p. 685 o querubim «recolheu a lâmina de fogo» (ܐܪܦܝ… ܫܢܢܐ ܕܢܘܪܐ): a fala ao redor
  é do ladrão contando ao Senhor o que houve; o excerto só dá o fato.
- **Natividade 17, estr. 6**: «câmara nupcial» (ܓܢܘܢܢ) é restituição de Beck; a tradução a segue sem colchetes. A estr. 6
  joga com Gn 3,14 (a serpente come pó; Eva tornou-se pó): conferir se a leitura «Eva se tornou o pão dela» agrada.
- **Afraates, Dem. 6, 6**: «a figueira foi amaldiçoada» (ܬܬܐ ܠܝܛܐ) junta a figueira das folhas (3,7) e a de Mt 21,19; «o pó se
  tornou sal» lembra 3,19 e Mt 5,13. Não pus nota.
- **Direitos**: tudo em domínio público. O siríaco dos hinos vem da edição de Beck pelo Digital Syriac Corpus (CC BY), como nos
  capítulos anteriores; Romano, da edição de Pitra (1876), não das críticas.
- **Liturgia**: o Gere pediu só a liturgia da Missa nas notas; nos comentários, a oriental entra quando é comentário de verdade.
  Os dois textos bizantinos (14, 16) são leitura da cena, não rubrica; mas, se o tema da liturgia do fim já tiver o *Exsultet* e
  o prefácio da Santa Cruz, talvez baste um deles.

## O que não existe ou não se usou

- O siríaco do *Comentário* e dos *Hinos sobre o Paraíso* de Efrém não tem texto digital em domínio público (ver acima).
- Os *Hinos sobre o Paraíso* têm muito de Gn 3 (pistas em `base/_pistas-orientais.md`), mas sem siríaco legível e com latim de
  paráfrase: fora.
- O Grande Cânon de André de Creta (ode 1, Triódio de 1876, p. 259) fica com o grupo dos gregos, que o tem na lista.
- Siríacos fora da comunhão (Narsai, memre 76 e 64; bar Salibi; Isaac de Nínive, Discurso 28; Filoxeno, Discurso 10): só pista.
- Não procurados: Narek, Nerses, coptas, etíopes, *Apophthegmata*, Pseudo-Macário, o *Fenqitho* siro-católico e o breviário
  caldeu.

## Armadilhas

- Bedjan V: a imagem fica uma folha atrás do índice do OCR (OCR n703 = imagem n702 = p. 677); regra da imagem: n = p. + 25.
- O item `menaion-tou-ianouariou-etc-2` do archive.org é o vol. 12 (dezembro), apesar do título «Janeiro»; os arquivos têm nome
  com «Mēnaion_tou_Ianouariou_etc(2)» (URL com %C4%93 e %28 %29).
- O OCR de Assemani III usa o «s» longo («fic» acha *sic*, *fici*…): buscar com palavras inteiras.
- O OCR de Assemani I perde linhas na virada das páginas (p. 30 → 31; p. 32 → 33): começar os excertos depois da virada.

## Para outros capítulos

- **Gn 4**: Afraates, Dem. 7, 8, logo depois do trecho usado (a Caim também foi dada a penitência: «se fizeres o bem…»; e a
  geração de Noé, 120 anos para se converter, Gn 6,3); Efrém, *Comentário* p. 38–39 continua em Gn 4.
- **Gn 6**: o mesmo Afraates (120 anos de penitência dados à geração de Noé).
