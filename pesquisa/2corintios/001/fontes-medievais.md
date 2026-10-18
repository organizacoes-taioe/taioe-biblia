# Comentários medievais e do início da era moderna às cartas de São Paulo: onde estão

Para os próximos capítulos de Paulo (grupo «medievais», séc. VIII–XVII). Primeiro uso: 2Cor 1,
2026-10-18 (`relatorio-medievais.md`). Juntar depois em `../../fontes/latinos.md`.

## 1. Corpus Corporum (PL de Migne): os comentários paulinos contínuos

Uma chamada por texto: `https://mlat.uzh.ch/php_modules/download.php?idno=<texto>&type=file-txt`
(cada um levou segundos em 18/10). Scripts: `cc.py` (works/text/dl), `clean.py` (põe `[col. …]` e
as notas entre parênteses), `cols.py <texto> <col.ini> <col.fim>` (recorta por colunas e mostra o
título acima); estão no scratchpad da conversa de 18/10, refazer é rápido (ver `../../fontes/latinos.md` §0).

| autor (idno) | obra | texto | PL | cobre | achar uma carta |
|---|---|---|---|---|---|
| São Tomás de Aquino | *Super epistolas S. Pauli* | Corpus Thomisticum: `c1c` (1Cor), `c2c` (2Cor), `cgl`, `cep`, `cpl`, `ccl`, `c1t`, `c2t`, `ct1`, `ct2`, `cro0x`/`cro1x` (Rm), `che01`/`che11` (Hb) | — | todas (falta 1Cor 7,10–10,33) | `TITLE="Super II Cor., cap. 1 l. 1"`; cada **lição é um parágrafo só**, com o número [87693]…; sem numeração Marietti |
| São Bruno, o Cartuxo (2035) | *Expositio in epistolas Pauli* (5448) | **10482** (`BruCar.ExInEpP`) | 153 | todas | `grep -n "EPISTOLA II AD CORINTHIOS"`; capítulo = `CAPUT PRIMUM`… (texto da Vulgata entre «» e depois `EXPOSITIO`) |
| «Haimo de Halberstadt» = Haimo de Auxerre (1543) | *Expositio in D. Pauli epistolas* (4056) | **9079** (`HayHal.ExInDPa`) | 117 | todas | `IN EPISTOLAM II AD CORINTHIOS`, `CAPUT II.` |
| Atão de Vercelli (1675) | *Expositio epistolarum S. Pauli* (4411) | **9440** (`AttVer.ExEpSPa`) | 134 | todas | `EPISTOLA SECUNDA AD CORINTHIOS`; os capítulos só aparecem como nota `(CAP. II.)`: procurar o marcador `[n]` |
| Sedúlio Escoto (1478) | *Collectanea in omnes B. Pauli epistolas* (3738) | **8761** (`SedSco.CoInOmB`) | 103 | todas | `III. IN EPISTOLAM II AD CORINTHIOS`; breve, quase todo Ambrosiaster e Pelágio |
| Lanfranco (1994) | *Commentarius in omnes epistolas Pauli* (5330) | **10364** (`LanCan.CoInOmE`) | 150 | todas | `AD CORINTHIOS SECUNDA`; texto com glosas e depois `COMMENTARIUS`: só LANFR. é dele (AMBROS. = Ambrosiaster) |
| Hervé de Bourg-Dieu (2262), como pseudo-Anselmo | *Commentaria in epistolas Pauli* (6141) | **11182** (`HerBur.CoInEpP2`) | 181 | todas | `IN EPISTOLAM II AD CORINTHIOS` (linha ~20420); o mais extenso; copia Ambrosiaster e Gregório sem aviso |
| Pedro Lombardo (2327) | *Collectanea in epistolas Pauli* 1 (6406) e 2 (6419) | **11454** (Rm, 1Cor), **11467** (2Cor em diante; `PetLom.CoInEpP4`) | 191–192 | todas | `IN EPISTOLAM II AD CORINTHIOS`, `VERS. 1-5.--`; siglas [Ambrosius], [Augustinus] |
| Hugo de São Vítor (escola) (2230) | *Quaestiones in epistolas Pauli* (6026) | **11066** (`HuDeSVi.QuInEpP`) | 175 | todas | `III. IN EPISTOLAM II AD CORINTHIOS`, `QUAESTIO I.`… |
| «Hugo de S. Victore?» (2229) | *Allegoriae in NT*, liv. VI–IX = Paulo (dentro de *Posteriores excerptiones*, 6013) | **11052** (`AuInHuD.PosExc`) | 175 | Rm–… | `LIBER OCTAVUS. IN EPISTOLAM PAULI AD CORINTHIOS SECUNDAM` (col. 919) |
| Rábano Mauro (1518) | *Enarrationes in epistolas B. Pauli* (3900) | **8923** (`RabMau.EnInEpB`) | 111 | **só Romanos** | a parte de PL 112 (1Cor–Hb) **não está** no Corpus Corporum |
| Atão, Bruno, Haimo, Hervé… | — | — | — | — | Dica: a passagem de um versículo se acha mais depressa pela frase da Vulgata (`Pater misericordiarum`, `testimonium conscientiae`) do que pelos títulos |

Outros ids úteis (2Cor 1): Guerrico de Igny (2276) *Sermones per annum* **21443** (`GueIgn.SePeAn`);
Isaac de Stella (2333) *Sermones* **11493**; Aelredo (1030) *Sermones de tempore* **11501**,
*Speculum caritatis* **11502**; Pedro de Celle (2375) *De conscientia* **11620**, *Sermones* **11625**;
Hugo de São Vítor *Soliloquium de arrha animae* **11090**, *Summa sententiarum* **11091**; Ricardo de
São Vítor *Explicatio aliquorum passuum difficilium Apostoli* **11549**; Santo Anselmo (1938)
*Epistolae* **10620**, *Homiliae* **10622**, *Meditationes* **10626**. Bernardo: ids em
`../../fontes/latinos.md` §6–9 (Natal = 11239, Todos os Santos = 11236, Anunciação = 11223,
*De moribus* = 11200, Cântico = 11258, Cartas = 21392).

Notas de Migne para Paulo: `(II Cor. I, 12)` em Bernardo, Bruno de Segni, Guerrico; **sem
versículo**, `(II Cor. I)`, em Ruperto, Haimo (Salmos), Pedro Damião, Aelredo, Ricardo, as
*Allegoriae*. Cuidado: as notas erram (Bruno de Segni dá `(I Cor. I, 8)` para 2Cor 1,8; Pedro Damião
`(II Cor. I)` para 1Cor 10,4).

## 2. Não está na PL do Corpus Corporum

- **Glosa ordinária** (Paulo): não consultada. Pistas: a ed. de Estrasburgo (Rusch, 1480/81) em
  fac-símile e o projeto Gloss-e (IRHT); a PL 114 (Walafrido) em imagem.
- **Rábano**, 1Cor–Hb (PL 112): só em imagem (archive.org / Google Books, PL 112).

## 3. Fora da PL (archive.org)

- **Cornélio a Lápide**, ed. Vivès/Crampon: **t. XVIII** (`commentariainscr18lapi`, 1868) = Romanos,
  1 e **2 Coríntios** (2Cor 1 nas pp. 420–425; linhas 68042–68883 do `_djvu.txt`); o t. XIX
  (`commentariainscr19lapi`) segue com as outras cartas (não conferido). Página impressa P = imagem
  `https://archive.org/download/commentariainscr18lapi/page/n(P+23).jpg` (3300×5000, boa); link para o
  leitor `https://archive.org/details/commentariainscr18lapi/page/<P>/mode/1up`. O OCR é bom, mas
  mistura as colunas e as notas de Crampon (numeradas (1), (2), que não são de Lápide); achar o
  capítulo com `grep -n "CAPUT SECUNDUM\|COMMENTARIA IN II EPISTOLAM"`. Em Paulo Lápide é mais
  curto que no AT (6 páginas para 2Cor 1). Tradução inglesa (Mossman, *The Great Commentary*, vol. 8 =
  2Cor e Gl, `TheGreatCommentaryOfCorneliusALapideV8`): só para conferir.
- **Belarmino**, *Opera omnia*, ed. Fèvre (Vivès, 1870–1874): `operaomnia03bell` = t. III
  (*De sacramentis*: *De effectu sacramentorum* II, 20 cita 2Cor 1,21-22, p. 122 = imagem n125);
  `operaomnia08bell` (*De justificatione*), `operaomnia09bell` (*Conciones*). OCR ruim no t. III
  (espaços duplos e letras trocadas): procurar com `grep -E "unxit +nos"`; transcrever da imagem.
- **São Boaventura**, Quaracchi: `doctorisseraphic04bona` (In IV Sent.), `05bona` (opúsculos e
  *Sermones de rebus theologicis*), `08bona` (opúsculos espirituais), `09bona` (sermões de tempore,
  de santis, de B. Virgine). As notas de rodapé dão a referência como `II. Cor. 1, 12`:
  `tr -s ' ' < arq | grep -n -E "II\.? *Cor\.? *1, *12"`. Boaventura não comentou as cartas de Paulo
  (o comentário atribuído não é dele); só sermões.
- **Santa Catarina de Sena**, *Dialogo* (ed. Fiorilli, 1912): `034CaterinaLibro1912Si073`; nada sobre 2Cor 1.
  As cartas (ed. Gigli, séc. XVIII, `bub_gb_*`) não foram varridas.
- **Tomás de Kempis**: *Imitação* em The Latin Library (`kempis/kempis1.shtml` a `kempis4.shtml`).
- Dionísio Cartuxo (*In omnes B. Pauli epistolas*, *Opera omnia* t. 13) e Nicolau de Lira: não
  procurados.

## 4. Quem vale mais em Paulo (impressão do 2Cor 1)

Tomás (de longe: lição por lição, todas as palavras) > Hervé (extenso, mas copia) ≈ Atão (próprio,
moral, com aplicações à Igreja do seu tempo) > Bruno Cartuxo (glosa contínua, boas frases) > Haimo
(algumas ideias boas) > Sedúlio, Lanfranco, Lombardo (compilação). Para os temas, os sermões de
Bernardo (varrer as 72 obras pela frase da Vulgata) e Lápide (reúne Padres e medievais e acrescenta
aplicações).
