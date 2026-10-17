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
