# Dt 18, todos os grupos: relatório (dt18)

25 achados em `achados-todos.json` (meta 20 a 30). Por trecho: T1 (vv. 1–8) 2; T2 (9–14) 11; T3 (15–20) 11; T4 (21–22) 1 mais o Tomás q. 172 que ficou só como pista (abaixo).

## O que entrou
- T1: Rábano, *In Dt* cap. 18 (ministros do altar; o Senhor é a herança); Bruno de Segni (o Senhor herdado; a espádua e o estômago).
- T2: Agostinho, *QH* V q. 29; Tomás, *ST* II-II q. 95 a. 1, a. 4, a. 6 e I-II q. 98 a. 5 (v. 13, «perfeito e sem mancha»); Rábano, *De magicis artibus* ×4 (Cristo fonte de verdade; pitonisa e Samuel; por que os demônios acertam; demônios × profecia); Máximo de Turim, Hom. 16 (auspícios de ano novo); Catecismo 2115–2116.
- T3: Rábano, *In Dt*; Ruperto, *De Trin., In Dt* I, 4 (mediador) e *In Apoc.* III; Beda, *Retract. in Acta* 3,22; Bruno de Segni (profeta ressuscitado); Agostinho, *C. Faustum* XVI, 15 e *Tr. in Io.* 24, 7; Cipriano, *Testimonia* II, 18; Tomás, *Super Io.* 6 l. 2; Francisco, Angelus 31/1/2021 (citação curta); Lápide, v. 15 (conferido na imagem, p. 465).
- T4: Ruperto, *In Dt* I, 4 (o sinal do profeta, as obras de Cristo).

## Como se procurou
Caches de Rábano, Agostinho (*QH*), Glosa, Bruno, Ruperto, Máximo e Tomás; `grep "Deut. XVIII"` nos caches (acha citações em *Contra Faustum*, *Tr. in Io.*, Beda, Máximo); download no Corpus Corporum (Rábano *De magicis*, Ruperto *In Apoc.*, Beda, Cipriano, *C. Faustum*) e no vatican.va. Scripts em `~/.cache/taioe-dt10-14/dt18/` (`add.py`, `run*.py`); downloads em `PRINC/pesquisa/cache/deuteronomio/dt18/`.

## Quem não comenta
Teodoreto (*Quaest. in Dt* 13–18 pulam o cap. 18); Orígenes, *Adnotationes* e *Selecta* (nada sobre Dt 18); Escrivá (índice sem Dt 18); Bento XVI, Angelus de 2009 e 2012 (sem menção a Dt 18).

## Autores novos
Nenhum no `autores.json` além do que já existe. Usados: Bruno de Segni, Máximo de Turim, Cipriano, Lápide (todos já cadastrados; ids de autor locais).

## Para outros capítulos
- Ruperto, *De Trin.* (PL 167, 999): cita Dt 18,15 no comentário a Dt 34,10 (Josué não é o profeta como Moisés); serve a Dt 34.
- Tomás, *ST* II-II q. 172 a. 5 ad 3 (cita Dt 18,21-22 com Crisóstomo; texto em `dt18/tomas-3171.txt`): não usado só para não passar de 5 do Tomás; é o melhor candidato para o v. 21–22 se faltar T4.
- Tomás, *In Jer.* (Jer 24 e 29) e Gerhoh de Reichersberg, *Comm. in Ps.* 29,9 citam Dt 18,22 (não lidos).
- Jerônimo, *Dial. c. Pelag.* I, 13 (Dt 18,13 «perfecti estote») é debate, não comentário: não usado.
- Cipriano, *Testimonia* III, 82 «Não se deve augurar» (Dt 18,10, só citação).

## Problemas
- T4 fraco (1 achado): poucos comentam vv. 21–22.
- Máximo: o texto da PL traz «auspiceminí», corrigido para «auspicemini». Rábano e Ruperto: textos do Corpus Corporum, sem conferir na imagem.
- Ids dos Padres só conferidos pelo `conferir.mjs` (passou, sem sobreposição com outros capítulos).
