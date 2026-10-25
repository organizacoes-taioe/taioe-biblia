# Gênesis: mapa das fontes

Primeiro uso: Gn 1 (2026-10-25). Os textos de Gn 1 estão em `genesis/001/base/` (índice em
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
| Agostinho, *Cidade de Deus* XI–XIV | Gn 1–3 | `gen-agostinho-cidade.py` |
| Agostinho, *A Trindade* (imagem); *83 questões* 51, 52, 74 | Gn 1,26-27; 6,6 | `gen-agostinho-trindade.py`, `gen-agostinho-83-questoes.py` |
| Ambrósio, *Hexaemeron* (Gn 1–2,2); *De paradiso*; *De Cain et Abel*; *De Noe*; *De Abraham*… | Gn 1–2,2 e outros | `gen-latinos-ambrosio.py` |
| Beda, *In principium Genesis* (Gn 1–21) | Gn 1–21 | `gen-latinos-beda.py` |
| Ruperto, *De Trinitate et operibus eius: In Genesim* | Gn inteiro | `gen-latinos-ruperto.py` |
| Rábano, Alcuíno, Isidoro, Hugo de São Vítor (compilações e alegorias; pouco próprio) | Gn inteiro | `gen-latinos-rabano.py`, `-alcuino.py`, `-isidoro.py`, `-hugo.py` |
| Jerônimo, *Quaestiones hebraicae in Genesim* | Gn inteiro (por versículos soltos) | `gen-latinos-jeronimo.py` |
| Basílio, *Hexaémeron* 1–9 (Gn 1,1–26); *Sobre a origem do homem* I–II (atribuídas; Gn 1,26–2,7) | Gn 1–2 | `gen-gregos-basilio.py` |
| Gregório de Nissa, *De opificio hominis*, *Apologia in Hexaemeron* | Gn 1–3 | `gen-gregos-nissa.py` |
| Crisóstomo, *Homilias sobre o Gênesis* 1–67 (só o latim da PG: o grego da PG 53 tem OCR ilegível) e *Sermões* 1–9 (grego) | Gn inteiro | `gen-gregos-crisostomo.py` |
| Teodoreto, *Quaestiones in Genesin*; Cirilo, *Glaphyra*; Procópio; Damasceno; Severiano; Orígenes (*Homilias*, Rufino) | Gn inteiro (Orígenes, 16 homilias) | `gen-gregos-<autor>.py`, `_gen_gregos.py` |
| Teófilo de Antioquia, *A Autólico* II, 10–32 | Gn 1–11 | `gen-gregos-teofilo.py` |
| Efrém, *Comentário ao Gênesis* (latim de Assemani/Benedetti, 1737; a ed. crítica de Tonneau, CSCO 152, tem direito) | Gn inteiro (âncoras só no cap. 1: `--ver` ajuda) | `gen-orientais-efrem.py` |
| Jacó de Sarug, *Hexaémeron* (Bedjan III; sem texto digital: OCR siríaco, ler na imagem) | Gn 1–2,3 | `gen-orientais-corpus.py` (Digital Syriac Corpus) |

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
