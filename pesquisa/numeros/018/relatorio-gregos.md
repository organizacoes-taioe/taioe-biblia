# Números 18: relatório da pesquisa nos Padres gregos e bizantinos

Pesquisa de 2026-10-24 (interrompida por uma queda de rede e retomada no mesmo dia). Resultado: **17 achados** em
`achados-gregos.json` (6 com relevância 3, 11 com 2; trecho 1: 4, trecho 2: 5, trecho 3: 5, trecho 4: 3). Todos «domínio
público»; um é só latim (Procópio, v. 7, sem grego impresso na PG). Textos em `textos/`: `clemente-romano-1cor-18.md`,
`constituicoes-apostolicas-2-18.md`, `crisostomo-varios-18.md`, `nissa-varios-18.md`, `nazianzeno-carmina-18.md`,
`clemente-alexandria-stromata-18.md`, `procopio-commentarii-in-numeros-18.md` (grego e latim conferidos na imagem) e
`gregos-outros-18.md` (reservas). Cirilo (*De adoratione*) e Teodoreto (*Quaest.* 34) saíram de `base/`, conferidos.

## Onde se procurou

- **Corpus grego já convertido** de uma sessão anterior neste PC (a de Nm 17), só lido, sem baixar de novo: 710 textos do
  khazarzar (Basílio, Nazianzeno, Nissa, Atanásio, Cirilo de Alexandria e de Jerusalém, Teodoreto, Epifânio, Dídimo, Eusébio,
  Clemente Romano e de Alexandria, Ireneu, Constituições Apostólicas, Damasceno, Macário, Máximo, Hesíquio, Severiano,
  Anfilóquio, Olimpiodoro, Paládio, Proclo, Fócio, Teodoro Estudita) e os 398 de Crisóstomo; mais a base AGES da hinografia
  bizantina (2 369 arquivos). Cache em `…/4b54597f-…/scratchpad/p-gregos/` (`txt/`, `b2/txt/`, `ages/`, `ia/`), fora do git e
  temporário. Os scripts desta pesquisa estão em `scratchpad/p-gregos/scripts/` (`busca.py`, busca sem acentos com a tabela
  `translate`; `seg.py`/`segs.py`, que tiram do texto convertido o trecho exato entre duas âncoras; `montar.py` e `textos.py`,
  que geram o JSON e os arquivos de `textos/`).
- **Padrões** (sem acentos): todas as frases da LXX de Nm 18 que um Padre citaria: «λήψεσθε τὰς ἁμαρτίας» (das coisas santas,
  do sacerdócio), «προσκείσθωσαν», «δόμα δεδομένον», «ὁ ἀλλογενὴς … ἀποθανεῖται», «διατήρησιν τῶν ἀπαρχῶν», «εἰς γέρας»,
  «πᾶν ἀνατεθεματισμένον», «λύτρωσις … ἀπὸ μηνιαίου», «πέντε σίκλων», «διαθήκη ἁλὸς», «ἅλας διαθήκης», «ἐγὼ μερίς σου (καὶ ἡ)
  κληρονομία σου», «ἐγὼ κλῆρος», «ἐν τῇ γῇ αὐτῶν οὐ κληρονομήσεις», «ἐπιδέκατον ἀπὸ τοῦ ἐπιδεκάτου», «δεκάτας τῶν δεκατῶν»,
  «ὡς σῖτος ἀπὸ ἅλω», «μισθὸς οὗτος»; e combinações: Λευΐτ- perto de μερίς/κλῆρος/κληρονομία; δεκάτ- perto de Λευΐτ-;
  ἀπαρχ- perto de ἱερεῦσι; «τῷ θυσιαστηρίῳ συμμερίζονται» (1Cor 9,13); κληρικ- perto de «κλῆρος Θεοῦ/Κυρίου» (a
  etimologia de «clérigo»). Em Crisóstomo, todas as 275 ocorrências de δεκατ-, filtradas por levitas, primícias, esmola e
  judeus.
- **Colunas e conferências**: imagens da PG 87/1 (`patrologiae_cursus_completus_gr_vol_087_1`, páginas n442 e n443) para
  Procópio; OCR de Funk 1905 (`didascaliaetcons00funk`) para a numeração das Constituições; OCR latino da PG 46
  (`patrologiaecursu46mignuoft`) para as colunas de Nissa; OCR da PG 78 (Isidoro de Pelúsio, só o latim).

## O que entrou (uma linha cada)

- **Trecho 1 (vv. 1–7)**: Clemente Romano 40–41 (cada um no seu posto; quem passa da medida tem a morte por pena; mais
  conhecimento, mais perigo); *Const. Ap.* II, 25, 9.12–15 (os bispos, imitadores de Cristo, tomam como seus os pecados do povo
  e por isso vivem da Igreja; cita Nm 18,1); Procópio, Nm 18,7, só latim (o ministério é o dom que o sacerdote devolve a Deus;
  fugir dele por precaução é ingratidão); Cirilo, *De ador.* XII (os «pecados» que os sacerdotes levam são as vítimas pelo
  pecado; Cristo feito «pecado» por nós, 2Cor 5,21).
- **Trecho 2 (vv. 8–19)**: Cirilo, *De ador.* XII (aliança de sal: consagrar-se a Deus com sensatez; «vós sois o sal da terra»);
  Teodoreto, *Quaest.* 34 (aliança de sal = a participação no altar, 1Cor 9,13); Procópio, Nm 18,15–16 (o primogênito do homem
  se resgata por honra; Cristo, resgate pela vida do mundo); Clemente de Alexandria, *Strom.* II, 18, 86 (dízimos e primícias,
  escola de piedade e de partilha); Nissa, *Vida de Macrina* 13 (Emélia oferece a primogênita como primícias e o décimo filho
  como dízimo).
- **Trecho 3 (vv. 20–24)**: Cirilo, *De ador.* XIII («eu sou a tua parte»: a diferença da esperança; quem serve a Deus sem
  distração o tem por única herança; o trabalho dos santos não fica sem salário); Nissa, *Ep.* 17 (o bispo que olha só para as
  coisas de Deus: por isso o levita não tem herança na terra); Nazianzeno, *Carm.* I, 2, 10 (na partilha, a parte de Levi era a
  melhor: Deus; em versos); Crisóstomo, *Hom. 64 sobre Mateus*, 4 (os judeus davam três dízimos, primícias e primogênitos; e tu,
  nem a décima parte?); *Const. Ap.* II, 26, 1–3 (as ofertas de então são as de agora; os levitas são hoje os diáconos).
- **Trecho 4 (vv. 25–32)**: Cirilo, *De ador.* XIII (o dízimo do dízimo a Aarão, figura de Cristo, a quem se deve todo fruto;
  hoje, frutos espirituais); Teodoreto, *Quaest.* 34 (o dízimo é salário em proveito do povo: os levitas servem em lugar de
  todos); Crisóstomo, *Hom. 9 sobre Filipenses*, 4 (ninguém dizia que os levitas comiam demais; hoje chamam de riqueza a roupa
  do sacerdote).

## Atenção na seleção (sobreposições)

- **Didascália (grupo dos orientais)**: as *Constituições Apostólicas* II, 25–26 ampliam o texto da Didascália, caps. 8–9.
  `constituicoes-apostolicas-2-25-imitadores-de-cristo-levam-os-pecados` repete o pensamento de
  `didascalia-8-o-bispo-leva-os-pecados-do-povo` (orientais): **escolher um dos dois** (o grego acrescenta «o sem mancha,
  crucificado pelos que mereciam o castigo» e a cadeia «vigias / modelo»). `constituicoes-apostolicas-2-26-os-levitas-sao-hoje-
  os-diaconos` corresponde ao começo do cap. 9 da Didascália (se os orientais o tiverem, ficar com um só).
- **Agostinho, *Quaest.* IV, 31 (latinos)** diz, como Cirilo, que os «pecados» de Nm 18,1 são as vítimas pelo pecado; Cirilo
  acrescenta 2Cor 5,21 (Cristo feito «pecado») e Os 4,8. Se os latinos usarem Agostinho, Cirilo pode ficar só se o tema
  pedir a leitura cristológica.
- **Procópio** copia Cirilo (*De ador.* XII–XIII) em quase todo o capítulo; só os dois escólios usados (v. 7, latim; vv. 15–16,
  grego) são dele. **Teodoreto** e **Cirilo** dão duas leituras diferentes da «aliança de sal» (comunhão no altar × sensatez,
  sal da terra): as duas cabem.
- **Crisóstomo** não cita as palavras de Nm 18: comenta a lei dos dízimos, primícias e primogênitos que sustentava os levitas
  (o PEDIDO o lembrava). **Nissa, *Vida de Macrina*** é aplicação, não comentário: usa o vocabulário de Nm 18 (ἀπαρχή,
  πρωτότοκος, ἐπιδέκατον, ἀνάθημα) e diz «a Lei consagra os dois a ti». **Clemente Romano** resume a ordem de Nm 18,1–7 sem
  citar o capítulo. Os três estão marcados com relevância 2 ou como estão; se o Gere quiser só citações explícitas, saem.

## Reservas (texto em `textos/`)

- *Const. Ap.* II, 18, 6–7 (Funk I, 67–69): «o leigo cuida só de si; tu, de todos», com Nm 18,1 («tu e Aarão levareis os
  pecados do sacerdócio»). Mesmo pensamento de II, 25.
- *Const. Ap.* II, 25, 4–6 (Funk I, 93–95): o bispo come da Igreja como o boi que debulha na eira, «come, mas não devora tudo»,
  como os levitas que serviam na tenda e por isso não tiveram terra. Bom para os vv. 30–31; deixado de lado para não haver três
  das *Constituições*.
- Crisóstomo, *Hom. 15 sobre 1 Timóteo*, 2 (PG 62, 581): os levitas não cuidavam de nada da vida, porque a lei lhes dava
  dízimos e primícias; «eu não peço mais que alimento e roupa para os que presidem». *Hom. 22 sobre 1 Coríntios*, 1 (PG 61,
  181–182): Paulo não diz «recebem dos que oferecem», mas «comem do templo», para que nem quem recebe seja humilhado nem quem
  dá se envaideça; o que se ofereceu já não é de quem ofereceu. *Hom. 4 sobre Efésios*, 4 (PG 62, 36; repetida nas *Eclogae*):
  «Fulano dá o dízimo!», e isso, que entre os judeus não admirava ninguém, entre cristãos virou admiração. *Adv. Iud.* VII
  (PG 48, 922): os levitas viviam dos dízimos.
- Cirilo, *Fragmenta duo in Numeros* (já em `base/`): sobre Nm 18,26, o mesmo que *De ador.* XIII (Aarão, figura de Cristo,
  que ministra na tenda interior); *Glaphyra in Gen.* (PG 69, 88–89): de novo o dízimo do dízimo e Hb 7,9.
- Teodoreto, *In Ps.* 118,57 (PG 80, coluna a conferir): «Deus não é a parte de todos, mas dos que abraçam a perfeição; assim
  foi a parte e a herança dos sacerdotes e levitas», citando Nm 18,20 misturado com Dt 18,2 (a mesma glosa aparece num *In Ps.
  118* atribuído a Crisóstomo, que é compilação). *In Mal.* 3,8–10 (PG 81, 1980–1981): «por isso não dei terra aos sacerdotes,
  para que vivam das primícias e dos dízimos e socorram os pobres que servem no templo»: privar o templo das primícias é roubar
  os pobres. Comentam outro texto: pistas.
- Orígenes (cadeia), *Selecta* (já em `base/`): «o lote de ter parte no altar é o que traz aos sacerdotes a pobreza»;
  atribuição incerta, curto.
- Procópio, latim: «Quemadmodum vero ipsi primitiae sunt populi, sic ex primitiis sustentantur» (como eles são as primícias
  do povo, assim vivem de primícias); e, sobre o v. 4, Ozias, ferido de lepra por querer a oferta suprema.

## O que não existe ou não se achou

- **«Ἐγὼ μερίς σου καὶ κληρονομία σου» citado por extenso** nos gregos: só Cirilo (*De ador.* XIII, duas vezes). Nazianzeno e
  Nissa aludem ao versículo; Eusébio (*In Ps.* 72 e 118) e Dídimo (*In Ps.* 15; *De Trin.*) partem do Salmo ou de Dt 18,2.
  **A etimologia de «clérigo»** (κλῆρος = parte do Senhor) não aparece em nenhum grego do corpus: é de Jerônimo (latinos).
- **Nm 18,2–7** (os levitas «juntos» a Aarão, *yillawu*, o «estranho» que morre, o sacerdócio como «dom»): nenhum grego cita
  além de Cirilo (que cita o paralelo de Nm 3,6–10 em *De ador.* XIII e lê bispos e presbíteros no altar, diáconos como
  levitas: ver reservas), Procópio e Teodoreto. O jogo Levi/«unido» não aparece nos gregos.
- **«Aliança de sal»**: só Cirilo, Procópio (que o copia) e Teodoreto. **O primogênito resgatado e a Apresentação de Jesus**: a
  homilia *In occursum Domini* atribuída a Nissa (PG 46, 1152–1181, autenticidade discutida) cita Nm 18,15–17 e Nm 3,12–13.40–51,
  mas o raciocínio é confuso e polêmico contra os judeus: não usada.
- **Hinografia bizantina (AGES)**: nada sobre Nm 18. «Μερίς μου εἶ ὁ Κύριος, καὶ κλῆρος ἐπιπόθητος» (Octoeco) vem do Sl
  118,57; os «levitas» dos hinos são diáconos mártires (Euplo, Cirilo, Irineu) ou São Nicolau ou o levita da parábola do bom samaritano.
- **Basílio, Atanásio, Epifânio, Damasceno, Máximo, Teodoro Estudita, Fócio, Ireneu (grego)**: nada sobre Nm 18 no corpus.
  **Isidoro de Pelúsio** (PG 78, só o latim): a carta I, 317 elogia quem paga primícias e dízimos, sem Nm 18 e banal.
  **Nilo** e **Isidoro** não estão no khazarzar.

## Cuidados

- **Cirilo** lê em Nm 18,1a «λήψεσθε τὰς ἀπαρχὰς τῶν ἁγίων» (recebereis as primícias das coisas santas), variante da LXX; a
  tradução do achado segue o texto dele. **Teodoreto** (PDF do khazarzar) segue a edição Fernández Marcos–Sáenz-Badillos (1979);
  colunas da PG 80 não conferidas (384–385, como em Nm 17).
- **Procópio, vv. 15–16**: a PG imprime «Τὸ δὲ λύτρον (60) μὴ ἐπὶ φθορᾷ παθῶν»; a nota 60 dá a variante «Χριστὸς δὲ τὸ λύτρον»
  e o latim de Clauser lê παθών («Christus … pro vita mundi passus est»). A tradução segue esse sentido («o Resgate, que é
  Cristo, sofreu…»). Procópio, v. 7: só existe o latim de Clauser na PG; se o Gere exigir grego, sai.
- **Colunas a conferir**: 1 Clem 40–41 (PG 1, 288–292, pelo hábito; o OCR da PG 1 é ilegível); Nissa, *Ep.* 17 (PG 46,
  1059–1062: o latim está logo depois do marcador 1060 no OCR); Clemente de Alexandria (PG 8, não conferida; citado por
  Stählin). Conferidas: Crisóstomo (marcadores do PDF), Nazianzeno (PG 37, 716), Cirilo (PG 68), Macrina (PG 46, 973–974),
  *Const. Ap.* (Funk, páginas e parágrafos no OCR de Funk).
- **Nazianzeno**: o poema atribui a Moisés a partilha da terra (foi Josué, a mando de Moisés); a tradução deixa como está.
- Crisóstomo, *Fl* 9, 4: «καὶ πάλιν ἑτέρας τρισκαιδεκάτας» (outras «décimas terceiras»?) parece erro do texto: ficou fora,
  com […].

## Para outros capítulos

- **Nm 19** (a novilha vermelha, a água da aspersão): Cirilo, *Glaphyra* (PG 69, 625–636, já em `base/`); Teodoreto,
  *Quaest.* (Nm 19, já em `base/`); **Epifânio, *Panarion* 30 (Holl I, 373–374)**: a novilha é a Virgem Maria («λάβε σοι
  δάμαλιν πυρράν», para mostrar o vaso escolhido de Maria; o vermelho, o fogo da divindade do Salvador contido nela; «sobre a
  qual não veio jugo»): leitura mariana rara, conferir; **Eusébio, *Dem. ev.* I, 3, 10–11**: a água da aspersão e a novilha como
  exemplo de lei que só valia para um povo e um lugar; Cirilo, *In xii proph.* (Os 4,16; Pusey I, 103) cita Nm 19,2.
- **Nm 20** (Meribá, a morte de Aarão no monte Hor): Cirilo, *Fragmenta duo* (Nm 20,8, já em `base/`); Orígenes (cadeia),
  *Selecta* (Nm 20,10–12: Moisés não glorificou a Deus; o túmulo escondido para que não o venerassem; em `base/` deste
  capítulo, por erro do corte automático); **Basílio, *Hom. in Ps.* 48** (PG 29, 437–440): a «voz de dúvida» de Moisés
  («Ouvi, rebeldes: tiraremos água desta rocha?») depois de tantos prodígios; **Cirilo, *Com. a João*** (Pusey I, 411–413):
  Moisés «desanimado pelo humano» na rocha; Nissa, *Contra Eunômio* II, 288 (o nome «água da contradição», de passagem);
  Cirilo, *De ador.* (duas menções do monte Hor).
- **Nm 3** (os levitas no lugar dos primogênitos): Cirilo, *De ador.* XIII (PG 68, 845–848: bispos e presbíteros no altar,
  diáconos como levitas, que anunciam os hinos e as orações e trazem os vasos sagrados na liturgia), em `textos/gregos-outros-18.md`;
  *In occursum Domini* (pseudo-Nissa), com o resgate dos primogênitos que passavam do número dos levitas (Nm 3,46–51).
