# Gênesis 4: relatório do grupo agostinho (2026-10-26)

Santo Agostinho em toda a obra. A pesquisa partiu da pré-pesquisa (`base/`: *Cidade de Deus* XV, *Quaestiones* e
*Locutiones*) e foi buscar o resto pelo texto da PL no Corpus Corporum: às 26 obras que a pesquisa de Gn 3 deixou em
`cache/genesis/agostinho/cc/` juntaram-se 17 (a *Primeira Carta de João*, o *Contra Iulianum* e a *Obra inacabada*, os
escritos contra os donatistas e os pelagianos, o *De consensu*, o *Speculum* e outros), 43 no total, todas varridas por
«Cain», «Abel», «Lamech» e pelas frases da Vetus Latina dele. **15 achados** em `achados-agostinho.json`. Todo
`original` foi conferido, pedaço por pedaço (entre os «[…]»), contra o texto do augustinus.it gravado em `base/`
(script `~/.cache/taioe-gn4/agostinho/montar.py`); as colunas da PL vêm do texto do Corpus Corporum. A tradução não
traz mesóclise, pronome contraído nem uso europeu, e nenhum excerto repete os publicados em `conteudo/` (sequências de
8 palavras, como no `conferir.mjs`).

## O que se procurou e onde

| obra | onde (Gn 4) | situação |
|---|---|---|
| *De civitate Dei* XV | 1, 2 (Caim e Abel, as duas cidades); 5 (o fundador fratricida, Rômulo); 7, 1–2 (a oferta mal dividida, a tristeza, «tu o dominarás»); 8 (a cidade); 16 (a mulher de Caim); 17–18 (Henoc, Set, Enós); 20–21 (Lamec, as duas linhagens) | `base/` (pré-pesquisa); 8 achados (1, 2 duas vezes, com XV, 17; 5; 7, 1 duas vezes; 7, 2; 16, 1; 18; 21); 8 e 20 são cálculo e numerologia |
| *In Epistolam Ioannis* 5, 8 | Gn 4,3-8 pela 1Jo 3,12 | baixado: `base/agostinho-in-epistolam-ioannis.md`; 1 achado |
| *Contra Iulianum opus imperfectum* VI, 23 e 27 | Gn 4,11-15 (crime enorme, pena leve, o sinal); Gn 4,8 (Abel inaugura o martírio) | baixado: `base/agostinho-opus-imperfectum-contra-iulianum.md`; 2 achados |
| *Enarrationes in Psalmos* 48, s. 2, 11; 61, 6–7; 128, 2 | Gn 4,8 (a iniquidade parece vencer); 4,17 (a cidade); 4,8 (a Igreja só em Abel) | baixado: `base/agostinho-enarrationes-in-psalmos.md`; 1 achado (48); os outros, pistas |
| *Epistola* 102, 16–17 | Gn 4,3-4 (o sacrifício é antigo, Deus não precisa dele) | baixado: `base/agostinho-epistolae.md`; 1 achado |
| *Contra Faustum* XII, 9–13 | Gn 4,3-16, versículo a versículo, em alegoria (Caim = os judeus) | baixado: `base/agostinho-contra-faustum.md`; 1 achado (XII, 10, sem a alegoria); o resto, pistas |
| *Enarrationes* (39, 40, 58, 64, 71, 77, 90, 101, 108, 118, 142), *Sermões* 51, 83, 201, 341, 350, *Cartas* 147 e 149, *De Trinitate* II, *Contra Iulianum* VI, *De nuptiis* II, *Contra Petilianum* II, *Contra adversarium legis*, *De diversis quaestionibus* 83 | menções de uma frase; o sinal de Caim = os judeus; o setenta vezes sete de Mt 18 | só pistas (`base/_pistas-agostinho.md`) |
| *De catechizandis rudibus* 19, 31; *Tract. in Io.*; *Quaest. in Hept.* I, 1; *Locutiones* | — | nada aproveitável (`base/_ausentes-agostinho.md`) |

## Os achados

| id | trecho | vv. | o que diz | rel. |
|---|---|---|---|---|
| `agostinho-civ-15-1-2` | 1 | 1–2 | Caim nasce primeiro e pertence à cidade dos homens, Abel à de Deus: como em cada homem, primeiro o carnal; «ninguém será bom sem ter sido antes mau»; peregrino pela graça | 3 |
| `agostinho-civ-15-7-1-a-oferta-mal-dividida` | 1 | 3–5, 7 | «Se ofereces bem, mas não divides bem» (LXX): Caim deu a Deus algo seu e guardou para si a si mesmo; quis comprar Deus para satisfazer os desejos; «os maus querem usar de Deus para gozar do mundo» | 3 |
| `agostinho-inepio-5-8` | 1 | 3–5, 8 | Deus não preferiu as ovelhas aos frutos: «não olhou para as mãos, mas viu no coração»; caridade em Abel, inveja em Caim; «porque não quis imitá-lo, quis matá-lo» | 3 |
| `agostinho-civ-15-7-1-a-tristeza-pelo-bem` | 1 | 5–6 | Caim devia imitar o irmão, não invejá-lo; a pergunta de Deus repreende a tristeza pelo bem do irmão, que só Deus via no coração | 3 |
| `agostinho-civ-15-7-2` | 1 | 7 | «Sossega... tu o dominarás»: domina o pecado quem o atribui a si e o sujeita pela penitência, em vez de defendê-lo; segurar a mão longe do crime para que a paixão se acostume a não se mover por dentro | 3 |
| `agostinho-civ-15-5` | 1 | 8 | O primeiro fundador da cidade terrena foi um fratricida; Rômulo matou Remo por domínio, Caim matou Abel só porque ele era bom; a bondade cresce quando é partilhada | 3 |
| `agostinho-en48-2-11` | 1 | 8 | Na noite deste mundo a iniquidade parece ter vencido a justiça; «virá a manhã, e se verá onde está Abel e onde está Caim» | 2 |
| `agostinho-opimp-6-27-abel-o-primeiro-martir` | 1 | 8 | Quem fez aquela morte foi Caim; Abel não inaugurou a morte, mas o martírio: morrendo com paciência pela justiça, usou bem o mal que sofreu | 3 |
| `agostinho-ep-102-17-deus-nao-precisa-de-ofertas` | 1 | 3–4 | A oferta dos dois irmãos mostra quão antigo é o sacrifício; Deus não precisa dele: «adorar a Deus é proveito para nós, não para Deus» | 2 |
| `agostinho-cfaust-12-10-a-voz-do-sangue` | 2 | 9–10 | Deus pergunta como juiz, não como quem ignora; «quem guarda Cristo no coração não diz como Caim...»; a voz maior do sangue de Cristo, o «Amém» dos povos que o recebem | 2 |
| `agostinho-opimp-6-23-o-sinal-de-caim` | 2 | 11–12, 14–15 | Crime horrendo, pena leve: Caim nem foi punido com a morte; com medo de que lhe fizessem o que fez ao irmão, recebeu o sinal; Deus pesa as culpas de outro modo que os homens | 2 |
| `agostinho-civ-15-1-2-e-17-a-cidade-de-caim` | 3 | 17 | Caim funda uma cidade com o nome do filho, que repousa na paz deste mundo; Abel, peregrino, não funda nenhuma: a cidade dos santos está no alto | 3 |
| `agostinho-civ-15-16-1-a-mulher-de-caim` | 3 | 17 | No começo os irmãos se casaram com as irmãs, por necessidade; depois foi proibido, para que os laços de família se espalhassem e a caridade se estendesse a mais gente | 2 |
| `agostinho-civ-15-21-de-homicida-a-homicida` | 3 | 17, 23, 26 | Uma linhagem vai de homicida a homicida (Lamec confessa o crime às mulheres) e dá o próprio nome a uma cidade; a outra não busca fama na terra, mas espera invocar o nome do Senhor | 2 |
| `agostinho-civ-15-18-enos-esperou-invocar` | 4 | 25–26 | «Enós esperou invocar o nome do Senhor» (LXX e Vetus Latina): o homem vive da esperança no que não vê, e não a põe em si mesmo | 3 |

Os 3 melhores, para o leitor comum: `agostinho-inepio-5-8` («Deus não olhou para as mãos, mas viu no coração»),
`agostinho-civ-15-7-1-a-oferta-mal-dividida` («dava a Deus algo seu, e guardava para si a si mesmo») e
`agostinho-civ-15-5` (a inveja dos maus contra os bons; a bondade que cresce partilhada).

## Decisões e dúvidas para a seleção

- **Trecho 1 tem 9 achados, de propósito**: é onde Agostinho é mais forte. Para o tema das ofertas, os três
  (`…-a-oferta-mal-dividida`, `inepio-5-8`, `ep-102-17-…`) dizem coisas diferentes (dar-se a si mesmo; o coração e a
  caridade; Deus não precisa de nada). Se couber só um, fica o `inepio-5-8`, o mais claro; o `ep-102-17` é o mais
  dispensável. Para o v. 8, `civ-15-5` (a inveja), `opimp-6-27` (o martírio) e `en48-2-11` (a manhã) também não se
  repetem; se couber só um, `civ-15-5`.
- **A Bíblia de Agostinho no v. 7** é a grega: «Se ofereces bem, mas não divides bem, não pecaste? Sossega: para ti se
  volta ele, e tu o dominarás», e no v. 5–6 «entristeceu-se» em vez de «ficou irado». As citações seguem o que ele leu,
  como manda o PEDIDO; os resumos avisam.
- **`agostinho-cfaust-12-10-a-voz-do-sangue` vem do *Contra Faustum*, onde Caim é figura do povo judeu.** Usei-o porque
  Agostinho não comenta os vv. 9–10 em mais lugar nenhum. Cortei, com «[…]», as frases sobre os judeus («Até hoje que
  nos respondem os judeus…»; «Assim a voz divina repreende os judeus nas Escrituras»); o que ficou é literal (Deus
  pergunta como juiz) e cristológico (o sangue de Cristo e o «Amém»), e não muda o sentido de nenhuma frase. Uma frase
  que liga «Habet enim» ao corte começa com «pois» no latim; na tradução ficou sem a conjunção. Se o Gere preferir não
  usar o *Contra Faustum*, o trecho 2 fica só com `opimp-6-23`.
- **O desespero de Caim (v. 13)**: Agostinho lê «Maior est causa mea» e só o comenta dentro da alegoria (*Contra
  Faustum* XII, 12: Caim não acha grave esconder-se da face de Deus, só ser morto). Ficou nas pistas; o `opimp-6-23`
  diz, sem alegoria, que Caim temia sobretudo a morte. Os latinos (Ambrósio, Jerônimo, Gregório) cobrem melhor.
- **Os dois achados da *Obra inacabada contra Juliano*** respondem a Juliano de Eclano, pelagiano. O `opimp-6-27`
  começa citando a frase dele («a morte não é um mal, porque foi um justo o primeiro a inaugurá-la»), para situar o
  leitor; o resumo diz de quem é. O `opimp-6-23` começa pela comparação com o pecado de Adão, que é de Agostinho.
- **`agostinho-civ-15-21-…` e `agostinho-civ-15-18-…`** usam as etimologias de Agostinho (Caim = «posse», Set =
  «ressurreição», Enós = «homem»). Deixei-as porque o que dizem vale sem elas (a cidade que dá o próprio nome, o homem
  que espera invocar o nome do Senhor); o resumo explica «filho da ressurreição». Se o Gere achar confuso, o XV, 21 pode
  sair, e o XV, 18 fica.
- **A mulher de Caim** (`civ-15-16-1`): dito com simplicidade, como o PEDIDO pede; o resto do capítulo XV, 16 (os
  primos, os graus de parentesco) ficou de fora.
- **Os dois achados de *Civ.* XV, 7, 1** não partilham nenhuma frase (a oferta: o meio do parágrafo; a tristeza: o fim).
  O mesmo com XV, 1, 2 (começo em `civ-15-1-2`, fim em `civ-15-1-2-e-17-…`).
- **Lamec e o setenta e sete; as artes e os ofícios**: Agostinho não comenta (ver `base/_ausentes-agostinho.md`). O
  *Sermão* 83, citado no PEDIDO, trata de Mt 18,22 sem Lamec.
- O `BASE.md` não foi regenerado (é de todos os grupos); os 5 arquivos novos de `base/` entram na próxima vez que o
  `base-indice.py` rodar.

## Pistas não seguidas

- *Contra Iulianum* (as duas obras) foi aberto só pela busca de «Cain/Abel»; não há comentário seguido de Gn 4.
- Os sermões fora da PL (Dolbeau, Mai, Erfurt) não estão no Corpus Corporum; o augustinus.it tem os de Erfurt e os
  «nuovi» (`discorsi/discorsi_nuovi_index.htm`), não abertos.
- *Sermão* 201, 3 (na Epifania) e as *Enarrationes* 39, 40, 58 e 77 repetem o sinal de Caim como figura dos judeus.
- O resto em `base/_pistas-agostinho.md`.

## Para outros capítulos

- **Gn 5,24** (Henoc arrebatado): *Civ.* XV, 19 (PL 41, 462–463); *En. in Ps.* 128, 2 (PL 37, 1689: «houve um tempo em
  que a Igreja estava só em Henoc»).
- **Gn 5,1-3** (o livro das gerações de Adão recomeça depois de Enós): *Civ.* XV, 21 (PL 41, 466–467), a recapitulação
  das duas cidades.
- **Gn 6,1-4** (os filhos de Deus e as filhas dos homens): *Civ.* XV, 22–23 (PL 41, 467–470; não lidos aqui).
- **Gn 6,6** («Paenitet me»): *Locutiones* I (PL 34, 487–488), διενοήθη = «repensou», não «arrependeu-se».
- **Gn 9,25-27** (os filhos de Noé, um reprovado e dois abençoados): *Civ.* XV, 20, 4 (PL 41, 465), numerologia.
