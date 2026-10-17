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
| Gerhoh de Reichersberg (2330), Ruperto de Deutz (2195), Honório de Autun (2211) | não consultados | | |


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
