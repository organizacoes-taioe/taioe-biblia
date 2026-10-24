# Números 18: relatório da pesquisa nos orientais não gregos (siríacos, armênios, coptas, etíopes, deserto)

Pesquisa de 2026-10-24. 6 achados em `achados-orientais.json` (trecho 1: 2; trecho 2: 1; trecho 3: 1; trecho 4: 2).
Originais em `textos/didascalia-8-9-18.md`, `isaac-de-ninive-discurso-22-18.md`, `efrem-in-numeros-18.md`,
`lambron-instituicoes-18.md`. Scripts em `scratchpad/p-orientais/scripts/` (`sc.py` e `scf.py`: busca no Digital Syriac
Corpus sem vogais; `ocrsyr.py`: busca no OCR siríaco de Bedjan sem espaços; `iapage.py`: acha a página `n` do archive.org
pelo `_djvu.xml`; `digitext.py`: texto das páginas do digilib.aua.am; `ctx.py`: contexto de uma busca; `montar.py`: monta o
JSON). Capítulo pobre nos orientais: quase todo o material é de ordens eclesiásticas (a *Didascália*) e de aplicações ao
clero; nenhum hino nem memra dedicado a Nm 18.

## Onde se procurou

- **Pistas automáticas** de `base/_pistas-orientais.md`, todas abertas no corpus: Afraates Dem. 14 § 20 (é Oza e a arca, 2Sm 6;
  coincide com «o serviço da tenda» de Nm 7/18), Dem. 15 § 2 (alimentos dos gentios; coincidência «lagar e eira»), *Liber
  Graduum* 29 § 16 (nada), João, o Solitário, *Diálogo sobre a alma* p. 82 (coincidência em ܦܘܪܫܢܐ), Rábula, *Cânones* p. 210
  (nada); **só Isaac de Nínive, discurso 22, é Nm 18 de verdade** (virou achado).
- **Digital Syriac Corpus** (632 textos, clone em `p-orientais/dl/sc`): ܦܠܓܘܬܟ ܘܝܪܬܘܬܟ (Nm 18,20 Peshitta), ܡܢܬ… ܘܝܪܬܘܬ,
  ܩܝܡܐ ܕܡܠܚܐ (aliança de sal), ܡܥܣܪܐ ܡܢ ܡܥܣܪ̈ܐ (dízimo do dízimo), ܥܘܠܗ ܕܡܩܕܫܐ, ܢܘܟܪܝܐ ܕܩܪܒ, ܐܓܪܟܘܢ ܚܠܦ, ܠܘܝ… ܝܘܪܬܢ,
  ܦܬܚ ܡܪܒܥܐ, ܡܪܝܐ ܗܘ ܝܘܪܬܢ/ܡܢܬ; e, nos textos sobre o sacerdócio (Jacó, *Sobre Aarão* e *Sobre a consagração da igreja*;
  Rábula, *Preceitos aos sacerdotes*; Balai, *Sobre o bispo Acácio*), ܠܘܝ, ܡܥܣܪ, ܝܘܪܬܢ, ܡܢܬ, ܐܓܪ. Fora Dionísio bar Salibi
  (proibido), nada.
- **Jacó de Sarug, Bedjan I–V** (OCR do archive.org, sem espaços): ܡܥܣܪ, ܦܠܓܘܬܟ, ܝܪܬܘܬܟ, ܩܝܡܐܕܡܠܚ, ܒܢܝܠܘܝ, ܫܒܛܐܕܠܘܝ,
  ܒܘܟܪ…ܦܪܩ, ܡܬܩܠ. Só Melquisedec e o dízimo de Abraão em Levi (Hb 7; Bedjan V) e «cessou o sacerdócio dos filhos de Levi»
  (Bedjan IV): nada de Nm 18.
- **Efrém em latim** (Assemani syr.-lat. I–III, Lamy I–IV, *Comentário ao Diatessarão* na versão de Aucher–Moesinger, 1876):
  decim-, primiti-, Levit-, pars/haereditas, pactum salis, sicl-, primogenit-. O *In Numeros* atribuído (Assemani I, p. 261 E–F)
  virou achado; o resto vai para reserva ou pista.
- **Didascália** siríaca: Gibson (inglês, 1903) e o latim de Funk (1905), caps. 8–9 inteiros e o cap. 9 até II, 36. Três achados.
- **Armênio**: o livro inteiro de Nerses de Lambron (133 capítulos do digilib.aua.am) por տասանորդ, ղեւտ-, երախայր-, «ուխտ աղի»
  (um achado); Wikisource armênio (Agatângelo, os três livros; busca por տասանորդ, Ղեւտացւոց, «բաժին եւ ժառանգութիւն»): nada.
- **Liturgia oriental**: Denzinger, *Ritus Orientalium* I–II (1863–64, latim dos rituais coptas, siríacos e armênios);
  *Testamentum Domini* (Rahmani, 1899); *Cânones de Hipólito* (Haneberg, 1870). Nada que cite Nm 18 (reserva e pistas abaixo).
- **Padres do deserto**: PG 65 (*Apophthegmata* e outros) por δεκάτ-, ἀπαρχ-, decim-, primiti-: nada sobre Nm 18.

## Achados (6)

1. **Didascália, cap. 8** (Gibson, p. 44–45), trecho 1, v. 1: o bispo, imitador de Cristo, carrega os pecados dos que lhe foram
   confiados; «não imagineis que o peso do episcopado seja leve»; e cita Nm 18,1. Relevância 3. Inglês de Gibson (com as leituras
   do ms. S, confirmadas pelo latim de Funk).
2. **Santo Isaac de Nínive, discurso 22** (Bedjan, p. 167–168), trecho 1, vv. 2.4.7: os pensamentos estranhos são os
   «estrangeiros» que a Lei não deixa entrar na tenda do testemunho; na oração pura, a fé leva a mente «para dentro do véu» do
   coração. Relevância 3. Siríaco do corpus. **Para decidir**: Isaac era bispo da Igreja do Oriente; não está na lista dos
   proibidos e o catálogo `fontes/orientais.md` o admite como escritor eclesiástico, mas é o primeiro uso dele no site.
3. **Didascália, cap. 9** (latim de Verona, Funk II, 26–27), trecho 2, vv. 7.8.11.12.21: primícias e dízimos de então são as
   oblações de agora, levadas ao bispo; os que viviam delas são o clero, as viúvas e os órfãos, «figura do altar»; e, como o
   estranho não se aproximava do altar sem o sacerdote, nada sem o bispo. Relevância 2.
4. **Didascália, cap. 8** (Gibson, p. 43–44), trecho 3, vv. 11.19.20–24: os levitas sem herança de terra, sustentados pelas
   ofertas porque só serviam a tenda; os bispos vivem da Igreja como o boi que debulha, sem devorar tudo. Relevância 3. Funk anota
   «Num. 18, 20» nesse parágrafo.
5. **Santo Efrém (atribuído), *In Numeros*, cap. XVIII** (Assemani I, p. 261 E–F), trecho 4, vv. 12.26.28.30: «o povo pagava o
   dízimo aos levitas, os levitas a Aarão, e Aarão a Deus». Relevância 2. É a leitura conhecida do pedido, agora com a página e o
   latim conferidos; as duas últimas linhas siríacas, lidas na imagem, estão em `textos/efrem-in-numeros-18.md` (a conferir).
6. **São Nerses de Lambron, *Reflexões sobre as instituições da Igreja*** (digilib 15030), trecho 4, vv. 21.24.31: aos levitas
   Deus não deu herança material, mas os dízimos do povo, «para que servissem sem distração»; o operário é digno do seu alimento.
   Relevância 2. **Repete em parte o achado 4** (Didascália): se ficar um só, a Didascália; Lambron acrescenta o «sem distração» e
   a voz armênia. Logo depois, no mesmo parágrafo, vem a frase de Aarão com o turíbulo, já usada em Nm 17.

**Sobreposição com os outros grupos**: a *Didascália* II, 25–28 é a fonte das *Constituições Apostólicas* II, 25–28 (grupo grego);
se o grupo grego trouxer as Constituições sobre os bispos «sacerdotes e levitas», as viúvas «altar» ou o estranho que não se
aproxima, ficar com a Didascália (séc. III, a fonte; as Constituições são uma reelaboração do séc. IV). Em 2026-10-24 o
`achados-gregos.json` já tinha `constituicoes-apostolicas-2-25-imitadores-de-cristo-levam-os-pecados` (= achado 1) e
`constituicoes-apostolicas-2-26-os-levitas-sao-hoje-os-diaconos` (= achado 3): escolher um de cada par. O achado 1 diz o mesmo
que Orígenes, hom. 10 sobre Números (o sacerdote que toma sobre si os pecados do povo, como Cristo): escolher um dos dois, ou os
dois se o tema admitir, porque a Didascália o diz do bispo em particular e cita Nm 18,1 expressamente.

## Reserva (achado e não usado)

- **Didascália, cap. 9** (Gibson, p. 51–52; Funk II, 34, 5 – 35, 2): «levai ao bispo os vossos frutos, os dízimos e as primícias…
  vós não estais presos aos dízimos e às primícias…; a vossa justiça supera os dízimos, as primícias e as ofertas deles quando
  fazeis como está escrito: “Vende tudo o que tens e dá aos pobres”». É o tema «os cristãos dão mais que o dízimo» (Ireneu IV, 18;
  Cassiano, *Conf.* 21); não cita as palavras de Nm 18. Texto em `textos/didascalia-8-9-18.md`. Bom para o tema, se os grupos
  latino e grego não trouxerem Ireneu e Cassiano.
- **Santo Efrém, *Sermões contra os perscrutadores* (Hinos sobre a fé), sermão XXIII** (Assemani III, p. 41, fim do sermão, latim de
  Benedetti), a um cantor: «paga ao teu Deus o dízimo dos teus cantos, oferece-lhe o feixe colhido dos pensamentos da tua mente,
  separa para ele as primícias dos hinos piedosos, devolve-lhe salmos da tua vindima». Bonito, mas é o dízimo e as primícias em
  geral, sem Nm 18; e só em paráfrase latina. https://archive.org/details/assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-3
- ***Cânones de Hipólito*, cânon 36** (ordem eclesiástica egípcia, árabe; Haneberg 1870, p. 93–94,
  https://archive.org/details/canonesshippoly00hanegoog): as primícias dos frutos, «da eira e dos lagares», do azeite, do mel, do
  leite, da lã e «do salário do trabalho das mãos» se levam ao bispo, que dá graças e pede que sejam «para a fartura dos pobres
  do teu povo». É Nm 18,12–13.27 na prática da Igreja, sem citá-lo; o original é árabe (latim de Haneberg).
- **Nerses de Lambron**, mesma obra (digilib 15032): os dízimos e as primícias devidos à Igreja, a partir de Ml 3,8–10; não é Nm 18.

## O que não existe ou não se achou

- Nenhum hino, memra ou homilia oriental dedicado a Nm 18: nem Efrém (Nisibenos, Natividade, Lamy), nem Jacó de Sarug (39 memre
  do corpus e o OCR de Bedjan I–V), nem Afraates, *Liber Graduum*, Isaac de Nínive (fora o discurso 22), Balai, Rábula.
- «Aliança de sal» (v. 19), «dízimo do dízimo» (v. 26) e «eu sou a tua parte e a tua herança» (v. 20, Peshitta ܦܠܓܘܬܟ ܘܝܪܬܘܬܟ):
  nenhuma ocorrência em autor permitido do corpus; só em Dionísio bar Salibi.
- O primogênito resgatado por cinco siclos (vv. 15–16): nenhum oriental o comenta; o Efrém do *Diatessarão* (Aucher–Moesinger,
  p. 25) cita «todo primogênito que abre o seio será chamado santo ao Senhor» (Lc 2,23 / Ex 13) para dizer que no batismo todos
  somos primogênitos: é Ex 13, não Nm 18 (pista para Lc 2 ou Ex 13).
- *Testamentum Domini* (Rahmani 1899, II, 14–16, p. 137–139): as primícias levadas ao bispo e a bênção dos frutos, sem Nm 18.
- *Apophthegmata* (PG 65): nada sobre dízimos, primícias ou levitas; os δεκάτ- de PG 65 são de outra obra (Marcos, o Eremita, sobre
  Melquisedec e o dízimo de Abraão).
- Copta e etíope: nada em domínio público com texto original acessível (como em Nm 17).
- Cassiano, *Conferências* 21, 3 (o abade João, a Teonas: «os dízimos eram, por mandado do Senhor, para o uso dos levitas; as
  oblações e as primícias, consagradas aos sacerdotes»; os justos vão além da lei): é Nm 18 e é um Padre do deserto, mas o texto é
  latino; ficou para o grupo latino (CSEL 13, p. 575, https://archive.org/details/iohanniscassian00petsgoog). Se ele não
  trouxer, vale achado.

## Só pista (proibidos no site ou fora do critério)

- Dionísio bar Salibi, *Comentário literal a Números* (base/): lemas dos vv. 1, 7, 9, 12, 19 («aliança de sal: firme como a
  aliança que os homens fazem com o sal; e ensina a pôr sal em toda oferta»), 26 e 29; também no *Comentário a Ezequiel* (bloco
  61, v. 26) e no *Comentário a Deuteronômio* (os dois dízimos). Não usar.
- Timóteo II, *Sobre o sacerdócio* (corpus 541): só Ez 44 e Moisés que impõe as mãos a Aarão. Narsai, Filoxeno, Isho`dad, bar Koni:
  não abertos.
- Afraates, Dem. 4 § 6: Jacó prometeu o dízimo «para o dar a Levi, porque nele estavam escondidos os que dão o dízimo e recebem as
  primícias» (Gn 28 e Hb 7, não Nm 18).
- Ritual siríaco de ordenação (Denzinger, *Ritus Orientalium* II, 1864, p. 124, provavelmente o diácono; ordinal jacobita):
  «Deus, que deste o sacerdócio à ínclita tribo dos filhos de Levi… os sacerdotes te serviram com os seus sacrifícios, e os
  levitas te celebraram nas suas ordens; assim estes te sirvam e guardem a porta do teu templo e o átrio do teu santo
  tabernáculo» (eco de Nm 18,2–4, sem citação). https://archive.org/details/bub_gb_ZvFmsYDPs2wC

## Para outros capítulos

- **Nm 19** (a vaca vermelha): Efrém atribuído, *In Numeros*, Assemani I, p. 261 F – 262 (logo depois do cap. XVIII; ver o OCR em
  `p-orientais/dl/assemani1_djvu.txt`, linhas ~49060–49110: «Adducent ad te vaccam rufam…»); Dionísio bar Salibi (só pista).
  *Didascália*, a parte final contra a «segunda legislação» (o cristão não fica impuro por tocar um morto, os ossos, as
  relíquias dos santos): latim de Verona em Funk, *Didascalia* VI, 18–23 (p. 304–320; Funk anota «Num. 19, 10» em VI, 19,
  «Num. 19» em VI, 21, 6–8, «Num. 19, 16» e «Num. 19, 11–18» em VI, 21, 9 – 22, 1, e de novo em VI, 22, 10 – 23, 4),
  https://archive.org/details/cu31924029335167. Gibson não traduziu essa parte (a tradução dele para no começo do cap. XXVI);
  Connolly (Oxford 1929) traduz tudo. Isaac de Nínive e Afraates: buscar ܬܘܪܬܐ ܣܘܡܩܬܐ (novilha vermelha) e ܡܝܐ ܕܕܘܝܬܐ.
- **Nm 20** (morte de Aarão no Hor): Jacó de Sarug, *Sobre Aarão* (syriaccorpus.org/344), p. 72–84, a despedida de Moisés e Aarão e
  a investidura de Eleazar, com refrão; p. 80–81: a bênção a Eleazar («a ti os levitas obedecerão… e o Senhor seja o teu
  companheiro», com jogo entre *lewāyā* «companheiro» e Levi). Lambron (digilib 15030 e seguintes): o luto de trinta dias.
  Afraates Dem. 11 § 9 (Edom, Nm 20,14–21) já em base/.
- **Lc 2,22–24 / Ex 13** (o primogênito apresentado): Efrém, *Diatessarão*, p. 25 de Aucher–Moesinger (o batismo nos faz a todos
  primogênitos).
- **Ml 3,8–10** (os dízimos roubados a Deus): Nerses de Lambron, *Reflexões* (digilib 15032).
- **Gn 28,22 e Hb 7,9** (o dízimo de Jacó e Levi nos rins de Abraão): Afraates Dem. 4 § 6; Jacó de Sarug, memra sobre
  Melquisedec (Bedjan V).
