# Fontes: Agostinho, Padres latinos e medievais latinos, o que se aprendeu de novo em 2Cor 3 (2026-10-20)

Só o que é novo em relação a `../001/fontes-*.md` e `../002/fontes-*.md` (ler aqueles primeiro). Para juntar
depois a `../../fontes/agostinho.md`, `../../fontes/latinos.md` e `../../fontes/paulo.md`.

## 1. Onde os latinos comentam 2Cor 3 (padrões de busca que funcionaram)

Busca por expressão regular sobre o texto normalizado (minúsculas, `j→i`, `v→u`, notas de Migne tiradas), nos
723 textos limpos dos caches anteriores (`7b3b5d55…/scratchpad/2c/clean/` e `c528d87d…/scratchpad/w/clean2/`):

| v. | padrão | rende |
|---|---|---|
| 2 | `epistola nostra uos estis\|epistola christi` | pouco; quase sempre junto com o v. 3 |
| 3 | `non atramento\|tabulis cordis carn\|cordis carnalibus\|spiritu dei uiui` | muito; o «não com tinta» é aplicado ao **Credo** que se entrega aos catecúmenos (Pedro Crisólogo, Sermões 58 e 60; Jerônimo, *Contra Ioannem* 28; Isidoro, *Etimologias*, livro VI, PL 82, 252B) |
| 5 | `(sufficientes\|idonei) (simus\|sumus) cogitare\|sufficientia nostra (ex\|a) deo` | a Vetus Latina de Agostinho é «**non quia idonei sumus** cogitare aliquid **quasi ex nobismetipsis**»; Orange e Próspero dizem «Ecclesiastica regula est» |
| 6 | `littera (enim )?occidit\|non littera,? sed spiritu` | centenas; Agostinho sozinho, ~60 parágrafos |
| 7–11 | `ministratio (mortis\|damnationis\|spiritus\|iustitiae)\|propter excellentem gloriam\|quod manet,? in gloria` | Agostinho lê «quae **destruitur**» (v. 7) e «id quod **declaratum** est propter excellentem **claritatem**» (v. 10) |
| 13–16 | `uelamen (super\|positum\|in lectione\|manet)\|cum legitur moyses\|conuersus fuerit ad\|auferetur uelamen` | Agostinho lê quase sempre «**cum transieris ad Christum/Dominum**» (v. 16) e «quamdiu legitur Moyses» |
| 17 | `dominus autem spiritus est\|ubi (autem )?spiritus domini,? ibi libertas` | Ambrósio, Agostinho, Hilário (divindade do Espírito); Gregório, Leão, Bernardo (liberdade × medo) |
| 18 | `reuelata facie\|gloriam domini speculantes\|in ea(m)dem imaginem\|a claritate in claritatem\|a gloria in gloriam\|de forma in formam` | Agostinho e Jerônimo leem «**de gloria in gloriam**»; Ambrósio «ad eamdem imaginem **reformamur**»; Jerônimo «gloriam Domini **contemplantes**» (também «speculantes»); Hilário «gloriam Dei **exspectantes** (id est, spectantes)» |

Script: `latinos/srch.py` (busca, grava `hits.json`), `show.py` (contexto), `para.py <texto> <p1> [p2]` (parágrafos
inteiros), `ex.py` + `specs.py` + `run.py` (extrai o `original` exato entre duas frases), `build.py` (JSON),
`textos.py`; no scratchpad desta conversa (`9acafcb3…/scratchpad/latinos/`). Atenção: o cabeçalho que `show.py`
mostra (obra, carta, capítulo) **erra** quando o título começa por número de página (ex.: as Cartas de Jerônimo
65 e 61; o *Contra adversarium legis*, livro II): conferir sempre o título no próprio texto.

## 2. Novos endereços

- **Corpus Thomisticum, *Suma* I-II q. 106** (a lei nova): `https://www.corpusthomisticum.org/sth2106.html`; a. 2 =
  parágrafos [38257]–[38264]. Padrão das questões da I-II: `sth2NNN.html` (NNN = número da questão, com três dígitos).
- **II Concílio de Orange (529)**: não está no Corpus Corporum nem na Wikisource latina (a página «Concilium
  Arausicanum II» está vazia). Texto em F. Maassen, *Concilia aevi merovingici* (MGH, 1893), archive.org
  `conciliaaevimero01maas`, pp. 44–54; o OCR (`_djvu.txt`) tem o cânon 7 na linha ~4352; grafia merovíngia dos
  manuscritos (pertinit, elegire). DS 377 para a numeração moderna.
- **augustinus.it**: 503 de novo em 20/10; o Internet Archive respondeu 429 (muitas consultas). Nomes de pasta
  conferidos no CDX: `spirito_lettera/spirito_lettera_libro.htm`, `contro_avversario/contro_avversario_1_libro.htm`
  e `_2_libro.htm`, `predestinazione_santi/predestinazione_santi_libro.htm`, `trinita/trinita_15_libro.htm`.
  Sermões: 248 = `discorso_345`, **249 = `discorso_346`**, 250 = `discorso_347` (tabela `sermmap.json` de
  `7b3b5d55…/scratchpad/2c/`). Por isso os achados deste capítulo usam o permalink do Corpus Corporum
  (`https://mlat.uzh.ch/browser/<cc_id>`).
- Corpus Corporum, ids usados pela primeira vez: Pedro Crisólogo, Sermões **7597** (`PetChr.Sermon7`; os sermões 57 ss. são a
  entrega do Símbolo); Máximo de Turim, Homilias **7652**; Gregório, *Expositio super Cantica*
  **8105**; Leão, Sermões **7631**; Bernardo, *De gratia et libero arbitrio* **11198**; Ricardo de São Vítor,
  *Benjamin maior* **11527**; Agostinho, *Contra adversarium legis* **7439**, *De utilitate credendi* **7447**,
  *Fragmenta sermonum* **7341** (excertos de Floro de Lião, por capítulo de Paulo: «Florus ad II Cor. III»).

## 3. Numerações a conferir

- Agostinho, *Contra adversarium legis et prophetarum*: o comentário a 2Cor 3,7–16 está no **livro II, cap. 7,
  §§ 24–28** (PL 42, 651–655), não no livro I.
- Bernardo, Sermões sobre o Cântico (texto 11258): o § 5 do Sermão 32 começa na col. 947D (parágrafo 802 do texto limpo).
- Jerônimo, Cartas (texto 7132): a Carta 65 (a Principia, Sl 44) está nas linhas 840 ss.; a Carta 38 (Blesila),
  col. 463–465.
