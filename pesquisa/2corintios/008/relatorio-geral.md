# 2Cor 8: relatório do grupo «geral» (todos os grupos), 2026-11-15

Achados em `achados-geral.json`: **25**. Por trecho: 1 = 3, 2 = 17, 3 = 5 (trechos: 1 (vv. 1–6), 2 (vv. 7–15), 3 (vv. 16–24)). Relevância: 3 = 16, 2 = 9. Crisóstomo e Tomás juntos: 5 de 25.

Os `original` que não estão em `base/` ficam também em `textos/` (um arquivo por autor e obra).

## Como se procurou

- Lidos o pedido (`../PEDIDO-8-13.md`), o texto do capítulo (`conteudo/2corintios/008.json`), o `BASE.md`, `proximos.md` e o relatório do 2Cor 7 como modelo.
- Latinos: busca por frases da Vulgata (e de variantes) nos 815 textos da PL já guardados em `pesquisa/cache/*-latinos/` (índice em `~/.cache/taioe-2cor-comum/latinos67/`; padrões e resultados em `~/.cache/taioe-2cor8-13/cap89/pats.txt` e `hits.json`), depois leitura de cada passagem no texto bruto; cada `original` é cópia exata da PL do Corpus Corporum, com cortes «[…]». Correções mínimas: «vanem» por «panem» (Leão, Sermão 48, 5), «abundatia» por «abundantia» (Gregório, *Regra pastoral*), e tirado o intertítulo «CAPUT III.» do meio do Sermão 36 de Agostinho.
- Gregos: busca em massa por frases do capítulo no corpus grego `pesquisa/cache/genesis/gregos/corpus4` (911 textos); entraram Clemente (*Quis dives*) e Nazianzeno (Disc. 1). Crisóstomo (homilias sobre 2Cor) e Tomás vêm de `base/`.
- Santos modernos: Escrivá pelas pistas de `base/_pistas-escriva.md` (texto espanhol, escriva.org); Papas pelo cache `pesquisa/cache/2corintios/modernos67/vat/` (Francisco, Bento XVI), só 2 a 3 frases em italiano.
- Orientais: Crisóstomo, Nazianzeno e Clemente. Efrém (OCR ruim no `base/`, tradução latina do armênio), Teodoreto, Teofilato e Ecumênio ficaram sem achado por falta de conferência na imagem (ver «Pistas não seguidas»).

## O que não existe ou não rendeu (não procurar de novo)

- Catecismo da Igreja Católica: não foi varrido (os arquivos do Catecismo não estavam no cache); candidatos a conferir: CIC 2443–2447 (esmola, obras de misericórdia) e 1969; também *Gaudium et spes* 69, que cita 2Cor 8,13 na nota.
- Afraates, *Dem.* 20 (no corpus siríaco, `pesquisa/cache/genesis/orientais/sc/data/tei/20.xml`): §9 cita 2Cor 8,9 e §18 cita 9,6, mas o capítulo é polêmico e a tradução do siríaco precisaria de revisão; não entrou.
- Basílio, *Regras morais* (PG 31, 769) e a *Homilia aos ricos* (final) citam 8,9 e 8,14-15 sem comentá-los; entraram só como pista.
- Cassiano (*Da Encarnação*, polêmica contra Nestório), Cesário de Arles (citações em lista) e Pedro Crisólogo (Sermão 160) citam 8,9 ou 8,14 sem comentar.
- Santo Afonso, Francisco de Sales (*Index scripturaire*), Teresinha, João da Cruz e Newman: não varridos para estes capítulos.

## O que entrou

| autor | obra | onde | trecho | resumo |
|---|---|---|---|---|
| São João Crisóstomo | Homilias sobre a Segunda Carta aos Coríntios | Homilia 16, 2 (PG 61, 514) | 1 (vv. 2) | Crisóstomo explica que a pobreza dos macedônios foi ocasião, e não obstáculo, da sua generosidade: o empenho se julga pela disposição de quem dá, não pela quantia. |
| Santo Ambrósio | Nabot, o israelita | cap. 14, 60 (PL 14, 750A–B) | 1 (vv. 2) | Ambrósio lê «a sua profunda pobreza transbordou em riquezas de generosidade» como lição sobre a verdadeira riqueza: ser rico para Deus é ser rico de fé, de misericórdia e de simplicidade. |
| São Tomás de Aquino | Comentário à Segunda Carta aos Coríntios | cap. 8, lição 1 (Corpus Thomisticum [87721]) | 1 (vv. 5) | Tomás vê na frase «deram-se a si mesmos, primeiro ao Senhor» a ordem certa do dar: antes do dom, a pessoa; Deus olhou primeiro para Abel e depois para a sua oferta. |
| Santo Ambrósio | Sobre os deveres dos ministros | I, 150 (PL 16, 67B–C) | 2 (vv. 9, 10) | Ambrósio diz que ninguém deve envergonhar-se de empobrecer para socorrer o pobre, porque Cristo, sendo rico, se fez pobre e deixou essa regra. |
| Santo Ambrósio | Sobre os deveres dos ministros | I, 153–154 (PL 16, 68B–C) | 2 (vv. 14, 15) | Ambrósio entende a «igualdade» de 8,14 como troca: o povo sustenta os santos com bens materiais e recebe deles a graça espiritual; e, no maná, quem tem muito não tem demais. |
| Santo Ambrósio | Tobias | cap. 16, 56 (PL 14, 781B–C) | 2 (vv. 9) | Ambrósio exorta os ricos a não temer a pobreza: Cristo, que se fez pobre, enriquece; o dinheiro dado ao pobre fica guardado sem vigia. |
| Santo Agostinho | Sermões | Sermão 36, 3 (PL 38, 215–216) | 2 (vv. 9) | Agostinho explica a pobreza de Cristo: ele se fez mortal, não perdeu as riquezas da divindade e, com o seu sangue, nos revestiu de imortalidade, a verdadeira riqueza. |
| Santo Agostinho | Sermões | Sermão 41, 7 (PL 38, 251) | 2 (vv. 9) | Agostinho responde a quem hesita em dar esmola por duvidar do pobre: o Senhor, rico, se fez pobre por nós até a cruz, e quem olha para a sua pobreza aprende a não calcular. |
| São Leão Magno | Sermões | Sermão 9, 3 (PL 54, 162D–163A) | 2 (vv. 9) | Leão vê o Cristo que se fez pobre presente nos pobres: quem o adora como Rei no céu o alimenta nos necessitados. |
| São Gregório Magno | Morais sobre Jó | XX, 36 (PL 76, 179C–180B) | 2 (vv. 9, 10, 13) | Gregório une 8,9, 8,13 e 9,6: Deus apareceu pobre para despertar a compaixão, e dar de coração vale mais do que dar de mão. |
| São Gregório Magno | Regra pastoral | III, 20 (PL 77, 84D–85A) | 2 (vv. 13, 14) | Gregório lê «não que os outros tenham alívio e vós, aperto» como aviso de prudência: é preciso preparar a alma para a pobreza antes de dar muito, para que a murmuração não estrague a generosidade. |
| São Bernardo de Claraval | Sermões sobre o Cântico dos Cânticos | Sermão 18, 3 (PL 183, 861A–B) | 2 (vv. 13) | Bernardo lê «de igualdade» como medida da caridade: só se pode derramar o que se tem de sobra; a concha imita a fonte, que primeiro se enche. |
| São Paulino de Nola | Cartas | Carta 32, 21 (PL 61, 340D–341A) | 2 (vv. 14, 15) | Paulino lê a «igualdade» de 8,14 como plano de Deus: o rico e o pobre se completam, e o que se dá aqui ao pobre volta como socorro lá. |
| São Gregório Nazianzeno | Discursos | Discurso 1, 5 (PG 35, 397–400) | 2 (vv. 9) | Gregório Nazianzeno faz de 8,9 o primeiro de uma série de trocas: Cristo tomou o que é nosso para nos dar o que é dele. |
| São João Crisóstomo | Homilias sobre a Segunda Carta aos Coríntios | Homilia 17, 2 (PG 61, 517–518) | 2 (vv. 9) | Crisóstomo explica que a «riqueza» recebida por meio da pobreza de Cristo é o conhecimento da fé, o perdão, a justiça e a santificação, tudo vindo da Encarnação e da Paixão. |
| São João Crisóstomo | Homilias sobre a Segunda Carta aos Coríntios | Homilia 17, 3 (PG 61, 520) | 2 (vv. 15) | Crisóstomo lê o maná como lição de igualdade: ninguém fica com mais do que come, e o pobre que recebe esmola é útil a todos, pois dá ao rico onde pôr o seu dinheiro. |
| São Tomás de Aquino | Comentário à Segunda Carta aos Coríntios | cap. 8, lição 2 (Corpus Thomisticum [87722]) | 2 (vv. 9) | Tomás analisa as palavras de 8,9: «necessitado» é mais que pobre, «sendo rico» diz que Cristo não perdeu as riquezas, e a pobreza dele é exemplo e sacramento para nós. |
| São Josemaria Escrivá | Amigos de Deus | n. 110, «Desprendimento» (Amigos de Dios, n. 110) | 2 (vv. 9) | São Josemaria convida a meditar a vida inteira o exemplo de Cristo, que se fez pobre por cada um, e a tirar daí propósitos de maior generosidade. |
| Papa Francisco | Mensagem para a Quaresma de 2014, «Fez-se pobre para nos enriquecer com a sua pobreza» | 2014, «A graça de Cristo» (Mensagem de 26 de dezembro de 2013) | 2 (vv. 9) | O Papa Francisco vê em 8,9 o estilo de Deus: a fraqueza e a pobreza, não o poder, porque o amor partilha a sorte do amado e cria igualdade. |
| Bento XVI | Mensagem para a Quaresma de 2008, «Cristo se fez pobre por vós» | 2008, n. 5 (Mensagem de 30 de outubro de 2007) | 2 (vv. 9) | Bento XVI, depois da viúva do Evangelho, lembra que Cristo, que se fez pobre por nós, se deu todo; a esmola da Quaresma é seguir esse exemplo. |
| Santo Agostinho | Cartas | Carta 125, 2, a Alípio (PL 33, 474–475) | 3 (vv. 21) | Agostinho, ao ver a suspeita do povo contra o dinheiro da Igreja, aplica 8,21: a boa consciência não basta a quem cuida de bens alheios; é preciso também cuidar do que se vê. |
| Santo Agostinho | Sermões | Sermão 355, 1 (PL 39, 1569) | 3 (vv. 21) | Agostinho distingue consciência e fama: a consciência é para si, a boa fama é para o próximo, e quem a descuida, sobretudo se é pastor, é cruel. |
| Santo Agostinho | A doutrina cristã | IV, 28, 61 (PL 34, 119) | 3 (vv. 21) | Agostinho diz que o pregador deve viver bem e cuidar também da boa fama, «diante de Deus e dos homens», para ser ouvido. |
| São Jerônimo | Homens ilustres | cap. 7, Lucas (PL 23, 619B) | 3 (vv. 18) | Jerônimo identifica o «irmão cujo louvor está no Evangelho» com Lucas, companheiro de Paulo e autor do Evangelho. |
| Bento XVI | Audiência geral de 13 de dezembro de 2006, sobre Timóteo e Tito | 13/12/2006 (Audiência geral) | 3 (vv. 6, 23) | Bento XVI situa a missão de Tito em Corinto: concluir as coletas para Jerusalém, como «companheiro e colaborador» de Paulo. |

## Liturgia da Missa onde o capítulo é lido (só datas e referências; o texto da CNBB tem direito autoral)

| ocasião | leitura |
|---|---|
| 13º domingo do Tempo Comum, ano B | 2Cor 8,7.9.13-15 |
| terça-feira da 11ª semana do Tempo Comum, ano I | 2Cor 8,1-9 |
| Ofício das Leituras, segunda-feira da 17ª semana do Tempo Comum | 2Cor 8,1-24 (2ª leitura: São Basílio, Homilia 6) |

Texto do lecionário: ver `../002/liturgia-2cor-2.md` e Vatican News (17/06/2025).

## Em dúvida

- Jerônimo, *Homens ilustres* 7 (8,18): é a leitura tradicional (o irmão é Lucas), não a única: Crisóstomo (hom. 18) discute se é Lucas ou Barnabé; relevância 2, a decidir pelo Gere.
- Paulino de Nola, Carta 32, 21: o número da carta é o da PL (na edição de Hartel é a Carta 34).

## Para outros capítulos (não mexi em `proximos.md`)

- 2Cor 9: Ambrosiaster sobre 9,5-7 e Gregório, *Regra pastoral* III, 20 (9,6-7) entraram no cap. 9; o excerto de Gregório sobre 8,13-14 é de outro trecho da mesma passagem.
- 2Cor 13,5: Agostinho, *Sermão* 355, 1 (consciência e fama) pode servir também ao «examinai-vos a vós mesmos».
