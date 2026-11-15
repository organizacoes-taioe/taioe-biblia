# Pesquisa: Salmos 38 a 47 (comentários dos Padres e dos santos)

Pedido comum aos pesquisadores dos Salmos 38 a 47 (numeração hebraica; Vulgata e LXX 37 a 46), feitos
juntos em 15/11/2026. Cada pesquisador recebe dois salmos e cobre **todos os grupos** (Padres latinos e
gregos, orientais, medievais, santos modernos, Magistério e liturgia). O texto de cada salmo está em
`conteudo/salmos/0NN.json` (a tradução ainda está sendo revista; leia o salmo inteiro antes de
pesquisar). Todos têm um trecho só (`"trecho": "1"`), sem subtítulo.

**Numeração**: o título do salmo conta como versículo 1 quando existe (Nova Vulgata = hebraico). A
Vulgata e a LXX, que os Padres leem, têm o número do salmo um a menos (Sl 38 hebr. = Sl 37 Vulgata;
Sl 42 e 43 hebr. = Sl 41 e 42 Vulgata; Sl 47 hebr. = Sl 46), e os versículos em geral coincidem com os
da Nova Vulgata. Os achados levam o salmo e os versículos da Nova Vulgata (hebraicos): «Sl 42,2».
`pesquisa/fontes/salmos.md` § 1 tem a tabela.

**O que já está feito (ler antes)**: para cada salmo, `pesquisa/salmos/0NN/BASE.md` e os textos em
`base/` (Agostinho, *Enarrationes*; Ambrósio, *Enarrationes in XII psalmos* onde houver; Cassiodoro;
Tomás; Belarmino; Teodoreto; Atanásio; Cirilo; Orígenes e Eusébio de cadeia; Bruno Cartuxo e Bruno de
Segni; Pedro Lombardo; Afonso; a liturgia em `liturgia.md`), as pistas em `base/_pistas-*.md` e as
ausências em `base/_ausentes-*.md`. O mapa do livro `pesquisa/fontes/salmos.md`, os catálogos de
`pesquisa/fontes/` (`agostinho.md`, `gregos.md`, `latinos.md`, `modernos.md`, `orientais.md`,
`escriva.md`) e `pesquisa/COMO-PESQUISAR.md`. O modelo de pesquisa completa de um salmo é o Sl 37:
`pesquisa/salmos/037/achados-*.json` e `relatorio-*.md` (os métodos e caches estão neles). Os caches já
baixados estão em `pesquisa/cache/` (Corpus Corporum, Corpus Thomisticum, Divinum Officium, Francisco
de Sales, Granada, Lourenço de Bríndisi, Belarmino, a lista dos documentos dos Papas: ver os relatórios
de Nm 20–25 e do Sl 37, § «Método e caches»).

**Agostinho é o óbvio** e já está em `base/`: no máximo um quarto dos achados de cada salmo. O tempo
vai para o que não é óbvio: homilias inteiras dos gregos (Crisóstomo comentou os Sl 41 e 43–49 da LXX =
42 e 44–50 hebr.; Basílio, o Sl 44 e 45 da LXX = 45 e 46 hebr.; Hilário, onde houver), citações em
sermões, cartas e tratados (Ambrósio, Jerônimo, Gregório Magno, Bernardo, Leão, Cesário), santos
modernos (Francisco de Sales, Teresa, João da Cruz, Afonso, Newman, Teresinha, Josemaria Escrivá pelo
índice `pesquisa/fontes/escriva.md`), as catequeses de João Paulo II e Bento XVI (ciclo de Laudes e
Vésperas, 2001–2006, quando o salmo estiver ali; com direito autoral: citação curta), o Catecismo, o
Missal (o *Iudica me* e o *Introibo* do Sl 43 nas orações ao pé do altar; o Sl 42 na Vigília Pascal e
no batismo; o Sl 47 na Ascensão; o Sl 45 nas festas de Nossa Senhora e das virgens; o Sl 40,7-9 na
Anunciação e em Hb 10).

Leituras conhecidas, para orientar (não para forçar): **Sl 38** (penitencial; Davi doente pelo
pecado; o «seta» de Deus; os amigos que se afastam; o silêncio diante dos acusadores, Cristo na
Paixão). **Sl 39** («Guardarei os meus caminhos para não pecar com a língua»: Ambrósio abre o *De
officiis* com ele; o silêncio e a palavra; a brevidade da vida, «um palmo»; «hóspede e peregrino»,
Hb 11,13). **Sl 40** («Esperei, esperei no Senhor»; o lodo e a rocha; o cântico novo; «Não quiseste
sacrifício… Eis que venho», Hb 10,5-9, a Encarnação e a obediência de Cristo, a Anunciação; «no rolo
do livro está escrito de mim»). **Sl 41** («Feliz quem pensa no pobre»; o amigo que comia o meu pão
e levantou contra mim o calcanhar, Jo 13,18, Judas; a doxologia que fecha o primeiro livro dos
Salmos). **Sl 42–43** (um só poema com o refrão «Por que estás abatida, ó minha alma?»; o cervo e as
fontes, o batismo e a sede de Deus; «Quando irei ver a face de Deus?»; «um abismo chama outro
abismo»; «Envia a tua luz e a tua verdade»; «Introibo ad altare Dei… ad Deum qui laetificat
iuventutem meam»). **Sl 44** (os feitos dos pais; a derrota sem culpa; «por tua causa somos mortos
todo o dia», Rm 8,36, os mártires; «Desperta! Por que dormes, Senhor?», Jesus na barca). **Sl 45**
(o cântico das núpcias do rei: «Transborda do meu coração uma palavra boa», o Pai que gera o Verbo;
«o mais belo dos filhos dos homens»; «o teu trono, ó Deus, é eterno», Hb 1,8-9; «ungiu-te com o óleo
da alegria»; a rainha à tua direita, a Igreja e Maria; «Escuta, filha, e vê… esquece o teu povo», as
virgens; «toda a glória da filha do rei é interior»). **Sl 46** («Deus é o nosso refúgio e a nossa
força»; o rio cujos braços alegram a cidade de Deus; «Parai e sabei que eu sou Deus», *vacate et
videte*, a contemplação). **Sl 47** («Povos todos, batei palmas»; «Deus sobe entre aclamações», a
Ascensão; o rei de toda a terra; os príncipes dos povos reunidos ao povo do Deus de Abraão).

**Meta** (regra do Gere, 20/10: «poucos e diferentes»; o capítulo fica entre uns 20 e 35
comentários): cada pesquisador entrega por salmo **de 22 a 35 achados bons e variados** (o Sl 43, de 12
a 20), espalhados pelos versículos, de autores diversos, cada um dizendo algo que os outros não dizem.
Sem cota de orientais ou ocidentais: o melhor. O Gere excluiu antes o que «não ajuda na compreensão do
trecho», o que «parece fazer sentido apenas dentro do contexto» da obra, o «muito hipotético» e o
«confuso»: prefira o que ilumina o versículo e a vida cristã, sozinho, fora da obra de onde veio; o
excerto começa pela frase que situa o leitor (a palavra do salmo que o Padre comenta). Evitar a
alegoria solta, palavra por palavra ou número por número. Excerto com sentido completo, de 2 a 8
frases.

Nomes: os do nosso texto (Coré, Jacó, Hermon, Misar, Jordão, Tiro, Ofir, Abraão…). A citação bíblica
dentro do comentário segue o texto que o Padre leu.

**Proibido no site** (só pista no relatório): os siríacos fora da comunhão com Roma (Dionísio bar
Salibi, Filoxeno de Mabug, Narsai, Isho`dad de Merv, Teodoro bar Koni, Timóteo II), Isaac de Nínive,
Gregório de Tatev, os hereges e os não cristãos (Fílon, Josefo, os rabinos, Apolinário, Lutero,
Calvino), e o pseudo-Basílio dado como Basílio (pode entrar só como «homilia atribuída a São Basílio»,
se for muito boa). Textos com direito autoral (Papas recentes, LEV, edições críticas recentes): no
máximo duas ou três frases no `original`, `"direitos": "citação curta"`. O `conferir` recusa excerto
repetido de outro capítulo: não entregar de novo o que já está em `pesquisa/salmos/03{3..7}/achados-*.json`
nem nos achados dos outros pesquisadores deste lote (Sl 42 e 43 são vizinhos: combinar pelos versículos).

## Formato da entrega

Para cada salmo: `pesquisa/salmos/0NN/achados-geral.json`, uma lista de objetos com `id`
(minúsculas, sem acento, **até 61 caracteres**, único: `<autor>-<obra>-<passagem>-<tema curto>`),
`autor`, `autor_id` (o de `ferramentas/autores.json`; autor novo: dizer no relatório o nome, as
datas, o «sobre» e se é oriental), `datas`, `titulo_autor`, `obra` (título em português e, entre
parênteses, o original), `passagem` (exata), `edicao`, `trecho` (`"1"`), `versiculos`, `lingua`,
`original` (o trecho na língua original, conferido letra a letra na fonte; `[...]` onde se corta),
`fonte_url` (https, o texto original na internet, de preferência na página), `traducao_pt` (tradução
nossa, do original, em português do Brasil de hoje, sem mesóclise, sem pronome contraído, sem uso
europeu; sem notas do pesquisador entre colchetes), `temas` (1 ou 2 rótulos curtos), `resumo` (uma
frase), `relevancia` (1 a 3) e `direitos`. Mais `pesquisa/salmos/0NN/relatorio-geral.md` (o que
entrou, em uma linha cada; como se procurou; o que não existe; «Para outros capítulos») e os originais
que não estão em `base/` em `pesquisa/salmos/0NN/textos/<autor>-<obra>-NN.md`. Modelo:
`pesquisa/salmos/037/achados-latinos.json` e `relatorio-latinos.md`.
