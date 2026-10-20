# Salmos: mapa das fontes baixadas (pré-pesquisa de 20/10/2026)

Para quem vai pesquisar um salmo: o texto latino dos comentários abaixo já está cortado por salmo em
`salmos/<ccc>/base/<autor>-<obra>.md` (ccc = número **hebraico**, 3 dígitos), com o índice em
`salmos/<ccc>/BASE.md` (gerado por `ferramentas/base-indice.py`). Este arquivo diz **o que** existe, **o que
falta** e **que armadilhas** já apareceram. Os catálogos por grupo (`latinos.md`, `agostinho.md`,
`gregos.md`, `orientais.md`, `modernos.md`) continuam valendo para o resto (citações em outras obras,
sermões, etc.). Esta leva cobre os **autores latinos até o séc. XVII**; gregos, orientais e modernos têm
os próprios scripts em `ferramentas/base/` (`grc-*`, `ori-*`, `mod-*`) e não estão na tabela abaixo.

Os Sl 33 a 36 (hebr.) ficaram de fora desta leva (feitos ou em andamento nas conversas deles).

## 1. Numeração: hebraico (pasta `salmos/<ccc>`) × Vulgata/LXX (a dos autores)

| hebraico | Vulgata/LXX | observação |
|---|---|---|
| 1–8 | 1–8 | igual |
| 9–10 | 9 | os dois hebraicos são **um só** na Vulgata: as duas pastas recebem o **mesmo** texto |
| 11–113 | 10–112 | hebraico = Vulgata + 1 |
| 114–115 | 113 | idem: duas pastas, mesmo texto |
| 116 | 114 e 115 | o arquivo traz os dois, com subtítulos «## Salmo 114 (Vulgata)» e «## Salmo 115 (Vulgata)» |
| 117–146 | 116–145 | hebraico = Vulgata + 1 |
| 147 | 146 e 147 | idem Sl 116: dois subtítulos |
| 148–150 | 148–150 | igual |

O campo `Passagem` de cada arquivo diz a numeração da Vulgata. `ferramentas/base/lat_comum.py` tem as
funções `vulgata_de_hebraico()` e `hebraicos_de_vulgata()`. Cuidado com o Sl 118 (Vulgata) = 119 hebr.
(176 versos, 22 letras): é o maior trecho de todas as obras (Agostinho 269 KB, Lombardo 250 KB, Ambrósio
840 KB). Os textos citam os salmos pelo número da Vulgata, inclusive nas notas de Migne («Psal. XXXII»).

## 2. Tabela-mestra: obra → salmos que cobre → script que a baixa

Todos os scripts estão em `pesquisa/ferramentas/base/`, usam a biblioteca comum `lat_comum.py` (baixa uma
vez para `pesquisa/cache/base/`, fora do git; corta; grava o cabeçalho do `COMO-PESQUISAR.md`) e rodam
assim: `python -I -X utf8 pesquisa/ferramentas/base/lat-<obra>.py [--so 37 38 ...]` (números hebraicos;
sem `--so`, faz todos). Contagens de 2026-10-20, sem os Sl 33–36 hebr.

| obra (arquivo em `base/`) | salmos que cobre | arquivos | tamanho | script | de onde vem o texto |
|---|---|---|---|---|---|
| Agostinho, *Enarrationes in Psalmos* (`agostinho-enarrationes-in-psalmos.md`) | todos os 150 (Vulgata) | 146 | 5,2 MB | `lat-agostinho.py` | augustinus.it (via web.archive.org), colunas da PL do Corpus Corporum (7329 e 21385) |
| Cassiodoro, *Expositio Psalmorum* (`cassiodoro-expositio-psalmorum.md`) | todos | 146 | 3,0 MB | `lat-cassiodoro.py` | Corpus Corporum 21404 (PL 70) |
| Arnóbio, o Jovem, *Commentarii in Psalmos* (`arnobio-commentarii-in-psalmos.md`) | todos | 146 | 0,8 MB | `lat-arnobio.py` | CC 21351 (PL 53) |
| São Bruno de Segni, *Expositio in Psalmos* (`bruno-segni-expositio-in-psalmos.md`) | todos | 146 | 1,5 MB | `lat-bruno-segni.py` | CC 10806 (PL 164) |
| São Bruno, o Cartuxo, *Expositio in Psalmos* (`bruno-cartuxo-expositio-in-psalmos.md`) | todos | 146 | 2,3 MB | `lat-bruno-cartuxo.py` | CC 10473 (PL 152) |
| Pedro Lombardo, *Commentaria in Psalmos* (`pedro-lombardo-commentaria-in-psalmos.md`) | todos | 146 | 3,6 MB | `lat-lombardo.py` | CC 11455 (PL 191) |
| Santo Hilário, *Tractatus super Psalmos* (`hilario-tractatus-super-psalmos.md`) | **só** os Sl 1, 2, 9, 13, 14, 51–69, 91, 118–150 (Vulgata) = hebr. 1, 2, 9, 10, 14, 15, 52–70, 92, 119–150 | 58 | 1,5 MB | `lat-hilario.py` | CC 21450 (PL 9) |
| Santo Ambrósio, *Enarrationes in XII psalmos* (`ambrosio-enarrationes-in-xii-psalmos.md`) | **só** Sl 1, 35–40, 43, 45, 47, 48, 61 (Vulgata) = hebr. 1, 36–41, 44, 46, 48, 49, 62 (aqui sem o 36, que ficou de fora da leva: 11 arquivos) | 11 | 0,6 MB | `lat-ambrosio.py` | CC 6956 (PL 14) |
| Santo Ambrósio, *Expositio in Psalmum CXVIII* (`ambrosio-expositio-in-psalmum-118.md`) | só o Sl 118 (Vulgata) = hebr. 119 | 1 | 0,8 MB | `lat-ambrosio.py` (o mesmo) | CC 6966 (PL 15) |
| São Tomás, *Postilla super Psalmos* (`tomas-postilla-super-psalmos.md`) | **só** Sl 1–54 (Vulgata) = hebr. 1–55 | 51 | 1,2 MB | `lat-tomas.py` | corpusthomisticum.org (cps01 … cps52) |
| pseudo-Jerônimo, *Breviarium in Psalmos* (`pseudo-jeronimo-breviarium-in-psalmos.md`) | todos | 146 | 1,3 MB | `lat-pseudo-jeronimo.py` | CC 7183 (PL 26) |
| «Haimo de Halberstadt», *Commentaria in Psalmos* (`haimo-commentaria-in-psalmos.md`) | todos | 146 | 1,5 MB | `lat-haimo.py` | CC 9073 (PL 116) |
| pseudo-Beda, *De Psalmorum libro exegesis* (`pseudo-beda-de-psalmorum-libro.md`) | todos | 146 | 2,4 MB | `lat-pseudo-beda.py` | CC 8477 (PL 93) |
| São Roberto Belarmino, *Explanatio in Psalmos* (`belarmino-explanatio-in-psalmos.md`) | todos | 146 | 3,4 MB | `lat-belarmino.py` | archive.org (`operaomnia10bell`, `operaomnia11bell`), OCR |

Total: 1581 arquivos, cerca de 28,5 MB. «CC» = Corpus Corporum (mlat.uzh.ch), idno do texto; baixa-se
`https://mlat.uzh.ch/php_modules/download.php?idno=<n>&type=file-txt` (o texto da Patrologia Latina com as
colunas e as notas de Migne). Em cada salmo, `base/_ausentes-latinos.md` lista as obras acima que **não**
comentam aquele salmo (só Hilário, Ambrósio e Tomás; o Sl 1 é o único com as três presentes).

O que **não** entrou (existe em outros catálogos): São Jerônimo (*Commentarioli* e *Tractatus in Psalmos*,
Morin, *Anecdota Maredsolana* III, archive.org `anecdotamaredsol03unse`; em `latinos.md`), Bernardo e outros
sermões, Alcuíno (só *De usu Psalmorum*), Gerhoh de Reichersberg e Honório de Autun (não consultados),
Gregório Magno e Agostinho fora das *Enarrationes* (citações; ver `agostinho.md`), Rábano Mauro (sem comentário
salmo a salmo). Os santos e Papas modernos estão em `modernos.md`.

## 3. Como cada obra foi cortada (e o que ficou de fora)

Regras comuns do corte (`lat_comum.py`): títulos em MAIÚSCULAS («PSALMUS N.», «IN PSALMUM N.», «EXPOSITIO IN
PSALMUM N.») localizados em sequência; o trecho vai do título até o título seguinte; títulos repetidos em
seguida (Sl 118 do Arnóbio) formam um só trecho. As marcas `-----[page 0225A]-----` do Corpus viram
`[col. 225A]` no ponto exato do texto; o `Edição` do cabeçalho vai da coluna em vigor no começo até a
última marca. As notas de Migne (`[522]` + `522: (Matth. V, 11)` no rodapé) entram no texto entre
parênteses. Os números soltos que aparecem no texto (`107`, `[11 Psalmus ...]`) são páginas da edição antiga
(Garet, Ballerini, Maurinos…), não versículos.

- **Cassiodoro** (PL 70): usa o saltério antigo (às vezes difere da Vulgata). Os Sl 51 e 101 (Vulgata) vêm como
  «TITULUS PSALMI LI/CI» depois de «PARS SECUNDA/TERTIA» (descartado); o Sl 71 começa em «EXPOSITIO IN OCTO
  DECADAS…» (prefácio às oito últimas décadas, que ficou no Sl 71); o trecho do Sl 150 termina antes da «ORATIO»
  final da obra toda.
- **Arnóbio** (PL 53): cada salmo traz o texto bíblico e o «COMMENTARIUM». Semipelagiano.
- **Bruno de Segni** (PL 164): o original repete «PSALMUS CXV» no lugar do CXVI; o script conserta
  (repetição seguida de salto de dois). Cabeçalhos às vezes têm número de página no meio.
- **Bruno, o Cartuxo** (PL 152): fim do Sl 150 antes da linha do editor «Finis tomi primi…».
- **Lombardo** (PL 191): no fim de cada salmo vem a «COLLATIO IN PSALMUM N» do editor do séc. XVI (variantes do
  hebraico e do grego: Pratensis, Munsterus…), que **não** é de Lombardo; as siglas [Aug.], [Cassiod.], [Hier.]
  dizem de quem é cada glosa (útil para achar a fonte).
- **Hilário** (PL 9): comenta só o que a tabela diz. O tratado sobre o **Sl 9 (Vulgata)** e sobre o **Sl 91** são
  só comentários ao título (curtos, 6 e 18 KB). O «PROLOGUS IN CANTICA QUINDECIM GRADUUM» (prólogo geral dos
  salmos graduais) ficou no começo do Sl 119 (Vulgata) = Sl 120 hebr.; o prólogo geral do *Tractatus* (antes do
  Sl 1) não está em nenhum arquivo (`cache/base/cc_21450.txt`, até a linha 525).
- **Ambrósio**: as *Enarrationes* começam, em vários salmos, com uma «PRAEFATIO»; a do Sl 61 abre com uma nota do
  editor sobre Máximo. A *Expositio in Ps. 118* tem prólogo e 22 sermões (um por letra do alfabeto hebraico) e
  vai inteira para o Sl 119 hebr.
- **pseudo-Jerônimo** (PL 26): no fim da obra há uma «SECUNDA EXPOSITIO SUPER PSALMUM CXIX» (Vulgata), anexada ao
  Sl 119 (Vulgata) = 120 hebr., sob o subtítulo «### Secunda expositio…». O título do Sl 106 vem como
  «PSALMUS. CVI.».
- **Haimo** (PL 116): o Sl 1 é «IN PRIMUM PSALMUM» (título em outra ordem). Autoria incerta (citar como «Haimo (?)»).
- **pseudo-Beda** (PL 93): o original traz «IN PSALMUM CXI» no lugar do XCI, que o
  script conserta; o «ARGUMENTUM PSALMI» depois do Sl 150 é do Sl 151 e fica de fora; há reticências do original.
- **Agostinho**: ver 4.
- **Tomás**: ver 5.
- **Belarmino**: ver 6.

## 4. Agostinho, *Enarrationes* (augustinus.it)

- Tabela arquivo → salmo: `fontes/agostinho.md` § 1.1 (confirmada pelo script contra o título de cada um dos
  208 arquivos). Salmos com mais de uma *enarratio*: todas no mesmo arquivo `base/`, com subtítulo
  «## Salmo N (Vulgata): enarratio II (arquivo 042 do augustinus.it)». O augustinus.it chama de «enarratio III»
  o que o PL chama de «enarratio II, sermo 2»; o script usa o rótulo do site.
- **O site esteve fora do ar** (503) em 2026-10-17 e 2026-10-20: o texto foi baixado do web.archive.org
  (`http://web.archive.org/web/2016id_/http://www.augustinus.it/latino/esposizioni_salmi/esposizione_salmo_NNN_testo.htm`,
  cerca de 4 s por arquivo; os 208 levam uns 25 minutos). O campo `Fonte` traz o endereço do augustinus.it e a
  `Nota` o da cópia usada. As notas de rodapé do augustinus.it (referências bíblicas da NBA, arquivos
  `..._note.htm`) **não estão** no web.archive.org e foram descartadas; vale tentar de novo quando o site voltar.
  Itálico (`*…*`) = citação bíblica; `[v 3.]` = versículo comentado; o número de cada parágrafo é o do original.
- **Colunas da PL**: o augustinus.it não as tem. O script baixa o PL do Corpus Corporum (texto 7329 = Sl 1–79,
  PL 36; texto 21385 = Sl 80–150, PL 37), tira as notas e ancora cada marca de coluna no augustinus.it pelas
  quatro palavras seguintes (letras sem acento, j=i, v=u). Ancoraram 889 de 961 marcas (PL 36) e 875 de 933
  (PL 37): faltam cerca de 7% das marcas inline, mas o campo `Edição` usa interpolação entre as âncoras e confere
  (Sl 36: PL 36, 354–395, igual ao Corpus). O texto do augustinus.it é o dos Maurinos com i/u modernizados
  (sem *j*, sem *v* consonântico): ao procurar uma frase no Corpus, normalizar.
- Há raros erros de digitação no augustinus.it (ex. «labis» por «tubis» no Sl 32); conferir no PL.

## 5. São Tomás, *Postilla super Psalmos*

A obra (uma «reportatio» de Reginaldo de Piperno) acaba no Sl 54 (Vulgata): os hebr. 56–150 estão em
`_ausentes-latinos.md`. Páginas do Corpus Thomisticum: cps01 = Sl 1; cps02 = 2–10; cps11 = 11–20; cps21 = 21–30;
cps31 = 31–40; cps41 = 41–50; cps51 = 51; cps52 = 52–54 (ISO-8859-1). Cada parágrafo traz `**n. M** [ref]`, em que
`ref` é o número do parágrafo no Corpus Thomisticum; o campo `Fonte` leva a âncora do primeiro (`#86786`). O
prólogo (`cps00`) não entrou. **Direitos**: o texto de Tomás é domínio público, mas a digitalização traz «© 2019
Fundación Tomás de Aquino quoad hanc editionem»; o cabeçalho registra isso na `Nota`. Se o Gere preferir não
guardar o texto dessa digitalização, basta apagar `tomas-postilla-super-psalmos.md` (o script o refaz).

## 6. Belarmino, *Explanatio in Psalmos* (1611): OCR do archive.org

- Foi achado em texto: *Opera omnia*, ed. J. Fèvre, Paris, Vivès, 1870–1874, t. X (Sl 1–75, archive.org
  `operaomnia10bell`) e t. XI (Sl 76–150, `operaomnia11bell`), no `_djvu.txt` (cache `cache/base/bel10.txt` e
  `bel11.txt`). OCR **legível mas sujo**: os números romanos dos títulos vêm trocados (G por C, Y por V, 1 por I), as
  notas de margem do original ficam misturadas ao texto na linha onde o OCR as pôs, há rodapés e ornamentos soltos
  (ex. «i l m» no fim do Sl 116 da Vulgata) e palavras partidas. O script tira os cabeçalhos correntes e as sílabas
  partidas (`¬`); não há marcas de página (o OCR dos números de página é pouco confiável). Para citar, conferir
  a imagem em `archive.org/details/operaomnia10bell` (ou `…11bell`).
- Cada salmo da edição Fèvre vem **precedido** de um «Commentaria» do editor (versão do hebraico «secundum
  Hebraeos», notas de Maurer, Ewald, Rosenmüller; numeração hebraica): isso foi **omitido**. O trecho de
  Belarmino começa em «BELLARMINI EXPLANATIO. / PSALMUS N. / (TITULUS ET) ARGUMENTUM» e acaba no começo do
  «Commentaria» do salmo seguinte. Os 150 começos foram achados por três sinais diferentes e numerados em
  sequência (o script confere os 150 e para se a conta não fechar).
- Há também a edição de Roma, 1611 (archive.org `bub_gb_7j0Mm5XItI4C`), com OCR pior: não usada.

## 7. Armadilhas encontradas

- **Numeração**: todos os autores usam a Vulgata/LXX. Nos Sl 9/10, 114/115, 116 e 147 hebr. as pastas dividem ou
  repetem o texto (tabela da seção 1); os arquivos dos Sl 9 e 10 hebr. são **idênticos**, assim como os dos Sl 114 e 115.
- **Títulos do Corpus Corporum diferem de obra para obra** («EXPOSITIO IN PSALMUM», «PSALMUS», «IN PSALMUM»,
  «TRACT. PSALMI», «IN PRIMUM PSALMUM»), às vezes com um número de página antes («47 EXPOSITIO IN PSALMUM XII»)
  ou com ponto depois de PSALMUS («PSALMUS. CVI.»). Procurar um salmo no arquivo bruto com `grep` por «PSALMUM XII»
  falha nesses casos; usar o trecho já cortado.
- **Erros dos próprios textos**: Bruno de Segni (CXV no lugar do CXVI), pseudo-Beda (CXI no lugar do XCI),
  augustinus.it (digitação), OCR de Belarmino e do Corpus («cruet» por *eruet*). Frases estranhas: conferir no PL.
- **Linhas coladas no original**: «sunt:Grandia» (Cassiodoro, Sl 36 Vulgata) é do próprio Corpus.
- **Parágrafos**: o Corpus quebra as linhas a ~80 colunas; o script junta em parágrafos por heurística (linha em
  branco depois de pontuação; linha recuada = título). Em mudança de página pode haver um parágrafo emendado ou
  partido. O texto é o mesmo.
- **Git Bash**: argumento que começa com `/` vira caminho do Windows (`MSYS_NO_PATHCONV=1`); rodar sempre
  `python -I -X utf8`; `>` do PowerShell grava UTF-16.
- **Servidores**: uma requisição por vez, pausa de 1 s. O Corpus Corporum respondeu bem; augustinus.it deu 503;
  o web.archive.org demora (3 a 15 s por arquivo). Tudo baixado fica em `pesquisa/cache/base/` (571 MB com os
  outros pesquisadores; fora do git): refazer os cortes não baixa de novo.
- **Cache do Corpus**: `cc_<idno>.txt` (21404 Cassiodoro; 21351 Arnóbio; 10806 Bruno de Segni; 10473 Bruno
  Cartuxo; 11455 Lombardo; 21450 Hilário; 6956 e 6966 Ambrósio; 7183 pseudo-Jerônimo; 9073 Haimo; 8477 pseudo-Beda;
  7329 e 21385 Agostinho, só para as colunas).

## 8. Padres gregos

Frente «gregos» da pré-pesquisa do Saltério: texto grego de cada comentário, baixado uma vez e cortado por salmo em
`salmos/<ccc>/base/<autor>-<obra>.md`. Os números abaixo são os **hebraicos** (como as pastas `<ccc>`); os gregos usam a
numeração da LXX, que está sempre dita no campo «Passagem» de cada arquivo. Ficam de fora os Sl 33–36 (feitos à mão).
Rodar tudo de novo: `python -I -X utf8 pesquisa/ferramentas/base/grc-tudo.py` (os PDFs ficam em
`pesquisa/cache/base/grc/`, fora do git; segunda rodada não baixa nada; uma requisição por vez, pausa de 1 s).

**Resultado**: 936 arquivos de texto (15,3 MB; 146 salmos têm ao menos um comentário grego), mais `_ausentes-gregos.md`
em 144 salmos e `_pistas-gregos.md` em 146.

### Numeração (hebraica ↔ LXX)

| hebraico | LXX | efeito nos arquivos |
|---|---|---|
| 1–8 | 1–8 | igual |
| 9 e 10 | 9 | os dois salmos hebraicos são um só; **o mesmo texto vai nos dois arquivos**. Exceção: Atanásio e Orígenes (*Selecta*) dividem o Sl 9 em dois blocos («Ἵνα τί, Κύριε, ἀφέστηκας» = Sl 9,22ss = Sl 10 hebraico): aí o Sl 9 tem o primeiro bloco e o Sl 10 o segundo |
| 11–113 | 10–112 | hebraico − 1 |
| 114 e 115 | 113 | um só; mesmo texto nos dois arquivos |
| 116 | 114 + 115 | o arquivo traz os dois salmos da LXX (ou só o que a obra tem, dito na Passagem) |
| 117–146 | 116–145 | hebraico − 1 |
| 147 | 146 + 147 | idem ao 116 |
| 148–150 | 148–150 | igual |

### Obras gravadas em `base/` (script → `pesquisa/ferramentas/base/`)

Biblioteca comum: `_grc.py` (download, limpeza com `gregos-limpar.py`, numeração, corte, cabeçalho). Fecham tudo
`grc-fechar.py` (junta ausentes e pistas e roda `base-indice.py --todos`) e `grc-tudo.py` (roda todos, em ordem).

| obra (arquivo) | salmos hebraicos cobertos (lista exata) | script | observações e armadilhas |
|---|---|---|---|
| Teodoreto de Ciro, *Interpretatio in Psalmos* (`teodoreto-interpretatio-in-psalmos.md`) | 1–32, 37–150 (146 arquivos; todos) | `grc-teodoreto-sl.py` | PG 80, 857–1997. Cabeçalho «ΕΡΜΗΝ. ΤΟΥ ΛΒʹ ΨΑΛΜΟΥ»; o OCR perde o ϛ e a koppa («Ν ʹ» = 56, «Αʹ» depois do 89 = 91) e o Sl 141 vem sem «ΕΡΜΗΝ.». O Sl 150 inclui o epílogo da obra. Quando divide um versículo em dois, os números seguintes do PDF ficam adiantados |
| Santo Atanásio, *Expositiones in Psalmos* (`atanasio-expositiones-in-psalmos.md`) | 1–32, 37–106, 108–147 (142 arquivos). Faltam 107 (LXX 106) e 148–150 | `grc-atanasio-sl.py` | PG 27, 60–548. O título vem **antes** do número («ΨΑΛΜΟΣ τῷ Δαυΐδ. ΙΔʹ. Ὑπόθεσις.») e a palavra ΨΑΛΜΟΣ nem sempre está lá; onde o cabeçalho falta (LXX 18, 90, 96, 123, 124, 126, 133–135, 143, 144), o começo foi achado pelo primeiro versículo e o arquivo traz uma «Nota». O Sl 147 hebraico tem só o Sl 146 da LXX (a *Expositio* acaba na col. 548). Depois dela o PDF segue com perguntas atribuídas a Atanásio (PG 27, 549–589, «Ἀθανάσιος. Διὰ τί δὲ…»): **não entram**. Colchetes = acréscimos de cadeia; muitas glosas coincidem com as de Teodoreto e de Cirilo, sem colchetes: comparar antes de atribuir. A LXX 105 e a 101 só têm resumo (não citam o versículo) |
| Eusébio de Cesareia, *Commentaria in Psalmos* (`eusebio-commentaria-in-psalmos.md`) | 1–32, 37–136, 138–150 (145 arquivos). Falta 137 (LXX 136) | `grc-eusebio-sl.py` | Dois PDFs: PG 23, 66–1396 (LXX 1–118) e PG 24, 9–76 (LXX 119–150); a fonte de cada arquivo é o PDF certo. **Só cadeia** em todos, exceto os hebr. 52–96 (LXX 51–95), onde é comentário contínuo: o campo «Cobre» diz qual. Os cabeçalhos são irregulares (título em maiúsculas + número, às vezes sem número): o começo foi achado pelo primeiro versículo e recuado até o cabeçalho; o texto dos Sl 119–150 acaba no meio do Sl 150,2. Pode parar antes do fim do salmo; nas cadeias, a primeira parte às vezes é de Dídimo (Mühlenberg) ou de Orígenes: conferir |
| São Basílio, *Homiliae super Psalmos* (`basilio-homiliae-super-psalmos.md`) | 1, 7, 15, 29, 30, 45, 46, 49, 60, 62, 116 (= LXX 1, 7, 14, 28, 29, 44, 45, 48, 59, 61, 114) | `grc-basilio-sl.py` | PG 29, 209–494. Só 13 homilias autênticas; as dos Sl 33 e 34 (hebr.) são da outra frente. A homilia sobre a LXX 29 termina aberta na PG («δυνήσεται;»); a sobre a LXX 59 não tem título de cabeçalho no Sl, só «ΕΙΣ ΤΟΝ ΝΘʹ ΨΑΛΜΟΝ» |
| Pseudo-Basílio (`pseudo-basilio-homilia-in-psalmum-<N>.md`) | 29 (LXX 28, outra homilia), 38 (LXX 37), 116 (LXX 115), 133 (LXX 132) | `grc-basilio-sl.py` | PG 30, PDFs à parte («In Psalmum XXVIII», «Homilia in Psalmum XXXVII 1», «…CXV», «…CXXII», este último é o Sl 132). **Espúrias**: não citar como de Basílio |
| São João Crisóstomo, *Expositiones in Psalmos* (`crisostomo-expositiones-in-psalmos.md`) | 4–13, 42, 44–50, 109–118, 120–150 (59 arquivos; LXX 4–12, 41, 43–49, 108–117, 119–150) | `grc-crisostomo-sl.py` | PG 55, 35–498. No PDF os Sl 8–12 da LXX aparecem **duas vezes** (duas redações seguidas): o arquivo junta as duas, com uma linha entre elas. Em 15 salmos hebraicos o comentário vem em várias homilias |
| Crisóstomo, PDFs à parte, sem marca de espúrio: `crisostomo-in-psalmum-50.md` (hebr. 51), `crisostomo-in-psalmum-145.md` (hebr. 146) | 51, 146 | `grc-crisostomo-sl.py` | PG 55, 527–532 e 519–528. O khazarzar não os marca com [Sp.]; autoria do Sl 50 a conferir |
| Pseudo-Crisóstomo (`pseudo-crisostomo-in-psalmum-<N>.md`, `…-50-homilia-1/2.md`, `…-in-psalmos-101-107.md`) | 51 (duas homilias), 76, 93, 95, 101, 102–108 (um arquivo por salmo, do PDF «101_107»), 119 (três homilias seguidas, 240 KB), 140 | `grc-crisostomo-sl.py` | PG 55, todos marcados [Sp.] no khazarzar: **espúrios**. O «Prooemia in Psalmos» (introdução geral, PG 55, 531–538) não entra |
| São Cirilo de Alexandria, *Expositio in Psalmos* (`cirilo-expositio-in-psalmos.md`) | 1–28, 30–32, 37–53, 58–84, 86, 88–89, 91–102, 104–105, 110, 114–116, 118–120 (99 arquivos) | `grc-cirilo-sl.py` | PG 69, 717–1273 (ed. Mai): **cadeia**; siglas «(A f. 175)» são de manuscritos; trechos entre colchetes têm origem incerta; muitas glosas repetem Basílio e Teodoreto. A koppa sai como «ς» («ΨΑΛΜΟΣς ʹ» = 90). O texto acaba no começo da LXX 119 (hebr. 120), e sob esse cabeçalho vêm uns trechos que são da LXX 138. «Cobre» diz que não são todos os versículos |
| Orígenes, *Selecta in Psalmos* (`origenes-selecta-in-psalmos.md`) | 1–32, 37–90, 92–116, 118–137, 139–150 (143 arquivos). Faltam 91, 117, 138 (LXX 90, 116, 137) | `grc-origenes-selecta-sl.py` | PG 12, 1053–1686. Glosas de cadeia (lemas «κ. τ. ἑ.»); parte é de Evágrio, parte Mühlenberg dá a Dídimo. O «Τόμος» sobre o Sl 1 está no Sl 1; a introdução geral («Διὰ τοὺς ἐπιγεγραμμένους…») fica de fora. O bloco «Ἵνα τί, Κύριε» vem rotulado «ΨΑΛΜΟΣ Ιʹ (Κατὰ Ἑβρ.)» = Sl 10 hebraico. A LXX 6 e a 96 foram achadas pelo versículo |
| Orígenes, *Fragmenta in Psalmos* (Pitra) (`origenes-fragmenta-in-psalmos.md`) | 1–32, 37–116, 118–150 (145 arquivos). Falta 117 (LXX 116) | `grc-origenes-fragmenta-sl.py` | Pitra, *Analecta sacra* III. **O marcador «[PG 32, 6]» é salmo 32, versículo 6, não coluna** (vem antes do texto do versículo); por isso «Edição» não dá colunas. O começo de cada salmo é o primeiro marcador; os vv. anteriores (títulos, v. 1–2), quando comentados, podem estar no fim do arquivo do salmo anterior. OCR ruim (palavras partidas, letras trocadas). Quase tudo é igual ou parecido com as *Selecta* |
| São Gregório de Nissa, *In inscriptiones Psalmorum* (`gregorio-nissa-in-inscriptiones-psalmorum.md`) | 3, 9, 10, 18, 30, 42, 45, 48, 49, 51–60, 71, 92, 95, 97, 102, 125 (25 arquivos; LXX 3, 9, 17, 29, 41, 44, 47, 48, 50–59, 70, 91, 94, 96, 101, 124) | `grc-nissa-sl.py` | GNO V (McDonough): tratado sobre a ordem do Saltério e os títulos, **não** comentário seguido. Os trechos são os parágrafos do Livro II em que aparece uma sequência de 5 palavras do título ou do v. 2 que não se repete em outro salmo: heurística, conferir. Os marcadores «[PG 5, 119]» são páginas da GNO V |

Tamanho (arquivos com cabeçalho): Teodoreto 2,3 MB; Eusébio 3,5 MB; Crisóstomo (principal + 2 sem marca) 3,0 MB;
Orígenes *Selecta* 1,2 MB e *Fragmenta* 1,1 MB; Cirilo 1,2 MB; Atanásio 1,2 MB; Basílio 0,5 MB; Nissa 0,2 MB;
espúrios 0,9 MB.

### Não gravado em `base/` (só pistas, em `_pistas-gregos.md`)

| obra | por quê | script |
|---|---|---|
| Dídimo, o Cego: comentário de Tura (Sl 20–44 da LXX, com lacunas; ed. Gronewald, PTA 4–8) e fragmentos de cadeia (ed. Mühlenberg, PTA 15–16, frgs. por salmo) | edição moderna: registrada só a pista (PDF do khazarzar e, nos fragmentos, o intervalo de números por salmo). No Tura o PDF quase não tem marcadores de salmo (só «177 32,13»); as páginas por salmo precisam ser lidas | `grc-didimo-pistas.py` |
| Hesíquio de Jerusalém, *Fragmenta in Psalmos* (PG 93, 1179–1340) | OCR do archive.org (`patrologiaecursu93mignuoft`) sem condições: as colunas grego/latim (tradução de Corderius) vêm misturadas e o grego sai quebrado. Pista para cada salmo | `grc-ia-pistas.py` |
| Eutímio Zigabeno, *Commentarius in Psalterium* (PG 128, 41–1326) | OCR do archive.org (`patrologiaecurs261unkngoog`): o latim sai legível («PSALMUS XXXIV.», algarismos da LXX), mas o grego sai com letras latinas («xai» por καὶ) e as colunas se misturam; refazer à mão. Compila sobretudo Teodoreto. Pista para cada salmo | `grc-ia-pistas.py` |

Não usados, por decisão do dono: Apolinário de Laodiceia (herege) e Teodoro de Mopsuéstia (condenado em 553); Diodoro de
Tarso também não está no khazarzar. Não procuradas nesta frente: Atanásio, *Carta a Marcelino*; Cirilo, *Fragmentum in
Psalmum*; Gregório de Nissa, *In sextum Psalmum* (baixado em cache: `nissa-sl6`, GNO V, ainda não cortado); Orígenes,
*Excerpta in Psalmos* (PG 17, 105 ss., cache `origenes-exc`, só o Sl 9,8–9); Cirilo, *Expositio in Psalmos_* (prefácio).

### Como o corte foi feito (e como conferir)

- **Régua**: o Saltério da LXX (Rahlfs 1935), de `eliranwong/LXX-Rahlfs-1935` no GitHub (`text_accented.csv` e
  `E-verse.csv`), guardado só em `cache/base/grc/` e lido por `_grc.lxx()`. Serve para achar onde cada salmo começa quando
  o cabeçalho falta no PDF (primeiro versículo citado, em janelas de 4 palavras que não se repetem em outro salmo) e para
  **conferir** os cortes: `_grc.verificar()` diz em quais salmos o v. 1 não aparece perto do começo. Isso nem sempre é erro
  (resumos que não citam o versículo, cadeias); os casos estão listados nas saídas dos scripts.
- **Amostras conferidas** (início e fim de ao menos cinco salmos por obra, mais os de borda 1, 9–10, 116, 118, 147, 150): início
  no cabeçalho do salmo certo e fim na frase anterior ao cabeçalho seguinte. Pequenos desvios possíveis: o fim do arquivo
  pode trazer 1 frase do título do salmo seguinte (Eusébio, Cirilo) e, onde o começo foi achado pelo versículo, o arquivo
  pode perder ou ganhar 1 frase do título (há «Nota» no arquivo).
- A numeração dos Padres é a LXX; **nunca** misturar com o hebraico ao citar. «PG 27, 61» é o marcador de coluna do PDF
  (o texto da coluna vem **depois** do marcador); a «Edição» de cada arquivo é a faixa de colunas tocada pelo trecho.
- Mesmo texto, vários nomes: cadeias (Eusébio, Orígenes, Cirilo, Atanásio) repetem Basílio, Teodoreto e Dídimo; a pesquisa do
  capítulo deve citar o autor da homilia ou do comentário seguido, não o da cadeia.
- O khazarzar responde em https; PDFs: `https://khazarzar.skeptik.net/pgm/PG_Migne/<pasta>/<arquivo>.pdf` (a URL exata de
  cada arquivo está no campo «Fonte»).

## 9. Modernos, Magistério e liturgia

Para juntar ao mapa do Saltério. Cobre os salmos **1 a 150 (numeração hebraica, pasta `salmos/<ccc>/`) menos 33, 34, 35 e 36**
(146 salmos). Nada disto foi traduzido nem escolhido: só baixado, cortado e indexado. Os textos com direito autoral (catequeses
e documentos papais, Lecionário, Catecismo) **não** foram guardados: só pistas com o endereço.

### Arquivos gravados em cada `salmos/<ccc>/base/`

| arquivo | conteúdo | salmos |
|---|---|---|
| `afonso-salmi.md` | Santo Afonso, *Traduzione de' Salmi e de' Cantici* (1774): argomento e, versículo a versículo, o latim da Vulgata e a paráfrase italiana, com as notas dele e as notas de rodapé da edição | 146 de 146 |
| `liturgia.md` | onde o salmo é rezado: Liturgia das Horas (saltério de 4 semanas), salmo responsorial (Lecionário de 1981), propers do Missal até 1962, saltério do Breviário de Pio V e de Pio X, com as antífonas latinas antigas | 146 de 146 |
| `_pistas-modernos.md` | catequeses e documentos papais (título, data, URL do vatican.va) e parágrafos do Catecismo | 146 de 146 (algumas seções dizem «Nenhuma») |
| `_ausentes-modernos.md` | o que se conferiu que não existe | 146 de 146 |

Números da pesquisa (salmos hebraicos entre os 146):
- **Santo Afonso**: 146 (todos). Os hebr. 9 e 10 recebem o mesmo texto (o Sl 9 da Vulgata, que Afonso trata como um só), e os hebr. 114 e 115
  também (o Sl 113 da Vulgata). O hebr. 116 junta os dois salmos 114 e 115 da Vulgata (duas seções) e o hebr. 147, os 146 e 147.
- **Catequese dedicada ao salmo** (ciclo de Laudes e Vésperas de João Paulo II, 2001–2005, e de Bento XVI, 2005–2006): 79 salmos, 108 catequeses
  (a pasta tem 110 no total; 2 são dos salmos 33–36, excluídos). Hebr.: 5, 8, 11, 15, 16, 19, 20, 21, 24, 27, 29, 30, 32, 41, 42, 43, 45–49, 51, 57, 62, 63, 65, 67, 72, 77,
  80, 81, 84–87, 90, 92, 93, 96, 98–101, 108, 110–119, 121–127, 130–132, 135–139, 141–150. Sem catequese: os outros 67.
- **Outras audiências e documentos papais que citam o salmo 3 vezes ou mais** (Bento XVI 2005–2013, Francisco, Leão XIV, e encíclicas, exortações e cartas
  apostólicas de João Paulo II, Bento XVI, Francisco e Leão XIV): 18 salmos (2, 3, 4, 8, 16, 22, 23, 42, 60, 71, 97, 110, 114, 119, 126, 128, 136, 139). Aqui entram a
  «Escola de oração» de Bento XVI (2011: Sl 3, 22, 23, 110, 119, 126, 136) e *Verbum Domini*.
- **Catecismo**: 53 salmos citados (notas ou texto); 93 salmos não aparecem.
- **Liturgia das Horas**: os 146 estão no índice; **omitidos da Liturgia das Horas: 58, 83 e 109** (imprecatórios). **Lecionário**: 123 salmos são salmo responsorial de alguma
  Missa nas tabelas (sem: 6, 14, 20, 38, 39, 53, 58, 61, 64, 70, 73, 75, 76, 83, 108, 120, 127, 129, 133, 134, 140, 142, 143). **Missal até 1962**: 132 salmos têm intróito,
  gradual, tracto, ofertório ou comunhão (sem: 49, 53, 58, 75, 82, 94, 99, 101, 121, 128, 131, 134, 136, 150). **Breviário antigo**: 146.

### Scripts (`pesquisa/ferramentas/base/`, uso no topo de cada um; Python com `python -I -X utf8`)

Ordem para refazer tudo: `mod-afonso-salmi.py baixar` e `cortar`; `mod-liturgia.py baixar` e `construir`; `mod-catecismo.py baixar` e `indice`;
`mod-papas.py baixar`, `baixar-docs` e `analisar`; por fim `mod-montar.py` (liturgia.md, `_pistas`, `_ausentes`) e `base-indice.py --todos`.

- `mod-afonso-salmi.py`: baixa as 38 páginas do IntraText (`_P36G` a `_P37H`), liga cada seção ao salmo pelo latim do 1º versículo (maior prefixo comum com o
  Saltério da Vulgata do Divinum Officium; o número impresso «(M. del salterio)» só desempata e tem 5 erros de impressão), corta por salmo, junta o que a
  quebra de página parte, e põe as notas de rodapé no fim da seção. `mapa` mostra a tabela.
- `mod-papas.py`: percorre os índices anuais de audiências de vatican.va (JP II 2001–2005, Bento XVI 2005–2013, Francisco 2013–2025, Leão XIV 2025–2026: 1.130
  audiências) e os índices de encíclicas, exortações e cartas apostólicas (112 documentos), em italiano; guarda o texto só no cache, conta as citações «Sal/Salmo N»
  e marca as catequeses do ciclo pelo título «Salmo N» ou pela «Lettura:». **Conferido** contra a lista de datas de `fontes/modernos.md` § 2: as 110 datas batem
  exatamente.
- `mod-catecismo.py`: baixa os 28 arquivos do Catecismo em português (vatican.va/archive/cathechism_po), liga cada chamada de nota «(N)» ao parágrafo e lê as notas «N. Cf. Sl …».
- `mod-liturgia.py`: tabelas de Felix Just (saltério de 4 semanas e Lecionário) e Divinum Officium (Missal e Breviário); `mod-montar.py` escreve os arquivos de `base/`.
- `mod-clerus.py`: percorre o Biblia Clerus (150 páginas de citações). **Não é usado nos arquivos finais**: ver a armadilha 1.

### Fontes usadas

- Afonso: https://www.intratext.com/IXT/ITASA0000/_IDX150.HTM (já descrito em `fontes/modernos.md` § 1).
- Catequeses papais: índices `https://www.vatican.va/content/<papa>/it/audiences/<ano>.index.html` (papa = `john-paul-ii`, `benedict-xvi`, `francesco`, `leo-xiv`) e
  `…/it/<encyclicals|apost_exhortations|apost_letters>.index.html` (cartas de João Paulo II: índices anuais `apost_letters/<ano>.index.html`; caminho dos documentos
  com `/<ano>/documents/`).
- Catecismo: https://www.vatican.va/archive/cathechism_po/index_new/prima-pagina-cic_po.html (28 arquivos).
- Saltério de 4 semanas: https://catholic-resources.org/LoH/Psalter-Index.html; Lecionário: https://catholic-resources.org/Lectionary/ (`1970USL-Sundays`, `1998USL-Solemnities`,
  `1970USL-WeekdaysA`, `1970USL-WeekdaysB`): numeração e versículos hebraicos, sem o refrão.
- Missal e Breviário antigos: https://github.com/DivinumOfficium/divinum-officium (`codeload` do `master`; só as pastas `web/www/missa/Latin` e `web/www/horas/Latin`).

### Armadilhas

1. **O Clerus erra os parágrafos do Catecismo**: os números vêm deslocados de 1 a 6 (Sl 22,15: Clerus «114», certo § 112; Sl 130,1: Clerus «2565», certo § 2559). Usar as notas do próprio Catecismo
   (já feito). Conferir qualquer parágrafo antes de citar. O Clerus também mistura a numeração da Vulgata nas páginas de citações.
2. **Numeração**: Afonso, as catequeses de 2001–2006, o Missal e o Breviário antigos usam a Vulgata; Catecismo, Lecionário, saltério de 4 semanas e Francisco, a hebraica. As pistas dizem
   qual vale em cada linha. Conversão: 1–8 igual; hebr. 9–10 = Vulg. 9; 11–113 = −1; hebr. 114–115 = Vulg. 113; hebr. 116 = Vulg. 114–115; 117–146 = −1; hebr. 147 = Vulg. 146–147; 148–150 igual.
3. **Versículos do Divinum Officium** contam o título como v. 1 quando ele existe (Vulgata); Afonso numera sem o título. O Lecionário (US) segue a numeração hebraica.
4. **«Hora Média»** na Liturgia das Horas = Terça, Sexta e Noa (a pessoa escolhe uma delas); «Semanas II e IV» = as duas.
5. **Matinas do Breviário de Pio V**: as seções `Day0…Day6` do Divinum Officium NÃO são a distribuição tridentina (Day0 traz 1, 2, 3, 8, 9, 10…); por isso as Matinas de Pio V saem da própria
   *Traduzione* de Afonso (que segue o Breviário tridentino). `Daya0…6` é o saltério de Pio X (1911). Laudes, Vésperas e horas menores de Pio V (`Day0 Laudes1`, `Vespera`, `[Tridentinum]`)
   conferem com a ordem de Afonso.
6. **Nomes de arquivo do Divinum Officium**: variantes `…t`, `…r`, `…pl`, `…m1` são rubricas diferentes (Tempora/Quad3-6 e Quad3-6t, Sancti/04-23pl etc.); o montador junta as iguais. Alguns
   `Sancti/` não têm título no arquivo e aparecem só com o código da data.
7. **Títulos de catequese**: no ciclo de 2001–2006 o número sem colchetes é o da Vulgata («Salmo 135» é o hebr. 136) e a referência do título às vezes é a leitura, não o salmo todo
   (uma catequese cobre um trecho; o Sl 51 tem 4, o Sl 119 tem 3).
8. **JP II antes de 2001 e o Angelus**: não varridos (audiências 1978–2000, Angelus, homilias, mensagens, discursos). Para um salmo muito citado (22, 51, 23, 110) a pesquisa do capítulo pode ainda
   procurar aí, ou usar o índice por versículo do Clerus.
9. **vatican.va**: respondeu bem a uma requisição por vez com 1 s de pausa (≈ 1.500 requisições no total). Francisco e Leão XIV têm títulos de audiência incompletos no cache (cabeçalho da página); a «frase do
   que comenta» das pistas não ciclo é só o título e o número de citações.

### O que falhou ou ficou «a confirmar»

- **Antífonas latinas da *Liturgia Horarum* (1971)**: sem fonte aberta raspável. Universalis bloqueia o `curl` (e cobra o Ofício das Leituras); iBreviary ignora o parâmetro de língua e de data;
  brewiarz.katolik.pl/latin só tem Domingos do Tempo Comum II–VIII e festas soltas (`…/latin/<DDMM>/laudes_matutinae.php3`), não o saltério semanal; almudi.org (leitor da *Liturgia Horarum*) não foi
  tentado. Todo `liturgia.md` diz «a confirmar» para as antífonas da Liturgia das Horas; as antífonas latinas **antigas** (Pio V e Pio X) estão lá, do Divinum Officium.
- **Refrão do salmo responsorial** (latim e CNBB): não coletado; as tabelas do Lecionário não o trazem. Onde achar: PDFs de `romanliturgy.org` (`Ps-<n>-…pdf`) para o latim e `liturgia.cancaonova.com` ou a
  Palavra do Dia para o texto da CNBB. Em `liturgia.md`: «Refrão: a confirmar».
- **Próprios de santos e do Tempo no Breviário antigo** (psalmos de antífonas dos Comuns, das Matinas de festas) e **textos do Ofício das Leituras**: não varridos.
- **Lecionário**: as tabelas de Felix Just são do Lecionário dos EUA (ciclo A/B/C e de dois anos iguais ao romano, mas sem a Vigília Pascal completa nem as Missas rituais); a numeração OLM só aparece nos dias de semana.
