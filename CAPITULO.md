# Como preparar um capítulo novo da Bíblia Taioé

Regras do Gere (17/10/2026). Os capítulos entram um de cada vez, e cada um passa pelas etapas
abaixo, nesta ordem. O primeiro feito assim foi o Salmo 33 (32), já revisado por ele: use-o como
modelo, sobretudo as quatro notas que ficaram. Antes de começar, ler `revisao/aprendizado.md`.

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

- **A tradução segue o original** (hebraico, aramaico ou grego); **a Nova Vulgata dá só a divisão
  de capítulos e versículos**, que se segue à risca (regra do Gere, 17/10). Onde a NV, a Bíblia grega
  ou a latina leem outra coisa (outra vogal, outra palavra), fica o original, sem nota: não se
  anotam variantes.
- Conferir verso a verso com o original (`python pesquisa/ferramentas/hebraico.py`, o texto
  hebraico com lemas; ver `pesquisa/COMO-PESQUISAR.md`).
- Para cada palavra ou fórmula importante, ver com grep como ela já foi traduzida no resto da
  Bíblia (`Software MEU/biblia/livros/*.js`) e nos capítulos da Taioé. Divergência vira escolha.
- **Nomes próprios: os da liturgia do Brasil** (regra do Gere, Nm 12): conferir cada nome no
  lecionário da CNBB, como diz `ESCOLHAS.md`, «Nomes próprios», e usar o mesmo nos comentários.
- O que for claro e seguro, corrigir direto (erro, palavra antiquada, eco perdido).
- O que tiver solução menos óbvia vira **escolha** em `revisao.escolhas`: título, referência,
  contexto curto (o que diz o original, como está no resto, o que os Padres leem), duas ou três
  opções, **uma** recomendada. O texto do site já leva a recomendada; se o Gere escolher outra, troca-se.
- A escolha que vale para a Bíblia inteira entra também em `revisao.registro`; aprovada, vai
  para `ESCOLHAS.md`.

## 3. Os versos pelo Versificador

Sempre que o capítulo tiver versos (`l`: salmos, cânticos, profetas, falas solenes), eles passam
pelo medidor de verso livre do Versificador, para soarem bem em português (pedido do Gere, 17/10):

```bash
node ferramentas/versos.mjs <livro> <capítulo>                  # cada verso medido, e o perfil
node ferramentas/versos.mjs <livro> <capítulo> --so-problemas   # só os marcados
node ferramentas/versos.mjs --verso "..."                       # testar uma nova forma
```

- Marcas: *ralo* (mais de 3,5 sílabas por acento: soa como prosa), *vazio* (5 átonas seguidas ou
  mais), *choques* (3 pares de tônicas vizinhas ou mais). Meta do conjunto: 2,4 a 2,8 sílabas por
  acento, intervalos perto de 15/30/29/16/5 % (o verso livre dos mestres, no estudo do ritmo do
  Versificador, `estudo/metros/verso-livre.md`).
- Para cada verso marcado, tentar outra ordem, outro sinônimo, outro corte de linha, e testar com
  `--verso`. **A fidelidade ao original vem antes**: a forma nova tem de dizer o mesmo que o
  hebraico (ou o grego), sem acrescentar nem tirar, e manter as escolhas do `ESCOLHAS.md`. Se não
  houver forma fiel que soe melhor, o verso fica como está (uma palavra longa como «misericórdia»
  costuma deixar o verso ralo, e tudo bem).
- Não há metro fixo nem rima: a poesia bíblica é verso livre. O que se busca é a cadência, sem
  vãos longos e sem filas de tônicas. Nunca mesóclise.
- Registrar em `revisao.divisao` (ou numa escolha, se a mudança for de sentido) o que se mudou por
  causa do ritmo.

## 4. Notas para o leitor comum

Critério do Gere (revisão do Sl 33, 17/10): **só notas importantes para entender o versículo**. No
Sl 33, de 20 notas ficaram 4.

- Entram: o contexto cultural e histórico que o leitor de hoje não tem (costume, objeto, lugar,
  a imagem antiga do mundo); o ponto importante para entender o texto mais a fundo que passaria
  despercebido (o *ruah* do Sl 33,6, em que os Padres leram a Trindade); o uso marcante na
  liturgia (o fim do *Te Deum* no Sl 33,22).
- Não entram: notas de língua (a palavra hebraica, o verbo no feminino, «no hebraico é o mesmo
  verbo de…»); variantes de manuscritos ou de traduções antigas; associações com outros textos da
  Bíblia, a não ser que sejam necessárias para entender o verso; análises e interpretações; notas
  preciosistas; o que basta o leitor saber pelo contexto (que a harpa é um instrumento).
- Uma a três frases curtas e simples, sem termos técnicos. A nota diz o necessário e para: no
  Sl 33,7 ficou só «Os abismos são as águas profundas que, na imagem antiga do mundo, ficavam
  debaixo da terra.»
- Cada nota tem `v` e `apos` (a palavra depois da qual entra a letra da nota); sem `apos`, a
  letra fica no fim do versículo. `origem` diz se é nova ou revista do projeto antigo, e por quê.
- Notas do projeto antigo: conferir uma por uma pelo mesmo critério (a maioria sai).
- As notas não repetem os comentários dos Padres.
- Passagem dura (imprecação, «os judeus» em João): traduzir sem atenuar, com nota que começa
  por «Nota do tradutor:» (regra do projeto antigo).
- Usar as explicações que o Gere deu nas revisões anteriores (`revisao/aprendizado.md`).

## 5. Avaliar a divisão em trechos

- Prosa: um subtítulo por trecho temático, como no projeto antigo; os comentários são por trecho.
- Salmos com menos de uns 40 versículos: sem subtítulo, um trecho só; o botão dos comentários
  fica abaixo do título. Salmos grandes: trechos com subtítulo (como 78, 89, 105–107, 119).
- Conferir os parágrafos e estrofes (`np`) com a NV e com o sentido; registrar em
  `revisao.divisao` o que se manteve, o que mudou e por quê.

## 6. Pesquisar os comentários (para cada trecho)

- Primeiro ler `pesquisa/COMO-PESQUISAR.md` e o catálogo `pesquisa/fontes/*.md`, que diz onde
  está cada comentário que cobre livros inteiros (Agostinho, Cassiodoro, Tomás, Belarmino…), com o
  padrão de URL. Depois, buscas pelos versículos marcantes em outras obras.
- Abrangência: Padres gregos e latinos, Doutores e santos medievais, santos modernos, Papas
  santos, Magistério, liturgia. Entram os santos, beatos e Padres da Igreja (Orígenes, Eusébio,
  Teodoreto e outros «escritores eclesiásticos» quando a tradição os usa, com a indicação do que
  são) e **os textos do Magistério**, de qualquer Papa ou concílio e o Catecismo («podem ficar, com
  certeza», o Gere, 17/10: *Verbum Domini*, *Laudato si'*), quando comentam de fato o versículo.
- Tudo se guarda em `pesquisa/<livro>/<ccc>/`: os textos inteiros (domínio público) em
  `textos/`, os excertos candidatos em `achados-*.json`, e um relatório do que se procurou e não
  existe. O que servir para outros capítulos vai para o catálogo `pesquisa/fontes/`.
- Pode correr em paralelo: um subagente por grupo (Agostinho; gregos; latinos e medievais;
  modernos, Magistério e liturgia), cada um gravando só os seus arquivos.

## 7. Escolher e organizar por temas

- Juntar os achados, tirar as repetições (o mesmo pensamento em dois autores: fica o melhor ou o
  mais antigo, salvo se o segundo acrescenta), e agrupar por **aspecto do trecho**: cada tema
  reúne os comentários que falam da mesma coisa (ex.: «O cântico novo», «O Verbo e o Espírito na
  criação»). Os temas seguem a ordem do texto; o da liturgia, se houver, vai por último.
- A página de comentários de um trecho não tem texto introdutório (o Gere, Nm 12): nada de `intro`.
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

## 8. Gerar, conferir e mandar para a revisão do Gere

O capítulo só termina com as pendências atualizadas (regra do Gere, 18/10): tudo o que segue,
até `/admin/biblia/` mostrar o capítulo na produção, vai no mesmo trabalho, sem esperar pedido.
E a página é atualizada limpa (regra do Gere, 18/10): antes do `revisao.mjs`, baixar as respostas
(`bash ferramentas/respostas.sh exportar`) e aplicar tudo o que ele já respondeu, em qualquer
capítulo, como na etapa 9, tirando do `revisao` cada item aplicado; só fica na página o que ainda
espera a resposta dele. Depois de publicar, `respostas.sh marcar`.

```bash
node ferramentas/conferir.mjs      # mesóclise, uso europeu, numeração, notas, comentários
node ferramentas/gerar.mjs         # public/biblia/
node ferramentas/revisao.mjs       # ../infra/dados/paginas/biblia.json
```

- `estado: "em revisão"` no capítulo. No taioe-infra: `python dados/paginas/gerar.py
  dados/paginas/biblia.json`, commit na `main`, e o workflow **Catálogo** (`taioe-infra`,
  `dados/paginas/biblia.sql`) no teste e na produção.
- Ver no local (http://localhost:8777/biblia/…) e na prévia; publicar (push na `main` do taioe-biblia).
- O Gere avalia em `/admin/biblia/` as escolhas de tradução, as notas, a divisão e o registro
  (aprovar, alterar, excluir, com a explicação); cada resposta grava sozinha, no clique ou ao parar
  de digitar. **Os comentários dos Padres não vão para a revisão** (17/10): entram direto no site,
  e ele pede as mudanças na conversa, à medida que for lendo.
- Estudo de uma palavra que vale para a Bíblia inteira (ex.: *nefesh*): `revisao/estudos/<id>.md`
  (o estudo) e `<id>.json` (resumo, casos e a decisão), que o `revisao.mjs` põe na mesma página
  enquanto o `estado` for «em revisão».

## 9. Aplicar as respostas

```bash
bash ferramentas/respostas.sh exportar        # baixa as respostas (workflow Respostas)
bash ferramentas/respostas.sh marcar <arquivo> # depois de aplicar: marca como lidas
```

- Aplicar cada resposta no `conteudo/`, gerar, conferir, publicar, marcar como lidas.
- Toda explicação do Gere que ensine algo para os próximos capítulos vai, resumida, para
  `revisao/aprendizado.md` (o que ele corrigiu, a regra que se tira disso). Escolhas aprovadas
  para a Bíblia inteira vão para `ESCOLHAS.md`.
- Quando tudo estiver respondido e aplicado: `estado: "revisado"` e apagar o `revisao` do capítulo
  (o histórico fica no git); ele sai da página de revisão no próximo `revisao.mjs`.
- Pedido de mudança num comentário, feito na conversa: aplicar direto no `conteudo/` e publicar.
