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
