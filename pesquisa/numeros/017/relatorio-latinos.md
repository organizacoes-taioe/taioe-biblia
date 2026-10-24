# Números 17: relatório da pesquisa (Orígenes, Agostinho, Padres latinos e medievais latinos)

Pesquisa de 2026-10-24. Numeração da Nova Vulgata nos achados; os autores citam pela Vulgata (o nosso 17,1–15 = Nm 16,36–50; o nosso 17,16–28 = Nm 17,1–13).
Entregues: `achados-latinos.json` (25 achados: trecho 1 = 4, trecho 2 = 8, trecho 3 = 13) e os originais em `textos/`:
`origenes-hnum9-17.md`, `jeronimo-ep128-17.md`, `ambrosio-varios-17.md`, `gregorio-moralia-17.md`, `pedro-damiao-varios-17.md`,
`ivo-varios-17.md`, `bernardo-missus-est-17.md`, `pseudo-agostinho-sermo245-17.md`, `agostinho-varios-17.md`, `boaventura-tomas-varios-17.md`.

## Como se procurou

- Lidos `base/` (Orígenes hom. 9, Agostinho *Quaest.* IV, 30 e *Locutiones*, Bruno, Ruperto, Rábano, Isidoro, pseudo-Beda, Paterius, Lápide) e as seções «Para Nm 17» dos relatórios de Nm 16.
- **Orígenes, hom. 9, §§ 2–9**: o OCR do archive.org é ruim; os §§ 2–5 e 7–9 foram **transcritos das imagens** (GCS 30, pp. 56–67) em `textos/origenes-hnum9-17.md`. O § 1 já estava limpo em `../016/textos/origenes-varios-16.md`.
- **Corpus Corporum** (API `navigate.php` / `download.php`): baixadas e varridas as obras completas de Ambrósio (45 textos), Jerônimo (59), Gregório Magno (24, todas), Pedro Damião (59), Bernardo (61 de ~72), Ruperto (26), Gerhoh (18), Ivo, Herveu, Pascásio, Fulberto, Ildefonso, Leão, Fulgêncio, Cesário, Máximo de Turim e os pseudo-Agostinhos; **Agostinho só em parte** (59 textos: faltaram, entre outros, as *Enarrationes*, os *Sermones* autênticos e o *Contra adversarium legis*). Busca por «virga(m) Aaron», «inter mortuos/vivos/viventes», «thuribul-» e pelas notas «Num. XVI, 36–50 / XVII». O download dos outros ~55 autores da lista (Beda, Rábano, Hugo e Ricardo de São Vítor, Honório, Alano, Comestor, Lombardo, Hildegarda, Amadeu de Lausanne, Guerrico, Aelredo etc.) não terminou: **não varridos**.
- **Corpus Thomisticum**: *Super Hebr.* inteiro e *Summa* I-II, q. 98–105.
- **Boaventura**: OCR dos tomos V–IX de Quaracchi (archive.org `doctorisseraphicNNbona`); o trecho usado foi conferido nas imagens.
- **Lápide**: o trecho usado (p. 284) conferido na imagem.

## Os achados, em uma linha

Trecho 1: Orígenes 9,1 (nada é inútil para Deus); Agostinho IV, 30 (Eleazar e a sucessão; vale o nome do Senhor, não o mérito de quem ofereceu); Ivo, Ep. 155 (o sacramento permanece, como os turíbulos no altar); Bruno 16 (as lâminas, livro de quem não sabe ler; o altar do coração).
Trecho 2: Orígenes 9,2 (a glória só aparece na perseguição), 9,3–4 (dois justos bastam; amam os inimigos), 9,5 (Cristo com o turíbulo da carne); Ambrósio, Ep. 63, 50–51 e 56 (bom pastor que se oferece pelos que lhe resistiam); Jerônimo, Ep. 128, 4 (o fogo não ousou passar; «quem hoje?», depois do saque de Roma); Gregório, *Moralia* IX, 23 (os santos resistem à ira de Deus com a força que ele mesmo lhes dá); Pedro Damião, Ep. VIII, 12 (turíbulo da Paixão; os dois ladrões, primícias dos mortos e dos vivos); Boaventura, *In Sap.* 18 (Sb 18,20–25 relê o episódio).
Trecho 3: Orígenes 9,7 (a vara da cruz; a noz e os três sentidos), 9,8 (Deus dá mais do que promete); Ambrósio, Ep. 63, 58 (a graça sacerdotal nunca murcha; Israel há de reflorescer) e *De sacramentis* IV, 1 (o batistério onde a vara floresce; o povo sacerdotal); Gregório, *Moralia* XIV, 68 (as outras varas, nós, continuam secas) e VI, 18 (ninguém se admira da árvore que nasce todo dia); pseudo-Agostinho, Sermão 245, 3 (a vara sem raiz e a Virgem) e 5 (a noz: carne, cruz e divindade); Bernardo, *Missus est* 2, 5–6; Ruperto II, 4; Bruno 17 («não é pontífice aquele cuja vara não germina»); Agostinho, *Quaest.* II, 105 (vara = poder, maná = graça); Lápide (vv. 27–28: «que fazer para não morrer?», resposta em Nm 18).

## Achado e não usado (candidatos de reserva)

- Orígenes 9,9 (os quatro degraus do crente: confissão, graça, costumes, frutos que alimentam os outros; Cristo «vara» para os preguiçosos e «flor» para os justos), GCS 30, 66–67: muito bom, ficou de fora só pelo limite. Orígenes 9,3 (Moisés = a Lei, Aarão = a súplica) e 9,5 fim (o pontífice ficará outra vez «entre os vivos e os mortos» no Juízo).
- Ambrósio, *In Ps. 39 enarr.* 8 (PL 14, 1060C–D): Aarão «entre os vivos e os mortos» como Cristo «advogado» — «quid tam proprium Christi, quam advocatum… mortem suam offerre pro cunctis»; bom, mas repete Orígenes 9,5 e Pedro Damião. *De officiis* II, 4, 11 (PL 16, 106C: Aarão nunca mais feliz que então); Ep. 4, 4 (PL 16, 890A: «insigne sacerdotalis gratiae; aruerat ante, sed in Christo refloruit»); Ep. 41, 3 (PL 16, 1113C–D: a pregação do sacerdote, como a vara de Aarão, parece seca e um dia floresce); *De virginitate* 98 e *In Cant.*/*De Isaac* 64 (a vara de nogueira: graça sacerdotal «amarga nas tentações, dura nos trabalhos, frutuosa por dentro»); *De Jacob* II, 4, 19.
- Isidoro, *In Num.* 15, 16–19 (PL 83, 348A–C): Cristo «está entre os vivos e os mortos porque nasceu e morreu»; a vara = a carne de Cristo ressuscitada; «outros» dizem Maria. Fonte de Pedro Damião e do pseudo-Beda; não usado para não repetir.
- Paterius IV, 11 (PL 79, 765C), excerto de Gregório: «é ofício do sacerdote derramar a oração a Deus pelos justos, para que não caiam, e pelos pecadores, para que se levantem» (Sl 141,2). **A fonte gregoriana não foi achada** nas obras de Gregório do Corpus (nem *Moralia*, *Reg. past.*, *Hom.*, *In I Regum*, cartas). Paterius IV, 12 = *Moralia* XIV, 68 (usado direto).
- Pedro Damião, *Collectanea* in Ios. cap. V, excerto do **sermão sobre São Bartolomeu** (PL 145, 1073A–B): «Que exprime a vara de Aarão, senão o estandarte salvador do verdadeiro Pontífice e o sacramento da cruz vivificante? … prefigurou a santa cruz, que reverdece num verdor de memória imortal». Ótimo para o tema «vara = Cruz»; ficou de fora pelo limite (o tema já está em Orígenes 9,7 e no pseudo-Agostinho 245, 5). *De divina omnipotentia* (PL 145, 610D–611A): a vara cortada que dá amêndoas contra o silogismo dos filósofos.
- Ivo, Sermões (PL 162, 536B–C e 585C): a vara = Cristo, «sem nenhum humor vindo de fora», amargura da Paixão na casca, doçura no miolo; e o raio de sol que atravessa o cristal (como no pseudo-Agostinho 245, 4).
- Bernardo, Sermão no domingo dentro da oitava da Assunção, 7 (PL 183, 433C): a vara sacerdotal que floresceu sem raiz, figura de Maria (só menção).
- Gregório, *Hom. in Ez.* II, 4 (PL 76, 1033D–1034A): «como a vara seca de Aarão floresceu, como a Virgem, vinda da sua linhagem, concebeu» (lista).
- Herveu, *In Hebr.* 9 (PL 181, 1608C–1609A): a vara na arca = o poder sacerdotal de Cristo, que, cortado pela morte, «refloresceu mais vivo na manhã da ressurreição»; repete Gregório *Moralia* XIV e parece copiar Beda (*De tabernaculo*, não conferido). Também discute como a vara estava «na arca» (Hb 9,4) se 1Rs 8,9 diz que só havia as tábuas. *In Is.* 47 (PL 181, 444B) copia Gregório *Moralia* IX.
- Gerhoh, *In Ps.* (PL 193, 1440C) copia Gregório *Moralia* VI, 18; *In Ps.* 54 (1653D–1654A: Cristo com o «turíbulo da carne», já anotado em Nm 16).
- Tomás, *Summa* I-II, q. 102, a. 4, ad 6: a vara guardada na arca «para reprimir a dissensão do povo sobre o sacerdócio de Aarão»; e «convenientemente a dignidade sacerdotal era significada na arca pela vara e, fora, pelo altar do incenso, porque o sacerdote é mediador entre Deus e o povo: governa o povo pelo poder divino, que a vara significa, e oferece a Deus, como no altar do incenso, o fruto do seu governo, a santidade do povo». Bom para o v. 25; reserva (Agostinho II, 105 entrou). *Super Hebr.* 9, l. 1: «virga est sacerdotium eius aeternum».
- Boaventura, Sermão da Ressurreição (Quaracchi IX, 282, só OCR): «Se crês que a vara seca de Aarão floresceu na tenda, crê que a verdadeira carne do Senhor ressuscitou»; Sermão do 1º domingo do Advento, 7 (IX, 33): a vara que floresce «sem sucessão de tempo» (a concepção); sermão do Natal: a vara achada «na casa de Levi» porque Maria, da raiz de Jessé, era aparentada à linhagem sacerdotal; *Sermão 5 da Natividade de Maria* (IX, 717): a arca com a vara = a virtude da confiança em Maria; *Collationes* (t. V): a vara que floresce numa noite = o Espírito Santo, «amor fecundo». Comentário ao Eclesiastes 12,5 (t. VI): a amendoeira que floresce, os falsos prodígios do Anticristo.
- Agostinho, *Quaest.* V, 29 (PL 34, 761): a vara que floresceu e deu nozes entre os sinais divinos que significam algo da regra da fé (só menção).
- Lápide, cap. XVII: a amendoeira, «vigilante» (Jr 1,11), primeira a florescer e última a perder as folhas; o pastor deve ser vigilante, ágil, paciente e austero (com Nissa e exemplos de santos bispos); três milagres (botão, flor, fruto de uma vez); cita Ambrósio, Bernardo, Ruperto e o pseudo-Agostinho 245.

## O que não existe ou não se achou

- Agostinho não comenta Aarão «entre os mortos e os vivos» (confirmado no relatório de Nm 16; as *Enarrationes* não foram varridas desta vez).
- Jerônimo: além da Ep. 128 (usada) e da Ep. 78 (mansões, igual a Isidoro), só menções curtas: *In Is.* sobre Is 58,12 (PL 24, 573A: Símaco traduz «muro que se opõe a quem fere», «como foram Moisés, Aarão e Samuel, que resistiram à ira do Senhor e, como que levantando um muro, puseram termo à sua indignação») e *In Ier.* sobre Jr 7,16 (PL 24, 732B: «Aarão, tomando o turíbulo, ficou entre o fogo e o povo que ia arder»; as preces dos santos podem resistir à ira de Deus). O *In Ezech.* (Ez 13,5 e 22,30) **não foi baixado** desta vez: conferir a pista do relatório de Nm 16 (PL 25, 110A).
- Gregório, *Regula pastoralis*: nenhuma citação de Nm 16,46–48 Vg (a frase de Paterius IV, 11 não está lá).
- O pseudo-Agostinho «Sermo 31 de Scripturis» («De virga Aaron», PL 39, 1805–1807) é só uma cópia resumida de Orígenes, hom. 9, §§ 7–9: não usar como texto próprio.
- Cipriano, Hilário, Optato: nada de novo para Nm 17 além do anotado em Nm 16 (Hilário, *In Ps.* 68, 22, eco de 16,38 LXX).

## Pistas para outros capítulos

### Para Nm 18
- Lápide sobre 17,12–13 Vg já faz a ponte: Deus responde ao medo do povo dando Aarão como intercessor e mandando sustentá-lo com dízimos e primícias.
- Agostinho, *Quaest.* IV, 31 (PL 34, 731–732), sobre Nm 18,1: «levareis os pecados dos santos» = os sacrifícios pelo pecado.
- Ambrósio, *In Ps. 118* (PL 15, 1295C–D) e o *In Cant.* compilado (PL 15, 1889C–D), sobre Nm 18,20 («Eu sou a tua parte»): quem tem Deus por parte possui toda a natureza. Pedro Damião, *Contra clericos regulares proprietarios* 1 e 4 (PL 145, 482D–487C), sobre Nm 18,20: os cônegos não devem ter propriedade. Ambrósio, *De Cain et Abel* I, 7 (PL 14, 342C), sobre as primícias (Nm 18). Jerônimo, *De perpetua virginitate* (PL 23, 192C), sobre Nm 18,15–16 (primogênito). Tomás, *Summa* II-II, q. 86–87 (dízimos, Nm 18).
### Para Nm 20
- Lápide: a rocha foi ferida pela vara de Aarão (Nm 20,8–9). Herveu e Gregório *Hom. in Ez.* II: a vara que divide o mar e tira água da pedra.
### Para Nm 21 (serpente de bronze)
- Pedro Damião, Ep. VIII, 12 (PL 144, 487A–B, logo antes do turíbulo): a vara mudada em serpente = Cristo na morte. Orígenes, *Selecta in Num.* 16,37: os turíbulos no altar «como a serpente de bronze», sinal da incredulidade.
