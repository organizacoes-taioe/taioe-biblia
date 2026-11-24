# Dt 13: relatório (dt13-14, 23/11/2026)

12 achados em `achados-todos.json`: Agostinho 2, Vicente de Lérins 2, Cirilo de Alexandria 2; Cassiano, Bruno de Segni, Ruperto, Rábano, Teodoreto, Tomás 1 cada. Acima da meta mínima (12), mas **só o trecho 1 está bem coberto** (10); trecho 2 (vv. 7–12) e trecho 3 (vv. 13–19) têm 1 cada: quase ninguém, nos textos que o corpus alcança, comenta o irmão/amigo que seduz nem a cidade apóstata sem defender a pena de morte.

## O que entrou (uma linha cada)

Trecho 1 (vv. 1–6):
- `vicente-lerins-commonit-10-deus-permite-mestre-novo`: *Commonitorium* I, 10, o comentário por extenso de Dt 13,1-3: o mestre amado que traz doutrina nova é a prova de Deus. Melhor candidato.
- `vicente-lerins-commonit-19-20-o-verdadeiro-catolico`: I, 19–20, a conclusão «pelas leis do Deuteronômio» e o retrato do verdadeiro católico.
- `cassiano-coll-15-1-2-sinais-nao-provam-santidade`: Coll. XV, 1–2: curas e sinais podem ser simulados ou vir de pecadores; Dt 13,1-3 e Mt 24,24.
- `agostinho-in-io-43-5-6-deus-tenta-para-que-saibais`: duas tentações, a que engana e a que prova; «para saber» = «para que saibais».
- `agostinho-qhept-5-19-tentar-e-fazer-saber`: QH V, 19: comentário direto a Dt 13,1.3 (LXX), com a leitura dos adivinhos.
- `tomas-st-1-114-2-tentar-para-que-saibam`: *ST* I q. 114 a. 2: tentar para saber, para ajudar, para prejudicar; Dt 13,3.
- `ruperto-in-io-4-como-provar-o-profeta`: Dt 13 não contradiz Dt 18: como julgar um profeta (nome de que deus, e cumprimento da palavra).
- `rabano-in-dt-2-5-todo-o-capitulo-contra-a-idolatria`: o capítulo inteiro é contra a idolatria e a heresia; Mt 5,29-30.
- `teodoreto-quaest-dt-12-os-sinais-do-falso-profeta`: *Quaest. in Deut.* 12: o prodígio é permitido por Deus, como o dos magos do Faraó; julga-se o ensino, não o sinal.
- `cirilo-hom-pasc-14-deus-permite-que-o-adivinho-acerte`: *Hom. pasc.* 14 (PG 77, 724): Deus deixa até o adivinho dizer algo verdadeiro, como prova.

Trecho 2 (vv. 7–12):
- `cirilo-in-io-dt-13-lei-sobre-um-ponto-aplicada-a-tudo`: *In Ioh.* (sobre Jo 9,13): cita Dt 13,7-9 por inteiro e nota que os judeus aplicaram sem juízo a toda falta o que valia para um caso.

Trecho 3 (vv. 13–19):
- `bruno-segni-in-dt-13-cidade-espada-do-espirito`: leitura espiritual da cidade que se destrói: a heresia, e a «espada do espírito» é a palavra de Deus; nada do erro deve ficar preso à própria fé. Útil por não defender a violência.

## Como se procurou

- Busca de texto completo do Corpus Corporum (`mlat.uzh.ch/php_modules/fulltext_search.php`, script `~/.cache/taioe-dt10-14/dt13-14/sr.py`) por frases de Dt 13 em latim (vv. 2–4, 7, 9, 10; v. 1 «nec addas quidquam»): achou Vicente, Cassiano (Coll. II/XV e XIII), Agostinho, Rábano (*De magicis artibus*, *Enarratio*), Ruperto, Tomás. Textos baixados em `PRINC/pesquisa/cache/deuteronomio/dt13-14/` (`cc_<idno>.txt`).
- Busca por frase no corpus grego já convertido (`~/.cache/taioe-dt1/gregos/busca.py`): Cirilo (*De adoratione*, *Hom. pasc.*, *In Ioh.*), Orígenes (*C. Cels.* II, 53), Teodoreto (Q. 12). O texto do Teodoreto vem do PDF com camada de texto (não é OCR), com palavras partidas pela quebra de linha; juntei à mão as partidas.
- Cache da pré-pesquisa do Dt 1–9 (Rábano, Anselmo de Laon, Agostinho QH, Bruno de Segni baixado de novo) e `sth1103.html` do Corpus Thomisticum.

## Quem não comenta ou não serviu

- Orígenes, *C. Cels.* II, 53–55: usa Dt 13 contra o judeu de Celso, é argumento *tu quoque*, não ajuda a entender o versículo.
- **Cirilo, *De adoratione* (PG 68, 420–421)**, sobre Dt 13,2-6: o comentário é só que a lei é santa porque quem mata a alma merece mais a morte que quem mata o corpo. **Deixei de fora**: defende a pena. Disponível se o Gere quiser.
- **Cassiano, Coll. XIII, 14** (Dt 13,1-3 sobre a tentação e a liberdade): deixei de fora; a Conferência XIII é a que Próspero criticou (graça e livre-arbítrio).
- Bernardo, *Ep.* 363, 3 («tentat vos Dominus Deus vester»): trata da Segunda Cruzada, não de Dt 13.
- Anselmo de Laon (Glosa ordinária), Beda/pseudo-Beda, Alcuíno, Gerhoh, João de Salisbúria: só repetem Agostinho ou citam sem comentar.
- Sem achado para os vv. 7–12 (parentes) e 13–19 (cidade), além dos dois acima: nenhum Padre latino ou grego do corpus os comenta fora de Mt 10,37.

## Autores novos (não estão em `ferramentas/autores.json`)

- **São Vicente de Lérins** (`vicente-de-lerins`), «† antes de 450», «monge de Lérins, autor do *Commonitorium* (434)»; **não oriental**. Sobre (sugestão): monge na ilha de Lérins, na Gália, autor do *Commonitório*, onde descreve a regra de fé: o que se creu em todo lugar, sempre e por todos.

Os outros autores já existem no cadastro (São João Cassiano, Santo Agostinho, São Tomás de Aquino, Ruperto de Deutz, Rábano Mauro, São Bruno de Segni, Teodoreto de Ciro, São Cirilo de Alexandria).

## Para outros capítulos

- Dt 8,2: Agostinho, QH V, 13 («Hic apertius dictum est, quod alibi...»): cita Dt 13,3 de passagem; Dt 8 já tem os seus.
- Dt 12,29-31 e Dt 13: Cirilo, *Hom. pasc.* 13 (PG 77, 677–680), e *De adoratione* (PG 68, 420), «Εὖ γε ὁ νομοθέτης ἀποφάσκει παντελῶς τῶν πλανωμένων τὴν μίμησιν» (os filhos queimados): serve ao pesquisador de Dt 12.
- Dt 18,9-13 (adivinhos): Cirilo, *Hom. pasc.* 14 (PG 77, 724: «οὐ μαθήσῃ ποιεῖν κατὰ τὰ βδελύγματα»), o parágrafo anterior ao usado aqui.
- Dt 12, 23–25 (o sangue): Teodoreto, Q. 11 (aparece logo antes da Q. 12).

## Cuidados e limites

- O `original` é cortado do texto baixado, não reescrito; tirei números de nota e de página, e uma nota editorial `[ Lips. in marg. auditu]` do Cassiano. Mantive as grafias da fonte (ex.: «tuî», «vestrâ» em Vicente; «του» em vez de «τοῦ» em Cirilo, *Hom. pasc.*).
- A numeração de Dt segue a Vulgata e a LXX nos Padres: o «Dt 13,1» de Agostinho (QH V, 19) é o nosso 13,2; Tomás escreve «Deut. XII» por Dt 13,3.
- Edições de página (PL 50, 650–651; PL 49, 992–993; PL 108, 881; PL 169, 384; PG 68, 420–421; PG 77, 724) tiradas dos marcadores de página dos textos; PL 35 do Agostinho (*In Ioh.* 43) sem coluna conferida.
