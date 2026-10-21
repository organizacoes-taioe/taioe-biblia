# Salmo 37 (LXX 36): relatório da pesquisa nos Padres gregos e orientais

Pesquisa de 2026-10-20/21. Resultado: **25 excertos** em `achados-gregos.json` (10 com relevância 3); os originais conferidos
estão em `textos/originais-gregos-orientais.md`. Numeração: a LXX e o hebraico coincidem em todos os versículos deste salmo
(o «Τῷ Δαυΐδ» faz parte do v. 1). Cobertos: vv. 1, 3–6, 8, 9, 11, 14–15, 19, 21, 23–27, 29, 31–33, 35–37. **Sem excerto:** vv. 2, 7,
10, 12–13, 16–18, 20, 22, 28, 30, 34, 38–40 (ver abaixo o melhor candidato de cada um, se faltar).

## Por autor

| Autor | Achados | Onde |
|---|---|---|
| São Cirilo de Alexandria | 4 | *Expositio* (cadeias, PG 69): vv. 19, 27, 37; *Com. a Isaías* IV (PG 70, 1120): v. 31 |
| Teodoreto de Ciro | 3 | *Interpretatio* (PG 80): vv. 1, 23–24; *História religiosa* 15, 1 (Acépsimas): v. 4 |
| Dídimo, o Cego | 3 | papiro de Tura, págs. 245, 251, 255 (citação curta): vv. 9, 21, 32–33 |
| Eusébio de Cesareia | 2 | *Commentaria* (PG 23, 325 e 329): vv. 3–4 (a Eucaristia), 14–15 (testemunha da perseguição) |
| Orígenes (latim de Rufino) | 2 | *Homilias sobre o Sl 36*, IV (v. 25) e V (vv. 35–36) |
| São João Crisóstomo | 2 | *Hom. 31 sobre Hebreus*, 3 (v. 5); *Hom. 15 sobre Mateus*, 3 (v. 11) |
| São Basílio Magno | 2 | *Hom. contra os irados* (v. 8); *Hom. sobre o Sl 33*, sobre os mansos (v. 11) |
| São Gregório Nazianzeno | 2 | *Discurso* 8, 15 (Gorgônia, v. 24); *Discurso* 14, 38 (v. 26) |
| Afraates, o Sábio Persa | 2 | *Demonstração* 3, 10 (Amã, v. 15); 14, 22 (a terra dos vivos, v. 29) |
| São João Clímaco | 2 | *Escada*, degrau 15 (vv. 35–36, PG 88, 896) e 24 (v. 11, PG 88, 981) |
| Santo Atanásio | 1 | *Expositiones* (PG 27, 177): v. 6, o bom ladrão ao meio-dia |

**Autor novo** para `ferramentas/autores.json`: «São João Clímaco», sobre: «monge e abade do Sinai (c. 579–c. 649), autor da
*Escada do Paraíso*», oriental: sim. (Já existe «Escólio antigo à Escada de São João Clímaco», que é outra coisa.)

## Onde se procurou

- **Pré-pesquisa (`base/`)**, lida inteira: Teodoreto, Atanásio, Eusébio (cadeia), Cirilo (cadeia de Mai), Orígenes (*Selecta* e Pitra).
  Atribuições: a glosa de Atanásio sobre o v. 19 («nas perseguições, faltando os mestres, o Senhor alimenta com o seu Espírito») está
  também em Cirilo; usou-se Cirilo, que a desenvolve. O v. 6 de Atanásio (o bom ladrão) não tem paralelo em Cirilo nem em Teodoreto.
  O texto de Eusébio sobre o v. 4 (comer as carnes e beber o sangue) tem paralelo no frag. 356 de Dídimo (Mühlenberg): atribuição
  de cadeia, mas as palavras são diferentes.
- **Dídimo, o Cego**: Tura, págs. 245–257 (o Sl 36 LXX retoma no v. 9; **lacunas: págs. 246–250, vv. 12–21, e 252–254, vv. 24–28**);
  fragmentos de Mühlenberg 355–372. Ambos edição moderna: citação curta.
- **Busca em todo o corpus grego convertido** (2 091 textos: Crisóstomo inteiro, Basílio, os dois Gregórios, Atanásio, Orígenes,
  Cirilo, Teodoreto, Eusébio, Epifânio, Máximo, Macário, Severiano, Hesíquio, Clemente, Constituições Apostólicas, o *Evergetinós* e
  a *Filocalia* em OCR) com 80 padrões, um ou mais por versículo, e depois 17 padrões frouxos: ~1 460 ocorrências, todas lidas
  depois de tirar os comentários e as duplicatas. Script: `p-gregos/busca.py` (normaliza acentos, ς→σ e χ→κ).
- **Orígenes, *Homilias sobre o Sl 36*** (latim de Rufino): OCR da PG 12. O grupo dos latinos baixou o mesmo texto
  (`textos/origenes-homiliae-in-ps36.md`) e tirou 7 achados dele (vv. 3, 4, 11, 14, 16, 24, 39–40); os dois daqui (v. 25 e
  vv. 35–36) não coincidem com aqueles. O original grego de quatro homilias está no *Monacensis gr. 314* (Perrone, GCS NF 19, 2015,
  com direito; não é de acesso aberto): só pista.
- **Padres do deserto e ascetas**: *Apophthegmata* (PG 65, OCR e a coleção alfabética em grego), Clímaco e Doroteu (PG 88, OCR e
  imagens), Barsanúfio (texto grego da azbyka), Nilo (PG 79), Pseudo-Macário (*Homilias* 50 e *Sermões* 64), *Evergetinós* I–IV,
  *Filocalia*. Clímaco foi transcrito da imagem da PG 88 (págs. n451 e n502 do item `PatrologiaGraeca` do archive.org).
- **Siríacos**: Digital Syriac Corpus (TEI): Afraates *Dem.* 3, 5, 9, 14; *Liber Graduum*, memre 7, 10, 11, 13, 21, 29.
- **Hinografia bizantina**: os 2 369 arquivos do AGES (Menaion, Triódio, Octoeco, Pentecostário, Eucológio), com os mesmos padrões.

## O que se achou e ficou fora (para não procurar de novo)

- **Liturgia bizantina** (AGES, a conferir numa edição antiga do Menaion): os **vv. 30–31** («Στόμα δικαίου μελετήσει σοφίαν…
  ὁ νόμος τοῦ Θεοῦ αὐτοῦ ἐν καρδίᾳ αὐτοῦ») são o **aleluia da missa dos santos hierarcas e monges** (ex.: 27/1, 6/2, 10/4, 4/6,
  9/6, 22/10, 13/11, 16/12; também verso das vésperas dos hierarcas); o v. 39 está nas vésperas de São João Batista; os vv. 34 e 1
  formam um *prokeímenon* de vésperas de um dia da Quaresma (Triódio). Bom para um tema de liturgia, se o capítulo tiver um.
- **Crisóstomo** não comentou o salmo; os usos são curtos: *Hom. 23 sobre Romanos* (v. 4, «só a experiência ensina» a delícia do amor
  de Deus, PG 60, 622), *Hom. 22 sobre João* (v. 4), *Sobre a esmola* (vv. 25–26), *Hom. 18 sobre Atos* (v. 25), *Hom. sobre 1 Cor* (vv.
  1–2: «onde está, depois da morte, o ladrão?»), *Hom. sobre Colossenses* (vv. 1, 35–36). *De paenitentia et in Herodem* (PG 59, 757,
  v. 24) é **espúrio**; *In s. Stephanum* (v. 32), *De patientia*, *De pseudoprophetis*, *Eclogae*, *In venerandam crucem*: espúrios.
- **Basílio**: *Carta 268* a Eusébio de Samósata exilado (v. 28, «mostrou também em nós que não abandona os seus santos»); *Hexaémeron*
  8, 8 (v. 4: «hoje, depois do jejum, permanece no serviço da alma: põe as tuas delícias no Senhor»); *Hom. no princípio dos
  Provérbios* (vv. 11 e 37: a *akakía*); *Hom. sobre o Sl 28* (o cedro, bom e mau). *Enarratio in Isaiam* e *Constitutiones asceticae*:
  autoria duvidosa.
- **Eusébio, *História eclesiástica*** X, 1, 7 (vv. 35–36 aplicados ao fim dos perseguidores e à paz de Constantino) e X, 4, 29–30 (vv.
  14–15); **São Clemente Romano**, *1 Clem.* 14–15 (vv. 35–37: «unamo-nos aos que vivem em paz com piedade»), o uso mais antigo,
  mas quase só citação; **São Cirilo**, *Hom. pascal* 15 (v. 4) e *Glaphyra*; **Teodoreto**, cartas (vv. 5–6, 20).
- **Cadeias sem achado**: Cirilo v. 18 («o Senhor só conhece o bem: "não te conheço"»), v. 9 («como o Salvador é sabedoria e justiça,
  é também a nossa paciência»: é de Dídimo, Tura pág. 245), v. 11 (os santos têm guerras nesta vida), vv. 14–15 («as nossas armas não
  são carnais»), v. 24 (a mão que levanta quem afunda), v. 31 (a lei como leme do navio e freio do cavalo), v. 34 (a terra tão alta
  que só Deus faz subir: é de Dídimo, frag. 370), v. 38 («subiu e caiu, apareceu e encolheu, floresceu e murchou»); Orígenes/Pitra
  v. 2 (o capim é comida dos animais: os aduladores comem o mau) e v. 25 («não diz "abandonado", mas "deixado por um tempo", para
  prova»); *Selecta* v. 20 (a fumaça que o fogo de Cristo expulsa da lenha). Os candidatos para os versículos sem excerto são estes.
- **Dídimo (Tura)**: v. 24 (o corredor que tropeça e não para, e Judas, que caiu de cabeça), v. 31 (as sandálias aladas do
  Evangelho), v. 36 (o diabo que quer pegar o mundo «como ovos abandonados»), vv. 39–40 (Abel; o escudo protege a alma, não
  sempre o corpo: parecido com o v. 33, por isso ficou fora).
- ***Liber Graduum***, memra 29, 16 (v. 25, aplicado aos solitários: não se fartar nem de pão seco e água) e 29, 3 (quem ensina o
  salmo «deixa a ira» sem praticá-lo): escritor anônimo de estatuto incerto; ficou fora. Afraates *Dem.* 5, 2 (vv. 35–36) e 9, 1
  (vv. 11/29): só citação.
- **Barsanúfio**, cartas 195 e outras: «ainda um pouco, espera o Senhor, e ele glorificará a tua saída» (vv. 10 e 34) a um irmão
  que ia morrer: uma frase só. **Evergetinós** e **Filocalia**: citações sem comentário; um dito sobre o v. 11 é do abade Zósimo.
- **Pseudo-Macário**, *Sermões* 64 (Berthold, com direito): v. 5 («não converses com o pensamento sem oração; revela ao Senhor o teu
  caminho») e v. 31; Anastácio Sinaíta (PG 89): v. 7. **Escólios** a Dionísio na PG 91 (vv. 35–36: o mal não tem subsistência):
  atribuição insegura.
- **Não se achou nada**: *Apophthegmata* (nenhum dito usa o salmo), Doroteu de Gaza, Nilo, Isaac de Nínive, Efrém (corpus siríaco e
  grego), Teodoro Estudita, Romano e André de Creta (sem uso deste salmo nos textos convertidos).
- **Fora da comunhão** (só registro): Dionísio bar Salibi (comentário literal, em `base/`), Filoxeno (*Disc.* 9 e 11), Narsai, Ishoʿyahb III
  e Tomás de Edessa (citações dos vv. 2, 8, 9, 34, 35): não entram.

## Cuidados

- **Direitos**: Dídimo (Tura, Gronewald 1969) é edição moderna: «citação curta». A *História religiosa* de Teodoreto no khazarzar
  segue Canivet (SC, moderna): marcada «citação curta»; o texto é o da PG 82 (colunas aproximadas).
- **Colunas a conferir**: Orígenes (PG 12, pelo OCR: hom. IV, cols. 1355–1356; hom. V, 1363–1364); Teodoreto *HR* (PG 82, 1413–1416);
  Clímaco (PG 88, 896 e 981, lidas na imagem). Os números de seção de Basílio (*Hom. 10*; *Hom. Sl 33*) não foram conferidos.
- **Eusébio, Orígenes, Dídimo e Teodoreto** não são santos: o `titulo_autor` diz «escritor eclesiástico (não é santo)».
- **Afraates**: traduzido do siríaco do Digital Syriac Corpus (Parisot); o «ele» do repouso no paraíso (*Dem.* 14, 22) foi explicitado
  como «no paraíso» na tradução.
- **Redundâncias com outros grupos**: o v. 11 (a bem-aventurança tirada do salmo) aparece também em Orígenes (achados dos latinos,
  `origenes-hps36-2-6`); o v. 5 (revelar o caminho = confissão) também em Santo Ambrósio (`ambrosio-en36-14`). Na escolha, ficar
  com o mais claro.
