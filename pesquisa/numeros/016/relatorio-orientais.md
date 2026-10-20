# Números 16,1–35: relatório da pesquisa nos Padres orientais (siríacos, armênios, coptas, Padres do deserto, liturgia bizantina)

Pesquisa de 2026-10-20 (regra nova do Gere: «quero ver mais comentários de padres orientais»). Rascunho em andamento: a parte
siríaca está fechada; as frentes bizantina, do deserto e armênia entram a seguir.

## Siríacos: onde se procurou

- **Digital Syriac Corpus** (https://syriaccorpus.org; TEI no GitHub `srophe/syriac-corpus`, baixado em zip — o `git clone` falha no
  Windows por caminho longo): 632 textos, entre eles Efrém (Hinos de Nísibis 1–77, Hinos da Natividade, Memre sobre José), Afraates
  (as 23 Demonstrações, ed. Parisot), Jacó de Sarug (39 memre), Narsai (81), Isaac de Nínive (82 discursos da 1ª parte), Filoxeno (13
  discursos), o *Liber graduum* (30 memre), Dionísio bar Salibi (comentários literais ao Pentateuco e outros), Timóteo II, Antão de
  Tagrit. Busca sem sinais vocálicos por ܩܘܪܚ (Coré), ܕܬܢ (Datã, palavra inteira), ܐܒܝܪܡ (Abiram), ܦܝܪܡܐ (turíbulo), «Deus dos
  espíritos» (ܐܠܗܐ ܕܪܘܚܬܐ), ܡܐܬܝܢ ܘܚܡܫܝܢ (250), ܐܣܬܕܩܬ ܐܪܥܐ, ܦܬܚܬ ܦܘܡܗ, ܟܕ ܚܝܝܢ ܠܫܝܘܠ. Scripts em
  `scratchpad/pesq-orientais/` (`sbusca2.py`, `plain.py`, `ext.py`).
- **archive.org, OCR latino**: Lamy, *Hymni et sermones* I–IV (`sanctiephraemsy00…04lamygoog`); ed. romana siríaco-latina II e III
  (`assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-2` e `-syr-3`); Bickell, *Carmina Nisibena* (`carminanisibenaa00ephr`).
  Busca por Core/Chore, Dathan, Abiron/Abiram; páginas conferidas na imagem.
- **Didascália siríaca**: Gibson 1903 (inglês, `didascaliaaposto00gibsuoft`) e Achelis–Flemming 1904 (alemão, `DieSyrischeDidaskalia`).
- NPNF II/13 (newadvent): só para conferir Efrém (Hinos de Nísibis 19 e 39) e Afraates.

## Siríacos: o que se achou

16 achados em `achados-orientais.json` (siríacos e Didascália), textos em `textos/`:
`efrem-hinos-nisibenos-16.md`, `efrem-lamy-e-assemani-16.md`, `afraates-siriaco-16.md`, `barsalibi-in-numeros-16.md`,
`siriacos-varios-16.md`, `didascalia-23-16.md`.

- **Efrém, Hinos de Nísibis 19, 7** (ao bispo Abraão): Coré e Datã «fizeram cisão» (ܣܕܩܘ), Moisés «fendeu a terra debaixo deles», e
  «com uma fenda acabou com a cisão» (ܒܣܕܩܐ ܣܕܩܐ ܒܛܠ) — o jogo de palavras é o centro. **Hino 39, 4** (fala a Morte): festa no
  Sheol quando engoliu os de Coré, banquete preparado por Satanás com a discórdia dos levitas; «Moisés me mandou vivos lá para baixo,
  mas Jesus fez subir os nossos mortos». Os dois do siríaco (Beck), conferidos com Bickell (latim) e NPNF.
- **Efrém (atrib.), Hinos sobre Juliano Saba 18, 14** (Lamy III, col. 901–902): o mesmo jogo — os de Coré fizeram cisma, «a terra
  se fendeu e os engoliu». Siríaco transcrito da imagem da página.
- **Efrém, Sermões contra os perscrutadores 8 (= Hinos sobre a Fé 8)** e **Necrosima 16** (atrib.): só o latim da ed. romana
  (paráfrase de Benedetti); o siríaco está ao lado, na mesma página, mas a impressão serto é pequena demais para transcrever com
  segurança. Para conferir: Beck, CSCO 154 (Hinos sobre a Fé, 1955).
- **Afraates**: Dem. 9, 8 (a inveja: Coré e Aarão e Miriam contra Moisés, o humilde) e Dem. 4, 3 (o fogo que «recebeu ordem» contra os
  250 que ofereceram turíbulos sem mandato, junto com Nadab e Abiú), do siríaco de Parisot. O original siríaco do achado grego
  `afraates-demonstracao-22-24` (que está em inglês) agora está em `textos/afraates-siriaco-16.md`: pode-se trocar o `original`.
- **Dionísio bar Salibi** (bispo de Amida, † 1171), *Comentário literal a Números*: o único comentário siríaco seguido de Nm 16 achado
  em domínio público. Quatro achados: as três ambições (Coré, primo de Moisés, quer o sacerdócio; os rubenitas, como primogênitos, a
  primazia; os 250, um sacerdócio de todas as tribos) e Moisés prostrado suplicando; «Deus dos espíritos e de toda carne» =
  «criador das almas e dos corpos» (o único oriental que liga o v. 22 à criação da alma); «vivos ao Sheol» = sepultados antes de
  morrer, e por isso «criação nova», uma morte que nunca houve; as causas (inveja, ousadia, sedução de Satanás) e os filhos inocentes
  que pereceram «para emenda dos outros».
- **Narsai**, Memra sobre João Batista, vv. 425–430 (a justiça calou no banquete de Herodes; podia sacudir a terra como com o bando de
  Datã e Coré): relevância 1, transcrição com palavras mal separadas.
- **Timóteo II** (católico da Igreja do Oriente, 1318–1332), *Sobre o sacerdócio* 7: os de Coré e Ozias, que tomaram para si o sumo
  sacerdócio sem imposição das mãos, foram queimados e feridos de lepra.
- **Didascália dos Apóstolos 23** (Sobre as heresias e os cismas): o comentário antigo mais rico de todos os orientais. Três achados,
  um por trecho: os de Coré «amaram o primeiro lugar e cobiçaram o sumo sacerdócio» e se separaram de Moisés com ares de pureza; todo
  o povo oferecia **um só turíbulo**, os cismáticos ofereceram **250**, e a multiplicação do culto no cisma de nada serviu; «fugi dos
  cismas como quem luta pela vida» (Nm 16,26.34). Traduzido do inglês de Gibson (1903); conferido com o alemão de Achelis–Flemming.

## Siríacos: anotados, sem virar achado

- Afraates, Dem. 1, 12 (os 250 queimados, numa lista de provas pelo fogo), Dem. 5, 3 (Datã e Abiram se gloriaram contra Moisés: lista;
  já anotado pela frente grega) e Dem. 14, 13 (a inveja «engoliu Coré»): siríaco em `afraates-siriaco-16.md`.
- Narsai, *Sobre a maldade do tempo* 66–67 (ed. Mingana 1905): «o abismo que engoliu os da casa de Datã», numa lista.
- Antão de Tagrit (séc. IX), *Sobre a providência*: «a boca aberta da terra, pela maldade de Datã e Abiram», numa lista.
- Efrém, Hinos sobre Abraão Qidunaya 5, 9 (Lamy III, col. 783–784): «pelas palavras morreram Coré e Datã». Hinos contra as heresias 48
  (Assemani II, «Adversus haereses» 48): contra Marcião, o corpo de Elias sobe, os de Datã e Abiram descem. Necrosima 16, p. 258: a
  morte mansa do sacerdote, «bem diferente da de Datã e Abiram» (que o texto confunde com os 250 queimados).
- Dionísio bar Salibi, sobre Nm 12: Aarão não ficou leproso para que os que «assaltaram o sacerdócio, e a terra os engoliu» não
  dissessem que o leproso continuava sacerdote e eles não.
- Timóteo II, *Sobre o sacerdócio* 6: Coré e Ozias de novo (texto em `siriacos-varios-16.md`).

## Siríacos: o que não existe ou não se achou

- **Jacó de Sarug**: nos 39 memre do corpus, nada sobre Coré (o memra *Sobre Aarão, o sacerdote* trata do turíbulo entre os mortos e os
  vivos: Nm 17). Os ~190 memre de Bedjan (*Homiliae selectae*, 1905–1910) só existem em imagem, sem OCR siríaco; nenhum catálogo
  indica memra sobre Coré.
- **Isaac de Nínive** (82 discursos), **Filoxeno** (13 discursos, Budge 1894), **Liber graduum** (30 memre): nenhuma menção.
- **Isho'dad de Merv**, *Comentário a Números*: só na ed. de Vosté–Van den Eynde (CSCO, 1950–1963), com direito autoral; não usado.
- **Efrém, *In Numeros*** (cadeia): já está na frente grega (latim da ed. romana).
- **Hinos sobre a Fé** e **Contra as heresias** de Efrém: o siríaco digital (Beck) não está em nenhum corpus aberto; só o latim de
  Assemani foi usado.

## Para Nm 17 (16,36–50 da LXX e da Vulgata = o nosso 17,1–15; a vara, 17,16–28)

| Autor, obra | Passagem | Onde | O que diz |
|---|---|---|---|
| Efrém, Hinos de Nísibis 39, 6 | estrofe 6 | https://syriaccorpus.org/293 | a Morte: «o turíbulo de Aarão, que ficou entre os mortos e os vivos, me assustava»; mais ainda a Cruz |
| Jacó de Sarug, *Sobre Aarão, o sacerdote* | memra inteiro | https://syriaccorpus.org/344 | Aarão com o turíbulo cheio de fogo detém o anjo destruidor: o fogo do incenso e o «fogo escondido» do amor |
| Dionísio bar Salibi, *Coment. literal a Números* | Nm 17,1–15 (16,36–50) | https://syriaccorpus.org/231 | os turíbulos «santificados à custa das suas almas»; Aarão «entre os mortos e os vivos», mediador; 14 700 mortos |
| Afraates, Dem. 4, 3 | fim | https://syriaccorpus.org/4 | «os seus turíbulos foram santificados à custa da vida deles» (Nm 17,3) |
| Didascália 23 | Gibson p. 103–104 | https://archive.org/details/didascaliaaposto00gibsuoft/page/n131/mode/1up | as lâminas de bronze no altar, memória para não fazer cisma; «o Senhor julgou o fogo pelo fogo» (o fogo estranho derramado) |
