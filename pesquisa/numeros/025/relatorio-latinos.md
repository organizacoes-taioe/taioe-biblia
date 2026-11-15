# Números 25: relatório da pesquisa (Orígenes/Rufino, Agostinho, Padres latinos e medievais latinos)

Pesquisa de 2026-11-15. Hebraico, Nova Vulgata, Vulgata e LXX coincidem nos 18 versículos usados (o v. 19 hebraico é o 26,1).
Entregues: `achados-latinos.json` (13 achados: trecho 1 = 5, trecho 2 = 7, trecho 3 = 1) e, em `textos/`, os originais que não estão em `base/`:
`origenes-hom-num-20-25.md` (transcrito das imagens do GCS 30), `ambrosio-varios-25.md`, `jeronimo-in-osee-25.md`, `cassiano-coll24-25.md`, `pedro-damiao-caelibatu-25.md`, `agostinho-enps105-25.md`, `gregorio-moralia-25.md`, `ruperto-in-nahum-25.md` e as reservas `latinos-reservas-25.md`.
Nenhum autor novo: todos já estão em `ferramentas/autores.json` (`origenes`, `ambrosio`, `jeronimo`, `cassiano`, `pedro-damiao`, `agostinho`, `gregorio-magno`, `bruno-segni`, `isidoro`, `ruperto`). Nenhum é oriental.

## Os achados, em uma linha

Trecho 1 (vv. 1–5, a queda):
- **Jerônimo**, *In Osee* sobre Os 9,10 (v. 3): como o glutão tem o ventre por deus, quem serve à luxúria tem Beelfegor; quem deixa a Deus serve àquilo por que o deixou (frase de etimologia crua cortada).
- **Orígenes**, *Hom.* XX, 3 (vv. 2–3): Beelfegor é uma «espécie de torpeza»; cada pecado por gosto nos consagra ao demônio que o promove, e os espíritos malignos andam em volta para consagrar cada um aos seus mistérios; «observa… não te aproximes das portas da casa da malícia». (OCR conferido na imagem, p. 193.)
- **Orígenes**, *Hom.* XX, 4 (v. 4): os chefes «diante do sol» respondem também pelos pecados do povo, que não ensinaram nem corrigiram; «se os homens pensassem nisso, nunca desejariam o governo do povo». (Imagens, pp. 196–197.)
- **Ambrósio**, *Ep.* 50, 13 (vv. 1–2): o conselho de Balaão por dentro: até as almas fiéis escorregam pelo atrativo do corpo; as mulheres só se entregam depois de provado o amor «pela participação no sacrilégio», e assim o povo perde a proteção do céu.
- **Cassiano**, *Coll.* XXIV, 17 (vv. 1–2): como no corpo os males atacam a parte já fraca, o demônio arma os laços onde a alma está doente, como Balaão com Israel (Isidoro, em `base/`, copia o trecho).

Trecho 2 (vv. 6–15, Fineias):
- **Pedro Damião**, *De caelibatu sacerdotum* 1 (vv. 4, 14–15): por que Moisés registra o posto de Zambri e de Cozbi, e por que o castigo cai sobre os chefes: a queda dos que estão em evidência pesa mais.
- **Ambrósio**, *In Ps.* 118, sermão 18, 10 e 13 (vv. 7–8, 11): há um zelo para a vida, o de Fineias, que salvou o povo da praga; «o zelo, pois, é caridade».
- **Agostinho**, *En. in Ps.* 105, 26 (vv. 7–8, 11): só foi «contado como justiça» porque nasceu do zelo da casa de Deus e do amor, não do ódio; Deus feriu o povo «como um só homem» para salvar a sua alma da morte.
- **Gregório Magno**, *Moralia* V, 45 (vv. 7–8, 11): há uma ira de vício e uma ira de virtude; sem esta Fineias não teria detido o castigo, e Eli, que não a teve, atraiu a ira de Deus.
- **Orígenes**, *Hom.* XX, 5 (vv. 6–8, 11): Fineias edificou o povo de então; ao cristão cabe a «espada do espírito» contra os pensamentos impuros, até chegar ao juízo «pelo verdadeiro Fineias, Cristo». (Imagem, p. 198; corte da frase crua.)
- **Bruno de Segni**, cap. XXV (vv. 7–8, 13): «Matemos nós também o espírito da fornicação», vivendo castamente e aconselhando bem os outros; assim se aplaca a ira de Deus. (As formas «Zarin» e «Corbi» do texto de Bruno foram cortadas.)
- **Isidoro**, *In Num.* XLII, 8 (vv. 7–8, 11): Fineias que trespassa Zambri e a madianita figura a cruz de Cristo, que extingue a idolatria e o desejo da carne.

Trecho 3 (vv. 16–18):
- **Ruperto**, *In Nahum* II (vv. 17–18): por que mandar ferir os madianitas então e ter hoje «paciência desarmada»: a coisa estava em risco porque dela nasceria Cristo; agora, nascido Cristo, está a salvo. É o único bom do trecho 3 neste grupo.

## Como se procurou

- Cache `pesquisa/cache/numeros20-latinos/` e `genesis/` (obras completas do Corpus Corporum, 782 textos), com as notas de Migne reinseridas (`~/.cache/taioe-nm23/latinos/clean/`): busca por `{(Num. XXV…)}` e por *Phinees, Beelphegor, Phogor, Zambri, Cozbi* em todas as obras; contexto lido de cada acerto (Ambrósio, Agostinho, Jerônimo, Gregório, Cassiano, Pedro Damião, Bernardo, Ruperto, Bruno, Isidoro, Gerhoh, Ricardo de São Vítor, Pedro Lombardo, Honório, Hugo, Tertuliano, Beda).
- Todos os excertos do Corpus foram cortados por script do próprio texto baixado (notas, colunas e números de página retirados; cortes marcados com «[...]»). Os de Orígenes foram lidos nas imagens do GCS 30 (pp. 193, 196–198), linha a linha.
- Conferido contra os achados de Nm 20–23: nenhuma sequência de 8 palavras repetida.
- Tomás, *S. Th.* I-II, q. 28, a. 4 (o zelo, efeito do amor): lido; **não cita** Nm 25 nem Fineias, por isso não entrou. O que Tomás diz de Fineias está em II-II, q. 60, a. 6, arg. 2 e q. 64, a. 4, arg. 2 (objeções, não resposta) e no *Super Ep. ad Ephesios* 4,26 («irascimini contra vitia aliena, et hoc cum zelo; Num. XXV, 11»), que repete Gregório (reserva).

## O que não existe ou não serviu

- Ambrósio, *Ep.* 50, 13–15: o §15 só repete que Deus não é injusto nem muda; a frase «a justiça de um só sacerdote desfez todo o conselho», anotada em Nm 23, **não está** nesta carta nem no Corpus.
- Bernardo, *De consideratione* e as cartas (*Ep.* 158, 161, 165, 178, 213, 235, 236, 247 e 276 da ed. de Migne): só usa «Fineias» como emblema do zelo (contra fornicadores, contra intrusos); nenhum trecho comenta Nm 25.
- Pedro Damião, *Epist.* (cc_10045) e *Collectanea in VT* (Números XIII): copiam Orígenes XX, 4–5 sem dizê-lo; `Contra intemperantes clericos` só traz «gladium Phinees» e a ordem de Nm 31,15–16.
- Gerhoh de Reichersberg, Pedro Lombardo (*In Ps.* 105): só glosas e citações em salmos; sem excerto próprio.
- Jerônimo, *Adv. Iovin.* II (PL 23, 241B–C, Fogor = Priapo, Dt 34,6): trata do túmulo de Moisés, não de Nm 25; fica para Dt 34.
- Cassiano, *Coll.* (PL 49, 1308B) entrou; Isidoro, *Sent.* (PL 83, 664C) não está no cache.

## Para outros capítulos

- **Nm 31**: Ambrósio, *De officiis* I, 139 (PL 16, 63D–64A): contra os madianitas, que fizeram pecar o povo pelas suas mulheres, a vingança foi maior («nullum Moyses victor superesse pateretur»), ao contrário dos gabaonitas; Pedro Crisólogo, *Sermo* 27 (PL 52, 276C–277B): o «escândalo» de Balaão, «Balaam divinum occidite», com a palavra de Ap 2,14 (texto em `textos/latinos-reservas-25.md`); Pedro Damião, *Contra intemperantes clericos* (PL 145, 411A–B), «Cur feminas reservastis?» (Nm 31,15–16); Ruperto, *In Num.* II, 26 (base): Balaão não previu que o seu conselho traria a lança de Fineias e a sua própria morte à espada.
- **Nm 26**: Isidoro, *In Num.* XLII, 8 (fim): «Post haec numeratur rursum populus… ut, interfectis primo carnalibus, novus Dei populus censeatur» (o novo censo depois da praga); Ruperto, *In Num.* II, 28 (PL 168, 908C–909C): as «sete pragas» que consumiram a geração do deserto, a última a de Fineias; Pedro Damião, *Collectanea* (Números XIV): só a tribo de Levi entra na terra.
- **Nm 27**: Pedro Damião, *Collectanea* (Números XV, PL 145, 1046C): Salfaad, «sombra na boca», e as cinco filhas (quem prega e não luta); Isidoro, *De eccl. officiis* (PL 83, 783A): Moisés impõe as mãos a Josué (Nm 27,23); Agostinho, *Quaest.* IV (ver `fontes/agostinho.md`).
- **Zelo, em geral** (para o capítulo 25 se faltar, ou para Js 22 e Sl 106): Gregório, *Moralia* (PL 76, 924D–925A, o zelo que «ergueu o braço» de Fineias) e *Hom. in Ezech.* (PL 76, 846B–C, e a passagem com «Phinees ante oculos deducatur», PL 76, 970B), Fineias como modelo do «zelo de retidão»; *Moralia* (PL 76, 872A–B): «An non Phinees irae Dei restitit?»; Jerônimo, carta a Ripário (cc_7132, «Legi seiromasten Phinees… non est crudelitas, pro Deo pietas») e a carta sobre a penitência («Cave ne te Phinees cum Madianitide fornicantem seiromaste configat»); Beda (*Hom.*, PL 94, 398C) e a *Catena aurea* sobre Mt 26,51 e Lc 9,54 (Pedro e os filhos do trovão «sabiam que Fineias fora contado como justo»).
