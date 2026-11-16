# Salmo 41 (40): relatório da pesquisa geral (Padres, medievais, gregos, modernos)

Pesquisa de 2026-11-15 (pesquisador p40, lote dos Sl 38–47). Todos os grupos juntos, a partir de `base/`.
Resultado: **25 excertos** em `achados-geral.json` (16 de relevância 3, 9 de relevância 2), de 10 autores, cobrindo os vv. 2–7 e 9–14.
Textos novos guardados em `textos/`.

## Numeração

- O título é o v. 1; os versículos dos Padres são um a menos (Vulgata v. 1 = «Beatus qui intelligit» = v. 2 nosso). Cassiodoro divide o v. 7 em dois
  (Vers. 6 e 7); a partir do v. 8 os dois sistemas coincidem em Cassiodoro («Vers. 10» = v. 10).
- Agostinho, Ambrósio e Tomás numeram por parágrafos; Ambrósio repete o número 36 (o segundo é o n. 39).

## O que se achou

| autor | obra e passagem | excertos |
|---|---|---|
| Santo Agostinho | *Enarrationes* n. 3, 6, 10, 13 (PL 36), n. 1 (v. 6) e *In Ioh.* tr. 59 | 6 |
| São Tomás de Aquino | *Postilla* n. 1, 3 (duas vezes), 4, 9 | 5 |
| Santo Ambrósio | *Enarrationes* n. 4, 13, 14, 24, 37 | 5 |
| Teodoreto de Ciro | *Interpretatio*, vv. 2 e 10 | 2 |
| São Bruno de Segni | *Expositio*, vv. 10 e 13 | 2 |
| Cassiodoro | *Expositio*, Vers. 13 | 1 |
| Santo Atanásio | *Exposições* (cadeia), v. 2 | 1 |
| São Cirilo de Alexandria | *Expositio*, v. 11 | 1 |
| São João Crisóstomo | *In Ioh.* hom. 70, sobre Jo 13,18 | 1 |
| São João Paulo II | catequese de 02/06/2004 (citação curta) | 1 |

Por versículo:
- v. 2: Ambrósio (penetrar o sentido da pobreza de Cristo, ponto por ponto), Teodoreto (a manjedoura), Tomás (socorrer antes de pedirem), Atanásio (Deus como devedor de quem dá aos pobres).
- v. 3: Agostinho (um só Senhor para esta vida e a outra).
- v. 4: Tomás (o febril que se revira no leito) e Ambrósio (Cristo como lutador que se vira).
- v. 5: Agostinho (o médico que corta; não culpar o destino), Tomás («pequei contra ti», só Deus perdoa), Ambrósio («a ferida procura o médico»).
- v. 6: Agostinho (o nome de Cristo é semente).
- v. 7: Tomás (abelhas e escaravelhos).
- v. 9: Agostinho (o que dorme ressurgirá; Adão e a Igreja do lado).
- v. 10 (Jo 13,18): Agostinho *In Ioh.* 59 (o pão do Senhor contra o Senhor), Crisóstomo *In Ioh.* 70 (a paciência de Jesus), Ambrósio (o calcanhar do lutador), Teodoreto (o calcanhar é o dolo), Bruno de Segni («Ai de ti, Judas»), João Paulo II (o amigo, «o homem da paz»).
- v. 11: Cirilo (Cristo pede misericórdia e ressurreição para nós).
- v. 12: Agostinho (não desceu da cruz).
- v. 13: Cassiodoro (rogou pelos inimigos) e Bruno de Segni (a força da inocência).
- v. 14: Tomás (bendizer é dizer o bem) e Ambrósio (fim do primeiro livro do saltério).

## Como se procurou

- Tudo o que está em `base/` foi lido (Agostinho, Ambrósio, Cassiodoro, Tomás, Teodoreto, Atanásio, Cirilo, Bruno de Segni, Belarmino; os demais por amostragem).
- Extração dos `original` por script, como no Sl 40 (substring exata; NFC no grego; sem marcas de coluna, asteriscos nem números de página). Correções declaradas:
  Agostinho *In Ioh.* 59, sem as chamadas de nota «2» e «4»; Ambrósio, sem o número de página `872`.
- Fora de `base/`, baixados: Agostinho, *In Evangelium Ioannis tractatus* 59 (augustinus.it); Crisóstomo, *In Joannem* hom. 70 (khazarzar, PG 59, 387–388);
  João Paulo II, audiência geral de 02/06/2004 (vatican.va, em italiano; não guardada, só as duas frases citadas).

## O que não existe ou não se achou

- Escrivá, Catecismo, Papas recentes: nada; só a catequese de João Paulo II de 2004 (ver pista).
- Basílio, Crisóstomo (Salmos), Gregório de Nissa e Hilário não comentaram este salmo.
- Orientais: Afraates, *Demonstração* 21 (v. 9) está em `base/` em siríaco, sem tradução; não entrou. Liber Graduum, Jacó de Sarug e Isho`dad: só pistas.
- Liturgia (`base/liturgia.md`): o Sl 41 é o responsorial do 7º domingo do Tempo Comum (B) e o intróito de São Paulo da Cruz e de São Camilo de Lélis (Missal antigo): sem comentário de Padre a acrescentar.

## Avisos para a seleção

- **Agostinho** passaria de um quarto se entrassem os dois excertos em reserva (n. 1, v. 2: «onde se te expõe a fraqueza, ali se esconde a divindade»; n. 5, v. 4: o viajante não ama a estalagem como se fosse a casa): ficaram de fora, só em `d41.py` do pesquisador (`/home/geremias/.cache/taioe-sl38-47/p40/`). São muito bons.
- **Atanásio**: a *Hypothesis* e as glosas desta cadeia têm autoria incerta (PG 27); a glosa do v. 2 (Deus devedor) tem a ideia de Pr 19,17 e Mt 25,40.
- **João Paulo II**: `direitos: citação curta`, só 2 frases, em italiano; a tradução é nossa.
- Há quatro leituras do «calcanhar» (Ambrósio, Teodoreto, João Paulo II, Bruno): não é preciso ficar com todas.
- O v. 8 (susurrabant), o v. 11 em Agostinho e os vv. 12–13 em Ambrósio têm material em `base/`, mas repetem Agostinho ou Cassiodoro.

## Para outros capítulos

- Ambrósio, n. 37, sobre as divisões do saltério em cinco livros, vale para os Sl 71, 88 e 105 (fins dos livros II a IV).
- Agostinho, n. 12 (a cidade de Jerusalém depois da paixão) e n. 14 (o Deus de Israel; o povo maior servirá ao menor) são úteis em Rm 9–11.
- Ambrósio, n. 25–31 (Dan e o cavalo mordido no calcanhar, Gn 49,16-17): Gênesis 49.
