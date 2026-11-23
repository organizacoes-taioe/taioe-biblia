# Dt 2: relatório do grupo `latinos`

Entregues: `achados-latinos.json`, 12 achados (trecho 1 = 3, trecho 2 = 2, trecho 3 = 2, trecho 4 = 5).
Nenhum autor novo; todos já têm `autor_id` usado em capítulos anteriores. Nenhum é oriental.
Agostinho 3, Lápide 3, Rábano 2, Jerônimo, Ruperto, Beda e Bruno de Segni 1 cada.

## O que entrou

Trecho 1 (vv. 1–8):
- **Jerônimo**, *In Abdiam*, prólogo: Edom é irmão de Israel; por isso a terra não lhe foi dada e foi proibido armar-se contra ele.
- **Bruno de Segni**, *Expositio in Pentateuchum*, sobre Dt 32,10 (cita Dt 2,3): os quarenta anos rodeando Seir foram cuidado de Deus («a menina dos seus olhos»).
- **Lápide**, Dt 2,3: Deus, compadecido, manda abreviar o rodeio e ir direto à terra prometida. Conferido na imagem (p. 398).

Trecho 2 (vv. 9–15):
- **Agostinho**, *Contra Faustum* XXII, 60: a terra dos descendentes de Ló é dom de Deus por causa de Abraão (a nota de Migne remete a Dt 2,9).
- **Beda**, *Ep.* 14 a Acca: os 38 anos de rodeios (cita Dt 2,1.14) têm sentido moral; depois do desvio, sobe-se de novo aos poucos, pela penitência.

Trecho 3 (vv. 16–23):
- **Ruperto**, *In Amos* I: Deus vedou as terras de Edom, Moab e Amon por serem parentes; eles responderam com hostilidade. Cita Dt 2,4-5.9.19.
- **Lápide**, Dt 2,19: em atenção aos méritos de Ló (Amon, Moab) e de Isaac e Abraão (Edom). Conferido na imagem (p. 399).

Trecho 4 (vv. 24–37):
- **Agostinho**, *Quaest. in Hept.* V, 2: o endurecimento de Seon (Dt 2,30), com a justiça de Deus nos juízos insondáveis. É o único comentário patrístico direto de Dt 2,30 que achei.
- **Agostinho**, *Quaest. in Hept.* IV, 44 (sobre Nm 21,24-25): guerra justa por passagem inofensiva negada; contra Edom, irmão, não lutaram. Trata do paralelo de Nm 21, não cita Dt 2: relevância 2, pode cair.
- **Rábano**, *Enarratio in Dt* (PL 108, 851): quem passa em paz pelo mundo irrita o príncipe do mundo e atrai perseguição (Dt 2,26-32).
- **Rábano**, ibid. (PL 108, 852–853): cada cristão foi antes «cidade de Seon» e agora vive sob o Rei manso e humilde (Dt 2,33-36).
- **Lápide**, Dt 2,30: como Deus endurece: retira a graça que abranda e deixa agir o temor do rei. Conferido na imagem (p. 400).

## Como se procurou

- Todo o cache latino já baixado (Corpus Corporum, 800 textos, Migne com notas reinseridas; script em `~/.cache/taioe-dt2/latinos/`, `prep.py`): busca por frases da Vulgata de Dt 2 e por *Seon/Sehon, Seir, Esau/Edom, filiis Lot, Zared, Cadesbarne, induraverat, verbis pacificis, triginta octo annorum*, e por «Deuteronomio» perto dessas palavras.
- Busca de frase na API do Corpus Corporum (`fulltext_search.php`) com os versículos; baixados *Quaest. in Hept.* (texto 7312), a Glosa de Anselmo de Laon (8945), *De gratia et lib. arb.*, *De corr. et gratia*, pseudo-Beda *Quaest. super Dt* (8480), em `PRINC/pesquisa/cache/deuteronomio/latinos/`.
- Lápide: texto do cache, conferido letra a letra nas imagens do t. II (archive.org `commentariainscr02lapi_0`, páginas 398–400).
- Conferido contra Nm 21 (conteudo/) e contra Dt 1, Dt 3 (pastas vizinhas): nenhuma sequência de 8 palavras repetida acima de 20%.

## Quem não comenta (ou não serve)

- **Tomás**: *Suma* I-II q. 98, 100, 105 e II-II q. 61 (cache) citam Edom/Moab/Amon só por Dt 23; nenhum Dt 2.
- **Gregório**, **Ambrósio**, **Bernardo**, **Cassiano**, **Isidoro** (*Allegoriae*, *QVT* sobre Dt: só nomes alegóricos), **Hugo de São Vítor**, **pseudo-Beda** (*Quaest. in Dt* não chega ao cap. 2): nada de Dt 2.
- **Jerônimo**, *Ep.* 78 (mansões): sobre Números. **Pedro Damião**, *Collectanea*: Seon só por Nm 21.
- **Agostinho**, *De gratia et libero arbitrio* e *De correptione*: não citam Seon. A pista dos 38 anos (Jo 5,5): Agostinho, Beda, Alcuíno, Hilário e Cassiano falam do paralítico sem citar Dt 2,14.
- **Rábano** sobre Dt 2,26-29 (promessa do batismo) copia Orígenes, *Hom. in Num.* 12, 4, que já entrou em Nm 21: deixei fora.
- **Ruperto**, *De Trinitate* (Nm 21, cap. XIV): por que Israel pediu passagem a Seon se Moab fora poupado; raciocínio longo, deixei fora.
- **Glosa** (Anselmo de Laon e escola, PL 113): reproduz Isidoro, Rábano e Agostinho; sem texto próprio.

## Problemas

- Corpus Corporum: o texto de Rábano tem coluna repetida/embaralhada (PL 108, 849–851); usei a segunda cópia, que está íntegra. Em Ruperto havia «filli» (corrigido para «filii»).
- Cinco textos não são comentário direto de Dt 2 (Bruno, Ruperto, Jerônimo, Beda, Agostinho IV,44): citam ou tratam do mesmo episódio. O pedido exige comentar o capítulo; só Agostinho V,2, Lápide e Rábano o fazem de fato.
- Falta o grosso da tradição latina medieval em Dt 2 (Hugo de São Caro, Nicolau de Lira, Dionísio Cartuxo) por não estar no Corpus; Dionísio e Lira ficam como pista.

## Para outros capítulos

- **Dt 1**: Agostinho *QH* V, 1 (Dt 1,29-30) já está no grupo do capítulo 1. Pseudo-Jerônimo, *De X tentationibus populi Israel* (PL 30/23, cita Dt 1,44).
- **Dt 3**: Agostinho *QH* V, 3 (Og, «reliquus a Raphain»).
- **Dt 4**: Agostinho *QH* V, 4–8 (imagem e semelhança, Dt 4,16-33).
- **Dt 5**: Agostinho *QH* V, 9–10 (Dt 5,2-6).
- **Dt 23** (Edom e Egito): Tomás, *Suma* I-II q. 105 a. 3 ad 2 (texto em `cache/deuteronomio/latinos/ct/sth2098.html`).
- **Nm 21** (Seon): Orígenes, *Hom. in Num.* 12; Ruperto, *De Trinitate* (PL 167, 892–893).
