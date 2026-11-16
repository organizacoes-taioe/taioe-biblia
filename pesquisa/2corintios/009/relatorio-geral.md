# 2Cor 9: relatório do grupo «geral» (todos os grupos), 2026-11-15

Achados em `achados-geral.json`: **22**. Por trecho: 1 = 3, 2 = 19 (trechos: 1 (vv. 1–5), 2 (vv. 6–15)). Relevância: 3 = 14, 2 = 8. Crisóstomo e Tomás juntos: 4 de 22.

Os `original` que não estão em `base/` ficam também em `textos/` (um arquivo por autor e obra).

## Como se procurou

- Lidos o pedido (`../PEDIDO-8-13.md`), o texto do capítulo (`conteudo/2corintios/009.json`), o `BASE.md`, `proximos.md` e o relatório do 2Cor 7 como modelo.
- Latinos: busca por frases da Vulgata (e de variantes) nos 815 textos da PL já guardados em `pesquisa/cache/*-latinos/` (índice em `~/.cache/taioe-2cor-comum/latinos67/`; padrões e resultados em `~/.cache/taioe-2cor8-13/cap89/pats.txt` e `hits.json`), depois leitura de cada passagem no texto bruto; cada `original` é cópia exata da PL do Corpus Corporum, com cortes «[…]». Correções mínimas: «vanem» por «panem» (Leão, Sermão 48, 5), «abundatia» por «abundantia» (Gregório, *Regra pastoral*), e tirado o intertítulo «CAPUT III.» do meio do Sermão 36 de Agostinho.
- Gregos: busca em massa por frases do capítulo no corpus grego `pesquisa/cache/genesis/gregos/corpus4` (911 textos); entraram Clemente (*Quis dives*) e Nazianzeno (Disc. 1). Crisóstomo (homilias sobre 2Cor) e Tomás vêm de `base/`.
- Santos modernos: Escrivá pelas pistas de `base/_pistas-escriva.md` (texto espanhol, escriva.org); Papas pelo cache `pesquisa/cache/2corintios/modernos67/vat/` (Francisco, Bento XVI), só 2 a 3 frases em italiano.
- Orientais: Crisóstomo, Nazianzeno e Clemente. Efrém (OCR ruim no `base/`, tradução latina do armênio), Teodoreto, Teofilato e Ecumênio ficaram sem achado por falta de conferência na imagem (ver «Pistas não seguidas»).

## O que não existe ou não rendeu (não procurar de novo)

- Catecismo da Igreja Católica: não foi varrido (os arquivos do Catecismo não estavam no cache); candidatos a conferir: CIC 2443–2447 (esmola, obras de misericórdia) e 1969; também *Gaudium et spes* 69, que cita 2Cor 8,13 na nota.
- Afraates, *Dem.* 20 (no corpus siríaco, `pesquisa/cache/genesis/orientais/sc/data/tei/20.xml`): §9 cita 2Cor 8,9 e §18 cita 9,6, mas o capítulo é polêmico e a tradução do siríaco precisaria de revisão; não entrou.
- Cesário de Arles (Sermões, sobre os dízimos e a esmola) cita 9,7 e 9,9 só em listas de textos; Isidoro (*Regra dos monges*) e Basílio (*Quod rebus mundanis*, de autenticidade duvidosa) também só citam.
- Santo Afonso, Francisco de Sales (*Index scripturaire*), Teresinha, João da Cruz e Newman: não varridos para estes capítulos.

## O que entrou

| autor | obra | onde | trecho | resumo |
|---|---|---|---|---|
| São Gregório Magno | Homilias sobre Ezequiel | livro II, homilia 6, 13 (PL 76, 1005B–C) | 1 (vv. 1, 2) | Gregório mostra como Paulo elogia os coríntios: louva a boa vontade deles, mas não sem uma censura, porque fizeram o bem tarde; é o médico que reanima o são e morde o podre. |
| São João Crisóstomo | Homilias sobre a Segunda Carta aos Coríntios | Homilia 19, 2 (PG 61, 531) | 1 (vv. 3, 4) | Crisóstomo observa o tato de Paulo: a vergonha de que fala é a dele («para não dizer vós»), e serve para animar os que se destacam nas outras virtudes. |
| Ambrosiaster | Comentário à Segunda Carta aos Coríntios | sobre 2Cor 9,5 (PL 17, 312C–D) | 1 (vv. 5) | Ambrosiaster explica a delicadeza de Paulo ao mandar os irmãos adiante: lembra os coríntios do que prometeram, por causa da boa fama deles, para que deem sem se arrepender. |
| São Gregório Magno | Regra pastoral | III, 20 (PL 77, 84B–D) | 2 (vv. 6, 7) | Gregório, aconselhando quem distribui os seus bens, aplica a cada defeito do doador uma palavra da Escritura: contra a tristeza, «Deus ama quem dá com alegria»; contra a avareza, «quem semeia com parcimônia…». |
| Santo Agostinho | Sermões | Sermão 165, 4 (PL 38, 904) | 2 (vv. 7) | Agostinho liga a alegria de dar à «largura» da caridade: quem dá apertado dá triste, e o que dá triste perde. |
| Santo Agostinho | A catequese dos principiantes | II, 4 (PL 40, 312) | 2 (vv. 7) | Agostinho aplica 9,7 a quem catequiza: se Deus ama quem dá dinheiro com alegria, quanto mais quem dá a doutrina; e essa alegria é, ela mesma, dom de Deus. |
| Santo Ambrósio | Sobre os deveres dos ministros | I, 143–144 (PL 16, 65B) | 2 (vv. 7) | Ambrósio diz que a beneficência perfeita junta querer o bem e fazê-lo, e que só vale o que nasce da boa vontade: «Deus ama quem dá com alegria». |
| São Leão Magno | Sermões | Sermão 87, 4 (PL 54, 440B–C) | 2 (vv. 6, 7) | Leão garante que a esmola é semente que nenhum calor, torrente ou granizo destrói: o que se dá ao pobre sobe do céu como prêmio, pois Cristo é o devedor. |
| São Leão Magno | Sermões | Sermão 48, 5 (PL 54, 300C–301A) | 2 (vv. 10) | Leão diz que quem dá esmola não precisa temer a falta, porque a mão que multiplica o pão intervém em toda obra de misericórdia; por isso o esmoleiro seja seguro e alegre. |
| São Pedro Crisólogo | Sermões | Sermão 42 (PL 52, 318B–D) | 2 (vv. 6, 7) | Crisólogo diz que o jejum só frutifica se for regado pelas lágrimas dos pobres: quem semeia misericórdia no pobre colhe no céu, e assim se cumpre 9,6-7. |
| São Cipriano de Cartago | Sobre as obras e as esmolas | 9 (PL 4, 608B–609A) | 2 (vv. 10, 12) | Cipriano responde a quem teme empobrecer dando esmolas: o que se gasta a serviço de Cristo não se esgota, e a oração agradecida dos pobres sobe a Deus e volta como retribuição. |
| São Máximo de Turim | Sermões | Sermão 21 (PL 57, 578A–B) | 2 (vv. 7) | Máximo manda jejuar de modo que o jejum alegre o outro: quando o pobre come do que o jejum poupou, quem almoça é Cristo. |
| São Bernardo de Claraval | Sermões diversos | Sermão 41, 6 (PL 183, 656D) | 2 (vv. 7) | Bernardo aplica 9,7 à obediência: obedecer é dar-se, e só agrada a Deus quem obedece com serenidade no rosto e doçura nas palavras. |
| Clemente de Alexandria | Que rico se salva? | 31, 7–9 (texto grego do corpus «Dromoi tes pisteos»; ed. O. Stählin, GCS 17 (1909)) | 2 (vv. 7) | Clemente de Alexandria acha bela a palavra de Paulo sobre o dar com alegria, mas ainda melhor a do Senhor: quem dá sem esperar que lhe peçam imita a Deus. |
| São João Crisóstomo | Homilias sobre a Segunda Carta aos Coríntios | Homilia 19, 3 (PG 61, 532) | 2 (vv. 6, 7) | Crisóstomo nota que Paulo chama a esmola de «semente» para que se pense na colheita, e que não cessa de repetir que o dom deve ser livre e alegre. |
| São João Crisóstomo | Homilias sobre a Segunda Carta aos Coríntios | Homilia 20, 2 (PG 61, 538) | 2 (vv. 15) | Crisóstomo entende o «dom inefável» como os bens da esmola e, sobretudo, a vinda de Cristo, e conclui que lembrar o que se recebeu é o maior incentivo à virtude. |
| São Gaudêncio de Bréscia | Tratados | Sermão 2 (PL 20, 859B–C) | 2 (vv. 15) | Gaudêncio vê o «dom inenarrável» na Eucaristia, penhor da presença de Cristo e viático da nossa viagem. |
| São Tomás de Aquino | Comentário à Segunda Carta aos Coríntios | cap. 9, lição 1 (Corpus Thomisticum [87724]) | 2 (vv. 6) | Tomás explica que «quem semeia com parcimônia» ceifa pouco, mas que a medida é a caridade: quem dá pouco com grande amor ceifará com abundância. |
| Ambrosiaster | Comentário à Segunda Carta aos Coríntios | sobre 2Cor 9,6-7 (PL 17, 313A) | 2 (vv. 6, 7) | Ambrosiaster explica o «parcimonioso» como o avarento que se arrepende de ter prometido, e diz que o dom só aproveita se for feito de ânimo alegre. |
| São Josemaria Escrivá | Amigos de Deus | n. 126, «Desprendimento» (Amigos de Dios, n. 126) | 2 (vv. 7, 8) | São Josemaria diz que o desprendimento verdadeiro leva a gastar-se pelos necessitados, por caridade e por justiça, sem mesquinharia com quem se entregou sem medida. |
| São Josemaria Escrivá | Amigos de Deus | n. 140, «Atrás dos passos do Senhor» (Amigos de Dios, n. 140) | 2 (vv. 7) | São Josemaria aplica 9,7 à vida de cada dia: quem suporta a contrariedade lamentando-se desperdiça a graça; Deus quer a entrega alegre de um coração enamorado. |
| Papa Francisco | Mensagem para a Quaresma de 2022 | 2022, n. 2 (Mensagem de 11 de novembro de 2021) | 2 (vv. 7, 10) | O Papa Francisco pede, na Quaresma, a esmola dada com alegria: Deus, que dá a semente ao semeador, nos provê para sermos generosos com os outros. |

## Liturgia da Missa onde o capítulo é lido (só datas e referências; o texto da CNBB tem direito autoral)

| ocasião | leitura |
|---|---|
| quarta-feira da 11ª semana do Tempo Comum, ano I | 2Cor 9,6-11 |
| São Lourenço, diácono e mártir (10 de agosto) | 2Cor 9,6-10 |

## Em dúvida

- Gregório, *Homilias sobre Ezequiel*: a passagem está no livro II, homilia 6, n. 13 (PL 76, 1005B), conferida só pela coluna da PL; confirmar o número da homilia na edição.
- Cipriano, *De opere et eleemosynis* 9: a PL numera os parágrafos em romano (IX); a edição de Hartel (CSEL 3) traz o mesmo trecho no cap. 9.

## Para outros capítulos (não mexi em `proximos.md`)

- 2Cor 8: Gregório, *Moralia* XX, 36 (8,9.13) e *Regra pastoral* III, 20 (8,13-14) entraram no cap. 8.
- 2Cor 10 e 12: Gregório, *Hom. Ez.* II, 6 fala da mansidão de Paulo (10,1) e pode ser lido de novo no cap. 10.
