# 2Cor 5: relatório do grupo «latinos» (Agostinho, Padres latinos, medievais latinos), 2026-11-02

Achados em `achados-latinos.json`: **20** (regra «poucos e diferentes»). Por trecho: 1 (vv. 1–10) = 9; 2 (vv. 11–17) = 6;
3 (vv. 18–21) = 5. Relevância: 3 = 17, 2 = 3. Por autor: Agostinho 8, Gregório Magno 4, Bernardo 3, Tomás 2, e um de cada:
Ambrosiaster, Tertuliano, Leão Magno.

Textos novos em `textos/`: `agostinho-varios-2cor-5.md` (8 achados + 3 reservas), `bernardo-varios-2cor-5.md` (3 + 2),
`latinos-varios-2cor-5.md` (Gregório e Leão: 5 achados; reservas de Gregório, Ambrósio, Leão e Ricardo de São Vítor) e
`tertuliano-ressurreicao-2cor-5.md` (*A ressurreição da carne* 41–43 inteiros e *Contra Marcião* V, 12, 1–3).

## Como se procurou

- Lidos inteiros os latinos de `base/` (Ambrosiaster, Tomás, lições 1–5); Estius, Lápide e os medievais carolíngios
  (Haimo, Atão, Bruno, Hervé, Lombardo, Lanfranco, Sedúlio, Cassiodoro) nos versículos-chave. Deles só ficaram Ambrosiaster
  e Tomás: os outros repetem Ambrosiaster ou Agostinho (Lombardo marca as fontes).
- Varredura por frases da Vulgata e da Vetus Latina de cada versículo (texto normalizado: minúsculas, j→i, v→u) em **813
  textos da PL** do Corpus Corporum que já estavam nos caches das pesquisas anteriores (`pesquisa/cache/*/cc_<id>.txt`:
  Agostinho quase inteiro, Ambrósio, Jerônimo, Gregório, Leão, Bernardo, Cipriano, Tertuliano, Hilário, Cassiano, Pedro
  Damião, Ricardo de São Vítor, Beda…). Contagem por versículo: v. 10 = 227 citações, v. 17 = 134, v. 19 = 117, v. 6 = 111,
  v. 16 = 96… Baixados agora só quatro textos de Fulgêncio (Corpus 7809, 7810, 7813, 7814), lidos e apagados.
- Scripts em `~/.cache/taioe-2cor-comum/latinos5/`: `bin/idx.py` (índice dos caches), `bin/srch.py` + `pats.json`
  (busca, grava `hits.json`), `bin/lst.py` (lista por versículo e autor), `bin/show.py` e `bin/where.py` (contexto, coluna
  e sermão), `bin/ex.py` (corte exato do original), `specs.py` (cortes e traduções), `build.py` (JSON) e `textos.py`.
- Cada `original` é cópia exata do texto baixado, com trechos cortados por « […] ». Correções mínimas: Gregório,
  *Hom. Ezequiel* «inimicitias mimicitiis» → «inimicitiis» (erro da digitalização); Tomás, os asteriscos de itálico do
  Corpus Thomisticum tirados e «duo desideria» com maiúscula no começo do excerto.

## O que se achou

| autor | obra | onde | trecho | situação |
|---|---|---|---|---|
| Bernardo | Carta 254, 1, ao abade Guarino de Aulps | PL 182, 459A–C | 1 (v. 1) | **achado**: o velho abade que recomeça a reforma; «não teme a ruína da velha morada quem vê subir o edifício espiritual» |
| Gregório | *Diálogos* IV, 25 (26) | PL 77, 356D–357B | 1 (vv. 1, 8) | **achado**: as almas dos justos perfeitos vão logo ao céu; no juízo ganham também a alegria do corpo |
| Agostinho | Sermão 299, 9 (Pedro e Paulo) | PL 38, 1374–1375 | 1 (vv. 2–4) | **achado**: «ó voz da natureza!»; a túnica terrena e a celeste; «nem embaixo, nem em cima: em parte nenhuma a morte» |
| Agostinho | Sermão 170, 10 | PL 38, 932 | 1 (vv. 5–7) | **achado**: o penhor é «participação, mas ainda distante»; «quem chama os peregrinos há de alimentá-los na pátria» |
| Ambrosiaster | *In II Cor.* 5,6-7 | PL 17, 294B–C | 1 (vv. 6–7) | **achado**: se Deus está em toda parte, como estamos longe dele? Porque não o vemos |
| Agostinho | Sermão Denis 10, 3 (Sl 149) | PL 46, 845 | 1 (v. 6) | **achado** (relev. 2): as Escrituras são «cartas da nossa pátria» que nos chamam de volta; as duas asas da caridade |
| Tomás | *Super II Cor.*, c. 5, l. 2 | [87710] | 1 (v. 8) | **achado**: o desejo da natureza (medo da morte) e o da graça (ousadia); os santos não só não se entristecem, mas se alegram |
| Tertuliano | *A ressurreição da carne* 43 | PL 2, 855B–856B | 1 (vv. 6–10) | **achado** (relev. 2): «quem peregrina há de voltar para casa»; «se todos, então inteiros»: o que se fez pelo corpo é pesado pelo corpo |
| Agostinho | *Enchiridion* 110 | PL 40, 283 | 1 (v. 10) | **achado**: a Missa e as esmolas pelos defuntos não contradizem o tribunal de Cristo; «é aqui que se adquire todo o mérito» |
| Gregório | *Regra pastoral* II, 5 | PL 77, 32B–33B | 2 (v. 13) | **achado**: Paulo no terceiro céu e no leito dos casados; a escada de Jacó; Moisés que entra e sai da tenda |
| Agostinho | *A Cidade de Deus* XX, 6, 1 | PL 41, 665 | 2 (vv. 14–15) | **achado** (relev. 2): «logo, todos morreram» = mortos nos pecados; um só vivo morreu por todos os mortos |
| Agostinho | *Confissões* X, 43, 70 | PL 32, 808–809 | 2 (v. 15) | **achado**: queria fugir para a solidão; Deus o deteve com 5,15 |
| Bernardo | *Cântico* 20, 6–7 | PL 183, 870A–871A | 2 (v. 16) | **achado**: o amor «carnal» à humanidade de Cristo (o Menino, o Mestre, o Crucificado) é bom e leva ao espiritual; Paulo já tinha subido |
| Leão | Sermão 71 (Ressurreição 1), 3–4 | PL 54, 388A–C | 2 (v. 16) | **achado**: «a ressurreição não foi o fim da carne, mas a sua transformação»; a mesma pela essência, não a mesma pela glória |
| Gregório | *Homilias sobre Ezequiel* I, 10, 8–10 | PL 76, 889B–890A | 2 (v. 17) | **achado**: a nova criatura não está no hábito, mas na mente: amar o inimigo, não exultar com a morte dele |
| Bernardo | *Cântico* 61, 3–4 | PL 183, 1072B–D | 3 (v. 19) | **achado**: «clama o cravo, clama a chaga» que Deus estava em Cristo reconciliando o mundo; a chave e o cravo |
| Tomás | *Super II Cor.*, c. 5, l. 5 | [87713] | 3 (vv. 18, 20) | **achado**: Deus fez a sua parte; a nossa se dá no Batismo e na penitência; Paulo suplica quando poderia mandar |
| Gregório | *Homilias sobre os Evangelhos* 32, 5 | PL 76, 1236B–C | 3 (v. 20) | **achado**: nós fizemos a discórdia e Deus, o ofendido, mandou primeiro os embaixadores: envergonhe-se quem não procura primeiro o irmão |
| Agostinho | *Tratados sobre João* 41, 5 | PL 35, 1695 | 3 (vv. 20–21) | **achado**: «o meio que separa é o pecado; o Mediador que reconcilia é Cristo»; «Deus não tem inimigos livres» |
| Agostinho | *Enchiridion* 41 | PL 40, 252–253 | 3 (v. 21) | **achado**: «pecado» = sacrifício pelo pecado da antiga Lei; a troca: «ele pecado, não seu, mas nosso; nós justiça, não nossa, mas de Deus» |
| Agostinho | Sermão 351, 7 | PL 39, 1542–1543 | 1 (v. 10) | reserva boa: «suba o homem ao tribunal da sua mente», com a consciência por testemunha, antes do tribunal de Cristo |
| Agostinho | *Sobre o Sl 38*, 21 | PL 36, 429–430 | 1 (v. 1) | reserva boa: somos inquilinos sem contrato; quando o Dono disser «Muda-te», é preciso ir: «moras de graça» |
| Agostinho | Carta 217, 16 (7º ponto) | PL 33, 984 | 1 (v. 10) | reserva: julgados pelo que fizemos no corpo, «não pelo que faríamos, se vivêssemos mais» (contra os semipelagianos) |
| Gregório | *Morais* XXXI, 69–70 | PL 76, 611C–612A | 1 (v. 4) | reserva: «Paulo ama o que evita»; o soldado que, à beira da batalha, «treme e se enfurece». Diz o mesmo que o Sermão 299, menos colado ao texto |
| Tomás | *Super II Cor.*, c. 5, l. 1 | [87709] | 1 (v. 1) | no texto (base): rejeita a Glosa (a casa = corpo glorioso) e lê a casa como a glória celeste recebida logo depois da morte; l. 2 diz que os santos veem Deus logo depois da morte. Ficou o Gregório dos *Diálogos*, mais claro |
| Tomás | id., l. 2 (penhor) | [87710] | 1 (v. 5) | **já usado** no cap. 1 (o penhor vale tanto quanto a coisa); por isso, para 5,5, o Sermão 170 |
| Tomás | id., l. 3–4 | [87711]–[87712] | 2 (vv. 13–17) | no texto (base): «sobriedade» = medida, contra a «embriaguez do Espírito»; «urget» = esporear; a nova criação é do nada, «porque quem não tem a graça é nada». Reservas |
| Ambrosiaster | *In II Cor.* 5,21 | PL 17, 298B–C | 3 (v. 21) | no texto (base), reserva: o Filho «feito pecado» sem deixar de ser o que era, «como quem é feito prefeito não perde o que era»; a vítima pelo pecado chamada «pecado». Diz o mesmo que o *Enchiridion* 41 |
| Ambrósio | *Sobre o Sl 118*, 18 (Sade), 42 | PL 15, 1467B | 3 (v. 21) | reserva: «Pecado és tu, ó homem; por isso o Pai fez Cristo pecado»; batizado, não morras de novo |
| Ambrósio | *Os sacramentos* IV, 4, 16 | PL 16, 441A | 2 (v. 17) | reserva: «eras criatura velha; depois de consagrado, começaste a ser nova criatura», dentro do argumento eucarístico (confuso fora da obra) |
| Leão | Sermão 59 (Paixão 8), 7 | PL 54, 342A–B | 2 (vv. 15, 17) | reserva: «ninguém fique na velhice da vida carnal… quem não progride regride»; perto da renovação diária de 4,16, já tratada |
| Bernardo | *Cântico* 85, 13–14 | PL 183, 1194C–D | 2 (v. 13) | reserva boa: «uma coisa é minha com Deus, só Deus por testemunha; outra é minha convosco» (o 85, 10–11 já foi usado no cap. 1) |
| Bernardo | Carta 107, 8 | PL 182, 246D | 1 (v. 5) | reserva: «tens o penhor do amor, o Espírito, e a testemunha fiel, Jesus crucificado: Cristo faz por que seja amado, o Espírito faz que seja amado» |
| Ricardo de São Vítor | *Os quatro graus da caridade violenta* | PL 196, 1222D–1223A | 2 (vv. 14, 17) | reserva: no 4º grau a alma, já unida a Deus, volta ao próximo («a caridade de Cristo o constrange; seja nova criatura») — místico demais para o leitor comum |
| Agostinho | Sermões 134, 4–5 e 152, 10–11 | PL 38, 745 e 824 | 3 (vv. 20–21) | reserva: «pecado» = sacrifício, com o rito da imposição das mãos sobre «o pecado» (Lv 4); o mesmo do *Enchiridion*, em sermão |
| Agostinho | Sermão 169, 1 | PL 38, 916 | 3 (v. 21) | pista: «se ele evitasse a pobreza, nós não deixaríamos de ser pobres» (5,21 com Fl 2,6-7; a «troca»), não lido por inteiro |
| Agostinho | *Tratados sobre João* 7, 23; *Sobre o Sl 119* (Lombardo) | PL 35, 1449 | 2 (v. 13) | reserva: Paulo «subindo e descendo» como os anjos de Jacó; ficou a *Regra pastoral*, mais completa |

Destaques, por ordem: Agostinho, *Confissões* X, 43; Bernardo, *Cântico* 61, 4 (o cravo que clama); Gregório, Hom. 32
(Deus manda os embaixadores primeiro); Agostinho, *Enchiridion* 41; Bernardo, *Cântico* 20 (a humanidade de Cristo na
oração); Agostinho, Sermão 299 (a túnica terrena e a celeste).

## O que não existe ou não rendeu (não procurar de novo)

- **Cipriano**: nada sobre 2Cor 5 nos tratados; o *De mortalitate* não cita o capítulo (fala do desejo da morte com Fl 1,21-23).
  Só os *Testemunhos* (PL 4, 5,10 duas vezes, sem comentário), o *De lapsis* 17 (o tribunal, de passagem) e a carta 66 (69 na PL)
  («no dia do juízo, diante do tribunal de Cristo, as duas cartas serão lidas»). A carta de consolo que cita 5,1 e 5,6 no
  volume das cartas (PL 3, 435C–438C) traz o cabeçalho «Carta do papa Cornélio a Cipriano» no Corpus: não é de Cipriano;
  não seguida.
- **Hilário**: só citações de 5,19 como prova da divindade do Filho (*A Trindade* VII; *Sobre Mateus*) e de 5,21 em *A
  Trindade* X (Cristo «feito pecado» para condenar o pecado na carne): nada que ilumine o leitor comum.
- **Jerônimo**: o comentário de PL 30 é de Pelágio; nas cartas, 5,6 e 5,8 só de passagem (Carta 22 e outras). Nada próprio.
- **Ambrósio**: *O bem da morte* 3, 9 cita 5,1, mas o trecho já foi usado no cap. 4; *A morte do irmão Sátiro* II (PL 16,
  1347) cita 5,16 só como ponte; *Sobre a morte de Teodósio* 31 (5,8-9, o imperador que «agora goza»): elogio fúnebre, fraco
  fora da obra.
- **Leão**: além dos Sermões 71 e 59, 5,19 citado nas Cartas 124 e 165 (cristologia) e nos sermões da Paixão: repetem o
  Tomo. **Cassiano**: só citações (*Conferências*: 5,1, 5,6-8 e 5,16; *A encarnação de Cristo*: 5,10 e 5,16 contra
  Nestório). **Fulgêncio**: o «fragmento 28» do *Contra Fabiano* (PL 65, 786A–B) argumenta com Ef 1,14
  («penhor da herança», e a herança é o Senhor), não com 5,5, que só aparece numa lista: não serve para 5,5.
- **Anselmo**: só o *Cur Deus homo* está no cache, e não cita 2Cor 5,21 (fala de reconciliação em geral). **Guilherme de São
  Teodorico** e **Boaventura**: não estão no subconjunto PL do Corpus Corporum (Guilherme, só o «Liber I»); não procurados fora.
- **Máximo de Turim**, Hom. 114 (o «donativo» do soldado, 5,5): autenticidade discutida; não usada. **Pedro Crisólogo**,
  Sermão 5 (o anel do filho pródigo, «penhor do Espírito, arra das núpcias celestes»): é sobre Lc 15; pista.
- **Agostinho, Sermões 23 e 156** (o penhor e a arra): não abertos; o Sermão 378, que diz o mesmo (arra × penhor), já foi
  usado no cap. 1. Por isso o Sermão 170.
- Excluídos por autoria ou regra: o *Breviarium* e as cartas espúrias sob o nome de Jerônimo; os *Sermones dubii* de
  Agostinho (PL 39: «reconciliamini Deo» aos penitentes); Pedro Lombardo e Hervé (compiladores, não santos).

## Dúvidas

- **Sermão Denis 10** (PL 46, 845): é o 10º dos sermões publicados por M. Denis (1792), que a PL 46 traz como *Sermones
  inediti*; a numeração bate com a do Sermão 305/A (= Denis 13), já usado no cap. 1. A autenticidade de cada sermão de Denis
  não foi conferida (o Denis 1, do círio pascal, é tido por espúrio): conferir na lista de Verbraken antes de publicar.
  Por isso relevância 2.
- **Gregório, *Diálogos***: a PL numera o capítulo como IV, 25; as edições modernas, IV, 26. O trecho começa por «há almas
  de alguns justos que ainda ficam retidas fora do Reino» (o purgatório, sem o nome); o diálogo entre Pedro e Gregório foi
  cortado em três partes por « […] », sem os rótulos.
- **Tertuliano** escreveu *A ressurreição da carne* já montanista. O excerto corta de propósito a frase anterior, em que diz
  que só os mártires vão logo para junto do Senhor (erro dele; o *Diálogo* de Gregório diz o contrário). Relevância 2.
- **Bernardo, *Cântico* 20**: «amor carnal» é o termo dele para o amor à humanidade de Cristo, e não tem sentido pejorativo
  («salutar»); se o Gere achar que a palavra assusta, a tradução pode dizer «amor sensível» (mantive «carnal», fiel).
- **Bernardo, *Cântico* 61**: o trecho é do Ofício das Leituras? (lembro-me de uma leitura com as «fendas da rocha»);
  conferir com o grupo «modernos» (liturgia) para não repetir.
- **Gregório, *Regra pastoral* II, 5**: o trecho fala de Paulo que, depois do terceiro céu, regula a vida íntima dos casados
  (1Cor 7,2-5): a tradução diz «o leito dos casados» e «como devem viver na sua intimidade». O II, 6 já foi usado no cap. 1.
- Agostinho ficou com 8 dos 20. Se for preciso cortar, os primeiros a sair são *A Cidade de Deus* XX, 6 (v. 14) e o Sermão
  Denis 10 (v. 6, há o Ambrosiaster); a melhor reserva para entrar é o Sermão 351, 7 (o tribunal da mente, v. 10).
- Colunas da PL: as do Corpus Corporum; nas obras de Agostinho o Corpus marca só o número da coluna, sem letra.

## Pistas não seguidas

- Agostinho, Sermão 169, 1 (PL 38, 916): 5,21 e a pobreza de Cristo (a «troca»); Sermões 23 e 156 (o penhor).
- Gregório, *Morais* XVI, 69 (PL 75, 1162B; na edição antiga XVI, 5, 6): o penhor «para termos certeza da promessa».
- Bernardo, *Sermões diversos* (PL 183, 727D): «nós também amamos carnalmente a nossa carne» com 5,16; *Na Ascensão* 3
  (o afeto carnal dos apóstolos, 5,16); *Dedicação* 2 (5,1); *Morte de São Malaquias* 2 (5,6: luto e alegria).
- Hugo de São Vítor, *Questões sobre as cartas de Paulo* (II Cor., q. 13–14: por que o Espírito é «penhor»; os dois
  «excessos» da mente, o pavor e a atenção ao alto): não é santo, mas é claro; só como pista.
- Os sermões de Agostinho fora dos Maurinos e dos de Denis (Dolbeau, Mainz) e o Biblindex: não varridos.

## Para outros capítulos

- **2Cor 6,2** («eis agora o dia da salvação»): Bernardo, *Sermões diversos*, junto com 5,10 (no cache, `cc_11257`);
  não lido.
- **2Cor 1,22 / 5,5** (o penhor): Bernardo, Carta 107, 8 (PL 182, 246D), «o penhor do amor», reserva aqui.
- Os caches do Corpus Corporum somam 813 textos da PL (índice em `~/.cache/taioe-2cor-comum/latinos5/idx.txt`); a mesma
  busca serve aos capítulos 6–13: basta trocar `pats.json`.
