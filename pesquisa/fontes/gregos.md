# Padres gregos e orientais: catálogo das fontes

Onde está o texto grego de cada comentário aos Salmos (e de algumas obras que os citam muito), com o padrão
para achar o salmo seguinte. Primeiro uso: Sl 33 (LXX 32), 2026-10-17 (`../salmos/033/relatorio-gregos.md`).
Numeração: todos usam a da LXX (o nosso Sl 33 é o «32» deles, λβʹ).

## Onde fica o texto

- **khazarzar** (espelho da «Ψηφιακή Πατρολογία», Univ. do Egeu, 2006, texto digital da PG em PDF):
  `http://khazarzar.skeptik.net/pgm/PG_Migne/<Autor>_PG <vols>/<Obra>.pdf` (espaços como `%20`).
  O índice de cada pasta lista as obras. Os PDFs trazem as colunas da PG como «29.325» (PG 29, 325).
  Exceções, que seguem edições modernas e não têm colunas da PG: Gregório de Nissa (GNO), João Damasceno
  (Kotter), Clemente (Stählin), Cirilo de Jerusalém (Reischl–Rupp; «11.16» = Catequese 11, 16), Dídimo e
  Apolinário (Mühlenberg; Tura), Teófilo.
- Converter e buscar: `../ferramentas/gregos-limpar.py` (PDF → texto limpo, com [PG n, m]) e
  `../ferramentas/gregos-buscar.py` (busca sem acentos; trocar os padrões pelos do capítulo).
- **Conferir colunas e seções**: OCR da PG no Internet Archive (busca: `title:(patrologiae cursus completus)
  AND volume:<n>`; ex.: PG 29 = `patrologicursus22migngoog`). O OCR grego é ruim, mas os números de seção
  e o latim da PG servem. O documentacatholicaomnia.eu tem a PG só em imagem.
- First1KGreek (OpenGreekAndLatin, GitHub) e Perseus não têm os comentários aos Salmos.

## Comentários aos Salmos

| Autor (datas) | Obra | PG | Cobre | Arquivo no khazarzar | Como achar o salmo |
|---|---|---|---|---|---|
| São Basílio (c. 330–379) | *Homiliae in Psalmos* | 29, 209–494 | **Só os Sl 1, 7, 14, 28, 29, 32, 33, 44, 45, 48, 59, 61, 114** (LXX) | `Basilius Caesariensis_PG 29-32/Homiliae super Psalmos.pdf` | título «ΕΙΣ ΤΟΝ ΛΒʹ ΨΑΛΜΟΝ». Espúrias, em PDFs à parte: Sl 28 (outra), 37, 115, 132 (arquivo «CXXII»). |
| Eusébio de Cesareia (c. 263–339) | *Commentaria in Psalmos* | 23 (Sl 1–118); 24, 9–76 (Sl 119–150) | todos, mas inteiro de verdade só nos Sl 51–95; o resto vem de cadeias, com trechos de outros autores | `Eusebius Caesariensis_PG 19-24/Commentaria in Psalmos.pdf` e `…_1.pdf` | «ΨΑΛΜΟΣ ΤΩ ΔΑΥΙΔ ΛΒʹ» ou «ΕΙΣ ΤΟΝ ΨΑΛΜΟΝ … ΛΓʹ» |
| Santo Atanásio (c. 296–373) | *Expositiones in Psalmos* | 27, 60–545 | todos, uma frase por versículo; colchetes = acréscimos de cadeia | `Athanasius the Great of Alexandria_ PG 25-28/Expositiones in Psalmos.pdf` | «ΨΑΛΜΟΣ… ΛΒʹ. Ὑπόθεσις.» (cuidado: os Sl 1, 2, 32… são todos «ἀνεπίγραφος») |
| Santo Atanásio | *Carta a Marcelino* | 27, 12–45 | o uso de cada salmo, por situação (§§ 15–26) e por gênero | `…/Epistula ad Marcellinum de interpretatione Psalmorum.pdf` | os números dos salmos vêm colados à palavra anterior («τὸνλβʹ») |
| Teodoreto de Ciro (c. 393–c. 460) | *Interpretatio in Psalmos* | 80, 857–1997 | todos, versículo por versículo; sentido histórico e espiritual | `Theodoretus of Cyrrhus_PG 80-84/Interpretatio in Psalmos.pdf` | «ΕΡΜΗΝ. ΤΟΥ ΛΒʹ ΨΑΛΜΟΥ.»; versículos «αʹ.», «βʹ, γʹ.» |
| São Cirilo de Alexandria (c. 376–444) | *Expositio in Psalmos* | 69, 717–1273 | muitos salmos, de cadeias (ed. Mai); mistura trechos de Basílio | `Cyril of Alexandria_PG 68-77/Expositio in Psalmos.pdf` | «ΨΑΛΜΟΣ ΛΒʹ.»; siglas «(A f. 175)» depois de cada lema |
| Orígenes (c. 185–254) | *Selecta in Psalmos* | 12, 1053–1686 | muitos salmos, glosas de cadeia; boa parte é de Evágrio | `Origenes_PG 11-17/Selecta in Psalmos.pdf` | «ΨΑΛΜΟΣ ΛΒʹ.»; lemas terminam em «κ. τ. ἑ.» |
| Orígenes | fragmentos (Pitra, *Analecta sacra*) | — | salmo a salmo | `Origenes_PG 11-17/Fragmenta in Psalmos.pdf` | o marcador «[PG 32, 6]» do texto limpo é **salmo 32, v. 6**, não coluna |
| Dídimo, o Cego (c. 313–398) | comentário do papiro de Tura (ed. Gronewald, PTA 4–8, 1968–70) | — | Sl 20–44, com lacunas (Sl 32: v. 13–22) | `Didymus the Blind_PG 39/Commentarii in Psalmos.pdf` | «177 32,13» = página do códice + salmo,versículo. Edição moderna: citação curta. |
| Dídimo | fragmentos de cadeia (ed. Mühlenberg, 1975–78) | — | todos | `Didymus the Blind_PG 39/Fragmenta in Psalmos.pdf` | «290 Ps 32,1bc»; o texto digital perdeu muitos espíritos e acentos |
| Apolinário de Laodiceia | fragmentos (Mühlenberg) | — | muitos | `Apollinaris of Laodicea_PG33/Fragmenta in Psalmos.pdf` | «Ps 32,6». Herege: não usar no site. |
| São João Crisóstomo (c. 349–407) | *Expositiones in Psalmos* | 55, 35–498 | **só os Sl 4–12, 41, 43–49, 108–117, 119–150** | `John Chrysostom_PG 47-64/Expositiones in Psalmos.pdf` | «ΕΙΣ ΤΟΝ ΡΜΘʹ ΨΑΛΜΟΝ». Há PDFs à parte para os Sl 50, 75, 92, 94, 100, 118, 139, 145 e «In Psalmos 101_107» (vários espúrios). |
| São Gregório de Nissa (c. 335–c. 395) | *In inscriptiones Psalmorum* | 44, 432–616 (GNO V) | os títulos dos salmos e a ordem do Saltério; poucas linhas por salmo | `Gregory of Nyssa_PG 44-46/In inscriptiones Psalmorum.pdf` | buscar o primeiro versículo; os marcadores são GNO V |
| Hesíquio de Jerusalém (séc. V) | comentário breve (como Pseudo-Atanásio, *De titulis Psalmorum*); fragmentos | 27, 649–1344; 93 | todos | **não está no khazarzar** (só as homilias) | procurar a PG 27/93 no archive.org (colunas a conferir) |
| Eutímio Zigabeno (séc. XII) | *Commentarius in Psalterium* | 128, 41–1326 | todos (compila os Padres) | **não está no khazarzar** | PG 128 no archive.org |
| Diodoro de Tarso; Teodoro de Mopsuéstia | comentários | — (CCSG 6; Studi e Testi 93) | Sl 1–50; Sl 1–80 | não | edições modernas; Teodoro foi condenado em 553 |

## Obras que citam muito os Salmos (para os versículos famosos)

| Autor | Obra | PG | Arquivo no khazarzar | Nota |
|---|---|---|---|---|
| São Basílio | *Sobre o Espírito Santo* | 32, 67–218 | **não está**; usar a ed. Johnston (Oxford 1892), https://archive.org/details/bookofsaintbasil00basi (OCR; corrigir à mão) | tradução antiga: NPNF II/8 (newadvent.org/fathers/3203.htm) |
| Santo Atanásio | *Contra os arianos*; *Cartas a Serapião* | 26 | `…/Orationes contra Arianos.pdf`; `…/Epistulae quattuor ad Serapionem.pdf` | no PDF das Cartas, as I e II estão juntas no começo |
| São Gregório de Nissa | *Grande catequese*; *Contra Eunômio*; *Refutação* | 45 (GNO) | `Gregory of Nyssa_PG 44-46/…` | marcadores da GNO |
| São Gregório Nazianzeno | Discursos (o 41 é «In pentecosten») | 35–36 | `Gregory of Nazianzus_PG 35-38/…` | um PDF por discurso |
| São Cirilo de Jerusalém | *Catequeses* | 33 | `Cyrillus Hierosolymitanus_PG 33/Catecheses ad illuminandos.pdf` | «11.16» = Catequese 11, 16 |
| São João Damasceno | *Exposição da fé* | 94 | `John of Damascus_PG 94-96/Expositio fidei.pdf` | ed. Kotter (capítulos 1–100) |
| São João Crisóstomo | homilias sobre Mateus, João, as Cartas, Gênesis (sermões) | 47–64 | uma pasta, ~400 PDFs; baixar os grandes e buscar | as homilias citam salmos de passagem, muitas vezes bem |
| Clemente de Alexandria | *Protréptico* | 8 | `Clement of Alexandria_PG 08-09/Protrepticus.pdf` | numeração de Stählin |
| São Teófilo de Antioquia | *A Autólico* | 6 | `Theofilus Antiochieus_PG 06/Ad Autolycum.pdf` | sem colunas |
| Santo Irineu | *Contra as heresias* | 7 | o khazarzar só tem o grego (fragmentos); o latim está na ed. Harvey (1857), https://archive.org/details/sanctiirenaeiep01harvgoog (OCR legível) | o OCR da PG 7 no archive.org é ilegível no latim; tradução antiga: ANF 1 (newadvent) |

## Cuidados que valem sempre

- As **cadeias** misturam autores: o mesmo trecho aparece sob vários nomes. Quando um trecho de Eusébio,
  Orígenes ou Cirilo repetir uma homilia de Basílio, citar Basílio.
- **Traduções antigas** de domínio público dos comentários gregos aos Salmos praticamente não existem; o
  latim da PG (ao lado do grego, no OCR do archive.org) serve para conferir.

## Comentários ao Pentateuco e ao Octateuco (primeiro uso: Nm 12, 2026-10-17, `../numeros/012/relatorio-gregos.md`)

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
- **Crisóstomo**: não comentou Números nem Êxodo (só *Gênesis*, homilias e sermões). Para o Pentateuco, buscar nas
  homilias: com todos os ~400 PDFs baixados, uma busca sem acentos acha as citações em minutos. Cuidado: na
  pasta do Crisóstomo há espúrios (*In Ps. 100*, *Synopsis scripturae*, *Contra theatra*, *Eclogae*, que repetem
  trechos autênticos) e obras em edição moderna (*Catecheses ad illuminandos*, Wenger; *De inani gloria*,
  Malingrey: só citação curta).
- **Nomes repetidos**: Nazianzeno e Nissa têm cada um um `Epistulae.pdf`; ao baixar as duas pastas para o mesmo
  diretório, um sobrescreve o outro. O de Nazianzeno segue Gallay («[PG 77, 8]» = carta 77, § 8).
- **Basílio**: o `Asceticon magnum` traz as *Regras longas* e as *breves* (perguntas «ΕΡΩΤΗΣΙΣ ΚΖʹ»); o
  *Hexaémeron* segue a ed. Giet (SC 26), com «[PG 1, 1]» = homilia 1, § 1.
- Não estão no khazarzar: Teodoreto, *Interpretatio in xiv epistulas Pauli* (PG 82); Teofilato (PG 123–126);
  Ecumênio sobre as cartas (PG 118–119 tem só o Apocalipse em edição moderna). Efrém: nada em grego útil.

## Usos litúrgicos e buscas em massa (primeiro uso: Sl 34 = LXX 33, 2026-10-17, `../salmos/034/relatorio-gregos.md`)

| Fonte | Arquivo no khazarzar | Nota |
|---|---|---|
| São Cirilo de Jerusalém, *Catequeses mistagógicas* | `Cyrillus Hierosolymitanus_PG 33/Mystagogiae.pdf` | ed. Reischl–Rupp: «[PG 5, 20]» = Mistagógica 5, § 20. A 5 descreve a missa de Jerusalém (prefácio, comunhão): procurar ali os salmos cantados na liturgia. |
| *Constituições Apostólicas* (anônima, c. 380) | `Constitutiones Apostolorum_PG 01/Constitutiones Apostolorum.pdf` | edição moderna, sem colunas da PG; a liturgia está no livro VIII (comunhão: VIII, 13). Buscar sem acentos (`ψαλμοσ δε λεγεσθω`): o número do salmo vem colado («ὁ λγἐντῷ»). |
| Orígenes, *Sobre a oração*; *Contra Celso* | `Origenes_PG 11-17/De oratione.pdf`; `…/Contra Celsum.pdf` | Koetschau: «[PG 31, 5]» = cap. 31, § 5; Borret: «[PG 8, 34]» = livro VIII, § 34. |
| São Gregório de Nissa, homilias de festa e de mártires | `Gregory of Nyssa_PG 44-46/De sancto Theodoro.pdf`, `In diem luminum.pdf`, `De iis qui baptismum differunt.pdf` | algumas com colunas da PG (Teodoro: PG 46), outras pela GNO. |

- **Basílio, homilia sobre o Sl 33 (LXX)**: PG 29, 349–388, logo depois da do Sl 32 no mesmo PDF; 14 seções, cujos números só se
  leem no OCR da PG 29 (o OCR perdeu a coluna da seção 3). As homilias de Basílio comentam o salmo inteiro: usar sempre que existam.
- **Eusébio** para no meio de alguns salmos (no Sl 33, no v. 10): conferir até onde vai antes de contar com ele.
- **Atanásio, *Expositiones***: no Sl 33 várias glosas são idênticas às de Teodoreto e de Cirilo, **sem colchetes** no PDF; comparar
  sempre com Teodoreto antes de atribuir a Atanásio.
- **Dídimo (Tura)** cobre o Sl 33 inteiro (págs. 184–203; ed. Gronewald, PTA 8); a lacuna é só no Sl 32, 1–12.
- **Busca em massa**: baixar a pasta inteira de um autor (curl no índice da pasta, um PDF por linha) e converter com `gregos-limpar.py`
  leva tempo: Crisóstomo (~400 PDFs, ~130 MB) passa de 40 minutos; começar em segundo plano logo no início. Ao decodificar os nomes
  dos arquivos, cuidado com `%20` (no Git Bash, `printf '%b'` não converte; o nome saiu com «x20»). Os resultados mais úteis vêm das
  homilias batismais (Nazianzeno 39–40, Basílio 13, Nissa), das de mártires e das catequeses.
- **Jo 19,36**: os gregos ligam «osso não se quebrará» ao cordeiro pascal (Ex 12,46), não ao Sl 33,21 (Cirilo, *Com. a João* e *De
  adoratione*; Crisóstomo, *Hom. 15 sobre 1 Cor*).

## Acréscimos do Sl 35 (LXX 34) (2026-10-17, `../salmos/035/relatorio-gregos.md`)

- **Textos já convertidos, para reaproveitar** (no notebook, fora do git; a pasta temporária pode ser limpa pelo sistema: procurar
  antes de baixar), em `C:\Users\geren\AppData\Local\Temp\claude\C--Users-geren-OneDrive-Documentos-Onedrive-do-Gere-Software-MEU-taioe\`:
  - `f1cb729b-…\scratchpad\txt\`: os comentários aos Salmos inteiros (`eusebio-ps`, `teodoreto-ps`, `atanasio-exp`, `atanasio-marc`,
    `cirilo-ps`, `origenes-sel`, `origenes-frag`, `didimo-tura`, `didimo-frag`, `apolinario-frag`, `nissa-inscr`, `basilio-hps`) e
    `cirjer-cat`, `cirjer-myst`, `constapost`; `…\txtall\<autor>\` (Basílio, Nazianzeno, Nissa, Atanásio, Orígenes, Cirilo de
    Alexandria, Teodoreto, Damasceno, Macário; Crisóstomo 285 de 398);
  - `94b210f9-…\scratchpad\g12\txt\` (991 textos: Crisóstomo inteiro, 445; Epifânio, Máximo, Severiano, Ecumênio, Gregórios…);
  - `dd91be4b-…\scratchpad\g13\txt\` (294: Cirilo de Alexandria 68, Eusébio 41, Teodoreto 25, Hesíquio 20 homilias, Melitão,
    Teodoro Estudita, Justino, Procópio, Fócio…). Nomes dos arquivos: `<Autor>__<Obra com %20>.txt`.
  - `54c8dfc5-…\scratchpad\ia\`: o OCR da PG 128 (Eutímio), duas digitalizações.
  - Ali, **`Theodo__Epistulae.txt` é de Teodoro Estudita** (pasta `Theodorus Studita_PG 99`, ed. Fatouros 1992, cartas numeradas),
    não de Teodoreto.
- **Busca rápida em todo o corpus** (~2 000 arquivos em pouco mais de 1 minuto): em vez do laço caractere a caractere de
  `gregos-buscar.py`, montar uma tabela `{ord(c): letra_base_minúscula}` para os caracteres do arquivo e usar `t.translate(tabela)`;
  cada caractere vira exatamente um, e as posições do texto sem acentos valem no original.
- **Eutímio Zigabeno** (PG 128): OCR em https://archive.org/details/patrologiaecurs261unkngoog (`…_djvu.txt`); buscar
  «PSALMUS XXXIV» (algarismos romanos da Vulgata). O latim é legível; o grego sai com letras latinas e precisa ser refeito à mão,
  com o latim ao lado. Compila sobretudo Teodoreto. Lista de volumes da PG: `archive.org/advancedsearch.php?q=title:(patrologiae
  cursus completus) AND volume:<n>&fl[]=identifier&output=json`.
- **Dídimo (Tura)**: o Sl 34 ocupa as págs. 203–230 (PTA 8); faltam as págs. 214–216. O Sl 35 começa na pág. 230.
- **Eusébio, PG 23**: nos salmos que só vêm de cadeias, a primeira parte do comentário pode trazer fragmentos que Mühlenberg dá a
  Dídimo (no Sl 34: frags. 331–333). Conferir com `didimo-frag` antes de atribuir. O mesmo vale para as *Selecta* de Orígenes.
- **Teodoreto**: quando divide um versículo em dois, os números seguintes do PDF ficam adiantados (no Sl 34, a partir do v. 17).
- **Cirilo, *Expositio***: trechos entre colchetes na PG têm origem não explicada no PDF; tratar como atribuição menos segura.
- **Usos achados fora dos comentários**: Nazianzeno, *Discurso* 14 (`De pauperum amore.pdf`) e 17 (`Ad cives Nazianzenos.pdf`);
  Cirilo, *Homilias pascais* (`Epistulae paschales sive Homiliae paschales.pdf`; cada uma é um «ΛΟΓΟΣ»); Melitão, *Sobre a Páscoa*
  (`Melito of Sardis_PG 05/De pascha.pdf`, edição moderna).
- **Espúrios que aparecem nas buscas** (não usar): Pseudo-Atanásio, *Homilia in sanctos patres et prophetas* (PG 28, 1061 ss.);
  Pseudo-Crisóstomo, *In illud Ignem veni mittere* (PG 62), *De circo* (PG 59), *De paenitentia et in lectionem de Davide* (PG 64);
  *Testimonia* atribuídos a Epifânio.
- **Teodoro de Mopsuéstia** (Sl 1–80, ed. Devreesse 1939) e **Diodoro** não estão no khazarzar; Teodoro foi condenado em 553 e Diodoro
  ficou suspeito pelo mesmo motivo: não entram no site.
## Cartas de São Paulo

Tudo em `paulo.md` (o mapa das cartas: as obras de cada carta, a tabela das homilias de Crisóstomo e a pré-pesquisa de 2Cor 3–13).

## Acréscimos do Sl 36 (LXX 35) (2026-10-20, `../salmos/036/relatorio-gregos.md`)

- **Dídimo (Tura)**: o Sl 35 LXX ocupa as págs. 230–240, inteiro; faltam as págs. 241–244 (começo do Sl 36 LXX, que retoma no v. 9 na pág. 245).
- **Crisóstomo** não comentou o Sl 35 LXX; **Basílio** também não. Para os versículos famosos, a busca no corpus inteiro rende mais
  que os comentários (no Sl 36: 13 padrões, ~420 ocorrências, 2 min com a tabela `translate`).
- **Unicode**: os textos convertidos misturam oxia (U+1F71…) e tonos (U+03AC…); antes de procurar uma frase digitada ou de fazer
  `replace`, normalizar com `unicodedata.normalize('NFC', …)`. Na mesma linha: `python -I` ignora `PYTHONIOENCODING`; nos scripts, pôr
  `sys.stdout.reconfigure(encoding='utf-8')`; e o Python do Windows não entende caminhos `/c/...` no `glob` (usar `C:/...`).
- **Basílio, *Sobre o Espírito Santo***: o OCR de Johnston (`bookofsaintbasil00basi_djvu.txt`) traz as seções («47.») e, à margem, as
  referências bíblicas («Ps. xxxvi.»); buscar por `Ps\. xxxvi` ou pela palavra grega. Grego ruim: refazer à mão com a PG 32.
- **Nazianzeno**: no khazarzar, `De spiritu sancto.pdf` é o *Discurso* 31 em edição moderna (sem colunas; seções 1, 2, 3…; Or. 31, 3 =
  PG 36, 136); `In Aegyptiorum adventum 1.pdf` (o «1» faz parte do nome) é o *Discurso* 34, com colunas da PG.
- **Basílio, *Asceticon***: há `Asceticon magnum.pdf` e `Asceticon magnu1.pdf`; as *Regras breves* (PG 31, 1052–1305) estão no
  segundo, com perguntas «ΕΡΩΤΗΣΙΣ ΠΑʹ» (= 81). *Contra Eunômio* IV–V (PG 29, 672 ss.) é espúrio.
- **Epifânio**, *Panarion*: `Epiphanius_PG 41-43/Panarion.pdf` segue Holl (GCS): «[PG 3, 200]» = vol. III, p. 200; cada heresia começa
  com «Κατὰ … ˉμˉθ, τῆς δὲ ἀκολουθίας ˉξˉθ» (= heresia 69) e os capítulos vêm como «54.».
- **Hesíquio**: `Hesychius_PG 93/` tem só as homilias de festa (ed. Aubineau, edição moderna: citação curta); o comentário aos Salmos não.
- **Cirilo de Alexandria** cita o par «fonte da vida / torrente das delícias» (Sl 35,9–10 LXX) em quase toda obra (*Com. a João*,
  *Glaphyra*, *De adoratione*, *Homilias pascais*, Isaías, Doze Profetas): sempre Cristo que rega com o Espírito. A glosa do v. 10 na
  *Expositio* de Mai vem do *Tesouro* 4 (PG 75, 40): as glosas de Mai podem vir de outras obras do próprio Cirilo.
- **Teodoreto, *História eclesiástica***: no khazarzar segue Parmentier (sem colunas); traz cartas de Alexandre de Alexandria e de Ário.

## Por livro

O que é de um livro só (quem comenta que capítulo, o que se achou em cada um) fica no mapa do livro: `numeros.md`, `salmos.md`, `paulo.md`. Aqui ficam o acesso às fontes e o que vale para a Bíblia inteira (20/10/2026).
