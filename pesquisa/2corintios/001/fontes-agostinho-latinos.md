# Fontes: Agostinho e Padres latinos antigos sobre as cartas de São Paulo (aprendido em 2Cor 1, 2026-10-18)

Para juntar depois a `../../fontes/agostinho.md` e `../../fontes/latinos.md`. Tudo da PL de Migne no Corpus
Corporum (Zurique): baixar o texto puro com
`https://mlat.uzh.ch/php_modules/download.php?idno=<texto>&type=file-txt` (em 18/10 o servidor respondeu rápido:
40 textos em 25 s, 8 em paralelo).

## 1. Os comentários latinos antigos que cobrem as cartas inteiras

| obra | autor | PL | Corpus: autor → obra → **texto** | cobre | observações |
|---|---|---|---|---|---|
| *Commentaria in XIII epistolas Pauli* | **Ambrosiaster** (Roma, c. 366–384; a tradição o pôs entre as obras de Ambrósio) | 17 | 960 → 428–440 → **6983–6995** (um texto por carta) | todas as cartas de Paulo, menos Hebreus | **o único comentário latino antigo, verso a verso, de domínio público na PL**; claro, histórico, com ideias próprias (unção régia, «fé é coisa de vontade», «a carta é imagem, a presença é a verdade»). Citar como «Ambrosiaster», escritor eclesiástico. Permalink `cps_2.Ambros.CoInEpA<N>` (2Cor = `CoInEpA3`) |
| | | | textos: Rm **6990**, 1Cor **6984**, 2Cor **6985**, Gl **6987**, Ef **6986**, Fl **6989**, Cl **6983**, 1Ts **6991**, 2Ts **6992**, 1Tm **6993**, 2Tm **6994**, Tt **6995**, Fm **6988** | | cada capítulo começa com `CAPUT N.`; os versículos vêm marcados `{(Vers. N.)}` (nota de Migne) e as colunas `[col. 275C]`; números soltos (169, 170…) são páginas da edição beneditina. Edição crítica: Vogels, CSEL 81/1–3 (1966–1969), com direitos |
| *Complexiones in epistolas apostolorum* | Cassiodoro (séc. VI) | 70 | 1027 → 2919 → **7917** | todas as cartas de Paulo, as católicas, Atos e Apocalipse | só **resumos** de blocos de capítulos (2Cor 1,1–2,11 em 4 parágrafos, PL 70, 1339A–D); `grep -n "EPISTOLA SECUNDA AD CORINTHIOS"`; serve pouco |
| *Commentaria in epistolas S. Pauli* | pseudo-Primásio (círculo de Cassiodoro, revisão de **Pelágio**) | 68 | 1196 → 2901 → **7897** | todas, com Hebreus | base pelagiana: **não usar** (só para conferir leituras); 2Cor 1 em PL 68, 554D–557B |
| *Expositio in epistolas Pauli* (PL 30) | **Pelágio** (sob o nome de Jerônimo) | 30 | 879 → (vários) → **7186** (`HieStr.CoInEpA15`) | 13 cartas | herege: **não usar**. Atenção, o Corpus o lista sob Jerônimo |
| Augustinus, *Expositio ad Galatas*; *Expositio quarundam propositionum ex ep. ad Romanos*; *Ep. ad Romanos inchoata expositio* | Agostinho | 35 | 900 → **7319**, **7321**, **7320** | só Gálatas e Romanos | para as outras cartas, só as citações espalhadas (abaixo) |
| *Collectaneum* sobre Paulo (excertos de Agostinho) | Beda | — | **não está na PL nem no Corpus** | todas | só ed. moderna; a coleção parecida de **Floro de Lião** (séc. IX, PL 119, parcial) é da frente medieval |

Vale lembrar: **Jerônimo** só comentou Gálatas, Efésios, Tito e Filêmon (PL 26; Corpus 879); **Gregório Magno,
Hilário, Ambrósio, Leão, Cipriano, Cesário, Isidoro** não comentaram nenhuma carta de Paulo. Para eles, buscar as
citações nas outras obras. *Paterius* (PL 79) não tem a parte do NT além dos Evangelhos.

## 2. Agostinho: onde ele cita Paulo

- **Não há índice**; as notas de Migne marcam pouco (em 2Cor 1, 45 notas em 127 obras). O que funciona: **buscar
  pelas palavras da Vetus Latina dele**, que muitas vezes difere da Vulgata. Em 2Cor 1: «non fuit **Etiam** et Non,
  sed **Etiam** in illo erat; quotquot enim promissiones Dei, **in illo Etiam**» (às vezes *Est*); «Testem Deum
  invoco **super** animam meam» (ou *Testem Deum facio*); «**cooperatores** sumus gaudii vestri»; «**Nam** gloria
  nostra haec est»; «**supra vires** gravati sumus, et supra modum»; *arrha* em vez de *pignus*. Nenhuma vez cita os
  vv. 3–4 (nem *pater misericordiarum*, nem *miserationum*).
- **Sermões**: procurar primeiro um sermão pregado sobre a leitura do dia. Em 2Cor 1 foi o **Sermão 305/A** (Denis
  13, São Lourenço, PL 46, 855–862: «Paulum Apostolum, cum legeretur, audistis»): no Corpus está nos *Sermones
  inediti* (**7505**, `AugHip.SerIne`, os 25 de M. Denis, 1792); os outros sermões: *de Scripturis* **7334** (1–183),
  *de tempore* **7335**, *de sanctis* **7333**, *de diversis* **7342**, *dubii* **21440** (aí estão o 376–378 e
  outros que os Maurinos deram como autênticos), *Sermones 1* **7504**, *Sermones 2* **7513**.
  Tabela do número do sermão → arquivo do augustinus.it (`latino/discorsi/discorso_NNN_testo.htm`): está no
  `<select>` de `latino/discorsi/sommario.htm` (cópia em `94b210f9…/scratchpad/wb/d_sommario.htm`); alguns:
  23 = 029, 47 = 058, 93 = 120, 156 = 201, 180 = 233, **305/A = 432**, 378 = 547.
- **augustinus.it**: padrões de arquivo conferidos no Internet Archive (o site deu 503 em 18/10):
  `lettere/lettera_NNN_testo.htm` (Cartas, NNN = número da carta), `cdd/cdd_NN_libro.htm` (*Cidade de Deus*),
  `trinita/trinita_NN_libro.htm`, `contro_fausto/libro_NN_testo.htm`, `commento_vsg/omelia_NNN_testo.htm`
  (*In Io.*), `commento_lsg/omelia_NN_testo.htm` (*In ep. Io.*), e para obras de um livro só
  `<pasta>/<pasta>_libro.htm` (`lettera_cattolici`, `agone_cristiano`, `dignita_vedovile`, `menzogna`). Lista das
  pastas: `latino/index.htm` (cópia em `639cd05d…/scratchpad/n14oa/augit/index_ia.htm`). Índice CDX do Internet
  Archive (`http://web.archive.org/cdx/search/cdx?url=augustinus.it/latino/<pasta>/*&output=txt&fl=original&collapse=urlkey`)
  dá os nomes de arquivo de uma pasta; às vezes responde «Temporarily Offline»: repetir após alguns segundos.
- Pistas temáticas de Paulo em Agostinho, achadas aqui: «gloria nostra… testimonium conscientiae» (2Cor 1,12) é
  dos versículos que ele mais usa: as **virgens prudentes** (o óleo nos vasos = a consciência: Sermão 93, 9–10;
  En. in Ps. 49, 9; 140, 13), a **glória humana dos romanos** (*Civ.* V, 12), **vida boa × boa fama** (*De bono
  viduitatis* 22, 27; Sermão 47, 12–13; Sermão 54, 2), En. in Ps. 53, 8 e 149, 11 (a glória da consciência sem
  soberba), *In ep. Io.* 6, 2–3. **Arra × penhor**: Sermões 23, 8–9; 156, 16; 378 (vale para 2Cor 5,5 e Ef 1,14).
  O **juramento de Paulo**: Sermão 180, 4–7; Ep. 157, 5, 40; *De mendacio* 15, 28; *De serm. Dom.* I, 17, 51.

## 3. Outros latinos: textos (`idno`) usados ou abertos nesta pesquisa

| autor (idno) | obra | texto | PL |
|---|---|---|---|
| Ambrósio (958) | *Exp. in Ps. 118* **6966**; *De Spiritu Sancto* **6967**; *De mysteriis* **6971**; *De sacramentis* **6976**; *In Lucam* **6965**; *De virginibus* **21380**; *De fide* **21369** | | 15–16 |
| Hilário (927) | *Tractatus super Psalmos* **21450**; *De Trinitate* 6871; *De synodis* 6878 | | 9–10 |
| Fulgêncio (1153) | *Contra Fabianum* (fragmentos; o Corpus chama de «Instrumenta fidei») **7810**; *Ad Trasimundum* **7812**; *Ad Monimum* 7811; Cartas 7809; *De veritate praedestinationis* 7808; sermões 7816; espúrios (1148) 7794 | 7803–7816 | 65 |
| Gregório Magno (1165) | *Regula pastoralis* **21435**; *Hom. in Ev.* **8053**; *Moralia* I–XVI **21427**, XVII–XXXV **8054**; Cartas **8064** | | 75–77 |
| Cassiano (1063) | *Collationes* **7530** (XVII, 25: a mudança de planos de Paulo, 2Cor 1,15–23) | | 49 |
| Leão Magno (1098) | Sermões 7631, inéditos **21442**, Cartas 7630 | | 54 |
| Cesário (1172) | Sermões (no Corpus: 2857), Cartas **7847**, Regras **7849–7850** | | 67 |
| Isidoro (1318) | *Sententiae* 8218, *De eccl. officiis* **8205**, *Differentiae* **8211**, *Prooemia* **8215**, *Synonyma* **8219** | | 83 |
| Pedro Crisólogo (1083) | Sermões **7597** | | 52 |
| Paulino de Nola (1131) | Cartas **7718**, Poemas 7720 | | 61 |
| Cromácio (987) | *In Matthaeum* **7084** | | 20 |
| Beda (1397) | *In Cantica* 8455; Homilias 8509; *In epistolas catholicas* **8492**; *In Marcum* **8471**; *In Io.* **8469**; *In Mt.* (espúrio) **8472**; *In Acta* **8468**, *Retractatio* 8474; *In Apocalypsim* **8490** | | 91–94 |

- **Formato das notas de Migne para 2Cor 1**: Agostinho, Ambrósio, Gregório, Hilário `(II Cor. I, 12)`, às vezes
  `(2 Cor. I, 5)` ou `(II Cor. I. 14)` e até `(I Cor. I, 8)` por engano (Sermão 305/A, 5; *Reg. past.* III, 18);
  Jerônimo `(2. Cor. 1. 5)`; Beda e Gregório às vezes só `(II Cor. I)`. Regex usada:
  `\{\(([^}]*?)\b(?:II|2)\.? ?Cor(?:inth)?\.?,? ?(?:I|1)\b(?:[,.] ?(\d+))?` sobre o texto com as notas reinseridas.
- **Scripts** (no scratchpad desta conversa, `7b3b5d55…/scratchpad/2c/`, só no notebook): `idx.py` (indexa por
  `cc_idno` todos os textos já baixados nos scratchpads anteriores: 658 em 18/10), `prep.py` (limpa: um parágrafo
  por linha, `[col. X]`, notas `{(...)}` no lugar), `phr.py` + `pats.txt` (frases de cada versículo, com o versículo
  na 1ª coluna), `sp2.py` (parágrafo + obra, livro, capítulo e número do parágrafo em volta de uma frase), `ex.py`
  (extrai o `original` exato entre duas frases), `texts.py` e `dl.py` (listar e baixar em paralelo).
