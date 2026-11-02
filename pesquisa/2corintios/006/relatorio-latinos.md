# 2Cor 6: relatório do grupo «latinos» (Agostinho, Padres latinos, medievais latinos), 2026-11-02

Achados em `achados-latinos.json`: **19** (regra «poucos e diferentes»). Por trecho: 1 (vv. 1–10) = 9; 2 (vv. 11–13) = 4;
3 (vv. 14–18) = 6. Relevância: 3 = 12, 2 = 7. Por autor: Agostinho 8, Leão Magno 2, Gregório Magno 2, Tomás 2, e um de
cada: Ambrosiaster, Cassiano, Bento, Tertuliano, Atão de Vercelli.

Textos novos em `textos/`: `agostinho-varios-2cor-6.md` (8 achados, 4 reservas), `latinos-varios-2cor-6.md` (Leão,
Gregório, Cassiano: 6 achados; Ambrósio, Jerônimo, Leão 42: 4 reservas), `tertuliano-ad-uxorem-2-2cor-6.md`,
`bento-regra-prologo-2cor-6.md`, `tomas-suma-1-2-q33-2cor-6.md`. Ambrosiaster, Tomás (comentário) e Atão estão em `base/`.

## Como se procurou

- Lidos os latinos de `base/`: Tomás (lições 1–3) e Ambrosiaster inteiros; Haimo, Atão, Bruno, Hervé, Lanfranco, Sedúlio,
  Lombardo nos versículos-chave (vv. 1–2, 7, 10, 11–13, 14–18); Estius e Lápide só para as pistas dos Padres. Quase tudo
  nos medievais repete Ambrosiaster, Pelágio ou Jerônimo (Belial «sem jugo» está em todos); o que têm de próprio ficou em
  Atão (6,17-18).
- Varredura por frases da Vulgata e da Vetus Latina de cada versículo (texto normalizado: minúsculas, j→i, v→u) nos
  **815 textos da PL** do Corpus Corporum já guardados no disco D: pelas pesquisas anteriores
  (`pesquisa/cache/{nm19,numeros20,numeros22,genesis}-latinos/` e outros: Agostinho 67 obras, Jerônimo 104, Bernardo 72,
  Pedro Damião 72, Ambrósio 45, Gregório 24, Leão, Cassiano, Cipriano, Tertuliano 30, Hilário, Máximo de Turim, Paulino…).
  Cerca de 1 900 ocorrências para os caps. 6 e 7; lidas as dos autores do grupo. Índice e scripts em
  `~/.cache/taioe-2cor-comum/latinos67/` (`indice.tsv`, `bin/busca.py`, `bin/lst.py`, `bin/ver.py`, `bin/ex.py`,
  `meta6.py`, `build.py`).
- Fora do Corpus: Corpus Thomisticum (*Suma* I-II, q. 26–39, `sth2026.html`; II-II, q. 34–43, `sth3034.html`); a *Regra*
  de São Bento na The Latin Library.
- Cada `original` foi extraído por script do texto baixado (marcas de coluna e chamadas de nota de Migne tiradas) e é
  cópia exata dele, com trechos longos cortados por « […] ». Correções mínimas: tirado «(II Cor. VI, 2)» de Migne no meio
  de Gregório, *Regra pastoral*; tirado «---» da digitalização em Gregório, *Morais*.

## O que se achou

| autor | obra | onde | trecho | situação |
|---|---|---|---|---|
| Agostinho | *Os atos de Pelágio* 14, 36 | PL 44, 342 | 1 (v. 1) | **achado** (2): Paulo pede que não se receba a graça em vão para mostrar a vontade; «não trabalhou para receber a graça, recebeu-a para trabalhar» |
| Leão Magno | Sermão 40, 2 (Quaresma 2) | PL 54, 268B–269A | 1 (v. 2) | **achado**: «que há de mais favorável do que estes dias, em que se declara guerra aos vícios?» |
| Gregório | *Regra pastoral* III, 12 | PL 77, 66C–D | 1 (v. 2) | **achado** (2): os sãos não desprezem o tempo; quem não quer quando pode, não poderá quando quiser |
| Agostinho | *A Trindade* VIII, 9, 13 | PL 42, 959–960 | 1 (vv. 2–10) | **achado**: por que nos inflamamos de amor por Paulo ao ler 6,2-10: vemos nele vivida a forma da justiça |
| Ambrosiaster | *In II Cor.* 6,6 | PL 17, 300B | 1 (v. 6) | **achado** (2, base): caridade fingida é a de quem abandona o irmão na necessidade |
| Cassiano | *Conferências* VI, 9–10 | PL 49, 656A–657B | 1 (vv. 7–8) | **achado**: as armas da direita e da esquerda; a prosperidade derruba mais; o «ambidestro» (Aod) |
| Agostinho | *Tratados sobre João* 29, 1 | PL 35, 1628 | 1 (v. 8) | **achado**: «seduzir» é levar de um lugar a outro: «oxalá todos sejamos sedutores» do mal para o bem |
| Agostinho | *Sobre o Sl 48*, s. 2, 5 | PL 36, 559–560 | 1 (vv. 9–10) | **achado**: o «como» só na tristeza e na pobreza, nunca na alegria e na posse; a tristeza é sonho |
| Agostinho | *Sobre o Sl 103*, s. 3, 16 | PL 37, 1371 | 1 (v. 10) | **achado**: Pedro deixou o que tinha e o que desejava ter: «deixou o mundo inteiro e recebeu o mundo inteiro» |
| Agostinho | *Sobre o Sl 118*, s. 10, 6 | PL 37, 1527 | 2 (vv. 11, 13) | **achado**: «a dilatação do coração é o deleite na justiça», dom de Deus; liga-se a 6,16 («como é largo onde Deus anda!») |
| Gregório | *Morais* XXIX, 16, 30 – 17, 31 | PL 76, 493A–B | 2 (vv. 11–13) | **achado**: todo vício estreita, toda virtude dilata; os santos, apertados por fora, se dilatam por dentro |
| Tomás | *Suma* I-II, q. 33, a. 1, obj. 1 e ad 1 | [34960], [34965] | 2 (v. 11) | **achado** (2): a dilatação do amor: o afeto se estende aos outros e cuida do que é deles |
| Bento | *Regra*, Prólogo 44–49 | The Latin Library | 2 (vv. 2, 11, 13) | **achado** (2): «correr e fazer agora»; o caminho começa estreito e, «dilatado o coração», corre-se com doçura |
| Tertuliano | *À esposa* II, 8, 6–9 (cap. IX da PL) | PL 1, 1302A–1304A | 3 (v. 14) | **achado**: «que jugo, o de dois fiéis!»: o casamento dos que rezam, jejuam e cantam juntos |
| Tomás | *Super II Cor.*, cap. 6, l. 3 | [87716] | 3 (vv. 14–15) | **achado** (base): jugo de Deus = caridade, do diabo = iniquidade; Belial «sem jugo» |
| Agostinho | Sermão 23, 7 | PL 38, 158 | 3 (vv. 16, 12) | **achado**: o grande patrono na casinha estreita: Deus, ao vir, não aperta, dilata |
| Leão Magno | Sermão 43, 1 (Quaresma 5) | PL 54, 281A–C | 3 (v. 16) | **achado** (2): o templo, como a casa estragada pela chuva, se repara sempre; «quem é reparado trabalha com o artífice» |
| Agostinho | *Contra a carta de Parmeniano* II, 18, 37 | PL 43, 79 | 3 (vv. 14–17) | **achado**: «saí do meio deles» com o coração, não pelo cisma (contra os donatistas) |
| Atão | *Expositio*, II Cor. 6,17-18 | PL 134, 451B | 3 (vv. 17–18) | **achado** (2, base): se os pais infiéis vos expulsarem, tereis a mim como Pai; «filhas»: os dois sexos |
| Agostinho | *Sobre o Sl 38*, 15 | PL 36, 426 | 1 (vv. 7–8) | reserva boa: as armas são os que louvam e os que censuram, anjos e homens; «com as duas firo o diabo: com as prósperas, se não me corrompo; com as adversas, se não me quebro». Diz o mesmo que Cassiano, mais breve |
| Leão Magno | Sermão 42, 1–2 (Quaresma 4) | PL 54, 275A–276C | 1 (vv. 2–3, 7, 10) | reserva: o jejum como ocasião das armas da justiça; «sempre é rica a pobreza cristã, porque é mais o que tem do que o que não tem». O § 2 (7,1) é achado em 2Cor 7 |
| Agostinho | Sermão 163, 1 | PL 38, 889 | 3 (vv. 13, 16) | reserva boa: na basílica antes pagã, «os ídolos sabiam ficar fixos, não andar; Deus anda em nós se encontrar a largura da caridade». Parecido com o Sermão 23 |
| Agostinho | *Tratados sobre João* 50, 10 | PL 35, 1762 | 3 (v. 15) | reserva: Pedro e Judas recebem do mesmo pão, e «que parte tem o fiel com o infiel?»; tolerar os maus sem dividir o corpo de Cristo (o Tratado 50, 7–8 já está em 2Cor 2; o § 10 é outro trecho) |
| Agostinho | *A doutrina cristã* IV, 20, 42 | PL 34, 109 | 1–2 (vv. 2–11) | reserva: 6,2-11 como modelo do estilo sublime, «vê-o ainda ardendo: a nossa boca está aberta…». Interessa mais à retórica |
| Ambrósio | *Sobre o Sl 118*, 4 (Daleth), 27 | PL 15, 1249C–D | 2 (vv. 11–14) | reserva boa: «o caminho seja mais estreito, o coração mais largo», para hospedar o Pai, o Filho e o Espírito. Parecido com Agostinho, Sl 118 |
| Jerônimo | *Sobre Isaías* VIII (Is 27,1) | PL 24, 305D–306A | 3 (v. 15) | reserva: Belial = «apóstata, prevaricador e sem jugo»; os «filhos da peste» dos LXX são, no hebraico, «filhos de Belial». É a fonte de todos os medievais |
| Jerônimo | Carta 53, 10–11 (a Paulino) | PL 22, 549 | 1 (v. 10) | reserva: «para quem crê, o mundo inteiro é riqueza; o infiel precisa até de um óbolo»; «comida e roupa são as riquezas dos cristãos» |
| Tertuliano | *À esposa* II, 4–6 | PL 1, 1294A–1299A | 3 (v. 14) | reserva: o marido pagão marca o banho no dia de estação e o banquete no dia de jejum; a mulher fiel não visita os irmãos nem beija as correntes dos mártires |
| Tomás | *Super II Cor.*, cap. 6, l. 2–3 (base) | [87715], [87716] | 1–3 | reserva: o «como» de 6,8-10 (o mesmo que Agostinho, Sl 48); o coração estreito de quem só cuida da terra (6,11); Deus está em tudo, mas só habita nos santos, pelo conhecer e amar (6,16); «sair» em espírito, contra os donatistas (6,17) |
| Ambrosiaster | *In II Cor.* 6,10-11 (base) | PL 17, 301B | 1–2 | reserva: os apóstolos possuíam não só os bens, mas os próprios donos; «a mente que tem má consciência treme ao falar, perde o rumo, erra nas palavras» |

Destaques, por ordem: Agostinho, *Sobre o Sl 48* (o «como»); Agostinho, Sermão 23 (o patrono e a casa estreita); Cassiano,
*Conferências* VI (o ambidestro); Agostinho, *Sobre o Sl 103* (Pedro); Gregório, *Morais* XXIX; Tertuliano, *À esposa* II, 8.

## O que não existe ou não rendeu (não procurar de novo)

- **Cipriano**: só cita 6,14-17 nos *Testemunhos* III (lista de versículos, sem comentário) e, no *De lapsis* 6, enumera
  entre os pecados que trouxeram a perseguição «unir-se aos infiéis pelo vínculo do matrimônio, prostituir aos pagãos os
  membros de Cristo» (PL 4, 470A): uma linha, sem 2Cor. Nada sobre 6,2 ou 6,10.
- **Ambrósio, *Sobre Abraão* I, 9, 84** (PL 14, 450D–451A): «como pode concordar a caridade, se a fé discorda?», sobre o
  casamento de Isaac; diz o mesmo que Tertuliano e põe «o judeu» ao lado do pagão: deixado de fora pela regra de não
  desprezar os judeus.
- **Leão**: além dos Sermões 40, 42 e 43, só o Sermão 8 (das Coletas, 3), 5 (PL 54, 159C: 6,14 e 6,17 contra os maniqueus), breve.
- **Gregório**: 6,2 aparece em *Morais* (PL 75, 819; 916), *Homilias sobre os Evangelhos* 12 (já usada em 2Cor 1 para
  outro versículo) e *Diálogos* IV, 39: sempre como «não há penitência depois da morte»; a *Regra pastoral* III, 12 é a
  mais clara. *Homilias sobre Ezequiel* II (PL 76, 1023A: Paulo levava a palma «dos dois lados») e *Regra pastoral* II, 3
  (o sacerdote armado à direita e à esquerda pelo «superumeral») dizem o mesmo que Cassiano.
- **Cassiano, *Instituições* XI, 4** (PL 49, 403A: a vanglória ataca pela direita e pela esquerda): curto, repete VI, 9.
- **Fulgêncio**: no cache só os Sermões (nada); *Ao rei Trasamundo* (pista de 2Cor 4, PL 65, 292A) não baixado.
- **Hilário**, *Tratados sobre os Salmos* (Sl 118, Daleth e He): o coração dilatado «pela fé, capaz da doutrina de Deus»,
  ligado a 6,16 e a 6,12 (PL 9, 531D–532B; 546B–C). Bom, mas diz o mesmo que Agostinho e Ambrósio sobre o Sl 118,32.
- **Pseudo-autores excluídos**: *Sermones suppositii* (pseudo-Agostinho: «nunc tempus acceptabile… post mortem
  vindictae»), *Breviarium in Psalmos* (pseudo-Jerônimo), *Dialogus quaestionum* (pseudo-Agostinho: «unde dilatatur cor
  nisi per charitatem»), *Meditationes* (pseudo-Agostinho), *Commentarii in epistolas Pauli* da PL 30 (Pelágio) e a Carta
  148 «a Celância» (atribuída a Jerônimo, provavelmente de Pelágio ou do seu círculo).
- **Boaventura e Anselmo**: nada. Do Anselmo há só o *Cur Deus homo* no cache; o comentário paulino «de Anselmo» citado
  por Lápide é de Hervé.
- **Agostinho, «não deixes para amanhã»** (o *cras, cras* do corvo, Sermão 82, 14; *Confissões* VIII, 12, 28, «até quando, amanhã e amanhã?»): não citam 2Cor 6,2;
  não entrou.

## Dúvidas

- **Tertuliano, *À esposa* II, 8**: não cita 2Cor 6,14; o «Apóstolo» do fim é 1Cor 7,39 («só no Senhor»), que é o tema do
  livro. Entrou porque é o melhor comentário latino ao «jugo» (e usa a palavra: «quale jugum fidelium duorum»). Tertuliano
  escreveu a obra no período católico. Numeração: na PL é o cap. IX; nas edições modernas, II, 8, 6–9 (o Catecismo, n. 1642,
  cita esta passagem como *Ad uxorem* 2, 8, 6-7).
- **Bento, *Regra***: o «dilatato corde» retoma o Sl 118,32, não 2Cor 6,11; entra como eco. Edição de base da Latin Library
  não declarada; não conferido com a PL 66.
- **Agostinho, *A Trindade* VIII**: o original corta a longa citação de 6,4-10 com «[…]» logo depois de «ministerium
  nostrum»; o leitor pode precisar de ver que Agostinho cita até «omnia possidentes».
- **Agostinho, Sl 48 e Tomás**: Tomás (l. 2, base) faz a mesma observação do «como» (só nos bens e males temporais Paulo
  põe «ut, sicut, quasi, tamquam»); ficou o de Agostinho, mais vivo.
- **Tomás, *Suma* I-II, q. 33**: começa por uma objeção («Pode parecer que…»), sem o rótulo; a resposta (ad 1) é a parte boa.
  Se parecer técnico demais, a reserva é Tomás, *Super II Cor.* l. 3: «o coração é estreito quando só cuida da terra; largo
  quando deseja grandes coisas».
- **Agostinho, *Contra Parmeniano***: «isti» são os donatistas; o nome entrou entre colchetes na tradução.
- **Leão**: Sermões 40 e 43 na numeração da PL (Al. 39 e 41). O texto de Leão lê «tempus acceptum».
- Colunas da PL: as do Corpus Corporum (sem letra nas obras de Agostinho).

## Fontes e endereços (novos em relação a `../004/relatorio-latinos.md`)

- Os 815 textos do Corpus Corporum já baixados estão espalhados em `pesquisa/cache/*-latinos/` e `pesquisa/cache/genesis/`
  (arquivos `cc_<idno>.txt`): antes de baixar de novo, procurar ali (`~/.cache/taioe-2cor-comum/latinos67/indice.tsv` lista
  autor, obra e caminho). Novos usados aqui: Leão, Sermões **7631**; Gregório, *Regra pastoral* **21435**, *Morais* (2ª
  parte) **8054**; Cassiano, *Conferências* **7530**, *Instituições* **7531**; Tertuliano, *À esposa* **42** (o subconjunto
  da PL tem Tertuliano, ao contrário do que dizia o relatório de 2Cor 4: autor «Tertullianus»); Agostinho, *Atos de Pelágio*
  **7474**, *Contra Parmeniano* **7460**, Sermões de Scripturis **7334**; Ambrósio, *Sobre o Sl 118* **6966**.
- Corpus Thomisticum, *Suma*: os arquivos juntam várias questões; I-II, q. 26–39 em `sth2026.html`, q. 72 em `sth2072.html`;
  II-II, q. 34–43 em `sth3034.html` (lista em `https://www.corpusthomisticum.org/iopera.html`). `sth2035.html` não existe.
- São Bento: `https://www.thelatinlibrary.com/benedict.html` (Regra inteira, latim).

## Pistas não seguidas

- Liturgia antiga: o responsório «Ecce nunc tempus acceptabile… commendemus nosmetipsos in multa patientia, in jejuniis
  multis, per arma justitiae» do *Liber responsalis* (Gregório, PL 78, 751–752) é o da Quaresma romana; fica para o grupo da
  liturgia.
- Máximo de Turim, Sermões (PL 57, 585; 747–750): 6,2 como «dias de remédio celeste»; 6,13-16 longamente, «se somos templo
  de Deus, não nos tornemos sepulcro do diabo». Coleção misturada, atribuições a conferir.
- Pedro Damião, *Coletânea do AT* (PL 145, 1011A): o «copo largo» da palavra (6,11-12); Cartas: 6,14 contra os clérigos
  proprietários. Não lidos por inteiro.
- Bernardo: *Sermões sobre o Cântico* 27, 10 (PL 183, 918D: «quanta largura daquela alma» que acolhe Deus, com 6,16 e o
  Sl 118,32) e *Sermões diversos* 4, 1 (PL 183, 552A: «eis agora o tempo de buscar, eis agora o dia de encontrar»). Bons, não
  traduzidos.
- Paulino de Nola, Carta 37, 7 (PL 61, 356C): aplica 6,6-10 a um bispo provado; Hilário, *Sobre o Sl 118* (acima).
- Sermões de Agostinho fora dos Maurinos (Dolbeau, Mainz) e o Biblindex: não varridos.

## Para outros capítulos

- **2Cor 7,1**: Leão, Sermão 42, 2 (achado no cap. 7); **7,5**: Agostinho, Carta 78, 7, e *Sobre o Sl 55*, 6 (achado no cap. 7).
- **2Cor 9,7** («Deus ama quem dá com alegria»): Agostinho, Sermão 165 (PL 38, 904: «a largura é a caridade… se dá triste,
  perde o que dá»), com 6,13-14; Tomás, *Suma* I-II, q. 39, a. 2, obj. 2 (dar com tristeza tira o mérito);
  Bernardo, *Sermões diversos* 123, 2 (PL 183, 746B: «com o coração dilatado… sabendo que Deus ama quem dá com alegria»).
- **2Cor 11,29** («quem tropeça, que eu não me abrase?»): Ambrosiaster sobre 6,6 e Agostinho, *Sobre o Sl 55*, 6.
- **2Cor 12,9-10**: Gregório, *Morais* XXIX, 17, 31 continua com Fl 1,12-13 (as correntes de Paulo).
