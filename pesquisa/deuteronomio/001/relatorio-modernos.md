# Deuteronômio 1: santos modernos, Magistério e liturgia — relatório

Pesquisa de 2026-11-23. **6 achados** em `achados-modernos.json` (abaixo dos 8 pedidos: o capítulo quase não tem comentário moderno).
Trecho 5: 4; trecho 6: 1; trecho 7: 1. Nenhum autor novo; nenhum oriental. Todos os originais conferidos na imagem da página
(Sales, Lourenço, Belarmino) ou no texto do newmanreader e do vatican.va (Newman, Francisco).

## 1. O que entrou
- **Sales, carta MDII à Sra. de Veyssilieu (16/1/1619), pp. 343–344** (rel. 3, v. 31): a edição de Annecy anota «Cf. Dt 1,31» em «où vous ne pourres pas marcher, il vous portera»; a criança nos braços do pai.
- **Papa Francisco, *Patris corde* 7** (rel. 3, v. 31; citação curta): Dt 1,31 como medida da paternidade de José.
- **Newman, PPS III, 2, pp. 16–17** (rel. 2, vv. 29–30): «o Senhor combaterá por vós»; esperar em vez de agir por conta própria (nota do autor: Dt 1,29-30).
- **Newman, PPS III, 2, pp. 17–18** (rel. 3, vv. 41–43): proibidos de subir, quiseram subir; a presunção que corre onde Deus não guia.
- **Lourenço de Bríndisi, 1º Quaresmal, Dom. II, p. 197** (rel. 2, v. 33): coluna de nuvem e de fogo como figura de Cristo guia (nota da edição: Dt 1,30-33).
- **Belarmino, *De amissione gratiae* V, 4, p. 400** (rel. 2, v. 39): «filhos que hoje ignoram a diferença entre o bem e o mal»; os pequenos não têm pecado atual (polêmico, mas curto).

## 2. Como se procurou
- Varredura dos 9.954 documentos papais em italiano e latim (lista do Nm 25, Bento XV a Leão XIV): `Dt 1,n`, `Deut. 1,n`, «porta il proprio figlio», «portavit te». Script em `~/.cache/taioe-dt1/modernos/scan.sh`, resultado `hits.txt`. Único resultado: *Patris corde* 7. Nenhum discurso à Rota Romana, nem *Verbum Domini* ou *Dei Verbum*, cita Dt 1 por essa forma de citação (talvez haja citações sem a referência).
- Catecismo da Igreja Católica (27 arquivos em português, vatican.va): **nenhuma citação de Dt 1**.
- Índices de citação: Sales (t. XXVII): Dt 1,31 → t. XVIII, 344 (achado); Dt 1,35-38 → t. VIII, 233 (ver reserva).
- Lourenço (13 volumes, as notas «Dt 1, …»): só remissões de passagem (Dt 1,26 ss, 1,29-39, 1,35-38 sobre a geração que morre no deserto; 1,37 Moisés; 1,38 Josué), sem comentar o versículo, exceto o achado e a reserva.
- Belarmino (12 tomos): só Dt 1,39 (achado) e «Deut. 1,11» (nota de passagem, sobre a bênção da multiplicação).
- Newman (523 arquivos do cache do Gênesis): só PPS III, 2.
- Granada (13 tomos), Teresa de Ávila, João da Cruz, Afonso, Teresinha, Santo Antônio: nenhuma citação de Dt 1 nos textos em cache (a «Deut. 1 8» do t. VIII de Granada é Dt 18, erro de OCR). Não procurados em texto integral: João de Ávila, Vicente de Paulo, Foucauld (sem cache).
- **Escrivá**: o índice (`escriva-indice.md`) só tem Dt 6, 10, 25, 30, 31 e 32; **nada em Dt 1**.
- **Liturgia**: o Missal antigo (Divinum Officium) não tem antífona, responsório nem leitura de Dt 1. Dt 1,9-14 só aparece como leitura da Missa de admissão dos candidatos ao diaconato e ao presbiterato (OLM 775.1), sem texto de comentário próprio.

## 3. Reserva (não entrou)
- **Sales, t. VIII, p. 233** (sermão sobre o Benedictus, «testamento»): em latim e francês, só diz que dos filhos de Israel só dois entraram na terra (margem: Dt 1,35-38); fraco e de OCR ruim.
- **Lourenço, vol. IV, p. 197 e outros** (Josué «salvador» que introduz na terra, vol. VI, p. 415; Dt 1,38 em nota): comentário de passagem sobre o nome de Josué.
- Newman, PPS III, 2 tem outro trecho útil (Samuel), fora do capítulo.

## 4. Para outros capítulos
- **Dt 4,20 e 9–10**: Lourenço vol. VI, p. 415 (nota: Ex 13,3; Dt 4,20); Sales t. XXVII indexa Dt 4,13; 4,39; 5,6; 5,15-17; 6,… (ver índice, linhas 13309–13345).
- **Dt 17,12**: Newman PPS III, 2, p. 17 (quem não ouve o sacerdote ou o juiz morrerá).
- **Dt 16,16**: Sales, t. VIII (sermão: «ninguém aparecerá diante de mim de mãos vazias»).
- **Dt 32**: a catequese de João Paulo II sobre o cântico (2002-06-19), no catálogo `modernos.md`.

## 5. Ressalvas
- A varredura dos Papas só acha citações com a sigla («Dt 1,n», «Deut. 1,n»); alusões sem referência passam. Não coberto: documentos do Vaticano II e textos em outras línguas além do it/la.
- Nos caches antigos o `grep` pode ser o alias do ugrep (ignora arquivos): as buscas em Lourenço, Belarmino, Granada e Sales podem ter deixado passar trechos.
- Newman e Francisco: originais tirados do texto do newmanreader e do vatican.va, não de imagem.
