# Gênesis 1: relatório do grupo agostinho (2026-10-25)

Santo Agostinho em toda a obra. Primeiro capítulo do Gênesis: a pré-pesquisa foi feita agora (sete obras
cortadas em `base/`, scripts reaproveitáveis em `pesquisa/ferramentas/base/gen-agostinho-*.py`), e a pesquisa
partiu dela e dos sermões, das *Enarrationes*, dos *Tratados sobre João* e das cartas. **20 achados** em
`achados-agostinho.json`: trecho 1 = 6, trecho 2 = 3, trecho 3 = 2, trecho 4 = 2, trecho 5 = 7.

## O que se procurou e onde

| obra | onde (Gn 1) | situação |
|---|---|---|
| *Confessiones* XI–XIII | XI (Gn 1,1 e o tempo), XII (Gn 1,1-2), XIII, 1–49 (os seis dias como a Igreja) | `base/agostinho-confissoes.md`; 5 achados |
| *De Genesi contra Manichaeos* I | I, 1, 1 – 21, 32 | `base/agostinho-de-genesi-contra-manichaeos.md`; 2 achados |
| *De Genesi ad litteram imperfectus liber* | inteiro (Gn 1,1-26) | `base/agostinho-de-genesi-ad-litteram-imperfectus.md`; lido, técnico, nenhum achado |
| *De Genesi ad litteram* I–III | I = vv. 1–5; II = vv. 6–19; III = vv. 20–31 | `base/agostinho-de-genesi-ad-litteram.md`; 4 achados |
| *De civitate Dei* XI–XII | inteiros (XI, 4–34: criação, tempo, luz, dias, bondade; XII, 21–28: o homem) | `base/agostinho-de-civitate-dei.md`; 2 achados, mais XIX, 15 (fora da base) |
| *De Trinitate* VII, XII, XIV | VII, 6, 12; XII, 4, 4 – 8, 13; XIV inteiro | `base/agostinho-de-trinitate.md`; 3 achados |
| *De diversis quaestionibus 83* | q. 51 e q. 74 | `base/agostinho-de-diversis-quaestionibus-83.md`; técnicas, nenhum achado |
| *Sermones* (Corpus 7333–7335, 7342, 7504–7505) | notas de Migne «(Gen. I, n)» e frases da Vetus Latina | 3 achados: Sermões 90, 190, 241 |
| *Enarrationes in Psalmos* (7329, 21385) | idem | só citações de passagem; En. 148, 9 nas pistas |
| *In Iohannis evangelium* (7323), cartas (7300), *Enchiridion* (7406), *Contra Faustum* (7432), *Contra adversarium legis* (7439) | idem | pistas (ver `base/_pistas-agostinho.md`) |
| *Quaestiones* e *Locutiones in Heptateuchum* I | — | não comentam Gn 1 (`base/_ausentes-agostinho.md`) |

## Os achados

| id | trecho | vv. | o que diz |
|---|---|---|---|
| `agostinho-conf-11-12-14` | 1 | 1 | «Que fazia Deus antes de criar?» Não a piada do inferno para os curiosos: nada, porque o tempo é criatura |
| `agostinho-gnman-1-2-4` | 1 | 1 | Por que Deus criou? Porque quis; quem quer conhecer a vontade de Deus, faça-se amigo dele |
| `agostinho-conf-13-5-6` | 1 | 1–2 | A Trindade nos dois primeiros versículos |
| `agostinho-gnlitt-1-18-36` | 1 | 2 | O cristão sírio: o Espírito «aquecia» as águas como a ave os ovos, com amor |
| `agostinho-civ-11-21` | 1 | 3–4 | «Viu que era bom»: Deus ensina, não aprende; quem fez, por meio de que, por quê |
| `agostinho-civ-11-7` | 1 | 5 | Dias sem sol; a Escritura nunca diz «noite»: a tarde e a manhã do conhecimento |
| `agostinho-gnlitt-2-9-20` | 2 | 6–8 | A forma do céu: o Espírito não quis ensinar o que não serve à salvação |
| `agostinho-conf-13-15-16` | 2 | 6–7 | O firmamento = a Escritura estendida como pele; os anjos leem na face de Deus |
| `agostinho-conf-13-17-20` | 2 | 9–12 | O limite do mar; o solo enxuto sedento de Deus dá obras de misericórdia |
| `agostinho-gnlitt-2-14-29` | 3 | 14 | Os «sinais» são os do marinheiro e do lavrador, não os da astrologia |
| `agostinho-sermo-190-1` | 3 | 14, 16 | No Natal, quando os dias crescem, festeja-se quem fez o sol, não o sol |
| `agostinho-sermo-241-2` | 4 | 20–21 | «Interroga a beleza…»: as criaturas respondem «somos belas» |
| `agostinho-gnlitt-3-13-21` | 4 | 22, 28 | A primeira bênção; repetida ao homem para que gerar filhos não pareça pecado |
| `agostinho-gnman-1-16-25` | 5 | 24–25 | A oficina do artesão; não sei para que servem ratos e rãs; Deus louvado na formiga |
| `agostinho-trin-7-6-12` | 5 | 26 | «Façamos… nossa» = a Trindade; aproximamo-nos de Deus pela semelhança, não pelo lugar |
| `agostinho-trin-12-7-10` | 5 | 27 | A natureza humana nos dois sexos é imagem; a mulher não fica fora dela |
| `agostinho-trin-14-8-11` | 5 | 26–27 | A imagem na mente, gasta mas não perdida; é imagem quando lembra, entende e ama a Deus |
| `agostinho-sermo-90-10` | 5 | 26–27 | A imagem gasta como moeda esfregada na terra; o homem é a moeda de Cristo |
| `agostinho-civ-19-15` | 5 | 26, 28 | Domínio sobre os animais, não sobre os homens; ninguém é escravo por natureza |
| `agostinho-conf-13-28-43` | 5 | 31 | Sete vezes «bom», a oitava «muito bom»: o corpo inteiro é mais belo que cada membro |

Os mais fortes: `conf-11-12-14`, `civ-11-21`, `gnlitt-1-18-36`, `civ-19-15`, `conf-13-28-43`.

## Repetições a decidir com os outros grupos

- `gnlitt-1-18-36` (o «cristão sírio», a ave que choca os ovos) diz o mesmo que Basílio, *Hex.* 2, 6, que cita
  «um sírio»: ficar com o mais claro (o de Agostinho acrescenta o «afeto de amor»).
- `civ-19-15` (o domínio) pode cruzar com Crisóstomo e com a *Laudato si'*; `gnman-1-16-25` (os bichos inúteis)
  com Basílio, *Hex.* 9; `trin-7-6-12` e `trin-14-8-11` (a imagem) com Ireneu, Orígenes, Nissa e Bernardo; o de
  Agostinho é o único sobre a semelhança como aproximação e sobre a imagem como memória, inteligência e amor.
- `sermo-190-1` (o sol no Natal) é o mesmo tema de Leão Magno (o culto do sol): se ficar Leão, o de Agostinho
  pode sair.
- Alternativas que dizem o mesmo que um achado (ver as pistas): *Gen. c. Man.* I, 8, 13 (= `civ-11-21`), I, 21, 32
  (= `conf-13-28-43`), *Civ.* XI, 6 e *Gen. c. Man.* I, 2, 3 (= `conf-11-12-14`), *Civ.* XI, 22 (= `gnman-1-16-25`),
  *Gen. ad litt.* I, 19, 39 (= `gnlitt-2-9-20`), *Trin.* XIV, 4, 6 (= `sermo-90-10` e `trin-14-8-11`).
- Não repete nada já publicado: o *Sermo* 223, 1 (Gn 1,4-5) já está em 2Cor 4, e as *Confissões* XI, 5, 7 («dixit
  et facta sunt») no Sl 33; ficaram de fora.

## O que ficou de fora, e por quê

- A luz = os anjos (*Civ.* XI, 9; *Gen. ad litt.* I e IV): leitura própria dele, especulativa (o Gere excluiu o
  «muito hipotético» em Nm 12); fica nas pistas. A tarde e a manhã do `civ-11-7` vêm dessa mesma leitura, mas o
  excerto se entende sem ela (relevância 2).
- «Pondus meum amor meus» (*Conf.* XIII, 9, 10): famoso, mas fala mais da alma que do v. 2.
- A ciência antiga (os quatro elementos, as águas acima do céu, a natureza do ar em *Gen. ad litt.* II–III) e as
  questões de técnica (a matéria informe, a palavra eterna e o tempo, *imperfectus liber*, *83 quaest.*): o
  leitor comum não guarda.
- As alegorias de *Conf.* XIII sobre os peixes e as aves (= sacramentos e pregação): difíceis fora do livro.
- Nada próprio sobre o alimento só de plantas (vv. 29–30): *Gen. ad litt.* III, 21, 33 discute a imortalidade e
  o alimento, de modo técnico.

## Notas para a montagem

- **Texto**: o do augustinus.it (Maurinos = PL, com *i/u* modernos); na *Cidade de Deus* XIX o site segue a
  grafia da CCSL («caeli», «condicio», «e contrario»), sem mudar o sentido. Os links `fonte_url` são as páginas
  `..._libro.htm` (ou `discorso_NNN_testo.htm`), que abrem o texto direto; `fonte_url_alternativa` é o permalink do
  Corpus Corporum (abre a obra, não o parágrafo).
- **Colunas da PL**: conferidas no texto do Corpus Corporum (marcas `[page]`), início e fim de cada parte.
- O grego de *Gen. ad litt.* II, 17, 35 («ἀποτελέσματα») é imagem no augustinus.it: veio do PL (Corpus); na
  tradução, «apotelésmata».
- Citações bíblicas nas traduções seguem a Vetus Latina dele: «pairava» (*superferebatur*), «um dia» (*dies
  unus*), «Crescei e multiplicai-vos», «à nossa imagem e semelhança».
- Dúvida de tradução: `conf-13-17-20`, *amaricantes* = «os amargurados» (os que vivem para a felicidade terrena,
  o mar); `sermo-241-2`, *confessio* = «confissão» no sentido de louvor (como nas *Confissões*).

## Ferramentas (pré-pesquisa dos próximos capítulos)

- `pesquisa/ferramentas/base/gen_agostinho_comum.py` (biblioteca) e um script por obra, com o capítulo como
  parâmetro: `gen-agostinho-confissoes.py` (Gn 1–2), `gen-agostinho-contra-maniqueus.py` (Gn 1–3),
  `gen-agostinho-literal-incompleto.py` (Gn 1), `gen-agostinho-literal.py` (Gn 1–3), `gen-agostinho-cidade.py`
  (Gn 1; Gn 2–3 com os livros XIII–XIV juntos), `gen-agostinho-trindade.py` (Gn 1), `gen-agostinho-83-questoes.py`
  (Gn 1 e 6). Uso: `python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-literal.py 2`.
- O augustinus.it responde HTTP 999 ao user-agent curto («Mozilla/5.0»): a biblioteca usa um de navegador, e o
  Internet Archive quando o site cai. Cache em `pesquisa/cache/genesis/agostinho/` (`aug/` e `cc/`, ~25 MB).
- As colunas vêm do Corpus Corporum por ancoragem de palavras; nos arquivos de base sobram poucas falhas (PL 32,
  845; PL 41, 349–350; uma inversão 279/280 em *Gen. ad litt.*): conferir no Corpus antes de citar.
- Os limites de Gn 2 e Gn 3 nos scripts foram tirados dos títulos da NBA, sem ler os textos: conferir ao rodar.

## Para outros capítulos

- **Gn 2,1-3** (o sétimo dia): *Gen. c. Man.* I, 22, 33 – 25, 43 (o descanso de Deus; as seis idades do mundo,
  a semana da história); *Conf.* XIII, 35, 50 – 38, 53 («dá-nos a paz do sábado sem tarde»); *Civ.* XI, 8 e
  XI, 30–31 (o descanso de Deus; o número seis); *Gen. ad litt.* IV inteiro; *Sermo* 259, 2 (o oitavo dia, a
  sexta idade em que somos renovados à imagem, PL 38, 1197–1198); *Ep.* 55 (o sábado e o oitavo dia).
- **Gn 2,4-25**: *Gen. ad litt.* V, 23, 44–45 (toda a árvore está na semente: as razões causais), VI–IX;
  *Civ.* XII, 21–23 (um só homem para a concórdia; a mulher tirada do lado; «a mão de Deus é o seu poder»,
  PL 41, 372–373); *Gen. c. Man.* II, 1–19.
- **Gn 3**: *Gen. ad litt.* XI; *Gen. c. Man.* II, 20–43; *Civ.* XIII–XIV; *Trin.* XII, 12–13.
- **Gn 4,17 em diante**: *Quaestiones in Heptateuchum* I começa ali (Caim e a cidade); **Gn 6,6**: *83 quaest.*
  q. 52 («Paenitet me hominem fecisse»).
