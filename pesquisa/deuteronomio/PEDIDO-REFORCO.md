# Pesquisa: reforço dos capítulos fracos do Deuteronômio (26, 28, 29, 31 e 33)

Pedido do Gere (25/11/2026): «reforçar os fracos». Esses capítulos ficaram com 3 a 6 comentários, porque a pesquisa de
23/11 foi feita perto do limite e só nas fontes à mão. Agora há folga: procurar também fora dos caches, com calma.

Raiz do trabalho (worktree): `/home/geremias/.cache/taioe-dt-reforco/wt` (= WT).
Pasta principal, só para ler os caches: `/home/geremias/Geremias/Software MEU/taioe/biblia` (= PRINC).

**Valem, sem mudança, estas seções de `WT/pesquisa/deuteronomio/PEDIDO-5-9.md`:** «Regras do Gere para escolher»,
«Onde procurar», «Cuidados com a máquina» e «Formato da entrega». Ler antes de começar, trocando o WT de lá por este.
Vale também, de `WT/pesquisa/deuteronomio/PEDIDO-25-34.md`, o parágrafo «Passagens duras» e a descrição dos capítulos
(trechos e pistas). Ler o `relatorio-todos.md` e o `achados-todos.json` do capítulo: o que já foi achado, o que não serviu
e onde já se procurou sem achar. O que está em `conteudo/deuteronomio/<ccc>.json` (campo `comentarios`) já está no site.

Os scripts ficam em `~/.cache/taioe-dt-reforco/<seu-nome>/`; os downloads, em `PRINC/pesquisa/cache/deuteronomio/<seu-nome>/`.
**Esta máquina tem só 6 GB de RAM, e há outros dois pesquisadores ao mesmo tempo:** um processo pesado por vez, com
`systemd-run --user --scope --slice=pesado.slice -q -- <comando>`; um PDF por vez, apagando o que já leu; preferir texto
(Corpus Corporum, Perseus, archive.org `_djvu.txt`, Corpus Thomisticum, vatican.va, escriva.org) a PDF grande.

**Caches que a pesquisa de 23/11 não usou nesses capítulos** (cobrem o Deuteronômio inteiro):
- `PRINC/pesquisa/cache/deuteronomio/gregos/`: `th-oct.txt` (Teodoreto, *Quaestiones in Octateuchum*, OCR: conferir na
  imagem em `gregos/img/` ou na fonte antes de citar), `or-adn.txt` e `or-sel.txt` (Orígenes, *Adnotationes* e *Selecta in
  Dt*, PG 17 e 12), `ass1.txt` (Efrém, Assemani I, comentário ao Deuteronômio).
- `PRINC/pesquisa/cache/deuteronomio/latinos/`: `lapide_t2.txt` (Cornélio a Lápide, OCR em colunas: conferir na imagem),
  `rabano-dt.txt`, `cc_*.txt` (Corpus Corporum).

**Meta: o que falta em cada um** (achados bons, diferentes do que já está; trechos sem nenhum comentário primeiro). O
`"trecho"` é o número da descrição em `PEDIDO-25-34.md`.

| pesquisador | capítulos | entrega |
|---|---|---|
| `r26-29` | Dt 26 e Dt 29 | 6 a 9 em cada; no 26, o trecho 3 (vv. 16–19) e o «arameu errante» (vv. 5–10); no 29, o trecho 2 (vv. 9–14) |
| `r28` | Dt 28 | 8 a 12; os trechos 5, 8, 9 e 10, que não têm nada, e os vv. 47 (servir com alegria), 65–67 (o coração sem repouso) e 66 (a vida suspensa, lida pelos Padres como a cruz: Melitão, Irineu, Atanásio, Cirilo de Jerusalém, Lactâncio, Cipriano) |
| `r31-33` | Dt 31 e Dt 33 | Dt 31: 4 a 6, sobretudo o trecho 3 (vv. 14–23: o cântico como testemunha, Deus que esconde o rosto, «sê forte», Josué); Dt 33: 6 a 9, **gregos e modernos** (Teodoreto, Orígenes, Efrém, Cirilo de Alexandria, *Glaphyra*, Hipólito, *Sobre as bênçãos de Moisés*, se houver original; v. 3, v. 9 «não vos conheço» como desapego, v. 25 a força como os dias, v. 27 os braços eternos), e os trechos 2, 4 e 5 |

Grupos a cobrir em cada capítulo: Padres gregos e latinos, medievais, santos modernos (Francisco de Sales, Lourenço de
Bríndisi, Belarmino, Afonso, Granada, Newman, Teresinha, João da Cruz), Papas e Catecismo (vatican.va; citação curta),
São Josemaria (`PRINC/pesquisa/fontes/escriva-indice.md`), liturgia (o lecionário: Dt 26,4-10 é o 1º domingo da Quaresma,
ano C; Dt 26,16-19, sábado da 1ª semana da Quaresma; Dt 31,1-8 e Dt 34, 19ª semana do TC, ano I).

**O mesmo excerto não pode entrar duas vezes:** antes de entregar, comparar (8 palavras seguidas) com todos os
`WT/pesquisa/deuteronomio/*/achados-*.json` e com `WT/conteudo/` (Bíblia inteira). O mesmo autor e a mesma obra podem
voltar, com outro trecho.

**Entrega:** `WT/pesquisa/deuteronomio/<ccc>/achados-reforco.json` (formato de «Formato da entrega») e
`relatorio-reforco.md` na pasta de cada capítulo. Gravar desde o primeiro achado. Os ids não podem repetir os de
`achados-todos.json`. Sem mesóclise, sem `noutro`/`nalgum`, sem pronome contraído, sem uso europeu.

Resposta final ao principal: só o número de achados por capítulo e trecho, os caminhos, autores novos e problemas.
