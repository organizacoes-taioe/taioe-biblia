# Dt 5, grupo latinos: relatório

20 achados em `achados-latinos.json` (Agostinho 6, Tomás de Aquino 6, Jerônimo 2, Ruperto de Deutz 2, Lápide, Rábano, Ambrósio e Pedro Damião 1 cada). Por trecho: 1 (vv. 1–5) quatro; 2 (vv. 6–21) sete; 3 (vv. 22–33) nove. Excertos do Corpus Corporum e do Corpus Thomisticum conferidos por script contra o texto do cache (cada trecho é achado literal no original); o de Lápide, transcrito e conferido na imagem.

## O que entrou
- v. 3: Agostinho, *QH* V, q. 9 (o «hoje» e o «vós»: os que eram meninos no Horeb).
- v. 4: Agostinho, *QH* V, q. 9 («face a face» não é visão de Deus; é a evidência da presença; Paulo, «espelho»).
- v. 5: Agostinho, *QH* V, q. 10 (Moisés «entre o Senhor e vós»: Deus não está num lugar); Tomás, *Super Hebr.* 2, l. 3 (o sacerdote medianeiro, Dt 5,5).
- v. 9: Agostinho, *Enchiridion* 46 (os pecados dos pais e a regeneração); Jerônimo, *In Ez* VI (Ez 18: a pena adiada é misericórdia).
- v. 12: Tomás, *Collationes in decem praeceptis*, art. 5 (o dia certo para o amor não esfriar; «arar é menos mau que brincar»).
- vv. 14–15: Lápide (as causas do sábado: criação, memória do Egito, descanso de servos e animais); Tomás, *Collationes*, art. 5 (cita Dt 5,12-14: o descanso do servo).
- v. 16: Tomás, *Super Eph.* 6, l. 1 (cita Dt 5,16; reverência, obediência, sustento); Agostinho, Sermão Denis 25 (honra dos pais e ordem do amor, com Mt 10,37).
- v. 22: Rábano, *In Dt* I, 11 (as duas tábuas, 3 + 7; da pedra ao coração de carne).
- vv. 24–29: Ruperto, *In Cant.* I (o povo que teme a voz de Deus e o óleo derramado, o Verbo); Tomás, *Super Hebr.* 12, l. 4 (Dt 5,26: a palavra que excede o homem); Ruperto, *In Ex* III, 33 («tudo o que disseram está bem dito», Dt 5,28-29); Agostinho, *QH* V, q. 11 (v. 29: o coração novo é graça); Tomás, *ST* III, q. 85, a. 5 (cita Dt 5,29: até o temor vem de Deus).
- vv. 30–32: Ambrósio, *In Ps.* 61 (cita Dt 5,31: «fica aqui comigo» e a queda); Pedro Damião, *Carta* VI, 5 (Dt 5,30-31: o servo de Deus fica de pé diante do Senhor); Jerônimo, *In Is* XVI (Dt 5,32: o caminho real, justo meio de cada virtude).

## Como se procurou
- Caches de `PRINC/pesquisa/cache/` (Dt 1–4, `genesis/`, `nm19-*`, `numeros2*`), com `command grep` e um script (`~/.cache/taioe-dt5-9/dt5-latinos/scan.py`) que varreu os 1,8 GB por frases da Vulgata de Dt 5 (vv. 3, 4, 9, 10, 14–16, 22, 24, 26, 28, 29, 31, 32) e por notas «Deut. V, n» do Migne. Achou: Agostinho (QH V, Enchiridion, Opus imperfectum, Denis 25), Jerônimo (In Ez, In Is), Ambrósio, Pedro Damião, Hilário, Ruperto, Tomás (Collationes, Super Hebr., Super Eph., ST).
- Lápide t. II (`lapide_t2.txt`), cap. V (pp. 409–421, archive.org `commentariainscr02lapi_0`, páginas n440–n452): imagens baixadas em `PRINC/pesquisa/cache/deuteronomio/dt5-latinos/`.
- Rábano, *In Dt* I, 11 (`rabano-dt.txt`), Glossa (cc 8945) e Isidoro, *QVT* (cc 21433): a Glossa e Isidoro repetem Agostinho e o próprio Rábano.
- Nada novo foi baixado.

## Não comentam Dt 5
- Pseudo-Beda, *Quaestiones super Deuteronomium* (cc 8480): nada sobre Dt 5.
- Isidoro, *QVT* In Dt (cc 21433): só outros capítulos (os cap. XXIX–XXXI do Êxodo, sobre as tábuas, repetem o Rábano).
- Ruperto, *De Trin.* In Dt: começa em Dt 18 (cap. IV, «Prophetam de gente tua»); sobre Dt 5 só serve o *In Ex* e o *In Cant.* usados acima.
- Hugo de São Vítor (*Adnotationes*, só de Dt 15 em diante), Bruno de Segni (começa em Dt 13), Gregório Magno (Moralia/Homilias do cache), Cassiano (*Collationes*), Leão, Crisólogo, Fulgêncio: nenhuma citação de Dt 5 nos textos do cache.

## Autores novos
Nenhum: todos os `autor_id` já estão em `ferramentas/autores.json`, e nenhum é oriental.

## Observações e problemas
- Três excertos de Lápide que eu havia escolhido (v. 9 «Deus zeloso», v. 9 «medida dos pais», v. 21) já estavam com `dt5-gregos-modernos` e **foram retirados**; ficou o do sábado (vv. 14–15). A conferência 8-a-8 contra todos os `achados-*` e o `conteudo/` não acusou excerto repetido.
- Rábano: o cache traz «Cur ego in duabus tabulis» (erro de edição digital); corrigido para «Cur ergo» no `original`.
- Agostinho, Sermão Denis 25: o cache traz «prae ponis» (quebra de linha); unido em «praeponis». A numeração (Sermão 25 de Denis, PL 46) a conferir pelo principal.
- Lápide, p. 416: o impresso diz «hic vers. 25» onde se espera 15; cortei essa oração com `[...]`.
- Textos do Êxodo 20 que citam o mesmo trecho: o *Enchiridion* 46 e o Jerônimo *In Ez* VI falam de Êx 20,5 / 34,7 e Dt 5,9 ao mesmo tempo (a nota do Migne remete a Dt 5,9-10), e a *Collationes* de Tomás comenta o sábado por Êx 20,8; se o pesquisador do Êxodo escolher o mesmo trecho, o `conferir` recusa o repetido.
- Tomás, *Super Hebr.* 12, l. 4 e *Super Hebr.* 2, l. 3: página «Reportatio vulgata» do Corpus Thomisticum; trato como texto de Tomás, como nos outros capítulos.
- Tomás, *Collationes* art. 5: o parágrafo traz, no meio, uma generalização sobre os judeus que não entra; cortada com `[...]`.
- Rábano: a frase «cor lapideum Judaeorum» ficou fora do excerto de propósito.

## Para outros capítulos
- Dt 6 (`dt6-latinos`): Rábano, *In Dt* I, 12 (o *Shemá*: «Diliges Dominum… ex tota anima»), com texto de Agostinho sobre a perfeição do amor na pátria; Agostinho, *QH* V, q. 12 (já com dt6-latinos).
- Dt 9–10: Agostinho, *QH* V, q. 14 (Dt 9,6-8: «dura cervice»; os que não souberam direita nem esquerda) e q. 15 (Dt 10,1-4: as segundas tábuas).
- Êx 20 / Êx 31: Agostinho, *Contra Adimantum* VII (Êx 20,5 e Dt 5,9, «os que me odeiam») e XVI (o sábado como signo; cita Dt 5,12-15); *Carta* 55 (o sábado, o único preceito figurado); Tomás, *Collationes* (todos os mandamentos); Ruperto, *In Ex* III, 33 (outras partes); Isidoro, *QVT* In Ex, cap. XXIX–XXXI (as duas tábuas).
- Mais pistas para o v. 31 («Tu vero hic sta mecum»), não usadas para não repetir o versículo: Ambrósio, *Ep.* (cc 21400, n. 41–42: «mecum stas, si stes in Ecclesia»), *Exp. Ps 118*, sermão 17 («Stans enim cum Deo, lapsum timere non poteris»), *De Cain et Abel* I, 7 (Moisés separado do povo, figura de Cristo); Hilário, *Tract. in Ps* 124 («in habitantibus standum est, non discurrendum»); Jerônimo, Hom. sobre Lc 15 («peccatorum jacere, justorum stare est»).
