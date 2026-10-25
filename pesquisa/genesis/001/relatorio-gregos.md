# Gênesis 1: relatório da pesquisa nos Padres gregos

Pesquisa de 2026-10-25. Resultado: **20 achados** em `achados-gregos.json` (15 com relevância 3, 5 com 2), todos «domínio
público»; por trecho: 1 (vv. 1–5) = 4; 2 (vv. 6–13) = 3; 3 (vv. 14–19) = 3; 4 (vv. 20–23) = 2; 5 (vv. 24–31) = 8. Autores:
São Basílio 11 (9 do *Hexaémeron* e 2 da homilia atribuída *Sobre a origem do homem*), São Teófilo de Antioquia 5, São Gregório
de Nissa, Santo Ireneu, Teodoreto e São João Crisóstomo 1 cada. Não havia pré-pesquisa do Gênesis: os textos gregos de Gn 1
estão agora em `base/` (lista abaixo), cortados por scripts novos que servem aos próximos capítulos.

## Onde se procurou

- **Base nova** (`base/`, gravada pelos scripts `pesquisa/ferramentas/base/gen-gregos-*.py`, com o módulo comum `_gen_gregos.py`):
  `basilio-hexaemeron.md` (as 9 homilias inteiras, com a coluna da PG 29 de cada parágrafo, aproximada), `basilio-origem-homem.md`
  (as duas homilias atribuídas), `nissa-de-opificio-hominis.md` (prólogo e caps. 1–18 e 22), `nissa-apologia-in-hexaemeron.md`,
  `crisostomo-sermones-in-genesim.md` (sermões 1–4, grego), `crisostomo-homiliae-in-genesim.md` (homilias 1–10, **só o latim** da
  PG), `teodoreto-quaestiones-in-genesim.md` (perguntas I–XXI), `cirilo-glaphyra-in-genesim.md` (o «Περὶ τοῦ Ἀδάμ»),
  `teofilo-ad-autolycum.md` (II, 10–18), `origenes-in-genesim.md` (homilia 1 em latim de Rufino; os fragmentos gregos dos
  *Commentarii*; as *Selecta*), `damasceno-expositio-fidei.md` (caps. 16–26 de Kotter), `severiano-sermo-valde-bona.md`,
  `procopio-commentarii-in-genesim.md` (OCR da PG 87/1). Mais `_ausentes-gregos.md` e `_pistas-gregos.md`.
- **Fontes**: khazarzar (Ψηφιακή Πατρολογία) para Basílio, Nissa, os sermões de Crisóstomo, Teodoreto, Cirilo, Orígenes,
  Damasceno e Severiano (PDFs baixados um por vez e apagados depois da conversão com o `pdftotext`; o PyMuPDF do
  `gregos-limpar.py` não está instalado no Ubuntu, e o módulo comum refaz a mesma limpeza); First1KGreek para Teófilo (ed.
  Otto, 1861) e a BKV de Friburgo para ler cada capítulo (texto de Grant); archive.org para conferir colunas e leituras (OCR da
  PG 6, 29, 44, 53 latina, 80, 87/1; Harvey II para Ireneu; GCS 29 para Orígenes). Para ler depressa, usei também, só para
  leitura, o corpus grego já convertido de uma conversa anterior neste PC (scratchpad `4b54597f-…/p-gregos/`, temporário).
- **Lido para escolher**: as 9 homilias de Basílio, *De opificio* 1–5, as homilias *Sobre a origem do homem* I (inteira) e II
  (começo), os sermões 1–4 de Crisóstomo, Teófilo II, 10–19, Teodoreto q. I–XXI, o sermão de Severiano, Damasceno II, 2 e II,
  12, Ireneu IV, 38 e V, 16 (fragmentos gregos), Cirilo de Jerusalém, *Cat.* 3, 5 e 11, 23, Nazianzeno, *Or.* 38, 9–11 e 44,
  4–6, Atanásio, *De inc.* 3.

## O que entrou (uma linha cada)

- **Trecho 1 (vv. 1–5)**: Basílio, *Hex.* 1, 2 (o nome de Deus posto como selo na primeira linha; o mundo tem começo e autor;
  o oleiro que não se esgota); Teófilo II, 10 (Deus, que de nada precisa, fez tudo do nada para ser conhecido pelo homem; o
  «princípio» é a sua Palavra); Basílio, *Hex.* 2, 6 (o Espírito Santo «pairava» como a ave que choca os ovos, citando «um
  sírio»); Basílio, *Hex.* 2, 8 («dia um» e não «primeiro»: a eternidade, o oitavo dia, o domingo).
- **Trecho 2 (vv. 6–13)**: Basílio, *Hex.* 4, 6–7 (Deus vê o mar com a sabedoria; mais bela que o mar é a assembleia da Igreja,
  cuja oração sobe como as ondas na praia); *Hex.* 5, 10 (a ordem «Faça a terra brotar» continua na natureza como o pião que
  gira depois do golpe); *Hex.* 5, 6 (a rosa sem espinhos antes do pecado).
- **Trecho 3 (vv. 14–19)**: Teófilo II, 15 (as plantas antes do sol, para que ninguém o adore; o sol figura de Deus, a lua do
  homem e da ressurreição; os três dias, figura da Trindade: é o primeiro uso cristão da palavra Τριάς); Basílio, *Hex.* 6, 1 (se
  este sol é tão belo, quanto mais o Sol da justiça); *Hex.* 6, 4–7 (os astros são sinais do tempo, não do destino: sem
  liberdade acabam a lei, o juízo e a esperança cristã).
- **Trecho 4 (vv. 20–23)**: Teófilo II, 16 (a primeira bênção, dada aos seres das águas: figura do batismo); Basílio, *Hex.* 7, 5 (o
  ouriço-do-mar e a providência: «se Deus não deixou o ouriço fora do seu cuidado, não cuidará das tuas coisas?»).
- **Trecho 5 (vv. 24–31)**: Teófilo II, 18 (o «Façamos» mostra a dignidade do homem, único digno das mãos de Deus; dito à
  Palavra e à Sabedoria; o alimento só de plantas, vv. 29–30); Nissa, *De opif.* 2 (o homem por último, como o convidado que
  entra quando a mesa está posta); Basílio (atribuído), *Sobre a origem do homem* I (a imagem dada, a semelhança conquistada:
  o retrato e o pintor); Ireneu V, 16, 2 (o Verbo feito carne mostrou a imagem e restituiu a semelhança); Basílio (atribuído),
  *Sobre a origem do homem* I («homem e mulher os fez»: a mulher também é imagem; a diferença está nas cortinas do corpo);
  Teodoreto, *Quaest. in Gen.* 20 (o homem imagem porque governa e porque cria, à imitação do Criador: o trabalho humano);
  Crisóstomo, *Sermão 3 sobre o Gênesis* (dominar as feras de dentro: quem amansa o leão pode amansar a ira); Teófilo II, 17 (a
  bênção guardada para o homem; tudo era «muito bom»; as feras ficaram ferozes com o pecado do homem e voltarão à mansidão).

## Atenção na seleção (sobreposições)

- **Peso de Basílio**: 11 dos 20 são dele (o *Hexaémeron* é o comentário grego por excelência de Gn 1). Se a montagem quiser
  variar os autores, as trocas de mesmo conteúdo são: Basílio 6, 4–7 → Orígenes, *Comm. in Gen.* III (Gn 1,14 contra o destino;
  escritor eclesiástico); Basílio 2, 8 → Nazianzeno, *Or.* 44 (o domingo novo); Basílio 7, 5 → nenhum outro grego sobre os seres
  das águas que ainda fale ao leitor.

- **Com os latinos**: Basílio 5, 6 (a rosa) é a fonte de Ambrósio, *Hex.* III; ficar com um só. Basílio 2, 6 (a ave que choca)
  está também em Ambrósio e em Jerônimo, *Quaest. hebr.* (o *merahefet*); Basílio é o original e cita «o sírio». Basílio 6, 4–7
  (contra os horóscopos) e Ambrósio, *Hex.* IV, 4 / Agostinho dizem quase o mesmo. Teófilo II, 16 (a bênção das águas e o
  batismo) e Tertuliano, *De baptismo* 1–4: ângulos diferentes (Teófilo: a primeira bênção; Tertuliano: os «peixinhos»).
- **Com os orientais**: Basílio 2, 6 cita um sírio (Santo Efrém, segundo a nota de Garnier na PG 29); se os orientais trouxerem o
  *Comentário ao Gênesis* de Efrém sobre o mesmo ponto, escolher um.
- **Com os modernos**: Basílio (atribuído), «homem e mulher», e *Mulieris dignitatem* 6–7; Teodoreto (o homem que cria) e
  *Laborem exercens* 4; Crisóstomo (o domínio por dentro) e *Laudato si'* 67.
- **Dentro do grupo**: a imagem e a semelhança têm três achados com ângulos diferentes (Basílio: a semelhança se conquista; Ireneu:
  Cristo revela a imagem e devolve a semelhança; Teodoreto: governar e criar); o «Façamos» tem Teófilo (dignidade, a Palavra e a
  Sabedoria) e, de reserva, Basílio, *Hex.* 9, 6 (a Trindade revelada quando se fala do homem).

## Reservas (bons, mas dizem o que outro já diz ou ficaram fora do limite de 20)

- Basílio, *Hex.* 2, 7 («Faça-se a luz. E a ordem já era obra»: a «voz» de Deus é o impulso da vontade; a luz bela aos olhos de
  Deus pelo proveito que traria). O único bom sobre o v. 3 no grupo; entra se os latinos não cobrirem bem a luz.
- Basílio, *Hex.* 3, 10 (o artista que louva cada parte antes de juntar a estátua: Deus louvará o mundo inteiro quando estiver
  completo; prepara o «muito bom» do v. 31).
- Basílio, *Hex.* 5, 1 (a terra produz antes do sol, para que deixem de adorá-lo): o mesmo de Teófilo II, 15.
- Basílio, *Hex.* 7, 3–4 (os peixes ficam nos seus limites, e até os grandes monstros marinhos ficam no alto-mar; nós é que
  mudamos as divisas do vizinho): bom para os «monstros marinhos» do v. 21.
- Basílio, *Hex.* 9, 6 (o «Façamos» e a Trindade: «enquanto não aparecia quem seria instruído, a pregação da Trindade estava
  escondida; quando se espera a criação do homem, a fé se descobre»). Cuidado: o parágrafo tem uma passagem dura contra os
  judeus, que deve ficar fora do corte.
- Teófilo II, 14 (o mundo como o mar: as ilhas com portos são as igrejas, as ilhas de pedra são as heresias): o mesmo campo de
  Basílio 4, 7.
- Nissa, *De opif.* 4 (o homem é rei por ser imagem do Rei: em vez da púrpura, a virtude; do cetro, a imortalidade; do diadema,
  a justiça) e 5 (as cores da imagem são as virtudes; «Deus é amor»: sem amor, todo o traço da imagem se desfaz).
- Crisóstomo, *Sermão 2 sobre o Gênesis* (o «Façamos» é honra: o homem entra por último como o rei numa cidade preparada; Deus
  o amou a ponto de não poupar o Filho). Cuidado: o fim do sermão diz que só o varão é imagem «pelo governo»: não usar.
- Basílio (atribuído), *Sobre a origem do homem* I, sobre «dominai os peixes e as feras»: as feras de dentro (a ira que late como
  um cão, o rancor como uma víbora): o mesmo de Crisóstomo, *Sermão* 3.
- Ireneu IV, 38, 3 (grego; Harvey II, 296): o homem chega aos poucos à imagem e semelhança, «o Pai aprovando e mandando, o Filho
  executando, o Espírito alimentando e fazendo crescer».
- Damasceno, *Exposição da fé* II, 2 e II, 12; Atanásio, *De inc.* 3, 3; Cirilo de Jerusalém, *Cat.* 3, 5 («o começo do mundo
  é a água, e o começo dos Evangelhos é o Jordão»); Severiano, sermão sobre o «muito bom»; Orígenes, *Hom. in Gen.* 1, 13 (a
  imagem do Salvador) e *Comm. in Gen.* III (Gn 1,14, contra o destino); Nazianzeno, *Or.* 38, 11. Lugares e links em
  `base/_pistas-gregos.md`.

## Texto, edições e direitos

- **Teófilo**: o texto digital de Otto no First1KGreek tem três erros de transcrição, corrigidos pela PG 6 (latim de Maran,
  conferido no OCR): II, 10 «τόκος» → **τόπος** («sibi ipse locus»); II, 15 «τύπῳ» → **τόπῳ** («quarto loco»); II, 18 «ἀΐδιον»
  → **ἰδίων** («propriis manibus»). Em II, 17 fica **θηριοῦσθαι** (Otto, seguindo a nota de Maran; a PG e Grant leem
  θηρεύεσθαι): «as feras se chamam assim por se terem tornado ferozes». O link de cada achado abre o capítulo na BKV (texto de
  Grant, 1970, quase igual). As colunas da PG 6 são estimadas pelos cabeçalhos do OCR (II, 10 ≈ 1063; II, 15–17 ≈ 1076–1082).
- **Basílio, Hexaémeron**: o PDF segue Giet (SC 26), que reproduz o texto de Garnier (PG 29); conferi alguns trechos no OCR da
  PG 29 (iguais). As colunas de cada parágrafo foram estimadas pelos cabeçalhos do OCR: estão «a conferir» (erro de ±2).
- **Basílio (atribuído), Sobre a origem do homem I**: o original vem da **PG 44** (OCR conferido palavra por palavra com a ed.
  Hörner da khazarzar), porque o PDF segue a edição moderna. Diferenças: a PG lê «ἐν τῷ **Χριστιανὸς** γενέσθαι» («quando me torno
  cristão»), Hörner «χρηστὸς» («bom»); e um trecho que o OCR não deixa ler («ἵνα … ᾖ τῆς ἐργασίας μισθός»; Hörner: «ἰσάγγελος»;
  o latim da PG: «quo merces operis nostra foret») ficou fora, com […]. Autoria discutida: Basílio (SC 160), Nissa (PG 44) ou outro
  capadócio; o achado diz «atribuída».
- **Ireneu V, 16, 2**: o grego, conservado nos *Sacra Parallela* de Damasceno, está em Harvey (II, 368) e termina em «τῷ ἀοράτῳ
  Πατρί»; o latim continua «per visibile Verbum» («por meio do Verbo visível»), que ficou fora para o original e a tradução
  coincidirem.
- **Teodoreto**: o PDF segue Fernández Marcos–Sáenz-Badillos (1979), como nos capítulos de Números (lá marcado «domínio
  público», com as colunas da PG 80); pergunta XX = PG 80, 104–108 pelo OCR.
- **Crisóstomo, Homilias sobre o Gênesis**: a khazarzar não as tem, e o OCR grego da PG 53 é ilegível (o latim, também, na
  edição greco-latina). Em `base/` ficou o latim da edição só latina de 1859. Para citar uma delas, transcrever o grego da
  imagem (archive.org, patrologiaecurs24migngoog).
- **autores.json**: falta **«São Teófilo de Antioquia»** (sugestão: «bispo de Antioquia (séc. II), autor do primeiro comentário
  cristão aos seis dias da criação», oriental: sim). Os outros já estão («São Basílio Magno», «São Gregório de Nissa», «Santo
  Ireneu de Lião», «Teodoreto de Ciro», «São João Crisóstomo»).

## Tabela das fontes

| autor | obra | onde | situação |
|---|---|---|---|
| Basílio | *Hexaémeron* 1–9 | khazarzar (Giet); PG 29, 4–208 | base/; 9 achados |
| Basílio (atrib.) | *Sobre a origem do homem* I–II | khazarzar (Hörner); PG 44, 257–298 | base/; 2 achados (texto da PG) |
| Teófilo | *Ad Autolycum* II, 10–19 | First1KGreek (Otto); BKV (Grant); PG 6 | base/; 5 achados |
| Nissa | *De opificio hominis* | khazarzar (PG 44, 124–256) | base/; 1 achado; caps. 4–5 de reserva |
| Nissa | *Apologia in Hexaemeron* | khazarzar (PG 44, 61–124) | base/; física antiga, nada para o leitor comum |
| Crisóstomo | *Sermões sobre o Gênesis* 1–9 | khazarzar (PG 54, 581–630) | base/ (1–4); 1 achado |
| Crisóstomo | *Homilias sobre o Gênesis* 1–67 | só PG 53–54 (archive.org) | base/ só em latim; grego ilegível; pista |
| Teodoreto | *Quaestiones in Genesin* | khazarzar (Fernández Marcos) | base/ (q. I–XXI); 1 achado |
| Ireneu | *Adv. haer.* IV, 38; V, 16 | Harvey II; khazarzar (fragmentos) | 1 achado; IV, 38, 3 de reserva |
| Cirilo de Alexandria | *Glaphyra in Genesim* | khazarzar (PG 69) | base/ («Περὶ τοῦ Ἀδάμ», mais Gn 2–3); nada para Gn 1 |
| Orígenes | *Hom. in Gen.* 1; *Comm.*; *Selecta* | GCS 29 (OCR); khazarzar | base/; pistas |
| Damasceno | *Exposição da fé* II, 2–12 | khazarzar (Kotter) | base/; reserva |
| Severiano (atrib.) | sermão sobre o «muito bom» | khazarzar (PG 56, 519–522) | base/; reserva (= Teófilo II, 17) |
| Severiano | *In mundi creationem* 1–6 | PG 56, 429–500 (não na khazarzar) | pista |
| Procópio | *Commentarii in Genesin* | OCR PG 87/1, 33–140 | base/; catena |
| Dídimo | *In Genesim* (Tura) | SC 233 (ed. moderna) | não guardado; pista |
| Nazianzeno | *Or.* 38, 9–11; 44, 4–6 | khazarzar (PG 36) | pistas |
| Atanásio | *De incarnatione* 3 | khazarzar | pista |
| Cirilo de Jerusalém | *Cat.* 3, 5; 9; 11, 23 | khazarzar (PG 33) | pistas |
| Clemente, Máximo, Anastásio Sinaíta | — | — | sem comentário próprio útil (ver ausentes e pistas) |

## Scripts para os próximos capítulos

Todos com o capítulo como parâmetro (`python3 -I pesquisa/ferramentas/base/gen-gregos-<autor>.py 2`, ou `2-11`) e o uso no
topo; baixam para `pesquisa/cache/genesis/gregos/` (fora do git) e apagam os PDFs depois da conversão. Rodar
`gen-gregos-fechar.py <cap>` no fim (junta ausentes e pistas, mantendo o que a pesquisa escreveu à mão).

- `gen-gregos-crisostomo.py`: sermões 1–9 (tabela por capítulo) e homilias 1–67 (pelo capítulo dos cabeçalhos «IN CAP. … GENES.»
  da PG latina; testado em Gn 1: homilias 1–10).
- `gen-gregos-teodoreto.py`: perguntas por capítulo, pelas citações da LXX (Gn 1 = I–XXI; Gn 2 = XXII–XXX; Gn 3 = XXXI–XLIII…).
- `gen-gregos-cirilo.py`: seções da *Glaphyra* pelas citações da LXX (Adão = Gn 1–3; Caim = 4; Noé = 6–11; Abraão… José).
- `gen-gregos-teofilo.py`: *Ad Autolycum* II, 10–32 (Gn 1–11).
- `gen-gregos-origenes.py`: homilia 1 (as outras ficam como pista: o OCR não separa os títulos), fragmentos e escólios.
- `gen-gregos-procopio.py`: catena por capítulo (o OCR perde títulos: o trecho do cap. II vai até o VI).
- `gen-gregos-nissa.py`, `gen-gregos-basilio.py`, `gen-gregos-damasceno.py`, `gen-gregos-severiano.py`: Gn 1 (e Gn 2 para o
  *De opificio* 19–20 e 28–30, Damasceno 25–26).
- `_gen_gregos.py` tem também `lxx_genesis()` e `capitulos_citados()` (a LXX de Rahlfs, para achar o capítulo de um trecho).

## Para outros capítulos

- **Gn 2**: Teófilo II, 19–28 (o paraíso, a mulher da costela); Nissa, *De opif.* 19–20 e 28–30 (o alimento do paraíso; alma e
  corpo criados juntos, Gn 2,7); Basílio (atrib.), *Sobre a origem do homem* II (Gn 2,7: «o pó da terra», o sopro); Crisóstomo,
  *Hom. in Gen.* 11–16 e *Sermões* 6–8 (a árvore, o mandamento); Crisóstomo, *Sermão* 3, segunda metade (Adão dá nome aos
  animais, sinal de domínio, Gn 2,19); Teodoreto q. XXI (a bênção do sétimo dia, Gn 2,3) e XXII–XXX; Nazianzeno, *Or.* 38, 11 (o
  homem, «segundo mundo, grande no pequeno», com o pó e o sopro); Damasceno, *Exposição da fé* II, 11 (o paraíso); Cirilo,
  *Glaphyra*, «Περὶ τοῦ Ἀδάμ».
- **Gn 3**: Crisóstomo, *Sermões* 4–5 (as três servidões que o pecado trouxe; não somos castigados por causa de Adão) e *Hom.* 17–18;
  Teófilo II, 21–26; Nissa, *De opif.* 20; Teodoreto q. XXXI–XLIII; Teófilo II, 17 (as feras ficaram ferozes com o pecado).
- **Gn 4–11**: Teófilo II, 29–32; Cirilo, *Glaphyra* (Caim e Abel; Noé, a arca, a nudez de Noé, a torre); Orígenes, *Homilia* 2 (a
  arca; o fragmento grego sobre a forma da arca, PG 12).
