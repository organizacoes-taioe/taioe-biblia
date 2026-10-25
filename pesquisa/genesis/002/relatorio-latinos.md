# Gênesis 2: relatório do grupo «latinos» (25/10/2026)

Latinos antigos e medievais, menos Agostinho. Partiu-se da pré-pesquisa (`BASE.md`: Ambrósio, *De paradiso*;
Beda; Ruperto; Rábano; Alcuíno; Isidoro; Hugo; Jerônimo; e o fim do *Hexaemeron* de Ambrósio em `../001/base/`)
e procurou-se o resto nos sermões, cartas e tratados da PL. Entregues **16 achados** em `achados-latinos.json`:
trecho 1 = 3, trecho 2 = 2, trecho 3 = 4, trecho 4 = 7. Dez autores; Ambrósio tem 4.

## Como se procurou

1. Leitura inteira das obras da base que comentam o capítulo (Ambrósio, *De paradiso*; Beda; Ruperto; Hugo,
   *De sacramentis* I, 6; Jerônimo; Alcuíno) e, por amostra, de Rábano, Isidoro e Hugo, *Adnotationes*.
2. Varredura de 130 textos da PL (`cache/genesis/latinos/`, Corpus Corporum): os que Gn 1 deixou no cache e uns
   90 baixados agora (Tertuliano, Cipriano, os 70 textos de Bernardo, Lombardo, Hilário, Gaudêncio, Cromácio,
   Paulino, Fulgêncio, Comestor, Honório, Vitorino de Petávio…), pelas notas de Migne «(Gen. II…)» e por 30 frases
   da Vulgata e da Vetus Latina; 233 parágrafos com ocorrência, resumidos numa linha, e o contexto aberto só dos
   melhores.
3. Corpus Thomisticum (q. 73 e q. 92, já no cache) e o *Breviloquium* de Boaventura (Quaracchi V, OCR do
   archive.org, guardado em `cache/genesis/latinos/bonav-05.txt`).
4. Cada `original` saiu por script como substring exata do texto limpo (sem as notas de Migne, as marcas de
   coluna e os números de página da edição anterior); as correções estão abaixo. Os scripts ficaram no scratchpad
   da conversa (`g-latinos/`: `cc.py`, `varrer.py`, `excerto.py`, `gerar_base.py`), no modelo dos de Gn 1.

## O que se achou

| autor | obra | onde | situação |
|---|---|---|---|
| Santo Ambrósio | *Hexaemeron* VI, 10, 75–76 | PL 14, 272C–D | `../001/base/`; 1 achado |
| Santo Ambrósio | *De paradiso* | PL 14, 275–307 | base; 2 achados (7, 35; 13, 63); reserva 4, 25, 10, 47, 11, 49–50 |
| Santo Ambrósio | *De institutione virginis* 3, 16–24; 5, 36 | PL 16, 309B–311B; 314–315 | `base/` novo; 1 achado |
| Santo Ambrósio | *Expositio in Lucam* II, 85–89 | PL 15, 1584A–1586A | `base/` novo; reserva (forte) |
| Santo Ambrósio | Cartas 44 e 45 (Maurinos) | PL 16, 1135C–1145B | `base/` novo; reserva |
| Santo Ambrósio | *Enarr. in Ps.* 37, 27; 39, 11 | PL 14, 1022A–B; 1061B–C | `base/` novo; reserva |
| São Beda | *In principium Genesis* I | PL 91, 34C–53A | base; 1 achado (35B–D); reserva 52A |
| Ruperto de Deutz | *In Genesim* II, 13–40 | PL 167, 257D–289A | base; 2 achados (23, 34); reserva 17, 22, 30, 33, 39, 40 |
| Hugo de São Vítor | *De sacramentis* I, 6, 3–37 | PL 176, 264D–288A | base; 1 achado (34–35); reserva 29 |
| São Jerônimo | *Quaestiones hebraicae* (Gn 2) | PL 23, 940A–942A | base; 1 achado (2,23, *virago*) |
| São Jerônimo | Carta 123, 12; Carta 51, 5 (de Epifânio) | PL 22, 1053; 522 | `base/` novo; fora (contra as segundas núpcias; Epifânio) |
| Tertuliano | *De anima* 43 | PL 2, 721A–724B | `base/` novo; 1 achado |
| Tertuliano | *De resurrectione carnis* 5–7 | PL 2, 800C–806A | `base/` novo; 1 achado |
| Tertuliano | *De exhortatione castitatis* 5; *De monogamia* 4–5 | PL 2, 920; 934–936 | lidos; fora (montanistas, contra as segundas núpcias) |
| São Pedro Crisólogo | Sermão 148 | PL 52, 596A–598A | `base/` novo; 1 achado |
| São Gregório Magno | *Moralia* XXXV, 14, 28; XIX, 21, 34 | PL 76, 765B–C; 119C | `base/` novo; 1 achado; reserva XIX |
| São Gregório Magno | *Hom. in Ez.* I, 6, 15 | PL 76, 835B | `base/` novo; só uma linha numa lista de figuras |
| São Bernardo | *In Septuagesima* 2; *De diversis* 15 e 2; *In dedicatione* 5 | PL 183, 166B–167C; 577; 544–545; 536 | `base/` novo; 2 achados |
| São Tomás | *Suma* I, q. 73 (sétimo dia) e q. 92 (a mulher) | Leonina 5 | q. 73 em `../001/base/`, q. 92 em `base/`; 1 achado (q. 73) |
| Pedro Lombardo | *Sentenças* II, d. 18; IV, d. 28 | PL 192, 687–688; 915–916 | `base/` novo; copia Hugo; pista para a liturgia |
| São Leão Magno | Sermões 24, 2 e 30, 4 | PL 54, 204C–205B; 231C–232B | `base/` novo; de passagem |
| São Zenão | Tratado I, 12, 1–2 | PL 11, 338A–341A | `base/` novo; reserva (*homo*/*humus*) |
| Santo Hilário | *Tract. in Ps.* 91, 118 (Iod), 129 | PL 9, 494; 565–567; 720 | `base/` novo; técnico, sem achado |
| Santa Hildegarda | *Liber divinorum operum* II, 1, 47–49 | PL 197, 953B–956A | `base/` novo; alegoria, sem achado |
| Alcuíno | *Interrogationes* 1–8, 42–59 | PL 100, 517–522 | base; respostas de uma linha; reserva 7 e 53 |
| Rábano, Isidoro, Hugo (*Adnotationes*) | | | base; compilação, alegoria e notas secas; sem achado |
| São Boaventura | *Breviloquium* II, 10–11 | Quaracchi V, 227–229 | lido no OCR; segue Hugo; sem achado |

Quem não comenta (ou só de passagem): `base/_ausentes-latinos.md`. Reserva e pistas não seguidas:
`base/_pistas-latinos.md`.

## Os 16 achados

1. **Trecho 1 (vv. 1–3)**: Ambrósio, *Hex.* VI, 10, 75–76: Deus não descansou depois do céu nem dos astros, mas
   depois do homem, «tendo a quem perdoar os pecados» (3); Beda: a bênção do sétimo dia prefigurava o grande
   sábado em que Cristo, depois do «Está consumado» do sexto dia, descansou no sepulcro; o sétimo dia sem tarde (3);
   Tomás, q. 73: no sétimo dia a consumação da natureza, na encarnação a da graça, no fim a da glória; Deus nos faz
   descansar nele (2).
2. **Trecho 2 (vv. 4–7)**: Tertuliano, *De res.* 5–6: Deus todo ocupado no barro, com afeto, e em cada traço pensava
   em Cristo, o homem futuro (3); Crisólogo, Sermão 148: a mão que tomou o barro tomou a carne; «homem, por que te
   tens em tão pouco, se és tão precioso para Deus?»; o corpo da terra e a alma do céu, a concórdia dos dois (3).
3. **Trecho 3 (vv. 8–17)**: Ruperto II, 23: só Deus é dono do jardim; o homem, forasteiro e colono; graça recebê-lo,
   justiça perdê-lo (3); Bernardo, *De diversis* 15, 1: se Adão foi posto no lugar das delícias para trabalhar, quem
   pensará que os filhos dele estão no lugar da aflição para folgar? (3); Gregório, *Moralia* XXXV, 14, 28: a
   obediência planta e guarda as outras virtudes; por isso o primeiro homem recebeu um mandamento (3); Ambrósio,
   *De paradiso* 7, 35: a morte veio da desobediência; Deus proibiu como bom médico (3).
4. **Trecho 4 (vv. 18–25)**: Ambrósio, *De inst. virg.* 3, 16.22: costuma-se acusar a mulher, mas «sem a mulher o
   homem não recebe louvor» (3); Hugo, *De sacr.* I, 6, 34–35: um só princípio para que todos se amem como um; do
   lado, «nem senhora nem serva, mas companheira» (3); Tertuliano, *De anima* 43: o sono de Adão era a morte de
   Cristo, e do lado ferido a verdadeira mãe dos viventes, a Igreja (3); Bernardo, *In Septuagesima* 2, 1: o sono de
   Adão veio da contemplação da verdade, o de Cristo, da caridade, «como leão vencedor» (3); Jerônimo: *ish*/*ishá*,
   *andrís*, *virago* (2); Ruperto II, 34: a costela mostra que o amor conjugal deve ser indissolúvel, mandamento
   «antigo, desde o princípio» (2); Ambrósio, *De paradiso* 13, 63: nus, mas vestidos de virtudes; a natureza não
   conhecia o manto do engano (3).

Os três mais fortes: `ambrosio-hex-6-10-75-76-descansou-no-homem`, `tertuliano-ressurreicao-6-o-barro-e-cristo`,
`hugo-sacramentos-1-6-35-nem-senhora-nem-serva`. Logo atrás: `pedro-crisologo-sermao-148-precioso-para-deus`,
`beda-hexaemeron-1-gn2-3-o-sabado-no-sepulcro`, `bernardo-diversos-15-1-adao-posto-para-trabalhar`.

## Sobreposições (para a escolha final)

- **O lado de Adão e o de Cristo** (2,21): Tertuliano (*De anima* 43) é a fonte de Agostinho, *Tract. in Io.* 9, 10
  e 120, 2, de Crisóstomo, *Catequeses* 3, e de Beda (PL 91, 51A–C, que segue Agostinho, *Gen. c. Man.* II, 12 e *Tract. in Io.* 9, 10). Ficar com um ou dois.
  Bernardo, *In Sept.* 2, diz outra coisa (o sono por amor, voluntário) e pode ficar ao lado de qualquer deles.
  Ambrósio, *In Lucam* II, 86–87 («e agora se edifica»), Ruperto II, 37 e Gregório, *Hom. in Ez.* I, 6, 15 repetem.
- **O sono como êxtase profético** (Bernardo, fim do excerto) é de Agostinho, *Gen. ad litt.* IX, 19 (que Beda
  cita, PL 91, 52B): se o grupo agostinho trouxer esse, cortar o fim do de Bernardo.
- **O lado, nem cabeça nem pés** (2,21-22): Hugo é a fonte de Lombardo (*Sent.* II, d. 18, c. 3), de Tomás (*Suma*
  I, q. 92, a. 3) e de Boaventura; o de Hugo é o mais bonito. Agostinho, *Civ.* XII, 22–23, diz só a primeira parte
  (um só princípio, para a concórdia).
- **O descanso de Deus**: Ambrósio (no homem, a quem perdoar) e Beda (o sábado do sepulcro) não repetem os
  agostinianos; Tomás, q. 73, a. 2 ad 3 («nos faz descansar nele») toca o que *Confissões* XIII, 35–38 diz melhor:
  se faltar lugar, tirar o fim do excerto de Tomás e deixar só as três consumações. O «sétimo dia sem tarde» de Beda
  é de Agostinho (*Conf.* XIII, 36).
- **O barro e Cristo** (2,7): Tertuliano e Crisólogo ligam os dois ao Verbo encarnado, mas de modo diferente (o
  modelo / a dignidade do homem); Ireneu (as mãos de Deus) e Nazianzeno (o «segundo mundo», terra e espírito) estão
  nos gregos: a «concórdia do céu e da terra» de Crisólogo toca Nazianzeno.
- **O trabalho** (2,15): Bernardo diz o que Agostinho, *Gen. ad litt.* VIII, 8–9 e Crisóstomo, *Hom.* 14 dizem,
  mas aplicado a nós; o de Agostinho é o clássico (o trabalho como alegria). Ruperto II, 23 (o colono) toca
  *Laudato si'* 67 (modernos).
- **O mandamento** (2,16-17): Gregório depende de Agostinho, *Civ.* XIV, 12 (a obediência, «mãe e guardiã de todas
  as virtudes» na criatura racional) e *Gen. ad litt.* VIII, 6, 12: se o grupo agostinho trouxer esse, trocar
  Gregório por Ruperto II, 30 («onde nada é confiado, não aparece fidelidade»; em `base/_pistas-latinos.md`).
  Ambrósio, o bom médico, é único.
- **A nudez** (2,25): Ambrósio (a veste das virtudes) está ao lado de Efrém (a veste de glória) e de Agostinho,
  *Civ.* XIV, 17; dizem coisas parecidas por caminhos diferentes.

## Correções nos originais (conferir na imagem da PL, se for preciso)

- Hugo, *De sacr.* I, 6, 35: o Corpus Corporum traz «praeferenda videretur viro ad damnationem»; posto «ad
  dominationem», que é o sentido e a leitura de Pedro Lombardo, que copia o trecho (*Sent.* II, d. 18, c. 3).
- Ruperto, *In Gen.* II, 34: «ab intio» → «ab initio»; «factoris suis» → «factoris sui».
- Jerônimo, *Quaest. hebr.*: tirados os parênteses vazios onde a PL tinha letras hebraicas («IS ( )», «ISSA ( )»).
- Gregório, *Moralia* XXXV, 14, 28: tirado o número de página «1156» que Migne deixa no meio da frase.
- Tomás: o excerto começa por «complevit Deus die septimo…», a citação do *sed contra* (sem «Sed contra est quod
  dicitur Gen. II»), em minúscula como na fonte.

## Dúvidas

- **Termos de 2,7 e 2,23**: segui o `PEDIDO.md` («o homem tornou-se alma vivente»; «varoa» só quando o Padre comenta
  a palavra, como Jerônimo). O `conteudo/genesis/002.json` em preparo traz «tornou-se um ser vivente» e, no v. 23,
  «Esta se chamará varoa, porque do varão foi tomada»; se ficar assim, ajustar «alma vivente» na tradução de
  Tertuliano e talvez «varão» em Jerônimo e Bernardo.
- **Tertuliano**: o *De resurrectione* e o *De anima* são da fase montanista (c. 208–213), mas os dois trechos não
  tocam nada disso; o `autores.json` já o tem como «escritor eclesiástico de Cartago».
- A numeração dos parágrafos modernos de Tertuliano (CCSL) não foi conferida: as passagens vão por capítulo e
  coluna da PL.
- Ambrósio, *De paradiso* 13, 63 comenta Gn 3,7, mas o que diz é sobre o estado de 2,25 (versículo marcado: 25).
- Bernardo, *In Septuagesima* 2: a citação de Adão vai na forma do texto que Bernardo leu («Isto, agora, é osso
  dos meus ossos»).

## Para o `autores.json`

Todos os autores já estão lá. `autor_id` usados: `ambrosio`, `beda`, `tomas-de-aquino`, `tertuliano`,
`pedro-crisologo`, `ruperto`, `bernardo`, `gregorio-magno`, `hugo-sao-vitor`, `jeronimo`.

## Para o catálogo `pesquisa/fontes/latinos.md` (ids do Corpus Corporum usados agora)

Tertuliano (texto = obra − 97, conferido): *De anima* **66** (`Tertul.DeAni`), *De resurrectione carnis* **75**
(`Tertul.DeReCa`), *Adv. Marcionem* 63, *De exhortatione castitatis* 69, *De monogamia* 72. Cipriano (também − 97):
*Ad Demetrianum* 117, *De bono patientiae* 118, *De habitu virginum* 119, *De opere et eleemosynis* 124;
*Testimonia* 21445. Pedro Crisólogo, Sermões 7597 (`PetChr.Sermon7`). Bernardo: *In Septuagesima* **11222**
(`BerCla.InSep`), *De diversis* **11257** (`BerCla.SeDeDi2`), *In dedicatione* 11229 (`BerCla.InDeEc`),
*In Purificatione* 11220, *Sententiae* 11256, *In Quadragesima* 11221; os 70 textos de 11189 a 11258 estão no cache.
Ambrósio: *De institutione virginis* **21372** (`AmbMed.DeInVi`), *De virginibus* 21380, *In Lucam* 6965
(`AmbMed.ExEvSeL`), *Expositio in Ps. 118* 6966, cartas classe I 21400 (`AmbMed.EpClI`), classe II 6979.
Pedro Lombardo, *Sententiae* **11468** (`PetLom.Senten12`). Hilário, *Tractatus super Psalmos* 21450. Gaudêncio,
Sermões 7088; Cromácio, *In Matthaeum* 7084; Paulino de Nola, cartas 7718; Fulgêncio, sermões 7816; Quodvultdeus,
cartas 7450; Vitorino de Petávio, *De fabrica mundi* 6800; Pedro Comestor, *Historia scholastica* 11575; Honório,
*Hexaemeron* 10991, *Elucidarium* 10986, *Speculum Ecclesiae* 11000. Para achar o `idno` do texto a partir da obra:
`navigate.php?load=/38/<autor>/<obra>` traz `<text type="text">…<idno>`. São Boaventura não está na PL: Quaracchi
V no archive.org (`doctorisseraphic05bona`, `_djvu.txt` legível, com as notas misturadas).

## Para outros capítulos

- **Gn 3**: Ambrósio, *De paradiso* 12 em diante (a serpente, a mulher, as vestes; PL 14, 300 ss.), e 13, 61
  («as tentações do diabo são cheias de mentira: de tudo o que prometeu, só uma coisa era verdade, e era para
  ferir»); Ruperto, *In Gen.* III, 1–4 (PL 167, 289–292) em diante; Bernardo, *De diversis* 22, 3 (PL 183, 596C–D):
  «Deus afirma, a mulher duvida, Satanás nega» (Gn 3,1-4, forte e curto); Bernardo, *In Septuagesima* 2, 2–3 (PL
  183, 167); Crisólogo, Sermão 148 (PL 52, 597C–598A: «enganada, a virgem enganou o marido»; Gabriel e Maria
  desfazem a obra do anjo mau); Zenão, Tratado I, 6 (*De patientia*), 3 (PL 11, 313C–314B: a impaciência de Adão); Tertuliano, *De res.*
  7 (PL 2, 804A: as túnicas de pele não são os corpos) e Jerônimo, Carta 51, 5 (Epifânio, contra Orígenes: o
  paraíso e os rios são reais; PL 22, 522–523); Ambrósio, Carta 45, 12–17 (PL 16, 1143–1145); Alcuíno, perg. 60 em diante
  (PL 100, 522 ss.); Leão, Sermão 24, 2 (PL 54, 205A–B: «quis ocupar a honra em vez de merecê-la»).
- **Gn 4**: Zenão, Tratado I, 6, 3 (PL 11, 314B–C: «o mundo vazio se espanta de ser pequeno para dois»; Caim).
- **Gn 22**: Gregório, *Hom. in Ez.* I, 6, 15 (PL 76, 835B: Isaac leva a lenha como Cristo a cruz).
