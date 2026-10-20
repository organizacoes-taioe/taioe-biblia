# Salmo 36 (35): relatório da pesquisa nos Padres latinos e nos autores medievais

Pesquisa de 2026-10-19/20. Grupo: Padres latinos (menos Santo Agostinho, coberto à parte), autores
medievais e São Roberto Belarmino. Nos autores é o «Psalmus XXXV» («Dixit injustus ut delinquat in
semetipso»). Resultado: **51 excertos** em `achados-latinos.json` (23 de relevância 3, 28 de
relevância 2), de 17 autores, cobrindo os vv. 1–3, 5–10, 12–13, e os textos em `textos/`. Onde achar
cada obra: `../../fontes/latinos.md`.

Numeração dos `versiculos`: a hebraica, que neste salmo coincide com a da Vulgata Clementina (o
título «In finem, servo Domini ipsi David» é o v. 1; 13 versículos; conferido com
`ferramentas/hebraico.py`). **Cassiodoro e Belarmino não numeram o título**: o «Vers. N» deles é o
nosso v. N+1 (aqui, ao contrário do Sl 35 (34), não dividem os versículos de outro modo). A
`passagem` dá a numeração deles; os `versiculos`, a nossa. Ambrósio e Gerhoh numeram como a
Clementina. Tomás não numera (n. 1 = vv. 2–5; n. 2 = vv. 6–7a; n. 3 = 7b–8a; n. 4 = 8b–10a; n. 5 =
10b; n. 6 = 11–12; n. 7 = 13).

Todo `original` tirado da PL ou do Corpus Thomisticum foi conferido por script com o texto baixado
(cada trecho entre «(...)» é substring exata, sem as notas de Migne, as marcas de coluna e os números
de página da edição anterior que Migne deixa no meio do texto). Os da edição Morin (Jerônimo) foram
conferidos contra o arquivo `textos/jeronimo-commentarioli-e-tractatus.md`, que é transcrição do OCR
corrigida à mão. Os de Belarmino vêm de OCR e foram limpos à mão.

## O que se achou

| autor | obra | onde | texto guardado | excertos |
|---|---|---|---|---|
| Santo Ambrósio | *Explanatio in Ps. 35* (das *Enarrationes in XII Psalmos*), §§ 1–29 | PL 14, 952D–966C | `ambrosio-enarratio-in-psalmum-35.md` (inteiro) | 11 |
| Santo Ambrósio | *De fuga saeculi* 9, 52; *Exhortatio virginitatis* 9, 57–58 (e mais 9 citações só no arquivo) | PL 14, 593C; PL 16, 353B | `ambrosio-citacoes.md` | 2 |
| Cassiodoro | *Expositio Psalmorum*, Ps. XXXV | PL 70, 251B–256C | `cassiodoro-expositio-psalmorum.md` (inteiro) | 6 |
| São Bernardo | *De diligendo Deo* 11, 33; *Cântico* 18, 4 e 85, 6; Carta 393, 3; Semana Santa, 9; Natal 1, 2 (e mais 10 só no arquivo) | PL 182–183 | `bernardo-citacoes.md` | 6 |
| São Tomás de Aquino | *Postilla super Psalmos*, Sl 35, n. 1–7 (cobre o salmo inteiro); *Suma* I, q. 12, a. 2 | Corpus Thomisticum [87144]–[87150] | `tomas-postilla-super-psalmos.md` (inteiro, com as outras obras) | 5 |
| São Roberto Belarmino | *Explanatio in Psalmos*, Sl 35 | Vivès, t. X (1874), pp. 221–224 | `belarmino-explanatio-in-psalmos.md` (inteiro, OCR bruto) | 4 |
| São Jerônimo | *Commentarioli*; Homilia de Natal; *Tract. de Ps. 146*; *In Isaiam* XVI | Morin, *An. Mar.* III/1, pp. 42–43; III/2, pp. 297, 392–393; PL 24, 571C | `jeronimo-commentarioli-e-tractatus.md`, `jeronimo-cartas-e-comentarios.md` | 4 |
| São Gregório Magno | *Hom. in Ez.* I, 10, 7; *Moralia* XXIX, 57 | PL 76 | `gregorio-magno-citacoes.md` | 2 |
| São Bruno de Segni | *Expositio in Psalmos*, Ps. XXXV | PL 164, 817A–820A | `bruno-segni-expositio-in-psalmos.md` (inteiro) | 2 |
| São Pedro Crisólogo | Sermão 8 | PL 52, 210C–211A | `outros-citacoes.md` | 1 |
| São Máximo de Turim | Homilia 97 | PL 57, 478C–479A | `outros-citacoes.md` | 1 |
| João Cassiano | *De institutis* XII, 6 | PL 49, 433A–434A | `outros-citacoes.md` | 1 |
| Arnóbio, o Jovem | *Commentarii in Psalmos*, Ps. XXXV | PL 53, 372C–373D | `arnobio-commentarii-in-psalmos.md` (inteiro) | 1 |
| Gerhoh de Reichersberg | *Commentarius aureus*, Ps. XXXV | PL 193, 1347D–1356B | `gerhoh-commentarius-in-psalmos.md` (inteiro) | 1 |
| Santo Anselmo | *Proslogion* 25 | PL 158, 240A–C | `outros-citacoes.md` | 1 |
| Ricardo de São Vítor | *Adnotationes mysticae in Psalmos*, Sl 121 | PL 196, 366B–C | `outros-citacoes.md` | 1 |
| Bem-av. Isaac de Stella | Sermão 26 | PL 194, 1775C–D | `outros-citacoes.md` | 1 |
| Bem-av. Guerrico de Igny | Sermão 4 no Natal, 2 | PL 185, 39C–D | `outros-citacoes.md` | 1 |
| pseudo-Jerônimo, *Breviarium*; «Haimo»; pseudo-Beda; São Bruno Cartuxo; Pedro Lombardo | comentários salmo a salmo | PL 26, 116, 93, 152, 191 | um arquivo inteiro de cada | 0 |

Temas e versículos:
- **O título, «o servo do Senhor»** (v. 1): Ambrósio (o único salmo com esse título; é Cristo, que
  tomou a forma de servo: «Bona servitus, quae omnes liberos fecit»); Cassiodoro, Bruno de Segni
  («puero Domini», o menino de Is 9,6).
- **O ímpio que peca «contra si mesmo»** (vv. 2–5): Ambrósio (a serpente envenena os outros, o
  injusto a si mesmo; a justiça é ouro, a iniquidade lama; Deus vê como o sol que entra nos quartos
  fechados; o leito é para chorar os pecados); Tomás (o exame de consciência fraudulento, que alivia o
  grave e agrava o leve).
- **A misericórdia no céu** (v. 6): Bruno de Segni («Misericordia me adduxit», a resposta de cada
  santo no céu); Crisólogo (a misericórdia do céu se alcança pelas da terra); Bernardo, Natal 1, 2 (a
  misericórdia presa no céu que «solta o cinto» e desce); Tomás (justiça = montes, verdade = nuvens,
  misericórdia = céus, a mais alta).
- **Os montes e o abismo** (v. 7a): Cassiodoro (os apóstolos, que recebem primeiro a luz e a passam
  aos vales; o mar sem fundo dos juízos); Gregório, *Moralia* XXIX, 57 (não perscrutar por que um é
  escolhido e outro não).
- **«Homens e animais salvarás»** (v. 7b): Jerônimo, Homilia de Natal («Si homo es, panem comede: si
  animal es, ad praesepe accede») e *Tract. de Ps. 146* (trigo e feno da Escritura); Guerrico, Natal
  (o pão dos anjos feito feno na manjedoura); Bruno de Segni (os monges que antes eram «como o cavalo
  e o mulo»); Belarmino (Deus sustenta com as próprias mãos os que o blasfemam); Ambrósio (uns no
  pasto, outros no banquete).
- **As asas** (v. 8): Cassiodoro, Tomás e Belarmino (a galinha e os pintinhos); Arnóbio (os braços
  abertos na cruz).
- **A embriaguez e a torrente** (v. 9), o grande tema latino deste salmo:
  - Cassiodoro: «Ebrietas sobria, vinolentia gloriosa» e a conclusão («O laudabilem nimis
    ebrietatem!»);
  - Ambrósio: três embriaguezes (do cálice, das Escrituras, do Espírito); a casa é a Igreja, a
    torrente o Espírito Santo, a fonte do paraíso com as quatro virtudes; a torrente que cresce no
    inverno da perseguição;
  - Gregório: bebe sem se embriagar quem ouve e não muda; o ébrio de Deus fica estranho a si mesmo;
  - Bernardo, *De diligendo Deo* 33 (comer antes da morte, beber depois, embriagar-se na
    ressurreição; «sobria ebrietas… non madens vino, sed ardens Deo») e Semana Santa 9;
  - Tomás (a embriaguez é excesso: a boca do desejo na fonte); Belarmino (só o ébrio deixa de ter
    sede; a sabedoria bebida gota a gota virá como torrente); Ricardo de São Vítor («aliud est
    gustare, aliud est potare»); Anselmo, *Proslogion* 25; Arnóbio (a casa nasceu do lado aberto).
- **A fonte da vida e a luz** (v. 10): Ambrósio (Cristo, fonte que desceu para regar a secura do
  coração; na sua luz vemos o Pai); Cassiodoro (fonte e luz, contrárias entre nós, uma coisa só em
  Deus); Tomás (a razão humana, «refulgentia divinae claritatis in anima»; luz da natureza, da graça e
  da glória; e na *Suma*, o «lumen gloriae»); Isaac de Stella (o olho só vê o sol na luz do sol);
  Bernardo, *Cântico* 18, 4 (concha, não canal); Máximo de Turim (a fonte junto do poço da
  samaritana); Jerônimo (*Commentarioli*: na luz do Pai, que é Cristo, a luz do Espírito; *In Is.*
  XVI); Ambrósio, *De fuga* e *Exhortatio*; Belarmino (o espelho das criaturas e o face a face).
- **O pé da soberba e a queda** (vv. 12–13): Cassiodoro (ninguém fica de pé num pé só); Ambrósio
  (cair do alto é precipício; o pé sem olho; «Nescit stare superbia»); Bernardo, Carta 393 (a
  soberba tem um pé, a humildade dois) e *Cântico* 85, 6; Cassiano, *Inst.* XII, 6; Gerhoh (a pedra
  que só descansa no seu lugar: Deus é o lugar da alma); Jerônimo (*Commentarioli*: Caim na terra de
  Nod, «agitação»).
- Sem excerto: v. 4 (Judas que «não quis entender», em Ambrósio, § 15, só no arquivo) e v. 11.

## O que não existe ou não se achou (não procurar de novo)

- **Santo Hilário não comentou o Sl 35**: nenhum *Tractatus* (cobrem os Sl 1, 2, 9, 13, 14, 51–69,
  91, 118–150; conferido no texto 21450). Só citações do v. 7 («Judicia tua sicut abyssus multa»)
  no *Tract. in Ps. 118* (PL 9, 514C–D, a diferença entre «judicia oris tui» e «judicia tua») e no
  *Tract. in Ps. 119*; o comentário espúrio aos Sl 15/31/41 (6864) cita o mesmo versículo.
- **Santo Ambrósio**: tem a *Explanatio* inteira (as *Enarrationes* cobrem os Sl 1, 35–40, 43, 45,
  47, 48, 61). ***De mysteriis* e *De sacramentis* não citam o Sl 35**; a «praeclara ebrietas, quae
  sobrietatem mentis operatur» de *De sacramentis* V, 3, 17 (PL 16, 450A) comenta o «calix
  inebrians» do Sl 22. O hino «Splendor paternae gloriae» («laeti bibamus sobriam ebrietatem
  Spiritus») também não é comentário deste salmo. *De Isaac et anima* não cita o salmo. Outras
  citações, guardadas no arquivo e não nos achados: *De Spiritu Sancto* I, 142 e 152–154 (leitura
  trinitária: o Pai fonte, o Filho luz, o Espírito luz), *De paradiso* 1, 4 e 3, 13, *De
  interpellatione* II, 2, 6, *De Abraham* I, 9, 88, *De fide* I, 7, 49, *In Lucam* VII, 208,
  *In Ps. 118* sermão 13, 17.
- **São Jerônimo**: nenhum *Tractatus* sobre o Sl 35 (nenhuma das duas séries de Morin). Os
  *Commentarioli* têm só notas curtas (vv. 2, 6, 7, 10, 13). Nas obras da PL, o salmo é citado
  dezenas de vezes por três frases (ver `jeronimo-cartas-e-comentarios.md`).
- **São Gregório Magno**: não comentou os Salmos; só as citações acima e *Moralia* XXXIII, 4 (os
  montes = apóstolos e profetas, só registro). O *In I Regum* (PL 79, 137B) hoje é de Pedro de Cava.
- **São Leão Magno**: nenhuma citação útil (Sermões 7631, Cartas 7630: só Ep., PL 54, 757A, o v. 4
  contra um herege).
- **Regra de São Bento**: não cita o salmo (o «torrens voluptatis infinitae» de PL 66, 237D é do
  comentador, não de Bento).
- **São Boaventura**: não procurado (não está na PL; a edição de Quaracchi está no archive.org em
  imagem, sem busca de texto feita). **Dionísio Cartuxo** e **Glosa Ordinária**: não consultados.
- **Ricardo de São Vítor**: as *Adnotationes mysticae in Psalmos* (texto 11526) não comentam o Sl 35;
  citam o v. 9 nas notas aos Sl 28 e 121 e o v. 7 na nota ao Sl 139.
- **Pedro Lombardo, «Haimo», pseudo-Beda, *Breviarium*, Bruno Cartuxo**: guardados sem excertos.
  Compilam Agostinho e Cassiodoro (o pé único da soberba, de Cassiodoro, está em Haimo e Lombardo;
  o *Breviarium* copia literalmente os *Commentarioli* de Jerônimo).
- **Santos em língua vulgar** (Teresa, João da Cruz, Francisco de Sales…): não procurados (grupo dos
  modernos).

## Avisos para a seleção

- **Belarmino: o texto guardado é OCR bruto**, com notas da margem no meio das frases e o cabeçalho
  da p. 222 lido «252». Os excertos foram limpos à mão («quae» por «qu*», «sapientiae» por
  «sapienti*», «injusta» etc.). Conferir com as imagens das pp. 222–224 antes de publicar.
- **Jerônimo, *Commentarioli***: Jerônimo leu «Electi sunt» (v. 13), que a nota entende «Eiecti»; a
  tradução segue o sentido («foram expulsos»).
- **Tom com os judeus**: Ambrósio (§§ 2–3, 20) e Bruno de Segni (v. 7) leem trechos contra os judeus;
  esses trechos ficaram de fora. No sermão de Bernardo da Semana Santa, o excerto pula a frase «O
  Judaei, lapides estis…».
- **Não são santos**: Arnóbio (semipelagiano), Gerhoh. Cassiano: «venerado como santo no Oriente e
  em Marselha». Isaac de Stella e Guerrico de Igny: bem-aventurados (culto local cisterciense).
  Ricardo de São Vítor: não canonizado.
- **Tomás, *Suma* I, q. 12, a. 2**: a edição é a Leonina (t. 4, 1888), não a de Parma.
- **Repetições** (escolher um só):
  - a galinha e os pintinhos (v. 8): Cassiodoro, Tomás, Belarmino (e Gerhoh, só no arquivo);
  - o pé único da soberba (v. 12): Cassiodoro, Bernardo (Carta 393), e no arquivo Haimo e Lombardo;
  - «homens e animais» no presépio (v. 7): Jerônimo e Guerrico; a Escritura como trigo e feno:
    Jerônimo (*Tract. 146*) e Cassiano (*Coll.* VIII, 3, só no arquivo);
  - «embriaguez sóbria» (v. 9): Cassiodoro e Bernardo (*De diligendo Deo* 33);
  - a luz do Pai em Cristo e do Espírito (v. 10): Ambrósio (*Explanatio* 22, *Exhortatio*, *De
    Spiritu Sancto*), Jerônimo (*Commentarioli* e *Tract. 66*), *Breviarium*, Gerhoh.
- Links do Corpus Corporum abrem a obra inteira, não o parágrafo: citar a coluna da PL.
