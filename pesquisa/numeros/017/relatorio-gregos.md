# Números 17: relatório da pesquisa nos Padres gregos e bizantinos

Pesquisa de 2026-10-24 (interrompida e retomada no mesmo dia). Resultado: **22 achados** em `achados-gregos.json`
(11 com relevância 3, 11 com 2; trecho 1: 5, trecho 2: 3, trecho 3: 14). Dois são «citação curta» (Máximo, pseudo-Macário).
Textos em `textos/`: `cirilo-de-adoratione-17.md`, `cirilo-varios-17.md`, `crisostomo-varios-17.md`,
`procopio-commentarii-in-numeros-17.md`, `nissa-varios-17.md`, `clemente-romano-1cor-17.md`,
`cirilo-de-jerusalem-catequeses-17.md`, `maximo-quaestiones-et-dubia-17.md`, `pseudo-macario-sermones-64-17.md`,
`andre-de-creta-17.md`, `gregos-outros-17.md`. Orígenes, latinos, siríacos e modernos ficaram com outras frentes.

## Onde se procurou

- **Corpus do khazarzar baixado de novo neste PC** (no Linux não havia cópia): pastas inteiras de Crisóstomo (398 PDFs), Cirilo
  de Alexandria, Cirilo de Jerusalém, Basílio, Nazianzeno, Nissa, Atanásio, Teodoreto, Epifânio, Damasceno, Macário, Máximo,
  Clemente Romano e de Alexandria, Constituições Apostólicas, Paládio, Proclo, Hesíquio, Teodoro Estudita, Fócio, Ireneu,
  Severiano, Anfilóquio, Astério, Olimpiodoro, Dídimo, Eusébio; convertidos com `pdftotext` (o `fitz` não está instalado).
  Cache fora do git: `scratchpad/p-gregos/txt/` e `p-gregos/b2/txt/` (Crisóstomo), com `scripts/busca.py` (busca sem acentos,
  linhas unidas) e `scripts/extrai.py` (trecho entre duas âncoras). Atenção: os PDFs trazem «∆» (U+2206) no lugar de «Δ».
- Padrões: ῥάβδος + Ἀαρών; ῥάβδος + ἐβλάστησε/ἐξήνθησε/κάρυα; «ἀνὰ μέσον τῶν τεθνηκότων», «μέσον ζώντων»; πυρεῖα + χαλκᾶ/
  λεπίδας/θυσιαστήριον; «λεπίδας ἐλατάς», περίθεμα; θυμιατήριον + Ἀαρών; Sb 18,20–25 («ἀνὴρ ἄμεμπτος», «θυμιάματος
  ἐξιλασμόν», «ἀντέστη τῷ θυμῷ»); «ἐκόπασεν ἡ θραῦσις».
- **Hinografia**: a base AGES (`AGES-Initiatives/ages-alwb-library-gr-gr-cog`, clone raso de 54 MB, 2 369 arquivos `.ares`),
  busca de Ἀαρών em todos os livros; conferência na PG 97 e 98 (imagens do archive.org, `bim_early-english-books-1641-1700_1860_97`
  e `_98`; o OCR do item «PatrologiaGraeca», Vol. 097, serve para achar a página).
- **Colunas**: OCR do item «PatrologiaGraeca» (Vol. 033, 044, 046, 075, 096–098) e da PG 87/1 (`patrologiaecurs267unkngoog` e
  `patrologiae_cursus_completus_gr_vol_087_1`); `scripts/iapag.py` diz em que página de um item do archive.org está uma frase.

## O que se achou e entrou

- **Trecho 1**: Cirilo, *De ador.* IX (a continuação da fala publicada em Nm 16: o altar de bronze como «lembrança e anúncio» da
  revolta contra o grande sacerdote; o fim do culto em sombras); Crisóstomo, *Adv. Iud.* VI, 6 (as lâminas falam pela vista,
  como a vara: achado novo, que o relatório de Nm 16 não tinha); Procópio (santos por terem sido oferecidos; o fogo estranho);
  Máximo, *Quaest. et dub.* 155 (as lâminas = a mente de zelo sem conhecimento, afinada pelo ensinamento); Teodoreto, *Quaest.* 34.
- **Trecho 2**: Cirilo, *De ss. Trinitate* I (Aarão com o incenso = o Filho mediador); Cirilo, *In Os.* 4,8 (o sacerdote que aplaca
  a ira e consagra a própria alma); Procópio («Pai, perdoa-lhes»: quem governa não rejeita o povo que o faz sofrer).
- **Trecho 3**: Clemente Romano 43; Crisóstomo, *Adv. Iud.* VI, 6 («as folhas em lugar de letras»), *In s. Romanum*, *Hb* hom. 15;
  Nissa, *Vida de Moisés* II, 284–286 (a noz) e a oração fúnebre por Melécio (o bispo, arca com a vara florida); Cirilo, *De ador.* X
  (a ressurreição) e *In Is.* 11,1 (a nogueira que tira o sono); Cirilo de Jerusalém, *Cat.* 18, 12; pseudo-Macário; André de Creta,
  *Hom. I* sobre a Natividade de Maria e o Triódio da Segunda-feira Santa; Cosme (a Cruz); Constituições Apostólicas II, 27.

## Achado e não usado (textos guardados)

- Nissa, *Vida de Moisés* I, 70–71 (a vara «seca, descascada e sem raiz»): repete Crisóstomo e Cirilo de Jerusalém. Nissa, *In
  Basilium fratrem* (GNO X/1, 125–126: o coração de cada fiel feito arca, com a vara do sacerdócio sempre florindo): par do Melécio.
- Cirilo, *Glaphyra* in Gn 49,9 (PG 69, 353: a vara de Aarão = símbolo da ressurreição) e in Ex 4 (PG 69, 469: a vara = o Filho,
  por quem o Pai reina): repetem *De ador.* X e *In Is.* 11,1. Cirilo, *Expositio in Ps.* 43 (cadeia de Mai, PG 69, 1024: os justos
  intercedem pelo povo «como Aarão com o turíbulo»): atribuição menos segura.
- Crisóstomo, *1 Cor* hom. 31, 4 (PG 61, 264: a inveja dos rebeldes fez Deus votar duas vezes por Aarão); *In Ps.* 147 (PG 55, 480:
  lenho seco com fruto mais belo que as árvores plantadas); *In Ps.* 117, 3 (PG 55, 329–330: o fogo, a terra aberta e a vara, honras
  dos sacerdotes). Espúrios na pasta: *Contra haereticos et in s. Deiparam* (PG 59, 709–712: a vara, figura da Virgem), *In
  resurrectionem domini* B (a vara de Aarão ↔ o bastão da cruz que fez o ladrão dar fruto), *In illud Memor fui Dei*.
- Epifânio, *Ancoratus* 95 e *Panarion* (Holl I, 200): a vara seca, sinal da ressurreição (repete Cirilo de Jerusalém).
  Constituições Apostólicas V, 7 (o mesmo argumento). Damasceno, *Exp. fidei* IV, 11 (a vara entre os tipos da Cruz) e *Contra os
  que rejeitam as imagens* III (a vara «imagem do mistério da Virgem», venerada: Kotter, citação curta). Olimpiodoro, *In Eccl.*
  12,5 (PG 93, 617: a vara de nogueira = Cristo; no século futuro floresce a palavra sacerdotal). Tudo em `gregos-outros-17.md`.
- André de Creta, Triódio da Segunda-feira Santa, teotókio da ode 1 (PG 97, 1400 C–1401 A: as varas de Moisés e de Aarão e o seio
  da Mãe de Deus, «que inova um parto novo»): em `andre-de-creta-17.md`; não virou achado para não haver dois iguais de André.
- Procópio sobre a vara (só latim, PG 87/1, 843–846): copia Cirilo (*In Is.* 11,1 e *De ador.* X); citar Cirilo. Procópio sobre
  os 14 700 mortos: «partim pereunt, partim discunt» (latim), bom, mas curto.
- **Hinografia não conferida numa edição antiga** (só na AGES; usar quando houver o Menaion escaneado): «Κατεπλάγη Ἰωσήφ»
  (autômelo do 4º tom: José se espanta e lembra «a vara de Aarão que floresceu»; `he.a.m4`); Natividade de Maria, 8/9: doxastikon
  das apósticas de Sérgio Hagiopolita («ἡ τοῦ Ἀαρὼν βλαστήσασα ῥάβδος, ἐκ τῆς ῥίζης τοῦ Ἰεσσαί») e teotókio da ode 4 do cânon de
  André de Creta; Moisés, 4/9 (cânon atribuído a Teófanes, teotókios de Clemente): «a vara de Aarão mostrou que farias brotar a
  libertação dos pecados: tu te tornaste propiciação»; Apresentação de Maria, 21/11, ode 4 («Ἐβλάστησεν ἡ ῥάβδος, ποτὲ τοῦ
  Ἀαρών»); 22/11, ode 4; Anunciação, 25/3, ode 1 do 2º cânon («Ῥάβδος Ἀαρών, βλαστησαμένη πρώην»); 27/1 e 19/2 (as nozes: «como ela
  as nozes, assim tu fizeste florescer Cristo»); Octoeco, 4º tom, segunda-feira, teotókio das apósticas («χαῖρε ἡ Ῥάβδος Ἀαρών»).
  O cânon do Akathistos (José Hinógrafo, ode 7) diz só «vara mística» que fez florescer a flor que não murcha, sem Aarão; o hino
  Akathistos propriamente dito não fala da vara.

## O que não existe ou não se achou

- **Aarão «entre os mortos e os vivos» em Crisóstomo, Basílio, Nazianzeno, Nissa, Atanásio, Teodoreto, Epifânio, Damasceno,
  Máximo, Teodoro Estudita, Fócio**: nada. Nos gregos, só Cirilo (três vezes) e Procópio. «Ἔστη… καὶ ἐκόπασεν ἡ θραῦσις» nos
  gregos é quase sempre Fineias (Sl 105,30 LXX).
- **Sb 18,20–25 ligado a Aarão**: nenhum grego do corpus cita «ἀνὴρ ἄμεμπτος» ou «θυμιάματος ἐξιλασμόν» a propósito de Nm 17.
- **Clemente de Alexandria, Ireneu (grego), Basílio, Nazianzeno, Atanásio autêntico, Dídimo, Eusébio**: nada sobre Nm 17
  (Atanásio só em homilias espúrias e na *Synopsis*). **Paládio**, *Diálogo* 1 (ed. Malingrey, SC 341, citação curta): «entre
  seiscentos mil, um só foi proclamado, Aarão, e o prodígio da vara que deu nozes fez os muitos respeitarem o sacerdote como
  escolhido por Deus», logo antes de Datã e Abiram; não usado (repete Clemente e Crisóstomo). **Teodoreto** não tem pergunta própria sobre a vara florida (só a q. 34).
- **Damasceno**: as homilias marianas autênticas (Natividade, Dormição) não estão no khazarzar; a da Anunciação (PG 96, 648 ss.,
  «χαίροις, ἡ ἁγιόβλαστος ῥάβδος Ἀαρών») é de autenticidade discutida. **Germano** e **Romano**: não procurados a fundo (sem
  texto pesquisável à mão); **Akathistos**: ver acima.
- Máximo, *Quaest. et dub.* 155: não está na PG 90 (só na ed. Declerck, CCSG 10).

## Cuidados

- **Cirilo** faz Beseleel «da tribo de Dã» (no Êxodo é de Judá; Dã é Ooliab) e lê κάρυα, «nozes»; o nosso texto diz amêndoas.
  Cirilo, Procópio, Olimpiodoro: a nogueira «tira o sono» (Jr 1,11 LXX, «vara de nogueira», ligada a ἐγρήγορα); o hebraico
  *shaqed* é amendoeira, a que «vigia».
- **Colunas a conferir**: 1 Clem 43 (PG 1, 293–296, pelo hábito; o OCR não deu); Teodoreto q. 34 (PG 80, 384); Nissa *Vida de
  Moisés* II (PG 44, 417–420, pelo OCR); Melécio (PG 46, 852–864, faixa da obra). *De ss. Trinitate*: o texto do PDF (Durand, SC 231)
  foi comparado com o OCR da PG 75, 689–692 e coincide; marcado como domínio público.
- **Procópio**: o grego foi refeito comparando dois OCR; variantes da PG anotadas no arquivo de textos.
- **André de Creta** e **Cosme**: transcritos da imagem da PG 97 e 98; os livros litúrgicos atuais têm pequenas diferenças
  (registradas em `andre-de-creta-17.md`).
- Crisóstomo, *Adv. Iud.* VI, 6: ele põe as varas antes dos turíbulos e atribui a Moisés a ordem das lâminas.

## Pistas para outros capítulos

- **Nm 18** (o sacerdócio e os dízimos): Teodoreto, *Quaest.* 34 (segunda metade: dízimos, «aliança de sal», os levitas sem
  herança); Procópio, PG 87/1, 845–848 (Nm 18,1 ss., grego e latim); Crisóstomo, *In Ps.* 117, 3 (honra dos sacerdotes).
- **Nm 20** (a morte de Aarão, Meribá): cânon de Moisés (4/9) na AGES; Nissa, *Vida de Moisés* (a rocha).
- **Nm 25** (Fineias): «ἔστη Φινεὲς καὶ ἐξιλάσατο» em Crisóstomo, *Adv. Iud.* (o zelo de Fineias), *In Kalendas* e *In Ps.* 105;
  Teodoreto, *In Ps.* 105, *Hist. relig.* (Jacó de Nísibis) e *Quaest. in Reg.*; Teodoro Estudita, *Cartas*.
- Cirilo, *Glaphyra in Gn* (as varas de Jacó, Gn 30: estoraque, nogueira, plátano) para Gênesis.
