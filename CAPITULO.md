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
  opções, **uma** recomendada. O texto leva a recomendada; se o Gere escolher outra, troca-se. O
  capítulo com escolha pendente fica fora do site até ele responder todas (26/10; `gerar.mjs`, `publicavel`).
- **Uma decisão por escolha** (o Gere, 24/10: «me mostre apenas questões pontuais, para eu decidir
  uma única coisa em cada pendência»): uma pergunta só, que ele responda escolhendo uma opção.
- O que vale para a Bíblia inteira e tem alternativa de verdade vira escolha; o resto (correções
  pelo original, termos já fixados, nomes) vai direto para `ESCOLHAS.md` e para a mensagem do
  commit, sem passar por ele. Não existe mais `revisao.registro` (o `revisao.mjs` recusa).

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
- O que se mudou por causa do ritmo vai na mensagem do commit (numa escolha, se a mudança for de
  sentido).

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
  por «Nota do tradutor:» (regra do projeto antigo). A nota não explica nem interpreta o texto:
  no Sl 35,4 o Gere excluiu a que explicava os pedidos contra os inimigos (18/10).
- Usar as explicações que o Gere deu nas revisões anteriores (`revisao/aprendizado.md`).

## 5. Avaliar a divisão em trechos

- Prosa: um subtítulo por trecho temático, como no projeto antigo; os comentários são por trecho.
- Salmos com menos de uns 40 versículos: sem subtítulo, um trecho só; o botão dos comentários
  fica abaixo do título. Salmos grandes: trechos com subtítulo (como 78, 89, 105–107, 119).
- Conferir os parágrafos e estrofes (`np`) com a NV e com o sentido. A divisão é decisão nossa e
  não vai à revisão do Gere (24/10: «confio nas suas escolhas agora que elas também se baseiam nos
  comentários»); o que se manteve, o que mudou e por quê vai na mensagem do commit. Não existe mais
  `revisao.divisao` (o `revisao.mjs` recusa).

## 6. Pesquisar os comentários (para cada trecho)

- **Partir da pré-pesquisa** (pedido do Gere, 20/10): `pesquisa/<livro>/<ccc>/BASE.md` lista o que
  já foi baixado e cortado para o capítulo em `base/` (os comentários de livro inteiro, na língua
  original), quem se confirmou que não comenta, e as pistas; `pesquisa/<livro>/proximos.md` traz o
  que a pesquisa de outros capítulos achou sobre este. O grosso já está ali: os subagentes leem
  esses textos, tiram os achados, e gastam o tempo nos comentários **menos óbvios** (citações em
  sermões, cartas e tratados, santos modernos, Magistério, liturgia), que enriquecem o capítulo.
  Capítulo sem `base/`: rodar antes os scripts de `pesquisa/ferramentas/base/` para ele.
- Depois, `pesquisa/fontes/<livro>.md` (o mapa do livro: `numeros.md`, `salmos.md`, `paulo.md`)
  e, para o acesso às fontes, os catálogos por grupo (`agostinho.md`, `gregos.md`, `latinos.md`,
  `modernos.md`, `orientais.md`) e `pesquisa/COMO-PESQUISAR.md`.
- Abrangência: Padres gregos e latinos, Doutores e santos medievais, santos modernos, Papas
  santos, Magistério, liturgia. Entram os santos, beatos e Padres da Igreja (Orígenes, Eusébio,
  Teodoreto e outros «escritores eclesiásticos» quando a tradição os usa, com a indicação do que
  são) e **os textos do Magistério**, de qualquer Papa ou concílio e o Catecismo («podem ficar, com
  certeza», o Gere, 17/10: *Verbum Domini*, *Laudato si'*), quando comentam de fato o versículo.
- **Escolher o melhor, venha de onde vier** (o Gere, 20/10: «a meta de orientais está exagerada, e
  não precisa favorecer eles sobre os ocidentais, quero que escolha o melhor»). Não há cota nem
  preferência por Oriente ou Ocidente. A pesquisa continua procurando também os orientais menos
  conhecidos (siríacos, armênios, Padres do deserto, hinografia bizantina; catálogo `orientais.md`),
  para que o melhor deles não fique de fora. **Os siríacos fora da comunhão com Roma ficam só como
  pista**, nunca no site (o Gere, 20/10): Dionísio bar Salibi, Filoxeno de Mabug, Narsai, Isho`dad
  de Merv, Teodoro bar Koni; em `autores.json` levam `"site": false`, e o `conferir` os recusa.
- **São Josemaria Escrivá** entra quando comentar o versículo (o Gere, 20/10: tem autorização do Opus
  Dei; basta o link do escriva.org). Tradução nossa do original espanhol, com o link do ponto ou do
  parágrafo no escriva.org; não vale o limite de «citação curta». Índice das citações bíblicas em
  `pesquisa/fontes/escriva.md`.
- Tudo se guarda em `pesquisa/<livro>/<ccc>/`: os textos inteiros (domínio público) em
  `textos/`, os excertos candidatos em `achados-*.json`, e um relatório do que se procurou e não
  existe. O que servir para outros capítulos vai para o mapa do livro (`pesquisa/fontes/<livro>.md`);
  o que se achar sobre outro capítulo, para `pesquisa/<livro>/proximos.md`, na seção dele.
- Pode correr em paralelo: um subagente por grupo (Agostinho e latinos; gregos; orientais não
  gregos e liturgia oriental; medievais; modernos, Magistério e liturgia), cada um gravando só os
  seus arquivos, cada um numa subpasta própria do scratchpad.

## 7. Escolher e organizar por temas

- Juntar os achados, tirar as repetições (o mesmo pensamento em dois autores: fica o melhor ou o
  mais antigo, salvo se o segundo acrescenta), e agrupar por **aspecto do trecho**: cada tema
  reúne os comentários que falam da mesma coisa (ex.: «O cântico novo», «O Verbo e o Espírito na
  criação»). Os temas seguem a ordem do texto; o da liturgia, se houver, vai por último.
- A página de comentários de um trecho não tem texto introdutório (o Gere, Nm 12): nada de `intro`.
- **Poucos e diferentes** (o Gere, 20/10: «não encher de textos muito parecidos»; «já tenho muitos
  comentários pendentes, em poucos capítulos»). Cada comentário de um tema tem de dizer algo que os
  outros não dizem; dois que dizem o mesmo, fica o melhor (o mais claro, bonito e fundo para o
  leitor comum). Tema que repete a ideia de outro tema, funde-se ou sai.
- Tema: id curto, título, versículos, resumo de uma frase. **De 2 a 4 comentários por tema** (5 só
  se cada um disser coisa claramente diferente); um tema de um comentário só, só se ele for
  essencial. O capítulo fica, em geral, **entre 30 e 50 comentários**, conforme o tamanho; nos
  Salmos 33–36 eram de 114 a 159, e foram enxugados em 20/10.
- Comentário: excerto com sentido completo (2 a 8 frases), na ordem do raciocínio, do mais
  claro ao mais fundo. `autor`, `sobre` (datas e o que foi: «bispo de Hipona, Doutor da
  Igreja»), `obra` (título em português e, entre parênteses, o original), `passagem` (a exata),
  `link` (o texto original na internet), `original` (o trecho na língua original, só para a
  revisão), `texto` (a tradução).
- Montar com `python -I -X utf8 ferramentas/montar-temas.py <livro> <cap>`, a partir de
  `pesquisa/<livro>/<ccc>/temas.json` (a escolha e a ordem: trecho → temas → ids dos achados; formato
  no topo do script) e de `ferramentas/autores.json` (o nome e o «sobre» de cada autor, iguais em
  todos os capítulos; autor novo entra lá, com `"oriental"`). `--mostrar` mostra antes de gravar; no
  fim ele dá a conta dos orientais por trecho. Ele tira as notas do pesquisador entre colchetes,
  passa os links para https e acusa ids que o `conferir` recusa.
- Tradução nossa, do original (o inglês antigo só para conferir), em português do Brasil
  contemporâneo, sem mesóclise, sem uso europeu, sem pronomes contraídos. A citação bíblica dentro
  do comentário segue o texto que o Padre leu (é ele que está comentando), entre aspas.
- Textos com direito autoral (Papas recentes, LEV): no máximo duas ou três frases, com o link para
  o texto inteiro (decisão do Gere, 17/10).

## 8. Gerar, conferir e mandar para a revisão do Gere

O capítulo só termina com as pendências atualizadas (regra do Gere, 18/10): tudo o que segue,
até `/admin/pendencias/` mostrar o capítulo na produção, vai no mesmo trabalho, sem esperar pedido.
E a página é atualizada limpa (regra do Gere, 18/10): antes do `revisao.mjs`, baixar as respostas
(`bash ferramentas/respostas.sh exportar`) e aplicar tudo o que ele já respondeu, em qualquer
capítulo, como na etapa 9, tirando do `revisao` cada item aplicado; só fica na página o que ainda
espera a resposta dele. Depois de publicar, `respostas.sh marcar`.

```bash
node ferramentas/conferir.mjs      # mesóclise, uso europeu, numeração, notas, comentários
node ferramentas/gerar.mjs         # public/biblia/
node ferramentas/revisao.mjs       # ../infra/dados/paginas/biblia.json e biblia-comentarios.json
```

- `estado: "em revisão"` no capítulo. No taioe-infra: `python dados/paginas/gerar.py
  dados/paginas/biblia.json` (e o mesmo com `biblia-comentarios.json`), commit na `main`, e o
  workflow **Catálogo** (`taioe-infra`, `dados/paginas/biblia.sql` e `biblia-comentarios.sql`) no
  teste e na produção.
- Ver no local (http://localhost:8777/biblia/…) e na prévia; publicar (push na `main` do taioe-biblia).
- O Gere avalia em `/admin/pendencias/`, tipo «Bíblia: tradução», só as perguntas pontuais: as
  escolhas de tradução e as notas (aprovar, alterar, excluir, com a explicação); cada resposta grava
  sozinha, no clique ou ao parar de digitar. Sem texto explicativo nem pergunta geral (19/10). A
  página põe no fim da fila o que ele já respondeu e o Claude ainda não aplicou (24/10).
- **Só o aprovado vai ao site** (o Gere, 26/10): o capítulo, sem escolha pendente; a nota, com
  `revista` (ou no capítulo revisado); o comentário, com `revisto` e sem `aviso_corte`; o tema, com o
  título aprovado e algum comentário aprovado, e o resumo só aprovado. O merge vai normalmente: o
  `gerar.mjs` esconde o resto. Nota nova num capítulo revisado: o capítulo volta a «em revisão».
- **Os comentários dos Padres** ele revisa à parte (desde 19/10),
  no tipo «Bíblia: comentários dos Padres», para não misturar com o que é prioritário: cada título de tema e
  cada texto (`resumo`) de tema (aprovar ou editar), cada comentário (aprovar, cortar ou excluir).
  O que ele aprova ganha `revisto` (no tema, a lista `["titulo", "resumo"]`; no comentário, `true`)
  e sai da página no próximo `revisao.mjs`.
- Estudo de uma palavra que vale para a Bíblia inteira (ex.: *nefesh*): `revisao/estudos/<id>.md`
  (o estudo) e `<id>.json` (resumo, casos e a decisão), que o `revisao.mjs` põe na mesma página
  enquanto o `estado` for «em revisão».

## 9. Aplicar as respostas

```bash
bash ferramentas/respostas.sh exportar        # baixa as respostas (workflow Respostas)
bash ferramentas/respostas.sh marcar <arquivo> # depois de aplicar: marca como lidas
```

- Aplicar cada resposta no `conteudo/`, gerar, conferir, publicar, marcar como lidas.
  Escolha respondida: sai de `revisao.escolhas`. Nota aprovada: `"revista": true` (vai ao site e sai
  da página); excluída: sai de `notas`.
- Toda explicação do Gere que ensine algo para os próximos capítulos vai, resumida, para
  `revisao/aprendizado.md` (o que ele corrigiu, a regra que se tira disso). Escolhas aprovadas
  para a Bíblia inteira vão para `ESCOLHAS.md`.
- Quando tudo estiver respondido e aplicado: `estado: "revisado"` e apagar o `revisao` do capítulo
  (o histórico fica no git); ele sai da página de revisão no próximo `revisao.mjs`.
- Pedido de mudança num comentário, feito na conversa: aplicar direto no `conteudo/` e publicar.
- Respostas dos comentários (tipo «Bíblia: comentários dos Padres»):
  ```bash
  bash ferramentas/respostas.sh comentarios exportar                 # caminho do JSON
  node ferramentas/aplicar-comentarios.mjs <respostas.json>           # aplica e lista os cortes
  bash ferramentas/respostas.sh comentarios marcar <respostas.aplicadas.json>
  ```
  A edição dele num comentário é só para cortar: conferir cada corte que o script lista (antes e
  depois) contra o original. Se o corte mudou o sentido ou deixou a frase manca, não corrigir por
  conta própria (pedido dele, 19/10): `node ferramentas/aplicar-comentarios.mjs --avisos <avisos.json>`
  com `[{"item": "<id c: do corte>", "aviso": "o que mudou", "sugestao": "o corte acertado, o mínimo"}]`.
  O comentário sai do site e volta às pendências com o corte
  dele, o aviso e a sugestão, para ele aprovar a sugestão, manter o corte, editar ou excluir
  (`aviso_corte` no comentário; a resposta vem como `<cap>:ca<n>:…` e o mesmo script a aplica).
  Ele responde tudo um por um: a página não tem «aprovar todos» (19/10).
  Depois, gerar, `revisao.mjs`, Catálogo e publicar, como acima.
