# Pesquisa: Salmos 48 a 57 (comentários dos Padres e dos santos)

Pedido comum aos pesquisadores dos Salmos 48 a 57 (numeração hebraica; Vulgata e LXX 47 a 56), feitos
juntos em 16/11/2026, no mesmo esquema dos Salmos 38 a 47 (`PEDIDO-38-47.md`). Cada pesquisador recebe
seus salmos e cobre **todos os grupos** (Padres latinos e gregos, orientais, medievais, santos modernos,
Magistério e liturgia). O texto de cada salmo está em `conteudo/salmos/0NN.json` (a tradução ainda está
sendo revista; leia o salmo inteiro antes de pesquisar). Todos têm um trecho só (`"trecho": "1"`), sem
subtítulo.

**Numeração**: o título do salmo conta como versículo 1 (ou 1 e 2) quando existe (Nova Vulgata =
hebraico). A Vulgata e a LXX, que os Padres leem, têm o número do salmo um a menos (Sl 48 hebr. = Sl 47
Vulgata; Sl 51 hebr. = Sl 50 Vulgata, o *Miserere*; Sl 57 hebr. = Sl 56), e os versículos em geral
coincidem com os da Nova Vulgata. Os achados levam o salmo e os versículos da Nova Vulgata (hebraicos):
«Sl 51,12». `pesquisa/fontes/salmos.md` § 1 tem a tabela.

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
vai para o que não é óbvio: homilias inteiras dos gregos (Crisóstomo comentou os Sl 47–49 da LXX = 48–50 hebr., e há
a homilia sobre o Sl 50 LXX = 51 hebr.; as duas «In Psalmum 50» de `base/` são espúrias: só como
«homilia atribuída a São João Crisóstomo», se forem muito boas; Basílio, o Sl 48 da LXX = 49 hebr.;
Ambrósio, *Enarrationes*, Sl 47 e 48 Vulgata = 48 e 49 hebr.; Hilário, *Tractatus*, Sl 51–56 Vulgata =
52–57 hebr.), citações em
sermões, cartas e tratados (Ambrósio, Jerônimo, Gregório Magno, Bernardo, Leão, Cesário), santos
modernos (Francisco de Sales, Teresa, João da Cruz, Afonso, Newman, Teresinha, Josemaria Escrivá pelo
índice `pesquisa/fontes/escriva.md`), as catequeses de João Paulo II e Bento XVI (ciclo de Laudes e
Vésperas, 2001–2006, quando o salmo estiver ali; com direito autoral: citação curta), o Catecismo, o
Missal (o Sl 51 na Quarta-feira de Cinzas e no *Lavabo*, «Lava-me, Senhor, da minha culpa»; o «Senhor,
abre os meus lábios», 51,17, que abre a Liturgia das Horas; o Sl 51 na Vigília Pascal depois da 7ª
leitura, quando não há batismo; o Sl 50 e o «sacrifício de louvor»). No Sl 51, o *Miserere*, a tradição
é imensa: escolher o melhor e o mais variado, sem repetir a mesma ideia (o pecado original no v. 7, o
hissopo e a neve no v. 9, o «coração puro» e o «espírito firme» no v. 12, o «espírito contrito» no v. 19),
e procurar também os santos que o rezaram (Tomás More, Teresa, Afonso, Josemaria Escrivá).

Leituras conhecidas, para orientar (não para forçar): **Sl 48** (Sião, «a cidade do grande rei», Mt
5,35; os reis que viram e fugiram; «como ouvimos, assim vimos»; «meditamos a tua misericórdia no meio do
teu templo», o intróito do 14º domingo comum, *Suscepimus*, e a Apresentação do Senhor; a Igreja, cidade
de Deus). **Sl 49** («Ouvi isto, povos todos»: Basílio e Ambrósio; as riquezas e a morte; «ninguém pode
resgatar o irmão», só Cristo é o resgate; «o homem na honra não permanece, é como os animais que
perecem»; «Deus resgatará a minha alma do poder do Xeol»). **Sl 50** (Deus convoca céu e terra para o
juízo do seu povo; «não te repreendo pelos teus sacrifícios»; «se eu tivesse fome, não to diria»;
«oferece a Deus um sacrifício de louvor», Hb 13,15, a Eucaristia; «tu odeias a disciplina e lanças às
costas as minhas palavras»; «quem oferece louvor me honra»). **Sl 51** (o *Miserere*: Davi depois de
Natã, 2Sm 12; «pequei contra ti, contra ti só»; «eu nasci na culpa», o pecado original; «tu amas a
verdade no íntimo»; «asperge-me com o hissopo… mais branco que a neve», o batismo e a penitência; «cria
em mim um coração puro»; «não retires de mim o teu santo Espírito»; «ensinarei aos transgressores os
teus caminhos»; «Senhor, abre os meus lábios»; «o sacrifício a Deus é um espírito contrito»; «edifica
os muros de Jerusalém»). **Sl 52** (Doeg, o edomita, que denunciou Davi e matou os sacerdotes de Nob, 1Sm
22; a língua como navalha afiada; o rico que confiava nas riquezas; «eu, como oliveira verdejante na
casa de Deus»). **Sl 53** (o mesmo que o Sl 14, com «Deus» por «o Senhor»: «Diz o insensato no seu
coração: Não há Deus», que Santo Anselmo comenta no *Proslogion* 2–4; «não há quem faça o bem, nem um
só», Rm 3,10-12; «Deus olha do céu sobre os filhos dos homens»). **Sl 54** (os zifeus que denunciaram
Davi a Saul, 1Sm 23,19; «Ó Deus, salva-me pelo teu nome»; «Deus é o meu auxílio»; «de bom grado te
oferecerei sacrifícios»). **Sl 55** («Quem me dera asas como a pomba, voaria e acharia repouso», a fuga
para o deserto, a vida monástica; o amigo traidor, «tu, homem igual a mim, meu companheiro e meu
íntimo», Judas; «à tarde, de manhã e ao meio-dia», as horas da oração; «lança sobre o Senhor o teu
fardo», 1Pd 5,7). **Sl 56** (Davi preso pelos filisteus em Gat, 1Sm 21; «quando tenho medo, confio em
ti»; «em Deus confio e não temo: que pode fazer-me um homem?»; «recolhe as minhas lágrimas no teu odre:
não estão no teu livro?»). **Sl 57** (Davi na caverna, fugindo de Saul, 1Sm 22 e 24; «à sombra das tuas
asas me refugio até que passe a desgraça»; «firme está o meu coração»; «Desperta, minha glória;
despertai, harpa e cítara; quero despertar a aurora», que os Padres leem da Ressurreição; «eleva-te
acima dos céus, ó Deus»).

**Meta** (regra do Gere, 20/10: «poucos e diferentes»; o capítulo fica entre uns 20 e 35
comentários): cada pesquisador entrega por salmo **de 22 a 35 achados bons e variados** (o Sl 51, de 40
a 55; os Sl 53 e 54, curtos, de 12 a 20), espalhados pelos versículos, de autores diversos, cada um
dizendo algo que os outros não dizem.
Sem cota de orientais ou ocidentais: o melhor. O Gere excluiu antes o que «não ajuda na compreensão do
trecho», o que «parece fazer sentido apenas dentro do contexto» da obra, o «muito hipotético» e o
«confuso»: prefira o que ilumina o versículo e a vida cristã, sozinho, fora da obra de onde veio; o
excerto começa pela frase que situa o leitor (a palavra do salmo que o Padre comenta). Evitar a
alegoria solta, palavra por palavra ou número por número. Excerto com sentido completo, de 2 a 8
frases.

Nomes: os do nosso texto (Coré, Sião, Társis, Asaf, Davi, Natã, Betsabé, Doeg, Saul, Aquimelec, os zifeus, Gat, os filisteus…). A citação bíblica
dentro do comentário segue o texto que o Padre leu.

**Proibido no site** (só pista no relatório): os siríacos fora da comunhão com Roma (Dionísio bar
Salibi, Filoxeno de Mabug, Narsai, Isho`dad de Merv, Teodoro bar Koni, Timóteo II), Isaac de Nínive,
Gregório de Tatev, os hereges e os não cristãos (Fílon, Josefo, os rabinos, Apolinário, Lutero,
Calvino), e o pseudo-Basílio dado como Basílio (pode entrar só como «homilia atribuída a São Basílio»,
se for muito boa). Textos com direito autoral (Papas recentes, LEV, edições críticas recentes): no
máximo duas ou três frases no `original`, `"direitos": "citação curta"`. O `conferir` recusa excerto
repetido de outro capítulo: não entregar de novo o que já está em `pesquisa/salmos/0{33..47}/achados-*.json`
nem nos achados dos outros pesquisadores deste lote (o mesmo sermão que comenta dois salmos fica só num).

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
