# Dt 9, todos os grupos: relatório (dt9)

20 achados em `achados-todos.json` (Ruperto 4; Agostinho 2, Jerônimo 2, Bento XVI 2; Teodoreto, Crisóstomo, Cassiano, Ambrósio, Tomás, Catecismo, Máximo de Turim, Remígio de Lião, Franco de Affligem, Marulo 1 cada). Abaixo da meta de 25: o cache e o Corpus Corporum quase não têm quem cite Dt 9 além dos vv. 4–6; vv. 22–24 sem achado (Nm 11–14 cobre). Excertos montados por script a partir dos textos baixados (o `original` é cortado do arquivo, não reescrito); a tradução é minha.

## O que entrou
- T1 (vv. 1–6, a graça e não o mérito):
  - Teodoreto, *Quaest. in Deut.* 7 (Enac abate o orgulho; nem das virtudes se envaidecer), relevância 2.
  - Cassiano, *Coll.* V, 15 (Dt 9,4 contra atribuir ao livre-arbítrio a vitória sobre os vícios), 3.
  - Tomás, *ST* I-II q. 98 a. 4 (a Lei e a terra vêm da promessa a Abraão, e esta, de eleição gratuita), 3. Não é o excerto de Dt 7 (q. 105 a. 3 ad 4).
  - Ambrósio, *De Cain et Abel* I, 7, 28 (o Testamento é a graça perfeita), 2.
  - Ruperto, *In Ioan.* I (Jo 1,16: Lei e promessa foram graça), 2; Ruperto, *De Trin., In Ex.* III, 19 (Dt 9,4-6 junto de Rm 3), 2.
  - Jerônimo, *Dial. c. Pelag.* I, 36 (somos conservados pela misericórdia), 2.
  - Franco de Affligem, *De gratia Dei* IV (nem espada nem arco nem justiça: a promessa aos pais), 2.
  - Agostinho, *QH* V, q. 14 (até os que a Escritura louvou são «de dura cerviz»), 1: argumento em muitas etapas, só para registro.
- T2 (vv. 7–21):
  - O jejum de Moisés (vv. 9.18): Ruperto, *In Matth.* VI (jejuou por vontade própria, primeiro para receber a palavra, depois para obter o perdão do povo), 3; Máximo de Turim, hom. 44 (Moisés e Cristo), 2; Bento XVI, audiência de 1/6/2011 (cita Dt 9,9; os quarenta dias), 2.
  - O dedo de Deus (v. 10): Agostinho, *De spir. et litt.* 16–17 (as tábuas e o Espírito Santo), 2; Ruperto, *De div. off.* X, 10 (cita Dt 9,10 por extenso), 3.
  - O medo de Moisés (v. 19): Crisóstomo, *In Hebr.* 32, 2; Jerônimo, *In Is.* (Dt 9,19), 2.
  - A ira de Deus e a oração (vv. 19–20): Remígio de Lião, *De damnatione generali per Adam* (cita Dt 9,19-20, e Aarão), 2.
- T3 (vv. 22–24): nada.
- T4 (vv. 25–29, intercessão): Bento XVI, mesma audiência (Moisés «entre dois amores», a honra de Deus), 3; Catecismo 2577 (os argumentos da oração de Moisés), 3; Marulo, *De inst. bene vivendi* II, 1 (cita Dt 9,25), 2.

## Como se procurou
- Caches de `PRINC/pesquisa/cache/` (Teodoreto, Rábano, Lápide, `genesis/`, `numeros20-latinos`, CCC): `command grep` por notas «Deut. IX» do Migne e por frases da Vulgata de Dt 9; deu Ambrósio, Ruperto, Jerônimo, Agostinho (*Enarr.*, *Tract.*).
- **Busca de texto completo do Corpus Corporum** (nova, serve aos outros capítulos): `https://mlat.uzh.ch/php_modules/fulltext_search.php?&query="frase"&offset=0&limit=30&order_by=&index_type=s` devolve XML com autor, obra, cabeçalhos e a frase; só frase entre aspas (sem AND), grafia normalizada (i por j, ae por e). Script em `~/.cache/taioe-dt5-9/dt9/srch.py` e `multi.py`. Achou Franco, Remígio, Máximo, Marulo, Jerônimo (*Dial.*).
- Baixados (em `PRINC/pesquisa/cache/deuteronomio/dt9/`): Cassiano, *Collationes* (7530), Jerônimo *Dial. c. Pelag.* (7158), Agostinho *De spir. et litt.* (7482), Máximo de Turim (7652), Remígio (9158), Franco (10847), Marulo (13242), Corpus Thomisticum *ST* I-II q. 98. Os *Moralia* de Gregório (baixados e apagados): só tratam de Êx 32,10, não de Dt 9.
- Bento XVI, 1/6/2011: `vatican.va` em italiano, lido por script.

## Quem não comenta Dt 9
- Rábano, *In Dt* (cap. XIV–XV dele): só copia Agostinho, *QH* V, 14 e 15; Glosa ordinária (Anselmo de Laon): só remete a Agostinho.
- Lápide sobre Dt 9: só filologia (hipérbole das cidades, quatro dias de jejum), nada que ajude o leitor.
- Orígenes (*Selecta* e *Adnotationes* gregos) e Procópio (cache `dt3-orientais/pg87.txt`): nada sobre Dt 9 no cache.
- Gregório Magno (*Moralia*, *Regula pastoralis*), Bernardo (*Cant.* e *Pro Dom. I Novembris*) e Agostinho (*Enarr.* Sl 105) só falam da intercessão de Moisés por Êx 32 e Sl 106,23: excluídos pela regra do Êxodo.
- Escrivá: o índice não tem Dt 9. Papas e Catecismo além do 2577: nada achado (Francisco, audiência de 17/6/2020, só cita Êx 32).
- Tomás, *Super Hebr.* 12, l. 4 (v. 21): diz que a frase de Moisés não é de Êx 20 e remete a Êx 3; não cita Dt 9.

## Autores novos
- `remigio-de-liao`: Remígio de Lião, † 875, arcebispo de Lião; sobre: «arcebispo de Lião (séc. IX), autor do tratado *Sobre a condenação geral por Adão*»; não oriental. Obra pouco conhecida: o principal decide se entra.
- `franco-de-affligem`: Franco de Affligem, séc. XI–XII, monge beneditino da abadia de Affligem (Brabante); não oriental.
- `marulo`: Marko Marulić (Marco Marulo), 1450–1524, humanista católico de Split, autor da *Institutio bene vivendi per exempla sanctorum* (1506); não oriental. Não é santo.
- `catecismo`, `bento-xvi`, `maximo-de-turim` já constam em `autores.json`.

## Problemas e cuidados
- **Crisóstomo, *In Hebr.* 32**: Dt 4 já tem o começo da passagem (até «Ἔκφοβός εἰμι καὶ ἔντρομος»). O meu começa depois dele («Μωϋσῆς εἶπεν· Ἔκφοβός εἰμι… Τί θαυμαστὸν…»), para não repetir, mas é um excerto curto que o principal pode juntar ao de Dt 4 ou descartar.
- Agostinho, *De spir. et litt.* e Ruperto, *De div. off.*: o «dedo de Deus» das tábuas; Agostinho cita Êx 31,18 e não Dt 9,10 (as notas de Migne remetem a Dt 9,10); decidir se entra.
- Jerônimo, *In Is.*: a referência a Dt 9,19 vem da nota do editor de Migne (o texto de Jerônimo diz só «com Moisés»).
- Remígio funde Dt 9,19 e 10,10 (« e te perdere noluit »); o excerto cita as duas coisas sem separar.
- Teodoreto (OCR do PDF): conferi só pelo texto do PDF, sem ver a imagem; juntei as palavras partidas no fim da linha («ἀκή κοας» → «ἀκήκοας» etc.).
- Marulo: o `original` conserva o «ę» da edição (æ).
- Catecismo e Bento XVI: `direitos` «citação curta»; o Catecismo está no português de Portugal (traduzi para o do Brasil).
- Edições de Remígio (coluna) e do Corpus (Marulo): só o que o Corpus Corporum mostra; sem volume da PL conferido para Remígio.
- Pouca cobertura de T3, e T4 só com três; nada de Padres gregos além de Teodoreto e Crisóstomo (o texto grego do cache não traz mais).

## Para outros capítulos
- Dt 8: Ambrósio, *Ep. extra coll.* a Teodósio (PL 16; `cc_21400`, cita Dt 8,17); Agostinho, *De gratia et lib. arb.* 7, 16 (já usado em Dt 8); Cassiano, *Coll.* V, 14 (Dt 7).
- Dt 10: Agostinho, *QH* V, q. 15 (Dt 10,1-4, as duas tábuas: Deus e o homem escrevem, a graça e a vontade) e Rábano, *In Dt* XV; Máximo (mesma hom. 44).
- Dt 25: Ruperto, *De Trin., In Dt* I, 34 (as quarenta chicotadas e o jejum de quarenta dias de Moisés, cita Dt 9,18).
- Gn 15,16 e Nm 21,26: Procópio (PG 87), cita Dt 9,5 e 9,1, mas o OCR do cache é ruim.
- Sl 105,23 (106): Agostinho, *Enarr.* Sl 105, 21; Bernardo, *SC* 76 e *Pro Dom. I Nov.*; CCC 2577 (intercessão de Moisés).
- Jo 9 (o cego de nascença): Ruperto, *In Ioan.* VIII (cita Dt 9,5-6 para dizer que ninguém foi escolhido por mérito), outro trecho do mesmo livro que o que usei.
- Os 2 e Mq 6: Ruperto, *In Osee* e *In Mich.* (citam Dt 9,4-6 e 9,7).
