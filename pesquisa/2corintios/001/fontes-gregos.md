# Padres gregos e orientais sobre as cartas de São Paulo: onde está o texto

Primeiro uso: 2Cor 1, 2026-10-18 (`relatorio-gregos.md`). Para juntar depois a `../../fontes/gregos.md`.
Padrão do khazarzar: `http://khazarzar.skeptik.net/pgm/PG_Migne/<Pasta do autor>/<Obra>.pdf` (espaços como `%20`);
converter com `../../ferramentas/gregos-limpar.py`. Marcadores «[PG n, m]» = começo da coluna m da PG n (nas obras em
edição moderna, é a numeração da edição).

## Comentários contínuos

| Autor | Obra | PG / edição | Cobre | Onde | Como achar o capítulo |
|---|---|---|---|---|---|
| São João Crisóstomo | Homilias sobre **Romanos** (32), **1 Cor** (44), **2 Cor** (30), **Gl** (comentário), **Ef** (24), **Fl** (15), **Cl** (12), **1–2 Ts** (11 + 5), **1–2 Tm** (18 + 10), **Tt** (6), **Fm** (3), **Hb** (34) | PG 60–63 (2 Cor: PG 61, 381–610) | todas as cartas, versículo por versículo; cada homilia acaba numa exortação moral longa | `John%20Chrysostom_PG%2047-64/In%20epistulam%20ii%20ad%20Corinthios.pdf` (e `…i%20ad%20Corinthios`, `…ad%20Romanos`, `…ad%20Ephesios`, `…ad%20Galatas%20commentarius`, `…ad%20Hebraeos` etc.) | cada homilia abre com o lema: buscar «ΟΜΙΛΙΑ Δʹ» e o primeiro versículo. 2 Cor: hom. 1 = 1,1-5; 2 = 1,6-11; 3 = 1,12-22; 4 = 1,23–2,4; 5 = 2,5-17 (seguir o lema das outras). O PDF às vezes erra o número («ΟΜΙΛΙΑ Ιʹ» por Γʹ) e põe um marcador de coluna adiantado no fim da homilia. Já convertido inteiro no cache `94b210f9-…\scratchpad\g12\txt\` (`John2__In%20epistulam%20ii%20ad%20Corinthios.txt`). Tradução antiga: NPNF I/11–13. |
| Teodoreto de Ciro | *Interpretatio in xiv epistulas sancti Pauli* | PG 82 (2 Cor: 375 ss.) | todas, versículo por versículo, breve | **não está no khazarzar**. OCR da PG 82: `archive.org/details/patrologiae_cursus_completus_gr_vol_082` (grego legível, com κ→χ e β→δ/θ; o latim sai em letras gregas) e `…/bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1859_82` (latim legível, grego ilegível) | `_djvu.txt` dos dois; buscar o lema sem acentos (trocar κ por [κχ]) e, no outro, o latim da Vulgata. Grego e latim em colunas paralelas: o grego fica numa coluna por página (2Cor 1: 377, 380, 381, 384, 385). Cabeçalho «INTERPRETATIO EPIST. II AD COR. CAP. I». |
| São João Damasceno | *Commentarii in epistulas Pauli* | PG 95 (2 Cor: 708 ss.) | todas | `John%20of%20Damascus_PG%2094-96/Commentarii%20in%20epistulas%20Pauli.pdf` (cache: `John2__Commentarii%20in%20epistulas%20Pauli.txt`; o prefixo «John2» do cache serve a Crisóstomo e a Damasceno) | «ΕΙΣ ΕΠΙΣΤΟΛΗΝ ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ Βʹ. ΚΕΦΑΛ. ΠΡΩΤΟΝ.». **É resumo quase literal de Crisóstomo**: só vale para registro. |
| São Cirilo de Alexandria | fragmentos de cadeia sobre **Rm**, **1 Cor**, **2 Cor**, **Hb** | ed. Pusey, *In D. Joannis Evangelium*, vol. III (Oxford 1872; 2 Cor: pp. 320 ss.); PG 74 | trechos escolhidos; cristologia e Trindade | `Cyril%20of%20Alexandria_PG%2068-77/Fragmenta%20in%20sancti%20Pauli%20epistulam%20ii%20ad%20Corinthios.pdf` (e `…i%20ad%20Corinthios`, `…ad%20Romanos`, `…ad%20Hebraeos`) | «ΤΟΜΟΣ Α ΛΟΓΟΣ Β.» + lema; números soltos = páginas de Pusey. 2Cor 1 = livro I, discursos 1–2 (Pusey III, 320–327). |
| Dídimo, o Cego | fragmentos de cadeia sobre **Rm**, **1 Cor**, **2 Cor**, **Hb** | ed. K. Staab, *Pauluskommentare aus der griechischen Kirche* (Münster 1933): 2 Cor pp. 14–44 (até 2Cor 13) | muitos versículos; 2Cor 1: vv. 1-16 e 23-24 | `Didymus%20the%20Blind_PG%2039/Fragmenta%20in%20epistulam%20ii%20ad%20Corinthios.pdf` | «2 Kor 1,3» antes de cada fragmento; números soltos = páginas de Staab. **Edição moderna: citação curta.** |
| Severiano de Gábala | fragmentos de cadeia sobre todas as cartas | ed. Staab (1933): 2 Cor pp. 278–298 | glosas curtas, versículo por versículo | `Severianus_PG%2065/Fragmenta%20in%20epistulam%20ii%20ad%20Corinthios.pdf` (e um por carta) | «2 Kor 1,21–22» antes de cada glosa. Citação curta. |
| Ecumênio | fragmentos de cadeia sobre todas as cartas | ed. Staab (1933): 2 Cor pp. 444–446 | poucas glosas (2Cor 1: só v. 9) | `Oecumenius_PG%20118-119/Fragmenta%20in%20epistulam%20ii%20ad%20Corinthios.pdf` | «2 kor 5,17». O comentário completo de «Ecumênio» (PG 118–119) não está no khazarzar. |
| Orígenes | *Comentário a Romanos* (latim de Rufino e fragmentos gregos); fragmentos sobre **1 Cor**, **Ef**; homilias sobre **Hb** | PG 14; ed. modernas | Rm inteiro (latim), o resto em fragmentos | `Origenes_PG%2011-17/Commentarii%20in%20epistulam%20ad%20Romanos.pdf`, `…Fragmenta%20ex%20commentariis%20in%20epistulam%20i%20ad%20Corinthios.pdf`, `…ad%20Ephesios.pdf` | nada sobre 2 Cor. |
| Teodoro de Mopsuéstia | fragmentos (Staab) e comentário às cartas menores (latim) | — | — | não usar (condenado em 553) | |
| Teofilato de Ocrida | *Expositio in epistulas Pauli* | PG 124–125 | todas; resume Crisóstomo | não está no khazarzar; procurar a PG 124 no Internet Archive (`patrologiae_cursus_completus_gr_vol_124`, se existir, ou a busca `title:(patrologiae cursus completus) AND volume:124`) | escritor eclesiástico; só se acrescentar. |
| Santo Efrém | comentário às cartas de Paulo (conservado em armênio) | tradução latina dos mequitaristas, Veneza 1893 (2 Cor: pp. 85 ss.) | todas as cartas (com 3 Coríntios apócrifa), glosas breves | `archive.org/details/commentariiinepi00ephruoft` (`_djvu.txt`, OCR ruim: corrigir à mão) | título «AD CORINTHIOS SECUNDA»; o latim segue o texto siríaco. Domínio público. |
| Cadeia de Cramer | *Catenae Graecorum Patrum in Novum Testamentum*, vol. V (1 e 2 Cor), 1844 | — | Crisóstomo, Severiano, Teodoreto, Cirilo, Dídimo em cadeia | `archive.org/details/catenaegraecorum05cramuoft` (e `…01`–`…08`) | **OCR do grego inutilizável** (letras latinas). Ver as imagens só se for preciso conferir uma atribuição. |

## Obras que citam muito as cartas (para os versículos marcantes)

| Autor | Obra | Onde | Nota |
|---|---|---|---|
| São João Crisóstomo | *Sobre o sacerdócio* | `John%20Chrysostom_PG%2047-64/De%20sacerdotio.pdf` (ed. Malingrey: «[PG 2, 3]» = livro II, cap. 3; PG 48) | a autoridade pastoral (2Cor 1,24 em II, 3) |
| São João Crisóstomo | catequeses batismais | `…/Catechesis%20ultima%20ad%20baptizandos.pdf` (ed. Papadopoulos-Kerameus 1909; números soltos = páginas); `…/Ad%20illuminandos%20catecheses.pdf` (PG 49); `…/Catecheses%20ad%20illuminandos.pdf` (Wenger, edição moderna) | unção, selo, crisma; a *Ultima* cita 2Cor 1,21 |
| São Cirilo de Jerusalém | *Catequeses*; *Mistagógicas* | `Cyrillus%20Hierosolymitanus_PG%2033/Catecheses%20ad%20illuminandos.pdf`, `…/Mystagogiae.pdf` (Reischl–Rupp) | Myst. 3 = o crisma; a tradição dá as Mistagógicas a Cirilo, alguns a João de Jerusalém |
| São Gregório Nazianzeno | *Discurso 40* (batismo), *31* (Espírito) | `Gregory%20of%20Nazianzus_PG%2035-38/In%20sanctum%20baptisma.pdf`, `…/De%20spiritu%20sancto.pdf` | o selo (40, 15–18) |
| São Basílio | *Sobre o Espírito Santo* | não está no khazarzar: ed. Johnston (1892), `archive.org/details/bookofsaintbasil00basi` (OCR com lixo de acentos, mas legível) | o penhor (15, 36), o selo e a unção |
| Santo Atanásio | *Cartas a Serapião* | `Athanasius%20the%20Great%20of%20Alexandria_%20PG%2025-28/Epistulae%20quattuor%20ad%20Serapionem.pdf` | o Espírito unção e selo (I, 23), com 1Jo 2 e Ef 1 |
| Santo Epifânio | *Panarion* 42 (Marcião) | `Epiphanius_PG%2041-43/Panarion.pdf` (ed. Holl: «[PG 2, 174]» = vol. II, p. 174) | os escólios e refutações do «Apóstolo» de Marcião passam por todas as cartas (2 Cor era a 3ª no cânon dele): um achado por versículo que Marcião manteve |
| São Cirilo de Alexandria | *Thesaurus*; *Comentário a João* | `Cyril%20of%20Alexandria_PG%2068-77/Thesaurus%20de%20sancta%20consubstantiali%20trinitate.pdf` (PG 75); `…/Commentarii%20in%20Joannem.pdf` (Pusey) | o *Thesaurus* usa as cartas contra os arianos, versículo a versículo |
| Orígenes | *Exortação ao martírio* | `Origenes_PG%2011-17/Exhortatio%20ad%20martyrium.pdf` (Koetschau; números = capítulos) | 2Cor 1,5-12 nos caps. 21 e 42 |

## Cuidados

- As **leituras do texto** variam entre os Padres (2Cor 1,12 ἁπλότητι/ἁγιότητι; 1,20 «ἐν αὐτῷ» ou «δι' αὐτοῦ τὸ
  Ἀμήν»): o achado traduz o que o Padre leu.
- **Pseudo-Crisóstomo** que aparece nas buscas das cartas: *De capto Eutropio* (PG 52, 395 ss.), duvidoso; os
  *Eclogae* e a *Synopsis* repetem trechos autênticos.
- Busca rápida em todo o cache: `t.translate({ord(c): letra_base})` (ver `../../fontes/gregos.md`, Sl 35); para
  ~1 300 textos leva cerca de um minuto. Os corpora convertidos estão em `…\94b210f9-…\scratchpad\g12\txt\`,
  `…\dd91be4b-…\scratchpad\g13\txt\` e `…\f1cb729b-…\scratchpad\txt\` (fora do git; conferir se ainda existem).
