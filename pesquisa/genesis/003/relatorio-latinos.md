# Gênesis 3: relatório do grupo «latinos» (26/10/2026)

Latinos antigos e medievais, menos Agostinho. Partiu-se da pré-pesquisa (`BASE.md`: Ambrósio, *De paradiso*;
Beda; Ruperto; Rábano; Alcuíno; Isidoro; Hugo, *Adnotationes* e *De sacramentis* I, 7; Jerônimo; Lápide) e das
pistas de Gn 2 (`../002/relatorio-latinos.md`, «Para outros capítulos»), e procurou-se o resto nos sermões, cartas
e tratados da PL. Entregues **16 achados** em `achados-latinos.json`: trecho 1 = 5, trecho 2 = 4, trecho 3 = 3,
trecho 4 = 4. Dez autores; Ambrósio tem 4, Gregório, Leão e Bernardo têm 2.

## Como se procurou

1. Leitura das obras da base que comentam o capítulo: Ambrósio, *De paradiso* 12–15 (a base só tinha 13, 64 em
   diante; os caps. 12–13 vieram do texto inteiro, no cache); Ruperto, *In Genesim* III, 1–36; Beda; Hugo,
   *De sacramentis* I, 7, 1–10; Jerônimo; Alcuíno. Rábano, Isidoro e Lápide só por amostra (compilação e alegoria).
2. Varredura dos 167 textos da PL que já estavam em `pesquisa/cache/genesis/latinos/` (o cache de Gn 1 e Gn 2,
   Corpus Corporum: Ambrósio, Bernardo inteiro, Gregório, Leão, Crisólogo, Máximo de Turim, Tertuliano, Cipriano,
   Jerônimo, Hilário, Zenão, Gaudêncio, Paulino, Anselmo, Lombardo, Comestor, Honório…) pelas notas de Migne
   «(Gen. III…)» e por 45 frases da Vulgata e da Vetus Latina de Gn 3: 687 parágrafos com ocorrência, resumidos
   numa linha cada, e o contexto aberto só dos melhores. Nada novo precisou ser baixado.
3. Corpus Thomisticum: a II-II, q. 155–169 está no arquivo `sth3155.html` (as questões vêm agrupadas; `sth3163`
   não existe), já no cache; III, q. 1 em `sth4001.html`. Boaventura, *Breviloquium* III, 2–3, no OCR de Quaracchi V
   (`bonav-05.txt`, no cache).
4. Cada `original` saiu por script como substring exata do texto limpo (sem as notas de Migne, as marcas de coluna,
   os números de página da edição anterior e os parágrafos numerados soltos), com a coluna calculada sozinha. Os
   scripts estão em `~/.cache/taioe-gn3/latinos/` (`varrer.py`, `ver.py`, `ct.py`, `excerto.py` com `specs.json`,
   `gerar.py`); `excertos.json` ali guarda também os originais prontos de seis reservas (abaixo).

## O que se achou

| autor | obra | onde | situação |
|---|---|---|---|
| Santo Ambrósio | *De paradiso* 12, 54 (a inveja do diabo) e 14, 70 («Onde estás?») | PL 14, 301A–C; 309C–310B | 2 achados |
| Santo Ambrósio | *De paradiso* 12, 56 («nem o tocareis»); 13, 61 (de tudo o que prometeu, só uma coisa era verdade); 13, 64–65 (as folhas: as desculpas e os exemplos dos santos que pecaram); 14, 71 (Eva confessa, «culpa perdoável a que vem com a confissão»); 15, 77 (não é maldito o homem, mas a serpente) | PL 14, 302D–303B; 306C; 307C–308A; 310B–D; 314B–C | reserva |
| Santo Ambrósio | *De excessu fratris* II, 37–38 (a morte como remédio, não como castigo) | PL 16, 1325A–B | 1 achado; II, 47 (1327C) diz o mesmo em tese, sem ler o versículo: reserva |
| Santo Ambrósio | *Explanatio psalmorum XII*, Sl 39, 19–20 (o bom ladrão; «Felix ruina»; «Eu te pus na luz») | PL 14, 1065A–1066A | 1 achado |
| Santo Ambrósio | *In Lucam* IV, 7 (do paraíso ao deserto, do deserto ao paraíso; «Mors per arborem, vita per crucem») | PL 15, 1614B–C | reserva forte (original pronto) |
| Santo Ambrósio | *De Iacob* I, 6, 21 («Fructuosior culpa quam innocentia») | PL 14, 607B–C | reserva (fala da Lei, Rm 7, não de Gn 3) |
| Santo Ambrósio | *De institutione virginis* 17, 104 («Amplius nobis profuit culpa, quam nocuit») | PL 16, 331A | reserva (virgindade) |
| São Bernardo | *De diversis* 22, 3 («Deus afirma, a mulher duvida, Satanás nega») | PL 183, 596C–D | 1 achado |
| São Bernardo | *Super Missus est* II, 3 (a desculpa de Adão mudada em ação de graças) | PL 183, 62B–63A | 1 achado |
| São Bernardo | *Super Missus est* II, 4 («Ipsa conteret»: Maria); *Dom. infra oct. Assumptionis* 4 | PL 183, 63B; 431C–D | reserva |
| São Bernardo | *De diversis* 66, 1–3 (os sete pecados da queda e as bem-aventuranças: Adão «pôs a vontade da mulher acima da de Deus»; «cruel consigo, que se desculpou, e com a mulher, que acusou») | PL 183, 688A–689B | reserva |
| São Gregório Magno | *Hom. in Ev.* I, 16, 2–3 (as três tentações de Adão e as de Cristo) | PL 76, 1136A–B | 1 achado |
| São Gregório Magno | *Moralia* XXII, 15, 30–31 (as desculpas; «esconde o Senhor de si») | PL 76, 230C–231C | 1 achado |
| São Gregório Magno | *Moralia* XXVIII, 1, 6 (Deus já não está parado, mas passeia; a brisa da tarde, o fervor da caridade perdido); XXXII, 22 (a «arma» da desculpa, 706A) | PL 76, 449C–450A; 705D–706A | reserva |
| São Leão Magno | Sermão 24, 2 («quis ocupar a honra em vez de merecê-la») | PL 54, 205A–B | 1 achado |
| São Leão Magno | Sermão 22, 1 (o protoevangelho: o remédio anunciado logo depois da queda) | PL 54, 194A | 1 achado |
| São Máximo de Turim | Homilia 53 (Adão se esconde, Pedro chora) | PL 57, 350C–351B | 1 achado |
| São Cipriano | *De bono patientiae* 11 (a sentença de Adão prende a todos) | PL 4, 629B–630A | 1 achado |
| São Cipriano | *Testimonia* II, 9 («Hoc semen praedixerat Deus de muliere procedere, quod calcaret caput diaboli») | PL 4, 704B–C | só a frase-título da lista de textos; reserva |
| São Pedro Crisólogo | Sermão 74 (na Páscoa, a mulher se torna mãe dos viventes) | PL 52, 409A–B | 1 achado |
| São Pedro Crisólogo | Sermão 148 (o anjo mau e Gabriel; «o homem, antes senhor de todos, caiu na servidão de todos») e 64 (Marta, «mãe dos viventes») | PL 52, 597C–598A; 380A | reserva |
| São Beda | *In principium Genesis* I, sobre 3,21 (as túnicas e a «primeira túnica» do pródigo) | PL 91, 60B–D | 1 achado |
| São Beda | sobre 3,8 (Cristo sobe à cruz ao meio-dia e morre à hora nona, «a mesma hora» do pecado) e 3,24 (a espada «versátil» removida no batismo) | PL 91, 55D–56A; 61D–62A | reserva |
| Ruperto de Deutz | *In Genesim* III, 29 (a árvore da vida negada por misericórdia) | PL 167, 315D–316D | 1 achado |
| Ruperto de Deutz | III, 14 («o lugar do homem é Deus, fora do qual não se está bem em lugar nenhum»); III, 6 (o diabo quer fazer Deus mentiroso como ele); III, 25 (a mortalidade, graça e não ira); III, 32 (a espada: ira no fogo, misericórdia em ser «versátil»; o bom ladrão) | PL 167, 300A–D; 292C–D; 311D–312C; 319A–320A | reserva (III, 14 forte, original pronto) |
| São Tomás | *Suma* II-II, q. 163, a. 1–2 (o primeiro pecado foi a soberba: decidir por si o bem e o mal) | Leonina 10 | 1 achado |
| São Tomás | II-II, q. 164, a. 2 (as penas, uma a uma; as túnicas «em sinal de mortalidade»); q. 165, a. 1–2 (por que Deus permitiu a tentação); III, q. 1, a. 3, ad 3 (o «ó feliz culpa» do Exsultet) | Leonina 10–11 | reserva (III, q. 1, original pronto) |
| Hugo de São Vítor | *De sacramentis* I, 7, 4 («Deus affirmavit; mulier dubitavit; diabolus negavit»… «quem duvidou se afastou de quem afirma e se aproximou de quem nega»); 7, 2 (por que serpente e não pomba) | PL 176, 288C–D; 287C | reserva (a mesma tríade de Bernardo) |
| Santo Anselmo | *Cur Deus homo* I, 3 (por uma mulher o pecado, de uma mulher o Salvador; o diabo vencido pela árvore como venceu pela árvore) | PL 158, 364C | reserva (é o prefácio da Santa Cruz explicado) |
| São Boaventura | *Breviloquium* III, 2–3 (a tentação pela tríplice concupiscência de 1Jo 2,16) | Quaracchi V | OCR ruim; segue Gregório e Hugo; reserva |
| São Jerônimo | Carta 22, 18–21 («Mors per Evam, vita per Mariam», PL 22, 408) | PL 22, 405–408 | fora: o assunto é a virgindade, a frase sozinha repete Agostinho, *Sermão* 289, 2 |
| São Jerônimo | *Quaestiones hebraicae*: 3,1 (*arum*, «astuto», não «sábio»), 3,15 («ipse conteret»), 3,17 («maldita por tua causa», não «nas tuas obras»), 3,24 | PL 23, 942B–944A | nota de língua; sem achado |
| Tertuliano | *De carne Christi* 17 («Crediderat Eva serpenti: credidit Maria Gabrieli») | PL 2, 782B | reserva (é Justino e Ireneu, grupo dos gregos, em latim) |
| Tertuliano | *De resurrectione* 7 (as túnicas de pele «são a pele posta por cima») | PL 2, 803B–804B | fora: especulação sobre a carne e a pele |
| Alcuíno | *Interrogationes* 10, 60–82 | PL 100, 517; 522–524 | quase tudo de Agostinho e Beda; a 10 (a terra amaldiçoada e não as águas, «porque nas águas Deus ia lavar o pecado») é bonita, mas especulativa: reserva |
| Rábano, Isidoro, Hugo (*Adnotationes*), Lápide | | | base; compilação, alegoria, notas de língua; sem achado próprio |
| Zenão, Hilário, Gaudêncio, Paulino, Cesário, Fulgêncio, Honório, Comestor, Lombardo | | | só de passagem ou repetindo os anteriores; ver `base/_ausentes-latinos.md` |

## Os 16 achados

1. **Trecho 1 (vv. 1–7)**: Ambrósio, *De paradiso* 12, 54: a serpente sábia é o diabo, e a causa da inimizade é a
   inveja (Sb 2,24): «Este inferior vai alcançar o que eu não pude guardar?» (3); Bernardo, *De diversis* 22, 3: não
   um leão, mas a serpente, que começa perguntando; «Deus afirma, a mulher duvida, Satanás nega» (3); Tomás, II-II,
   q. 163: a soberba de querer ser como Deus, «determinar por si mesmo o que é bom e o que é mau» (3); Gregório,
   *Hom. in Ev.* 16, 2–3: gula, vanglória e ambição de grandeza, as mesmas três tentações que Cristo vence no deserto
   (3; Migne: «pregada ao povo na basílica de São João, no 1º domingo da Quaresma», sobre Mt 4,1-11, o Evangelho do ano A); Leão, Sermão 24, 2:
   «preferiu apoderar-se da honra em vez de merecê-la», e por isso «És terra, e à terra irás» (3).
2. **Trecho 2 (vv. 8–13)**: Ambrósio, *De paradiso* 14, 70: «não pergunto em que lugar, mas em que estado»; chamar já
   é sinal de que vai curar (3); Gregório, *Moralia* XXII, 15, 30–31: as desculpas, que fazem «Deus semelhante a eles
   na culpa»; quem se esconde «não se esconde do Senhor, esconde o Senhor de si» (3); Bernardo, *Super Missus est*
   II, 3: «Senhor, a mulher que me deste me deu da árvore da vida, e eu comi» (3); Máximo de Turim, Homilia 53: Adão
   corre para o esconderijo, Pedro rompe em lágrimas (3).
3. **Trecho 3 (vv. 14–19)**: Leão, Sermão 22, 1: logo depois da queda Deus anuncia o remédio, Cristo nascido da
   Virgem (3); Ambrósio, *De excessu fratris* II, 37–38: os espinhos e o suor são castigo, a volta à terra é remédio,
   «a meta dos nossos castigos» (3); Cipriano, *De bono patientiae* 11: a sentença de Adão prende a todos, por isso a
   paciência (2).
4. **Trecho 4 (vv. 20–24)**: Crisólogo, Sermão 74: na Páscoa, «a que se tornara mãe dos que morrem» se torna mãe dos
   viventes (3); Beda: as túnicas de pele, sinal da mortalidade, e a primeira túnica que o pai devolve ao pródigo (3);
   Ruperto III, 29: «felicidade eterna, eternidade feliz»… «infelicidade temporal», para que a eternidade volte com
   a felicidade: a árvore negada por misericórdia (3); Ambrósio, Sl 39, 19–20: ao bom ladrão, «estarás comigo»;
   a Adão não o disse; «Feliz queda, que é reparada para melhor!»; «Eu te pus na luz, e tu procuraste as trevas» (3).

Os três mais fortes: `gregorio-moralia-22-15-30-esconder-o-senhor`, `bernardo-missus-est-2-3-a-arvore-da-vida`,
`ruperto-gen-3-29-a-arvore-negada-por-misericordia`. Logo atrás: `maximo-turim-hom-53-adao-se-esconde-pedro-chora`,
`ambrosio-sl-39-19-20-feliz-queda`, `bernardo-diversos-22-3-deus-afirma-satanas-nega`, `leao-sermao-24-2-ocupar-em-vez-de-merecer`.

## Sobreposições (para a escolha final)

Conferido com `achados-agostinho.json` e `achados-modernos.json`, que já estavam na pasta.

- **«Onde estás?»** está cheio: Agostinho, *Civ.* XIII, 15; Francisco (homilia de 08/07/2013); Catecismo 2568;
  aqui Ambrósio 14, 70 e Máximo (que fala do esconder, mais que da pergunta). Ambrósio 14, 70 diz o que Agostinho
  diz (não é pergunta de quem não sabe) e acrescenta que o chamado já é cura; se faltar lugar, fica Agostinho e
  sai Ambrósio. Ruperto III, 14 («o lugar do homem é Deus») é a alternativa mais bonita a Ambrósio, com o original
  pronto em `~/.cache/taioe-gn3/latinos/excertos.json` (`rup-14`). O fim do excerto de Ambrósio, Sl 39 («Eu te pus
  na luz») também toca a pergunta: se o tema ficar cheio, cortar dali a última peça.
- **As desculpas** (vv. 12–13): Agostinho, *Gen. ad litt.* XI, 35, 47 («nenhum dos dois diz pequei») e Gregório,
  *Moralia* XXII, 15, dizem o mesmo no começo; Gregório vai além (fazer Deus cúmplice; esconder Deus de si; a confissão
  como começo da luz). Bernardo, *Super Missus est* II, 3, diz outra coisa (a desculpa mudada em ação de graças por
  Maria) e casa com Agostinho, *Sermão* 289, 2 (Eva e Maria): ficar com um dos dois no tema de Eva e Maria, se houver.
- **A soberba** (v. 5): Agostinho, *Civ.* XIV, 13 é o clássico; Leão (tomar em vez de merecer) e Tomás (decidir
  sozinho o bem e o mal) dizem coisas diferentes dele e entre si; Escrivá (modernos) e Bento XVI (Deus como
  concorrente) tocam Tomás. Se for preciso cortar, sai Tomás.
- **A conversa com a mulher** (vv. 1–4): Bernardo (Deus afirma, a mulher duvida) não repete Francisco de Sales
  (a serpente exagera a proibição); Ambrósio, *De paradiso* 12, 56 («nem o tocareis»: nada se acrescenta ao
  mandamento, nem por cautela; reserva, original pronto, `amb-par-56`) diz uma terceira coisa. Hugo, *De sacr.* I,
  7, 4, tem a tríade de Bernardo com uma frase a mais: «quem duvidou já se afastou de quem afirma e se aproximou de
  quem nega» (trocar Bernardo por Hugo, se o Gere preferir a ideia à imagem da serpente).
- **A tentação de Cristo** (1º domingo da Quaresma): Gregório, *Hom. in Ev.* 16, e Ambrósio, *In Lucam* IV, 7 (reserva,
  original pronto, `amb-luc-4-7`: Adão expulso do paraíso para o deserto, Cristo vai ao deserto buscá-lo e o leva de
  volta) se completam: o primeiro lê os vv. 5–6, o segundo o v. 24. Hugo, *De sacr.* I, 7, 6 e Boaventura repetem
  Gregório.
- **A morte como remédio** (v. 19): Nazianzeno, *Or.* 38, 12 (gregos) e Ambrósio, *De excessu* II, 37–38; Ambrósio
  é o único que tira a ideia da própria letra da sentença (o castigo é a terra maldita; a volta à terra, não).
  Ruperto III, 29 (v. 22, a árvore negada) é parente dos dois, mas sobre outro versículo; Ruperto III, 25 (reserva)
  repetiria Ambrósio.
- **As túnicas** (v. 21): Francisco, audiência de 22/04/2015 (a ternura de Deus) e Beda (a mortalidade, e a túnica
  devolvida ao pródigo) dizem coisas diferentes; ficam os dois.
- **O paraíso reaberto** (vv. 23–24): João da Cruz (as duas árvores) e Ambrósio, Sl 39 (o bom ladrão) se completam.
  Beda sobre a espada «versátil», removida no batismo (reserva), e Ruperto III, 32 dizem a mesma coisa que Ambrósio
  por outro caminho.
- **«Ó feliz culpa»**: o Exsultet (modernos) e Agostinho, *Sermão* 174, 2; Ambrósio, Sl 39 («Feliz queda») ecoa
  na frase do Exsultet, hino que a tradição atribuiu a ele; Tomás, III, q. 1, a. 3, ad 3 (reserva, original pronto, `tomas-3-1-3`)
  cita o Exsultet e diz o porquê (Rm 5,20). Se houver tema próprio no fim, Ambrósio vai para lá.
- **Eva, mãe dos viventes** (v. 20): Crisólogo, Sermão 74 (as mulheres da Páscoa); Epifânio (gregos) e o Catecismo
  494 dirão Maria, a nova Eva. Crisólogo diz outra coisa: o nome se cumpre na Páscoa.

## Dúvidas e escolhas

- **Termos**: segui o `PEDIDO.md`, mas as citações bíblicas dentro dos comentários seguem o texto que cada Padre leu:
  Ambrósio e Leão leem a Vetus Latina («a mais sábia», «És terra, e à terra irás»), Gregório e Bernardo a Vulgata
  («Sereis como deuses», «A mulher que me deste por companheira»). Em Bernardo, «Nequaquam moriemini» ficou «Certamente
  não morrereis», como no nosso v. 4.
- **Quem é quem**: em Máximo, «este… aquele» ficou «Adão… Pedro»; em Ambrósio, Sl 39, «a vontade dele» ficou «a vontade
  de Cristo»; em Ruperto, «Parcamus, inquam» é Ruperto falando por Deus (o «nós» é a Trindade, como no v. 22).
- **Tomás**: o excerto junta o fim do a. 1 e o meio do a. 2; tirei o «Sed» do começo da segunda peça na tradução.
- **Máximo de Turim, Homilia 53**: a numeração é a da PL 57 (Bruni); a edição crítica de Mutzenbecher (CCSL 23, com
  direitos) numera de outro modo, não conferido. Migne registra oito códices com o nome de Máximo.
- **Crisólogo, Sermão 74**: o excerto começa pelo Evangelho da Páscoa (Mt 28,1, que ele lê «Vespere sabbati»), não por
  Gn 3; a frase de Gn 3,20 vem no meio. Se o Gere achar que se afasta do versículo, a alternativa é o Sermão 64 (Marta:
  «seja enfim, por Deus, mãe dos viventes a que foi, pelo diabo, mãe dos mortos», PL 52, 380A).
- **Cipriano** (relevância 2): é o único latino sobre a sentença do homem (o trabalho e a fadiga); se sobrar espaço
  no tema, *Laborem exercens* 9 (modernos) diz o lado positivo.

## Para o `autores.json`

Todos os autores já estão lá. `autor_id` usados: `ambrosio`, `bernardo`, `tomas-de-aquino`, `gregorio-magno`,
`leao-magno`, `maximo-de-turim`, `cipriano`, `pedro-crisologo`, `beda`, `ruperto`.

## Para o catálogo `pesquisa/fontes/latinos.md`

- Corpus Thomisticum: a Suma está agrupada por blocos de questões, e o nome do arquivo é o da primeira questão do bloco
  (`sth3155.html` = II-II, q. 155–169; `sth1090.html` = I, q. 90–102); a lista está em `iopera.html`. `sth3163` dá
  «página não encontrada» (HTML de 3940 bytes, sem `<P TITLE`).
- Permalinks novos: Leão, Sermões `LeoI.Sermon9`; Bernardo, *De laudibus Virginis Matris* `BerCla.DeLaViM`; Ambrósio,
  *De excessu fratris* `AmbMed.DeExFrS`; Cipriano, *De bono patientiae* `CypCar.DeBoPa`; Beda, *Hexaemeron*
  `Beda.Hexaem2`; Máximo, Homilias `MaxTau.Homili3`.
- Ambrósio, *Explanatio* do Sl 39 (texto 6956): 19–20 sobre o bom ladrão e Adão, «Felix ruina» (PL 14, 1065).

## Para outros capítulos

- **Gn 2**: Ambrósio, *De paradiso* 12, 54 também lê 2,15 («escolhido para morar no paraíso»), mas o excerto é de 3,1.
- **Gn 4**: Ambrósio, *De paradiso* 14, 71 (PL 14, 310C): Caim nega o crime («Não sei; sou eu o guarda do meu irmão?»)
  e por isso não é castigado com os homens: o sacrilégio de pensar que se pode mentir a Deus. Bernardo, *De diversis*
  66, 3 (PL 183, 689B–C): o sétimo pecado, Caim contra Abel, «desde então ficou o costume de os maus se levantarem
  contra os bons». Zenão, Tratado I, 6, 3 (PL 11, 314B–C, já anotado em Gn 2). Ruperto, *In Gen.* IV, 2 (PL 167,
  326B–327B): Abel ofereceu primeiro o coração, Caim guardou o coração para si e ofereceu os frutos.
- **Gn 18**: Ruperto III, 25 (PL 167, 312C): «Falarei ao meu Senhor, eu que sou pó e cinza» (18,27), a lembrança do pó
  que abre a misericórdia.
- **Gn 27**: Ambrósio, *De paradiso* 14, 72 (PL 14, 311A–B): a «servidão» de Esaú ao irmão como bênção.
