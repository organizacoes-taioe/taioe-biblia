# Gênesis 2: relatório da pesquisa nos orientais não gregos e na liturgia oriental

Pesquisa de 2026-10-25. **16 achados** em `achados-orientais.json` (trecho 1: 4; trecho 2: 2; trecho 3: 4; trecho 4: 6).
Textos novos em `base/` (cabeçalho do `COMO-PESQUISAR.md`), gravados por `pesquisa/ferramentas/base/ori-genesis-gravar.py 2`
(script novo; o `gen-orientais-gravar.py` não foi tocado): `afraates-demonstracao-13.md`, `efrem-contra-marciao.md`,
`efrem-hinos-paraiso.md`, `jaco-de-sarug-veu-de-moises.md`, `liber-graduum-memra-15.md`, `triodio-1876-sabado-santo.md`,
`eucologio-1862-matrimonio.md`; mais `_pistas-orientais.md` e `_ausentes-orientais.md`. Já estavam em base:
`efrem-comentario-genesis.md` (aqui) e, em `../001/base/`, `efrem-hino-natividade-26.md` e `afraates-demonstracao-6.md`.

## Onde se procurou

- **Efrém, Comentário ao Gênesis** (Assemani I, p. 20–27): cada trecho usado foi conferido na imagem (p. 20, 22, 23, 24, 25,
  26). O latim de Benedetti confere com o OCR, que só erra letras; o siríaco ao lado (serto miúdo) não foi transcrito.
- **Efrém, Hinos sobre o Paraíso**: a edição romana (Assemani III, Roma 1743, p. 562–598) traz os hinos 1–12 com latim em
  prosa (paráfrase); lidos pelo OCR e conferidos na imagem os trechos usados (p. 569, 597, 598). Beck (CSCO 174) tem direito.
  Page/n = p. + 76.
- **Digital Syriac Corpus**: `gen-orientais-corpus.py 2` (78 blocos) e `--kw` (ܥܠܥܐ, ܥܪܛܠܝ, ܠܒܘܫܐ ܕܫܘܒܚܐ, Eva junto de «lado»):
  Afraates (Dem. 6, 8, 11, 13, 14, 18, 22, 23), *Liber Graduum* (memre 15, 21, 28), Efrém (Contra Marcião; Natividade 26),
  Tito de Bostra, e os proibidos (Narsai, Timóteo II, bar Salibi, Moisés bar Kepha).
- **Jacó de Sarug, Bedjan III**: OCR do archive.org só para achar as páginas (o índice do OCR está uma folha adiante da imagem:
  OCR n = folha + 1). Achados o 7º dia do Hexaémeron (p. 138) e o memra 79, «Sobre os véus no rosto de Moisés» (p. 283–305),
  que lê Gn 2,21-24 em Cristo e na Igreja. A p. 299 foi **lida na imagem e transcrita sem vogais** (conferir antes de publicar,
  sobretudo «ܘܬܪܥܘܗܝ ܠܓܒܗ», linha 14).
- **Liturgia bizantina**: AGES (cache), conferido no Triódio de Veneza (1876, p. 411) e no Eucológio de Veneza (1862, p. 246).
- **Parisot** (Afraates) e **Kmosko** (*Liber Graduum*, PS I/3, OCR baixado para o cache) para as colunas; **Mitchell II**
  (1921, reimpressão no archive.org `cu31924092341670`) para Contra Marcião: o siríaco é paginado da direita para a
  esquerda (p. 61 = page/n375).
- Não procurados nesta rodada: Narek, Nerses (além de Gn 1), coptas, etíopes, *Apophthegmata*, Pseudo-Macário, Romano, os
  *Hinos sobre a fé* e o comentário ao *Diatessaron* de Efrém (ver `_pistas-orientais.md`).

## Achados (16)

| # | id | autor, obra, onde | vv. | rel. | nota |
|---|---|---|---|---|---|
| 1 | `efrem-coment-gn-2-2-deus-nao-se-cansa` | Efrém, Comentário, Assemani I, p. 20 (latim) | 1–3 | 2 | **Diz o que Agostinho diz no Sermão 125, 4** (grupo agostinho): quem fez tudo pela palavra não se cansa. O próprio de Efrém: Moisés e Josué não se cansaram dando ordens ao mar e aos astros. Fica um dos dois |
| 2 | `efrem-hino-nat-26-10-o-sabado-dos-cansados` | Efrém, Natividade 26, estr. 10 (siríaco, Beck pelo corpus; Lamy II) | 2–3 | 3 | O sábado como cuidado de Deus pelos cansados, homens e animais; o Senhor do sábado se faz escravo para quebrar o jugo |
| 3 | `afraates-dem-13-13-o-sabado-de-deus` | Afraates, Dem. 13, 13 (siríaco; Parisot col. 569–574) | 2–3 | 2 | O sábado que agrada a Deus é fazer a sua vontade; entrar no sábado em que o céu e a terra descansam (Hb 4,9). Parecido com Agostinho, *Conf.* XIII e *Civ.* XXII, 30, mas com o lado moral (o sábado não serve aos maus) |
| 4 | `liturgia-sabado-santo-o-sabado-abencoado` | Triódio, Sábado Santo, Matinas, «Glória» dos Louvores (grego, Veneza 1876, p. 411) | 2–3 | 3 | **Diz o que Beda diz** (grupo latinos, `beda-hexaemeron-1-gn2-3-o-sabado-no-sepulcro`): o sétimo dia, figura do sábado de Cristo no sepulcro. A liturgia cita Gn 2,3 palavra por palavra; fica um dos dois |
| 5 | `efrem-coment-gn-2-7-as-maos-e-o-sopro` | Efrém, Comentário, p. 22 (latim) | 7 | 2 | Os animais também têm corpo e alma; o homem, modelado pelas mãos e animado pelo sopro, recebe domínio, razão e «senso de Deus». Toca Tertuliano (latinos) nas mãos; o próprio é o contraste com os animais |
| 6 | `afraates-dem-6-14-alma-vivente-e-espirito` | Afraates, Dem. 6, 14 (siríaco; col. 293–294) | 7 | 2 | «Alma vivente», primeiro nascimento; o Espírito Santo, no segundo, o batismo (cf. 1Cor 15,45). Cortei a frase sobre a imortalidade do espírito natural (Parisot e NPNF a leem ao contrário) e o que segue, a tese de Afraates sobre o espírito que «dorme» com o corpo |
| 7 | `efrem-coment-gn-2-15-guardar-o-mandamento` | Efrém, Comentário, p. 23 (latim) | 15 | 2 | «Cultivar e guardar» = guardar o mandamento (o paraíso não tinha espinhos nem ladrões); termina admitindo também o trabalho. Contraponto a Agostinho, *Gen. ad litt.* VIII, 8 e 10 |
| 8 | `efrem-coment-gn-2-17-o-preceito-leve` | Efrém, Comentário, p. 23–24 (latim) | 16–17 | 3 | O jardim inteiro dado, uma só árvore proibida: não foi a necessidade, foi o desprezo; o medo, «de sentinela» junto da árvore. Perto de Gregório, *Moralia* 35 (obediência) e Ambrósio (o bom médico), mas diz outra coisa |
| 9 | `efrem-paraiso-12-os-frutos-antes-do-tempo` | Efrém, Hinos sobre o Paraíso XII, Assemani III, p. 597–598 (latim) | 9, 16–17 | 3 | A árvore não era má: o fruto, colhido maduro, seria de vida; Adão o colheu verde. As duas árvores, vida sem morte e sabedoria sem erro. **Teófilo, *Ad Autolycum* II, 25** (grupo gregos, se vier) diz algo parecido (Adão ainda criança): ver qual é o mais claro |
| 10 | `efrem-marciao-1-a-morte-adiada` | Efrém, Contra Marcião I (siríaco; Mitchell II, p. 60–61) | 17 | 2 | A ameaça era advertência de amor; Deus temperou a justiça: Adão viveu 930 anos e agora vive na vida eterna. Outra resposta ao «no mesmo dia» que a de Agostinho, *Civ.* XIII, 15 (a morte da alma) |
| 11 | `efrem-coment-gn-2-19-os-animais-como-rebanho` | Efrém, Comentário, p. 24–25 (latim) | 19–20 | 3 | Os animais vêm como rebanho ao pastor, feras na frente e mansos atrás, sem medo; acertar cada nome foi dom de Deus |
| 12 | `efrem-coment-gn-2-23-um-e-dois` | Efrém, Comentário, p. 25–26 (latim) | 21–23 | 2 | «Adão era um e era dois»; «esta, agora»: não tirada do solo como os animais |
| 13 | `jaco-sarug-veu-moises-o-lado-do-esposo` | Jacó de Sarug, memra 79, Bedjan III, p. 299 (siríaco, transcrito da imagem) | 21–22 | 2 | O sono de Adão e o lado de Cristo. **O tema já tem três** nos outros grupos (Agostinho, *Tract. in Io.* 120, 2; Tertuliano, *De anima* 43; Bernardo). O próprio de Jacó: Eva, mãe dos viventes em figura, e o batismo, mãe da vida |
| 14 | `liturgia-matrimonio-que-o-homem-nao-esteja-so` | Eucológio, coroação, 3ª oração (grego, Veneza 1862, p. 246) | 7, 18, 21–22, 24 | 3 | «Coroa-os numa só carne». **O grupo modernos traz a bênção nupcial do Missal de 1570**, que reza o mesmo trecho: se o tema da liturgia for um só, ficam as duas lado a lado ou uma delas |
| 15 | `efrem-coment-gn-2-25-a-veste-de-gloria` | Efrém, Comentário, p. 26 (latim) | 25 | 3 | A veste de glória; não eram crianças. **Agostinho, *Civ.* XIV, 17** («vestia-os a graça») e **Ambrósio** («vestidos de virtudes») dizem algo próximo; Efrém é a forma clássica da imagem |
| 16 | `liber-graduum-15-3-nus-como-criancas` | *Liber Graduum*, memra 15, 3 (siríaco; Kmosko col. 339–342) | 25 | 2 | Nus como as crianças de peito, porque o coração era puro; Mt 18,3. Corte feito para deixar de fora a tese da obra (o desejo conjugal só depois do pecado) |

Os três mais fortes: o preceito leve de Efrém (8), o hino do Sábado Santo (4) e os frutos colhidos antes do tempo (9); logo
depois, os animais como rebanho (11), a veste de glória (15) e a oração do matrimônio (14).

Efrém tem 10 dos 16: é o único oriental com comentário corrido de Gn 2 em domínio público, e os trechos dizem coisas
diferentes. Se for preciso cortar: 1 (repete Agostinho), 12 e 13 (tema cheio) primeiro.

## Para a conversa principal

- **Autores para `ferramentas/autores.json`**: «Liber Graduum (Livro dos Degraus)» é novo (`autor_id` `liber-graduum`;
  «sobre» sugerido: «obra ascética siríaca anônima (séc. IV–V), sobre os degraus da vida cristã»); já foi proposto em 2Cor 3
  e Nm 17, mas não entrou. «Liturgia bizantina» existe com «sobre» das exéquias: generalizar («a liturgia das Igrejas de rito
  bizantino, rezada também nas Igrejas católicas orientais»), como pedia o relatório de Gn 1. «Santo Efrém, o Sírio»,
  «Afraates, o Sábio Persa» e «São Jacó de Sarug» já existem.
- **Siríaco a conferir antes de publicar**: a transcrição de Jacó (p. 299) foi lida na imagem, sem vogais. No hino 26, «ܦܟܐ
  [ܕܥܒܕܗ]» (a bofetada «do seu servo») tem o complemento entre colchetes de Beck; a tradução o segue. Em Contra Marcião, o
  palimpsesto tem lacunas (* * *): a tradução diz só o que se lê.
- **Latim de Benedetti e de Assemani**: é tradução livre do siríaco (o dos Hinos sobre o Paraíso é paráfrase em prosa de
  versos). Os trechos foram conferidos na imagem; o sentido confere com o que se sabe do siríaco (a «veste de glória», p. 26;
  «guardar a lei», p. 23), mas o siríaco da página não foi lido. Na mesma linha do Gn 1, o `original` é o latim.
- **Direitos**: tudo em domínio público. O siríaco de Natividade 26 vem da edição de Beck pelo Digital Syriac Corpus (CC BY),
  como nos capítulos anteriores; o hino está também em Lamy II (1886).

## Armadilhas

- OCR de Bedjan III: o índice das páginas (`b3_pageindex`) está uma folha à frente da imagem (OCR n158 = folha n157 = p. 138);
  a regra da imagem continua page/n = p. + 19. Os algarismos das páginas no OCR erram («188» por 138).
- Mitchell II: o siríaco é paginado da direita para a esquerda (folha 372 = p. 64, 373 = p. 63, 374 = p. 62).
- O OCR do Assemani III usa o «s» longo: buscar «Paradif», «fcienti».
- Afraates, Dem. 6, 14: «ܘܠܐ ܡܝܘܬܬܐ ܬܘܒ ܐܝܬܝܗ», sobre o espírito natural, Parisot traduz «nunca morre» e NPNF «não é imortal»;
  por isso a frase ficou fora do corte.

## Para outros capítulos

- **Gn 3**: Efrém, Contra Marcião I (Adão 930 anos fora da cerca da árvore da vida; nenhum «outro deus» pôde fazê-lo entrar);
  Efrém, Hinos sobre o Paraíso III (a serpente sabe por Eva o que é o paraíso; os olhos abertos e fechados; Ozias e Adão, XII);
  *Liber Graduum*, memre 15 e 21 (o desejo e a árvore); Afraates, Dem. 22, 1 (a morte reinou pela transgressão); o Triódio do
  Domingo do Perdão (Adão diante do paraíso).
- **Gn 4–6**: Efrém, Hinos sobre o Paraíso (pelo prefácio de Assemani: os filhos de Set no alto, os de Caim na terra de Nod);
  Afraates, Dem. 18, 9 (os filhos de Set e as filhas de Caim) e Dem. 13, 5–7 (Noé só casou aos 500 anos, para não se misturar
  com a raça de Caim; Gn 5,32; 6,9).
