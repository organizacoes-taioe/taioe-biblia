# Dt 11: relatório (dt11, 23/11/2026)

18 achados em `achados-todos.json` (trecho 2: 9; trecho 3: 6; trecho 4: 3; trecho 1: nenhum).
Procópio 5, Lápide 5, os demais 1 cada: Rábano, Gregório (via Paterius), Agostinho, Beda, Pedro de Celle,
Antônio de Pádua, Lourenço de Bríndisi, Pedro Comestor. Abaixo da meta de 18 a 28 só por pouco: há pouco
comentário patrístico a Dt 11 (o Corpus Corporum quase só acha o versículo citado).

## O que entrou
- Dt 11,10-12 (o Egito regado com o pé × a terra que bebe a chuva do céu): Rábano (Gregório, a graça do alto), Beda *In Lc* II (a sabedoria do mundo rasteja, a divina troa do céu), Antônio de Pádua *Sermo* 73 (a penitência), Procópio (Igreja regada do céu), Lápide (o «regar com o pé» e a providência). **Cinco no mesmo versículo, e três (Rábano, Beda, Antônio) são alegorias parecidas; se o principal cortar, tirar primeiro Antônio e Rábano.**
- Dt 11,13-17 (a chuva): Gregório/Paterius, Procópio (Lei e Evangelho; seca e fim das profecias), Lápide (os meses das duas chuvas), Comestor (a terra que vive da chuva obriga a servir a Deus).
- Dt 11,18-21: Procópio (meditar a lei e imitá-la), Lápide (mão e olhos = ação e reflexão, por Abulense; «enquanto o céu estiver sobre a terra»), Agostinho *QH* V, 17 (escrever nos umbrais é exagero; relevância 1).
- Dt 11,24: Pedro de Celle *De disciplina claustrali* XI.
- Dt 11,25-26: Procópio (o justo temido até pelas feras; a luz e o fogo), Lápide (aguilhão do temor), Lourenço de Bríndisi (as duas vias).

## Como se procurou
Caches `PRINC/pesquisa/cache/deuteronomio/` (Rábano, Agostinho *QH* V, Glosa, Paterius, Procópio PG 87, Lápide, Teodoreto, Orígenes *Adnotationes*, Lourenço, Antônio), busca de frase do Corpus Corporum (`fulltext_search.php`, frase exata da Vulgata) e download de Beda *In Lc*, Pedro de Celle, Comestor. Baixados em `PRINC/pesquisa/cache/deuteronomio/dt11/`. Procópio (PG 87/1, 903–906) e Lápide (t. II, p. 441–442) conferidos nas imagens do archive.org (Procópio: usei o latim de Clauser, que vem impresso ao lado do grego, como em Dt 3). Lourenço: texto do OCR, não conferido na imagem (p. 290).

## Quem não comenta (ou não rendeu)
Teodoreto *Quaest. in Dt* (nenhuma questão sobre Dt 11); Orígenes *Adnotationes/Selecta in Dt* (nada em Dt 11); Glosa de Anselmo de Laon (só repete Rábano/Agostinho; Garizim/Hebal só etimologia); pseudo-Beda *Quaest. super Dt* (nada); Agostinho *De gratia et libero arbitrio* e *De correptione* (o cache só trata Dt 8,17); Jerônimo *In Dan* (Dt 27, não 11); Ruperto *In Dt* (só Dt 32 com Dt 11,10, e *In Gen* I, 41, que cita Dt 11,10 só para dizer que a terra da promessa dispensa o sol: não usado); Gerhoh (copia Ruperto); Pedro Cluniacense *Adv. Iudaeos* (usa Dt 11,18-21 só como argumento de polêmica). Nada de Escrivá em Dt 11 (índice), nenhum Papa achado na busca (nem Bento XVI, Angelus de 1/6/2008).

## Autores novos
- `pedro-de-celle`: Pedro de Celle, c. 1115–1183, «abade de Celle e de Saint-Rémi de Reims, bispo de Chartres; não canonizado», não oriental. **Não está em `autores.json`.**
- `pedro-comestor`, `lapide`, `procopio-de-gaza`, `lourenco-de-brindisi`, `antonio-de-padua`, `rabano`, `beda`, `agostinho`, `gregorio-magno` já usados em outros capítulos (conferir se o `conferir.mjs` aceita os ids dos outros capítulos).

## Para outros capítulos
- Dt 27: Jerônimo *In Dan* IX (PL 25, 1363, nota a Dt 27: as bênçãos e maldições, depois ditas em Garizim e Ebal); Comestor, *Hist. Dt* cap. 4 (PL 198, 1250D), o rito de Garizim e Ebal (usei só o que toca Dt 11,29: se Dt 27 quiser, o trecho do rito é de lá).
- Dt 8,17 (já em Dt 8?): Agostinho *De gratia et libero arbitrio* (cc 7476) cita Dt 8,17; Jonas de Orléans *De inst. laicali* II, 14 cita Dt 6,6-7 e 11,18-19 (cc 8874; o dt12 também baixou este arquivo).
- Dt 32,13: Ruperto *In Dt* (já visto) e Gerhoh *Exp. in cant. Moysis* II.
- Dt 28 etc.: Procópio (PG 87/1) tem notas a muitos capítulos em OCR legível no cache `dt3-orientais/pg87.txt` (col. 891 ss.).

## Problemas
- Meta de 18 atingida no limite; nenhum achado em Dt 11,1-9 e nenhum Papa, santo moderno ou Magistério.
- Todos os achados são em latim; não foi possível conferir o grego de Procópio linha por linha (usei só o latim).
- Pedro de Celle: texto do Corpus Corporum (PL 202), ainda sem conferência na imagem.
