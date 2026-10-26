# Gênesis 3: relatório do grupo agostinho (2026-10-26)

Santo Agostinho em toda a obra. A pesquisa partiu da pré-pesquisa (`base/`: *Comentário literal* XI, *Contra os
maniqueus* II, 14–29, *Cidade de Deus* XIII–XIV) e foi buscar o resto nas *Confissões*, nas *Enarrationes*, nos
sermões e no *De doctrina christiana*, pelo texto da PL no Corpus Corporum (já em `cache/genesis/agostinho/cc/`:
26 obras) e pelas páginas do augustinus.it. **16 achados** em `achados-agostinho.json`: 4 por trecho. Cada um diz uma
coisa que os outros não dizem; as alternativas que dizem o mesmo, e as boas que ficaram de fora, estão em
`base/_pistas-agostinho.md`. Todo `original` foi conferido, pedaço por pedaço (entre os «[…]»), contra o texto do
augustinus.it (script `~/.cache/taioe-gn3/agostinho/montar.py`); a tradução não traz mesóclise nem pronome contraído e
não repete excerto publicado (conferido contra os 1121 comentários de `conteudo/`).

## O que se procurou e onde

| obra | onde (Gn 3) | situação |
|---|---|---|
| *De Genesi ad litteram* XI | 2, 4 – 42, 60: a serpente, a tentação, a soberba, os olhos abertos, a voz de Deus, as desculpas, a sentença, Eva, as túnicas, «como um de nós», a expulsão, Adão e Salomão | `base/` (pré-pesquisa); lido inteiro; 5 achados (4, 6 e 6, 8; 34, 46; 35, 47–48; 39, 53; 42, 59) |
| *De Genesi contra Manichaeos* II, 14–29 | Gn 3 inteiro, em alegoria | `base/`; lido inteiro; 1 achado (22, 34); o resto é alegoria ou repete (pistas) |
| *De civitate Dei* XIII–XIV | XIII, 12–15 (as mortes; «Adão, onde estás?»); XIV, 11–17 (a soberba, as desculpas, a pena, os olhos abertos), 26–28 | `base/`; 4 achados (XIII, 15, a parte não publicada; XIV, 13; XIV, 15; XIV, 17, a segunda metade, não publicada) |
| *Confessiones* V, 2, 2 | fugir da face de Deus (vv. 8–9, sem citar) | baixado: `base/agostinho-confissoes.md`; 1 achado |
| *Enarrationes in Psalmos* 103, s. 4 (= Sl 104) | 6, 9, 11: a cabeça da serpente e o calcanhar (v. 15); «comerás terra» e «és terra» (vv. 14.19) | baixado: `base/agostinho-enarrationes-in-psalmos.md`; 2 achados |
| *Sermones* 51, 174, 232, 289 | Eva e Maria, «por uma mulher a morte, por uma mulher a vida»; «se o homem não se tivesse perdido» | baixado: `base/agostinho-sermones.md`; 2 achados (174, 2; 289, 2) |
| *De doctrina christiana* I, 14, 13 | a cura pelos contrários e pelos semelhantes (o capítulo inteiro) | baixado: `base/agostinho-de-doctrina-christiana.md`; 1 achado |
| *Enarrationes* (outras), *Tratados sobre João*, *De Trinitate*, *Enchiridion*, *Contra Faustum*, *De diversis quaestionibus*, sermões (Corpus Corporum) | busca por frases da Vetus Latina dele: «Adam, ubi es», «tunicas pelliceas», «observabit caput», «terra es et in terram ibis», «in sudore vultus», «per feminam mors», «eritis sicut dii», «quam dedisti mihi» | só pistas (`base/_pistas-agostinho.md`) |

## Os achados

| id | trecho | vv. | o que diz | rel. |
|---|---|---|---|---|
| `agostinho-gnlitt-11-4-6` | 1 | 1 | Por que Deus permitiu a tentação: o desígnio o ultrapassa, mas não seria mérito viver bem só por falta de tentação; «é mais gloriosa a palma de não consentir quando tentado do que a de não poder ser tentado» | 2 |
| `agostinho-civ-14-13` | 1 | 5 | A queda começou por dentro: o homem já agradava a si mesmo. «Sereis como deuses»: só se é «deus» pela participação no Deus verdadeiro; «quem deseja mais fica menos» | 3 |
| `agostinho-gnlitt-11-42-59` | 1 | 6 | Adão não acreditou na serpente: cedeu, como Salomão, para não entristecer a mulher; ofende-se a Deus para não perder um amigo | 2 |
| `agostinho-civ-14-17-2` | 1 | 5, 7 | Os olhos se abriram não para ver, mas para distinguir o bem perdido do mal em que caíram; como o doente entende a saúde; «conheceram o que seria mais feliz ignorar» | 3 |
| `agostinho-conf-5-2` | 2 | 8–9 | «Para onde fugiram, quando fugiam da tua face?» Deus não abandona a criatura que o abandonou; «onde estava eu, quando te procurava?» | 3 |
| `agostinho-civ-13-15-2` | 2 | 9, 19 | «Adão, onde estás?»: não ignorância, mas advertência, para que ele reparasse onde estava, ele em quem Deus já não estava; e «és terra», a morte do corpo | 3 |
| `agostinho-gnlitt-11-34-46` | 2 | 8, 10 | Deus vinha como um amigo, como com Abraão em Mambré; a mesma amizade que dava confiança pesa de vergonha; esconder-se de quem vê o coração | 2 |
| `agostinho-gnlitt-11-35-47` | 2 | 12–13 | «Soberba! Por acaso disse: Pequei?» Confusão, não confissão; o mal se atribui ao Criador, o bem a si; a mulher culpa a serpente; o salmista dirá «pequei contra ti» | 3 |
| `agostinho-en103-4-6` | 3 | 15 | «Ela vigiará a tua cabeça»: a cabeça da serpente é a primeira sugestão do pecado; pisá-la logo; o diabo espreita o calcanhar, a saída do caminho | 3 |
| `agostinho-sermo-289-2` | 3 | 15 | Eva concebeu no coração o veneno da serpente; Maria, no ventre, a carne do Onipotente; por uma mulher a perdição, por uma mulher a salvação | 3 |
| `agostinho-civ-14-15` | 3 | 16–19 | Um só mandamento, levíssimo, desprezado; a pena da desobediência é a desobediência: «porque não quis o que podia, quer o que não pode»; a alma perturbada, a carne que sofre, envelhece e morre | 3 |
| `agostinho-en103-4-11` | 3 | 14, 19 | «Comerás terra» e «és terra»: o corpo é terra, mas quem busca as coisas do alto não é terra, e a serpente não o come | 2 |
| `agostinho-gnlitt-11-39-53` | 4 | 22 | «Como um de nós»: o plural pela Trindade; a promessa da serpente devolvida ao soberbo, mais aviso aos leitores que zombaria; não se tornou o que quis nem conservou o que era | 3 |
| `agostinho-gnman-2-22-34` | 4 | 22–23 | «Mandou para fora», não «excluiu»: o peso do pecado o levou; mandado aos trabalhos para um dia estender a mão à árvore da vida, e o estender da mão é a cruz | 2 |
| `agostinho-sermo-174-2` | 4 | 22–24 (o capítulo) | «Se o homem não se tivesse perdido, o Filho do homem não teria vindo»; «onde estaria o primeiro homem, se não tivesse vindo o segundo?» (para o «ó feliz culpa») | 3 |
| `agostinho-doctrchr-1-14-13` | 4 | 5, 6, 15, 19 (o capítulo) | Cristo, médico e remédio, cura pelos contrários (soberba/humildade, sabedoria da serpente/«loucura» de Deus, imortalidade mal usada/mortalidade bem usada, mulher/mulher) e pelos semelhantes | 3 |

Os 3 melhores, para o leitor comum: `agostinho-civ-14-17-2` (os olhos abertos para conhecer o que seria mais feliz
ignorar), `agostinho-gnlitt-11-35-47` («Soberba! Por acaso disse: Pequei?») e `agostinho-en103-4-6` (a cabeça da
serpente é a primeira sugestão).

## Decisões e dúvidas para a seleção

- **Duas metades já publicadas**: *Civ.* XIII, 15 (`agostinho-civ-13-15`) e XIV, 17 (`agostinho-civ-14-17`) saíram em
  Gn 2; os achados `-2` são as partes seguintes, sem frase em comum (conferido).
- **Desculpas (vv. 12–13)**: ficou *Gen. ad litt.* XI, 35, 47–48, e não *Civ.* XIV, 14, o texto mais citado («em parte
  nenhuma soa o pedido de perdão»), porque o do *Comentário literal* diz o mesmo e mais (o jogo *confusio*/*confessio*,
  o mal atribuído ao Criador, o salmista). Trocar é fácil; o de *Civ.* XIV, 14 está nas pistas.
- **Gn 3,15**: Agostinho lê «ipsa observabit caput», e não como profecia de Maria; por isso o achado do v. 15 é moral (a
  primeira sugestão) e o de Maria vem de um sermão que não cita o versículo (289, 2: Eva e Maria). No `traducao_pt`
  ficou «ela vigiará a tua cabeça», que é o que ele leu.
- **O «dragão»** de `agostinho-en103-4-11` é o do Sl 104,26 (Vulgata 103), que ele identifica com a serpente; o resumo
  diz isso. A citação «comerás terra» segue a Bíblia dele (*Terram manducabis*), porque a frase seguinte joga com «és
  terra».
- **Sem tema próprio para as túnicas e os querubins**: Agostinho só tem alegoria (pistas); os outros grupos cobrem.
- **`agostinho-gnlitt-11-42-59`** compara Adão a Salomão e diz que ele não foi vencido «pela cobiça da carne»; cortei a
  oração técnica que segue («que ainda não sentia na lei dos membros…»).
- `agostinho-sermo-174-2` e `agostinho-doctrchr-1-14-13` servem a um tema final («ó feliz culpa» / o remédio), se
  houver; senão, cabem no trecho 4 (o primeiro com «onde estaria ele», eco do v. 9).

## O que não existe

Ver `base/_ausentes-agostinho.md`: a leitura mariana de Gn 3,15 (não há), o «ó feliz culpa» (não é dele), o *Tract. in
Io.* 120, 2 (já publicado), o *Enchiridion* 26–27 e o *De Trinitate* XII, 12–13 (técnicos), os querubins (só alegoria).

## Pistas não seguidas

- *En. in Ps.* 139 (PL 37, 1814; o suor do rosto e a face de Deus): bonito, não baixado do augustinus.it; o número do
  arquivo na tabela de `fontes/agostinho.md` (Sl 119–150 = 177–208) dá `esposizione_salmo_197_testo.htm`.
- *Contra Iulianum* e *De nuptiis et concupiscentia* (as obras sobre o pecado original) não foram abertos: técnicos.
- *De libero arbitrio* III (por que Deus fez quem ia pecar) e *De correptione et gratia* 10–12 (Adão podia não pecar):
  não estão no cache do Corpus Corporum; técnicos.
- O resto em `base/_pistas-agostinho.md`.

## Para outros capítulos

- **Gn 2,21-22** (Eva do lado de Adão; a Igreja do lado de Cristo): *Sermão* 336, 5 (PL 38, 1474–1475): «daquele lado
  foi feita Eva, que pecando nos matasse; deste lado, a Igreja, que dando à luz nos vivificasse»; *En. in Ps.* 103, s.
  4, 6 (PL 37, 1381). O mesmo que o `agostinho-io-120-2`, já publicado.
- **Gn 4,9** (Caim que nega): *Civ.* XIV, 14 (PL 41, 422): Adão e Eva não negam o que fizeram, «como Caim», mas jogam a
  culpa em outro.
- **Gn 2,15-17** (a vida no paraíso, o preceito leve): *Civ.* XIV, 26 (PL 41, 434) e XIV, 12 (PL 41, 420).
