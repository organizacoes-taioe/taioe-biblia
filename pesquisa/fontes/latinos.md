# Padres latinos e santos medievais e modernos (até o séc. XVII): catálogo

Fora Santo Agostinho (catálogo próprio). Numeração dos Salmos: todos usam a grega e latina
(Vulgata): o nosso Sl 33 é o «Psalmus XXXII» deles. Primeiro uso: Sl 33 (32), 2026-10-17
(ver `salmos/033/relatorio-latinos.md`).

## 0. As duas ferramentas que resolvem quase tudo

### Corpus Corporum (Universidade de Zurique): a Patrologia Latina inteira em texto

Texto revisto da PL de Migne (5277 textos, 1528 autores), domínio público. O site é uma aplicação
em JavaScript, mas tem uma API simples, que funciona com `curl` ou Python (`urllib`):

- Navegar: `https://mlat.uzh.ch/php_modules/navigate.php?load=/<caminho>&group_by=` (XML).
  `load=/38` = PL (lista de autores, com `<name>` seguido de `<idno>`); `/38/<autor>` = obras do
  autor (`<work>`: o `<idno>` que vem depois do bloco `<corpora>`); `/38/<autor>/<obra>` = o texto
  (`<text>` → `<idno>`).
- Baixar o texto puro: `https://mlat.uzh.ch/php_modules/download.php?idno=<texto>&type=file-txt`.
  O arquivo marca as colunas da PL (`-----[page 0225A]-----`) e as notas de Migne (`[522]` no texto,
  `522: (Matth. V, 11)` no rodapé). Achar um salmo: `grep -n "PSALMUS XXXII\|IN PSALMUM XXXII"`.
  Achar citações de um salmo numa obra qualquer: `grep "(Psal. XXXII, "` nas notas.
- Link para o leitor: o *permalink* do topo do arquivo (`https://mlat.uzh.ch/browser/cps_2.<sigla>`)
  abre a obra, não o parágrafo; citar sempre a coluna da PL.
- No Git Bash, caminho começando com `/` vira caminho do Windows: passar `38/1027` e pôr a barra no
  script, ou usar `MSYS_NO_PATHCONV=1`.
- Scripts usados no Sl 33: `cc.py` (works / text / dl), `ccall.py` (baixa todas as obras de um autor),
  `clean.py` (põe `[col. 225A]` no texto e as notas entre parênteses), `para.py` (parágrafo inteiro
  em volta de uma linha). Estavam no scratchpad da conversa de 17/10; refazer é rápido.

Autores e textos já identificados (autor → obra → texto):

| autor (idno) | obra | texto | PL |
|---|---|---|---|
| Cassiodoro (1027) | Expositio in Psalterium (2924) | **21404** | 70 |
| Arnóbio, o Jovem (1085) | Commentarii in Psalmos (21469) | **21351** | 53 |
| pseudo-Jerônimo (1004) | Breviarium in Psalmos (627) | **7183** | 26 |
| São Jerônimo (879) | Epistolae (576) | **7132** | 22 |
| Santo Ambrósio (958) | Enarrationes in XII psalmos (401) | **6956** | 14 |
| Santo Ambrósio | Expositio in Ps. 118 (411); Hexaemeron (403) **6958**; De Spiritu Sancto (412) **6967**; De fide (21486) **21369** | | 14–16 |
| Santo Hilário (927) | Tractatus super Psalmos (21560) **21450**; De Trinitate (316) **6871** | | 9–10 |
| São Gregório Magno (1165) | Homiliae in Evangelia **8053**; Moralia I–XVI **21427**; Moralia XVII–XXXV **8054**; Hom. in Ezechielem **21412**; Regula pastoralis **21435**; Dialogi **8063** | | 75–77 |
| pseudo-Beda (1395) | De Psalmorum libro exegesis (3460) | **8477** | 93 |
| «Haimo de Halberstadt» (1543) | Commentaria in Psalmos (4050) | **9073** | 116 |
| São Bruno, o Cartuxo (2035) | Expositio in Psalmos (5439) | **10473** | 152 |
| São Bruno de Segni (2171) | Expositio in Psalmos (5768) | **10806** | 164 |
| Pedro Lombardo (2327) | Commentaria in Psalmos (6407) | **11455** | 191 |
| São Bernardo (2268) | 72 textos (sermões, tratados, cartas); Sermones in Cantica **11258** | | 182–185 |
| Alcuíno (1047) | só De usu Psalmorum (3679), sem comentário salmo a salmo | | 100–101 |
| Gerhoh de Reichersberg (2330), Honório de Autun (2211) | não consultados | | |
| Ruperto de Deutz (2195) | De Trinitate et operibus ejus (comentário à Bíblia inteira, do Gênesis aos Evangelhos) | **10873** | 167 |
| Rábano Mauro (1518) | Enarrationes in librum Numerorum (3875) **8898**; Comm. in Genesim **8885**; Expositiones in Leviticum (3877) | | 107–108 |
| Santo Isidoro (1318) | Quaestiones in Vetus Testamentum (21546) **21433**; Allegoriae (3196) **8202**; De ortu et obitu Patrum (3203) **8209**; Sententiae (3212) **8218** | | 83 |
| pseudo-Beda (1395) | Quaestiones super Genesim/Exodum/Leviticum/Numeros (3467: **8484**)/Deuteronomium/Jesu Nave/Regum | | 93 |
| «Beda» (1397) | Commentarii in Pentateuchum (3444) **8461** (espúrio) | | 91 |
| Paterius (1280) | Expositio Veteris ac Novi Testamenti (3103) **8106**: excertos de Gregório por livro | | 79 |
| Hugo de São Vítor (2230) | Adnotationes in Pentateuchon **11054** | | 175 |
| São Gregório Magno (1165) | também: Epistolae **8064**; In Cant. **8105**; In I Regum **21352** (hoje de Pedro de Cava) | | 77–79 |
| Santo Ambrósio (958) | também: De officiis **6974**; Epist. classis I **21400**; classis II **6979**; Apologia David **6945**; In Lucam **6965**; De Noe **21361**; De institutione virginis **21372**; De virginibus **21380** | | 14–16 |
| São Jerônimo (879) | também: Adversus Iovinianum **7149**; In Sophoniam **7180**; Quaest. hebr. in Gen. **7160**; In Isaiam **7170** | | 23–25 |
| João Cassiano (1063) | Collationes **7530**; De institutis **7531** | | 49 |
| São Pedro Damião (928) | Epistolae **10045**; Collectanea in VT (de seu discípulo João) **10066** | | 144–145 |


### Corpus Thomisticum: São Tomás

`https://www.corpusthomisticum.org/cpsNN.html`, de dez em dez salmos: `cps00` prólogo, `cps01`
Sl 1, `cps02` Sl 2–10, `cps11` Sl 11–20, `cps21` 21–30, `cps31` 31–40, `cps41` 41–50, `cps51`
Sl 51, `cps52` Sl 52–54. A página é ISO-8859-1; cada parágrafo é
`<P TITLE="Super Psalmo 32 n. 1">` com número de referência `[87088]`.

## 1. Comentários de livro inteiro (Salmos)

### Cassiodoro, *Expositio Psalmorum* (c. 540–570)
Todos os 150 salmos. Para cada um: título, divisão, explicação verso a verso, conclusão. É a fonte
principal do grupo: claro, espiritual, cheio de imagens; muito usado depois (Lombardo, Glosa). Usa
o saltério antigo (às vezes difere da Vulgata: «Gaudete, justi», «in jubilatione»). PL 70, 9–1056
(Corpus Corporum, texto 21404). CCSL 97–98 (1958) é a edição crítica, com direitos: não guardar.

### São Tomás de Aquino, *Postilla super Psalmos* (1272–1273)
**Só Sl 1–54 (Vulgata)**; acaba no Sl 54. Divisões escolásticas, mas muito rico: sentido literal,
místico e moral; frases curtas e citáveis. Ed. Parma, t. 14; Corpus Thomisticum (acima).

### São Roberto Belarmino, *Explanatio in Psalmos* (1611)
Todos os 150 salmos, verso a verso: sentido literal com o hebraico e o grego, depois a aplicação
espiritual; cita os Padres. Muito bom para o leitor comum.
- *Opera omnia*, ed. J. Fèvre, Paris, Vivès, 1870–1874: **t. X** (archive.org `operaomnia10bell`,
  1874) traz os Sl 1–75 (Vulgata); o resto deve estar no t. XI
  (`operaomnia11bell`, não conferido). OCR razoável, mas com as notas da margem misturadas ao texto.
  **Cuidado**: nesse volume o editor pôs antes de cada salmo um «Commentaria» alheio (versão do
  hebraico com «Jova», notas de Maurer, Ewald, Rosenmüller); o de Belarmino começa em
  «BELLARMINI EXPLANATIO». Achar: `grep -n "PSALMUS  XXXII"` no `_djvu.txt` (espaços duplos).
- Roma, 1611: archive.org `bub_gb_7j0Mm5XItI4C` (OCR ruim, só para conferir imagem).

### Arnóbio, o Jovem, *Commentarii in Psalmos* (séc. V)
Todos os salmos, breve; às vezes alegórico e original (no Sl 32, o salmo inteiro como as dez cordas).
Semipelagiano: usar com cuidado. PL 53, 327–570 (texto 21351).

### São Jerônimo
- *Commentarioli in Psalmos*: notas breves, só alguns versículos de cada salmo. Morin, *Anecdota
  Maredsolana* III/1 (1895), archive.org `anecdotamaredsol03unse` (o volume digitalizado reúne
  III/1–3; OCR bom). CCSL 72 tem direitos.
- *Tractatus in Psalmos* (homilias): série I (Morin, *An. Mar.* III/2, 1897; CCSL 78) com os Sl 1, 5,
  7, 9, 14, 15, 66–68, 74–78, 80–84, 86–91, 93, 95–111, 114, 115, 119, 127, 128, 131–133, 135, 136,
  140, 141, 143, 145–149 (numeração da Vulgata); série II (*An. Mar.* III/3, 1903) com mais 14. Mesmo
  arquivo do archive.org. Também ali: homilias sobre Marcos e outras (ex. *Homilia in Iohannem*).
- Cartas: PL 22 (Corpus Corporum, obra 576).

### pseudo-Jerônimo, *Breviarium in Psalmos* (séc. VII–VIII?)
Todos os salmos; copia os *Commentarioli* e acrescenta muito. PL 26, 821–1270 (texto 7183). Citar
como «autor antigo», não como Jerônimo.

### São Bruno de Segni (Bruno Astensis), *Expositio in Psalmos* (c. 1100)
Todos os salmos. Simples, moral, boas frases. PL 164, 695–1228 (texto 10806).

### São Bruno, o Cartuxo, *Expositio in Psalmos* (séc. XI)
Todos os salmos, glosa contínua («id est…»), seca mas com achados. PL 152, 637–1420 (texto 10473).

### Pedro Lombardo, *Commentarium in Psalmos* («Magna glosatura», c. 1140)
Todos os salmos; compilação com siglas da fonte ([Aug.], [Cassiod.], [Hier.], [Alcuin.], [Gl. int.]).
Útil para achar de quem é uma ideia. PL 191, 55–1296 (texto 11455).

### «Haimo de Halberstadt», *Commentaria in Psalmos* (séc. IX; de Haimo ou Remígio de Auxerre)
Todos os salmos; depende de Agostinho e Cassiodoro. PL 116, 191–696 (texto 9073).

### pseudo-Beda, *De Psalmorum libro exegesis* (medieval)
Todos os salmos; quase só Agostinho e Cassiodoro. PL 93, 477–1098 (texto 8477). Beda autêntico não
comentou os Salmos.

### Dionísio Cartuxo, *Enarratio in Psalmos* (séc. XV)
*Opera omnia*, Montreuil, t. 5–6 (1898): **não achados digitalizados** (archive.org tem outros tomos
da coleção, identificadores `doctorisecstati*`). Procurar no Google Books ou na Gallica se for preciso.

## 2. Quem NÃO comentou salmo a salmo (só citações)

- **Santo Ambrósio**: *Enarrationes in XII Psalmos* = Sl 1, 35–40, 43, 45, 47, 48, 61; *Expositio in
  Ps. 118*. Para outros salmos, varrer as notas «(Psal. N, v)» do *De Spiritu Sancto*, *Hexaemeron*,
  *De fide*, *De officiis*, *De mysteriis* e as cartas.
- **Santo Hilário**: *Tractatus super Psalmos* = Sl 1, 2, 9, 13, 14, 51–69, 91, 118–150 (PL 9; texto
  21450). O comentário aos Sl 15, 31, 41 (texto 6864) é espúrio.
- **São Gregório Magno**: nenhum comentário dos Salmos (as *Expositio in VII psalmos poenitentiales*
  são espúrias); muitas citações nos *Moralia* e nas homilias.
- **São Bernardo**: só o *In psalmum Qui habitat* (Sl 90, 17 sermões). Para outros salmos, varrer
  as notas de todas as obras (72 textos no Corpus Corporum).
- **Alcuíno**: salmos penitenciais, 118 e graduais (PL 100); nada salmo a salmo.
- **São Boaventura**: sem comentário autêntico aos Salmos.
- **Glosa Ordinária**: não está no Corpus Corporum; PL 113–114 (como de Walafrido Estrabão,
  atribuição falsa) em imagem no archive.org/documentacatholicaomnia.

## 3. Armadilhas

- Sl 148, 5 e Sl 32, 9 têm as mesmas palavras: conferir a nota de Migne antes de atribuir.
- O saltério dos Padres antigos (Cassiodoro, Breviarium, Bruno de Segni) nem sempre é o da Vulgata
  Clementina: anotar a leitura que o autor comenta.
- Não confundir os dois Brunos: o de Segni (Bruno Astensis, PL 164) e o Cartuxo (PL 152). «Bruno
  Coloniensis» no Corpus Corporum é outro (só um diploma).

## 4. Comentários latinos ao Pentateuco e a Números (primeiro uso: Nm 12, 2026-10-17)

Ver `numeros/012/relatorio-latinos.md`. Busca que funcionou: as notas de Migne (`Num. XII`; no
Jerônimo a PL usa algarismos, `Num. 12. 3`) e as palavras da Vulgata **Clementina** (os Padres leem
*mitissimus*, não o *humillimus* da Nova Vulgata). Para achar o capítulo dentro de um comentário,
procurar o primeiro versículo e o título `(CAP. XII.)` que Migne põe nos títulos de capítulo.

- **Ruperto de Deutz**, *De Trinitate et operibus eius* (c. 1112–1117): comentário de toda a
  Escritura em 42 livros; *In Numeros* em dois livros, capítulos curtos com título, versículo a
  versículo, sentido literal e depois alegórico. Original, vivo, cheio de observações humanas. É o
  melhor latino para Números (e provavelmente para o Pentateuco). PL 167 (texto **10873**, 5,7 MB;
  `grep -n "IN NUMEROS\|IN LEVITICUM\|IN DEUTERONOMIUM"` acha os livros).
- **Rábano Mauro**, *Enarrationes in librum Numerorum* (PL 108): compilação, com as fontes às vezes
  indicadas (*Ex Augustino*): Orígenes (Rufino), Agostinho (*Quaest. in Hept.*), Jerônimo (Ep. 78),
  Isidoro. Útil para ter Orígenes latino em texto; quase nada próprio. Também Gênesis, Êxodo,
  Levítico, Deuteronômio.
- **Santo Isidoro**, *Quaestiones in Vetus Testamentum* (PL 83, 207–424): Gênesis a Macabeus,
  alegórico e breve, por capítulos; em Números segue as mansões de Nm 33 (de Jerônimo, Ep. 78).
  *Allegoriae* (PL 83, 97–130): uma frase por personagem; boa chave alegórica.
- **pseudo-Beda**, *Quaestiones super …* (PL 93): copiam Isidoro. **«Beda», *In Pentateuchum***
  (PL 91, 189–394): espúrio, breve, quase nada. Beda autêntico não comentou o Pentateuco além do
  Gênesis (*In principium Genesis*, não conferido) e do Tabernáculo (*De tabernaculo*, Ex 25–30).
- **Paterius**, *Liber testimoniorum* (PL 79): excertos de Gregório Magno organizados por livro e
  capítulo da Bíblia; atalho para achar o que Gregório disse de um versículo (mas tem lacunas: em
  Números salta do cap. 11 ao 16).
- **Hugo de São Vítor**, *Adnotationes in Pentateuchon* (PL 175, 29–86): notas literais, poucas em
  Números (só até o cap. 14 da obra).
- **São Jerônimo**, Ep. 78 a Fabíola, *De XLII mansionibus* (PL 22, 698–724): as 42 mansões de
  Nm 33, cada uma com o episódio ligado a ela (Haserot = Nm 12; Cades = Nm 20 etc.). Fonte de
  Isidoro, Rábano e da Glosa para Números.
- **Glosa Ordinária**: não está no Corpus Corporum; para o Pentateuco é sobretudo Orígenes,
  Isidoro e Rábano.

## 5. Orígenes latino (Rufino e Jerônimo): as homilias sobre o Pentateuco e os históricos

Primeiro uso: Nm 12, 2026-10-17 (`numeros/012/relatorio-origenes-agostinho.md`). Orígenes não é
santo: citar como «Orígenes», sem título, e dizer que é a tradução de Rufino.

- **No Corpus Corporum só há** (autor 1049): homilias sobre o Cântico (7164), Isaías (7172),
  Jeremias e Ezequiel (7182, de Jerônimo), as 39 sobre Lucas (7192). **As homilias sobre Gn, Ex,
  Lv, Nm, Js, Jz, 1Rs (Sm) não estão** (são da PG 12, que o Corpus não tem).
- **Edição crítica de domínio público: Baehrens, GCS (Origenes Werke)**, no archive.org, com OCR
  (`_djvu.txt`) e imagens por página:
  - Bd. 6 (GCS 29, 1920): homilias sobre **Gênesis, Êxodo, Levítico** → `origenes-werke.-bd-6-1920`;
  - Bd. 7 (GCS 30, 1921): homilias sobre **Números (28), Josué (26), Juízes (9)** →
    `origenes-werke.-bd-7-1921` (Nm hom. 7 = págs. 37–48);
  - Bd. 8 (GCS 33, 1925): homilias sobre **1 Samuel, Cântico, Isaías, Jeremias, Ezequiel** e o
    Comentário ao Cântico → `GCS33` ou `origenes-werke.-bd.-8-1925`.
- Página impressa P = leaf P+36 no Bd. 7 (conferir em `..._page_numbers.json` nos outros);
  imagem: `https://archive.org/download/<id>/page/n<leaf>.jpg` (3542×5251, legível; recortar com
  PIL); link para o leitor: `https://archive.org/details/<id>/page/<P>/mode/1up`.
- O OCR mistura o aparato crítico, as referências («vgl.») e os números de linha e **perde linhas
  inteiras**: transcrever da imagem (um subagente fez as 12 páginas da hom. 7 em ~8 min).
  Achar uma homilia: `grep -n "HOMILIA VII\|in Numeros Homilia"` (os cabeçalhos de página).
- As margens dão as páginas de Delarue («Del.», = PG) e de Lommatzsch («Lomm.», t. 10 para
  Números); a coluna da PG 12 não sai daí: conferir no PDF da PG se for preciso.
- Rábano Mauro, *Enarrationes in librum Numerorum* (Corpus Corporum 8898, PL 108) copia Orígenes
  quase palavra por palavra: serve para conferir o latim de Rufino num trecho duvidoso.

## 6. Aprendido no Sl 34 (33), 2026-10-17 (`salmos/034/relatorio-latinos.md`)

- Ids novos: **São Bento** (1163), *Regula cum commentariis* = texto **21434** (PL 66; a Regra em
  parágrafos numerados, cada um seguido do comentário de Martène e outros; o Prólogo está nas
  col. 215D–218). **Ambrósio**: *De mysteriis* **6971**, *De sacramentis* **6976**, *Apologia
  Prophetae David* 6945 e *altera* 6946. **Cassiano**: *Collationes* **7530**, *De institutis*
  **7531** (permalinks `cps_2.JoaCas.Collat` e `cps_2.JoaCas.DeCoIn`).
- Permalinks conferidos (o sufixo varia e não se adivinha: copiar do topo do arquivo baixado):
  Ambrósio `AmbMed.DeMys`, `AmbMed.EnInXiP`; Jerônimo, cartas `HieStr.Episto32`; Hilário
  `HilPic.TrSuPs`; Bernardo `BerCla.DeCon4`, `BerCla.InDoPa`, `BerCla.SeDeDi2`, `BerCla.Episto308`,
  `BerCla.InFeOmS`, `BerCla.SeInCaC`; Arnóbio `ArnJun.CoInPs`; Bruno de Segni `BruAst.ExInPs3`;
  Bruno Cartuxo `BruCar.ExInPs2`; Lombardo `PetLom.CoInPs3`; *Breviarium* `AuInAuH.BrInPs`;
  Haimo `HayHal.CoInPs2`; pseudo-Beda `AuInBe.DeLiPs`; Gregório `GreI.HoInEv`.
- **O Corpus Corporum pode ficar muito lento** (17/10, à noite: ~1 texto por minuto no `ccall.py`).
  Baixar só os textos certos com `cc.py dl <texto>`, vários em paralelo (cada um levou ~1 min). Os
  arquivos já baixados numa conversa anterior ficam no scratchpad dela: procurar antes de baixar.
- Formatos das notas de Migne, para o `grep`: Bernardo, Ambrósio, Hilário, Gregório
  `(Psal. XXXIII, 9)`; **Jerônimo, cartas: algarismos** `(Psal. 33. 9)` ou `(Ps. 33)`; **Cassiano:
  sem versículo** `(Psal. XXXIII)`. A numeração das notas é a da Clementina (com o título como v. 1
  nos salmos com título), mas erra às vezes por um: conferir o texto.
- **Cassiodoro e Belarmino não numeram o título**: nos salmos com título, o «Vers. N» deles é o v.
  N+1 da Clementina. Tomás não numera (segue o texto).
- Belarmino, t. X: o Sl 33 está nas pp. 202–208 (`grep -n "PSALMUS  XXXIII"`; o dele começa em
  «BELLARMINl  EXPLANATIO.», com OCR variável do nome: procurar `EXPLANATIO`).
- Jerônimo, *Tractatus*: além das homilias sobre o próprio salmo, as de outros salmos citam muito
  (ex.: *Tract. de Ps. XV*, série II, p. 25, sobre o anjo do v. 8). Buscar no `_djvu.txt` com os
  espaços normalizados (o OCR tem espaços duplos e hifenização) e pelas notas de rodapé de Morin
  (`Ps. 33, 9`).
- Santos em língua vulgar (Catarina, Teresa, João da Cruz, Inácio, Francisco de Sales): não estão na
  PL; a busca na internet por um versículo não dá nada. Se for preciso, baixar as obras completas
  (Wikisource, archive.org) e varrer pelo texto do versículo em castelhano/italiano/francês.

## 8. Aprendido no Sl 35 (34), 2026-10-17 (`salmos/035/relatorio-latinos.md`)

- Desta vez o Corpus Corporum respondeu rápido (cada texto em menos de 1 min, 6 downloads em
  paralelo). Fluxo que funcionou: baixar direto pelos `idno` conhecidos; varrer tudo com um script
  que põe as notas de Migne de volta no texto («{(Psal. XXXIV, 3)}») e procura as palavras dos
  versículos (com `j`→`i`, `v`→`u`); depois conferir cada `original` como substring do texto
  baixado (sem notas, sem marcas de coluna). Cuidado com falsos positivos: «unicam meam» acha
  «tunicam meam» (usar `\b`).
- **Gerhoh de Reichersberg** (2330), *Commentarius aureus in Psalmos*: texto **11469** (PL 193;
  Sl 34 = col. 1333–1348, `grep -n "PSALMUS XXXIV"`); continuação **11474** (PL 194). Comenta
  primeiro sobre Cristo, a «cabeça», e depois sobre a Igreja, o «corpo». Muito de Agostinho e
  Cassiodoro, alguma coisa própria. Permalink `GerRei.CoAuInP`.
- Ids de texto novos:

| autor | textos |
|---|---|
| São Leão Magno (1098) | Cartas **7630**, Sermões **7631** |
| São Máximo de Turim (1102) | Homilias 7652, Sermões **7653** |
| Tertuliano (867) | texto = id da obra − 97: Ad martyres 40, Apologeticum 43, De oratione 47, De patientia 48, De paenitentia 49, Adv. Judaeos 62, Adv. Marcionem 63, De carne Christi 67, De jejuniis 71, De resurrectione 75, Scorpiace 77 |
| São Cipriano (878) | também id − 97: Cartas 95 e 130, De lapsis 121, De mortalitate 123, De oratione dominica 125, De unitate 127; Testimonia 21445 |
| São Bernardo (2268) | *De consideratione* **21366**, Cartas **21392** (o resto entre 11189 e 11258; 11207 e 11208 não são dele) |
| Santo Aelredo (1030) | *De Iesu puero duodenni* **11260** (PL 184, entre os escritos atribuídos a Bernardo) |
| São Beda (1397) | Homilias **8509** (permalink `Beda.Homili8`) |
| São Jerônimo (879) | *In Isaiam* **7170** (`HieStr.CoInIs`) |
| São Gregório (1165) | *Hom. in Ezechielem* **21412** (`GreI.HoInEz`); Moralia I–XVI **21427** (`GreI.Morali`), XVII–XXXV **8054** (`GreI.Morali2`) |

- Outros permalinks: Ambrósio, *In Lucam*, `AmbMed.ExEvSeL`; Tertuliano, *Adv. Judaeos*,
  `Tertul.AdvJud`; Bernardo, sermão de São Martinho, `BerCla.InFeSMa`; Páscoa, `BerCla.InDiSaP`;
  Aelredo `AelRie.DeJePuD`; Regra de São Bento `BenNur.ReCuCo`.
- **Paterius** (8106) cobre também os Salmos: reúne por versículo os trechos de Gregório (Sl 34
  em PL 79, 839C–840B), com o livro e o número dos *Moralia*. É o atalho para Gregório num salmo.
- **Belarmino, t. X**: o Sl 34 está nas pp. 212–219 (`grep -n "EXPLANATIO"` perto da linha 25064 do
  `_djvu.txt`). Nos salmos longos, ele e Cassiodoro não só deixam o título sem número: dividem
  os versículos de outro modo (no Sl 34 contam 32, a Clementina 28). Fazer a tabela de
  correspondência pelo texto, não pela regra «N+1».
- Os *Commentarioli* de Jerônimo do Sl 34 estão logo depois dos do Sl 33, na p. 41–42 de Morin
  (o OCR escreve «XXXIIIl.»).
- Nos salmos «da Paixão», os medievais (os dois Brunos, Gerhoh, Ruperto, Haimo) leem as
  imprecações como a ruína de Jerusalém, com dureza contra os judeus. Nas imprecações, os
  melhores trechos são de Cassiodoro, Arnóbio, Cassiano (*Coll.* VII, 21), Tomás e Belarmino.
## Cartas de São Paulo

Tudo em `paulo.md` (o mapa das cartas: as obras de cada carta, a tabela das homilias de Crisóstomo e a pré-pesquisa de 2Cor 3–13).

## 10. Aprendido no Sl 36 (35), 2026-10-20 (`salmos/036/relatorio-latinos.md`)

- **Índice dos textos já baixados**: os scratchpads das conversas anteriores do taioe guardam 655
  textos da PL (70 autores). Listar só as pastas `dl/`, `bern/`, `n12/`, `a<autor>/` com
  `find -maxdepth 6 -name "*.txt" -size +15k` e ler o cabeçalho (`cc_idno`, autor, obra): leva
  segundos. Um `os.walk` no scratchpad inteiro não termina (há worktrees e cópias enormes).
- Fluxo que funcionou: varrer todos os textos (menos Agostinho) com as notas de Migne reinseridas
  e com 16 padrões das palavras dos versículos (`j`→`i`, `v`→`u`); ~600 ocorrências, resumidas
  numa linha cada; depois abrir o contexto só das melhores. Os `original` saem por script, como
  substring do texto limpo (sem notas, sem marcas de coluna e sem os números de página da edição
  anterior, «766», que Migne deixa no meio das frases), com a coluna calculada sozinha.
- Ids de texto novos: **Santo Anselmo** (autor 1938), *Proslogion* **10631** (`AnsCan.Proslo`; o
  cap. 25 está também, retrabalhado, nas *Meditationes* 10626, col. 818); **Ricardo de São Vítor**
  (2350), *Adnotationes mysticae in Psalmos* **11526** (`RiSVi.AdMyInP`; só os Sl 2, 25, 28, 30, 40,
  44, 71, 74, 80, 84, 90, 98, 104, 113, 117–118, 121, 134, 136, 138–139, 143), *Benjamin major*
  11527, *Benjamin minor* 11528; **Isaac de Stella** Sermões **11493** (`IsDeSt.Sermon43`);
  **Guerrico de Igny** Sermões **21443** (`GueIgn.SePeAn`); **Pedro Crisólogo** Sermões **7597**
  (`PetChr.Sermon7`); **Máximo de Turim** Homilias 7652 (`MaxTau.Homili3`); **Ambrósio** *De fuga
  saeculi* 6954 (`AmbMed.DeFuSa`), *Exhortatio virginitatis* 6980 (`AmbMed.ExhVir`), *De Spiritu
  Sancto* 6967 (`AmbMed.DeSpSa`), *De paradiso* 21375, *De Isaac* 6949, *De Abraham* 6947;
  **Bernardo** *De diligendo Deo* 11196 (`BerCla.DeDiDe2`), quarta-feira santa 11231
  (`BerCla.InFeIvH`), Natal 11239 (`BerCla.InNaDo`), Purificação 11220, Septuagésima 11222.
- **Corpus Thomisticum inteiro** já baixado (579 páginas) em
  `…/94b210f9-de88-4ff1-a06d-f01e9346d6d5/scratchpad/n12/ct/`: buscar ali antes de baixar de novo.
  Atenção ao filtrar títulos: «I q. 12» casa com o fim de «I-II q. 12» (comparar o título inteiro).
- **Santo Ambrósio comentou o Sl 35 (36)**: *Explanatio in Ps. 35*, PL 14, 952D–966C (texto 6956,
  depois da do Sl 1; `grep -n "IN PSALMUM XXXV ENARRATIO"`). Para os Sl 36–40, 43, 45, 47, 48, 61,
  começar por ele.
- Na **edição Morin** (Jerônimo), os *Tractatus* e a homilia de Natal citam muito os salmos; achar
  pelas notas de rodapé de Morin («Ps. 35, 7») no `_djvu.txt` com os espaços normalizados e a
  hifenização desfeita, e ler o texto ~2000 caracteres antes da nota.
- Com o Corpus Corporum rápido (20/10), listar as obras de um autor (`navigate.php?load=/38/<autor>`)
  e baixar um texto levou segundos. No XML das obras, o `<idno>` da obra vem logo depois do `<name>`
  que segue o bloco `</corpora>`.
- Temas fortes nos latinos para os salmos com «embriaguez», «torrente» e «fonte»: Cassiodoro,
  Ambrósio, Gregório (*Hom. in Ez.* I, 10, 7), Bernardo (*De diligendo Deo* 33), Ricardo de São
  Vítor, Tomás; para «na tua luz veremos a luz», o *lumen gloriae* de Tomás (*Suma* I, q. 12, a. 2 e
  5) e Isaac de Stella, Sermão 26.

## Por livro

O que é de um livro só (quem comenta que capítulo, o que se achou em cada um) fica no mapa do livro: `numeros.md`, `salmos.md`, `paulo.md`. Aqui ficam o acesso às fontes e o que vale para a Bíblia inteira (20/10/2026).
