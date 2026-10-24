# Números 17: relatório da pesquisa nos orientais não gregos (siríacos, armênios, coptas, etíopes)

Pesquisa de 2026-10-24. 14 achados em `achados-orientais.json` (trecho 1: 2; trecho 2: 7; trecho 3: 5). Originais em
`textos/efrem-varios-17.md`, `jaco-sarug-sobre-aarao-17.md`, `liber-graduum-21-17.md`, `didascalia-23-17.md`,
`lambron-instituicoes-17.md`, `shnorhali-tagh-cruz-17.md`. Scripts em `scratchpad/p-orientais/scripts/` (`sc.py`: busca no
Digital Syriac Corpus sem vogais; `iapage2.py`: acha a página `n` do archive.org pelo `_djvu.xml`; `digilib.py`: baixa um
livro inteiro do digilib.aua.am; `wscat.py`: baixa uma categoria do Wikisource armênio; `montar.py`: monta o JSON).

## Onde se procurou

- **Digital Syriac Corpus** (clone do `srophe/syriac-corpus`): busca por ܦܝܪܡ (turíbulo), ܐܗܪܘܢ junto de ܚܘܛܪ/ܫܒܛ (vara),
  ܡܝܬܐ ܠܚܝܐ («entre os mortos e os vivos»), ܠܘܙܐ (amêndoas), ܐܪܘܢܐ/ܩܒܘܬܐ (arca), ܠܐ ܢܨܝܒ, ܠܐ ܫܩܝ; e os versículos da
  Peshitta (as pistas de `base/_pistas-orientais.md`).
- **Latim antigo de Efrém**: OCR de Lamy I–IV, Assemani syr.-lat. II e III, Bickell (Carmina Nisibena), por «Aaron»,
  «virga», «thuribul», «amygdal»; páginas conferidas na imagem.
- **Jacó de Sarug, Bedjan I–V** (OCR do archive.org): o siríaco sai com letras separadas; busca sem espaços por ܐܗܪܘܢ e ܦܝܪܡ.
- **Armênio**: Wikisource armênio (busca e a categoria inteira dos tagh de Shnorhali, 59 peças); *Livro das Lamentações* de
  Narek inteiro; digilib.aua.am, o livro inteiro de Nerses de Lambron (*Reflexões sobre as instituições da Igreja*, 133 capítulos).
- **Copta e etíope**: só busca na web; nada em domínio público com texto original acessível.

## O que se achou e entrou

- **Efrém**: Nísibis 39, 6 (o turíbulo de Aarão e a Cruz); Nísibis 53, 12–13 (Satanás: Aarão conteve a Morte com o incenso,
  mas fez o bezerro); Nísibis 48, 1–4 (**hino inteiro sobre a vara de Aarão e a ressurreição dos corpos**: o achado oriental
  mais rico do capítulo; as doze varas como figura do juízo); Natividade 1, 15–17 (a vara florida e o seio virgem).
- **Efrém atribuído**: *In Numeros* (Assemani I, p. 260–261), duas glosas novas: os turíbulos santificados → os corpos dos
  confessores (relíquias), e a vara = o corpo de Cristo que não viu a corrupção; *Paraenesis* 61 (Assemani III, p. 528): o
  incenso de Aarão e o sacrifício da Igreja contra a «praga» dos cismas (latim de Benedetti, paráfrase); *Hinos sobre Maria* 5,
  5–6 (Lamy II, col. 535–538): a vara posta na arca, sem plantio nem rega, figura da Virgem (só o latim de Lamy; o serto da
  página não foi transcrito com segurança).
- **Jacó de Sarug**, *Sobre Aarão* (Bedjan I, memra 5): o «fogo escondido» do amor (p. 70, no metro de Jacó) e o anjo que foge
  do fogo (p. 71). **Cuidado**: o memra é composto; o manuscrito marca trechos «no metro de Mar Efrém» (7 sílabas) e «de Mar
  Balai» (5 sílabas). O segundo achado vem do trecho no metro de Efrém: posto como «São Jacó de Sarug (atribuído)».
- **Liber Graduum** 21, 12: Moisés, mandado sair do meio do povo «para que eu os destrua num instante», não se separa dos
  pecadores. Funde Nm 17,10 (= 16,21) com Ex 32; relevância 2.
- **Didascália** 23 (Gibson, p. 103–104): as lâminas de bronze no altar e «o Senhor julgou o fogo pelo fogo» (o fogo estranho
  derramado). Completa os três achados de Nm 16 sem repetir nenhum.
- **Nerses de Lambron**: o bispo mora na cidade para ser o Aarão dela, o intercessor que mantém fechada a ira de Deus.
- **Nerses Shnorhali**, Tagh da Santa Cruz (phokh 72): a Cruz, «vara florida do novo Aarão», que deu como fruto o Rei do céu.
  A edição de base do Wikisource não está indicada (talvez Srapyan, Erevã 1987): conferir antes de publicar.

## Achado e não usado

- Lambron, mesma obra (digilib 15053): «os turíbulos [de Coré] foram guardados em Israel como memória dos males» (Nm 17,5):
  meia frase, continuação do achado armênio de Nm 16 (não publicado); fica no texto, não virou achado.
- Narek, *Lamentações*, Oração 75: a igreja de pedra, «maior que o homem, como o bastão de Moisés; mais que o racional, como a
  vara mística de Aarão que floresceu»: comparação de passagem; relevância 1.
- Efrém (atribuído), *Sermões de rogação* (Lamy, vol. 3 e 4 do archive.org, `sanctiephraemsy01lamygoog`/`04lamygoog`, Sermão 7):
  Deus «pôs na arca a vara que produziu amêndoas»; e Lamy IV, col. 411–412: Deus «fez germinar a semente seca, como a vara de
  Aarão que floresceu», numa súplica pela chuva. Alusões curtas.
- Efrém, Nísibis 18, 3 (Aarão invejado pelos levitas, seus irmãos; Moisés o carrega com amor): é Nm 16, já coberto.
- Efrém, Nísibis 43, 1 («turíbulo de misericórdia», sobre ossos dos santos) e Natividade 2, 18; 9, 15; 25, 2; Lamy II
  («in Levi thuribulum tuum»): uso genérico do turíbulo, sem Nm 17.
- Afraates Dem. 4, 3 (os turíbulos santificados à custa da vida deles): **já publicado em Nm 16**. Dem. 23 §16, §20 e Dem. 8
  §23 (pistas automáticas): coincidência de palavras, nada sobre Nm 17.
- Jacó de Sarug, memra sobre Ozias (Bedjan V, página não localizada; OCR ruim): o turíbulo cheio de vida e de misericórdia, os filhos de Levi
  com os seus turíbulos; é 2Cr 26, só toca Nm 17,5. Ler na imagem se houver capítulo de Crônicas.
- Grigoris Aghtamartsi (católico de Aghtamar, séc. XVI), tagh à Virgem «Տապանակ կազմեալ անփուտ»: «A vara de Aarão floresceu
  na tenda, anunciava o teu nascimento… turíbulo de ouro, em ti se acende o fogo, Deus»: poeta armênio tardio, sem estatuto de
  santo; só pista (Wikisource armênio).

## O que não existe ou não se achou

- Nenhum outro memra de Jacó sobre a vara de Aarão nos 39 do corpus nem no OCR de Bedjan II–V (que é fraco).
- Nada em Afraates, Isaac de Nínive, Liber Graduum (além do 21, 12) sobre a vara.
- Shnorhali: entre os 59 tagh do Wikisource, só o da Santa Cruz traz Aarão; *Jesus Filho* (*Yisus Ordi*) não está online
  em texto (ed. Veneza 1643 e seguintes: procurar no archive.org).
- Theotokia copta («tu és a vara de Aarão que floresceu sem ser plantada nem regada»): não se achou o copta em edição antiga
  acessível; a de Tuki (1764) e a *Psalmodia* do Cairo (1908) existem só em imagem. Hinos etíopes (*Weddase Maryam*,
  *Anáfora de Maria*): idem. Ficam como pista.
- Maronitas e caldeus: o *Breviarium Chaldaicum* (Bedjan) e o *Fenqitho* de Mossul têm OCR siríaco inútil; não lidos.

## Só pista (proibidos no site)

- Dionísio bar Salibi, *Comentário literal a Números* (base/): turíbulos «santificados à custa das suas almas»; Aarão
  mediador «entre os mortos e os vivos»; 14 700 mortos. Pistas automáticas em bar Salibi (Levítico, Deuteronômio, Jó),
  Filoxeno (Discursos 11 e 13) e Timóteo II: não lidas, por serem proibidas.

## Para outros capítulos

- **Nm 18** (o sacerdócio de Aarão e o dízimo dos levitas): Assemani I, p. 261 E–F (*In Numeros* atribuído a Efrém,
  cap. XVIII: «o povo pagava o dízimo aos levitas, os levitas a Aarão, e Aarão a Deus»).
- **Nm 19** (a vaca vermelha): Assemani I, p. 261 F em diante.
- **Nm 20** (morte de Aarão no Hor): Jacó de Sarug, *Sobre Aarão* (syriaccorpus.org/344), p. 72–84, inteiro sobre a
  despedida de Moisés e Aarão e a investidura de Eleazar (com refrão «Vai em paz, irmão»); Lambron (digilib 15030): «Israel
  chorou Aarão trinta dias» e a oração pelos mortos.
- **Nm 25** (Fineias): Efrém, Nísibis 39, 5 e 7 (a lança de Fineias; a lança que traspassou Jesus); Afraates Dem. 23, 16.
- **Hb 9,4 / Ex 16,33** (a urna do maná na arca): Efrém atribuído, *Hinos sobre Maria* 5, 5 (Lamy II).
