# Gênesis 1: relatório da pesquisa nos orientais não gregos e na liturgia oriental

Pesquisa de 2026-10-25. **19 achados** em `achados-orientais.json` (trecho 1: 5; trecho 2: 3; trecho 3: 2; trecho 4: 1;
trecho 5: 8). Textos originais em `base/` (cabeçalho do `COMO-PESQUISAR.md`): `efrem-comentario-genesis.md`,
`efrem-hino-natividade-26.md`, `efrem-discurso-a-hipacio-4.md`, `efrem-atribuido-hinos-epifania-8.md`,
`afraates-demonstracao-6.md`, `afraates-demonstracao-14.md`, `jaco-de-sarug-hexaemeron.md`,
`jaco-de-sarug-sobre-o-amor-de-deus.md`, `diadoco-capitulos-gnosticos.md`, `eucologio-evlogitaria-defuntos.md`,
`triodio-1876.md`, `nerses-shnorhali-confesso-com-fe.md`; mais `_pistas-orientais.md` e `_ausentes-orientais.md`.

Scripts novos em `pesquisa/ferramentas/base/` (capítulo como parâmetro, uso no topo):
- `gen-orientais-efrem.py <cap>`: o Comentário de Efrém ao Gênesis inteiro (Assemani I, 1737), corte do latim pelo OCR e os
  trechos conferidos na imagem; `--ver a b` ajuda a pôr as âncoras de um capítulo novo (só o cap. 1 está em `CORTES`);
- `gen-orientais-corpus.py <cap>`: as citações de Gn <cap> (Peshitta) no Digital Syriac Corpus; `--kw` (palavra sem vogais)
  e `--bloco` (ler um texto). Clona o corpus em `cache/genesis/orientais/sc` (fora do git);
- `gen-orientais-gravar.py <cap>`: grava os textos escolhidos (lista `ITENS`, por capítulo).

## Onde se procurou

- **Digital Syriac Corpus** (632 textos): n-gramas de Gn 1 na Peshitta e palavras-chave (ܡܪܚܦ «pairar», ܒܨܠܡܢ, ܨܠܡܐ,
  ܢܗܝܪ̈ܐ, ܬܘܗ ܘܒܘܗ…), em Afraates, Efrém (Nísibe, Natividade, refutações em prosa), Jacó de Sarug (39 memre), Isaac de
  Nínive, *Liber Graduum*, Rábula, Balai; Narsai, bar Salibi e Timóteo II só como pista.
- **Efrém, Comentário ao Gênesis**: o texto autêntico existe só no Vat. sir. 110. A edição crítica (R.-M. Tonneau, CSCO
  152–153, 1955) **tem direito autoral** (no archive.org, só empréstimo: `ingenesimetinexo0000ephr`). Usou-se a edição
  romana (Assemani/Benedetti, *Opera omnia syr.-lat.* I, Roma 1737, p. 1–115), siríaco com latim ao lado: o siríaco é miúdo
  e não deu para transcrever com segurança; os achados citam o **latim de Benedetti**, conferido na imagem. Esse latim é
  livre: antes de publicar, convém conferir o sentido no siríaco da mesma página.
- **Bedjan, *Homiliae selectae* de Jacó de Sarug III (1907)**: o Hexaémeron abre o volume. OCR do archive.org só para achar as
  páginas; os trechos usados foram **lidos na imagem e transcritos sem vogais** (p. 70 e 108): conferir antes de publicar.
  Páginas: page/n = p. + 19 (n89 = p. 70; n127 = p. 108).
- **Hinos atribuídos a Efrém** em Lamy I–II (1882–1886) e NPNF II/13 (1898); **Mitchell** (1912) para as refutações em prosa.
- **Liturgia bizantina**: a biblioteca AGES (grego de todos os livros litúrgicos, clonada em `cache/genesis/orientais/ages`),
  conferida no Eucológio de Veneza (1862) e no Triódio de Veneza (1876), no archive.org.
- **Diádoco**: edição de Weis-Liebersdorf (Teubner, 1912), a única grega em domínio público (a PG 65 só tem o latim).
- **Armênio**: Nerses Shnorhali, *Preces* poliglotas (Veneza 1882) e Wikisource armênio.
- Não procurados nesta rodada: Romano, o Melodista; a Grande Bênção das Águas; Gregório de Narek; coptas e etíopes;
  *Apophthegmata*; Pseudo-Macário (ver `_pistas-orientais.md`).

## O «sírio» de Basílio (Gn 1,2) não é o Comentário de Efrém

O pedido manda verificar se o «sírio» de Basílio, *Hex.* 2, 6 (o Espírito que «aquecia» as águas como a ave os ovos) é
Efrém. **No Comentário ao Gênesis, Efrém lê ܪܘܚܐ como vento, e diz que não é o Espírito Santo** (Assemani I, p. 8: «Etsi
Interpretes nonnulli his verbis Spiritum Sanctum indicari crediderint… nihilominus… spiritus seu ventus»; «Spiritus ergo
ille flabat super aquas»). Jacó de Sarug diz o mesmo no Hexaémeron (p. 23, pelo OCR: «vento criado, não o Santo, como se
pensou»). A imagem da ave que choca, aplicada ao Espírito Santo e ao batismo, aparece sim no siríaco: no hino 8 da Epifania
atribuído a Efrém (achado do trecho 4), em Jacó de Edessa e em Dionísio bar Salibi (só pistas). A hipótese corrente
identifica o «sírio» com Eusébio de Emesa (ter Haar Romeny, *A Syrian in Greek Dress*, 1997; a conferir). **O achado dos
gregos `basilio-hex-2-6-o-espirito-choca-as-aguas` diz «provavelmente Santo Efrém»: convém trocar por «um cristão de língua
siríaca».** O mesmo vale para `agostinho-gnlitt-1-18-36`, se o comentário o chamar de Efrém.

## Achados (19)

Trecho 1 (vv. 1–5)
1. `efrem-coment-gn-1-1-sem-alegorias` (Assemani I, p. 6; latim): o céu e a terra são reais, feitos do nada; não procurar
   alegorias nos seis dias; nada do que veio depois é eterno. Relevância 2.
2. `efrem-coment-gn-1-2-as-trevas-nao-sao-eternas` (p. 13; latim): as trevas são sombra que nasce com as criaturas e a luz
   desfaz, não um princípio eterno inimigo das criaturas (contra Mani e Bardesanes; à margem, «Taxat Manichaeos»). 2.
3. `afraates-dem-6-14-o-espirito-paira-sobre-a-agua` (siríaco): na invocação do batismo o Espírito abre os céus, desce e paira
   sobre as águas, e os batizados se revestem dele. 2. Parecido com Tertuliano (latinos) e a bênção da água (modernos).
4. `efrem-hino-nat-26-o-primeiro-dia` (estr. 3–4; siríaco): a luz do 1º dia, figura do Natal que rasga as trevas do coração;
   o dia do Salvador, árvore plantada no mundo (morte raiz, ressurreição copa, corpo fruto). 2.
5. `nerses-confesso-com-fe-2-criador-da-luz` (armênio): a Trindade «criadora da luz e que expulsa as trevas» expulse da alma
   as trevas do pecado. 2. Diz quase o mesmo que o 4: se ficar um só, Efrém.

Trecho 2 (vv. 6–13)
6. `efrem-coment-gn-1-11-plantas-ja-crescidas` (p. 15–17; latim): plantas de um instante com aparência de meses, árvores de
   um dia carregadas como de anos; a terra já preparava o pasto e os frutos para os que viriam; tudo «adulto e recém-nascido»
   ao mesmo tempo. 3. Toca Basílio 5, 6 (gregos), mas o ponto é outro.
7. `efrem-hino-nat-26-o-terceiro-dia` (estr. 6): quem fez brotar botões e flores nasceu da Virgem, terra sedenta, e se tornou
   a Flor santa. 2.
8. `afraates-dem-14-36-o-mar-obedece-a-palavra` (siríaco): toda criatura cumpre a ordem, só o homem desobedece; o mar fica no
   limite pela palavra, não pela natureza (prova: o dilúvio, quando Deus a retirou). 2. **Parecido com Ambrósio, *Hex.* 3, 1
   (latinos, «as águas obedecem»)**: o próprio de Afraates é o «não pela natureza, mas pela palavra».

Trecho 3 (vv. 14–19)
9. `efrem-hipacio-4-o-homem-maior-que-o-sol` (siríaco, Mitchell 1912): contra os maniqueus que adoravam o sol: os luzeiros
   servem; o que é grande pela palavra e pelo conhecimento vale mais que o que é grande pela luz. 3.
10. `jaco-sarug-hexaemeron-4-a-lampada-da-criacao` (Bedjan III, p. 70; transcrição da imagem): o sol é lâmpada que Deus
    acendeu na casa da criação; todo dia pede à bondade dele o azeite da luz. 2.

Trecho 4 (vv. 20–23)
11. `efrem-atrib-epifania-8-16-o-espirito-que-choca` (inglês de 1898, conferido com o latim de Lamy): o Espírito que chocava
    as águas, que deram à luz répteis, peixes e aves, choca as águas do batismo, que dão à luz «águias», «peixes» e
    serpentes que viram pombas. 3. Autoria discutida (Beck: de um discípulo, séc. V): «atribuído». O siríaco está em Lamy
    I, col. 85, só na imagem.

Trecho 5 (vv. 24–31)
12. `efrem-hipacio-4-a-imagem-do-dominio` (siríaco, Mitchell 1912): «à nossa imagem» = à imagem da autoridade de Deus; o
    senhorio sobre todos os animais, até os ferozes, perdido no pecado. 3. É a leitura siríaca clássica; **Teodoreto
    (gregos) e Beda (latinos) dizem coisa parecida**: Efrém é o mais antigo e o mais direto.
13. `efrem-coment-gn-1-28-a-bencao-antes-da-queda` (p. 19–20; latim): Deus abençoou na terra, antes do pecado, para que a culpa
    não anulasse as bênçãos; a bênção da graça vem antes e lava a maldição da justiça. 3. Escrivá (modernos) também nota a
    bênção antes do pecado, mas para o trabalho.
14. `jaco-sarug-hexaemeron-6-a-cidade-e-a-imagem-do-rei` (p. 108; transcrição): o mundo, cidade cheia de belezas onde devia
    erguer-se a imagem do Rei. 2. **Parecido com Nissa, *De opif.* 2 (gregos)**: se ficar um só, Nissa.
15. `jaco-sarug-amor-de-deus-imagem-do-filho` (Bedjan I, p. 614; siríaco do corpus): modelado à imagem do Filho, só te pareces
    com ele amando quem te odeia. 2.
16. `diadoco-cap-89-a-graca-pinta-a-semelhanca` (grego, 1912): o batismo devolve a imagem; a graça pinta a semelhança cor sobre
    cor, e a última cor é o amor. 3. Ambrósio (latinos) também compara o homem a uma pintura, com outro sentido.
17. `liturgia-evlogitaria-sou-imagem-da-tua-gloria` (Eucológio 1862, p. 407): «sou imagem da tua glória, ainda que traga as
    marcas das quedas»; reconduz-me à semelhança. 3. Diz o que Bernardo e Agostinho dizem (a imagem que o pecado não apaga),
    na voz do moribundo.
18. `liturgia-kontakion-ortodoxia-a-imagem-restaurada` (Triódio 1876, p. 126): o Verbo encarnado restaurou a imagem manchada
    e a uniu à beleza divina. 2.
19. `liturgia-hora-sexta-o-sexto-dia` (Triódio 1876, p. 71): no sexto dia e na sexta hora, Cristo pregou na cruz o pecado de
    Adão. 2. Na mesma segunda-feira da 1ª semana da Quaresma as Vésperas leem Gn 1,1-13.

Fora dos achados, como reserva: Diádoco, cap. 4 (repete Basílio sobre imagem e semelhança); as outras estrofes do hino 26 da
Natividade (a do 4º dia repete Agostinho, Sermão 190); Rábula (repete Afraates). Ver `_pistas-orientais.md`.

## Para a conversa principal

- **Autores para `ferramentas/autores.json`**: «São Diádoco de Fótice» é novo (sugestão de «sobre»: «bispo de Fótice, no Epiro
  (séc. V), mestre da vida espiritual»). «Liturgia bizantina» existe, mas o «sobre» fala só das exéquias: generalizar
  («a liturgia das Igrejas de rito bizantino, rezada também nas Igrejas católicas orientais»). «Santo Efrém, o Sírio
  (atribuído)» existe com «sobre» das glosas da cadeia: para o hino da Epifania, «hino da Epifania de autoria discutida».
  «São Jacó de Sarug», «Afraates, o Sábio Persa», «São Nerses Shnorhali» e «Santo Efrém, o Sírio» já existem. Os
  `autor_id` seguem os já usados (`efrem`, `afraates`, `jaco-sarug`, `shnorhali`); novos: `diadoco`, `liturgia-bizantina`.
- Diádoco está no catálogo dos orientais (`fontes/orientais.md`, ascetas), mas o pedido o cita no trecho 5 sem grupo:
  se os gregos também o trouxerem, ficar com um só.
- Direitos: tudo é domínio público. O siríaco do hino 26 vem da edição de Beck (1959) pelo Digital Syriac Corpus (CC BY),
  como nos capítulos anteriores; o mesmo hino está em Lamy II (1886), col. 493–500.

## Armadilhas

- O OCR siríaco do archive.org (Assemani, Lamy, Bedjan) só serve para achar a página; os números de página do OCR de
  Bedjan erram (lê «88» por 68, «270» por 70). Conferir sempre o cabeçalho na imagem.
- Assemani I: page/n = p. + 20 no começo do volume (n26 = p. 6, n38 = p. 18). Logo depois do Comentário de Efrém (p. 116 ss.)
  vêm os escólios de **Jacó de Edessa** (miafisita), que dizem o contrário de Efrém sobre Gn 1,2: não confundir.
- Os hinos da Natividade têm duas numerações: Beck (e o corpus) 26 = NPNF 19.

## Para outros capítulos

- **Gn 2,1-3** (o sétimo dia): Efrém, hino 26 da Natividade, estr. 10 (o sábado, descanso para homens e animais); Efrém,
  Comentário (Assemani I, p. 20 ss.: Deus não descansa por cansaço; o sábado, figura do verdadeiro sábado); Afraates,
  Dem. 13 (Sobre o sábado); Jacó de Sarug, Hexaémeron, 7º dia (Bedjan III, no fim do ciclo).
- **Gn 2,7**: Afraates, Dem. 6, § 14 (o primeiro nascimento, «alma vivente», e o segundo, na água); Jacó de Sarug,
  Hexaémeron, 6º dia (p. 112–114, pelo OCR: Adão modelado da terra).
- **Gn 2–3**: Efrém, Hinos sobre o Paraíso (Beck, CSCO 174, com direito; Assemani III, com latim); *Liber Graduum*, memra 21
  (a árvore de Adão); Efrém, hino 26 da Natividade, estr. 8–9 (a serpente; Adão envenenado e o remédio da vida); o Triódio
  do Domingo do Perdão (a expulsão de Adão); Romano, o Melodista (pista).
- **Gn 6–8** (o dilúvio): Afraates, Dem. 14, § 36 (Deus tirou a palavra das mãos do abismo; o firmamento se rompeu).
