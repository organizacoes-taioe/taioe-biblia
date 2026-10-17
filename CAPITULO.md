# Como preparar um capítulo novo da Bíblia Taioé

Regras do Gere (17/10/2026). Os capítulos entram um de cada vez, e cada um passa pelas etapas
abaixo, nesta ordem. O primeiro feito assim foi o Salmo 33 (32); use-o como modelo.

## 1. Trazer o texto

```bash
node ferramentas/importar.mjs <livro> <capítulo>      # ex.: salmos 34
```

- O ponto de partida é a tradução do projeto antigo (`Software MEU/biblia`). Ela só é lida: a
  partir daqui o texto vivo é o da Taioé, e as correções **não** voltam ao site antigo.
- O capítulo fica em `conteudo/<livro>/<ccc>.json`. Formato do texto, igual ao do projeto
  antigo: `{s}` subtítulo (abre um trecho), `{v,t}` prosa, `{v,l:[…]}` verso, `np:1` abre
  parágrafo ou estrofe. As notas saem do versículo e vão para `notas`.
- Antes de tudo, ler `ESCOLHAS.md`: as escolhas de tradução já fixadas valem para o capítulo novo.

## 2. Avaliar a tradução

- Conferir verso a verso com o hebraico (ou o grego) e com a Nova Vulgata (a versificação e as
  variantes são as da NV; onde a NV segue o grego ou o latim, segue-se a NV e anota-se o original).
- Para cada palavra ou fórmula importante, ver com grep como ela já foi traduzida no resto da
  Bíblia (`Software MEU/biblia/livros/*.js`) e nos capítulos da Taioé. Divergência vira escolha.
- O que for claro e seguro, corrigir direto (erro, palavra antiquada, eco perdido).
- O que tiver solução menos óbvia vira **escolha** em `revisao.escolhas`: título, referência,
  contexto curto (o que diz o original, como está no resto, o que os Padres leem), duas ou três
  opções, **uma** recomendada. O texto do site já leva a recomendada; se o Gere escolher outra, troca-se.
- A escolha que vale para a Bíblia inteira entra também em `revisao.registro`; aprovada, vai
  para `ESCOLHAS.md`.

## 3. Notas para o leitor comum

- Para quem lê a Bíblia em casa, não para o especialista. Explicar o que trava a leitura: costume,
  objeto, lugar, instrumento, medida; a palavra hebraica ou grega que carrega mais do que o
  português mostra (*hesed*, *ruah*, *nefesh*); a imagem antiga do mundo; o eco de outro texto da
  Bíblia (com a referência); o uso na liturgia, quando for marcante.
- Uma a três frases, frases simples, sem termos técnicos («acróstico», «paralelismo», «LXX» só
  explicados ou trocados por «a Bíblia grega»). A palavra original em itálico, transliterada de
  modo simples (*hesed*, *teruá*), sem diacríticos acadêmicos.
- Cada nota tem `v` e `apos` (a palavra depois da qual entra a letra da nota); sem `apos`, a
  letra fica no fim do versículo. `origem` diz se é nova ou revista do projeto antigo, e por quê.
- Notas do projeto antigo: conferir uma por uma (a do Sl 33,1 estava errada).
- As notas não repetem os comentários dos Padres; podem dizer que eles leram o verso de certo modo.
- Passagem dura (imprecação, «os judeus» em João): traduzir sem atenuar, com nota que começa
  por «Nota do tradutor:» (regra do projeto antigo).
- Usar as explicações que o Gere deu nas revisões anteriores (`revisao/aprendizado.md`).

## 4. Avaliar a divisão em trechos

- Prosa: um subtítulo por trecho temático, como no projeto antigo; os comentários são por trecho.
- Salmos com menos de uns 40 versículos: sem subtítulo, um trecho só; o botão dos comentários
  fica abaixo do título. Salmos grandes: trechos com subtítulo (como 78, 89, 105–107, 119).
- Conferir os parágrafos e estrofes (`np`) com a NV e com o sentido; registrar em
  `revisao.divisao` o que se manteve, o que mudou e por quê.

## 5. Pesquisar os comentários (para cada trecho)

- Primeiro ler `pesquisa/COMO-PESQUISAR.md` e o catálogo `pesquisa/fontes/*.md`, que diz onde
  está cada comentário que cobre livros inteiros (Agostinho, Cassiodoro, Tomás, Belarmino…), com o
  padrão de URL. Depois, buscas pelos versículos marcantes em outras obras.
- Abrangência: Padres gregos e latinos, Doutores e santos medievais, santos modernos, Papas
  santos, liturgia. Só santos, beatos e Padres da Igreja (Orígenes, Eusébio, Teodoreto e outros
  «escritores eclesiásticos» entram quando a tradição os usa, com a indicação do que são).
- Tudo se guarda em `pesquisa/<livro>/<ccc>/`: os textos inteiros (domínio público) em
  `textos/`, os excertos candidatos em `achados-*.json`, e um relatório do que se procurou e não
  existe. O que servir para outros capítulos vai para o catálogo `pesquisa/fontes/`.
- Pode correr em paralelo: um subagente por grupo (Agostinho; gregos; latinos e medievais;
  modernos, Magistério e liturgia), cada um gravando só os seus arquivos.

## 6. Escolher e organizar por temas

- Juntar os achados, tirar as repetições (o mesmo pensamento em dois autores: fica o melhor ou o
  mais antigo, salvo se o segundo acrescenta), e agrupar por **aspecto do trecho**: cada tema
  reúne os comentários que falam da mesma coisa (ex.: «O cântico novo», «O Verbo e o Espírito na
  criação»). Os temas seguem a ordem do texto; o da liturgia, se houver, vai por último.
- Tema: id curto, título, versículos, resumo de uma frase. Entre 2 e 8 comentários por tema;
  um tema de um comentário só, só se ele for essencial.
- Comentário: excerto com sentido completo (2 a 8 frases), na ordem do raciocínio, do mais
  claro ao mais fundo. `autor`, `sobre` (datas e o que foi: «bispo de Hipona, Doutor da
  Igreja»), `obra` (título em português e, entre parênteses, o original), `passagem` (a exata),
  `link` (o texto original na internet), `original` (o trecho na língua original, só para a
  revisão), `texto` (a tradução).
- Tradução nossa, do original (o inglês antigo só para conferir), em português do Brasil
  contemporâneo, sem mesóclise, sem uso europeu, sem pronomes contraídos. A citação bíblica dentro
  do comentário segue o texto que o Padre leu (é ele que está comentando), entre aspas.
- Textos com direito autoral (Papas recentes, LEV): no máximo duas ou três frases, com o link para
  o texto inteiro (decisão do Gere, 17/10).

## 7. Gerar, conferir e mandar para a revisão do Gere

```bash
node ferramentas/conferir.mjs      # mesóclise, uso europeu, numeração, notas, comentários
node ferramentas/gerar.mjs         # public/biblia/
node ferramentas/revisao.mjs       # ../infra/dados/paginas/biblia.json
```

- `estado: "em revisão"` no capítulo. No taioe-infra: `python dados/paginas/gerar.py
  dados/paginas/biblia.json`, commit na `main`, e o workflow **Catálogo** (`taioe-infra`,
  `dados/paginas/biblia.sql`) no teste e na produção.
- Ver no local (http://localhost:8777/biblia/…) e na prévia; publicar (push na `main` do taioe-biblia).
- O Gere avalia em `/admin/biblia/`: cada escolha, nota, a divisão, cada tema e cada comentário
  (aprovar, alterar, excluir, mover de tema), com a explicação.

## 8. Aplicar as respostas

```bash
bash ferramentas/respostas.sh exportar        # baixa as respostas (workflow Respostas)
bash ferramentas/respostas.sh marcar <arquivo> # depois de aplicar: marca como lidas
```

- Aplicar cada resposta no `conteudo/`, gerar, conferir, publicar, marcar como lidas.
- Toda explicação do Gere que ensine algo para os próximos capítulos vai, resumida, para
  `revisao/aprendizado.md` (o que ele corrigiu, a regra que se tira disso). Escolhas aprovadas
  para a Bíblia inteira vão para `ESCOLHAS.md`.
- Quando tudo estiver respondido e aplicado: `estado: "revisado"`; o capítulo sai da página de
  revisão no próximo `revisao.mjs`.
