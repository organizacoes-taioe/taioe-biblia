# Gênesis 4: relatório do grupo «latinos» (26/10/2026)

Latinos antigos e medievais, menos Agostinho. Partiu-se da pré-pesquisa (`BASE.md`: Ambrósio, *De Cain et Abel*, a obra
inteira; Beda; Ruperto; Rábano; Alcuíno; Isidoro; Hugo; Jerônimo; Lápide) e das pistas de `../proximos.md` («Gn 4» e
«Gn 4–11»), e procurou-se o resto nos sermões, cartas e tratados da PL. Entregues **16 achados** em
`achados-latinos.json`: trecho 1 = 7 (um deles, Tomás, para um eventual tema da liturgia), trecho 2 = 6, trecho 3 = 2,
trecho 4 = 1. Nove autores; Ambrósio tem 5, Gregório 3, Beda 2.

## Como se procurou

1. Leitura inteira das obras da base: Ambrósio, *De Cain et Abel* I–II (o grosso é alegoria moral da alma; o que
   comenta a cena está em I, 1–3, I, 7 e 10, e II, 6–10); Ruperto, *In Genesim* IV, 2–11 (IV, 2 está antes do corte da
   base, no texto inteiro do cache); Beda, *In principium Genesis* II; Jerônimo, *Quaestiones hebraicae*; Hugo; Alcuíno;
   Isidoro. Rábano e Lápide por amostra (compilação; OCR ruim no Lápide).
2. Varredura dos 169 textos da PL que já estavam em `pesquisa/cache/genesis/latinos/` (cache de Gn 1–3) pelas notas de
   Migne «(Gen. IV…)» e por 45 frases de Gn 4 na Vulgata e na Vetus Latina (*vox sanguinis*, *custos fratris*, *maior est
   iniquitas*, *septuagies septies*, *in foribus*, *dominaberis illius*, *recte offeras*, *signum Cain*, *invocare nomen
   Domini*…): 727 parágrafos com ocorrência, 505 com mais que o nome de Caim ou de Abel, resumidos numa linha cada.
3. Baixados do Corpus Corporum três textos que faltavam: Cipriano, *De dominica oratione* (125); Tertuliano, *De patientia*
   (48) e *Adversus Iudaeos* (62). Corpus Thomisticum: `sth4083.html` (III, q. 83) e `sth3034.html` (II-II, q. 34–43,
   para a inveja, q. 36), no cache.
4. Cada `original` saiu por script como substring exata do texto limpo (sem as notas de Migne, as marcas de coluna e os
   números de página), com as colunas calculadas sozinhas. Scripts em `~/.cache/taioe-gn4/latinos/` (`varrer.py`, `par.py`,
   `ver.py`, `excerto.py` com `specs.json`, `gerar.py`, `base.py`); `excertos.json` ali guarda também os originais prontos
   de três reservas (`cip-zelo-5`, `rup-4-10`, `crisol-109`).
5. Gravados em `base/` os trechos das obras novas (cabeçalho de `../../COMO-PESQUISAR.md`): `cipriano-de-dominica-oratione`,
   `cipriano-de-zelo-et-livore`, `tertuliano-de-patientia`, `zenao-tractatus`, `gregorio-moralia` (IV, V, XIII),
   `gregorio-moralia-2` (XXII), `jeronimo-epistula-36`, `bernardo-sermones-in-cantica-61`, `ambrosio-in-lucam-8`,
   `pedro-crisologo-sermo-109`, `tomas-summa-3-83-4`; e `_ausentes-latinos.md`, `_pistas-latinos.md`.

## O que se achou

| autor | obra | onde | situação |
|---|---|---|---|
| Santo Ambrósio | *De Cain et Abel* I, 1, 2 («Adquiri um homem por meio de Deus»: Deus autor, não instrumento) | PL 14, 316A–317A | achado (2) |
| Santo Ambrósio | *De Cain et Abel* II, 9, 27–28 (Deus pergunta para levar à confissão; «nega como diante de quem não sabe, recusa guardar o irmão como se estivesse fora da natureza, foge do juiz») | PL 14, 354D–355B | achado (3) |
| Santo Ambrósio | *De Cain et Abel* II, 9, 30 («clama o sangue, não o irmão»; a terra testemunha e juiz) | PL 14, 356A–B | achado (3) |
| Santo Ambrósio | *De Cain et Abel* II, 10, 35 e 38 (o sinal convida à correção; a mansidão ensinada aos juízes; «não quis punir o homicida com o homicídio») | PL 14, 358A–360A | achado (3) |
| Santo Ambrósio | *In Lucam* VIII, 23–24 (sobre Lc 17,4: Lamec setenta e sete vezes, o perdão setenta vezes sete) | PL 15, 1771C–1772C | achado (2) |
| Santo Ambrósio | *De Cain et Abel* I, 7, 25 (duas culpas: ofereceu «depois de dias» e não das primícias); II, 6, 18 («Deus não se aplaca pelos dons, mas pelo afeto de quem oferece»; a tristeza de Caim, testemunho da consciência); II, 7, 24 («Pecaste, sossega»: depois de pecar, não defender o pecado; «pelo pudor a culpa diminui, pela defesa se acumula»); II, 8, 26 («Vamos ao campo»: o lugar sem fruto escolhido para o crime); II, 9, 32 («nada é mais grave que o errante ser abandonado por Deus») | PL 14, 329D; 350B; 353B–C; 354A–B; 357A–B | reserva |
| Santo Ambrósio | *Explanatio* do Sl 35 (36 no hebraico) (o sinal, para que a morte não lhe tirasse o tormento: «ele mesmo era o seu carrasco»); *De Iacob* II, 11, 48 (a voz do sangue nos Macabeus); *Ep.* 2, 10 (o remorso de Caim) | PL 14, 956D–957A; 634C; PL 16, 881C | reserva (o primeiro lê o sinal como castigo, o contrário de II, 10, 35) |
| Santo Ambrósio | *De sacramentis* IV, 6, 27: o Cânon «sicut suscipere dignatus es munera pueri tui iusti Abel» | PL 16, 445B–446A | só a oração, sem comentário; o mais antigo testemunho do texto do Cânon: para o tema da liturgia, se houver (grupo dos modernos) |
| São Cipriano | *De dominica oratione* 24 (Deus olhava os corações; Abel ensina a vir ao altar; feito sacrifício, primeiro mártir) | PL 4, 536A–B | achado (3) |
| São Cipriano | *De zelo et livore* 5 («as primeiras inimizades da nova fraternidade»; Abel «sofreu o ódio sem saber odiar») | PL 4, 641B | reserva forte (original pronto) |
| São Cipriano | *De bono patientiae* 10 (Abel «não resiste nem luta, mas, humilde e manso, é morto com paciência») e 16 (setenta vezes sete) | PL 4, 628B; 632B | reserva (Cipriano 24 diz o mesmo de Abel) |
| São Gregório Magno | *Moralia* V, 46, 84 (só se inveja quem se julga melhor; Caim eliminou o irmão que via melhor) | PL 75, 727C–728A | achado (3) |
| São Gregório Magno | *Moralia* IV, 19, 36 (o pecado à porta quando bate nos pensamentos; dominá-lo no começo) | PL 75, 655B–C | achado (3) |
| São Gregório Magno | *Moralia* XIII, 23, 26 (o sangue de Abel pediu a morte do fratricida, o de Cristo a vida dos perseguidores; Hb 12,24) | PL 75, 1029A–B | achado (3) |
| São Gregório Magno | *Moralia* XXII, 14, 28 («não Abel pelos dons, mas os dons por Abel»: Deus olhou primeiro para quem dava); XXXIII, 38, 67 (a chama da inveja) | PL 76, 229C–230A; 716B | reserva (o primeiro é a fórmula mais citada da ideia de Cipriano 24) |
| Ruperto de Deutz | *In Gen.* IV, 3 (o rosto voltado para a terra; Deus o chama ao próprio coração antes do crime) | PL 167, 327B–328A | achado (3) |
| Ruperto de Deutz | IV, 2 (Abel ofereceu primeiro o coração, Caim guardou-se a si mesmo); IV, 6 (o sangue de Cristo «interpela pelo mundo inteiro» pela boca da terra fiel); IV, 7 (os sete pecados de Caim, de Jerônimo); IV, 9 (o sinal como o selo do rei, que ninguém ousa tocar); IV, 10 («a primeira causa das cidades terrenas é o homicídio»); IV, 11 (Set) | PL 167, 326C–327A; 330D–331B; 332B–C; 334D–335D; 336B; 337A–C | reserva (IV, 10 com original pronto) |
| São Zenão de Verona | *Tractatus* I, 6, 3, sobre a paciência («o mundo vazio se espanta de ser pequeno para dois») | PL 11, 314B–315A | achado (3) |
| São Jerônimo | *Ep.* 36, 2 a Dâmaso (Caim não quis pedir perdão; se esconde da luz) | PL 22, 453–454 | achado (2) |
| São Jerônimo | *Ep.* 36, 3–7 (o servo que pede a morte; as setenta e sete gerações até Cristo; os sete pecados de Caim; adiado sete gerações «para que ao menos fizesse penitência»); *Adversus Iovinianum* I, 14 («Lamec, sanguinário e homicida, dividiu uma só carne em duas mulheres»); *Quaest. hebr.* 4,6-8 e 4,16 | PL 22, 454–456; PL 23, 233C; 944B–945B | reserva; cálculo de gerações (fora, pelo pedido); a do *Adv. Iov.* é polêmica contra as segundas núpcias |
| São Bernardo | *Sermões sobre o Cântico* 61, 3–4 (as chagas do Senhor; «errou aquele que disse: A minha iniquidade é grande demais») | PL 183, 1072B–C | achado (3) |
| São Bernardo | *Cântico* 16 (Judas e Caim confessaram, mas sem esperança: «confissão infiel»); *De diversis* 66, 3 («desde então ficou o costume de os maus se levantarem contra os bons»); *De adventu* 3, 6 (o prelado não pode dizer com Caim «sou eu o guarda do meu irmão?») | PL 183, 854A; 689B–C; 46D | reserva |
| São Beda | *In principium Genesis* II, sobre 4,20–22 (as artes, usadas como o viajante usa a hospedaria) | PL 91, 74A–C | achado (3) |
| São Beda | II, sobre 4,25–26 (Set no lugar de Abel; Enós, «homem», reza tanto mais quanto se sabe frágil; o «Pai nosso») | PL 91, 76D–77C | achado (3) |
| São Beda | II, sobre 4,2 (Abel, «luto»: nem os primeiros irmãos puderam ter paz); 4,3-5 (Noé e Melquisedec também ofereceram frutos da terra: não foi o tipo de oferta, mas a mente; Deus olha «primeiro a pessoa, depois os dons»); 4,8 (Abel segue o irmão com simplicidade, Caim pensa esconder-se de Deus no campo); 4,9 («resposta estulta e soberba»); 4,10 (a voz do sangue dos mártires: «clamam não por ódio, mas por amor da justiça», Ap 6,9) | PL 91, 63B–C; 63D–64B; 65D–66A; 66A–B; 66B–67A | reserva (4,10 forte) |
| São Tomás | *Suma* III, q. 83, a. 4, obj. 8 e ad 8 («os dons do justo Abel» no Cânon) | Leonina 12 | achado (2), para o tema da liturgia |
| São Pedro Crisólogo | Sermão 109 (Caim, «sacerdote ingrato», queimou o pior e guardou o melhor; Abel, levando um cordeiro, «é recebido como cordeiro»; Caim, levando palha, achou o combustível para se queimar) | PL 52, 502A | reserva (original pronto) |
| Tertuliano | *De patientia* 5 (a impaciência: Caim só matou porque se irou, e só se irou porque foi impaciente) | PL 1, 1258A | reserva; Zenão diz o mesmo melhor |
| São Cromácio de Aquileia | *Tract. in Matthaeum* sobre Mt 5,23-24 (as ofertas de Caim recusadas porque guardava ira contra o irmão) | PL 20, 346B–347A | reserva; repete Cipriano 24 |
| Santo Hilário | *Tract. in Ps.* 119, 4 (Deus pergunta «para dar o perdão ao pecado ou a honra à fé»: Adão confessou, Caim negou) | PL 9, 647C–648B | reserva; o mesmo que Ambrósio II, 9, 27 |
| Isidoro, Rábano, Alcuíno, Hugo, Lápide | | | base; ver `base/_ausentes-latinos.md` |

## Os 16 achados

1. **Trecho 1 (vv. 1–8)**: Ambrósio I, 1, 2: «Adquiri um homem por meio de Deus», Deus autor, não instrumento (2);
   Cipriano, *Oração do Senhor* 24: Deus olhava os corações; Abel, pacífico, ensina a vir ao altar e se torna o primeiro
   mártir (3); Gregório, *Moralia* V, 46: o invejoso se confessa menor (3); Ruperto IV, 3: o rosto voltado para a terra,
   e Deus que o chama ao coração (3); Gregório, *Moralia* IV, 19: o pecado à porta bate nos pensamentos (3); Zenão I, 6, 3:
   «o mundo vazio se espanta de ser pequeno para dois» (3); Tomás III, q. 83, a. 4: os dons do justo Abel no Cânon (2).
2. **Trecho 2 (vv. 9–16)**: Ambrósio II, 9, 27–28: a pergunta que chama à confissão e a resposta que nega o irmão (3);
   Ambrósio II, 9, 30: clama o sangue, não o irmão (3); Gregório, *Moralia* XIII, 23: o sangue que fala melhor que o de
   Abel (3); Jerônimo, *Ep.* 36, 2: Caim não quis pedir perdão (2); Bernardo, *Cântico* 61, 3–4: as chagas de Cristo
   contra o desespero de Caim (3); Ambrósio II, 10, 35 e 38: o sinal e a mansidão ensinada aos juízes (3).
3. **Trecho 3 (vv. 17–24)**: Beda: as artes e a hospedaria (3); Ambrósio, *In Lucam* VIII, 23–24: Lamec e o perdão (2).
4. **Trecho 4 (vv. 25–26)**: Beda: Set e Enós, a oração de quem se sabe frágil (3).

Os mais fortes: `ambrosio-cain-abel-2-9-30-nao-o-irmao-o-sangue`, `ambrosio-cain-abel-2-10-35-38-o-sinal-e-a-mansidao`,
`zenao-tratado-1-6-3-o-mundo-pequeno-para-dois`, `bernardo-cantico-61-3-4-as-chagas-e-o-erro-de-caim`,
`cipriano-oracao-dominical-24-deus-olhava-os-coracoes`, `gregorio-moralia-13-23-26-o-sangue-que-fala-melhor`.

## Sobreposições (para a escolha final)

Conferido no fim com `achados-agostinho.json` e `achados-modernos.json`, que já estavam na pasta (os dos gregos e dos
orientais ainda não). O que cruza diretamente:

- Cipriano 24 × Agostinho, *In Ep. Io.* 5, 8 (Deus «não olhou para as mãos, mas para o coração») × Francisco de Sales
  (primeiro o coração): a mesma ideia três vezes. Cipriano é o mais antigo e acrescenta Abel mártir; se o tema encher,
  fica um dos três.
- Gregório IV, 19 × Agostinho, *Civ.* XV, 7, 2 (v. 7): Agostinho lê a Bíblia grega («sossega»); Gregório lê a Vulgata,
  como o nosso texto, e diz quando se domina o pecado (no começo, quando bate nos pensamentos).
- Ambrósio II, 9, 27–28 × Agostinho, *Contra Faustum* XII, 10 (Deus pergunta como juiz) × *Evangelium vitae* 19 (todo homem
  é guarda do irmão): Ambrósio junta a pergunta e a resposta; se o tema encher, cortá-lo até «Pesa agora a resposta».
- Ambrósio II, 10 × *Evangelium vitae* 9 × Agostinho, *Op. imp.* VI, 23 (o sinal): Ambrósio diz a mansidão ensinada aos juízes,
  que os outros dois não dizem.
- Bernardo, *Cântico* 61 × *Evangelium vitae* 21 (v. 13): João Paulo II vê na confissão de Caim um resto de consciência;
  Bernardo responde ao desespero com as chagas. Dizem coisas diferentes.
- Beda sobre as artes × Newman, *PPS* 7, 18 (Tubalcaim) × Francisco, 27/05/2020 (os ofícios e a violência): Beda é o único
  antigo e diz o uso «de passagem»; os três se completam, mas é provável que caiba só um ou dois.
- Ambrósio, *In Lucam* VIII × Francisco, 27/05/2020 (o canto de Lamec): Ambrósio liga ao perdão de Mt 18,22.
- Beda sobre Set e Enós × Agostinho, *Civ.* XV, 18 (Enós esperou) × Francisco, 27/05/2020 (a oração, dique contra o mal) ×
  Catecismo 2569: o tema da oração em 4,26 está cheio; Beda diz a fragilidade que reza e o «Pai nosso».
- Tomás III, q. 83 × `liturgia-canon-romano-os-dons-do-justo-abel` (modernos): Tomás explica o porquê da petição do Cânon;
  vai junto ou fica fora com ele.

Outras sobreposições, previstas pelo `PEDIDO.md`:

- **As duas ofertas** (vv. 3–5): Cipriano 24 é a raiz latina da ideia que Agostinho, *Civ.* XV, 7 («dar a Deus algo seu e
  guardar-se a si mesmo»), Ruperto IV, 2 (Abel ofereceu primeiro o coração), Gregório XXII, 14, 28 («não Abel pelos dons,
  mas os dons por Abel») e Beda (Deus olha primeiro a pessoa) repetem; Ireneu IV, 18, 3 (gregos) diz o mesmo. Fica
  Cipriano, que diz também Abel mártir; se o tema da liturgia ficar com Ireneu ou Agostinho, a fórmula de Gregório é a
  alternativa mais curta. Crisólogo 109 (o cordeiro e a palha) é a imagem mais viva, para o caso de faltar uma.
- **A inveja** (v. 5): Gregório V, 46 (o invejoso se confessa menor) e Cipriano, *De zelo* 5 (Abel sofreu o ódio sem saber
  odiar) dizem coisas diferentes; Gregório copia a série de exemplos de Cipriano (Esaú, José, Saul). Clemente de Roma e
  Basílio (gregos) e o Catecismo 2538 (modernos) devem disputar o tema: se sobrar lugar para um latino, Gregório.
- **«Por que estás irado?» e «tu o dominarás»** (vv. 6–7): Ruperto IV, 3 (Deus chama ao coração antes do crime) e
  Gregório IV, 19 (o pecado bate à porta dos pensamentos) se completam; Crisóstomo, *Hom.* 18, 6 (gregos) e Agostinho,
  *Civ.* XV, 7 dirão o mesmo que Ruperto e Gregório, respectivamente. Ambrósio II, 7, 24 lê a Bíblia grega («pecaste,
  sossega») e fica de reserva.
- **O assassínio** (v. 8): Zenão não repete ninguém. Beda sobre 4,8 (Abel segue o irmão com simplicidade) é reserva.
- **«Onde está Abel?» e «o guarda do meu irmão»** (v. 9): Ambrósio II, 9, 27–28 junta as duas coisas; Hilário e Beda dizem
  a primeira parte; os modernos (*Evangelium vitae* 8, Francisco em Lampedusa) dirão a segunda: se o tema encher, cortar
  Ambrósio até «Pesa agora a resposta do fratricida».
- **A voz do sangue** (v. 10): Ambrósio II, 9, 30 (o sangue, não o irmão; a terra testemunha) e Gregório XIII, 23 (Hb 12,24)
  dizem coisas diferentes. Ruperto IV, 6 e Beda dizem o de Gregório; Beda sobre os mártires (Ap 6,9) é uma terceira
  ideia, de reserva. O Catecismo 2259 e Hb 12,24 virão dos modernos.
- **«A minha iniquidade é grande demais»** (v. 13): Jerônimo diz o desespero, Bernardo o remédio; se só couber um, Bernardo
  (que nomeia o erro de Caim). Bernardo, *Cântico* 16 (Judas e Caim, a confissão sem esperança) é outra forma do contraste
  pedido com Pedro ou Davi.
- **O sinal** (v. 15): Ambrósio II, 10 casa com *Evangelium vitae* 9 (modernos); Ambrósio, *Expl. Ps.* 35 (36), lê o sinal ao
  contrário (para que vivesse no tormento), e Jerônimo e Beda também: ficaram fora, por não iluminarem a cena como o
  Ambrósio de *De Cain*.
- **A cidade** (v. 17): o tema é de Agostinho (*Civ.* XV, 1–5); Ruperto IV, 10 («a primeira causa das cidades terrenas é o
  homicídio», original pronto) só se o grupo de Agostinho não trouxer a cidade de Caim fundada por um fratricida.
- **Lamec e «setenta e sete»** (vv. 23–24): Ambrósio, *In Lucam* VIII, 23–24, é o único latino que liga o canto ao
  perdão de Mt 18,22 e acaba em «aprende a perdoar»; Agostinho, *Sermão* 83, e Basílio, *Ep.* 260, dirão o mesmo com mais
  vagar. O começo (o descanso do sétimo dia) pode ser cortado se ficar longo: o excerto se sustenta a partir de «Foi esse
  o mistério».
- **Set e Enós** (vv. 25–26): Beda e Agostinho, *Civ.* XV, 18 e 21 (a esperança), se completam; Beda diz a oração de quem
  se sabe frágil.

## Dúvidas e escolhas

- **Termos**: as citações bíblicas dentro dos comentários seguem o texto que cada Padre leu. Ambrósio lê «Adquiri um homem
  por meio de Deus» (o argumento depende do «por meio de»); Gregório e Ruperto, a Vulgata («O teu pecado estará à porta,
  mas o seu desejo estará debaixo de ti, e tu o dominarás»); Jerônimo, *Ep.* 36, a Bíblia grega («A minha culpa é grande
  demais para que eu seja perdoado», «gemendo e tremendo»); Bernardo, a Vulgata («para que eu mereça perdão»); Beda,
  «Este começou a invocar o nome do Senhor» e «cítara e órgão» (traduzi «flauta», como no nosso v. 21).
- **Gregório, *Moralia* V, 46**: o versículo comentado é Jó 5,2 («a inveja mata o pequeno»); daí o «pequeno» do excerto. Está
  dito na `passagem`; se o Gere achar obscuro, cortar a primeira frase com «pequeno» e começar em «Foi por isso que Caim».
- **Zenão**: o *Tractatus* I, 6 trata da paciência; o excerto começa em Caim, sem o parágrafo sobre Adão. «Fraterni invidus
  muneris» ficou «invejando a oferta do irmão».
- **Ambrósio II, 10, 35 e 38**: dois parágrafos não seguidos (o 36–37 é sobre a imortalidade da alma); o «terceira razão» do
  segundo se refere às razões do sinal que Ambrósio vem enumerando.
- **Ambrósio, *In Lucam* VIII, 23–24**: o parêntese de Ambrósio («nada pode ofender quem tem o costume de perdoar») caiu na
  extração automática (o script tira tudo o que está entre parênteses, por causa das notas de Migne) e ficou fora do excerto.
- **Bernardo, *Cântico* 61**: o sermão comenta Ct 2,14 («nas fendas da rocha»); o excerto começa em «Cometi um grande
  pecado», a frase que situa, e só a segunda peça fala de Caim. «Nisi quod non erat de membris Christi» ficou «Só se explica
  porque ele não era dos membros de Cristo».
- **Tomás**: obj. 8 e resposta, sem os rótulos; a objeção virou frase («parece, portanto, que não convém»).
- **Beda**: «dicente parente» (4,25) ficou «quando a mãe diz», como no hebraico; Beda não diz quem.
- **Jerônimo, *Ep.* 36, 2** depende da Bíblia grega e foi copiado por Beda quase palavra por palavra; ficou Jerônimo, que é a
  fonte.

## Para o `autores.json`

Falta **São Zenão de Verona** («bispo de Verona († c. 371)», `oriental: false`); `autor_id` usado: `zenao-de-verona`. Os
outros já estão lá: `ambrosio`, `cipriano`, `gregorio-magno`, `ruperto`, `jeronimo`, `bernardo`, `beda`, `tomas-de-aquino`.

## Para o catálogo `pesquisa/fontes/latinos.md`

- Ids de texto novos no Corpus Corporum: Cipriano, *De dominica oratione* **125** (`CypCar.DeOrDo`); Tertuliano, *De
  patientia* **48**, *Adversus Iudaeos* **62**; Zenão, *Tractatus* **6894** (`ZenVer.Tracta2`); Cromácio, *Tract. in Mt.*
  **7084**; Cesário (1172): *Sermones* da PL 67 = **7852** (só uma parte; o resto está no apêndice de Agostinho, PL 39).
- Corpus Thomisticum: III, q. 83 em `sth4083.html`; II-II, q. 34–43 em `sth3034.html`.
- No Gregório do Corpus Corporum, o `limpar_pl` parte os parágrafos dos *Moralia* em pedaços nas notas de Migne; o
  `excerto.py` junta o texto inteiro antes de procurar, então funciona.

## Para outros capítulos

- **Gn 3**: Tertuliano, *De patientia* 5 (PL 1, 1256B–1257C) e Zenão, *Tract.* I, 6, 3 (PL 11, 314A–B): a queda pela
  impaciência (a mulher «não suportou» o mandamento; Adão perdeu-se por impaciência com o diabo e com Deus).
- **Gn 5**: Ruperto IV, 10 e Beda (PL 91, 73B): Henoc, o sétimo depois de Adão, que «andou com Deus», contra Henoc, filho de
  Caim e nome da cidade («dedicação»): os justos esperam a dedicação futura. Jerônimo, *Ep.* 36, 7 (PL 22, 456): Henoc
  arrebatado na sétima geração.
- **Gn 6–9**: Beda (PL 91, 74D–75A): o dilúvio veio quando os homens se entregaram às artes, à música e aos prazeres (Mt
  24,38); Pedro Crisólogo, Sermão 147 (PL 52, 594D): depois do dilúvio Deus chama Noé com «sermão brando», para curar o
  mundo do medo.
- **Gn 22**: Ambrósio, *De Cain et Abel* I, 8, 29–31 (PL 14, 331B–332B): a prontidão de Abraão («levantou-se de manhã»), contra
  o «depois de muitos dias» de Caim.
