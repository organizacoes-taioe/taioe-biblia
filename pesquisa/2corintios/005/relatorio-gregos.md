# II Coríntios 5: relatório da pesquisa nos Padres gregos

Pesquisa de 2026-11-02. Resultado: **18 achados** em `achados-gregos.json` (13 com relevância 3, 5 com 2; 16 em domínio
público, 2 em citação curta). Todos em grego (Irineu pelo fragmento grego dos *Sacra Parallela*, que o latim confirma).

| trecho | achados | autores |
|---|---|---|
| 1 (vv. 1–10, «A morada eterna nos céus») | 6 | Metódio (5,1), Crisóstomo 3 (*Ressurreição dos mortos* 6 e 8; hom. 10, 2), Irineu (V, 13, 3), Teodoreto (5,10) |
| 2 (vv. 11–17, «O amor de Cristo nos constrange») | 8 | Gregório de Nissa (*Cântico* 10), Teofilato (5,13), Crisóstomo 3 (hom. 11, 1; 11, 2; *Catequese* 4), Teodoreto (5,14), Basílio (*Regras breves* 172), Nazianzeno (Or. 38) |
| 3 (vv. 18–21, «O ministério da reconciliação») | 4 | Crisóstomo 2 (hom. 11, 2–3; 11, 3), Cirilo de Alexandria (5,21), Nazianzeno (Or. 37) |

Por versículo: 1 (Metódio), 2-4 (Crisóstomo), 4-5 (Irineu), 5 (Crisóstomo), 6-8 (Crisóstomo), 10 (Teodoreto), 13 (Nissa,
Teofilato), 14-15 (Crisóstomo, Teodoreto, Basílio), 16 (Crisóstomo), 17 (Crisóstomo, Nazianzeno), 19-20 (Crisóstomo), 21 (Cirilo,
Crisóstomo, Nazianzeno). Nada escolhido para os vv. 9, 11-12 e 18 (só paráfrases do que já está nos outros).

Textos novos em `textos/`: `crisostomo-ressurreicao-dos-mortos-2cor-5.md` (§§ 6–8, PG 50, 426–432), `irineu-adversus-haereses-2cor-5.md`
(Harvey, grego e latim), `basilio-regras-breves-2cor-5.md` (172 e 215), `nazianzeno-discursos-37-38-2cor-5.md`,
`atanasio-contra-arianos-2cor-5.md` (reservas) e `gregos-citacoes-curtas-2cor-5.md` (Nissa, *Catequese* 4, Simeão: só o trecho).

## Onde se procurou

- **Pré-pesquisa** (`base/`): Crisóstomo hom. 10–11, Teodoreto, Cirilo, Cramer, Teofilato, Ecumênio, Damasceno, lidos inteiros (Teofilato
  e Ecumênio sobretudo pelo latim de Migne); Macário (hom. 5) lido, deixado ao grupo orientais.
- **Busca em massa** (sem acentos) por 20 frases de 2Cor 5 em 475 textos do khazarzar baixados agora e convertidos com
  `gregos-limpar.py` (Crisóstomo 142 obras escolhidas, Nazianzeno 64, Nissa 79, Basílio 32, Atanásio 15, Cirilo de Jerusalém 12, Máximo,
  Simeão, Palamas, Irineu) e nos caches do Gênesis e de Números 19–20 (Orígenes, Epifânio, Dídimo, Eusébio, Teodoreto). Scripts e textos em
  `~/.cache/taioe-2cor-comum/gregos5/` (`baixar.sh`, `par.sh`, `um.sh`, `busca.py`, `montar.py`, `textos.py`; `txt/`, 89 MB).
  O caminho antigo dos ~1 300 textos convertidos (scratchpads de outras conversas) não existe mais: tudo foi baixado de novo.
- **Fora dos caches**: Irineu, ed. Harvey II (archive.org); imagens da PG 82, cols. 407–412 (Teodoreto) e de Cramer V, p. 379 (Metódio),
  pelo `page/n<folha>` do archive.org (folhas achadas pelo `hocr_pageindex`).

## O que se achou

| Autor, obra | Onde | Situação |
|---|---|---|
| **Crisóstomo, *Hom. 2 Cor* 10–11** | PG 61, 465–480 | 5 achados: 5,6-8 (troca dos nomes: a morte é «morar junto do Senhor», a vida daqui é exílio); 5,14-15 (se um morreu por todos, todos estavam mortos; a dívida tripla); 5,16 (Cristo não deixou a carne: «segundo a carne» = fome, sede, cansaço); 5,19-20 («quem foi ofendido? Ele. Quem veio primeiro? Ele»; «reconciliai-vos», não «reconciliai Deus»: Deus nunca é inimigo); 5,21 (não «pecador», mas «pecado»; não «justos», mas «justiça de Deus»). Reservas: 10, 2–3 (5,9-10: o mesmo corpo que serviu é coroado ou castigado, contra «outro corpo»; «imaginemos o tribunal agora presente»); 11, 2 (5,17: a lista do novo, «em vez da Jerusalém de baixo, a de cima; em vez da circuncisão, o batismo; em vez do maná, o corpo do Senhor…»); 11, 1 (5,13: o êxtase = falar de si coisas grandes). A exortação da hom. 11 (PG 61, 479–480: quem ama Cristo prefere o castigo a tê-lo ofendido) não entrou. |
| **Crisóstomo, *Sobre a ressurreição dos mortos*** | PG 50, 426–432 | **2 achados** (a pista dava PG 50, 423–426: o comentário a 5,1-5 está nos §§ 6–8, cols. 426–432): «uma coisa é o corpo, outra a corrupção» (5,2-4); o penhor é parte do todo, e está hoje no batismo, no perdão, na Eucaristia e no sacerdócio (5,5). Reserva: § 7 (a semente que apodrece, o ouro no crisol). |
| **Crisóstomo, *Catequeses batismais*** (série de Stavronikita) | Cat. 4, 12–14 (ed. Wenger, SC 50) | 1 achado em citação curta (5,17): aos recém-batizados, «que proveito haveria em ver um céu novo…»; a graça muda a vontade, não a natureza. **Achado novo**: a catequese 4 inteira é sobre 5,17. |
| Crisóstomo, outras obras | *A Teodoro caído* I (5,19-20); *Hom. Rom.* 5 (5,20) e 12 (5,15); *Hom. Hb.* 28 (5,21, de passagem); *Habentes eundem spiritum* hom. 1 (5,1 só como leitura do dia); *Eutrópio preso* (5,5, o anel do noivo; duvidoso); *In illud «Si qua in Christo nova creatura»* (PG 64, 25: espúrio) | só usos. Reserva: *A Teodoro caído* I (ed. moderna, SC 117: citação curta): «nenhum amante arde tanto pela amada como Deus deseja a nossa salvação»; «reconciliai-vos» dito ao cristão que caiu: «não só a incredulidade, também a vida impura cria essa inimizade». Boa para um tema da penitência, se houver. |
| **Santo Irineu, *Contra as heresias* V, 13, 3** | PG 7, 1158–1159; Harvey II, 357–358 | 1 achado (5,4-5): «isto ele diz da carne: nem a alma é mortal, nem o Espírito»; a carne viva e incorruptível «cantando a Deus». |
| **São Metódio, *Sobre a ressurreição*** | fragmento na catena de Cramer, V, 379 (imagem conferida; a atribuição vem no fim do trecho, «οὕτως ὁ ἐν ἁγίοις Μεθόδιος ἐν τῷ περὶ ἀναστάσεως λόγῳ») | 1 achado (5,1): a vida daqui se sustenta pelas mãos (pão, bebida, roupa); por isso a eterna é «não feita por mãos». O *Panarion* 64 de Epifânio, que guarda longos trechos do *De resurrectione*, não cita 2Cor 5. Teofilato repete a mesma explicação sem nome («nonnulli…»). |
| **Teodoreto, *Interpretação*** | PG 82, 407–412 (imagem conferida, cols. 408, 409 e 412) | 2 achados: 5,10 («não disse comparecer, mas ser manifestados»: curar agora as feridas do pecado); 5,14 («estamos incendiados pelo amor de Cristo»). Reservas: 5,4 («como a luz que nasce faz sumir as trevas, a vida indestrutível faz desaparecer a corrupção», col. 408); 5,5 (o Criador, prevendo a queda de Adão, preparou o remédio); 5,13 (σωφροσύνη = humildade; êxtase = narrar os próprios feitos); 5,17 (no batismo despimos a velhice do pecado, col. 412); 5,21 («chamado o que nós éramos, nos chamou o que ele era», col. 412: a «troca admirável», deixada de fora porque Crisóstomo diz o mesmo mais largo). |
| Teodoreto, *História religiosa* 31, 8 | SC 257 | reserva (citação curta): Paulo prefere o castigo com o amor ao Reino sem ele; cita 5,21 e 5,14-15: «os que já não vivem para si aceitam com alegria fazer e sofrer tudo por ele». Teodoreto já tem dois achados. |
| **São Cirilo de Alexandria, fragmentos** | Pusey III, 350–356 | 1 achado (5,21): «pecado» = sacrifício pelo pecado da Lei de Moisés, com Os 4,8 («comerão os pecados do meu povo»); é a leitura que o pedido procurava (*ḥaṭṭāʾt*). Reservas: 5,1-4 (o mortal «absorvido» não é aniquilado, é transformado em incorrupção, como no princípio o sopro de vida em Gn 2,7); 5,16 (Cristo «acima da carne», Rm 6,9); 5,19 («em Cristo» = «na pessoa de Cristo»; os apóstolos falam «tomando o rosto de Cristo», útil para o sacerdote e a absolvição). Ecumênio, na catena de Cramer, cita a leitura «pecado = vítima» como de «outros». |
| **São Basílio, *Regras breves* 172** | PG 31, 1196–1197 | **Achado novo** (5,14-15): a disposição para receber o corpo e o sangue de Cristo é a de 2Cor 5,14-15. Reserva: *Regras breves* 215 (PG 31, 1225): o «pacificador» de Mt 5,9 é quem coopera com o Senhor, segundo 5,20. *Sobre o Espírito Santo* 15, 36 (o penhor, Catecismo 736) **já foi usado em 2Cor 1** (`conteudo/2corintios/001.json`, tema «penhor»): não repetido. |
| **São Gregório de Nissa, *Cântico* 10** | GNO VI, 308–309 (PG 44, 989–992) | 1 achado em citação curta (5,13): a «sóbria embriaguez»; Paulo, «o Benjamim mais novo» (alusão ao Sl 67,28 LXX, «Benjamim, o mais novo, em êxtase»), fora de si para Deus e em seu juízo para Festo (At 26,25). Outras: *Sobre os mortos* (GNO IX; 5,1: «ninguém desenhe a forma daquela casa não feita por mãos»; ama o teu corpo purificado, não a escória) — reserva, citação curta; *Contra Eunômio* III (5,21: «pecado» = a carne; leitura isolada, não serve ao leitor); *Sobre o tríduo* (5,4, de passagem); *Diálogo sobre a alma e a ressurreição* (a «Festa das Tendas» da morada desfeita e refeita, sem citar 2Cor 5: alegórico). |
| **São Gregório Nazianzeno** | Or. 37, 1 (PG 36, 284); Or. 38, 1–2 (PG 36, 312–313) | 2 achados: 5,21 (Or. 37: «é chamado o próprio pecado e a própria maldição: não é, mas é chamado assim», por humildade); 5,17 (Or. 38, Natal: «a letra recua, o espírito avança; as sombras passam, a verdade chega»). Reservas: Or. 30, 5 (5,21 com Gl 3,13: faz sua a nossa insubmissão, como cabeça do corpo; texto do khazarzar segue edição moderna); Or. 45, 1 (Páscoa: «se alguém está em Cristo, é nova criatura: renovai-vos»). |
| **Teofilato** | PG 124, 853–854 | 1 achado (5,13): «Paulo estava louco da loucura do amor… já não vivia a sua vida, mas a do Amado» (eco de Dionísio, *Nomes divinos* 4, 13). Relevância 2: se for preciso só um no v. 13, fica Nissa. |
| Santo Atanásio | *Contra os arianos* II, 47 (PG 26, 248) e II, 65 (PG 26, 285); *Sobre a encarnação* 10 (5,14-15 citado como prova) | reservas em `textos/`: II, 47 (não «se tornou» pecado e maldição «inteiro», mas tomou sobre si a maldição e os pecados: Is 53, 1Pd 2,24) — diz o mesmo que Cirilo e Nazianzeno; II, 65 (a nova criação precisava de um primeiro, que não podia ser um homem só terreno: é Cristo). *Carta a Epicteto* 8 usa Gl 3,13, não 2Cor 5,21. |
| São Simeão, o Novo Teólogo | *Discurso ético* 5 (SC 129) | reserva (citação curta, em `textos/`): «que coisas se fizeram novas? O céu? A terra? Não: mortos, ressuscitamos para a vida…», e isso «conscientemente», já no corpo. Repete o que a *Catequese* 4 de Crisóstomo diz melhor. Os *Capítulos* não comentam 5,14 de modo próprio (só citam em lista de virtudes). |
| São Máximo | *Capítulos teológicos* II, 61 (PG 90, 1152); *Capítulos sobre a caridade* IV, 77 | 5,16 aplicado à leitura da Escritura (da letra ao espírito, do Verbo «na carne» das palavras ao Verbo puro); 5,5 numa frase. Alegóricos: não entraram. |
| Orígenes (escritor eclesiástico) | *Contra Celso* V, 19; VII, 32 e 50 | 5,1-4 e 5,6-8 contra Celso, com a teoria da «veste» do corpo que muda de lugar para lugar (o córion do feto): especulativo, não entrou. |
| Damasceno, Ecumênio, Cramer | `base/` | resumem Crisóstomo e Teodoreto. Cramer traz ainda Clemente de Alexandria, *Hipotiposes* IV, sobre 5,16 (Cristo «segundo a carne» = sujeito às paixões naturais), igual a Crisóstomo. |

## O que não existe ou não se achou

- **Basílio, *Sobre o Espírito Santo* 15, 36**: já usado em 2Cor 1 (penhor de 1,22). Não há outro comentário de Basílio a 5,5.
- **Gregório de Nissa sobre a túnica de pele e 5,1-4**: o *Diálogo sobre a alma e a ressurreição* não cita 2Cor 5,1-4 (as «túnicas de pele» estão
  ali sem ligação com a tenda de Paulo). Sobre 5,21, só a leitura isolada do *Contra Eunômio*.
- **São Cirilo de Jerusalém**: as *Catequeses* só citam 5,5 junto com 1,22 (Cat. 17; e Cat. 1, «adquiri o penhor do Espírito Santo pela fé»),
  sem comentário próprio. Nada sobre os outros versículos.
- **Metódio**: não está no khazarzar; o *De resurrectione* só em Bonwetsch (GCS 27, 1917) e nos trechos do *Panarion* 64, que não citam 2Cor 5.
  O fragmento usado é o da catena de Cramer (1844, domínio público).
- **Gregório Palamas**: os dois tomos do khazarzar só citam 5,5 dentro de uma citação de Macário, e 5,20 em sentido comum («πρεσβεύομεν» = «sustentamos»); sem achado.
- **Penitência e 5,20 nos gregos**: nenhum Padre grego do corpus liga «embaixadores de Cristo» ao sacramento da penitência; o mais próximo é
  *A Teodoro caído* I (reserva) e Cirilo, «tomando o rosto de Cristo» (reserva). A fórmula da absolvição fica com o grupo da liturgia.
- **Teodoro de Mopsuéstia**: excluído, não lido.

## Dúvidas para conferir antes de publicar

- **Teofilato**: coluna lida do cabeçalho do OCR («859 / 854»; pela sequência, PG 124, 853–854). O OCR traz «ἵνα ἡμᾶς αὐτῷ παραστήσωμεν»; o latim de
  Migne («ut vos ad ipsum perducamus») e o sentido pedem ὑμᾶς, que adotei. A última oração do trecho grego («ὡς σφόδρα ἐρωτικὴν ἤτοι
  ἀγαπητήν») ficou fora: o OCR está estragado e o latim não ajuda.
- **Teodoreto, 5,14**: a PG traz no texto «ἵνα Πνεῦμα ἡμῖν τὴν ζωὴν πραγματεύσηται»; a nota 88 de Migne dá, do códice B, «πᾶσιν ἡμῖν» (sem
  «Πνεῦμα»), «que parece a lição melhor»; adotei «πᾶσιν ἡμῖν».
- **Irineu**: o khazarzar dá «φανερώτατα περὶ τοῦ Πνεύματος λέγων τοῦτο», que contradiz a frase seguinte; Harvey (grego dos *Sacra Parallela*) e
  o latim («manifestissime hoc de carne dicens») dão «περὶ τῆς σαρκός»: adotado. Harvey omite o artigo em «ἀῤῥαβῶνα».
- **Crisóstomo, hom. 11, 1**: ele lê «ἡ ἀγάπη τοῦ Θεοῦ» (5,14), e a tradução segue («o amor de Deus»). Em 5,4 (hom. 10) lê «τὸ φθαρτόν».
- **Crisóstomo, *Catequese* 4**: o texto do khazarzar segue Wenger (SC 50, 1957), edição com direitos: o `original` tem só duas frases e o lema.
  Numeração «Cat. 4, 12–14» pelos marcadores do PDF.
- **Nissa, *Cântico* 10**: o khazarzar segue a GNO (Langerbeck); coluna da PG 44 aproximada (989–992), não conferida na imagem. Na tradução,
  «o Benjamim mais novo» é a alusão de Nissa ao Sl 67,28 LXX; se o Gere achar obscuro, pode virar «Paulo, da tribo de Benjamim».
- **Metódio**: «São Metódio de Olimpo, bispo e mártir (†c. 311)»; o fragmento só existe na catena (não verificado em Bonwetsch). A frase
  omitida ([…]) é a distinção «uma coisa é a casa, outra a tenda, outra nós», que confunde fora do contexto.
- **Colunas da PG 50** (Crisóstomo, *Ressurreição*): pelos marcadores do khazarzar ([PG 50, 427] no meio do § 6, [PG 50, 432] no § 8).
- Crisóstomo ficou com 8 dos 18. Se for preciso enxugar: hom. 10, 2 (5,6-8) e *Ressurreição* 8 (5,5) são os mais dispensáveis do ponto de vista
  do grupo; a hom. 11, 2–3 (5,19-20) e Cirilo (5,21) são os que eu mais manteria.
- **Cruzamentos com outros grupos**: Macário, hom. 5 (5,1-4, a primavera da ressurreição) é do grupo orientais; o «pecado = sacrifício» deve
  aparecer em Agostinho e Ambrosiaster (latinos) — Cirilo é o melhor grego; a «loucura do amor» de 5,13 deve estar em Tomás e nos místicos;
  «caritas Christi urget nos» em Escrivá (modernos). Clemente de Alexandria sobre 5,16 (em Cramer) é igual a Crisóstomo.

## Pistas não seguidas

- Dídimo, Severiano, Ecumênio (glosas) e Fócio sobre 2Cor 5 (Staab, edição moderna; o cache de Números 20 tem
  `Didymus__Fragmenta in epistulam ii ad Corinthios.txt` com 5,1-4): não lidos.
- Cirilo de Alexandria, *Comentário a João* (5,14, 5,17, 5,19-20 e 5,5 aparecem várias vezes, cache do Gênesis) e *Glafira* (5,16-17): não lidos
  um a um. Os PDFs de Cirilo e de Orígenes do khazarzar não chegaram a ser baixados (download interrompido).
- Eusébio, *Demonstração evangélica* e *Comentário aos Salmos* (5,21 e 5,16, cache de Números 20): escritor eclesiástico; não lidos.
- Crisóstomo: *Hom. Jo.* (5,10, quatro vezes) e *Hom. Gên.* não lidos em detalhe; a pasta inteira (398 PDFs) não foi baixada, só 142 obras
  escolhidas (homilias sobre Paulo, Mateus, João, Gênesis, penitência, ressurreição, catequeses e avulsas).

## Para outros capítulos

- **2Cor 6,1-2** («eis agora o tempo favorável»): Teodoreto, PG 82, 412 (logo depois de 5,21, imagem já conferida).
- **2Cor 6,16** e 5,1: Nissa, *Diálogo sobre a alma e a ressurreição* (a Festa das Tendas, PG 46): alegórico.
- **2Cor 12,2-4** (o arrebatamento): Nissa, *Cântico* 10 (a sóbria embriaguez, junto de 5,13) e Teofilato, PG 124, 853 (Dionísio, *Nomes
  divinos* 4, 13).
- **2Cor 8,9** («sendo rico, se fez pobre»): Teodoreto, *História religiosa* 31, 8, junto de 5,21.
