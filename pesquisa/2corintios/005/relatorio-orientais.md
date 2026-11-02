# II Coríntios 5: relatório da pesquisa nos orientais (não gregos), ascetas e liturgia oriental

Pesquisa de 2026-11-02. Ponto de partida: `BASE.md`, `base/efrem-commentarii-2cor.md`, `base/macario-homilias-espirituais.md`,
`base/_pistas-orientais.md`, `base/_pistas-orientais-gregos.md`, `../proximos.md`, `../004/relatorio-orientais.md`.
Entregues **9 achados** em `achados-orientais.json` (trecho 1: 4; trecho 2: 3; trecho 3: 2) e três textos em `textos/`:
`efrem-commentarii-2cor-5.md` (corrigido na imagem), `afraates-demonstracoes-2cor-5.md`, `macario-homilias-2cor-5.md`.

**Resumo honesto**: o capítulo rende mais que o 4 nos orientais, por causa da ressurreição (5,1-5) e de 5,17 e 5,21.
Efrém comenta tudo, em glosas breves; os outros achados bons são dois de Afraates, dois de Macário. Nada de Jacó de
Sarug, dos armênios, dos coptas nem da hinografia que valha.

## O que se procurou

- **Efrém**, *Comentário* (latim de 1893): pp. 95–97, corrigidas **na imagem** (`page/n112`–`n114`).
- **Digital Syriac Corpus** (clone em `cache/genesis/orientais/sc/`): todas as 24 pistas de `base/_pistas-orientais.md`
  abertas no contexto, e busca própria por frases da Peshitta de 5,1-8 (ܒܢܝܢܐ ܕܡܢ ܐܠܗܐ, ܕܠܐ ܒܥܒܕ ܐܝܕܝܐ, ܬܬܒܠܥ ܡܝܬܘܬܗ ܒܚܝܐ,
  ܪܗܒܘܢܐ ܕܪܘܚܗ, ܘܠܐ ܒܚܙܝܐ, ܢܥܢܕ ܡܢ ܦܓܪܐ) e 5,14-21 (ܚܘܒܗ ܕܡܫܝܚܐ ܐܠܨ, ܒܪܝܬܐ ܚܕܬܐ, ܥܬܝܩܬܐ ܥܒܪ, ܬܫܡܫܬܐ ܕܬܪܥܘܬܐ,
  ܐܝܙܓܕܐ ܚܢܢ, ܚܛܝܬܐ ܥܒܕܗ). Ferramentas em `~/.cache/taioe-2cor-comum/orientais/` (`ctx.py`, `tei.py`, `orig.py`).
- **Afraates** (Dem. 1–23) e **Liber Graduum** (Memre 1–30), no corpus; latim de Parisot (PS I/1) para conferir.
- **Jacó de Sarug**: os 39 memre do corpus; o OCR siríaco de Bedjan I–V (`djvu.txt` e `hocr`) pelas mesmas frases.
- **Pseudo-Macário**, *50 Homilias* (grego do khazarzar, cópia `cache/genesis/orientais/dl/mac50.txt`): καινὴ κτίσις,
  ἀρραβών, καταποθῇ, ἀχειροποίητον, βῆμα, καταλλαγ-, πρεσβεύ-, ἡ ἀγάπη τοῦ Χριστοῦ συνέχει.
- **Hinografia bizantina** (AGES, 2 369 `.ares`): οἰκίαν ἀχειροποίητον, σκήνους, καινὴ κτίσις, τὰ ἀρχαῖα παρῆλθεν,
  βήματος τοῦ Χριστοῦ, καταλλάγητε.
- **Armênios**: Nerses Shnorhali, *Preces* (latim da poliglota de 1882, em cache); Gregório de Narek, *Lamentações*
  (grabar do Wikisource) por նոր արարած, անձեռագործ, ձեռագործ.
- **Padres do deserto**: *Paradise of the Fathers* (Budge, inglês do siríaco de Anan-Isho, 1907), índice e texto.

## O que se achou

| Autor, obra | Onde | Versículos | Situação |
|---|---|---|---|
| Santo Efrém, *Comentário* (armênio; latim de 1893) | p. 95 | 5,1-4 | achado (rel. 3): a casa nos céus é a glória que Adão perdeu |
| idem | p. 96 | 5,5-8 | achado (rel. 2): o corpo que foi morada do Espírito; Cristo conosco, mas escondido |
| idem | pp. 96–97 | 5,14-15 | achado (rel. 2): quem não morreu mártir morre para as paixões |
| idem | p. 97 | 5,16 | achado (rel. 2): porta fechada aos falsos cristos |
| idem | p. 97 | 5,18-21 | achado (rel. 2): embaixadores e intercessores; o «pecado» é a cruz na carne |
| Pseudo-Macário, *Hom.* 5, 9 | PG 34, 512–513 (aprox.) | 5,1-4 | achado (rel. 3): a casa é o Espírito; a primavera da ressurreição |
| Pseudo-Macário, *Hom.* 44, 1 | PG 34, 777–778 (aprox.) | 5,17 | achado (rel. 3): nova criatura, odres novos |
| Afraates, *Dem.* 6, 14 | corpus 6; PS I/1, c. 293–298 | 5,4-5.8 | achado (rel. 2): o Espírito do batismo à porta do cemitério |
| Afraates, *Dem.* 7, 1 | corpus 7 | 5,21 | achado (rel. 3): carregou o pecado que não cometeu e o pregou na cruz |
| Afraates, *Dem.* 8, 4–5 e 23 | corpus 8 | 5,4.8.10 | lido, fora: a «forma terrena absorvida pela celeste» (§ 5) e a objeção de 5,8 (§ 23) repetem a Dem. 6, 14, menos bem |
| *Liber Graduum*, Memra 15, 15 | corpus 202 | 5,8 | lido, fora: «quando sairmos do corpo, estaremos com o Senhor», até que os corpos «sejam absorvidos na luz dos seus espíritos»: mesmo pensamento de Afraates |
| *Liber Graduum*, Memra 16, 5 | corpus 203 | 5,21 | lido, fora: «o fez pecado» lido como humildade a imitar; Afraates 7, 1 é mais claro |
| *Liber Graduum*, Memra 20, 15 e 17 | corpus 207 | 5,8.17 | lido, fora: tomar a cruz para estar com o Senhor; «nova criatura» = o coração puro de Adão antes do pecado |
| *Liber Graduum*, Memra 24, 2 | corpus 211 | 5,20 | lido, fora: o selo do batismo fica até no servo mau; leitura em várias etapas, confusa fora da obra |
| Pseudo-Macário, *Hom.* 17 e 16 | khazarzar | 5,5 | lido, fora: o «penhor» (ἀρραβών) dá segurança de quem «já está coroado» (17); sem o penhor, a alma é retida ao sair do corpo (16, sombrio) |
| Liturgia bizantina, ectenia de toda Divina Liturgia | AGES `prayers` | 5,10 | anotado: «καλὴν ἀπολογίαν τὴν ἐπὶ τοῦ φοβεροῦ βήματος τοῦ Χριστοῦ αἰτησώμεθα» («peçamos uma boa defesa diante do tribunal temível de Cristo»): eco, não comentário; liturgia oriental não entra em nota |

**Traduções**: Efrém, do **latim** dos mequitaristas (o comentário só existe em armênio; o armênio não foi consultado);
Afraates, do siríaco (o latim de Parisot só para conferir); Macário, do grego de Dörries (khazarzar).

## Dúvidas (para a conversa principal)

- **Efrém 5,1-4**: «sicut domus Adae, quam perdidit» traduzido «como Adão, que perdeu a sua morada» (literal: «como a casa
  de Adão, que ele perdeu»).
- **Efrém 5,14**: «sicut Deus pro multis mortuus est» é a linguagem de Efrém (o Deus que morreu, ortodoxa: a pessoa é uma).
  «servati sunt a manifesta morte» = os que escaparam do martírio («poupados da morte visível»). Cortada a glosa de 5,13
  («se somos atormentados, isso alegra a divindade»), estranha fora da obra.
- **Efrém 5,16**: «si veniat, non novimus eum Christum» traduzido «se alguém vier assim, não o reconhecemos como Cristo»;
  a glosa seguinte confirma o sentido («não é possível que Cristo venha de novo na carne»).
- **Efrém 5,21**: «idest crucem fecit carnem ejus» = «fez da sua carne uma cruz» (literal). Pode ser lido «entregou a sua
  carne à cruz»; mantive o literal. Se parecer obscuro, cortar só essa glosa: o resto se sustenta.
- **Afraates, Dem. 6, 14**: Afraates pensa que, na morte, o Espírito recebido no batismo volta a Cristo e a alma «animal»
  fica sepultada com o corpo, sem sentidos, até a ressurreição (o «sono da alma», que a Igreja não ensina). Cortei a frase
  sobre a alma sepultada; ficou o Espírito que intercede pelo corpo e o reveste de glória (5,4-5). A frase «quando o
  Espírito vai para junto de Cristo» ainda supõe a ideia dele; se a conversa principal preferir, o excerto pode começar
  em «Quando chegar o tempo em que se cumpre o fim…». Plurais conferidos com os seyame do TEI («cemitério», «sepulcros»).
  Parisot traduz ܡܬܒܠܥ ܡܘܬܐ ܒܚܝܐ «mors absorbebitur a gloria»; o siríaco diz «pela vida» (= 2Cor 5,4).
- **Afraates, Dem. 7, 1**: ܙܟܝܐ traduzido «vencedor» (casa com «Eu venci o mundo», ܙܟܝܬܗ ܠܥܠܡܐ, Jo 16,33); pode ser também
  «inocente». Colunas de Parisot não conferidas.
- **Macário**: grego de Dörries; colunas da PG 34 aproximadas (conferir na PG antes de publicar, como nos caps. 3 e 4). Hom.
  5, 9: mantido o «primeiro mês, o Xântico, chamado abril» (no Oriente, a primavera); para o leitor do Brasil, abril é
  outono, mas a imagem das árvores depois do inverno já explica.

## Sobreposições com os outros grupos (para o enxugo)

- **5,1-4**: Efrém (a glória de Adão) e Macário (a casa é o Espírito; a primavera) não se repetem; ficam perto de
  Crisóstomo, hom. 10, e de Tertuliano/Metódio sobre a ressurreição da carne. Afraates 6, 14 fica perto de Macário (o
  Espírito que veste o corpo de glória): se só couber um, Macário é mais claro; Afraates tem o batismo e o 5,5.
- **5,17**: Macário 44 × Escrivá (*En diálogo con el Señor* 45) e os latinos: Macário é o mais concreto (mente, olhos,
  ouvidos, língua novos).
- **5,21**: Afraates 7, 1 diz em duas frases o que Agostinho e Ambrosiaster dizem com o *ḥaṭṭāʾt* (vítima pelo pecado):
  carregou o pecado sem tê-lo cometido. Efrém (a cruz na carne) é complemento.
- **5,20**: Efrém (embaixadores e intercessores) fica perto de Crisóstomo, hom. 11.

## O que não existe ou não se achou

- **Jacó de Sarug**: nada nos 39 memre do corpus; no OCR siríaco de Bedjan as frases não aparecem (o OCR é ruim demais
  para frases: dá para buscar palavras soltas, não sequências).
- **Efrém fora do comentário**: os hinos *Sobre o Paraíso* e *Sobre a ressurreição* não estão no corpus (só Nísibis e
  Natividade); nos *Carmina Nisibena* nada de 5,1-4. *Nisibena* 35 tem a Morte dizendo que o filho de Maria «criou uma
  nova criação para a humanidade»: não é 2Cor 5,17.
- **Armênios**: Shnorhali (*Preces*) e Narek, nada de 2Cor 5. **Coptas**: não procurados (sem edição antiga útil).
- **Hinografia**: em nenhum livro do AGES (Menaion, Triódio, Pentecostário, Octoeco, Eucológio, orações) aparecem οἰκίαν
  ἀχειροποίητον, σκήνους καταλυ-, καινὴ κτίσις ou τὰ ἀρχαῖα παρῆλθεν; o ofício dos mortos não foi conferido numa edição antiga.
- **Padres do deserto** (*Paradise*): nenhuma citação de 2Cor 5.

## Pistas não seguidas (fora da comunhão com Roma: só pista, nunca achado)

- **Isho`dad de Merv** (Gibson V, inglês, `commentariesofis0005isho_h2o7`, linhas 3821–3877): 5,1-4, o corpo «ginásio» que
  se desfaz e os santos vestidos de glória (já apontado em `../004/`); não lido nesta rodada.
- **Isaac de Nínive**, Discurso 18 (corpus 409, 5,16); **Narsai**, *Sobre a tentação de Cristo* (47) e *Sobre o filho
  pródigo* (60), 5,19; **Dionísio bar Salibi**, comentários a Jó (233), Salmos (238) e Ben Sira (258): não lidos.

## Para outros capítulos

- **2Cor 1,22** (o penhor): Pseudo-Macário, *Hom.* 17 (ἀρραβὼν τοῦ πνεύματος, «seguros pelo penhor, como já coroados»).
- **1Cor 15,44-53**: Afraates, *Dem.* 8, 4–5 e 6, 14 (corpo animal e espiritual; «a morte absorvida pela vida»).
