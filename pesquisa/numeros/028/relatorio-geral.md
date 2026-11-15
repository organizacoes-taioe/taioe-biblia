# Números 28: relatório da pesquisa (todos os grupos)

Pesquisa de 2026-11-15. Hebraico, Nova Vulgata, Vulgata e LXX coincidem nos 31 versículos. Orígenes: 3 de 11 achados.

Entregues: `achados-geral.json` (11 achados) e, em `textos/`, os originais que não estão em `base/`.
Nenhum autor novo: todos já estão em `ferramentas/autores.json`. Orientais: só Cirilo de Alexandria.

## Os achados, em uma linha

Trecho 1:
- **Orígenes**, Homilias sobre Números XXIII, 2 (GCS: «XXII», 2) (vv. 2): Deus começa por dizer que os dons são «dados por ele»: quem oferece apenas devolve, e pensar que dá algo a um Deus necessitado seria impiedade.
- **Orígenes**, Homilias sobre Números XXIII, 2 (GCS: «XXII», 2) (vv. 2): Os «dias de festa de Deus» são as conversões, uma a uma: cada pecador que muda de vida alegra o Pai, o Filho, o Espírito Santo e os anjos.
- **Orígenes**, Homilias sobre Números XXIII, 3 (GCS: «XXIII», 3) (vv. 3, 4): O holocausto de cada dia vem antes de todas as festas porque o justo deve celebrar sem cessar, orando sem intermissão.
- **São Bruno de Segni**, Exposição sobre Números cap. XXVIII (vv. 3, 4, 7): O holocausto da manhã e da tarde pede que Deus seja louvado o dia inteiro, e a Igreja o cumpre em suas horas de oração, na assembleia dos fiéis.
- **Cornélio a Lápide**, Comentário ao Pentateuco: Números cap. XXVIII, nota ao v. 3 (vv. 3, 4): O cordeiro da manhã e o da tarde ensinam o cristão a abrir e a fechar o dia com Deus, agradecendo e entregando-lhe tudo.
- **São Cirilo de Alexandria**, Da adoração e do culto em espírito e verdade XVII (diálogo com Paládio) (vv. 3, 4, 6): O sacrifício de cada dia figura a vida inteira do cristão oferecida em Cristo, sem cessar, na Igreja, e o Cordeiro que sobe ao Pai levando consigo os que nele creem.
- **São Tomás de Aquino**, Suma Teológica I-II, q. 102, a. 4, ad 10 (vv. 3, 9, 11, 16, 26): Para Tomás, o sacrifício perpétuo é uma festa contínua que figura a perpetuidade de Cristo, e cada festa seguinte recorda um benefício de Deus e prefigura um mistério da Igreja.

Trecho 2:
- **Ruperto de Deutz**, Comentário a Mateus sobre Mt 12,5 (vv. 9, 10): Os sacerdotes trabalhavam no sábado oferecendo os cordeiros e não pecavam: o sábado se viola pela obra servil, que é, no fundo, desprezar o preceito.

Trecho 3:
- **São Cirilo de Alexandria**, Da adoração e do culto em espírito e verdade XVII (diálogo com Paládio) (vv. 11, 14): A lua nova do mês figura o século novo aberto pela ressurreição, e o sacrifício que lhe convém é morrer para o pecado a fim de viver com Cristo.

Trecho 4:
- **Santo Isidoro de Sevilha**, Questões sobre o Antigo Testamento cap. XVII, §9 (vv. 11, 16): O cristão não repete a Páscoa do cordeiro nem a festa da lua nova porque Cristo, Cordeiro sem mancha e nova criatura, cumpriu o que elas anunciavam.

Trecho 5:
- **Santo Agostinho**, A cidade de Deus XVI, 43 (vv. 26): Cinquenta dias depois da Páscoa do cordeiro foi dada a Lei; cinquenta dias depois da Páscoa de Cristo veio o Espírito, o «dedo de Deus» que escreve a nova lei.

## Como se procurou

- `base/` de cada capítulo (Orígenes, Bruno de Segni, Cirilo, Agostinho, Ruperto) e as obras completas do Corpus Corporum já baixadas, por palavras do texto da Vulgata (iuge sacrificium, neomenia, scenopegia, vovete et reddite etc.) e pelas notas de Migne; Corpus Thomisticum (Suma, I-II q. 102 a. 4 ad 10; II-II q. 88).
- Orígenes lido nas imagens do GCS 30 (pp. 211, 212, 214, 221, 222, 229, 230); Lápide, na imagem da p. 353. Os demais excertos foram cortados por script do texto baixado (notas, colunas e números de página retirados; cortes marcados com «[...]»).
- Conferido contra os achados de Nm 12–25 e entre os três capítulos: nenhuma sequência de 8 palavras repetida.
- Os links do Corpus Corporum (`mlat.uzh.ch/browser/cps_2…`) são da obra, não da página; a coluna de Migne vai no campo `edicao`.

## O que não existe ou não serviu

- Sem excerto próprio sobre as medidas das oblações (décimos, him, números de vítimas): só alegoria numérica, deixada de fora de propósito.
- Procópio (catena): OCR ilegível no grego e atribuição por capítulo incerta; copia Cirilo e Teodoreto. Não usado.
- Rábano e pseudo-Beda: só compilação de Orígenes e Isidoro. Isidoro, *In Num.* XLII, 13 (sábado, calendas, Páscoa, Pentecostes em uma linha) está em `base/` e não entrou: a mesma ideia está melhor em Tomás e Isidoro, *In Lev.*
- Agostinho, *Locutiones* IV: só gramática. Escrivá: nenhum ponto cita o capítulo.
- Jerônimo, *In Ez.* XIV (Ez 46,13–15, o «holocausto sempiterno» de cada manhã) e *In Dan.* (o «juge sacrificium» tirado por Antíoco e pelo Anticristo; Gregório, *Moralia* (PL 76, 651C), sobre Dn 8,12: «tira o sacrifício perpétuo quem interrompe o zelo da Igreja»): não comentam Nm 28; ficam como reserva para o sacrifício perpétuo.
- Pseudo-Atanásio, *De sabbatis et circumcisione* e Cirilo, *De adoratione* XVII, 1081–1092 (as medidas): não lidos além das falas do `base/`.

## Para outros capítulos

- **Nm 29**: Tomás, I-II q. 102 a. 4 ad 10 serve aos dois capítulos (festas do sétimo mês); usei só a segunda metade em Nm 29. Cirilo, *De adoratione* XVII, 1120 (a última trombeta; o jejum).
- **Nm 30**: Isidoro, *In Num.* XLII, 13 («uxorum et filiarum vota absque auctoritate patrum… cassa memorantur») em `base/`.
