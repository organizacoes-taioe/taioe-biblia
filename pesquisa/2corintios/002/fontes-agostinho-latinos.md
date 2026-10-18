# Fontes: Agostinho e Padres latinos antigos, o que se aprendeu de novo em 2Cor 2 (2026-10-18)

Só o que é novo em relação a `../001/fontes-agostinho-latinos.md` (ler aquele primeiro). Para juntar depois a
`../../fontes/agostinho.md` e `../../fontes/latinos.md`.

## 1. Textos novos baixados do Corpus Corporum

`https://mlat.uzh.ch/php_modules/download.php?idno=<texto>&type=file-txt` (16 textos em ~1 min, 8 em paralelo).
Lista de obras de um autor: `https://mlat.uzh.ch/php_modules/navigate.php?load=/38/<autor>&group_by=`; textos de
uma obra: `…load=/38/<autor>/<obra>&group_by=` (o `<idno>` de cada `<text>`).

| autor (idno) | obra (idno da obra) | texto | PL | rendeu em 2Cor 2 |
|---|---|---|---|---|
| Cipriano (878) | Cartas 1 (192) **95**, Cartas 2 (227) **130**, *De baptismate haereticorum* (193) **96**, *De lapsis* (218) **121**, *De unitate* (224) **127**, *De zelo* (225) **128**, *De bono patientiae* (215) **118**, *Testimonia* (21557) **21445**, carta avulsa (191) **94** | | 4 | nada |
| **Paciano de Barcelona** (954) | Cartas a Semproniano (384) **6939** (`cps_2.PacBar.Episto17`); *Paraenesis ad paenitentiam* (385) **6940** | | 13 | **sim**: Carta I, 7 (2Cor 2,10–11 e o perdão do bispo) e Carta III, 18 (o incestuoso absolvido em 2Cor 2,6–10), contra os novacianos |
| Cassiano (1063) | *De institutis* (2545) **7531** | | 49 | nada (o achado é das *Collationes*, 7530: XIV, 17) |
| Cesário de Arles (1172) | Sermões (2857) **7852**, Apêndice (2851) **7846** | | 67 | nada (o Corpus só tem os poucos sermões da PL 67; o grosso de Cesário está no apêndice dos sermões de Agostinho, PL 39) |
| Máximo de Turim (1102) | Homilias (2663) **7652**, Sermões (2664) **7653** (e Tratados 7654, já baixado) | | 57 | só alusões (bom odor; *caupones* de Is 1,22); não usado |

## 2. Onde os latinos comentam 2Cor 2 (padrões de busca que funcionaram)

- **Vetus Latina** de Agostinho no v. 11: «ut non **possideamur** a satana; non enim ignoramus **mentes** ejus» (Vulgata:
  *circumveniamur*, *cogitationes*); v. 6 «sufficit ei **correptio** haec quae fit a **multis**»; v. 7 «ne **majore**
  tristitia absorbeatur»; v. 14 «qui semper **triumphare nos facit** in Christo». Ambrósio lê «nec enim **versutias**
  ejus ignoramus»; Paciano «versutias»; Jerônimo «astutias» (e «cogitationes»); Tertuliano «ne **fraudemur** a
  Satana… **injectiones** ejus» e «abundantiore tristitia **devoretur**». No v. 17, Jerônimo (Carta 120) lê
  «**venundantes** verbum Dei» e Ambrósio fala de **caupones** (taberneiros que põem água no vinho, Is 1,22), as duas
  leituras próximas do grego καπηλεύοντες; a Vulgata e Gregório leem *adulterantes*.
- Busca útil por expressão regular sobre o texto normalizado (`j→i`, `v→u`): `tristitia[^.;]{0,25}absorb`,
  `scripsi[^.]{0,60}lacr[yi]m`, `ignoramus[^.]{0,20}(astuti|uersuti|cogitation|mentes)`, `triumph[^.]{0,30}in christo`,
  `caupon`, `adulter[^.]{0,10}uerbum`, `in persona christi`, `bonus odor`, `odor (mortis|uitae) (in|ad)`.
  O «bonus odor» dá centenas de alusões (sobretudo Agostinho, Ambrósio, Jerônimo, Gregório); as que comentam de fato
  o versículo são as que citam também o v. 16 ou explicam «quis idoneus».
- **Comentários contínuos** que cobrem 2Cor 2: só o **Ambrosiaster** (texto 6985, PL 17, 281A–284D); o resumo de
  Cassiodoro (*Complexiones*, 7917, PL 70, 1339C–D) e o pseudo-Primásio (7897, PL 68, 557B–559B, de base pelagiana,
  não usar). **Jerônimo, Carta 120 a Hedíbia, questão 11** (PL 22, 1000–1004; texto 7132, `HieStr.Episto32`) é uma
  exegese inteira de 2Cor 2,12–17: vale como «comentário» desse trecho.

## 3. augustinus.it: nomes de arquivo conferidos (o site deu 503 em 18/10; usar o Internet Archive)

- Internet Archive: `curl -L "http://web.archive.org/web/2020id_/http://www.augustinus.it/latino/<pasta>/<arquivo>"`;
  sem `-L` volta só o 302 para a cópia datada.
- `esposizioni_salmi/esposizione_salmo_NNN_testo.htm`: NNN ≠ número do salmo, por causa das *Enarrationes* em vários
  sermões. Conferidos: Sl 44 → **059**, Sl 53 → 069, Sl 91 → 112, Sl 92 → **113**, Sl 106 → 131, Sl 128 → 186,
  Sl 129 → 187, Sl 130 → 188, Sl 149 → 207. De 128 a 150 a diferença é fixa (+58): Sl 141 → **199**.
- Sermões (tabela do número → arquivo, `sermmap.json` do scratchpad `7b3b5d55…/scratchpad/2c/`): 4 → 004,
  210 → **266**, 254 → **352**, 273 → **386**, 312 → **444**, 313 → 445.
- Pastas: `contro_parmeniano/contro_parmeniano_N_libro.htm` (N = 1, 2, 3); `predestinazione_santi/predestinazione_santi_libro.htm`;
  `lettere/lettera_NNN_testo.htm`; `commento_vsg/omelia_NNN_testo.htm`. Sem cópia no Archive conferida: `sul_battesimo`,
  `genesi_lettera` (para *De baptismo* e *De Genesi ad litteram*, usar o Corpus).

## 4. Numerações a conferir ao citar

- Gregório, *Regula pastoralis*: a PL repete o «cap. XXIII» na parte III, e o cap. XXIV da PL é o **III, 25** das
  edições modernas (Admonitio 25).
- Ambrósio, *De paenitentia* II: a partir do § 63 a PL dá «cap. VII, alias VIII».
- Gregório, *Homilias sobre Ezequiel*: o arquivo 21412 tem os dois livros; as homilias do livro II trazem «[Al. XIII…]»
  no título (II, 9 = «Al. XXI»).
- Gregório, Cartas (texto 8064): a numeração é a da PL (livro e número); o *Registrum* moderno (Norberg) pode diferir.

## 5. Scripts (scratchpad desta conversa, `c528d87d…/scratchpad/w/`, só no notebook)

`grp.py` (parágrafos com as frases de `pats.txt`, com obra, § e coluna), `ctx.py` (parágrafos com cabeçalhos, § e
coluna), `head.py` (título da obra/sermão/carta acima de um parágrafo), `ex2.py` + `specs2.py` (extrai o `original`
exato, com trechos unidos por « […] », e calcula as colunas), `build.py` (monta o JSON), `textos.py` (gera os `textos/`).
Os textos limpos continuam em `7b3b5d55…/scratchpad/2c/clean/` (707) e `c528d87d…/scratchpad/w/clean2/` (16 novos).
