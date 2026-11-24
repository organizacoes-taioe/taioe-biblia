# Dt 10, todos os grupos: relatório (dt10)

11 achados em `achados-todos.json` (abaixo da meta de 25: a busca no Corpus Corporum quase só devolve a Vulgata e cópias de Agostinho; a conta de uso foi limitada).

## O que entrou
- T1: Agostinho, *QH* V q. 15 (Deus e o homem escrevem as segundas tábuas), 3.
- T2: Agostinho, *QH* V q. 16 (Levi, o Senhor como parte; sacerdócio régio), 3.
- T3 (vv. 12–17): Teodoreto, *Quaest. in Dt* 7 (o que Deus pede; o amor aos pais) 2; Ruperto, *De Trin., In Dt* I, 3 (Moisés atrai ao amor) 3; Lápide, v. 12 (temor filial; conferido na imagem, p. 438) 2; Francisco, *Laudato si'* 67 (Dt 10,14; a audiência de 7/11/2018 só o retoma) 2; Teodoreto q. 8 (Deus dos deuses = juízes) 2.
- v. 16, circuncisão do coração: Gregório Magno, *Moralia* XXVIII, 12; Rábano, *In Dt* II, 1; Teodoreto q. 7. 

## Como se procurou
Busca por frase no Corpus Corporum (`~/.cache/taioe-dt10-14/dt10/srch.py`, `add.py`, `b*.py`); cache de Rábano, Agostinho, Teodoreto e Lápide; baixados em `PRINC/pesquisa/cache/deuteronomio/dt10/` (Paterius, Moralia, Jerônimo *Epistolae*, Ruperto).

## Fora
- Jerônimo, *Ep.* 52, 5 (Levi, «pars Domini»): já está em Nm 18; retirado.
- Ruperto: o início do excerto («Haec legis explanatio») está em Dt 1; aqui só vale desde «Et nunc, Israel».
- Rábano sobre os vv. 17–19 reproduz Gregório (Moralia / Hom.) sobre Dt 6,5; não usado.
- Escrivá, *Conversaciones* 40 (Dt 10,17): escriva.org bloqueou o acesso (Cloudflare); não conferido.
- Orígenes, *Adnotationes*: nada sobre Dt 10. Ambrósio, *In Ps.* 118 cita Dt 13,4, não 10,20.
- Não pesquisados por falta de fôlego: Catecismo 2056 (Dt 10,4; talvez já em Dt 5), Orígenes *Hom. in Gn* 3, Justino, Cirilo, Bernardo, Basílio, Tomás, Crisóstomo sobre o estrangeiro, João Paulo II, *Fratelli tutti*.

## Autores novos
Nenhum (todos já em `autores.json`: Agostinho, Gregório Magno, Rábano, Teodoreto, Ruperto, Lápide, Francisco).

## Problemas
- Teodoreto: texto do PDF, sem conferir na imagem (palavras partidas no fim da linha juntadas por mim).
- Ids dos Padres conferidos só pelo tamanho; rodar o `conferir` no principal.
- Gregório: o texto traz «Sede cum» (erro de edição), corrigido para «Sed cum».
