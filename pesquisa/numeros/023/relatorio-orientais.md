# Números 23: relatório da pesquisa nos orientais não gregos (siríacos, armênios, coptas, etíopes, liturgia)

Pesquisa de 2026-11-02 (retomada de uma tentativa que caiu sem entregar; o que ela achou foi aproveitado). 3 achados em
`achados-orientais.json` (trecho 1: 2; trecho 2: 1), todos do Efrém atribuído da ed. romana. Originais novos em
`textos/efrem-in-numeros-23.md` e `textos/efrem-in-michaeam-23.md`. Scripts em `~/.cache/taioe-nm23/orientais/` (`corpus.py`,
`janela.py`: Digital Syriac Corpus; `bedjan.py`, `prox.py`: OCR dos cinco volumes de Bedjan; `lat.py`, `ocr.py`: latim de Assemani;
`montar23.py`: monta o JSON; `ler_log.py`, `ler_res.py`: leitura do registro da tentativa anterior). Imagens e downloads em
`pesquisa/cache/numeros23-orientais/` (no D:).

**Páginas no archive.org**: Assemani, t. I (Syr 1), p. 264 = n284, p. 265 = n285 (p = n − 20); t. II (Syr 2), p. 281 = n305.

Os orientais deste capítulo são poucos: nenhum Padre siríaco ou armênio em domínio público comenta os oráculos de Nm 23 fora do
Efrém atribuído; o resto fala de Balaão pela jumenta (Nm 22) ou pela estrela (Nm 24,17). Não forcei.

## O que entrou (3)

Trecho 1 (vv. 1–12):
1. **Efrém atribuído, *In Num.* XXIII** (Assemani I, p. 264 D–F) (vv. 7–8.11), rel. 3: por que Deus não deixou Balaão amaldiçoar:
   para que a peste que o povo ia atrair com o próprio pecado (Nm 25) não fosse atribuída ao adivinho, e ninguém julgasse que os
   adivinhos têm um poder divino «que não têm»; nem Balaão se gabasse dela. E pergunta: precisava amaldiçoar? Depois da bênção, o
   povo foi castigado «não com palavras, mas com fatos». Bom para «quem Deus abençoa ninguém amaldiçoa» e contra a superstição.
2. **Efrém atribuído, *In Num.* XXIII** (p. 264 F – 265 B) (v. 10b), rel. 2: «Seja o meu fim semelhante ao deles» se cumpre ao
   avesso: os hebreus que pecaram morreram na peste, e Balaão caiu à espada na guerra contra Madiã (Nm 31,8); «a bênção se mudou
   em maldição para uns e para o outro». Leitura própria do v. 10, diferente da de Orígenes e dos sermões sobre a boa morte; mas
   o raciocínio é um tanto torcido (o «deles» passa a ser os israelitas que pecaram): se o Gere achar confuso, fica de fora.

Trecho 2 (vv. 13–30):
3. **Efrém atribuído, *In Mich.* 6,5** (Assemani II, p. 281 B–C) (vv. 8.19), rel. 3: Balaão respondeu a Balac «porque conhecia a
   justiça do Senhor», isto é, «a sua fidelidade e a sua verdade: Deus não muda o que decretou, nem desmente o que prometeu». Cita
   Nm 23,19 pela Peshitta («ele diz e faz, e a sua palavra permanece para sempre»). Siríaco transcrito da imagem, sem vogais; uma
   palavra ilegível ficou no [...].

Os dois primeiros têm o original em latim (a tradução da ed. romana), como os de Nm 20: o siríaco ao lado foi lido na imagem só nas
frases-chave do primeiro (confirma o latim) e não foi transcrito por inteiro; o OCR siríaco do archive.org é ilegível.

## Como se procurou

- **Registro da tentativa anterior** (caiu às 15h16 por falta de internet): tinha extraído a Peshitta de Nm 23, buscado Balaão em
  todo o Digital Syriac Corpus e no OCR de Bedjan, achado o cap. XXIII do Efrém atribuído (Assemani I, p. 264–265) e começado a busca
  em Eznik e no Wikisource armênio. Retomei daí.
- **Digital Syriac Corpus** (~630 textos): «Balaão» (65 ocorrências, 40 de Dionísio bar Salibi) e as frases da Peshitta de Nm 23
  (vv. 8, 9, 10, 13, 19, 21, 23, 24): nenhuma citação de Nm 23 fora de Dionísio, Narsai, Isaac de Nínive e Filoxeno (proibidos).
- **Pistas da pré-pesquisa** (`base/_pistas-orientais.md`), conferidas e descartadas: Afraates, *Dem.* 3, § 14 (vv. 6.17) é o anjo
  que apareceu à jumenta de Balaão (Nm 22) e as palavras coincidem por acaso; *Dem.* 15, § 7 (v. 22) é só «Deus os tirou do Egito»;
  Efrém, *Contra Marcião* (v. 13): no texto não há Balaão nem as palavras de Nm 23,13 (coincidência do achado automático).
- **Jacó de Sarug**: busca de ܒܠܥܡ e das frases de Nm 23 no OCR dos cinco volumes de Bedjan (sem espaços, com letras trocáveis).
  Quase todas as ocorrências são falsas (ܒܠܥ, «engolir»; ܠܘܩܒܠ ܥܡܐ). As verdadeiras: o memra «Sobre a estrela que os magos viram»
  (I, pp. 96–98: Nm 24,17), a jumenta de Balaão (III, p. 758; IV, p. 188) e B1 p. 510 (a conferir, provavelmente Nm 22). **Não há
  memra sobre Balaão nos volumes de Bedjan**: nenhum título nem texto corrido. Há homilias inéditas (lista de Akhrass, 2015; ed.
  Akhrass e Syryany, 2017, com direito); não conferido.
- **Efrém, outras obras**: Assemani I–III (latim do OCR), Lamy I–IV (latim do OCR; `sanctiephraemsy00`, `02`, `04` e `03lamygoog`): fora do
  comentário a Números e do de Miqueias, Balaão só pela jumenta e pela estrela; nada de «morte dos justos», do unicórnio, dos agouros
  nem de «Deus não é homem».
- **Armênios**: Eznik de Kolb, *Contra as seitas* (tradução alemã de Schmid, 1900, e francesa de Le Vaillant de Florival, 1853;
  OCR do grabar ilegível): trata da magia, dos encantadores e dos astrólogos, mas não cita Balaão nem Nm 23. Wikisource armênio:
  Balaão só em autores modernos e em Aristakes Lastivertsi (historiador do séc. XI, não Padre). Gregório de Narek e Nerses Shnorhali:
  nada achado na web.
- **Coptas, etíopes, liturgia siríaca e armênia**: sem texto pesquisável em domínio público; a hinografia que conheço cita Balaão
  pela estrela (Natal, Epifania), Nm 24.

## O que não existe

- Comentário autêntico de Efrém a Números (já anotado em `base/_ausentes-numeros.md`); o atribuído **tem** o cap. XXIII (só os
  vv. 10–11): o corte automático não o achou porque o cabeçalho da página diz «CAP. XXII. v. 13. CAP. XXIII. v. 10.».
- Memra de Jacó de Sarug sobre Balaão nos volumes de Bedjan (ver acima).
- Balaão em Eznik.

## Só pista (proibidos no site)

- Dionísio bar Salibi, comentário literal a Números (em `base/`), glosas aos vv. 3–27.
- Isaac de Nínive, *Discurso* 19 (corpus 410, p. 158): a adivinhação «foi dada» a Balaão.
- Narsai, «Sobre Sansão» (corpus 101) e «A cananeia» (corpus 59, «as palavras de Balaão se cumpriram»).
- Filoxeno, *Discurso* 10, bloco 65 (a pista do v. 19), não lido.

## Para outros capítulos

- **Nm 22** (para o grupo que procura o memra de Jacó de Sarug sobre Balaão: não está em Bedjan): Efrém atribuído, *In Num.* XXII
  (Assemani I, p. 264 A–C, n284): Balaão não pôde amaldiçoar «para mostrar que Satanás não pode fazer mal aos justos»; a jumenta,
  batida três vezes e não ferida, é tipo da natureza humana, carroça do diabo, que ao ver o Esposo sacode o jugo e vira carro de
  Cristo. Afraates, *Dem.* 3, § 14 (o anjo da jumenta é Miguel, o mesmo de Josué); *Dem.* 8, § 9 e *Dem.* 11, § 9 (Moab alugou
  Balaão). Efrém, *Nísibis* 54, § 8 (o anjo no caminho). Jacó de Sarug, Bedjan III, p. 758, e IV, p. 188 (a jumenta); B1 p. 510 a
  conferir. Assemani III (Efrém, latim): a jumenta que falou (n150, n232).
- **Nm 24**: Jacó de Sarug, «Sobre a estrela que os magos viram» (Bedjan I, pp. 96–98; corpus 345, blocos 275–286): os magos acharam
  nos seus livros a profecia que Balaão disse a Balac; os povos tinham Balaão por grande, e por isso creram na palavra dele.
  Efrém, *Natal* 1, § 5 e 24, § 20; Assemani II, n420 (hino de Natal). Efrém atribuído, *In Num.* XXIV (Assemani I, p. 265 B–C):
  a estrela é Cristo, e, no sentido literal, Zorobabel; Nm 24,24, Antíoco; *In Dan.* (Assemani II, n250): Nm 24,24. Afraates,
  *Dem.* 14, § 11 (Nm 24,21, os quenitas). Assemani I, p. 264 E: Nm 24,9 lido como ameaça ao rei Balac.
- **Nm 25**: Efrém atribuído, *In Num.* XXV (Assemani I, p. 265 C–F): Fineias, figura de Cristo, que trespassa o diabo com a lança da
  cruz; Zambri, figura do diabo, «que nenhum poder pôde frear»; «cessando o pecado, cessou a praga».
