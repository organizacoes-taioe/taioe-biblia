# Números: mapa das fontes (pré-pesquisa de 2026-10-20)

Mapa do livro dos Números para a pesquisa dos capítulos 1–11 e 17–36 (os capítulos 12–16 já têm pesquisa própria em `numeros/012` a `016`). Pedido do Gere
(20/10/2026): baixar as obras antes e deixá-las cortadas por capítulo, para que o grosso da pesquisa já esteja feito quando ele pedir o capítulo.

- **Onde estão os textos**: `numeros/<ccc>/base/<autor>-<obra>.md` (cabeçalho do `COMO-PESQUISAR.md`, seção «Pré-pesquisa»); o índice de cada capítulo é
  `numeros/<ccc>/BASE.md` (gerado por `ferramentas/base-indice.py`). Em cada `base/` há também `_ausentes-numeros.md` (quem não comenta o capítulo) e
  `_pistas-numeros.md` (onde ainda procurar). O que os pedidos e relatórios de Nm 12–16 anotaram sobre outros capítulos: `numeros/proximos.md`.
- **Como refazer**: `python -I -X utf8 pesquisa/ferramentas/base/num-tudo.py` roda os 17 scripts de Números, na ordem, e o `base-indice.py --todos`. Cada script baixa a obra
  UMA vez para `pesquisa/cache/base/numeros/` (fora do git; ~60 MB com os PDFs e os OCR) e corta por capítulo; o módulo comum é `_numeros_comum.py`.
  Rodar o Python com `-I -X utf8`; no Git Bash, `MSYS_NO_PATHCONV=1` quando um argumento começar com `/`.
- **Outras mãos na mesma pasta**: outros agentes gravam em `numeros/<ccc>/base/` as fontes orientais em siríaco e a hinografia (Narsai, Jacó de Sarug, Dionísio bar Salibi, Cosme de
  Jerusalém…), com os scripts `ori-*.py`; elas aparecem no `BASE.md` e não são descritas aqui.
- **A pré-pesquisa só baixa e corta**: não traduz nem escolhe. Texto original e inteiro do que cada obra diz do capítulo; a pesquisa do capítulo parte do `BASE.md` e procura o resto.

## 1. Numeração e divisão

O capítulo é sempre o da **Nova Vulgata** (NV, numeração do hebraico). Os Padres citam a Vulgata de Jerônimo (Clementina) e a LXX; cada arquivo diz a divisão da fonte no campo *Passagem*.

| NV (hebraico) | Vulgata de Jerônimo e LXX antiga | Observação |
|---|---|---|
| 12,16 | 13,1 | Nm 13 deles começa um versículo antes (12,16 nosso) e vai até o 13,34; o 14 coincide (14,1–45) (pedido de Nm 13 e de Nm 14) |
| 15 | 15 | coincide (15,1–41) (pedido de Nm 15) |
| 16,1–35 | 16,1–35 | |
| **17,1–15** | **16,36–50** | os turíbulos batidos em lâminas para o altar, a murmuração do dia seguinte, a praga e Aarão entre os mortos e os vivos com o turíbulo |
| **17,16–28** | **17,1–13** | a vara de Aarão que floresce |
| 18–24 | 18–24 | coincidem |
| 25,19 | 26,1 (primeira oração) | a Vulgata põe no começo do cap. 26 o que o hebraico tem no fim do 25; o resto de 26 coincide |
| 29 (39 vv.) | 29 (40 vv.) | o v. 40 da Vulgata é o 30,1 hebraico |
| 30,1 | 29,40 | o 30,2 hebraico é o 30,1 da Vulgata (30 tem 17 vv. no hebraico, 16 na Vulgata) |
| 31–36 | 31–36 | coincidem |

- A edição de Rahlfs (1935, a LXX usada no script de pontuação) segue o hebraico em 16–17 (16 tem 35 vv., 17 tem 28) e em 30 (17 vv.), mas segue a Vulgata em 25/26 (25 tem 18 vv.): as edições antigas da LXX (Swete) e os Padres citam como a Vulgata.
- Os 16,36–50 da Vulgata são o nosso 17 (o pedido de Nm 16 manda anotar o que os Padres dizem deles numa seção «Para Nm 17»: ver `proximos.md`).
- Nos Padres a numeração dos Salmos é a grega e latina; nos de Números o único cuidado é o da tabela acima.

## 2. As obras: onde cobrem, com que divisão

### 2.1 Latinos

Todos os textos latinos vêm do Corpus Corporum (Univ. de Zurique, PL de Migne revista), exceto Lápide (OCR do archive.org) e Orígenes (OCR do archive.org, GCS). O PL traz as colunas
(`[col. 0687A]` nos arquivos) e as notas de Migne (referência bíblica de cada passagem, no rodapé); `[N]` no texto remete à nota. «cobertura» abaixo = capítulos NV com arquivo em `base/`.

| Obra | O que é e como se divide (capítulo da obra → Nm NV) | Edição | URL do texto (campo *Fonte*) | Script | base/ |
|---|---|---|---|---|---|
| **Orígenes**, *Homiliae in Numeros* (versão latina de Rufino) | 28 homilias; cobrem Nm 1–4, 11–14, 17–18, 21–34 (ver 3.1: H9 = Nm 17; H12–13 = Nm 21; H27 = Nm 33); **não há homilia sobre Nm 5–10, 19–20, 35, 36** | GCS 30 (*Origenes Werke* VII, Baehrens 1921); PG 12; Lommatzsch t. 10 (páginas «Del.» e «Lomm.» nas margens do texto) | https://archive.org/details/origenes-werke.-bd-7-1921 (OCR: `…/download/origenes-werke.-bd-7-1921/Origenes%20Werke.%20Bd%207%2C%201921_djvu.txt`) | `lat-origenes-num.py` | 21 arquivos, 754 KB; Nm 1–4, 11, 17–18, 21–34 |
| **Santo Agostinho**, *Quaestiones in Heptateuchum* IV | 65 questões, referências «[Ib. XII, 1.]» da Vulgata; cobrem Nm 1, 3–6, 8–11, 17–23, 25, 27, 30–31, 35 (ver 3.4) | PL 34, 717–?; CSEL 28/1 (Zycha 1895) | https://mlat.uzh.ch/browser/cps_2.AugHip.QuInHe (texto 7312; o augustinus.it, `latino/questioni_ettateuco/quest_ettateuco_4_libro.htm`, estava fora do ar em 20/10, HTTP 503, e troca o grego por imagens) | `lat-agostinho-num.py` | 21 arquivos, 107 KB; Nm 1, 3–6, 8–11, 17–23, 25, 27, 30–31, 35 |
| **Santo Agostinho**, *Locutiones in Heptateuchum* IV | notas de gramática sobre a Vetus Latina de Agostinho, uma por expressão, referência «[Ib. VI, 2.]»; uma entrada «[Ib. 9.]» sem capítulo continua no último citado | PL 34, 521–?; CSEL 28/1 | https://mlat.uzh.ch/browser/cps_2.AugHip.LoInHe (texto 7311) | `lat-agostinho-num.py` | 28 arquivos, 45 KB; Nm 1, 3–11, 17–23, 25–35 |
| **Santo Isidoro**, *Quaestiones in Vetus Testamentum*, In Numeros | só a *Praefatio* e 42 capítulos = as 42 mansões de Nm 33 (de Jerônimo, Ep. 78); em cada mansão resume o episódio ocorrido: cap. XII (Sinai) = Nm 1–10, XIII = Nm 11, XIV = Nm 12, XV (Rethma) = Nm 13–19, XXXIII–XXXIV = Nm 20, XXXVI e XXXIX = Nm 21, XLI–XLII = Nm 22–36 (ver 3.2) | PL 83, 339–? | https://mlat.uzh.ch/browser/cps_2.IsiHis.QuInVeT (texto 21433) | `lat-isidoro-num.py` | 25 arquivos, 104 KB; Nm 1, 3–11, 17, 19–29, 31–33 |
| **Rábano Mauro**, *Enarrationes in librum Numerorum* | compilação em 4 livros (I = Nm 1–8; II = Nm 9–20,13; III = Nm 20,14–27; IV = Nm 28–36), com as fontes às vezes indicadas («Ex Augustino»): Orígenes/Rufino quase palavra por palavra, Agostinho, Jerônimo (Ep. 78), Isidoro; cobre os 36 capítulos (ver 3.3) | PL 108, 587–? | https://mlat.uzh.ch/browser/cps_2.RabMau.EnInLiN (texto 8898) | `lat-rabano-num.py` | 31 arquivos, 742 KB; Nm 1–11, 17–36 |
| **pseudo-Beda**, *Quaestiones super Numeros* | diálogo Discipulus/Magister em 29 capítulos curtos, copiados de Isidoro; sem capítulo sobre Nm 2, 3, 7, 18, 30 e 34–36 (ver 3.5; os capítulos de Nm 12–16 não foram cortados) | PL 93, 395–410 | https://mlat.uzh.ch/browser/cps_2.AuInBe.QuSuNu (texto 8484) | `lat-pseudobeda-num.py` | 23 arquivos, 72 KB; Nm 1, 4–6, 8–11, 17, 19–29, 31–33 |
| **Ruperto de Deutz**, *De Trinitate et operibus eius*: In Numeros | 2 livros: I = 40 capítulos (Nm 1–14), II = 32 capítulos (Nm 15–36); versículo a versículo, sentido literal e depois alegórico; sem capítulo próprio sobre Nm 27–29, 31–32, 34–36 (só o resumo final, II cap. XXXII); ver 3.6 | PL 167, 835–? | https://mlat.uzh.ch/browser/cps_2.RupTui.DeTrEtO (texto 10873) | `lat-ruperto-num.py` | 31 arquivos, 276 KB; Nm 1–11, 17–36 |
| **São Bruno de Segni**, *Expositio in Pentateuchum*: In Numeros | 36 capítulos que acompanham os da Vulgata; XVI inclui Vulg. 16,36–40 (= NV 17,1–5), XVII = a vara, XXVI–XXVII = Nm 27,22–23, **XXXII, XXXIV e XXXVI só dizem «omittitur»**; Nm 26 sem capítulo | PL 164, 435–? | https://mlat.uzh.ch/browser/cps_2.BruAst.ExInPe (texto 21403) | `lat-bruno-num.py` | 27 arquivos, 127 KB; Nm 1–11, 17–25, 27–31, 33, 35 |
| **Hugo de São Vítor**, *Adnotationes in Pentateuchon* | só 4 notas literais sobre Números (cap. XIV da obra: «NUM. XIV», «XVIII», «XXI», «XXIV» de Migne); acaba com «Et haec in Numeros. Reliqua enim desideramus» | PL 175, 29–86 | https://mlat.uzh.ch/browser/cps_2.HuDeSVi.AdInPe (texto 11054) | `lat-hugo-num.py` | 3 arquivos, 6 KB; Nm 18, 21, 24 |
| **Paterius**, *Liber testimoniorum* (excertos de Gregório Magno), livro IV | 24 excertos, cada um com a nota de Migne «Num. X, Y»; o livro **salta de Nm 11 a Nm 16** e acaba em Nm 35 (ver 3.7) | PL 79, 761–? | https://mlat.uzh.ch/browser/cps_2.PaNoGrI.ExVeAcN (texto 8106) | `lat-paterio-num.py` | 13 arquivos, 61 KB; Nm 6–11, 17, 19, 22–24, 32, 35 |
| **Cornélio a Lápide**, *Commentaria in Numeros* | versículo a versículo, 36 capítulos da Vulgata (cada um com «SYNOPSIS CAPITIS»); XVI (a partir do v. 37) + XVII = Nm 17; OCR com as colunas misturadas; páginas estimadas | ed. Vivès, Paris, 1866–1868 (A. Crampon), t. II, pp. ~192–389 | https://archive.org/details/commentariainscr02lapi_0 (página P = imagem n(P+31)) | `lat-lapide-num.py` | 31 arquivos, 907 KB; Nm 1–11, 17–36 |

### 2.2 Gregos e orientais

Textos gregos da «Ψηφιακή Πατρολογία» (Univ. do Egeu, 2006; espelho `https://khazarzar.skeptik.net/pgm/PG_Migne/<pasta>/<obra>.pdf`), exceto Procópio e Efrém (OCR do archive.org).
Os PDFs de PG trazem as colunas «69.592» (viram `[PG 69, 592]`); os que seguem edição moderna (Teodoreto, Nissa) trazem outra numeração e têm possível direito autoral: **citação curta** na publicação.

| Obra | O que é e como se divide | Edição | URL do texto (campo *Fonte*) | Script | base/ |
|---|---|---|---|---|---|
| **São Cirilo de Alexandria**, *Glaphyra in Pentateuchum* (in Numeros) | só 5 episódios de Números, lidos como figura de Cristo: Nm 12; Nm 13–14; Nm 15,17–29 com Lv 23 («Ὅτι γέγονεν ἡμῖν ἄρτος ζωῆς ὁ Χριστός»); **Nm 19** («Περὶ τῆς δαμάλεως τῆς πυῤῥᾶς», PG 69, 625–636); **Nm 21,6–9** («Περὶ τοῦ ὄφεως τοῦ χαλκοῦ», PG 69, 636–641). Só Nm 19 e 21 caem no que se pediu | PG 69, 589–641 | https://khazarzar.skeptik.net/pgm/PG_Migne/Cyril%20of%20Alexandria_PG%2068-77/Glaphyra%20in%20Pentateuchum.pdf | `grc-cirilo-num.py` | 2 arquivos, 43 KB; Nm 19, 21 |
| **São Cirilo de Alexandria**, *De adoratione et cultu in spiritu et veritate* | 17 livros (diálogo com Paládio); cita Números dezenas de vezes («ἐν τοῖς Ἀριθμοῖς»). O script divide nas falas {ΚΥΡ.}/{ΠΑΛΛ.} e guarda as que têm ≥ 8 grupos de 4 palavras em comum com a LXX do capítulo (≥ 5 se dizem «ἐν τοῖς Ἀριθμοῖς») ou uma palavra-chave do episódio. **Não é a obra inteira** nem as alusões sem citação | PG 68, 133–1125 | https://khazarzar.skeptik.net/pgm/PG_Migne/Cyril%20of%20Alexandria_PG%2068-77/De%20adoratione%20et%20cultu%20in%20spiritu%20et%20veritate.pdf | `grc-cirilo-num.py` | 28 arquivos, 541 KB; Nm 1–11, 17–26, 28–33, 35 |
| **São Cirilo de Alexandria**, *Fragmenta duo in Numeros* | dois fragmentos de cadeia: Nm 18,26 («Ἀφελεῖτε ὑμεῖς ἀπ' αὐτοῦ ἀφαίρεμα») e Nm 20,8 («Λαβὲ τὴν ῥάβδον») | fragmentos (ed. Mai) | https://khazarzar.skeptik.net/pgm/PG_Migne/Cyril%20of%20Alexandria_PG%2068-77/Fragmenta%20duo%20in%20Numeros.pdf | `grc-cirilo-num.py` | 2 arquivos, 2 KB; Nm 18, 20 |
| **Teodoreto de Ciro**, *Quaestiones in Octateuchum*: In Numeros | 51 perguntas numeradas I–LI no corpo («XXII Τίνα χρὴ νοῆσαι τὴν αἰθιόπισσαν…»), de Nm 1 a Nm 36, com lacunas (ver 3.8). O PDF segue a ed. Fernández Marcos–Sáenz-Badillos (1979), **sem colunas da PG** | PG 80, 349–400 | https://khazarzar.skeptik.net/pgm/PG_Migne/Theodoretus%20of%20Cyrrhus_PG%2080-84/Quaestiones%20in%20Octateuchum.pdf | `grc-teodoreto-num.py` | 24 arquivos, 125 KB; Nm 1, 3–6, 8–11, 17–27, 31, 33, 35–36 |
| **Procópio de Gaza**, *Commentarii in Octateuchum*: In Numeros | catena (Cirilo, Teodoreto, Orígenes, Nissa) com o latim de Clauser e, em alguns trechos, escólios gregos; sem título de capítulo nem número de versículo; o script atribui unidades de ~1500 caracteres do OCR por palavras-chave, em ordem: **aproximado** | PG 87/1, 793–897 (Nm 12 = 823–828; Nm 14 = 829–836; Nm 15 = 835–838, segundo os relatórios) | https://archive.org/details/patrologiaecurs267unkngoog (OCR); o grego lê melhor em `patrologiae_cursus_completus_gr_vol_087_1` | `grc-procopio-num.py` | 29 arquivos, 286 KB; Nm 1, 3–11, 17–28, 30–36 |
| **Santo Efrém** (atribuído), *In quartum Pentateuchi librum, qui Numeri dicitur, Explanatio* | tradução latina de uma cadeia siríaca (Assemani, *Opera Syriaca et Latina* I, pp. 250–272); o OCR do siríaco é ilegível (cortado); latim com «s longo»; atribuição aos capítulos por palavras-chave: **aproximada**; Nm 13–14 = pp. 258–259, Nm 15 = pp. 259–260 | Assemani, Roma 1737, t. I | https://archive.org/details/assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-1 | `sir-efrem-num.py` | 15 arquivos, 80 KB; Nm 1, 3–4, 6, 9, 11, 17, 19–22, 25, 27, 31, 35 |
| **São Gregório de Nissa**, *Vida de Moisés* | livro I (a história) §§ 61–76 passam por Números; livro II (a contemplação) §§ 256–304 cobrem Nm 12–25 como etapas da alma (ver 3.9); o PDF segue a GNO VII/1 (Musurillo 1964): seções «livro.seção» | PG 44, 297–430 | https://khazarzar.skeptik.net/pgm/PG_Migne/Gregory%20of%20Nyssa_PG%2044-46/De%20vita%20Mosis.pdf | `grc-nissa-num.py` | 8 arquivos, 65 KB; Nm 11, 17, 20–25 |
| **Orígenes** (cadeia), *Adnotationes in Numeros* e *Selecta in Numeros* (acréscimo: não estava no pedido) | escólios gregos de cadeia, atribuição incerta: as *Adnotationes* têm 6 notas com título «ΚΕΦ. ΚΒʹ.» (cap. e versículo da LXX); a *Selecta* (PG 12, 576–584) vai de Nm 11 a 36 sem títulos (a maior parte é sobre Balaão) | PG 17, 21; PG 12, 576–584 | https://khazarzar.skeptik.net/pgm/PG_Migne/Origenes_PG%2011-17/Adnotationes%20in%20Numeros.pdf e …/Selecta%20in%20Numeros.pdf | `grc-origenes-num.py` | 6 arquivos, 59 KB; Nm 11, 18, 22–25 |

## 3. Tabelas de correspondência (divisão de cada obra → capítulo NV)

Nm 12–16 aparecem nas tabelas quando a divisão da obra os mistura com os pedidos (os arquivos de `base/` só existem para 1–11 e 17–36).

### 3.1 Orígenes, *Homiliae in Numeros* (28 homilias; versão de Rufino)

| Homilia | Tema (título e lema) | Nm NV | Observação |
|---|---|---|---|
| H1 | «Divinis Numeris non omnes digni sunt» (abertura do livro, o recenseamento) | 1 | |
| H2 | «De ordine et collocatione castrorum» | 2 | |
| H3 | «et ego assumpsi Levitas de medio filiorum Istrahel…» | 3 | Nm 3,12 ss. |
| H4 | «viginti duo milia numero inventos esse primogenitos» | 3 e 4 | Nm 3,39 e o começo de 4: entra inteira nos dois capítulos |
| H5 | «nolite exterminare de tribu sua plebem Caath» | 4 | Nm 4,18 |
| H6 | «exiit Moyses ad populum» e os setenta anciãos, e a etíope | 11 (§§ 1–3) e 12 (§ 4) | Nm 11,24–29; § 4 = Nm 12,1 |
| H7 | «Rursum de Aethiopissa et de lepra Mariae» | 12 e 13 (§ 5) | Nm 12 e 13,1 |
| H8 | «De his quae ab exploratoribus renuntiantur» | 13–14 | |
| **H9** | «De batillis Chore et seditione populi adversum Moysen et de virgis, in quibus virga Aaron germinavit» | **17** | Vulg. 16,36–17,13 inteiro. **Não há homilia sobre Nm 16,1–35** (o próprio Orígenes diz que Nm 16 não se lera antes) |
| H10 | «tu et filii tui et domus patris tui … sumetis peccata sanctorum» | 18 | Nm 18,1 |
| H11 | «De primitiis offerendis» | 18 | Nm 18,8 ss. (primícias e dízimos); 50 KB |
| H12 | «De puteo et cantico eius» | 21 | Nm 21,16–18 (o poço) |
| H13 | «De his quae superfuerunt priori tractatui, et de Balaam atque asina eius» | 21 (§§ 1–2: Seon e Og) e 22 (§ 3 ss.) | corte na posição +7879 do OCR |
| H14 | «Item de Balaam» | 22 | |
| H15 | «De prophetia Balaam» | 23 | 1.ª profecia (Nm 23,7–10) |
| H16 | «Priore tractatu… Secundae nunc prophetiae initium» | 23 | 2.ª profecia (Nm 23,18–24) |
| H17 | «Tertiam nunc prophetiam» | 24 | Nm 24,3–9 |
| H18 | «Quartam nunc prophetiam» | 24 | Nm 24,15–19 |
| H19 | «Quinta haec nobis eademque ultima Balaam visio» | 24 | Nm 24,20–24 (Amalec, o cineu); corte na posição +22600 |
| H20 | «Lectio hodie recitata est… de fornicatione viri Istraheli[tae]» | 25 | Baal-Fegor, Finéias |
| H21 | «De eo quod secundo populus numeratus est» | 26 | |
| H22 | «De filiabus Salphaat et de successore Moysis» | 27 | |
| H23 | «Si observatio sacrificiorum… munera mea data mea» (as festas) | 28 (§§ 1–8) e 29 (§§ 9–10) | corte na posição +27042 |
| H24 | «De sacrificiis… per unamquamque festivitatem… et de votis» | 28, 29 (§ 1) e 30 (§§ 2–3) | corte na posição +10920 |
| H25 | «De ultione, quae in Madianitas facta est» | 31 | |
| H26 | «De summa numeri filiorum Istrahel» | 31 (§§ 1–2) e 32 (§ 3 ss.) | corte na posição +10358; Rúben, Gad e meia tribo |
| H27 | «De mansionibus filiorum Istrahel» | 33 | 65 KB de OCR |
| H28 | «Quae sit terrae sanctae descriptio terminorumque eius et finium» | 34 | |

O texto das homilias vai das posições 76839 (H1) a 838361 (começo das homilias sobre Josué) do OCR; o script confere uma frase do começo de cada homilia antes de cortar.
O OCR mistura o aparato crítico («vgl.», variantes «BCE», referências «Num. N, V» no pé da página, que são da Vulgata), os números de linha e perde linhas inteiras: **transcrever da imagem antes de citar**
(página P = imagem n(P+36) no Bd. 7; as margens trazem as páginas de Delarue = PG 12 e de Lommatzsch).

### 3.2 Isidoro, *In Numeros* (PL 83, 339 ss.): parágrafo → capítulo de Números

| Capítulo de Isidoro (mansão de Nm 33) | Parágrafos | Nm NV |
|---|---|---|
| *Praefatio* | §§ 1–4 (o nome do livro, as 42 mansões) | 1 e 33 |
| XII (Sinai) | § 1 | 1 |
| | § 2 (recenseamento, levitas, ofertas dos príncipes, trombetas) | 1, 3, 7, 10 |
| | § 3 (a Páscoa do segundo mês) | 9 |
| | §§ 4–6 (nazireus) | 6 |
| | § 7 (leprosos e imundos fora do arraial) | 5 |
| | § 8 (a partir dos vinte anos) | 1 |
| | §§ 9–10 (levitas de 25 a 50 anos) | 4 e 8 |
| | §§ 11–12 (a luta contra os vícios; os levitas raspam os pelos) | 8 |
| | §§ 13–15 (as duas trombetas de prata) | 10 |
| XIII (sepulcros da concupiscência) | §§ 1–3 | 11 |
| XIV (Haserot) | §§ 1–2 | 12 |
| XV (Rethma) | §§ 3–4 (sumário: exploradores, Core, o turíbulo, a vara, a vitela ruiva) | 17 |
| | §§ 5–11 (exploradores, o cacho na vara, os dois carregadores) | 13 |
| | §§ 12–13 (o homem da lenha) | 15 |
| | §§ 14–15 (Core, Datã e Abiron) | 16 |
| | §§ 16–19 (o turíbulo de Aarão entre os vivos e os mortos; a vara) | 17 |
| | §§ 20–28 (a vitela ruiva) | 19 |
| | § 29 (volta às mansões) | |
| XVI–XXXII | uma mansão por capítulo, sem episódio de Números | 33 |
| XXXIII (Cades) | §§ 1–6 (Maria morre; as águas da contradição) | 20 |
| XXXIV (monte Hor) | § 1 (Aarão morre) | 20 |
| | § 2 (o rei de Arad) | 21 |
| XXXVI (Phunon) | §§ 1–4 (as serpentes e a serpente de bronze) | 21 |
| XXXIX (Dibongad) | §§ 1–3 (Seon e Og) | 21 |
| XLI (Abarim) | §§ 1–2 | 27 |
| XLII (campos de Moab) | §§ 2–5 (Balaão e a jumenta) | 22 |
| | § 2 (as bênçãos) | 23, 24 |
| | §§ 6–8 (o conselho de Balaão; Finéias) | 25 |
| | §§ 9–10 (os 600 mil e os dois que entram) | 26 |
| | §§ 11–12 (as filhas de Salfaad; Josué sucede a Moisés) | 27 |
| | § 13 (os sacrifícios do ano) | 28 e 29 |
| | § 14 (Madiã; a morte de Balaão) | 31 |
| | § 15 (Rúben e Gad) | 32 |
| | § 16 (destruir os ídolos) | 33 |

Nm 33 recebe a *Praefatio* e os 42 capítulos inteiros (47 KB). Os parágrafos que servem a mais de um capítulo entram em todos eles. O relatório de Nm 14 dizia que Isidoro «salta de Nm 13 (cap. 15) às mansões de Nm 33 (cap. 16)»: o cap. XV (Rethma) é longo (11 KB) e cobre Nm 13–19.

### 3.3 Rábano Mauro, *Enarrationes in librum Numerorum* (PL 108): livro e capítulo → Nm NV

| Livro | Capítulos de Rábano → Nm |
|---|---|
| I | I = 1 · II = 1,47–54 (os levitas não são recenseados) · III = 2 e o começo de 3 · IV = 3,1ss (os filhos de Aarão) · V = 3,11ss (levitas pelos primogênitos) · VI = 4 · VII = 5,1–4 (leprosos) · VIII = 5,5–10 · IX = 5,11ss (zelotipia) · X = 6,1–21 (nazireu) · XI = 6,22–27 (bênção) · XII = 7 (seis carros) · XIII = 7 (dedicação) · XIV = 8,1–4 (candelabro) · XV = 8,5–22 (purificação dos levitas) · XVI = 8 (levitas pelos primogênitos) · XVII = 8,23–26 |
| II | I = 9,1–14 (Páscoa) · II = 9,6–14 · III = 9,15–23 e 10 (partir) · IV = 10,1–10 (trombetas) · V = 10,29–36 (Hobab) · VI = 11,1–3 · VII = 11,16–30 (os setenta) · VIII = 11,31–35 (codornizes) · IX = 12 · X = 13 · XI = 14 · XII = 15,1–16 · XIII = 15,17–21 (primícias) · XIV = 15,22–29 · XV = 15,30–31 · XVI = 15,32–41 (lenha, franjas) · XVII = 16,1–35 (Core) · **XVIII = 17,1–5 (turíbulos; Vulg. 16,36–40) · XIX = 17,6–15 (Vulg. 16,41–50) · XX = 17,16–28 (a vara; Vulg. 17)** · XXI = 18,1–7 · XXII = 18,8–20 · XXIII = 18,21–32 · XXIV = 19 · XXV = 20,1–13 |
| III | I = 20,14–29 e 21,1–3 · II = 21,4–9 · III = 21,10–20 · IV = 21,21–32 · V = 21,33–35 · VI = 22 · VII = 23–24 (profecias) · VIII = 25,1–5 · IX = 25,6–13 · X = 26 · XI = 27,1–11 · XII = 27,12–23 |
| IV | I = 28–29 · II = 30,1–? (voto do homem) · III = 30 (voto da mulher) · IV = 31,1–12 · V = 31,13–24 · VI = 31,25–54 · VII = 32 · VIII = 33,1–49 · IX = 33,50–56 · X = 34 · XI = 35,1–8 · XII = 35,9–34 · XIII = 36 |

A correspondência com Números foi lida dos títulos de Rábano (aproximada nas pontas). O corte usa as notas de Migne «N: (CAP. X.)», que marcam no texto onde começa cada capítulo da Vulgata; o título «CAPUT …» colado antes da marca entra no capítulo. Nm 17 começa no título «CAPUT XVIII. De thuribulis…». O prefácio a Freculfo (col. 587) não entra em nenhum capítulo.

### 3.4 Santo Agostinho, *Quaestiones in Heptateuchum* IV: questão → Nm NV

| Questões (numeração do livro IV) | Referência da Vulgata | Nm NV |
|---|---|---|
| 1–3 | I, 1–44; I, 20–46; I, 51 | 1 |
| 4–6 | III, 5–7; III, 10; III, 12–31 | 3 |
| 7–8 | IV, 7; IV, 11 | 4 |
| 9–11 | V, 6–8; V, 6–7; V, 21 | 5 |
| 12 | VI, 14–17 | 6 |
| 13–14 | VIII, 24; VIII, 24–26 | 8 |
| 15–16 | IX, 6–12; IX, 15–23 | 9 |
| 17 | X, 7 | 10 |
| 18–19 | XI, 17; XI, 21–23 | 11 |
| 20 | XII, 1 | 12 |
| 21–23 | XIII, 18–26; XIII, 33; XIV, 9 | 13–14 |
| 24–25 | XV, 24–29; XV, 30–31 | 15 |
| 26–29 | XVI, 13–14; 20–21; 30; 32–33 | 16 |
| **30** | **XVI, 36–40** (os turíbulos) | **17** |
| 31–32 | XVIII, 1; XVIII, 12 (a questão 32 sai numerada «XXVII» no Corpus Corporum) | 18 |
| 33–34 | XIX, 1ss; XIX, 16 | 19 |
| 35–39 | XX, 11; 13; 17,19; 17; 24 | 20 |
| 40–45 | XXI, 2; 3; 13–14; 16; 24–25; 27 | 21 |
| 46–50 | XXII, 4–6; 7–13; 12–38; 22 e 32; 23–29 | 22 |
| 51 | XXIII, 5 | 23 |
| 52 | XXV, 4, 7, 8 | 25 |
| 53–55 | XXVII, 13–14; 18–19; 20 | 27 |
| 56–59 | XXX, 3; 4–6; 6; 7–16 | 30 |
| 60–63 | XXXI, 5–6; 8; 9; 15–16 | 31 |
| 64–65 | XXXV, 11–12; 19, 12 | 35 |

Sem questão de Agostinho: Nm 2, 7, 24, 26, 28, 29, 32–34, 36. As *Locutiones* IV têm entradas em quase todos os capítulos (só gramática da Vetus Latina dele); faltam Nm 2, 24 e 36.

### 3.5 pseudo-Beda, *Quaestiones super Numeros* (PL 93, 395–410): capítulo → Nm NV

I catálogo das mansões = 33 · II Páscoa do segundo mês = 9 · III nazireus = 6 · IV leprosos, fluxos, imundos = 5 · V idade dos guerreiros = 1 · VI levitas e guardas dos vasos = 4 e 8 ·
VII as duas trombetas = 10 · VIII sepulcros da concupiscência = 11 · IX os setenta eleitos = 11 · X Maria = 12 · XI os doze exploradores (resumo de Nm 13–19) = 17 (e 13) · XII o homem da lenha = 15 · XIII Core = 16 ·
XIV Aarão com o turíbulo = 17 · XV a vara que floresce = 17 · XVI a vitela ruiva = 19 · XVII a morte de Maria = 20 · XVIII a hesitação de Moisés na rocha = 20 · XIX a morte de Aarão e as serpentes = 20 e 21 ·
XX Seon e Og = 21 · XXI a morte de Moisés (mansão Abarim) = 33 · XXII Balaão e Balac = 22–24 · XXIII Finéias = 25 · XXIV o número do povo = 26 · XXV as cinco filhas de Salfaad = 27 ·
XXVI gêneros de oferendas = 28 e 29 · XXVII a morte de Balaão = 31 · XXVIII Rúben e Gad = 32 · XXIX a destruição dos ídolos = 33.

### 3.6 Ruperto de Deutz, *In Numeros*: livro e capítulo → Nm NV

| Livro | Capítulos de Ruperto → Nm |
|---|---|
| I (40 caps.) | I–II = 1 (a abertura sobre Ap 10 e os nomes das tribos) · III = 2 · IV = 1 (os levitas não são recenseados) · V–VI = 3 · VII–VIII = 4 · IX = 5 (leprosos) · X = 5 (a mulher suspeita) · XI–XV = 6 (nazireu) · XVI = 6 (a bênção) · XVII–XIX = 7 · XX–XXII = 8 · XXIII–XXIV = 9 · XXV–XXIX = 10 · XXX–XXXII = 11 · XXXIII–XXXV = 12 · XXXVI–XL = 13–14 |
| II (32 caps.) | I = 15 · II = 15 e 16 · III = 16 · **IV = 17 (a vara que germina)** · V = 18 · VI = 19 · VII–IX = 20 · X–XV = 21 · XVI–XVII = 22 · XVIII–XX = 23 · XXI–XXV = 24 · XXVI–XXVIII = 25 · XXIX = 26 · XXX = 30 · XXXI = 33 (as 42 mansões) · XXXII = resumo final (Nm 24–36) |

O cap. XXXII do livro II (3 KB, com as notas de Migne «Num. XXIV» … «Num. XXXVI») entra nos capítulos 27, 28, 29, 31, 32, 34, 35, 36 e 33, onde Ruperto não tem capítulo próprio. Para Nm 15 ver `numeros/015`.

### 3.7 Paterius, livro IV (excertos de Gregório Magno): capítulo → referência de Migne → Nm NV

I «Nazaraei capillos nutriunt» (Num. VI, 18) = 6 · II Moisés entra e sai da tenda (Num. 7) = 7 · III os levitas raspam os pelos (VIII, 7) = 8 · IV os levitas de 25 e 50 anos (VIII, 24–25) = 8 ·
V Moisés consulta o Senhor (IX, 7–9) = 9 · VI duas trombetas (X, 2.5) = 10 · VII «veni nobiscum» (X, 29) = 10 · VIII panelas do Egito (XI, 5–7) = 11 · IX setenta anciãos (XI, 16) = 11 · X «quis tribuat ut omnis populus prophetet» (XI, 29) = 11 ·
XI Aarão entre vivos e mortos (XVI, 47–48 Vulg.) = 17 · XII as doze varas (XVII, 2 Vulg.) = 17 · XIII–XV a vitela ruiva (XIX, 3 ss.; XIX, 15) = 19 · XVI Balaão e a jumenta (XXII, 31–33) = 22 · XVII–XIX «Moriatur anima mea morte justorum» e continuações (XXIII, 10) = 23 ·
XX–XXII «Dixit homo cujus obturatus est oculus» e «Robustum est habitaculum tuum» (XXIV, 3–4; 21) = 24 · XXIII a terra de Galaad (XXXII, 4 ss.) = 32 · XXIV o homicida volta depois da morte do pontífice (XXXV, 27–28) = 35.
Os «Item unde supra» continuam o excerto anterior. O livro IV não tem nada sobre Nm 1–5, 12–16 (saltos de 11 para 16), 18, 20, 21, 25–31, 33–34, 36.

### 3.8 Teodoreto, *Quaestiones in Octateuchum*: In Numeros (51 perguntas) → Nm NV

| Perguntas | Assunto | Nm NV |
|---|---|---|
| I–III | por que mandar recensear; por que os levitas são menos; a tribo de Judá | 1 (II também 3) |
| IV–V | obras dos sacerdotes e levitas; os primogênitos | 3 |
| VI | o pano de jacinto nos vasos | 4 |
| VII–X | o imundo «sobre a alma»; os leprosos e gonorréicos fora do arraial; «homem ou mulher… pecados humanos»; a farinha de cevada | 5 |
| XI | o voto do nazireu | 6 |
| XII–XIII | os levitas raspam os pelos; dos 25 aos 50 anos | 8 |
| XIV | a Páscoa dos imundos | 9 |
| XV–XVI | «com sinal tocareis a trombeta»; Jetro/Ragüel | 10 |
| XVII–XXI | a murmuração; castigo imediato; a dúvida de Moisés; os setenta que profetizam e não mais; Eldad e Modad | 11 |
| XXII–XXIII | a mulher etíope; só Maria castigada | 12 |
| XXIV–XXVI | os exploradores; Oseias chamado Jesus; a raça de Enac | 13 |
| XXVII | «a glória do Senhor encherá toda a terra» | 14 |
| XXVIII–XXXI | por que repetir as leis; «de mão levantada»; o homem da lenha; o jacinto das franjas | 15 |
| XXXII–XXXIII | Core, Datã e Abiram; «não olhes para o sacrifício deles» | 16 |
| **XXXIV** | os incensários dos rebeldes como revestimento do altar (e o sacerdócio dos filhos de Aarão) | **17** e 18 |
| XXXV–XXXVI | a novilha ruiva; quem asperge e quem é aspergido fica imundo | 19 |
| XXXVII | por que o Senhor se irou com Moisés e Aarão na rocha | 20 |
| XXXVIII | a serpente de bronze | 21 |
| XXXIX–XLII | Balaão adivinho; manda ir e não ir; o anjo e a jumenta; a força da maldição do adivinho | 22 (XLII também 23) |
| XLIII | «como a glória do unicórnio» | 23 |
| XLIV | «Balaão não foi, como de costume, ao encontro dos presságios» | 24 e 25 |
| XLV–XLVI | por que recensear de novo; a terra repartida por sorte | 26 |
| XLVII | Josué recebe a imposição das mãos | 27 |
| XLVIII | as mulheres madianitas mortas | 31 |
| XLIX | por que anotou as estações | 33 |
| L | o homicida involuntário volta com a morte do pontífice | 35 |
| LI | por que as tribos distintas | 36 |

Sem pergunta de Teodoreto: Nm 2, 7, 18 (só XXXIV), 28–30, 32, 34. Os números romanos fazem parte do texto; os algarismos soltos (191, 216…) são páginas da edição de 1979.

### 3.9 Gregório de Nissa, *Vida de Moisés* (seção «livro.seção» → Nm NV)

| Seções | Assunto | Nm NV |
|---|---|---|
| I, 63–64 | o povo se farta de carne | 11 |
| I, 66; II, 269–270 | a falta de água; a sede e a rocha | 20 |
| I, 67–68; II, 271–283 | a saudade do Egito, as serpentes e a serpente de bronze (o madeiro) | 21 |
| I, 69–71; II, 284–286 | a revolta pelo sacerdócio, as varas, a vara que floresce | 17 |
| I, 72; II, 287–291 | a passagem proibida pelas terras vizinhas; a vida entre os estrangeiros | 20–21 |
| I, 73–74; II, 292–297 | Balac, Balaão e a jumenta; a maldição contra quem vive na virtude | 22 (II, 292–297 também 23 e 24) |
| I, 75; II, 298–304 | Finéias e a queda no prazer | 25 |

Fora do pedido: I, 61–62 e II, 256–264 = Nm 12; I, 65 e II, 265–270 = Nm 13–14 (o cacho, II, 268). I, 61 passa pela tenda e pelas leis (Nm 1–10) sem nomear capítulo; II, 305–321 é a conclusão, sem Números.

### 3.10 Cornélio a Lápide e Bruno de Segni: coincidem com os capítulos da Vulgata

Lápide: o capítulo n de Lápide é o capítulo n de Números, exceto Nm 17 (NV) = cap. XVI a partir do v. 37 (linha «37. TOLLAT THURIBULA QUAE JACENT IN INCENDIO») mais o cap. XVII inteiro. Páginas estimadas no campo *Edição*
(âncoras: cap. XVIII ≈ p. 285; XIX ≈ 291; XX ≈ 297; XXI ≈ 303; XXII ≈ 311; XXIII ≈ 317; XXVI ≈ 345; XXVIII ≈ 353; XXIX ≈ 357; XXXII ≈ 361; XXXIII ≈ 369).
Bruno: capítulo n de Bruno = Nm n, com as exceções do quadro 2.1 (Nm 17 = cap. XVI a partir de «Deinde praecepit Dominus ut Eleazar…» mais XVII; Nm 27 = XXVI–XXVII; Nm 26, 32, 34 e 36 sem texto).

## 4. O que não existe, o que não se achou e os limites desta pré-pesquisa

### 4.1 Quem não comenta (confirmado nos relatórios de Nm 12–15 e nos textos baixados)

| Autor ou obra | Situação |
|---|---|
| **Crisóstomo** | não comentou Números nem Êxodo (só Gênesis, homilias e sermões); só citações de passagem |
| **Santo Efrém** | não há comentário autêntico a Números (só Gênesis e Êxodo); o «comentário» da ed. romana de Assemani vem de cadeias siríacas; nos hinos, nada localizado até agora |
| **Beda** | não comentou Números; o *In Pentateuchum* (PL 91, 189–394) é espúrio (breve, quase nada) e as *Quaestiones super Numeros* (PL 93) são espúrias e copiam Isidoro; Beda autêntico também não comentou o Pentateuco além do Gênesis e do Tabernáculo (*De tabernaculo*, Ex 25–30; *In principium Genesis* não conferido) |
| **São Gregório Magno** | nenhum comentário a Números; só citações nos *Moralia*, nas homilias, na *Regra pastoral* (e os excertos de Paterius) |
| **Santo Tomás** e **São Roberto Belarmino** | não comentaram Números (só citações em outras obras) |
| **Basílio, Nazianzeno, Atanásio, Dídimo, Epifânio, Macário, Máximo, Damasceno** | só menções |
| **Hugo de São Vítor** | só 4 notas curtas sobre Números |
| **Paterius** | o livro IV salta de Nm 11 a 16 e acaba em Nm 35 |
| **Bruno de Segni** | omite Nm 32, 34 e 36 («omittitur»); Nm 26 não tem capítulo; Nm 27,18–23 só tem uma frase |
| **Isidoro** | só as 42 mansões de Nm 33 |
| **Taio de Saragoça** | só um catálogo de virtudes («mansuetudinis de Moyse») |
| **Cassiano** | não cita Nm 12 nem a mansidão de Moisés |
| **Glosa Ordinária** | não está no Corpus Corporum (PL 113–114 só em imagem); para o Pentateuco é sobretudo Orígenes, Isidoro e Rábano: **não baixada** |
| **Teodoreto, *Interpretatio in xiv epistulas Pauli*; Teofilato; Ecumênio** | não estão no khazarzar |
| **Isidoro de Pelúsio, Diádoco, João Clímaco** | não estão no khazarzar; o latim de Isidoro de Pelúsio (PG 78, OCR) não tem Caleb, exploradores nem as dez tentações |
| **Hipólito** | a pasta do khazarzar só tem «extras»; não procurado |
| **Fílon** (não cristão), **Apolinário** (herético) | só para entender; não usar |

### 4.2 Limites das fontes baixadas

| Obra | Limite |
|---|---|
| Orígenes (latim) | OCR do GCS com aparato, números de linha e linhas perdidas; sem homilia sobre Nm 5–10, 19–20, 35–36 e sobre Nm 16,1–35; transcrever da imagem antes de citar; as colunas de Delarue (PG 12) só nas margens |
| Agostinho | texto do Corpus Corporum; OCR leve do Corpus (por ex. «cruet» por *eruet*); o augustinus.it (503 em 20/10/2026; cópia do Wayback Machine em `web.archive.org/web/2024id_/https://www.augustinus.it/latino/questioni_ettateuco/quest_ettateuco_4_libro.htm`) troca as palavras gregas por imagens |
| Isidoro, Rábano, pseudo-Beda, Ruperto, Bruno, Hugo, Paterius | texto revisto da PL no Corpus Corporum; as notas de Migne ficam no texto; os cortes em capítulos de Números vêm das notas de Migne ou dos títulos dos capítulos |
| Lápide | OCR com as duas colunas misturadas, «æ» estropiado e a coluna dos versículos intercalada; páginas só estimadas |
| Teodoreto | o PDF não traz as colunas da PG 80 (segue a ed. de 1979); possível direito autoral da edição: citar curto |
| Cirilo, *Glaphyra* | só cinco episódios de Números |
| Cirilo, *De adoratione* | seleção **automática** (4-gramas da LXX de Rahlfs, sem os que também estão em Gn–Dt, mais palavras-chave): pode faltar fala que só alude, e podem sobrar falas que repetem fórmulas; as falas são do diálogo ({ΚΥΡ.}, {ΠΑΛΛ.}); a PG 68 só traz a coluna |
| Procópio | OCR com grego e latim intercalados; sem título de capítulo; atribuição aproximada (unidades de ~1500 caracteres); faltam texto para Nm 2 e 29; o grego dos escólios lê melhor no OCR `patrologiae_cursus_completus_gr_vol_087_1` |
| Efrém | só o latim de Assemani; o OCR do siríaco é ilegível; «s longo»; atribuição aproximada; sem texto para Nm 2, 5, 7, 8, 10, 18, 23, 24, 26, 28–30, 32–34 e 36 |
| Nissa | o PDF segue a GNO (Musurillo 1964): sem colunas da PG 44; possível direito autoral da edição: citar curto |
| Orígenes (cadeia grega) | atribuição a Orígenes incerta; a *Selecta* tem atribuição de capítulo aproximada |

### 4.3 O que falhou ou não foi feito

- **augustinus.it fora do ar** (HTTP 503 em 20/10/2026, de novo): o texto de Agostinho veio do Corpus Corporum, que tem as colunas da PL e o grego em letras; a cópia do Wayback Machine existe, mas o grego vira imagem.
- Nada mais falhou tecnicamente: os dez textos do Corpus Corporum baixaram em segundos (sem a lentidão de 17–18/10), o khazarzar e o archive.org responderam, e o Wayback também.
- **Não baixados nem cortados** (ficam como pista em `_pistas-numeros.md` ou neste mapa): Jerônimo, Ep. 78 (as 42 mansões, PL 22, 698–724); Pedro Damião, *De quadragesima et XLII mansionibus*; Glosa Ordinária; Gregório Magno, *Moralia* etc.; Tomás, Belarmino, os Papas, a liturgia (ver as seções 5.4 e 6); Cirilo, *Comentário a João* e outros que citam Números; Teodoreto, *Interpretatio in Psalmos* (Sl 77, 94, 105) e *In Ezechielem* 20; Afraates; Dionísio Cartuxo; Boaventura.
- **Grego do OCR de Procópio** e **colunas da PG 80/44** (OCR do archive.org): não conferidos nos cortes.
- **Orígenes, *Homiliae in Numeros* na PG 12**: as colunas de Delarue não foram conferidas (só as marcas «Del.» das margens).

## 5. Tudo o que os catálogos por grupo dizem de Números

Esta seção reúne, em tabelas, o que `fontes/latinos.md`, `fontes/agostinho.md`, `fontes/gregos.md` e `fontes/modernos.md` dizem de Números (ou do Pentateuco em geral), de modo que as seções
dedicadas a Números nesses catálogos possam sair de lá. As seções sobre Salmos e sobre as cartas de Paulo ficam nos catálogos. Cada subseção diz de que seção do catálogo vem.

### 5.1 `fontes/latinos.md`

#### 5.1.1 Seção «4. Comentários latinos ao Pentateuco e a Números (primeiro uso: Nm 12, 2026-10-17)»

Ver `numeros/012/relatorio-latinos.md`. **Busca que funcionou**: as notas de Migne (`Num. XII`; no Jerônimo a PL usa algarismos, `Num. 12. 3`) e as palavras da Vulgata **Clementina** (os Padres leem
*mitissimus*, não o *humillimus* da Nova Vulgata). Para achar o capítulo dentro de um comentário, procurar o primeiro versículo e o título `(CAP. XII.)` que Migne põe nos títulos de capítulo.

| Obra | O que é | Onde |
|---|---|---|
| **Ruperto de Deutz**, *De Trinitate et operibus eius* (c. 1112–1117) | comentário de toda a Escritura em 42 livros; *In Numeros* em dois livros, capítulos curtos com título, versículo a versículo, sentido literal e depois alegórico. Original, vivo, cheio de observações humanas. **O melhor latino para Números** (e provavelmente para o Pentateuco) | PL 167 (texto **10873**, 5,7 MB; `grep -n "IN NUMEROS\|IN LEVITICUM\|IN DEUTERONOMIUM"` acha os livros) |
| **Rábano Mauro**, *Enarrationes in librum Numerorum* | compilação, com as fontes às vezes indicadas (*Ex Augustino*): Orígenes (Rufino), Agostinho (*Quaest. in Hept.*), Jerônimo (Ep. 78), Isidoro. Útil para ter Orígenes latino em texto; quase nada próprio. Também Gênesis, Êxodo, Levítico, Deuteronômio | PL 108 (Corpus Corporum 8898) |
| **Santo Isidoro**, *Quaestiones in Vetus Testamentum* | Gênesis a Macabeus, alegórico e breve, por capítulos; em Números segue as mansões de Nm 33 (de Jerônimo, Ep. 78) | PL 83, 207–424 |
| Isidoro, *Allegoriae* | uma frase por personagem; boa chave alegórica | PL 83, 97–130 |
| **pseudo-Beda**, *Quaestiones super …* | copiam Isidoro | PL 93 |
| **«Beda»**, *In Pentateuchum* | espúrio, breve, quase nada. Beda autêntico não comentou o Pentateuco além do Gênesis (*In principium Genesis*, não conferido) e do Tabernáculo (*De tabernaculo*, Ex 25–30) | PL 91, 189–394 |
| **Paterius**, *Liber testimoniorum* | excertos de Gregório Magno organizados por livro e capítulo da Bíblia; atalho para achar o que Gregório disse de um versículo (mas tem lacunas: em Números salta do cap. 11 ao 16) | PL 79 |
| **Hugo de São Vítor**, *Adnotationes in Pentateuchon* | notas literais, poucas em Números (só até o cap. 14 da obra) | PL 175, 29–86 |
| **São Jerônimo**, Ep. 78 a Fabíola, *De XLII mansionibus* | as 42 mansões de Nm 33, cada uma com o episódio ligado a ela (Haserot = Nm 12; Cades = Nm 20 etc.). Fonte de Isidoro, Rábano e da Glosa para Números | PL 22, 698–724 |
| **Glosa Ordinária** | não está no Corpus Corporum; para o Pentateuco é sobretudo Orígenes, Isidoro e Rábano | PL 113–114 (imagem) |

#### 5.1.2 Seção «5. Orígenes latino (Rufino e Jerônimo): as homilias sobre o Pentateuco e os históricos»

Primeiro uso: Nm 12, 2026-10-17 (`numeros/012/relatorio-origenes-agostinho.md`). Orígenes não é santo: citar como «Orígenes», sem título, e dizer que é a tradução de Rufino.

- **No Corpus Corporum só há** (autor 1049): homilias sobre o Cântico (7164), Isaías (7172), Jeremias e Ezequiel (7182, de Jerônimo), as 39 sobre Lucas (7192). **As homilias sobre Gn, Ex, Lv, Nm, Js, Jz, 1Rs (Sm) não estão** (são da PG 12, que o Corpus não tem).
- **Edição crítica de domínio público: Baehrens, GCS (Origenes Werke)**, no archive.org, com OCR (`_djvu.txt`) e imagens por página:

| Volume | Conteúdo | Identificador do archive.org |
|---|---|---|
| Bd. 6 (GCS 29, 1920) | homilias sobre **Gênesis, Êxodo, Levítico** | `origenes-werke.-bd-6-1920` |
| Bd. 7 (GCS 30, 1921) | homilias sobre **Números (28), Josué (26), Juízes (9)** | `origenes-werke.-bd-7-1921` (Nm hom. 7 = págs. 37–48) |
| Bd. 8 (GCS 33, 1925) | homilias sobre **1 Samuel, Cântico, Isaías, Jeremias, Ezequiel** e o Comentário ao Cântico | `GCS33` ou `origenes-werke.-bd.-8-1925` |

- Página impressa P = *leaf* P+36 no Bd. 7 (conferir em `..._page_numbers.json` nos outros); imagem: `https://archive.org/download/<id>/page/n<leaf>.jpg` (3542×5251, legível; recortar com PIL); link para o leitor: `https://archive.org/details/<id>/page/<P>/mode/1up`.
- O OCR mistura o aparato crítico, as referências («vgl.») e os números de linha e **perde linhas inteiras**: transcrever da imagem (um subagente fez as 12 páginas da hom. 7 em ~8 min). Achar uma homilia: `grep -n "HOMILIA VII\|in Numeros Homilia"` (os cabeçalhos de página).
- As margens dão as páginas de Delarue («Del.», = PG) e de Lommatzsch («Lomm.», t. 10 para Números); a coluna da PG 12 não sai daí: conferir no PDF da PG se for preciso.
- Rábano Mauro, *Enarrationes in librum Numerorum* (Corpus Corporum 8898, PL 108) copia Orígenes quase palavra por palavra: serve para conferir o latim de Rufino num trecho duvidoso.

#### 5.1.3 Seção «7. Aprendido em Nm 13, 2026-10-18» (`numeros/013/relatorio-latinos.md`)

- **O servidor do Corpus Corporum fica lento** (cada `navigate.php` leva 30–40 s quando há várias chamadas em paralelo); listar todas as obras de 30 autores levou mais de meia hora. Melhor: baixar direto pelo `idno` do texto os já conhecidos e, para o resto, listar as obras do autor (uma chamada por autor), escolher pelo nome e só então pedir os textos dessas obras. (Em 20/10/2026 respondeu em segundos.)
- Texto (`idno`) de obras novas, úteis para o Pentateuco e para o tema da terra prometida:

| Autor | Obra | Texto | PL |
|---|---|---|---|
| São Bruno de Segni (2171) | Expositio in Pentateuchum (21519) | **21403** (*In Numeros* começa na linha «INCIPIT EXPOSITIO IN NUMEROS») | 164 |
| Tertuliano (867) | Adversus Judaeos **62**; Adversus Marcionem **63** | | 2 |
| Lactâncio (902) | Divinae institutiones IV **6810**; Epitome **6814** | | 6 |
| Cipriano (878) | Testimonia **21445** | | 4 |
| Máximo de Turim (1102) | Homiliae **7652** (a Hom. 79 estava entre os sermões de Ambrósio) | | 57 |
| Beda (1397) | Homiliae **8509**; In Cantica **8455**; In Samuelem **8459**; «In Pentateuchum» (espúrio) **8461** | | 91–94 |
| Ricardo de São Vítor (2350) | De exterminatione mali **11536**; Benjamin major **11527** | | 196 |
| «Hugo de S. Victore?» (2229) | Posteriores excerptiones **11052** (= *Allegoriae in VT* e *in NT*, hoje de Ricardo, *Liber exceptionum*); Miscellanea **11093** | | 175–177 |
| Hugo de São Vítor (2230) | De sacramentis **11082** | | 176 |
| Honório de Autun (2211) | Speculum Ecclesiae **11000**; In Cantica **10988** | | 172 |
| São Pedro Damião (928) | De quadragesima et XLII mansionibus **10104**; De bono status religiosi **10076** | | 145 |
| São Bernardo (2268) | Sermones de diversis **11257**; In psalmum Qui habitat **11246** (e as outras obras, quase todas com `idno` entre 11189 e 11258) | | 183–184 |
| Ambrósio (958) | Expositio in Ps. 118 **6966**; De Joseph **21359**; De mysteriis **6971** | | 14–16 |
| Gregório (1165) | Concordia testimoniorum **8103**; In I Regum **21352** | | 79 |
| Euquério (1068) | Formulae spiritalis intelligentiae **7549** (dicionário de símbolos: «Botrus, Ecclesia, sive corpus Domini») | | 50 |

- **Cornélio a Lápide, *In Numeros***: t. II da ed. Vivès (archive.org `commentariainscr02lapi_0`): página impressa P = imagem `page/n<P+31>.jpg` (Nm 13 = pp. 255–261). O OCR (`_djvu.txt`) mistura as duas colunas; transcrever da imagem o trecho que entrar nos achados.
- **Corpus Thomisticum inteiro**: as 464 páginas de `iopera.html` (todos os links `c*`, `s*`, `q*`, `o*`) baixam em ~2 min com 10 conexões; a página é ISO-8859-1, e cada parágrafo tem `TITLE="Super Heb., cap. 3 l. 2"`. As citações vêm como «Num. XIII» ou «Num. 13».
- Busca que funcionou para um capítulo narrativo: as palavras raras da Vulgata Clementina do próprio capítulo (*in vecte*, *phalanga*, *botryo*, *praecoquae*, *compescens murmur*), não só as notas de Migne, que em muitas obras não marcam a citação.

#### 5.1.4 Seção «9. Aprendido em Nm 14, 2026-10-18» (`numeros/014/relatorio-latinos.md`)

- **Reaproveitar os downloads**: os scratchpads das conversas anteriores guardam 528 textos da PL já baixados (pastas `dl/`, `dl/a<autor>/`, `n12/a<autor>/`) e o Corpus Thomisticum inteiro (`ct/`). Um índice pelo cabeçalho de cada arquivo (`cc_idno: N, cc_id: ...`) dispensa o servidor lento.
- **As notas de Migne ficam no rodapé**: o `grep` em «Num. XIV» acha a nota, não o texto. Achar o marcador `[N]` correspondente antes da nota e mostrar o texto em volta dele.
- O texto baixado quebra linhas no meio das frases: normalizar os espaços antes de procurar uma frase.
- Ids novos úteis: **Ruperto** (2195) *In XII prophetas minores* **10877** (PL 168; *In Osee*, *In Michaeam*, *In Zachariam*… com títulos «IN OSEE PROPHETAM COMMENTARIORUM LIBER...»), *In Cantica* **10876**, *In Job* 10878; **Gregório** *Expositio in VII psalmos poenitentiales* (espúria) **8104**; **Jerônimo** *Dialogus adversus Pelagianos* **7158**, *In Hiezechielem* **21347**; **Bernardo** *De consideratione* **21366**, *Sententiae* **11256**; **Leão Magno** *Sermones* **7631**, *Epistolae* **7630**.
- Temas transversais e onde estão: os pecados dos pais nos filhos (Êx 20,5; 34,7): Gregório, *Moralia* XV, 51, 57; Tomás, I-II q. 87 a. 8; Jerônimo, Ep. 130, 8 (pensamentos e obras); Bruno de Segni, *In Num.* 14. Moisés intercessor: Gregório, *Moralia* IX, 11 e 24; XX, 5, 14; Ruperto, *In Mich.* I e *In Cant.* VI. Os quarenta anos: Ruperto, *In Osee* V; Pedro Damião, *Collectanea* (sobre Dt 25); Jerônimo, *In Hiez.* IX (Ez 29,11).
- O comentário de Tomás a **1 Coríntios 7,10–10,33 não existe** (lacuna do texto autêntico).

#### 5.1.5 Linhas da seção «0» (Corpus Corporum) que servem a Números

A API do Corpus Corporum (texto puro da PL, 5277 textos, 1528 autores; só domínio público) e as colunas: ver `fontes/latinos.md` § 0; os textos de Números usados aqui:

| Autor (idno) | Obra | Texto | PL |
|---|---|---|---|
| Ruperto de Deutz (2195) | De Trinitate et operibus ejus | **10873** | 167 |
| Rábano Mauro (1518) | Enarrationes in librum Numerorum (3875) **8898**; Comm. in Genesim **8885**; Expositiones in Leviticum (3877) | | 107–108 |
| Santo Isidoro (1318) | Quaestiones in Vetus Testamentum (21546) **21433**; Allegoriae (3196) **8202**; De ortu et obitu Patrum (3203) **8209**; Sententiae (3212) **8218** | | 83 |
| pseudo-Beda (1395) | Quaestiones super Genesim/Exodum/Leviticum/Numeros (3467: **8484**)/Deuteronomium/Jesu Nave/Regum | | 93 |
| «Beda» (1397) | Commentarii in Pentateuchum (3444) **8461** (espúrio) | | 91 |
| Paterius (1280) | Expositio Veteris ac Novi Testamenti (3103) **8106**: excertos de Gregório por livro | | 79 |
| Hugo de São Vítor (2230) | Adnotationes in Pentateuchon **11054** | | 175 |
| São Jerônimo (879) | Epistolae (576) **7132** (Ep. 78 = De XLII mansionibus); Adversus Iovinianum **7149**; In Sophoniam **7180**; Quaest. hebr. in Gen. **7160**; In Isaiam **7170** | | 22–25 |
| São Gregório Magno (1165) | Homiliae in Evangelia **8053**; Moralia I–XVI **21427**; Moralia XVII–XXXV **8054**; Hom. in Ezechielem **21412**; Regula pastoralis **21435**; Dialogi **8063**; Epistolae **8064**; In Cant. **8105**; In I Regum **21352** (hoje de Pedro de Cava) | | 75–79 |
| São Pedro Damião (928) | Epistolae **10045**; Collectanea in VT (de seu discípulo João) **10066** | | 144–145 |
| Santo Ambrósio (958) | Hexaemeron **6958**; De Spiritu Sancto **6967**; De fide **21369**; De officiis **6974**; Epist. classis I **21400**; classis II **6979**; Apologia David **6945**; In Lucam **6965**; De Noe **21361**; De institutione virginis **21372**; De virginibus **21380** | | 14–16 |
| João Cassiano (1063) | Collationes **7530**; De institutis **7531** | | 49 |
| Santo Hilário (927) | Tractatus super Psalmos **21450**; De Trinitate **6871** | | 9–10 |
| São Bernardo (2268) | 72 textos; Sermones in Cantica **11258** | | 182–185 |
| São Bruno de Segni (2171) | Expositio in Psalmos **10806** (e o Pentateuco, **21403**) | | 164 |

### 5.2 `fontes/agostinho.md`

#### 5.2.1 Seção «3. Pentateuco e Antigo Testamento (primeiro uso: Nm 12, 2026-10-17)»

- **O Corpus Corporum tem as 140 obras dele no PL, inclusive as *Enarrationes* (obra 771, texto 7329, e «[2]» 21501/21385) e os sermões** (775–784, 2519, 2528). A observação do catálogo («não tem as *Enarrationes*») vale só para a **busca de frase**, que não as indexa; baixando os arquivos, tudo se acha com `grep`. Autor `900`; script `ccall.py` (baixa todas as obras de um autor, 6 em paralelo, ~10 min) descrito em `numeros/012/relatorio-origenes-agostinho.md` e em `latinos.md`. Achar um versículo: `grep -o -E "Num(er)?\.? ?XII\b[^;)]{0,15}"` nas notas (são poucas: Migne anota pouco nas obras de Agostinho), depois frases-chave da Vetus Latina dele.
- Obras (work → texto) úteis para o AT:

| Obra | work → texto | Para Números |
|---|---|---|
| *Quaestiones in Heptateuchum* | 754 → **7312** (PL 34, 547–824; questões curtas, quase sempre literais, livro a livro: I Gn, II Ex, III Lv, IV Nm a partir da linha «LIBER QUARTUS», V Dt, VI Js, VII Jz; cada questão começa com «[Ib. XII, 1.]») | o livro IV (65 questões) |
| *Quaestiones in Heptateuchum* (CSEL 28/1, Zycha 1895, domínio público) | texto **15028** do Corpus (o mesmo arquivo traz as *Locutiones*), com página CSEL | idem |
| *Locutiones in Heptateuchum* | 753 → **7311** (só gramática, mas mostra a Vetus Latina dele) | o livro IV |
| *De Genesi ad litteram* | 744 → **7302** (livro XII = as visões, Moisés e Paulo) | Nm 12 |
| Cartas | 742 → **7300** (Carta 147 *De videndo Deo* nas linhas ~29000–30500) | Nm 12 |
| *De Trinitate* | 2456 → **7441** (II–III: as teofanias do AT) | Nm 12 |
| *Contra Faustum* | 2447 → **7432** (defesa dos patriarcas e de Moisés contra os maniqueus; nada sobre Nm 12) | |
| *De civitate Dei* | 21481 (e 21364) | |
| *Contra Gaudentium* | 2473 → 7458 | a mansidão de Moisés (I, 19,20) |
| *In Ioannis ev.* | 765 → 7323 | |

- **Pseudo-Agostinho** (autor 1024, «Auctor incertus (Augustinus Hipponensis?)»): *Sermones supposititii de Scripturis* **7338** (PL 39; muitos de Cesário de Arles: conferir), *De mirabilibus sacrae Scripturae* **7315** (Agostinho Hibérnico, 655; questões literais sobre todo o AT), *Sermones ad fratres in eremo* **7388** (autor 1028?, medieval). Citar com a autoria certa.
- Pistas temáticas: os etíopes = as nações (En. in Ps. 71,12; 73,16; 67,40 de memória); a visão de Deus por Moisés (*Gen. ad litt.* XII, 26–28; Ep. 147, 13; *De Trin.* II, 16–17; *Contra Maximinum* I, 15); a mansidão de Moisés (*Contra Gaudentium* I, 19,20).

#### 5.2.2 Linhas de outras seções de `agostinho.md` que falam de Números

- **Seção «4. Salmo 33 da Vulgata», bullet «Nm 13 (2026-10-17)»**: as *Enarrationes* no Corpus são **dois textos**: 7329 (Sl 1–79, PL 36) e **21385** (Sl 80–150, PL 37); *De civitate Dei* = texto **21364**. Pistas temáticas: o nome de Josué = Jesus (Sermão 352, 4; *Contra Faustum* XVI, 19–20 e XII, 31; *Quaest. in Hept.* II, 103); Cristo, o cacho pendurado no madeiro (En. in Ps. 8, 2; *Contra Faustum* XII, 31 e 42; alusões em En. in Ps. 55, 4; 83, 1; Sermões 191, 1 e 267); a terra desejável desprezada por falta de fé (En. in Ps. 105, 22). Ver `numeros/013/relatorio-origenes-agostinho.md`. Sermões fora das coleções dos Maurinos: «Sermones 1» (obra 2519 → texto 7504) e «Sermones 2» (2528 → **7513**, os quatro de A. Mai, autenticidade discutida; o III, sobre Caná, traz os dois carregadores do cacho de Nm 13). O `ccall` de todas as obras travou duas vezes depois da obra 2458: baixar as que interessam pelo número do texto.
- **Seção «1.1»** (augustinus.it) dá o padrão dos arquivos da Nuova Biblioteca Agostiniana, que vale para as obras: `latino/confessioni/`, `latino/cdd/` (*De civitate Dei*), `latino/trinita/`, `latino/genesi_lettera/` (*De Genesi ad litteram*), `latino/dottrina_cristiana/`, `latino/lettere/`, `latino/commento_vsg/` (*In Iohannis evangelium tractatus*), `latino/discorsi/` (sermões, arquivo = ordem do índice `sommario.htm`, não o número do sermão). Do relatório de Nm 14: `questioni_ettateuco/quest_ettateuco_N_libro.htm`, `locuzioni_ettateuco/locuz_ettateuco_N_libro.htm`, `contro_fausto/libro_NN_testo.htm`, `enchiridion/enchiridion_libro.htm`, `contro_giuliano/contro_giuliano_N_libro.htm`, `incompiuta_giuliano/incompiuta_giuliano_N_libro.htm`, `contro_adimanto/contro_adimanto_libro.htm`, `commento_lsg/omelia_NN_testo.htm`, `commento_vsg/omelia_NNN_testo.htm`, Sermão 252 = `discorsi/discorso_349_testo.htm` (nomes achados pelo índice CDX do Internet Archive).
- Quando o augustinus.it cai, a cópia do Wayback: `http://web.archive.org/web/2016id_/http://www.augustinus.it/latino/…` (o `id_` devolve o HTML original, em windows-1252).

### 5.3 `fontes/gregos.md`

#### 5.3.1 Seção «Comentários ao Pentateuco e ao Octateuco (primeiro uso: Nm 12, 2026-10-17, `../numeros/012/relatorio-gregos.md`)»

| Autor | Obra | PG | Cobre | Onde | Como achar |
|---|---|---|---|---|---|
| São Cirilo de Alexandria | *Glaphyra in Pentateuchum* | 69, 9–678 | episódios escolhidos de Gn, Ex, Lv, Nm, Dt, lidos como figura de Cristo e da Igreja (Nm: 589–641) | khazarzar `Cyril of Alexandria_PG 68-77/Glaphyra in Pentateuchum.pdf` (texto da PG) | títulos «ΓΛΑΦΥΡΩΝ ΕΙΣ ΤΟΥΣ ΑΡΙΘΜΟΥΣ», depois «Περὶ …»; seções «βʹ.», «γʹ.» |
| São Cirilo | *De adoratione et cultu in spiritu et veritate* (17 livros, diálogo com Paládio) | 68, 133–1125 | a Lei de Moisés por temas (lepra, sacrifícios, sacerdócio) | khazarzar, mesmo diretório | «ΛΟΓΟΣ …»; falas «{ΚΥΡ.}», «{ΠΑΛΛ.}» |
| Teodoreto de Ciro | *Quaestiones in Octateuchum* | 80, 77–528 | Gn a Rt, por perguntas (Nm: 349–400) | khazarzar `Theodoretus of Cyrrhus_PG 80-84/Quaestiones in Octateuchum.pdf`: segue a ed. Fernández Marcos–Sáenz-Badillos (1979), **sem colunas da PG**; números soltos no texto são linhas da edição | perguntas «XXII», «XXIII»; colunas da PG no OCR do archive.org `bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1860_80` |
| Procópio de Gaza | *Commentarii in Octateuchum* | 87/1, 21–1080 | Gn a Rt; cadeia que copia Cirilo, Teodoreto, Orígenes | **não está no khazarzar** (só as cartas e declamações); PG 87/1 no archive.org `patrologiaecurs267unkngoog` (Nm: 793–897). Para Ex–Rt a PG só tem o latim de Clauser, com escólios gregos | buscar o latim da Vulgata do versículo |
| Orígenes | *Selecta* e *Adnotationes* (escólios de cadeia) em Gn, Ex, Lv, Nm, Dt | 12; 17 | glosas curtas | khazarzar `Origenes_PG 11-17/Adnotationes in Numeros.pdf` etc. | «ΚΕΦ. ΙΒʹ. Στίχ. …» = capítulo e versículo. As *Homilias sobre Números* só existem no latim de Rufino (PG 12; ver latinos) |
| São Gregório de Nissa | *Vida de Moisés* | 44, 297–430 | a vida inteira de Moisés: I = história, II = contemplação | khazarzar `Gregory of Nyssa_PG 44-46/De vita Mosis.pdf`: segue a GNO VII/1 (Musurillo), «[PG 2, 256]» = livro II, § 256 | colunas da PG no OCR `patrologiaecursu44mignuoft` (latim legível) |
| Santo Ireneu | *Contra as heresias* | 7 | tipologia de Moisés: IV, 20 (Massuet) = IV, 34 (Harvey) | ed. Harvey vol. 2: `sanctiirenaeiep00harvgoog` (o vol. 1 é `sanctiirenaeiep01harvgoog`); OCR legível; à margem, as referências bíblicas | buscar o latim do versículo |

- As colunas de início e fim de cada obra (e das partes sobre Nm) nesta tabela são aproximadas; conferidas só as de Nm 12 (Cirilo 69, 589–605; Teodoreto 80, 373–376; Procópio 87/1, 823–828; Nissa 44, c. 317 e 413–416).
- **Crisóstomo**: não comentou Números nem Êxodo (só *Gênesis*, homilias e sermões). Para o Pentateuco, buscar nas homilias: com todos os ~400 PDFs baixados, uma busca sem acentos acha as citações em minutos. Cuidado: na pasta do Crisóstomo há espúrios (*In Ps. 100*, *Synopsis scripturae*, *Contra theatra*, *Eclogae*, que repetem trechos autênticos) e obras em edição moderna (*Catecheses ad illuminandos*, Wenger; *De inani gloria*, Malingrey: só citação curta).
- **Nomes repetidos**: Nazianzeno e Nissa têm cada um um `Epistulae.pdf`; ao baixar as duas pastas para o mesmo diretório, um sobrescreve o outro. O de Nazianzeno segue Gallay («[PG 77, 8]» = carta 77, § 8).
- **Basílio**: o `Asceticon magnum` traz as *Regras longas* e as *breves* (perguntas «ΕΡΩΤΗΣΙΣ ΚΖʹ»); o *Hexaémeron* segue a ed. Giet (SC 26), com «[PG 1, 1]» = homilia 1, § 1.
- Não estão no khazarzar: Teodoreto, *Interpretatio in xiv epistulas Pauli* (PG 82); Teofilato (PG 123–126); Ecumênio sobre as cartas (PG 118–119 tem só o Apocalipse em edição moderna). Efrém: nada em grego útil.

#### 5.3.2 Seção «Acréscimos de Nm 13 (2026-10-17, `../numeros/013/relatorio-gregos.md`)»

| Autor | Obra | Onde | Nota |
|---|---|---|---|
| Epístola de Barnabé | 12, 8–9 | khazarzar `Barnabas_PG 02/Barnabae epistula.pdf` | marcadores «[PG 12, 8]» = capítulo e versículo |
| São Justino | *Diálogo com Trifão* | khazarzar `Iustinus_PG 06/Dialogus cum Tryphone.pdf` | sem colunas nem capítulos; o OCR mistura letras latinas («Aὐσῆς») e põe «·» por «ῥ» |
| Eusébio | *Demonstratio evangelica*; *Historia ecclesiastica*; *Eclogae propheticae*; *Onomasticon* | khazarzar `Eusebius Caesariensis_PG 19-24/`: as *Eclogae* estão no PDF «Generalis elementaria introductio» (ed. Gaisford 1842; «ΙΑʹ» = I, 11); o *Onomasticon* segue Klostermann (1904), com a referência bíblica de cada verbete | DE e HE: «[PG 4, 17] .3» = livro, capítulo, § (ed. GCS), não coluna |
| São Cirilo de Alexandria | *De adoratione* V («Sobre a coragem em Cristo») | PG 68, 372–376 | Nm 13–14 lido com Dt 20,8: a pusilanimidade que contagia |
| São Gregório de Nissa | *Homilias sobre o Cântico* 3 (Ct 1,14) | GNO VI, 98–99 | o «verdadeiro cacho» nas varas de madeira (Nm 13,23) |
| Santo Anfilóquio de Icônio | *In Zacchaeum* | khazarzar `Amphilochius Iconiensis_PG 39/` (ed. Datema, CCSG 3, 1978: citação curta) | Raab e Zaqueu, Josué e Jesus |
| Procópio de Gaza | *In Numeros* | OCR da PG 87/1 (`patrologiaecurs267unkngoog`), Nm 13: c. 829–830 | só latim; compila Cirilo e Nissa |

- Busca de «ὡσεὶ ἀκρίδες»: quase todas as ocorrências são de Is 40,22, não de Nm 13,33. O padrão «Ὡσηέ» acha sobretudo o profeta Oseias: para Josué, buscar «Αὐσῆ».

#### 5.3.3 Seção «Acréscimos de Nm 14 (2026-10-18, `../numeros/014/relatorio-gregos.md`)»

| Autor | Obra | Onde | Nota |
|---|---|---|---|
| Procópio de Gaza | *In Numeros*, **escólios gregos** | PG 87/1, 829–836 (Nm 14) | Para alguns capítulos a PG imprime, ao lado do latim de Clauser, escólios gregos da cadeia. O OCR `patrologiae_cursus_completus_gr_vol_087_1` (archive.org) lê bem o grego e mal o latim; o `patrologiaecurs267unkngoog`, o contrário: usar os dois juntos |
| Santo Efrém (atribuído) | *In Numeros*, ed. romana | *Opera Syriaca et Latina* I (Roma 1737), p. 250 ss.; archive.org `assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-1` | Glosas de cadeia siríaca com tradução latina; o OCR do latim é legível, o do siríaco não. Nm 13–14: p. 258–259. O vol. I cobre também Gn, Ex, Lv, Dt, Js, Jz e Reis |
| Teodoreto | *Interpretatio in Psalmos* | khazarzar (PDF com colunas da PG) | Os Sl 77, 94 e 105 (LXX) relembram o deserto: procurar ali os episódios do Êxodo e de Números |
| Cirilo de Alexandria | *Commentarii in Joannem* | khazarzar (ed. Pusey: «[PG 2, 140]» = vol. II, p. 140) | Digressões longas sobre o AT: Ex 34,6–7 e Nm 14,17–19 em VI (Jo 9,2); a arca e Dt 1,41–44 em IV (Jo 6). Colunas da PG 73 pelo OCR `bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1859_73` |

- Não estão no khazarzar: Isidoro de Pelúsio (PG 78; latim no archive.org, OCR fraco), Diádoco (PG 65), João Clímaco (PG 88).

#### 5.3.4 Linhas de outras seções de `gregos.md` que servem a Números

| Item | O que diz |
|---|---|
| «Onde fica o texto» | **khazarzar** (espelho da «Ψηφιακή Πατρολογία», Univ. do Egeu, 2006): `https://khazarzar.skeptik.net/pgm/PG_Migne/<Autor>_PG <vols>/<Obra>.pdf` (espaços como `%20`; o índice de cada pasta lista as obras; os PDFs trazem as colunas da PG como «29.325»). Exceções que seguem edições modernas e não têm colunas da PG: Gregório de Nissa (GNO), João Damasceno (Kotter), Clemente (Stählin), Cirilo de Jerusalém (Reischl–Rupp; «11.16» = Catequese 11, 16), Dídimo e Apolinário (Mühlenberg; Tura), Teófilo. Converter e buscar: `ferramentas/gregos-limpar.py` e `gregos-buscar.py`. Conferir colunas e seções: OCR da PG no Internet Archive (`title:(patrologiae cursus completus) AND volume:<n>`); o documentacatholicaomnia.eu tem a PG só em imagem. First1KGreek e Perseus não têm os comentários |
| Cuidados | as **cadeias** misturam autores (o mesmo trecho aparece sob vários nomes; citar o original); traduções antigas de domínio público dos comentários gregos praticamente não existem; o latim da PG (ao lado do grego, no OCR do archive.org) serve para conferir |
| Textos já convertidos (acréscimos do Sl 35) | os scratchpads de 17–18/10 no notebook (pasta temporária do sistema; podem ter sido limpos) guardam `txtall/`, `g12/txt/`, `g13/txt/` com ~2 000 textos já convertidos; busca rápida em todo o corpus com `str.translate` (~1 min); Eutímio Zigabeno (PG 128, OCR `patrologiaecurs261unkngoog`); Eusébio PG 23 pode trazer fragmentos de Dídimo; Teodoreto numera diferente quando divide versículos |
| Espúrios que aparecem nas buscas | Pseudo-Atanásio, *Homilia in sanctos patres et prophetas*; Pseudo-Crisóstomo, *In illud Ignem veni mittere*, *De circo*, *De paenitentia…*; *Testimonia* atribuídos a Epifânio — não usar |
| Teodoro de Mopsuéstia, Diodoro | não estão no khazarzar; Teodoro foi condenado em 553: não entram no site |

### 5.4 `fontes/modernos.md`

#### 5.4.1 Seção «7. São Tomás em toda a obra (fora dos Salmos) — primeiro uso: Nm 12, 2026-10-17»

Para achar **todas** as vezes que Tomás cita um capítulo:

| Passo | Como |
|---|---|
| Baixar | do Corpus Thomisticum (`https://www.corpusthomisticum.org/<pág>.html`) as ~290 páginas da *Suma* (`sth1001`…`sth4090`; I = `sth1`, I-II = `sth2`, II-II = `sth3`, III = `sth4`), *Contra gentiles* (`scg*`), *De veritate* (`qdv*`), *Sentenças* (`snp*`) e os comentários bíblicos (`cio` Jó, `cps` Salmos, `cis` Isaías, `cph` Jeremias, `cmt` Catena/Mt, `cih` João, `cro` Rm, `c1c`/`c2c` Coríntios, `cgl` Gl, `cep` Ef, `ct1`/`ct2` Timóteo, `che` Hebreus…). A lista de páginas sai de `https://www.corpusthomisticum.org/iopera.html` (links `href=…org/<pág>.html`); 16 downloads em paralelo levam ~45 s (53 MB). Depois de Nm 13 baixaram-se as 464 (depois 469) páginas inteiras, em ~2 min com 10 conexões |
| Converter e buscar | de ISO-8859-1; a referência como Tomás a escreve: `Num. XII`, `Num. 12`, `Numer. XII` (e uma frase-chave do versículo; para capítulos narrativos, as palavras raras da Vulgata Clementina) |
| Ler | cada parágrafo é `<P TITLE="I q. 12 a. 11 arg. 2">` com o número `[28763]`; scripts `win.py` (janela em volta do achado) e `para.py` (parágrafo inteiro), no scratchpad da conversa; refazer é rápido |
| Páginas da *Suma* usadas | `sth1003` (I q. 3–14), `sth3061` (II-II q. 61–78: detração, murmuração), `sth3155` (q. 155–170), `sth3171` (q. 171–178: profecia e arrebatamento), `sth4002` (III q. 2–15) |

Tomás não comentou Números; só citações. Achados de Nm 12 (28 passagens, só os vv. 6–8), Nm 13–15: ver `numeros/012/relatorio-modernos.md` e os relatórios latinos (`Super Heb.` 3, l. 2 etc.).

#### 5.4.2 Seção «8. Cornélio a Lápide, *Commentaria in Scripturam Sacram* (séc. XVII)»

- Jesuíta, não canonizado: citar como «escritor». Comenta **toda a Bíblia, menos Jó e Salmos**, versículo a versículo, juntando os Padres, os medievais e os exegetas (Tostado/«Abulensis», Lira, Ruperto), com longas aplicações morais cheias de exemplos. Domínio público.
- Edição usada: Vivès, Paris, 1866–1868, ed. Augustin Crampon (21 vol. + suplementos). No archive.org, série `commentariainscrNNlapi` (com variantes `_0`, `_1`: são exemplares/edições diferentes; conferir o título no começo do `_djvu.txt`). **Confirmado**: `commentariainscr02lapi_0` = t. II, Levítico, Números, Deuteronômio (Nm 12 nas pp. 251–255, linhas 39515–40326 do OCR). Atenção: `commentariainscr02lapi` é **outra** edição (Lyon, Pelagaud), t. II = Josué a Macabeus.
- Outras séries: `commentariiinsac01lapi`…`09lapi` (1840), `commentariainsac07lapi`…`10lapi` (Nápoles? 1854, «Editio Xysto Riario Sfortiae dicata»), e volumes avulsos do séc. XVII (`bub_gb_*`). Busca: `https://archive.org/advancedsearch.php?q=creator%3A%28lapide%29&fl%5B%5D=identifier&fl%5B%5D=title&rows=100&output=json`.
- Achar um capítulo no OCR: `grep -n "CAPUT DUODECIMUM\|IN NUMEROS"` (os títulos dos capítulos vêm por extenso). OCR bom, mas Æ sai «JE»/«ZE», as notas da margem entram no meio do texto, e os números de página se estropiam: conferir na imagem.
- Páginas de Números (relatórios): Nm 12 = pp. 251–255; Nm 13 = pp. 255–261; Nm 14 = pp. 261–268 (imagens 263 e 266 conferidas); Nm 15 = pp. 269–273 (imagens 271 e 272); Nm 16 começa em 273. Página P = imagem `page/n<P+31>.jpg`.
- Achado deste levantamento: cada capítulo começa com «CAPUT … / SYNOPSIS CAPITIS» (o OCR estraga o título do cap. XXIX), e o cap. XVI vai até o v. 50 da Vulgata (o NV 17 começa em «37. TOLLAT THURIBULA»).

#### 5.4.3 Seção «9. Catecismo: busca em todos os arquivos»

O índice `prima-pagina-cic_po.html` lista 34 arquivos; baixar todos e procurar «Nm 12» (sigla portuguesa) dá a lista completa em segundos. Os arquivos são ISO-8859-1. Para Nm 12: só §§ 2576–2577.
Do relatório de Nm 13: em todo o Catecismo, Números só aparece nos capítulos **1, 7, 11, 12, 21, 24 e 28**; os §§ 1222 e 1334 falam da terra prometida como imagem da vida eterna e do pão como fruto dela, sem Nm 13. Os §§ 2574–2577 (a oração de Moisés) citam Ex 32–34 e Nm 12, não Nm 14; o § 2577 cita Ex 34,6.

#### 5.4.4 Seção «10. Liturgia: dias de semana e o Missal antigo»

- Leituras dos **dias de semana** (Lecionário de 1981, ciclo de dois anos: ano I = ímpar, ano II = par): não há quadro único conferido ainda; as páginas do dia (Franciscan Media, catholicreadings.org, liturgia.silvestrini.org com um epub por dia, ex. `…/epubs/2021-08-03.epub`) dão leitura e salmo. Nm 12,1-13: terça-feira da 18ª semana, ano I.
- **Missal antigo**: `gh api -X GET search/code -f q='"!Num" repo:DivinumOfficium/divinum-officium path:web/www/missa/Latin'` lista todas as perícopes de Números (só Nm 20, sexta da 3ª semana da Quaresma). Para o Breviário, o mesmo com `path:web/www/horas/Latin` (busca por «Num 12» deu só falsos positivos).
- **Universalis**: bloqueia `curl` e cobra pelo Ofício das Leituras; para ele, usar outro breviário.

#### 5.4.5 Seção «11. Achados novos de Nm 13 (2026-10-17)»

| Item | Onde e como |
|---|---|
| **Francisco de Sales, índice escriturístico** | o t. XXVII da edição de Annecy (Table analytique), `https://www.donboscosanto.eu/francesco_di_sales/27-Oeuvres%20de%20S.%20Francois%20de%20Sales-Tome%20XXVII-Table%20analytique-web.pdf`, tem um **Index scripturaire** com todas as citações bíblicas das *Œuvres* (tomo e página, versículos na numeração da Vulgata). Baixar, `pdftotext`, procurar o livro (ex.: «NOMBRES»): dá os lugares em segundos, inclusive nas cartas (t. XI–XXI), que a busca de palavras não cobre. Os tomos com «-web» no nome são os leves |
| **Clerus (Biblia Clerus)** | o índice de cada livro é navegável sem busca: `http://www.clerus.org/bibliaclerusonline/en/65g.htm` → livro (Números = `wu.htm`) → capítulo (`gpg.htm#rk` para Nm 13) → no fim de cada perícope, o link das citações (ex.: `9abv11m.htm` = Nm 13,1-24). Mostra Padres, Magistério, Lecionário e Antônio de Pádua |
| **Cantus Index, busca de texto** | `https://cantusindex.org/json-text/<palavra>` devolve, em JSON (com BOM: ler com `utf-8-sig`), o texto inteiro de antífonas, responsórios, hinos e **sequências** (inclusive as do *Analecta Hymnica*, ids `ah<vol><nº>`) que contêm a palavra. Achou três sequências com o cacho de Escol («botrum», «botrus», «vecte», «bajulus»). A página `https://cantusindex.org/id/<id>` abre a peça |
| **Iconografia tipológica** | Warburg Institute Iconographic Database (`https://iconographic.warburg.sas.ac.uk/`), com as inscrições do altar de Verdun (Klosterneuburg, 1181) e as cenas do *Speculum humanae salvationis*, classificadas por versículo |
| **Liturgia das Horas, ciclo de um ano** | índice bíblico do Ofício das Leituras por Felix Just, `https://catholic-resources.org/LoH/OfficeOfReadings-Biblical-Index.html` (livro → dia e página do volume americano). Números na Quaresma: Nm 11,4-6.10-30; Nm 12,16–13,3.17-33 (quinta da 4ª semana); Nm 14,1-25 (sexta da 4ª semana); Nm 20,1-13; 21,4-9 (dias dos outros a conferir no índice) |
| **Bloqueios** | bible.usccb.org (desafio anti-robô) e escriva.org (403) não abrem por `curl`; para as leituras do dia, usar ewtn.com/daily-readings/AAAA-MM-DD ou ucatholic.com |
| **Bossuet** | *Œuvres complètes* (Guérin, 1885) no archive.org, `oeuvrescompl01boss`…`oeuvrescomplt10boss` (OCR em `…_djvu.txt`); a lista sai de `https://archive.org/advancedsearch.php?q=creator%3A%28Bossuet%29+AND+title%3A%28oeuvres%29&fl%5B%5D=identifier&rows=300&output=json` |

#### 5.4.6 Seção «13. Achados novos de Nm 14 (2026-10-18)»

| Item | Onde e como |
|---|---|
| **Belarmino, *Opera omnia*** | ed. Vivès, 1870–1874, 12 t., no archive.org, com OCR: `operaomnia01bell_0`, `02bell_0`, `03bell_0`, `operaomnia04bell`, `05bell`, `06bell_0`, `07bell` … `12bell` (`<id>_djvu.txt`). t. III = *De Ecclesia militante / purgatorio*; t. IV = sacramentos (*De Eucharistia*, *De Poenitentia*); t. VI = *De gratia et libero arbitrio*; t. X–XI = ***Explanatio in Psalmos*** (comentário de todos os salmos, numeração da Vulgata); t. VII traz defesa de Belarmino por outro autor. Busca: `Num. xiv`, `Numer. XIV`, `Num. 14` (o OCR põe as referências em romanos minúsculos). Os cabeçalhos de capítulo vêm como «CAPUT XI.», «LIBER IV.» e o título da obra em maiúsculas espaçadas («DE P (ENITENTIA», «UBER QUARTUS»): achar com `grep -E` e espaços múltiplos |
| **Varredura completa dos Papas** (Francisco, Bento XVI, João Paulo II, Leão XIV), em italiano | os índices anuais `https://www.vatican.va/content/<papa>/it/<homilies|audiences|angelus|cotidie>/<AAAA>.index.html` listam todos os documentos do ano (links `href="/content/<papa>/it/<tipo>/<AAAA>/documents/….html"`). Baixar com `xargs -P 24` (≈4.000 documentos em ~5 min) e procurar «Nm 14», «Numeri 14», nomes e frases. Francisco: 2.584 documentos; Bento XVI + João Paulo II (sem Angelus): 4.169; Leão XIV: 352 (inclui exortações, encíclicas e mensagens). Para outro capítulo, refazer é rápido (os 7.105 documentos juntados num só arquivo de texto, ~60 MB, buscam-se em segundos) |
| **Clerus**, índice de Números | os capítulos estão em arquivos sequenciais, `…/en/gpg.htm` (RSV, cap. 7 a 13), `…/en/gph.htm` (cap. 14 a 20…); os links das citações têm `title="Nb 14,1-12"` etc. |
| **Lecionário da CNBB** | a Canção Nova guarda cada dia litúrgico em `https://liturgia.cancaonova.com/pb/liturgia/<semana>-<dia>[-N]/` (ex.: `18a-semana-tempo-comum-quarta-feira-5`); os sufixos `-1`…`-7` são anos diferentes (ano I/II): provar todos e procurar a referência. A *Palavra do dia* do Vatican News (`https://www.vaticannews.va/pt/palavra-do-dia/AAAA/MM/DD.html`) traz a 1ª leitura e o evangelho (sem o salmo). Texto da CNBB com direito autoral: guardar só referência, nomes e citação curta |
| **Lecionário, índice por livro** (Felix Just) | `https://catholic-resources.org/Lectionary/Index-Pentateuch.htm` (e `Index-Deuteronomistic-History.htm`, `Index-Deuterocanonicals.htm`, `Index-Sundays.htm`, `Index-Weekdays.htm`): todas as perícopes da Missa de cada livro, com o número do OLM |
| **Santo Afonso** | as páginas `_FA<c>.HTM` da concordância têm os links na forma `<a href=…>palavra</a>` com a frequência antes; para ver o contexto, abrir a página da palavra e seguir o link da linha (o rótulo da obra vem deslocado). Achados de Nm 14: *Apparecchio alla morte* XVIII, 1 (`_P3J.HTM`) e *Sermoni compendiati* XV (`_P31I.HTM`) |
| **Francisco de Sales** | o Index scripturaire (t. XXVII) já citado deu todos os lugares de Nm 14; as cartas a Santa Joana de Chantal de 1605 estão no t. XIII |
| **Missal antigo, textos inteiros** | `web/www/missa/Latin/Tempora/Quad6-5.txt` (Sexta-feira Santa, Improperios) e `web/www/horas/Latin/Psalterium/Invitatorium.txt` (Sl 94 do invitatório) no repositório do Divinum Officium (`https://raw.githubusercontent.com/DivinumOfficium/divinum-officium/master/…`) |

#### 5.4.7 Linhas de outras seções de `modernos.md` que serviram a Números

| Seção | O que serve a Números |
|---|---|
| 1. Santo Afonso | a concordância do IntraText (`https://www.intratext.com/IXT/ITASA0000/_FA.HTM`, letra → palavra rara → página) cobre a Opera omnia italiana inteira: buscar uma palavra latina rara do versículo mostra onde ele usa o versículo; fórmula da página da letra: `_FA<c>.HTM` com `c` = base 36 de (2 + posição da letra, A = 0): A=2, B=3 … I=A, L=D, M=E, P=H, R=J, S=K, T=L, V=N |
| 3 e 4. Catecismo e Magistério | índice de citações bíblicas (inglês, IntraText do Vaticano: `https://www.vatican.va/archive/ENG0015/_INDEX.HTM`); página do **Clerus** por versículo; texto português oficial em `https://www.vatican.va/archive/cathechism_po/index_new/<arquivo>`; varredura rápida do italiano de vatican.va por «Sal <n>»; para Números, «Nm 14», «Numeri 14» |
| 5. Liturgia | Divinum Officium (`https://github.com/DivinumOfficium/divinum-officium`, `web/www/missa/Latin/…`, `web/www/horas/Latin/…`; referência na linha `!Ps 32:5-6`; buscar palavra **acentuada**); Lecionário de 1981 (`https://es.catholic-resources.org/Lectionary/1970USL-Sundays.htm`, `1998USL-Solemnities.htm`); Liturgia das Horas (Universalis, GregoBase, Cantus Index) |
| 6. Santos modernos | Newman (`http://www.newmanreader.org`; os endereços são `https://`; 259 sermões em ~1 min com `xargs -P 16`); Teresinha; Francisco de Sales (Annecy, `oeuvresdesaintfr01fran`…`20fran`; `https://www.donboscosanto.eu/francesco_di_sales/`); Vianney (*Sermons*, 4 tomos); João da Cruz, Santa Teresa e Santa Catarina (`https://documentacatholicaomnia.eu/03d/`; o `.doc` da DCO em cp1252 se lê sem conversor) |
| 12. Sl 35 | Divinum Officium sem a API do GitHub (baixar as pastas latinas, ~19 MB: `curl -sL https://codeload.github.com/DivinumOfficium/divinum-officium/tar.gz/refs/heads/master \| tar xz --wildcards '*/web/www/missa/Latin/*' '*/web/www/horas/Latin/*'`); Ofício das Leituras em latim (`https://universalis.com/L/<AAAAMMDD>/readings.htm`; semana do saltério = semana do Tempo Comum módulo 4); Missal de 2002 no Clerus (`…/en/gld.htm`, `glh.htm`, `gli.htm`); o Clerus mistura as numerações; quadros do Lecionário (`1970USL-WeekdaysA.htm` e `…B.htm`); Newman com `https://` |

## 6. O que os relatórios de Nm 12–15 dizem do livro

Os relatórios (`numeros/012` a `015`, `relatorio-*.md`, `liturgia-nm-14.md`, `liturgia-nm-15.md` e os `PEDIDO.md`) ficam onde estão; aqui está só o que eles dizem de onde as obras tratam Números, o que não existe,
onde se procurou e como. Os excertos escolhidos (achados) e as leituras de cada capítulo estão nos próprios relatórios e nos `achados-*.json`.

### 6.1 Onde cada obra trata Nm 12–15

| Obra | Nm 12 | Nm 13 | Nm 14 | Nm 15 |
|---|---|---|---|---|
| Ruperto, *In Numeros* | I, 33–35 (PL 167, 869B–873B); a fonte principal do grupo | I, 36–40 (873C–880A) | I, 38 (fim)–40 (876C–880A); mais *In Osee* V, *In Michaeam* I, *In Cantica* VI, *In Leviticum* II, 34, *In Zachariam* I | II, 1–2 (879B–881B) (os números de colunas dos relatórios de 14 e 15 se sobrepõem: conferir); não comenta os vv. 1–21 nem as franjas; *In Deut.* I, 18 (936D–937C, Dt 22,12), *In Ex.* (641D) e *In Lev.* (818B) falam da hemorroíssa sem Nm 15 |
| Rábano, *Enarrationes* | II, 9 (PL 108, 661C–667): compilação de Jerônimo Ep. 78, Agostinho QH IV, 20 e Orígenes hom. VI–VII | II, 10–11 (666D–672; II, 11 = 669C–671C copia Orígenes, hom. VII, 6) | II, 11 fim (675A–C): próprio dele (a «protérvia» contra a presunção «pelagiana») | II, 12–16 (675D–680D): sentido espiritual sem fonte indicada; o resto é Agostinho, Isidoro e Jerônimo |
| Isidoro, *Quaest. in Num.* | 14 (de Ambrósio) e *Allegoriae* 61–62 | 15 (de onde vêm Rábano e o pseudo-Beda: os dois carregadores) | salta de Nm 13 (cap. 15) às mansões (cap. 16 = Ramot, Nm 33); nada | 15, 12–13 (PL 83, 347B–C): o homem da lenha = o cristão que junta obras da carne (1Cor 3,12); copiado por Rábano, pseudo-Beda e *De fide catholica* II |
| pseudo-Beda, *Quaest.*; «Beda», *In Pentateuchum* | copiam Isidoro; nada próprio | PL 91, 364D–365A (copia Isidoro) | | |
| Paterius | o livro IV salta do cap. 11 ao 16 | idem | idem (nada) | idem; as 10 notas «Num. 15» do Paterius são números de parágrafo |
| Hugo de São Vítor, *Adnotationes* | não toca o cap. 12 | não toca Nm 13; *De sacramentis* I, 10, 7 (PL 176, 340C–D) repete Beda (o cacho «em sombra e figura») | *De sacramentis* (PL 176, 305) cita Ex 20,5 sobre os pais e os filhos (não lido a fundo) | |
| Bruno de Segni, *In Num.* | | *In Num.* 14 (PL 164, 481D–482B): os doze não são os apóstolos; são os pastores | *In Num.* 14 (482B–D): a fórmula de 14,18 palavra por palavra | *In Num.* 15 (483A–485C): o melhor latino aqui; comenta o capítulo inteiro |
| Cornélio a Lápide | t. II pp. 251–255 | pp. 255–261 | pp. 261–268 (imagens 263 e 266 conferidas) | pp. 269–273 (imagens 271 e 272) |
| Orígenes, hom. (Rufino) | hom. 6, 4 (Maria = a sinagoga) e hom. 7 §§ 1–4 (transcritas das imagens); a etíope = a Igreja das nações | hom. 7 §§ 5–6; hom. 8 § 1; hom. 9 § 1 (GCS 56: o relatório de Nm 13 cita «Homilia 9, § 1» nessa página, mas no OCR a H9 começa na p. 54 com os turíbulos de Nm 16,37: **conferir a numeração**); homilias sobre Josué 1, 1–3 (o nome de Jesus), 18, 2–3 e 20, 5 | hom. 8 inteira (GCS 49–53), 9, 8 (GCS 66), 27, 4 e 7 (GCS 262, 265), hom. sobre o Êxodo 7, 4 (GCS 29, 209–210); a hom. 9, 2 (GCS 56–57) é Nm 16 | |
| Agostinho, *Quaest. in Hept.* IV | 20 (PL 34, 727; CSEL 28/1, 331) | 21–22 (PL 34, 727: só literais) | 23 (v. 9: «abscessit tempus ab eis»); *Locutiones* IV (vv. 7, 10, 11, 24, 26, 29, 31, 35) | 24–25 (o relatório de Nm 14 pergunta se o texto de Lápide sobre Nm 14,9 vem de IV, 24) |
| Teodoreto, *Quaest. in Num.* | 22–23 (PG 80, 373–376) | 24–26 (PG 80, 377) | 27 | 28–31 (PG 80, 379–381) |
| Cirilo, *Glaphyra* | PG 69, 589–605 | 605–616 (cobre Nm 13–14: «Sobre os que exploraram a terra da promessa») | 608–616 (o choro e a volta ao Egito 608–609; a glória e a súplica 609; as mulheres e os filhos 612; as crianças que entram com Caleb 613–616) | 616–625 (Nm 15,17–29 com Lv 23,10–14; a flor de farinha e o «não comereis do novo» 624–625 são Lv 23) |
| Cirilo, *De adoratione* | XIV (PG 68, 889) | V (PG 68, 372–376) | IV (PG 68, 352: o censo de Nm 26,64–65 que cumpre Nm 14,29–30); V (373–376, Nm 14,1–10) | XVI (1029–1032: Nm 15,1–16 inteiro); IX (605); VII (481–484 e 493–497: as franjas e o homem da lenha) |
| Cirilo, *Comentário a João* | | | IV (PG 73, 619–620: a arca que não sobe) e VI (PG 73, 944–948; Pusey II, 140–144: «até a terceira e a quarta geração») | IV, 2 (Pusey I, 521–522: a primícia da massa) e IV, 6 (623–624: o homem da lenha) |
| Procópio, *In Numeros* | PG 87/1, 823–828 | 829–830 (só latim) | 829–836 (latim e escólios gregos) | 835–838 (escólios gregos para os vv. 2, 15, 22–29; o resto só no latim; próprio dele: vv. 30–36) |
| Efrém (atribuído), *In Numeros* | | Assemani I, p. 258–259 | p. 258–259 | p. 259–260 |
| Nissa, *Vida de Moisés* | I, 61–62; II, 256–264 (PG 44, c. 317 e 413–416) | II, 265–270 (PG 44, c. 416–417); *Hom. sobre o Cântico* 3 (GNO VI, 98–99) | I, 65 (duas frases) | *In Cant.* 13 (GNO VI, 381–382: «primícia da nossa massa») |
| Ireneu, *Adv. haer.* | IV, 20, 9 e 12 (Harvey II, 220–224) | | | |
| Crisóstomo | *Estátuas* 20, 4; *Mt* 78, 4 e 5, 4; *Sl* 44, 5; *1 Cor* 1, 2; *A Estagírio* III; *Hb* 5; *Sl 100* (atribuído); *At* 34, 4 | *Mt* 39, 4; *Hb* 6, 2 e 27, 3 | *Hb* 6, 1 e 3; *1 Cor* 23, 3; *Jo* 13, 1 | *Mt* 72, 2; *2 Cor* 6, 3; *1 Ts* 8, 4; *At* 11; *Rm* 19 (Rm 11,16) |
| Basílio | *Hexaémeron* 1, 1; *Regras breves* 25–27; *Hom. 10 Contra os irados* | nada | só menções | *De iudicio Dei* (PG 31, 661 e 668) |
| Eusébio, Barnabé, Justino, Cirilo de Jerusalém, Anfilóquio | | Barnabé 12, 8–9; Justino *Dial.* 75 e 113; Eusébio DE IV, 17, HE I, 3, 4, *Ecl. proph.* I, 11, *Onomasticon*; Cirilo Jer. *Cat.* X, 11; Anfilóquio *In Zacchaeum* | Eusébio *In Ps.* 94 (PG 23, 1216–1217); Clemente Romano 1 *Clem.* 53; Teodoreto *In Ps.* 94 e 105, *In Ez.* 20, *Quaest. in Ex.* 40 e 67, *in Deut.* 1 | Máximo Confessor *Quaest. et dubia* 76; Damasceno *Exp. fidei* 46 (III, 2); Isidoro de Pelúsio *Ep.* I, 185 (PG 78, 301–304); Teodoreto *In Gen.* 37 e *In Ps.* 109 |

### 6.2 O que os relatórios de Nm 12–15 dizem que não existe, só com ressalva ou não serve (por obra; o que vale para todo o livro está em 4.1)

| Obra ou autor | Nm 12 | Nm 13 | Nm 14 | Nm 15 |
|---|---|---|---|---|
| Agostinho | **Contra Faustum**: nada sobre Nm 12; a etíope = Igreja das nações: não em obra autêntica; *Locutiones* IV só gramática («lenis valde»); *De Trin.* II, 16,27 só Ex 33; sem achados para a oração por Maria (v. 13) e a cusparada (v. 14); a mansidão: *Contra Gaudentium* I, 19,20 | o nome de Josué: três textos fortes; **sem achados** para Caleb que faz calar o povo, os gigantes e **gafanhotos** (v. 33), os doze = apóstolos, os 40 dias, as primeiras uvas, as romãs e figos; *De civ. Dei* XVI, 43 só menciona Josué; **os dois carregadores** do cacho não estão nas obras autênticas (só no sermão sobre Caná publicado por Mai, texto 7513) | nenhum texto dele aplica o perdão e a pena a Nm 14; Moisés intercessor: sempre Ex 32 (Sermão 88, 24; En. in Ps. 77, 22 e 105, 21); sem achados para Horma, o «outro espírito» de Caleb, as dez tentações, «toda a terra se encherá da glória» (v. 21), o «até quando?» (v. 11) | |
| Orígenes | não consultada a PG 12 (colunas de Delarue); os fragmentos gregos de cadeia ficaram com os gregos | **não há** leitura do cacho na vara (nem latim nem grego); nada sobre os doze = apóstolos; *Hom. sobre o Êxodo* 11, 3 (o primeiro Jesus, Ex 17) e *Hom. sobre o Sl 36*, 2, 4 não procurados | **não existe** leitura de «eles são o nosso pão» (o PEDIDO de Nm 14 atribuía a Orígenes «os vícios vencidos alimentam a alma»: **não achada** em nenhuma obra dele; talvez seja de Cirilo ou de Ambrósio), da «sombra», do «outro espírito» de Caleb, das «dez tentações», da «glória», de Horma; homilias gregas sobre os Salmos do códice de Munique (Sl 77, ed. Perrone, GCS NF 19, 2015): direitos, não consultadas | |
| Latinos | Rábano só compilação; Paterius nada; Beda nada; Cassiano nada (nem a mansidão de Moisés); Hugo nada; Taio só um catálogo; Glosa não consultada; **Ambrósio** *De virginibus* e *De institutione virginis*: Maria, irmã de Moisés, só em Ex 15; nenhum latino usa *humillimus* | **gafanhotos e gigantes** (v. 33): nenhum latino (só Orígenes hom. VII, 6, copiado por Rábano II, 11); Tomás II-II q. 133 e q. 129 não citam Nm 13 (no Corpus Thomisticum inteiro Nm 13 só em *Super Heb.* 3, *Super Is.* 40 e na *Catena aurea*); Rábano II, 10–11 só compilação; Honório, Cipriano (e *Testimonia*), Gregório (*Concordia testimoniorum*, *In I Regum*, *Dialogi*, cartas, *Regra pastoral*), Cassiano, Prudêncio, Cesário, Zenão, Gaudêncio, Euquério (só *Formulae*), Próspero: nada além do registrado; Bernardo: 72 obras varridas (só SC 44, *De diversis* 18 e *Qui habitat* 7, 7); Boaventura e a edição crítica de Ricardo (Châtillon 1958, direitos) não consultados | «sicut panem ita eos possumus devorare» e «recessit ab eis omne praesidium»: nenhum latino (só Lápide, sobre a «sombra»); «portabunt fornicationem vestram», «scietis ultionem meam», «sicut locuti estis… sic faciam»: só citações; Ez 4,6: Jerônimo e Ruperto sem ligar a Nm 14; Leão Magno, Cipriano, Tertuliano, Lactâncio, Prudêncio, Zenão, Gaudêncio, Euquério, Hugo e Ricardo de São Vítor: nada próprio; Isidoro salta; Paterius nada; **Gregório sobre Moisés intercessor** (*Moralia* IX, 11 e 24; *Hom. Ev.* PG 76, 1209B; *Reg. past.* PG 77, 97C) fala de Êx 32 ou Jr 15,1, não de Nm 14; **Tomás, comentário a 1 Cor 10: não existe** (lacuna de 1Cor 7,10–10,33); II-II q. 97 e q. 21 não conferidas; Bernardo (PL 183, 935C–D) é Êx 32,10; «Haimo» *In Ps.* 105 e pseudo-Jerônimo *Breviarium* in Ps. 109: no texto, fora dos achados; Boaventura não consultado | **o estrangeiro com a mesma lei** (vv. 14–16): nenhum latino; «cum ingressi fueritis terram» como promessa depois do castigo: nenhum latino; Gregório nada (só os três modos de pecar, *Moralia* XXV, 11, 28, repetidos na *Concordia testimoniorum*, PL 79, 675B, e em Isidoro, *Sent.* II, 17, 3, PL 83, 620A); Hilário (*In Mt*, texto 6863, e os demais) sem Nm 15; Cipriano, Leão, Máximo de Turim, Cromácio, Gaudêncio, Pedro Crisólogo, Fulgêncio, Cesário, Aelredo, Guerrico, Isaac de Stella, Bernardo, Hugo e Ricardo de São Vítor, Lombardo nada próprio; Tomás I-II q. 76–78, q. 100, II-II q. 122, *Super Heb.* 10, l. 3 e a *Catena* sobre Mt 9,20 e 23,5 não citam Nm 15; Jerônimo Ep. 148 (as franjas) não é dele (Pelágio ou círculo) e não foi usada; Rm 11,16: Atão, Hervé, Bruno Cartuxo, Lanfranco, Sedúlio, Lombardo, Rábano sem Nm 15; Boaventura e Belarmino não consultados |
| Gregos | Efrém: ver 4.1; Teodoreto *In Heb.*, Teofilato, Ecumênio: não no khazarzar; Damasceno só escólios; Basílio *Regras longas*: nenhuma citação; Fílon só para entender; Apolinário herético; **nenhum grego** trata «Moisés viu a essência de Deus?» a partir de Nm 12 (exceto Cirilo e Ireneu) | Cirilo **não lê o cacho** cristologicamente em nenhuma obra (só Nissa, Procópio e Anfilóquio); **os dois carregadores** não aparecem em nenhum grego; Basílio, Nazianzeno etc.: só menções; «éramos como gafanhotos»: só Teodoreto (*In Gen.* 48, *In Deut.* 7) e Cirilo; «a terra que devora seus habitantes»: nenhum grego; os doze = apóstolos: nenhum (Cirilo faz de **Caleb e Josué** os apóstolos); Teodoreto *Quaest. in Num.* sem pergunta sobre o cacho nem sobre Caleb; **Afraates** (*Dem.* 11, ed. Parisot, PS I, 1894) não conferido; Hipólito não procurado | «eles são o nosso pão» e «a sombra»: nenhum grego fora Orígenes; «visto face a face» (v. 14): nenhum; Josué e Caleb rasgam as vestes: só Cirilo *De ador.* V; os 40 anos «um ano por dia»: só Teodoreto *In Ez.* 4,6; **Horma**: nenhum grego nomeia; Nissa só I, 65; Crisóstomo: nenhuma homilia sobre o choro, a glória ou Horma; Isidoro de Pelúsio, Diádoco, João Clímaco fora; cadeia de Nicéforo (Leipzig 1772–73) não digitalizada; Eusébio *In Ps.* 94 existe mas não virou achado | Nm 15,1–16 fora de Cirilo, Procópio e Teodoreto: nenhum grego; «de mão levantada»: só Basílio, Teodoreto e Procópio (latim); os pecados de ignorância: as citações são de Lv 4; «fora do acampamento»: ninguém liga a Hb 13,12–13; o sábado e o domingo: Damasceno *Exp. fidei* 96 (IV, 23), Pseudo-Atanásio *De sabbatis* (PG 28, 136), Epifânio *Panarion* 66, 82–83 (fraco): não usados; Cirilo *Collectio dictorum VT* (PG 77, 1200) é resumo; as franjas: fora de Cirilo, Teodoreto, Crisóstomo, Máximo e Procópio só menções; a mulher que toca a orla (Mt 9,20): nenhuma liga às franjas; Clemente de Alexandria, Justino, Ireneu (grego), Const. Apost., Cirilo de Jerusalém (*Mistag.* 3, 6 usa Rm 11,16 para o crisma), Nazianzeno, Atanásio, Eusébio, Epifânio: nada; Teofilato, Ecumênio, Diádoco, Padres do deserto: não conferidos; liturgia grega: nada |
| Modernos | Santa Teresa, Santa Catarina, Afonso (concordância e *Condotta ammirabile*), Francisco de Sales (*Introdução* inteira), Newman («Miriam» em nenhum sermão): nada ou quase; **ninguém** deste grupo comenta a lepra de Maria; não procurados: Boaventura, Belarmino (não comentou Números), Pedro Canísio, João Bosco, Teresinha; João Paulo II (catequeses sobre Moisés), *Verbum Domini*, *Gaudete et exsultate*, Clerus: não pesquisados | Catecismo: nenhuma citação de Nm 13; Papas: só Santa Marta de 20/03/2018; Missal/Breviário antigo: nada; Afonso: só a *Condotta*; João da Cruz: nada; Bossuet (20 vols.): nada; Josemaría (escriva.org 403): não verificado; Inácio e jesuítas antigos: não procurados; Liturgia das Horas, 2ª leitura do dia: não conferida | Catecismo: nenhuma citação de Nm 14 (nem o Catecismo Romano, nem Trento); Papas: só 1/06/2011 (Moisés intercessor, Ex 32) e a Vigília Pascal de 2013; *Verbum Domini*, *Spe salvi*, *Lumen fidei*, *Evangelii gaudium*, *Laudato si'*, *Gaudete et exsultate*, *Misericordiae vultus*: nada; Leão XIV: nada; sem catequese de João Paulo II ou Bento XVI sobre o Sl 95; João da Cruz (só Nm 11, 12, 17, 22), Teresa, Vianney: nada; Missal e Breviário antigos: nada além dos Improperios e do invitatório; Cantus Index: nada com Caleb/Horma; Liturgia das Horas: 2ª leitura e responsório da sexta da 4ª semana da Quaresma não conferidos | Catecismo, Catecismo Romano, Trento, *Dies Domini*, Francisco (Mt 23,5 só como vaidade), Leão XIV, João da Cruz, Teresa, Vianney, Afonso (concordância e *Theologia moralis* lib. III, tract. 3), Belarmino (*Explanatio in Psalmos*, *Dottrina cristiana*), Canísio (só transcreve Nm 15,32–36): nada de Nm 15; Antônio de Pádua (80 sermões): nada; Bernardino de Sena (t. III–V de Lyon 1650 e II–IV de Veneza 1591): só o sermão X; Newman: só a nota de *Essays on Miracles* II, 5; não procurados: Lourenço de Brindisi, Luís de Granada, Catarina de Sena, Inácio, Teresinha, Pio XII, Gregório VII |
| Liturgia | Missal/Breviário antigo: nenhum uso (busca por «Num 12»: só falsos positivos); Ofício das Leituras não conferido | Missal antigo: nenhum uso de Nm 13; «botrum»: nada | Missal e Breviário antigos: nenhuma leitura de Nm 14 («Caleb» só em 1Mc 2,56) | nenhum versículo de Nm 15 na Missa, no Ofício das Leituras (ciclo anual) nem no Breviário antigo; Ofício das Leituras salta os caps. 15–19; ciclo bienal e responsórios: não conferidos |

### 6.3 Onde se procurou nos relatórios (para não procurar de novo)

| Frente | Corpus varrido |
|---|---|
| Gregos | ~990 PDFs do khazarzar (Crisóstomo, Basílio, Nazianzeno, Nissa, Damasceno, Ireneu, Epifânio, Dídimo, Astério, Macário, Máximo, Ecumênio, Clemente, Atanásio, Severiano, Cirilo de Jerusalém, Orígenes; *Glaphyra* e *De adoratione* de Cirilo; *Quaestiones* de Teodoreto) + 294 (Justino, Eusébio exceto os Salmos, Cirilo de Alexandria inteiro, Teodoreto inteiro, Procópio no que há, Barnabé, Melitão, Evágrio, Hesíquio, Gregório Taumaturgo, Anfilóquio, Diodoro, Const. Apost., Clemente Romano, Eustácio, Marcelo, Paládio, Olimpiodoro, Fócio) + Teodoreto *In Psalmos* e Eusébio *In Psalmos*; busca sem acentos pelas palavras da LXX de cada versículo; OCR do archive.org da PG 80, 87/1, 44, 73, 78 e do vol. I de Efrém |
| Latinos | a PL do Corpus Corporum (528 textos já baixados, depois 766 com os escritos de Paulo e 238 dos scratchpads), o Corpus Thomisticum (464–469 páginas) e Lápide; busca pelas notas de Migne e pelas palavras da Vulgata Clementina de cada capítulo |
| Orígenes e Agostinho | GCS 30 (Bd. 7) por imagens das páginas; as 140 obras de Agostinho no Corpus (desde Nm 13, copiadas dos scratchpads) |
| Modernos | Corpus Thomisticum, Lápide, Index scripturaire de Francisco de Sales, Newman inteiro, Belarmino (12 t.), os 7.105 documentos papais em italiano, Clerus, Lecionário (CNBB, Felix Just), DCO (João da Cruz, Teresa, Antônio de Pádua, Bernardino de Sena), Catecismo (34 arquivos), Bossuet (20 vols.), Afonso (IntraText) |

### 6.4 Liturgia de Números (relatórios de Nm 12–15)

| Onde | O quê |
|---|---|
| Missa, Lecionário de 1981 (também o da CNBB) | Números só aparece em 6,22-27; 11,4b-15; 11,25-29; 12,1-13; 13,1-2.25–14,1.26-30.34-35; 20,1-13; 21,4b-9; 24,2-7.15-17 (o romano tem 13,1-2.25–14,1.26a-29a.34-35; o brasileiro inclui o v. 30). Nm 12,1-13 = terça-feira da 18ª semana, ano I (03/08/2021, 08/08/2023, 05/08/2025, 03/08/2027; salmo 50[51]; evangelho Mt 14,22-36); Nm 13–14 = quarta-feira da 18ª semana, ano I (04/08/2021, 09/08/2023, 07/08/2019; próxima 04/08/2027; salmo 105[106]; evangelho Mt 15,21-28) |
| Missal antigo (1570–1962) | só Nm 20, sexta da 3ª semana da Quaresma (`Tempora/Quad3-5`); nenhuma perícope de Nm 12–15 |
| Ofício das Leituras (ciclo de um ano) | 4ª semana da Quaresma: Nm 11,4-6.10-30 (quarta); 12,16–13,3.17-33 (quinta); 14,1-25 (sexta); 20,1-13; 21,4-9 (sábado); **salta os caps. 15–19** |
| Textos do NT lidos na liturgia que pressupõem Números | Hb 3,7-14 (quinta da 1ª semana do TC, ano I; Sl 94[95]) e Hb 4,1-5.11 (sexta); 1Cor 10,1-6.10-12 (3º domingo da Quaresma, ano C); At 3,17 (3º domingo da Páscoa B); Mt 9,20 e 23,5 (ver `numeros/015/liturgia-nm-15.md`) |
| Canto e hino | Improperios da Sexta-feira Santa («eduxi te per desertum quadraginta annis…»); invitatório Sl 95; três sequências com o cacho (Cantus Index); antífonas sobre Mt 9,20-21 (Cantus 002187 e 004914) |
| Nomes da liturgia do Brasil (Lecionário da CNBB) | Moisés, Aarão, **Faran** (ou Farã), Cades, Canaã, Enac, Caleb filho de **Jefoné**, Josué filho de **Num**, amalecitas, **Negueb**, hititas, jebuseus e amorreus, **Comunidade**/comunidade para *ʿēdâ* (não «assembleia»); Sl 105(106),6-7a.13-14.21-22.23 |

### 6.5 Divergências entre os relatórios e este levantamento

- Isidoro: os relatórios falam em «Quaest. in Num. 14, 15» como capítulos de Números; no texto do Corpus Corporum os capítulos de Isidoro são as 42 mansões de Nm 33 (cap. XIV = Haserot = Nm 12; XV = Rethma = Nm 13–19).
- Orígenes: ver 6.1 (a numeração «hom. 9, 1» do relatório de Nm 13).
- Agostinho: o catálogo dizia que o Corpus Corporum não tem as *Enarrationes*; a observação vale só para a busca de frase (já corrigida em `agostinho.md`, § 3).
- O relatório de Nm 14 diz que Procópio tem escólios gregos para Nm 14 (o de Nm 13 dizia «só latim»): para Nm 13 é verdade; para Nm 14 não.

## 7. Scripts e como refazer ou estender

| Script (`pesquisa/ferramentas/base/`) | Faz |
|---|---|
| `_numeros_comum.py` | `baixar` (cache, 1 s de pausa, novas tentativas), `cc_*` (Corpus Corporum), `cortar`/`estrutura`/`edicao_pl`, `gravar` (cabeçalho exato), PDFs do khazarzar (`pdf_linhas`), LXX de Rahlfs (`pontuar`: 4-gramas por capítulo), `atribuir_dp` (capítulo por palavras-chave com ordem preservada) |
| `lat-rabano-num.py`, `lat-isidoro-num.py`, `lat-pseudobeda-num.py`, `lat-ruperto-num.py`, `lat-bruno-num.py`, `lat-hugo-num.py`, `lat-paterio-num.py`, `lat-agostinho-num.py` (Quaestiones e Locutiones) | cortes do Corpus Corporum pelas notas de Migne, títulos e referências |
| `lat-origenes-num.py`, `lat-lapide-num.py` | OCR do archive.org (GCS 30; Vivès t. II) |
| `grc-teodoreto-num.py`, `grc-cirilo-num.py` (Glaphyra, Fragmenta, De adoratione), `grc-nissa-num.py`, `grc-origenes-num.py` | PDFs do khazarzar |
| `grc-procopio-num.py`, `sir-efrem-num.py` | OCR do archive.org com atribuição por palavras-chave |
| `pistas-ausentes-num.py` | grava `_ausentes-numeros.md` e `_pistas-numeros.md` de cada capítulo |
| `num-tudo.py` | roda tudo e o `base-indice.py --todos` |

Para estender a outro livro, copiar o script da obra mais parecida (o corte por notas de Migne vale para todo o Corpus Corporum; o `pdf_linhas` para os PDFs do khazarzar).
