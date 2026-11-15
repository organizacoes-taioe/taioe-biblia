# Números 25: relatório da pesquisa nos Padres gregos e bizantinos

Pesquisa de 2026-11-15. Resultado: **12 achados** em `achados-gregos.json` (trecho 1, vv. 1–5: 5; trecho 2, vv. 6–15: 6; trecho 3, vv. 16–18: 1;
relevância 3: 4, relevância 2: 8). Direitos: 11 «domínio público» (Teodoreto e Nissa com o texto equivalente ao da PG, embora o PDF siga a
edição moderna); Teodoro Estudita, «citação curta» (ed. Fatouros, 1992). Nenhum autor novo: todos já estão em `ferramentas/autores.json`
(ids usados: `teodoreto`, `cirilo`, `crisostomo`, `nissa`, `nazianzeno`, `maximo-confessor`, `nilo` = São Nilo de Ancira, `teodoro-estudita`, `basilio`).
Originais novos em `textos/` (7 arquivos); os de `base/` (Teodoreto q. 44, Cirilo, Nissa) não foram copiados.

## O que entrou (uma linha cada)

- **Trecho 1 (vv. 1–5)**
  - Teodoreto, *Quaest. in Num.* 44: Balaão, que não pôde amaldiçoar, aconselha os madianitas a armar as mulheres; a beleza e as palavras
    são as armas, para levar o povo à impiedade e privá-lo do socorro de Deus (vv. 1–3) (3).
  - Cirilo, *De ador.* XIV (PG 68, 908): o prazer desregrado força à apostasia; os chefes expostos «diante do sol» dizem que ninguém
    escapa ao olhar do juiz (vv. 1–4) (2).
  - Crisóstomo, *In 1 Cor.* hom. 23 (PG 61, 193): o mal nasce da fartura e da gula; a praga dos vinte e três mil foi a maior, porque as
    mulheres vieram por conselho de Balaão (vv. 1–3) (3).
  - Teodoreto, *In Os.* 9,10 (PG 81, 1601–1604): Deus achou Israel como uvas no deserto; o povo preferiu Beelfegor e só colheu vergonha (v. 3) (2).
  - Nissa, *Vida de Moisés* II, 298–299 e 303: os vencedores de todas as armas foram vencidos pelo prazer; a lição é afastar a vida da
    vizinhança do mal (vv. 1–3) (3).
- **Trecho 2 (vv. 6–15)**
  - Crisóstomo, *In Kalendas* 6 (PG 48, 961–962): o homicídio de Fineias, feito por Deus e para poupar os demais, trouxe justiça; o médico que
    corta o membro podre (vv. 7–8, 11) (2).
  - Nazianzeno, *Or.* 16, 9 (PG 35, 961–964): «sê para mim, hoje, um Moisés ou um Fineias»: pôr-se diante de Deus pelo povo e deter a praga
    pela intercessão (vv. 8, 11, 13) (3).
  - Máximo, *Ambigua* 67 (PG 91, 1201–1204): a lança de Fineias é a palavra do sumo sacerdote que mata na alma o prazer e o pensamento que o
    acolhe; os nomes Cozbi («minha cócega») e Zambri («meu canto») (vv. 7–8, 14–15) (2).
  - Nilo, *Carta* II, 142 (PG 79, 264–265): as filhas de Madiã são os pensamentos vergonhosos; contra o adultério interior, é preciso Fineias,
    a palavra do sacerdote com a lança do ensinamento temível (vv. 6–8, 14–15) (3).
  - Teodoro Estudita, *Carta* 48: milhares caíam e só Fineias se levantou; se tivesse temido o que tantos faziam, o mal não teria parado (vv. 7–8, 11) (2).
  - Basílio, *Hom. no tempo de fome e seca* (PG 31, 316): o pecado de um (Acã, Zambri) fere todo o povo; a calamidade é pedagogo que lembra a
    cada um o seu pecado (vv. 6, 9) (2).
- **Trecho 3 (vv. 16–18)**
  - Cirilo, *De ador.* III (PG 68, 321–324): os madianitas, sabendo que a juventude não está segura diante do prazer, enviaram moças enfeitadas;
    por isso Deus mandou a guerra (vv. 16–18) (2).

## Atenção na seleção (sobreposições)

- **Fineias com a lança**: Nilo, Máximo e Nissa (II, 300) dizem a leitura interior; Nilo é o mais claro e curto (relevância 3), Máximo é mais
  técnico (se for preciso cortar, sai Máximo). Crisóstomo (*Kalendas*) e Teodoro Estudita tratam do ato; Nazianzeno, da intercessão.
- **As mulheres como arma**: Teodoreto q. 44 (T1) e Cirilo III (T3) dizem o mesmo plano; no T3 o ponto de Cirilo é a guerra como resposta
  (a citação de Nm 31,2 vem no fim). Se o T3 parecer forçado, sai o Cirilo III.
- **Crisóstomo, *Kalendas* 6** justifica a morte dos culpados de modo bem direto; ficou por causa do critério («por Deus, para poupar os
  demais») e da imagem do médico. Pode sair, sem perda, a favor de Nazianzeno e Nilo.
- **Máximo** é a única alegoria por nomes (etimologia de Cozbi e Zambri, segundo Orígenes/Fílon via Máximo); o `original` corta a parte
  filosófica (forma e matéria).

## Onde se procurou

- Corpus já convertido (`cache/genesis/gregos/corpus4`, 911 obras do khazarzar; `cache/numeros20-gregos/txt`; scripts em
  `/home/geremias/.cache/taioe-nm25/gregos/`: `busca.py`, `ver.py`, `ext.py`): padrões sem acento «βεελφεγ», «φογωρ», «φινεε», «ζαμβρι» em todo o corpus
  (70 e 100+ ocorrências, lidas por obra).
- Imagens da PG 79 no archive.org (`…1860_79`, páginas n129–n132) para Nilo, o OCR sendo ilegível.
- Os originais foram conferidos letra a letra contra os textos-fonte (script de comparação só de letras, sem acento nem pontuação). Falha só em
  Máximo (correção de um erro de digitação da fonte, ver Cuidados) e Nilo (lido na imagem).

## O que não existe ou não se achou

- **São Teodoro Estudita, «o grande Fineias»** (PG 99, página n369 do volume): o texto digital do khazarzar só tem as *Epistulae* (ed. Fatouros),
  que não trazem essa frase (busca por «μέγας Φινεές»: zero); o OCR do volume no archive.org (`bim_…_1860_99`) é ilegível. Não conferido: ficou só a
  Carta 48.
- **São Nilo, *Peristeria*** (a pista do Nm 15): a passagem achada é a *Carta* II, 142; a *Peristeria* não está no corpus.
- **Padres do deserto (*Apotegmas*, Poimen, Doroteu, Clímaco), Isidoro de Pelúsio**: não estão no khazarzar; não consultados.
- **Eusébio** (*Dem. ev.* IX, 1, 6; *In Ps.* 105, PG 23, 1316), **Atanásio** (*In Ps.* 105: «Fineias... ao matar a madianita com o fornicário»),
  **Epifânio** e **Orígenes** (*In Jo.* VI): só citações curtas ou resumo da história.
- **Procópio** (PG 87/1, c. 874, em `base/`): o latim de Clauser traz um bom parágrafo sobre Fineias («o zelo de Deus o moveu e obteve a vontade
  divina», o sacerdócio), mas está em latim e a transcrição do grego exige a imagem; não entrou (os mesmos pensamentos estão em Crisóstomo e Teodoreto).
- **Gregório de Nissa, *In diem luminum*** (PG 46): o pecado morto pelo batismo como o fornicário pelo zelo de Fineias; só alusão.

## Cuidados

- **Máximo**: o `original` traz «ἀγανακτήσεως», e a fonte digital «ἀναγακτήσεως» (erro de digitação); os acentos do texto da fonte (só agudos) foram
  mantidos. A numeração «Ambigua 67» é a do texto digital («ΞΖ (67)»); as colunas 1201–1204 vêm dos marcadores =1201= e =1204=.
- **Nilo**: «Μαδινέοι» está assim impresso; a lacuna da edição («τὸν …….») virou [...]. Link: página n131 (a carta começa no fim da coluna 264, continua em 265).
- **Teodoro Estudita**: o número da carta (48) foi tirado do marcador do texto digital, que não traz a coluna da PG; conferir na ed. Fatouros.
- **Crisóstomo, hom. 23 sobre 1Cor**: não se conferiu se o trecho está no § 3 ou no § 4 da homilia.
- **Nomes**: «Beelfegor» nas citações do salmo e de Oseias, «Fogor» nas de Nm 31 (Teodoreto, Crisóstomo), como o nosso texto, que também usa «Baal-Fogor».
  «Fineias», «Zambri», «Cozbi», «Madiã», «madianitas», «Setim», «Moab» como o nosso texto.

## Para outros capítulos

- **Nm 26–31**: Cirilo, *De ador.* PG 68, 325–328 (o Fineias de Nm 31,6 como figura de Cristo, com os vasos santos e as trombetas; Moisés repreende os
  que pouparam as mulheres; o terceiro e o sétimo dia, PG 68, 328–329).
- **Nm 31,16** (conselho de Balaão): Crisóstomo, *In 1 Cor.* hom. 23 (já usado aqui); *Ad Stagirium* (PG 47, 477: depois das bênçãos de Balaão, ou antes, de
  Deus, o povo caiu de novo; Moisés manda matar «como se, numa ferida cortada e queimada, ordenassem cortar e queimar de novo»).
- **Zelo sem ira**: Crisóstomo, *In Acta* (PG 60, 139): «Fineias matou, e não se irou»; Basílio, *Hom. contra os irados* (PG 31, 368: Fineias, tão
  manso, usou a ira como devia contra os fornicários; «seja a tua ira só contra a serpente»); Nazianzeno, *Ep.* 77, 7 (Fineias elogiado por matar, mas
  mais ainda por interceder); Nazianzeno, *De pauperum amore* (PG 35, 861: «o zelo é bom, e o testemunha Fineias»); Basílio, *In ebriosos* (PG 31, 464:
  separai-vos dos que se recusam à correção, e recebereis o prêmio do zelo de Fineias).
- **A ordem e o sacerdócio**: Crisóstomo, *Adv. Iud.* (PG 48, 874) e *In Mt.* (PG 57, 262): Fineias, que matou, foi honrado com o sacerdócio;
  Crisóstomo, *De sacerdotio* III (diz que não se pode chamar Fineias de homicida).
- **Dt 7,3-4**: Cirilo, *De ador.* (PG 68, 517: as moças de Madiã e a proibição de casar com estrangeiros).
- **Sl 105 (106)**: Teodoreto, *In Ps.* 105 (PG 80, 1729–1732: «sacrifícios de mortos» são as libações que os gregos fazem aos mortos; Fineias,
  «o seu zelo Deus aceitou»).
