# Gênesis 3: relatório do grupo `gregos` (2026-10-26)

Padres gregos (e Ireneu, no latim antigo onde o grego se perdeu). Ponto de partida: `BASE.md`, os arquivos gregos de
`base/`, as pistas de `../proximos.md` («Gn 3») e o que sobrou de `../002/achados-gregos.json`. **16 achados** em
`achados-gregos.json`, quatro por trecho, cada um com uma ideia própria.

## O que se entregou

| trecho | achado | v. | ideia |
|---|---|---|---|
| 1 | Basílio, *Sobre o jejum* I, 3–4 | 3, 6 | o «não comereis» foi o primeiro jejum; caímos por não jejuar, jejuamos para voltar |
| 1 | Basílio, *Sobre a humildade* 1 | 5 | quis a glória própria de Deus e perdeu a que tinha; volta-se pela humildade |
| 1 | Ireneu, *Adv. haer.* V, 21, 2 | 6 | o inimigo venceu pela comida quem não tinha fome; Cristo faminto o vence no deserto (Mt 4) |
| 1 | Ireneu, *Adv. haer.* III, 23, 5 | 7–8, 21 | as folhas ásperas da figueira, roupa de penitência; a veste do Espírito perdida |
| 2 | Teófilo, *A Autólico* II, 22 | 8, 10 | quem passeava no jardim era o Verbo; a «voz» é o Filho |
| 2 | Crisóstomo, *Hom. in Gen.* 17, 3 | 9–10 | «Onde estás?»: deixei-te vestido de glória e te encontro nu |
| 2 | Crisóstomo, *Hom. in Gen.* 17, 5 | 12–13 | as desculpas provam a liberdade: «deu», não obrigou; «enganou», não forçou |
| 3 | Ireneu, *Adv. haer.* IV, 40, 3 (grego das cadeias) | 15 | Deus devolve contra a serpente a inimizade que ela quis pôr entre o homem e Deus |
| 3 | Justino, *Diálogo* 100, 4–6 | 13, 15 | Eva e Maria; por Cristo, nascido da virgem, Deus destrói a serpente |
| 3 | Crisóstomo, *Sermão 4 sobre o Gênesis*, 1–2 | 16 | antes do pecado, igual honra; o domínio veio do pecado, e Deus o tempera («recurso», refúgio) |
| 3 | Cirilo de Jerusalém, *Cat.* 13, 18–19 | 17–18 (8) | Jesus recebe os espinhos; queda num jardim, salvação num jardim; à tarde |
| 3 | Nazianzeno, *Or.* 38, 12 | 19 (21, 23) | a morte corta o pecado «para que o mal não seja imortal» |
| 4 | Epifânio, *Panarion* 78, 18 | 20 | o nome «mãe dos viventes» logo depois da sentença: figura de Maria |
| 4 | Nissa, *Grande catequese* 8 | 21 (19) | as túnicas = a mortalidade, roupa de fora e passageira; o vaso cheio de chumbo refeito |
| 4 | Teodoreto, *Quaest. in Gen.* 40 | 22 | «como um de nós» é ironia; a árvore negada sem inveja, para deter o pecado |
| 4 | Cirilo de Jerusalém, *Cat.* 13, 31 | 24 | ao bom ladrão: não temas a serpente nem a espada de fogo, que se inclina diante do Senhor |

Os três melhores: **Ireneu IV, 40, 3** (a inimizade «devolvida», leitura funda e pouco conhecida de 3,15), **Crisóstomo
17, 3** («Onde estás?») e **Nazianzeno 38, 12** (a morte que impede o mal de ser imortal).

## Texto, edições e direitos

- **Crisóstomo, Homilias sobre o Gênesis**: grego transcrito da imagem da PG 53 (archive.org `patrologiaecurs24migngoog`):
  col. 137 na página n141, col. 139–140 na n144 (a n143 é o latim). O mapa de Gn 2 continua valendo: as páginas gregas e
  latinas se alternam sem regra fixa; procurar em `cache/genesis/gregos/ia/pg053-pags.json`.
- **Basílio** (*Sobre o jejum* I; *Sobre a humildade*): a khazarzar **não tem** essas homilias. Grego transcrito da imagem
  da PG 31 (`patrologicursus02migngoog`, n83 = col. 167–168; n257 = col. 525–526). O OCR local `ia/pg031.txt` é dessa
  digitalização.
- **Achar a página de uma passagem num volume da PG do archive.org**: baixar `<id>_hocr_searchtext.txt.gz` e
  `<id>_hocr_pageindex.json.gz` (poucos MB) e buscar o latim; o índice da página é o `n` do BookReader. Script em
  `~/.cache/taioe-gn3/gregos/hocr.py` (fora do repositório); os arquivos baixados ficaram em `cache/genesis/gregos/hocr/`.
  Imagem da página: `https://archive.org/download/<id>/page/n<n>.jpg` (3–4 MB; recortar por coluna antes de ler).
- **Ireneu**: III, 23, 5 e V, 21, 2 só em latim (Harvey II, p. 128 e pp. 381–382); colunas da PG 7 conferidas na imagem
  (`bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1857_7`: n483 = 963–964, n560 = 1113–1114,
  n593 = 1179–1180; n482 = 961–962). **IV, 40, 3 tem o grego das cadeias** na PG 7, 1113–1114 (Grabe), usado no achado;
  o trecho entre colchetes (o resto de Gn 3,15) a PG supre pelo latim. O id `patrologiaecur07mign` do archive.org **não é a
  PG 7** de Ireneu.
- **Teodoreto q. 40**: grego da imagem da PG 80 (n70 = col. 141–142); igual à ed. Fernández Marcos.
- **Epifânio**: PG 42, 728–729 pelo OCR (bom neste trecho), igual a Holl; segui a PG («αὐτὴ ἡ ζωή» pela nota dela).
- **Textos digitais da khazarzar usados como estão** (edições antigas, domínio público): Nazianzeno 38 (PG 36), Nissa,
  *Grande catequese* (sem colunas da PG; conferido com o latim da PG 45), Cirilo de Jerusalém (Reischl–Rupp), Justino,
  Crisóstomo *Sermões*. Correções de erros do texto digital anotadas no campo `edicao` (Justino «ἄνθρωπον», «Εὔα»,
  «ῥῆμα»; Nazianzeno «ἣν προσήγαγεν ὡς»; Teófilo «τόπος»).
- **Colunas a conferir**: Teófilo II, 22 (PG 6, 1087–1088), Justino 100 (PG 6, 709–712), Cirilo *Cat.* 13, 18–19
  (PG 33, 796–797) e 13, 31 (PG 33, 809–812), Nissa *Or. catech.* 8 (PG 45, 33–37). O hOCR do archive.org não achou esses
  trechos (o latim das digitalizações de PG 6 e 33 não bateu); o texto, porém, vem de edição digital, não de OCR.

## Dúvidas para a revisão

- **Basílio, humildade**: «τὴν τῆς θείας δόξης ἐπιθυμίαν μετέθηκε» é ambíguo («mudou o desejo da glória divina»);
  traduzi como «passou a desejar a glória que é própria de Deus», que é o sentido do contexto e do latim.
- **Crisóstomo, Sermão 4**: ἀποστροφή (LXX, 3,16) traduzido por «recurso», porque ele mesmo o explica como refúgio e
  porto; o nosso texto diz «o teu desejo será para o teu marido». O Sermão cita como «aos coríntios» os versos de Ef 5:
  cortei a frase com […]. O começo do domínio do marido como «servidão» pode soar duro; deixei a parte em que Deus o
  tempera e Paulo o transforma em amor.
- **Cirilo 13, 19**: «μέχρι ξύλου ἡ ἁμαρτία» traduzido como «o pecado durou até o lenho da cruz» (explicita «da cruz»).
- **Ireneu V, 21, 2**: «repletio … per duplicem gustationem» = «a fartura … quando os dois provaram do fruto»
  (interpretação: Eva e Adão).
- **Justino**: o excerto começa no meio da frase («… e que se fez homem por meio da virgem»); na tradução, sujeito
  explícito: «O Filho de Deus».
- **Nazianzeno e Teodoreto** tocam a mesma ideia (a morte que detém o pecado); por isso cortei de Teodoreto a frase «a
  morte é remédio, não castigo» e o deixei só com a ironia de 3,22 e a árvore negada sem inveja.

## O segundo de cada par (ficou de fora, para não repetir)

- **Ireneu III, 23, 6** (PG 7, 964A–B): Deus não interroga a serpente e a amaldiçoa primeiro; odeia o sedutor e tem
  piedade do seduzido; afasta-o da árvore da vida «para que o pecado não fosse imortal». Diz o mesmo que Nazianzeno 38, 12
  (mais claro) e, na parte da serpente, o mesmo que Crisóstomo *Hom.* 17, 6.
- **Ireneu III, 23, 7** (PG 7, 964B–C) e **V, 21, 1** (PG 7, 1179–1180): o protoevangelho como recapitulação («não teria
  sido vencido com justiça se não fosse um homem nascido de mulher»). IV, 40, 3 diz o essencial, em grego.
- **Ireneu III, 22, 4** (PG 7, 959–960): «o nó da desobediência de Eva foi desatado pela obediência de Maria». Muito
  conhecido (está em *Lumen gentium* 56 e no Catecismo 494): fica para o grupo `modernos`, que citará esses textos; Justino
  e Epifânio cobrem Eva e Maria aqui.
- **Teófilo II, 26** (BKV, divisão 43): a expulsão como benefício, para não ficar para sempre no pecado e ser chamado de
  volta depois da correção; o vaso refeito pela morte; «Onde estás?» como ocasião de arrependimento e confissão. Os três
  pontos estão em Nazianzeno, Nissa e Crisóstomo 17, 3; Teófilo é o mais antigo e o mais breve: bom substituto se o
  Gere quiser menos texto.
- **Crisóstomo, *De cruce et latrone* I, 2** (PG 49, 401) e II, 2 (PG 49, 409–410): o paraíso fechado há cinco mil anos
  aberto hoje; Cristo, senhor dos querubins e da espada de fogo. Diz o mesmo que Cirilo, *Cat.* 13, 31.
- **Cirilo de Jerusalém, *Cat.* 2, 7**: Deus expulsa Adão, mas o faz morar diante do paraíso, para que, vendo de onde caiu,
  se salve pela penitência. Depende do «κατῴκισεν αὐτὸν ἀπέναντι τοῦ παραδείσου» da LXX (3,24), que não está no nosso
  texto (o mesmo vale para o fim de Teodoreto q. 40).
- **Cirilo, *Cat.* 13, 2**: «se pela árvore do alimento foram expulsos do paraíso, pela árvore de Jesus os que creem
  entrarão mais facilmente».
- **Crisóstomo, *Hom.* 17, 4** (o homem, cabeça da mulher, inverteu a ordem) e 17, 6–7 (a serpente amaldiçoada, como a
  espada que o pai quebra depois de matar o filho): bons, mas longos; e **Teodoreto q. 37** («Que há de cruel em “és
  terra”?»: «da terra te formei e te elevei a uma natureza melhor; não quiseste guardar o mandamento: volta à primeira»).
- **Crisóstomo, *Hom.* 16, 1** (a veste de glória, 2,25), que ficou de fora de Gn 2: o mesmo tema está em 17, 3.

## O que não se achou ou não se leu a fundo (pistas)

- **Ireneu, *Demonstração* 16–17 e 31–33**: só em armênio; as traduções inglesas de domínio público (Robinson, 1920) não
  foram procuradas. Pista para quem precisar.
- **Atanásio, *De incarnatione* 4–5** (a volta ao nada, a corrupção; o 3 já saiu em Gn 2) e ***Contra os pagãos* 2–3**:
  não lidos para este capítulo.
- **Basílio, *Deus não é autor dos males* 7–9** (`txt/basilio-quod-deus.txt`): não lido; provavelmente repete a morte como
  remédio. **Basílio, *Sobre o jejum* II**: não procurado.
- **Nazianzeno, *Or.* 2, 25** e **45, 8**: o 45, 8 repete 38, 12 quase palavra por palavra (PG 36, 632–633).
- **Nissa, *De virginitate* 12–13** (as túnicas, a volta ao paraíso): não lido; o PDF está na khazarzar
  (`Gregory of Nyssa_PG 44-46/De virginitate.pdf`).
- **Cirilo de Alexandria, *Glaphyra*, «Περὶ τοῦ Ἀδάμ»** (em `base/`): lido só de passagem; nada que superasse os escolhidos.
- **Máximo** (*Questões a Talássio* 61, o prazer e a dor; *Ambigua* 10), **Damasceno** (*Exposição da fé* II, 30; homilias
  da Dormição), **André de Creta** (*Grande Cânon*), **Anastásio Sinaíta**, **Metódio**: não procurados.
- **Procópio** (`base/`): é cadeia; não há nele trecho de Padre identificado que não esteja nos originais acima.
- **Orígenes** (`base/`): só escólios curtos; nada escolhido.

## Para outros capítulos

- **Gn 4**: Crisóstomo, *Hom.* 18, 6 («Por que estás triste?»: Deus estende a mão a Caim como a Adão com «Onde estás?»); Ireneu III, 23, 4 (Caim, que responde com insolência «a Deus que sabe tudo», PG 7, 962C–963A);
  Teodoreto q. 41–43 (a tristeza de Caim, o sinal, a mulher de Caim); Cirilo de Jerusalém, *Cat.* 2, 7 (Caim: «grande o
  pecado, pequena a condenação»).
- **Gn 6–9**: Cirilo de Jerusalém, *Cat.* 2, 8 (os cem anos de paciência antes do dilúvio); Crisóstomo, *Sermão* 4, 2 (a
  segunda servidão, a de Cam, Gn 9).
