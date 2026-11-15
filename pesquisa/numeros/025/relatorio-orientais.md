# Números 25: relatório da pesquisa nos orientais não gregos

Pesquisa de 2026-11-15. 6 achados em `achados-orientais.json` (trecho 1: 1; trecho 2: 5; trecho 3: 0). O material oriental sobre Nm 25
é curto e concentrado em Fineias: nada achado de Nm 25,1–5 (a queda em Baal-Fogor) além de Afraates, e nada do trecho 3. Não forcei.
Originais novos em `textos/efrem-in-numeros-25.md`, `textos/efrem-sermo-reprehensione-25.md` e `textos/afraates-dem-6-25.md`.
Scripts em `~/.cache/taioe-nm25/orientais/` (`corpus.py`, `janela.py`, `bedjan.py`, `montar25.py`); imagens em
`pesquisa/cache/numeros25-orientais/img/` (no D:).

## O que entrou (6)

Trecho 1 (vv. 1–5):
1. **Afraates, *Dem.* 6, § 3** (Parisot col. 258), rel. 1: Zambri, chefe de Simeão, derrubado por uma só mulher, Cozbi, e os 24 mil caídos
   num só dia, na lista dos poderosos que a mulher arruinou (Hamã e a sua mulher antes). Curto; fica de reserva.

Trecho 2 (vv. 6–15):
2. **Afraates, *Dem.* 4, § 14** (Parisot col. 169–172), rel. 3: o zelo de Fineias «foi contado como oração» (Sl 106,30-31): quem faz o que
   dá repouso a Deus (visitar o doente, dar pão ao pobre) reza, e quem adia o socorro para terminar a oração fica devedor de pecado.
   Leitura própria e útil; é o melhor do grupo.
3. **Efrém atribuído, *In Num.* XXV** (Assemani I, p. 265 D–F), rel. 3: Fineias, figura de Cristo; Zambri, do diabo, que nada refreou; um
   só Fineias o trespassou, um só Cristo trespassou o diabo com a lança da cruz; cessando o pecado, cessou a praga.
4. **Efrém atribuído, *In Num.* XXV** (p. 265 F – 266 B), rel. 2: morta Cozbi, as companheiras fogem («aos hebreus foi tirado o poder, se
   não a vontade de pecar»); a lança como marco da justiça divina; o medo salutar; Moisés a interceder no luto. Corta a conjetura
   sobre o disfarce de Fineias.
5. **Efrém, *Hinos de Nísibis* 39, estr. 5 e 7** (Beck, CSCO 240; conferido com Bickell, p. 155), rel. 2: a Morte fala: a lança de Fineias lhe
   deu um banquete (Zambri e Cozbi), mas a lança que traspassou Jesus lhe tirou o povo. Siríaco do Digital Syriac Corpus; tradução
   nossa, conferida com o latim de Bickell. A edição de Beck é moderna: só duas estrofes e meia.
6. **Efrém atribuído, *Sermão sobre a repreensão*** (Lamy II, col. 388, nota «Num. XXV»), rel. 3: Fineias matou o impudico e salvou o povo;
   hoje cresce a autoridade dos libertinos e quem deveria advertir cala por medo. Bom para o zelo e a correção do pecado público.

Os itens 3 e 4 são do mesmo cap. XXV; se o capítulo ficar cheio, o 3 basta.

## Como se procurou

- **Digital Syriac Corpus** (~630 textos, `corpus.py`): Fineias (ܦܝܢܚܣ), Zambri (ܙܡܪܝ), Cozbi (ܟܘܙܒܝ), Fogor/Peor (ܦܓܘܪ, ܦܥܘܪ), «filhas de Moab»,
  «madianita». Afraates: *Dem.* 4 § 14, 6 § 3, 8 § 9, 14 §§ 13, 27, 40, 18 § 6, 19 § 3, 23 §§ 16 e 54. Efrém: só *Nísibis* 39. Jacó de Sarug:
  nenhum dos 39 memre do corpus.
- **Jacó de Sarug, Bedjan** (OCR dos cinco volumes, `bedjan.py`, sem espaços): só dois acertos de Fineias, ambos no vol. V (ver «Pista»).
- **Efrém em latim** (Assemani I–III e Lamy I–IV, OCR): Lamy II col. 388 (item 6); Lamy III, *Sermo IV de reprehensione* (Satanás e os seus
  encantos; uma cláusula sobre Zambri e Fineias, não usada); Lamy IV, *Sermones rogationum* («reprimamos as fornicações de Zambri»).
- **Armênios** (Narek, Nerses Shnorhali): busca na web sem resultado; nada achado. **Coptas, etíopes, hinografia siríaca**: sem texto
  pesquisável em domínio público que cite Nm 25.
- Dionísio bar Salibi (comentário a Nm, em `base/`), Narsai («Sobre João Batista», corpus 33), Isaac de Nínive (*Disc.* 10) e Filoxeno
  (*Disc.* 4): só pista, não lidos para o site.

## O que não existe

- Comentário de Efrém autêntico a Números (já anotado em `base/_ausentes-numeros.md`).
- Memra de Jacó de Sarug sobre Fineias, Zambri ou Baal-Fogor nos volumes de Bedjan; nada oriental sobre o v. 17-18 (a ordem contra Madiã).

## Pista (não entrou: sem conferência letra a letra)

- **Jacó de Sarug, Bedjan V (homilia IV, «Sobre Sodoma», pp. 152–153?)**: o OCR (`bedjan.py --folha 5 178`) traz «o Messias, o zeloso, é
  melhor que Fineias; e se pecares, a lança não estará no teu corpo, mas na tua alma». É o achado mais forte para Nm 25 entre os siríacos
  e **não está no Digital Syriac Corpus**; a página no archive.org (`homiliaeselectae05jaco`, n178–n179) usa Serto e não consegui
  conferir a letra na imagem. Fica para um revisor que leia Serto. Há outro acerto no mesmo volume, p. 590 (`n615`), a conferir.

## Para outros capítulos

- **Nm 31** (Baal-Fogor, o conselho de Balaão): Afraates, *Dem.* 8, § 9 (Moisés enterrado «diante de Bet-Fogor, onde Israel pecou»).
- **Nm 26–27** (os sacerdotes): Afraates, *Dem.* 14, § 27 (Fineias, sacerdote por 365 anos; o pacto do sacerdócio); *Dem.* 23, § 16
  (a descendência de Fineias por Eleazar, filho de Aarão, e Aminadab).
- **Nm 25 (reserva)**: Afraates, *Dem.* 14, § 40 e *Dem.* 18, § 6 (Zambri: «vinte e quatro mil numa só hora», por causa da luxúria);
  *Dem.* 23, § 54 (oração: «desviaste a tua ira pelo zelo de Fineias»); Lamy IV, *Sermones rogationum* («reprimamos as fornicações de Zambri»).
