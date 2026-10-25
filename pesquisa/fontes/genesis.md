# Gênesis: mapa das fontes

Primeiro uso: Gn 1 (2026-10-25). **Pré-pesquisa feita: Gn 1–50, 2026-10-25, 745 textos em Gn 3–50** (mais as
pistas `_pistas-*.md` e os `_ausentes-*.md` de cada capítulo; índice em `genesis/<ccc>/BASE.md`). Os textos de Gn 1 estão em `genesis/001/base/` (índice em
`genesis/001/BASE.md`, 67 fontes); os relatórios `genesis/001/relatorio-<grupo>.md` dizem o que se
procurou, o que não existe e onde está cada texto. Para outro capítulo, rodar os scripts abaixo com o
número dele (cada um tem o uso no topo); os cortes por capítulo das obras que comentam o Gênesis inteiro
foram testados só por amostra: conferir. Downloads em `cache/genesis/<grupo>/` (fora do git); um PDF por vez.

## Obras que comentam o Gênesis inteiro (ou um bloco grande)

| autor e obra | cobre | script |
|---|---|---|
| Agostinho, *Confissões* XI–XIII | Gn 1 | `gen-agostinho-confissoes.py` |
| Agostinho, *Sobre o Gênesis contra os maniqueus* I–II | Gn 1–3 | `gen-agostinho-contra-maniqueus.py` |
| Agostinho, *Comentário literal ao Gênesis* (e o *incompleto*) | Gn 1–3 (o incompleto, 1,1–26) | `gen-agostinho-literal.py`, `gen-agostinho-literal-incompleto.py` |
| Agostinho, *Cidade de Deus* XI–XIV (Gn 1–3, livros inteiros) e XV–XVI (Gn 4–49, por capítulo de Agostinho: tabela `CAPS_XV_XVI`) | Gn 1–30, 32, 46, 48–49 | `gen-agostinho-cidade.py 4-50` |
| Agostinho, *Quaestiones in Heptateuchum* I (173 questões, Gn 4,17–50,22) e *Locutiones* I (gramática da Vetus Latina, Gn 1,14–50) | Gn 4–50 (sem questão: 16; sem locução: 5 e 35) | `gen-agostinho-quaestiones.py` |
| Agostinho, *A Trindade* (imagem); *83 questões* 51, 52, 74 | Gn 1,26-27; 6,6 | `gen-agostinho-trindade.py`, `gen-agostinho-83-questoes.py` |
| Ambrósio, *Hexaemeron* (Gn 1–2,2); *De paradiso*; *De Cain et Abel*; *De Noe*; *De Abraham* (12–24), *De Isaac* (21–27), *De Iacob* II (25–49), *De Ioseph* (37–46), *De benedictionibus* (49) | Gn 1–49 | `gen-latinos-ambrosio.py` (os quatro dos patriarcas: tabela `POR_CAPUT`) |
| Beda, *In principium Genesis* (Gn 1–21) | Gn 1–21 | `gen-latinos-beda.py` |
| Ruperto, *De Trinitate et operibus eius: In Genesim* | Gn inteiro | `gen-latinos-ruperto.py` |
| Rábano, Alcuíno, Isidoro, Hugo de São Vítor (compilações e alegorias; pouco próprio) | Gn inteiro | `gen-latinos-rabano.py`, `-alcuino.py`, `-isidoro.py`, `-hugo.py` |
| Jerônimo, *Quaestiones hebraicae in Genesim* | Gn inteiro (por versículos soltos) | `gen-latinos-jeronimo.py` |
| Basílio, *Hexaémeron* 1–9 (Gn 1,1–26); *Sobre a origem do homem* I–II (atribuídas; Gn 1,26–2,7) | Gn 1–2 | `gen-gregos-basilio.py` |
| Gregório de Nissa, *De opificio hominis*, *Apologia in Hexaemeron* | Gn 1–3 | `gen-gregos-nissa.py` |
| Crisóstomo, *Homilias sobre o Gênesis* 1–67 (só o latim da PG: o grego da PG 53 tem OCR ilegível) e *Sermões* 1–9 (grego) | Gn inteiro (cada homilia do seu lema ao da seguinte: tabela `INICIO`) | `gen-gregos-crisostomo.py` |
| Teodoreto, *Quaestiones in Genesin*; Cirilo, *Glaphyra*; Procópio; Damasceno; Severiano; Orígenes (*Homilias*, Rufino) | Gn inteiro (Orígenes, 16 homilias) | `gen-gregos-<autor>.py`, `_gen_gregos.py` |
| Teófilo de Antioquia, *A Autólico* II, 10–32 | Gn 1–11 | `gen-gregos-teofilo.py` |
| Efrém, *Comentário ao Gênesis* (latim de Assemani/Benedetti, 1737, pp. 6–116; a ed. crítica de Tonneau, CSCO 152, tem direito) | Gn 1–50, menos o 36 (33 e 34 num trecho só; 35 só vv. 1–4 e 27–29) | `gen-orientais-efrem.py 3-50` |
| Cornélio a Lápide, *Commentaria in Genesim* (ed. Vivès 1866, t. I; OCR do archive.org, `commentariainscr01lapi`) | Gn 1–50, versículo a versículo | `gen-latinos-lapide.py` |
| Jacó de Sarug, *Hexaémeron* (Bedjan III; sem texto digital: OCR siríaco, ler na imagem) | Gn 1–2,3 | `gen-orientais-corpus.py` (Digital Syriac Corpus) |

## Pistas por capítulo (Gn 3–50)

- `_pistas-modernos.md`: Catecismo (parágrafos cujas notas citam o capítulo), Escrivá (pelo `escriva-indice.md`) e a
  liturgia da Missa (tabelas de Felix Just: lecionário dos EUA = OLM 1981; os cortes do Brasil podem diferir):
  `gen-modernos-pistas.py baixar` e `… 3-50` (não rodar para Gn 1–2, que têm pistas à mão).
- `_pistas-orientais.md`: tabela das citações do capítulo no Digital Syriac Corpus (3-gramas raros da Peshitta), com
  «fora» (Igreja fora da comunhão) e «apócrifo»: `gen-orientais-corpus.py --pistas 3-50`. Só o primeiro passo.
- `_pistas-gregos.md` e `_ausentes-*.md`: os scripts de cada grupo (`gen-gregos-fechar.py`, `gen-latinos-comum.py`,
  `gen-agostinho-quaestiones.py`, `gen-orientais-efrem.py`).
- Ainda não procurados para Gn 3–50 (pista para a pesquisa do capítulo): Agostinho, *Contra Faustum* XII (Noé, a arca) e
  XXII (a moral dos patriarcas: Abraão e Sara, as filhas de Ló, as mulheres de Jacó, Judá e Tamar) e os *Sermões* 2, 4, 5
  (Abraão, Jacó e Esaú); Gregório Magno; a Liturgia das Horas; os siríacos por palavra-chave (`--kw`).

## Achados de Gn 1 por autor (para não repetir excerto)

O `conferir.mjs` recusa excerto repetido. Já publicados em Gn 1: Basílio, *Hex.* 1,2; 2,6; 2,8; 4,6–7; 5,10;
6,1 e *Sobre a origem do homem* I (dois trechos); Agostinho, *Conf.* XI, 12–13; XIII, 5; XIII, 28; *Civ.*
XI, 21; XIX, 15; *Gen. ad litt.* II, 14; *Gen. c. Man.* I, 16; *Sermões* 90 e 241; Ambrósio, *Hex.* I, 9;
III, 11; IV, 8; V, 2; Teófilo II, 15 e 17; Efrém (*Hipácio* IV; *Comentário* sobre 1,28); os outros, um
cada (ver `conteudo/genesis/001.json`). Os achados que ficaram de fora estão nos `achados-*.json` de Gn 1 e
podem servir a Gn 2 (o «Façamos» de Agostinho e de Teófilo, a imagem do domínio de Efrém, Beda sobre os
santos e os animais, as orações bizantinas sobre a imagem).

## Armadilhas

- O «sírio» que Basílio cita sobre Gn 1,2 (o Espírito que choca as águas) **não é Efrém**: no
  *Comentário*, Efrém lê ali o vento, não o Espírito Santo (Assemani I, p. 8). A hipótese corrente é
  Eusébio de Emesa (não conferida).
- O augustinus.it recusa user-agent curto (HTTP 999): os scripts usam um de navegador.
- O Prefácio V dos domingos («De creatione») e a coleta do Natal de 2002 não se acharam em latim na
  internet (pista).
- Edith Stein comenta Gn 1,27-28, mas o alemão não está em fonte aberta.
- Crisóstomo, *Homilias*: o OCR da edição latina de 1859 estropia os títulos («HOMILIA XL. V.», «HNOMILIA XXVI.» = 27,
  «ROMILIA LV.») e a regra antiga achava só 1–41 e com vãos (23, 26–27, 33–35, 38–40 grudadas na anterior); o vol. 54 repete
  uma página (o fim da 43 e o começo da 44: a primeira cópia sai). Os lemas do OCR erram números: «Gen. 25, 5» da hom. 48 é
  23,5; «Gen. 15, 2» da 33 é 13,2; «Gen. 35, 18» da 59 é 33,18. A hom. 16 (2,25–3,7, a queda) está no Gn 2 e no Gn 3.
- Procópio: o `romano()` lia «CAP. Il.» como 49, e os arquivos de Gn 3–48 saíam com o trecho de Gn 2 (e o de Gn 49 com
  Gn 3–49, 1 MB). Corrigido para Gn 3–50 (lista dos títulos lidos à mão); o arquivo de Gn 2 continua dizendo «o trecho
  do OCR cobre Gn 2–48», mas o texto é só o de Gn 2. Procópio trata Gn 39–47 num trecho só; Gn 4, 15, 20 e 29–30 ficam
  no trecho do título anterior. As colunas da PG 87/1 no fim (Gn 39–50) saem iguais (451…491): ler na imagem.
- Ambrósio, *De Abraham*, *De Isaac*, *De Iacob*, *De Ioseph*: o corte pelos lemas não funciona (ele cita o versículo no
  meio do texto): achava só 1 versículo de Gn 13 e dava «não comenta» para Gn 18–25 (Mamre, Sodoma, o sacrifício de
  Isaac, Rebeca). Agora vale a tabela `POR_CAPUT` (capítulos de Migne → capítulos do Gênesis). *De Iacob* I e os caps.
  X–XII do II (os Macabeus) não falam do Gênesis; *De Isaac* é quase todo sobre o Cântico (alegoria).
- Orígenes, fragmentos (`gen-gregos-origenes.py`): o corte pela LXX põe escólio no capítulo errado quando a frase se
  repete (o escólio de Gn 3,21, que cita 2,23 «osso dos meus ossos», caiu em Gn 4 e Gn 29, por causa de 29,14). Conferir.
- Agostinho, *Quaestiones* I: os colchetes variam («[Ib. V, 25.]», «[Ib XXVIII, 18.]», «[In XXV, 1.]», «[Ib. 28, 2.]» com
  o capítulo em arábico); o número da questão fica na linha de cima (a 173.ª, «CLXXIII [Ib. L, 22.]», na mesma linha).
  A q. 108 (33,5 e 34,25) e a 122 (35,29 e 37,2) vão aos dois capítulos. CSEL: *Quaestiones* 28/2 (1895), *Locutiones*
  28/1 (1894).
- Efrém (`gen-orientais-efrem.py`): o OCR perde a inicial decorada de cada seção («Ixitque» = Dixitque, «Rat autem» =
  Erat, «YOA hac» = Post haec), e as notas de margem «CAP. XII.» vêm noutra página: os cortes seguem o lema que Efrém
  cita. Três cortes caem no meio de um parágrafo (8,3; 28,1; 30,1). Página impressa = folha − 20 até n136; dali em
  diante (n136 ss.) vêm a vida de Moisés e as *Collectanea* de Jacó de Edessa, que não são de Efrém.
- Lápide: 50 «SYNOPSIS CAPITIS» antes do Êxodo, mais a «Synopsis historiae et chronologiae totius Geneseos» (fica de
  fora). As folhas do archive.org não seguem as páginas (lâminas e folhas em branco): a folha de cada capítulo vem do hOCR.
- Catecismo: o cache antigo (`cache/base/modernos/catecismo/`) não existe no Ubuntu; o novo é
  `cache/genesis/modernos/catecismo/`. Notas sem ponto na última página («2 Cf. Mt 6, 9-13»), «Gn 18. 14», hífen U+2011;
  o § 2260 traz «Gn 9, 5-61» (marcado [sic]).
- Liturgia: em `cache/genesis/modernos/liturgia/`, seis arquivos de 867 bytes são páginas 404 (1970USL-Saints,
  1998USL-Lent-Easter, 1998USL-Saints, 1998USL-VariousNeeds, 2002USL-Masses-VariousNeeds, 2002USL-VariousNeeds);
  os bons são `Index-Sundays.htm`, `Index-Weekdays.htm` e os `2002USL-Masses-*.htm`.
- Escrivá: o `mod-escriva.py pistas` não aceita o Gênesis e o cache dele não existe aqui; as pistas de Gn 3–50 vêm só
  do `escriva-indice.md` (sem as citações sem referência).
