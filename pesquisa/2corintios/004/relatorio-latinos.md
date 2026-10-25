# 2Cor 4: relatório do grupo «latinos» (Agostinho, Padres latinos, medievais latinos), 2026-10-24

Achados em `achados-latinos.json`: **20** (regra «poucos e diferentes»). Por trecho: 1 (vv. 1–6) = 6; 2 (vv. 7–15) = 7;
3 (vv. 16–18) = 7. Relevância: 3 = 17, 2 = 3. Por autor: Agostinho 9, Ambrósio 3, Tomás 2, Gregório Magno 2, e um de
cada: Atão de Vercelli, Tertuliano, Bernardo, Leão Magno.

Textos novos em `textos/`: `agostinho-varios-2cor-4.md` (18 passagens, achados e reservas), `latinos-varios-2cor-4.md`
(Ambrósio, Gregório, Leão, Jerônimo: 11), `tertuliano-varios-2cor-4.md` (4), `bernardo-varios-2cor-4.md` (4) e
`tomas-suma-1-q65-2cor-4.md` (Suma I, q. 65, a. 1, reserva).

## Como se procurou

- Lidos inteiros os latinos de `base/`: Ambrosiaster, Tomás (lições 1–5), Atão, Bruno, Haimo, Hervé, Lanfranco, Lombardo,
  Sedúlio, Cassiodoro; Estius e Lápide nos versículos-chave e nas citações dos Padres (que serviram de pista: Estius aponta
  *Contra Fausto* XXI, 2 e 9, *Contra o adversário da Lei* II, 7–8, Tertuliano e a *Suma* I, q. 65; Lápide aponta Bernardo,
  *Qui habitat* 17 e *De diversis* 1, e Agostinho, *Sl 93*).
- Varredura por frases da Vulgata e da Vetus Latina de cada versículo (texto normalizado: minúsculas, j→i, v→u) em ~560
  textos da PL do Corpus Corporum: o cache das conversas anteriores no Linux (`4b54597f…/scratchpad/p-latinos/dl`, 498
  textos: Agostinho, Ambrósio, Jerônimo, Gregório, Leão, Bernardo em parte, Pedro Damião, Ruperto, Pascásio…) mais 45 textos
  baixados agora (Agostinho: *Contra Fausto*, *A Trindade*, *Contra Adimanto*, *A Cidade de Deus*, a 2ª parte das
  *Enarrationes* (Sl 80–150), *Sermones* 1, 2 e *inediti*, obras antipelagianas; Cipriano inteiro; Hilário: *A Trindade*,
  *Tratados sobre os Salmos*, *Sobre Mateus*; Cassiano; Fulgêncio; Bernardo: *Sermões diversos*, *Cântico*, *Cartas*,
  *Consideração*). Padrões usados, por versículo, em `pesq-latinos/bin/tally.py` (scratchpad desta conversa).
- Fora do Corpus: Tertuliano (*Contra Marcião* V, *A ressurreição da carne*, *Escorpião*) na The Latin Library; Tomás,
  *Suma* I, q. 65 no Corpus Thomisticum.
- Cada `original` foi extraído por script do texto baixado (marcas de coluna e chamadas de nota de Migne tiradas) e é
  cópia exata dele, com trechos longos cortados por « […] ». Correções mínimas, todas de erro de digitalização ou de
  tipografia: Carta 188 «proficienter habentis» → «habeatis»; fragmento de São Quadrato «propter quod elloquimur» →
  «et loquimur»; *O bem da morte* «post mortem. hoc est» → «post mortem, hoc est»; Tertuliano «gratiam----vide quantam,» →
  «gratiam (vide quantam),»; Leão «PLUS EST», «AD PRAESENTIA» (versaletes de Migne) → minúsculas; *Contra Fausto* «sed
  justitia:» → «sed justitia.» antes do corte.

## O que se achou

| autor | obra | onde | trecho | situação |
|---|---|---|---|---|
| Atão | *Expositio*, II Cor. 4,1 | PL 134, 435B–C | 1 (v. 1) | **achado**: desanima quem pregou por gosto próprio, não quem recebeu o ministério por misericórdia |
| Agostinho | *Contra Fausto* XXI, 2 e 9 | PL 42, 389 e 394 | 1 (v. 4) | **achado**: as duas leituras (o Deus verdadeiro, por justiça; o diabo, por sugestão); «o diabo sugere, o homem consente, Deus abandona» |
| Agostinho | *Contra o adversário da Lei* II, 7, 29 – 8, 30 | PL 42, 655–656 | 1 (vv. 3–4) | reserva: mesma doutrina, contra o marcionita; «ilumina por misericórdia, cega por juízo» |
| Tomás | *Super II Cor.*, cap. 4, l. 2 | [87705] | 1 (vv. 3–4) | **achado**: três leituras do «deus deste século»; a 3ª, o deus de cada um é o seu fim último (os luxos, as honras) |
| Tomás | id., l. 2 | [87705] | 1 (v. 5) | **achado**: «servo é quem existe para o proveito do senhor»; o ministro que não busca o bem dos fiéis é tirano |
| Tomás | id., l. 2 | [87705] | 1 (v. 4) | no texto (base): Cristo imagem perfeita (semelhança, origem, igualdade): a efígie do rei na moeda × o filho do rei. Lombardo copia a mesma ideia de Agostinho, *83 Questões*, q. 74 (PL 40, 85–86: o espelho, pais e filhos, «dois ovos iguais»). Ficou para os gregos (Atanásio, Basílio) |
| Ambrósio | *Sobre o Salmo 43*, 87 | PL 14, 1130C–1131B | 1 (v. 6) | **achado**: o rosto de Deus é Cristo, «brilho eterno das almas»; Zaqueu «viu Cristo e encontrou a luz». É o texto do Ofício das Leituras (quinta da 16ª semana) com 2Cor 4,5-18 |
| Agostinho | Sermão 223, 1 (Vigília Pascal) | PL 38, 1092 | 1 (v. 6) | **achado**: os recém-batizados de branco: o Deus que fez a luz no 1º dia fez deles dia |
| Agostinho | Sermão 186, 3 (Natal) | PL 38, 1000 | 1/3 (vv. 6, 16) | reserva: o dia de Natal, desde o qual cresce a luz, significa a obra de Cristo, que renova de dia em dia o homem interior |
| Agostinho | *O espírito e a letra* 11, 18 | PL 44, 219–220 | 1 (vv. 2, 5–7) | reserva: a «astúcia» de 4,2 é a hipocrisia dos que querem parecer justos por si; «a ciência da glória é saber que ele é a luz que ilumina as nossas trevas» |
| Gregório | *Regra pastoral* II, 6 (= *Morais* XXVI, 26, 45–46) | PL 77, 36B–C | 1 (v. 5) | **já usado no cap. 1** (para 1,24): não repetir. *Morais* VI (PL 75, 742B) e XXIV (PL 76, 312B) dizem o mesmo (humildade e disciplina) |
| Agostinho | *Questões sobre o Heptateuco* VII (Juízes), 49 | PL 34, 815 | 2 (v. 7) | **achado**: as bilhas de Gedeão (Jz 7) prefiguram os santos: quebrado o vaso no martírio, a luz brilha mais. Tomás (l. 3) cita a mesma passagem de Juízes |
| Gregório | *Morais* III, 9, 15 | PL 75, 606C–D | 2 (v. 7) | **achado**: Jó, vaso rachado pelas úlceras, tesouro íntegro por dentro |
| Agostinho | Carta 188, 6 | PL 33, 851 | 2 (v. 7) | **achado**: «vossos, mas não de vós», como o pão «nosso» que pedimos: «dá-nos» |
| Tertuliano | *A ressurreição da carne* 44 | The Latin Library | 2 (vv. 6–7, 10–11) | **achado**: a carne, «depósito do tesouro divino», templo de Deus e sepulcro de Cristo, há de ressuscitar |
| Tertuliano | *Contra Marcião* V, 11, 9–16; *Ressurreição* 40; *Escorpião* 13, 7–8 | Latin Library | 1–3 | reserva: a pontuação «In quibus Deus | aevi huius» contra Marcião (11, 9–11); «Deus seria ingrato e injusto se não ressuscitasse a substância em que tanto se sofre por ele» (11, 15); o homem exterior não é a carne condenada (*Ress.* 40); 2Cor 4,8-18 como prova de que Paulo quis o martírio (*Escorpião*) |
| Ambrósio | *O bem da morte* 3, 9 | PL 14, 543D–544A | 2 (vv. 10–12) | **achado**: há uma «boa morte» nesta vida; «a morte de um só, de quantos povos edificava a vida!» |
| Ambrósio | *Os deveres* II, 28, 140–141 | PL 16, 141B–C | 2 (v. 7) | reserva boa: São Lourenço mostra os pobres, «tesouros da Igreja», com 4,7 |
| Agostinho | Sermão 274 (São Vicente) | PL 38, 1252–1253 | 2 (v. 9) | reserva: o corpo do mártir lançado ao mar «dizia calado: somos derrubados, mas não perecemos» |
| Agostinho | Sermão de São Quadrato (fragmento de Beda) | PL 39, 1731 | 2 (v. 13) | **achado**: «crendo, alcançaram a vida; falando, encontraram a morte» |
| Agostinho | *Sobre o Sl 115*, 1–2 | PL 37, 1491–1492 | 2 (v. 13) | reserva: «não crê perfeitamente quem não quer dizer o que crê» (Hervé e Lombardo copiam) |
| Agostinho | *Tratados sobre João* 45, 9 | PL 35, 1722–1723 | 2 (v. 13) | **achado**: «os tempos mudaram, a fé não»: «virá» e «veio». O mesmo em *Sobre o Sl 50*, 17, *Contra duas cartas* III, 4, 11 e *A graça e o livre-arbítrio* 14, 28 («não diz ciência da fé, mas espírito da fé»): reserva |
| Ambrosiaster | *In II Cor.* 4,15 | PL 17, 292B | 2 (v. 15) | no texto (base), reserva boa: o banquete farto com poucos convidados é uma afronta a quem o deu; por isso Paulo quer a ação de graças «de muitos» (Atão e Lombardo copiam). Ficou fora por espaço |
| Agostinho | *A Trindade* XIV, 17, 23 | PL 42, 1054–1055 | 3 (v. 16) | **achado**: tirar a flecha (o Batismo) e curar a ferida (a renovação diária) |
| Agostinho | Carta 147, 2 (a Paulina) | PL 33, 597 | 3 (v. 16) | **achado**: a velhice: o homem interior «não murchou» com os anos |
| Agostinho | *O perdão dos pecados* II, 7, 9; *Sobre o Sl 131*, 1 | PL 44, 157; PL 37, 1716 | 3 (v. 16) | reserva: «quem ainda se renova não está todo renovado»; «não progridamos de modo que de novos fiquemos velhos, mas que a novidade cresça» |
| Gregório | *Morais* VI, 13, 15 | PL 75, 737C | 3 (v. 16) | **achado**: «o homem nasce para o trabalho, e a ave para o voo» |
| Gregório | *Morais* X, 18, 35 | PL 75, 940D–941B | 3 (vv. 16–17) | reserva: «quando te julgares consumido, nascerás como a estrela da manhã»; Paulo «não se sabia consumido, julgava-se» |
| Jerônimo | Cartas 108, 18 (Santa Paula); 65, 4; 22, 4 | PL 22, 893–894; 625; 396 | 2–3 | reserva: Santa Paula repetia 4,16-18 nas provações e 4,7 nas doenças; «não há tempo em que o santo não mude» |
| Agostinho | *Sobre o Sl 93*, 23–24 | PL 37, 1211–1212 | 3 (vv. 17–18) | **achado**: o Reino à venda; um descanso eterno valeria trabalho eterno, mas Deus pede «uma moedinha» |
| Bernardo | *Qui habitat* 17, 3 | PL 183, 251D–252A | 3 (vv. 17–18) | **achado**: «não disse: será recompensado, mas: produz»; a glória escondida na tribulação como o fruto na semente |
| Bernardo | *Sermões diversos* 1, 7–8 | PL 183, 540D–542A | 3 (v. 17) | reserva boa: «Vai, continua a murmurar: é longo, é pesado!… Passa a hora, passa a pena; a glória fica toda inteira» |
| Bernardo | *Cântico* 43, 1; *Advento* 3, 6 | PL 183, 993D; 46C | 2–3 | reserva: o ramalhete de mirra que vira «monte de glória»; o tesouro em vaso de vidro, e mais frágil ainda, de barro |
| Tomás | *Super II Cor.*, l. 5 | [87708] | 3 (v. 17) | no texto (base): o «peso» de glória porque o peso arrasta tudo consigo (alma e corpo) e porque só se pesa o que é precioso (Bruno: «o que na balança tem peso é mais caro») |
| Leão Magno | Sermão 27, 6 (Natal) | PL 54, 220B–221B | 3 (v. 18) | **achado**: contra quem saudava o sol na escadaria de São Pedro: usar bem as criaturas; «nascemos para o presente, renascemos para o futuro» |
| Tomás | *Suma* I, q. 65, a. 1, ad 1 e ad 3 | Corpus Thomisticum [31165]–[31167] | 3 (v. 18) | reserva: 4,18 não diz que o visível é mau; fala dos bens visíveis como prêmio; as criaturas por si levam a Deus. Diz o mesmo que Leão, menos bonito |
| Ambrósio | *Os mistérios* 3, 8 | PL 16, 391B–C | 3 (v. 18) | **achado**: ao recém-batizado: viste água, mas não só; crê na presença que não se vê. *Os sacramentos* I, 3, 10 (PL 16, 420C) diz o mesmo |
| Agostinho | Sermão 105, 7 | PL 38, 621 | 3 (v. 18) | reserva boa: a esperança é um ovo: «é ovo, e ainda não é pinto», coberto pela casca, não se vê |

Destaques, por ordem: Agostinho, *Sobre o Sl 93*, 24 (o Reino à venda); Bernardo, *Qui habitat* 17, 3; Agostinho, Carta 147
(a velhice); Agostinho, *Questões sobre Juízes* 49 (Gedeão); Gregório, *Morais* VI (a ave); Agostinho, Sermão 223
(os neófitos).

## O que não existe ou não rendeu (não procurar de novo)

- **Cipriano**: nenhuma citação de 2Cor 4 nos tratados nem nas cartas (varredura por todas as frases do capítulo).
  O *De XII abusionibus saeculi* que cita 4,18 é pseudo-Cipriano (irlandês, séc. VII).
- **Hilário**: nada sobre 2Cor 4 nos *Tratados sobre os Salmos* (que não incluem o Sl 115), em *A Trindade* nem em
  *Sobre Mateus*; só «imago Dei» de Cl 1,15.
- **Cassiano** e **Fulgêncio**: só citações soltas (Cassiano, *Conferências*, PL 49, 565B e 574A: v. 18; 933B e 952A:
  v. 17; 949C: v. 7, entre as «regras eclesiásticas»; Fulgêncio, *Verdade da predestinação*, PL 65, 632A: v. 13, repete
  Agostinho).
- **Agostinho, *Contra Adimanto*** e ***A Cidade de Deus***: nada sobre o «deus deste século» (o que há está em *Contra
  Fausto* XXI e *Contra o adversário da Lei* II, 7–8). *A Cidade de Deus* XIV, 3 (PL 41, 405) cita 4,16 só como ponte para 5,1.
- **Leão**: além do Sermão 27, só o Sermão 49 (PL 54, 302B: «está escondido o caminho das virtudes»), breve; as Cartas
  (PL 54, 651B, 660B) falam de «vasos de barro» de 2Tm 2,20, não de 2Cor 4.
- **Guilherme de São Teodorico**: o Corpus Corporum (PL) só tem o «Liber I» (cps_2.GuSTh.LibI); as obras espirituais
  não estão lá. Não procurado fora.
- Excluídos por autoria ou regra: *Breviarium in Psalmos* (pseudo-Jerônimo: o tesouro são «as palavras rústicas da
  Escritura»); *Expositio super Cantica* de «Gregório» depois de Ct 1,8 (é de Roberto de Tombelaine: as nozes, «doces por
  dentro, vis por fora»); *Hypomnesticon* e *Sermones suppositii* (pseudo-Agostinho); Ruperto, Gerhoh, Hervé (não santos;
  Hervé só copia Agostinho e Ambrosiaster). Pela regra de não desprezar os judeus, nada de Cassiodoro («corda dementium
  Judaeorum», 4,3) nem do Ambrosiaster sobre o véu «sobretudo nos judeus».
- Isidoro, *Sentenças* I (PL 83, 687A): o tesouro é a sabedoria escondida nas palavras simples da Escritura. É a leitura
  «simbólica» de Orígenes (Lápide a cita); deixada de fora como alegoria do texto, não do sentido de 4,7.

## Dúvidas

- **Agostinho, fragmento de São Quadrato** (PL 39, 1731): conservado só por Beda (excertos sobre II Cor. 4, ainda inéditos
  quando Migne o publicou); não se conhece o sermão inteiro. A mesma frase está em Hervé (base, 1038D), sem nome.
- **Tertuliano**: a The Latin Library (digitalização de R. Pearse) não diz a edição de base; a coluna da PL 2 não foi
  conferida (*De resurrectione carnis*, PL 2, 791–886, cap. 44 por volta de 856–858). Tertuliano escreveu *A ressurreição
  da carne* já no período montanista; a doutrina do trecho é a da Igreja (ressurreição da carne). Tomás (base, l. 5) e
  Lápide lembram que Tertuliano errou ao ler em 4,16 uma alma corpórea (*A alma* 9): esse ponto não entrou.
- **Agostinho, *Questões sobre Juízes* 49**: o trecho inclui «os trezentos homens (número que remete ao sinal da cruz)»
  (300 = T, a letra grega da cruz). É detalhe alegórico dentro de uma leitura figurada (Gedeão prefigura os santos); se o
  Gere achar demais, cortar só esse inciso.
- **Agostinho, *Sobre o Sl 93***: «siliqua» é a menor moeda (1/24 do sólido; Agostinho acabou de falar de sólido,
  semionça e libra); traduzida «moedinha». O latim de Agostinho para καθ’ ὑπερβολὴν εἰς ὑπερβολήν é «juxta incredibilem
  modum, et in incredibilem modum» («num grau incrível e para um grau incrível»).
- **Ambrósio, *Sobre o Salmo 43***: o número 87 é o da PL (Explanatio psalmi XLIII). O Ofício das Leituras (quinta da 16ª
  semana) usa outro corte deste comentário; conferir com o grupo «modernos» (liturgia) para não repetir.
- **Leão, Sermão 27**: na numeração antiga é o «Sermo XXVI» (Natal 7). Os dois versaletes de Migne foram passados para
  minúsculas.
- **Tomás, l. 2 (deus deste século)**: o achado só traz a 3ª leitura; as duas primeiras (o Deus verdadeiro que tira a
  graça; o diabo, deus «por imitação» dos mundanos) estão no achado de Agostinho. Bruno (base) tem as mesmas três leituras e
  uma quarta: o Deus que governa também a terra, contra os que diziam que o mundo vai ao acaso.
- **Atão**: relevância 2; a ideia (o ministério recebido por misericórdia não desanima) também está em Ambrosiaster e
  Tomás, menos incisiva.
- Agostinho ficou com 9 dos 20. Se for preciso equilibrar, os primeiros a sair são o *Tratado 45* (v. 13: há o fragmento
  de Quadrato) e a Carta 188 (v. 7: há Gedeão, Jó e Tertuliano); as melhores reservas de outros autores são Ambrosiaster
  (v. 15), Bernardo, *Sermões diversos* 1 (v. 17) e Ambrósio, *Os deveres* II, 28 (v. 7).
- Colunas da PL: as do Corpus Corporum; nas obras de Agostinho e nas cartas de Jerônimo o Corpus marca só o número da
  coluna, sem letra.

## Fontes e endereços (novos em relação a `../003/fontes-latinos.md`)

- Corpus Corporum, textos usados pela primeira vez: Agostinho, *Contra Fausto* **7432**, *A Trindade* **7441**,
  *Enarrationes* (Sl 80–150) **21385** (a parte 1, Sl 1–79, é 7329), *Contra Adimanto* **21356**, *A Cidade de Deus* **21364**,
  *Sermones inediti* **7505**; Ambrósio, *O bem da morte* **6953**, *Os mistérios* **6971**; Leão, Sermões **7631**
  (cps_2.LeoI.Sermon9); Bernardo, *Qui habitat* **11246**, *Sermões diversos* **11257**, *Cântico* **11258**, *Cartas*
  **21392**; Cipriano **94–130**; Hilário **6863, 6864, 6871, 21450**; Cassiano **7530–7531**; Fulgêncio **7809–7816**.
  Padrão de busca das obras de um autor: `navigate.php?load=/38/<autor>/<obra>` (autor: Agostinho 900, Bernardo 2268,
  Cipriano 878, Hilário 927, Cassiano 1063, Fulgêncio 1153, Leão 1098, Guilherme de São Teodorico 2283).
- Tertuliano não está no subconjunto PL do Corpus Corporum (só «Auctor incertus (Tertullianus?)», 868): usar
  `https://www.thelatinlibrary.com/tertullian/tertullian.<obra>.shtml` (marcionem5, resurrectione, scorpiace, anima).
- Corpus Thomisticum, *Suma* I, q. 65: `https://www.corpusthomisticum.org/sth1065.html` (padrão da I: `sth1NNN.html`).
- Scripts desta busca em `/tmp/claude-1000/-home-geremias-Geremias-Software-MEU-taioe/98a6d4f8-8ddd-46c9-b621-058e5f0bc420/scratchpad/pesq-latinos/`:
  `bin/srch.py` (busca), `bin/tally.py` (contagem por versículo, grava `hits.json`), `bin/lst.py` (lista por versículo),
  `bin/show.py` (contexto), `bin/ex.py` + `specs.py` (originais exatos), `build.py` (JSON), `textos.py` (arquivos de
  `textos/`).

## Pistas não seguidas

- Agostinho, *83 Questões*, q. 74 (PL 40, 85–86): imagem, igualdade e semelhança (o espelho, pais e filhos, «dois ovos
  iguais»), fonte de Lombardo sobre «Cristo, imagem de Deus» (4,4); é sobre Cl 1,15.
- Leão, Sermão 70, 5 (PL 54, 383A–B): «a Paixão do Senhor se prolonga até o fim do mundo… em todos os que sofrem pela
  justiça, ele padece com eles». Paralelo forte de 4,10-11, mas sem citar 2Cor 4. Haimo (base, 624D) diz o mesmo com o
  «Venio Romam iterum crucifigi» (o *Quo vadis*), e Atão (438B): «Jesus morre todos os dias nos seus membros».
- Ambrósio, *Sobre o Sl 118*, 14 (Nun), 7 (PL 15, 1392A): «brilha no barro, fulge no vaso de barro aquele tesouro»
  (Cristo, lâmpada); *O Espírito Santo* II (PL 16, 797C–798A): 4,6 como prova da divindade do Espírito. Não lidos por inteiro.
- Pedro Damião, Cartas (PL 144, 475B–C): a quem sofre, «levarás pesos de ouro precioso» por 4,17, e a comparação palavra
  por palavra (momentâneo × eterno, leve × peso). Pascásio Radberto tem várias citações de 4,16-18 não lidas.
- Gregório, *Morais* V (PL 75, 718B): 4,7 com 5,1 («habitamos casas de barro», Jó 4,19).
- Tomás fora do comentário e da q. 65: II-II, q. 124 (o martírio), *Super Rom.* 8,18 e *Super Heb.* (o «peso» da glória).
- Sermões de Agostinho fora dos Maurinos (Dolbeau, Mainz) e o Biblindex: não varridos.
- Guilherme de São Teodorico, Ricardo de São Vítor, Boaventura (*Itinerarium*, *Breviloquium*): não procurados.

## Para outros capítulos

- **2Cor 5,1-4** (a tenda terrestre): Tertuliano, *Contra Marcião* V, 12, 1–3 (logo depois do trecho de 2Cor 4, em
  `textos/tertuliano-varios-2cor-4.md` só até V, 11) e *A ressurreição da carne* 41–43; Ambrósio, *O bem da morte* 3, 9
  termina com 5,1 («para que a nossa casa terrestre se desfaça e se abra a morada celeste»); Agostinho, *A Cidade de Deus*
  XIV, 3 (PL 41, 405): 4,16 → 5,1; Gregório, *Morais* V (PL 75, 718B).
- **2Cor 12,9-10** («quando sou fraco, então sou forte»): Jerônimo, Carta 108, 18 (Santa Paula) junta 12,10 com 4,7 e 1,5-7.
- **2Cor 6,9-10** («como moribundos, e eis que vivemos… como nada tendo, e possuindo tudo»): Gregório, *Morais* X, 18, 35
  (PL 75, 941A–B); Fulgêncio, *Ao rei Trasamundo* (PL 65, 292A); Tomás, l. 3 (base), junto com 4,8.
- **2Cor 1,22 e 5,5** (o penhor): Bernardo, *Sermões diversos* 1, 7 chama as primícias do Espírito «arra da herança
  paterna» (PL 183, 540D).
