# Santo Agostinho (354–430): catálogo das fontes

Agostinho comentou **os 150 salmos** nas *Enarrationes in Psalmos* e cita os salmos em toda a
obra. Numeração sempre grega e latina (Vulgata): o nosso Sl 33 é o «Psalmus 32» dele.
Primeiro uso: Sl 33 (Vulgata 32), 2026-10-17 (`salmos/033/relatorio-agostinho.md`).

## 1. *Enarrationes in Psalmos* (todos os salmos)

- **Edições**: PL 36–37 (texto dos Maurinos, 1681, reimpresso por Migne); CCSL 38–40 (Dekkers–
  Fraipont, 1956); CSEL 93–95 (ed. crítica em curso; 93/1A = Sl 1–32 «expositiones»,
  93/1B = Sl 18–32 «sermones», ed. C. Weidmann). Para o site, citar o PL (domínio público).
- **Natureza**: para alguns salmos há mais de uma *enarratio*. As de Sl 1–32 que vêm primeiro
  (enarratio I) são **glosas curtas ditadas** (c. 392–394), uma ou duas linhas por versículo;
  as outras são **sermões pregados**, longos e vivos (o que mais serve ao leitor comum).

### 1.1 Latim: augustinus.it (Nuova Biblioteca Agostiniana)

- Padrão: `https://www.augustinus.it/latino/esposizioni_salmi/esposizione_salmo_NNN_testo.htm`
  (italiano: troca `latino` por `italiano`). **NNN não é o número do salmo**: é a ordem do
  arquivo, e os salmos com várias *enarrationes* ocupam vários arquivos. Tabela completa
  (salmo na numeração da Vulgata = arquivo):
  Sl 1-17 = 001-017; Sl 18 (I, II) = 018-019; Sl 19-20 = 020-021; Sl 21 (I, II) = 022-023;
  Sl 22-24 = 024-026; Sl 25 (I, II) = 027-028; Sl 26 (I, II) = 029-030; Sl 27-28 = 031-032;
  Sl 29 (I, II) = 033-034; Sl 30 (I, II, III, IV) = 035-038; Sl 31 (I, II) = 039-040;
  **Sl 32 (I, II, III) = 041-043**; Sl 33 (I, II) = 044-045; Sl 34 (I, II) = 046-047; Sl 35 = 048;
  Sl 36 (I, II, III) = 049-051; Sl 37-47 = 052-062; Sl 48 (I, II) = 063-064; Sl 49-57 = 065-073;
  Sl 58 (I, II) = 074-075; Sl 59-67 = 076-084; Sl 68 (I, II) = 085-086; Sl 69 = 087;
  Sl 70 (I, II) = 088-089; Sl 71-87 = 090-106; Sl 88 (I, II) = 107-108; Sl 89 = 109;
  Sl 90 (I, II) = 110-111; Sl 91-100 = 112-121; Sl 101 (I, II) = 122-123; Sl 102 = 124;
  Sl 103 (I, II, III, IV) = 125-128; Sl 104-112 = 129-137; Sl 113 (I, II) = 138-139;
  Sl 114-117 = 140-143; Sl 118: prólogo = 144, sermões I–XXXII = 145-176; Sl 119-150 = 177-208.
- Atenção aos rótulos: o augustinus.it chama de «enarratio II» e «III» o que o PL chama de
  «enarratio II, sermo 1» e «sermo 2» (caso do Sl 32). Conferir o título da página.
- O texto do augustinus.it é o dos Maurinos, com i/u modernizados (não usa *j*); as notas com
  as referências bíblicas ficam num arquivo à parte (`..._NNN_note.htm`). Pequenos erros de
  digitação existem (Sl 32, en. 2, s. 2, 10: «labis» por «tubis»): conferir no PL quando estranho.
- **Quando o site cai** (em 2026-10-17 respondia 503 o dia todo): a cópia do Internet Archive
  funciona, com o mesmo caminho:
  `http://web.archive.org/web/2016id_/http://www.augustinus.it/latino/esposizioni_salmi/esposizione_salmo_NNN_testo.htm`
  (o `id_` devolve o HTML original, em windows-1252). O índice com a tabela acima está em
  `.../esposizioni_salmi/sommario.htm` (cópia de 2024 boa; a de 2016 é página de erro).
  Script de conversão para Markdown usado no Sl 32: `aug2txt.py` (descrito no relatório).

### 1.2 Latim com colunas do PL: documentacatholicaomnia.eu (PDF do Migne)

- `https://www.documentacatholicaomnia.eu/02m/0354-0430,_Augustinus,_Enarrationes_In_Psalmos_%5B001-079%5D,_MLT.pdf`
  (PL 36, 87 MB) e `..._%5B080-144%5D,_MLT.pdf` (PL 37; o resto do PL 37, Sl 145–150, conferir).
  É o fac-símile com OCR ruim, mas os números de coluna do cabeçalho saem bem: serve para dar o
  «PL 36, col.». No Sl 32: PDF págs. 104–116 (índice 0), colunas 275–300. Com PyMuPDF
  (`fitz`), `page.get_text('words')` dá a posição x de cada parágrafo (coluna esquerda = ímpar,
  direita = par).

### 1.3 Traduções inglesas de domínio público (só para conferir)

- **NPNF** I/8 (1888, Schaff; resumo da tradução de Oxford): `https://www.newadvent.org/fathers/1801NNN.htm`,
  com **NNN = número hebraico** do salmo (o Sl 32 da Vulgata é `1801033`). Atenção: o NPNF corta
  muito; no Sl 32 só traz a enarratio I e omite os dois sermões. Também em
  `https://bkv.unifr.ch/works/cpl-283-1/versions/expositions-on-the-book-of-psalms/divisions` e
  `https://ccel.org/ccel/schaff/npnf108`.
- **Library of the Fathers** (Oxford, 1847–1857, 6 vols., tradução completa, com notas): numeração
  inglesa com «Lat.» ao lado. archive.org, texto OCR em `.../<id>/<id>_djvu.txt`:
  vol. I (Sl 1–37) `expositionsonboo01auguuoft`; vol. II (37–52) `expositionsonps02auguuoft`
  ou `25ALibraryOfFathersOfTheHolyCatholicV25`; vol. III (53–75) `expositionsonboo03auguuoft`;
  vol. IV (76–101) `expositionspsalm04auguuoft`; vol. V (102–125) `expositionsonthe05auguuoft`;
  vol. VI (126–150) `expositionsonboo06auguuoft` (identificadores dos vols. II–VI tirados da
  busca do archive.org, não abertos; conferir o volume no título).

## 2. Outras obras (onde procurar citações de um versículo)

Não há índice bíblico livre e completo das obras de Agostinho. O que funciona:

- **Busca no texto latino**:
  - The Latin Library (`https://www.thelatinlibrary.com/august.html`): *Confessiones*
    (`augustine/confN.shtml`), *De civitate Dei* (`civN.shtml`), *De Trinitate* (`trinN.shtml`),
    *De catechizandis rudibus*, *De fide et symbolo*, alguns sermões e cartas. Baixar tudo
    (58 páginas, 3,7 MB; arquivos em latin-1) e buscar com `grep -i -E` com variantes
    (`[uv]`, `c[oa]eli`, `i[uv]bil`): Civ. usa *u* por *v*.
  - Corpus Corporum (Zurique): API de busca de frase, sem login:
    `https://mlat.uzh.ch/php_modules/fulltext_search.php?&query="<frase>"&offset=0&limit=200&index_type=s`
    (XML; autor em `cc:author//cc:name`). Tem as *Confessiones*, mas **não** as *Enarrationes*
    nem os sermões (testado em 2026-10-17): serve para os outros autores latinos.
  - augustinus.it, obra a obra (mesma lógica de arquivos, mesma cópia no Internet Archive):
    `latino/confessioni/`, `latino/cdd/` (*De civitate Dei*), `latino/trinita/`,
    `latino/genesi_lettera/` (*De Genesi ad litteram*), `latino/dottrina_cristiana/`,
    `latino/lettere/`, `latino/commento_vsg/` (*In Iohannis evangelium tractatus*; o título da
    página diz outra coisa, conferir), `latino/discorsi/` (sermões).
  - **Sermões**: `latino/discorsi/discorso_NNN_testo.htm`, onde NNN também é a ordem do arquivo,
    não o número do sermão, porque entram os sermões «/A», «/B» (ex.: Sermo 9 = 010,
    Sermo 33 = 043, Sermo 34 = 045). O índice com a lista está em `latino/discorsi/sommario.htm`
    (na ordem: 1, 2, 3, 4, 4/A, 5, …); contar a posição.
- **Índices impressos** (a conferir, não abertos): o PL 46 traz os índices gerais dos Maurinos,
  com o índice dos lugares da Escritura citados em toda a obra (se houver PDF no
  documentacatholicaomnia, é o caminho mais rápido). O **Biblindex** (biblindex.org, Sources
  Chrétiennes) indexa citações bíblicas nos Padres; bloqueia `curl` (403), abrir no navegador.
- **Pistas temáticas já achadas** (servem para outros salmos):
  - saltério de dez cordas = Decálogo (3 + 7): Sermo 9, 6 e Sermo 33 (sobre Sl 143,9);
    *Confissões* III, 8, 16; En. in Ps. 32, II, s. 1, 6; En. in Ps. 143, 16 (conferidos); En. in Ps. 91, 5 (de memória, conferir).
  - cítara × saltério (embaixo/em cima: padecer/agir, carne/espírito): En. in Ps. 32, II, s. 1, 5;
    42, 5; 70, s. 2, 11 (conferidos); 56, 16; 80, 5; 150, 8 (de memória, conferir); 149, 8 (tímpano e saltério).
  - júbilo sem palavras: En. in Ps. 32, II, s. 1, 8; 99, 4–5 (conferidos); 46, 7; 94, 3 (de memória, conferir).
  - cântico novo = homem novo, caridade: Sermo 33 e 34; En. in Ps. 32, II, s. 1, 8; 95, 2; 149, 1–2.
  - «dixit et facta sunt» (Sl 32,9 = Sl 148,5): *Confissões* XI, 5, 7 e 7, 9; *De civitate Dei*
    XI, 9 e *De catechizandis rudibus* 17, 28 (estes citam o Sl 148).
- **Traduções inglesas de domínio público das outras obras** (newadvent, padrão
  `https://www.newadvent.org/fathers/<código>.htm`): Confissões 1101, Cartas 1102, Cidade de Deus
  1201, Doutrina cristã 1202, Trindade 1301, Enchiridion 1302, Sermões sobre o NT 1603,
  Tratados sobre João 1701, Comentário à 1 João 1702 (códigos de memória, conferir).

## 3. Pentateuco e Antigo Testamento (primeiro uso: Nm 12, 2026-10-17)

- **O Corpus Corporum tem as 140 obras dele no PL, inclusive as *Enarrationes* (obra 771, texto
  7329, e «[2]» 21501/21385) e os sermões** (775–784, 2519, 2528). A observação acima («não tem as
  *Enarrationes*») vale só para a **busca de frase**, que não as indexa; baixando os arquivos, tudo
  se acha com `grep`. Autor `900`; script `ccall.py` (baixa todas as obras de um autor, 6 em
  paralelo, ~10 min) descrito em `numeros/012/relatorio-origenes-agostinho.md` e em `latinos.md`.
  Achar um versículo: `grep -o -E "Num(er)?\.? ?XII\b[^;)]{0,15}"` nas notas (são poucas: Migne
  anota pouco nas obras de Agostinho), depois frases-chave da Vetus Latina dele.
- Obras (work → texto) úteis para o AT: *Quaestiones in Heptateuchum* 754 → **7312** (PL 34,
  547–824; questões curtas, quase sempre literais, livro a livro: I Gn, II Ex, III Lv, IV Nm a partir
  da linha «LIBER QUARTUS», V Dt, VI Js, VII Jz; cada questão começa com «[Ib. XII, 1.]»);
  CSEL 28/1 (Zycha, 1895, domínio público) no Corpus como texto **15028** (o mesmo arquivo traz
  as *Locutiones*), com página CSEL; *Locutiones in Heptateuchum* 753 → **7311** (só gramática,
  mas mostra a Vetus Latina dele); *De Genesi ad litteram* 744 → **7302** (livro XII = as visões,
  Moisés e Paulo); Cartas 742 → **7300** (Carta 147 *De videndo Deo* nas linhas ~29000–30500);
  *De Trinitate* 2456 → **7441** (II–III: as teofanias do AT); *Contra Faustum* 2447 → **7432**
  (defesa dos patriarcas e de Moisés contra os maniqueus; nada sobre Nm 12); *De civitate Dei*
  21481; *Contra Gaudentium* 2473 → 7458; *In Ioannis ev.* 765 → 7323.
- **Pseudo-Agostinho** (autor 1024, «Auctor incertus (Augustinus Hipponensis?)»): *Sermones
  supposititii de Scripturis* **7338** (PL 39; muitos de Cesário de Arles: conferir), *De
  mirabilibus sacrae Scripturae* **7315** (Agostinho Hibérnico, 655; questões literais sobre todo o
  AT), *Sermones ad fratres in eremo* **7388** (autor 1028?, medieval). Citar com a autoria certa.
- Pistas temáticas: os etíopes = as nações (En. in Ps. 71,12; 73,16; 67,40 de memória);
  a visão de Deus por Moisés (*Gen. ad litt.* XII, 26–28; Ep. 147, 13; *De Trin.* II, 16–17;
  *Contra Maximinum* I, 15); a mansidão de Moisés (*Contra Gaudentium* I, 19,20).

## 4. Salmo 33 da Vulgata (= Sl 34; primeiro uso 2026-10-17, `salmos/034/relatorio-agostinho.md`)

- **Só dois sermões, nenhuma glosa ditada**: arquivo 044 = sermo 1 (só o título, PL 36, 300–307),
  045 = sermo 2 (vv. 2–23, PL 36, 307–322). No PDF do PL 36 (§ 1.2): págs. 116–127 (índice 0).
  O NPNF (`1801034`) só traz o sermo 2, resumido e com a numeração um a menos.
- Sermões que comentam um salmo inteiro ou um versículo dele aparecem no título dos *Sermones de
  Scripturis* («De eo quod scriptum est in Psalmo XXXIII…» = Sermo 16, PL 38, 121): procurar
  `grep "SERMO .* Psalmo <número romano>"` no arquivo 776_7334 do Corpus Corporum.
- **Corpus Corporum, mais depressa**: baixar só as obras-chave em paralelo (10 por vez, ~3 min):
  work → texto: Cartas 742 → 7300; *De doctr. christ.* 747 → 7305; *De serm. Dom. in monte*
  749 → 7307; *In ep. Io.* 764 → 7322; *In Io.* 765 → 7323; *Enarrationes* 771 → 7329 (Sl 1–~75)
  e 21501 → 21385; *Sermones de sanctis* 775 → 7333, *de Scripturis* 776 → 7334, *de tempore*
  777 → 7335; *Confissões* 712 → 7270. As 140 em ordem levam mais de 30 min. As notas de Migne
  («NNN: (Psal. XXXIII, v)») usam a numeração da Vulgata com o título como v. 1 no Sl 33.
  Permalinks: `cps_2.AugHip.Confes2`, `.InEpJoA`, `.InJoEvT`, `.SeDeSc`, `.EnInPs`.
- Armadilha do `aug2txt.py`: não trocar `* *` por espaço (cola `**9.** *Inquisivi` em `**9.* …`).
- **Nm 13 (2026-10-17)**: as *Enarrationes* no Corpus são **dois textos**: 7329 (Sl 1–79, PL 36) e **21385**
  (Sl 80–150, PL 37); *De civitate Dei* = texto **21364**. Pistas temáticas: o nome de Josué = Jesus (Sermão 352, 4;
  *Contra Faustum* XVI, 19–20 e XII, 31; *Quaest. in Hept.* II, 103); Cristo, o cacho pendurado no madeiro
  (En. in Ps. 8, 2; *Contra Faustum* XII, 31 e 42; alusões em En. in Ps. 55, 4; 83, 1; Sermões 191, 1 e 267);
  a terra desejável desprezada por falta de fé (En. in Ps. 105, 22). Ver `../numeros/013/relatorio-origenes-agostinho.md`.
  Sermões fora das coleções dos Maurinos: «Sermones 1» (obra 2519 → texto 7504) e «Sermones 2» (2528 → **7513**,
  os quatro de A. Mai, autenticidade discutida; o III, sobre Caná, traz os dois carregadores do cacho de Nm 13,24).
  O `ccall` de todas as obras travou duas vezes depois da obra 2458: baixar as que interessam pelo número do texto.

## 5. Salmo 34 da Vulgata (= Sl 35; 2026-10-17, `salmos/035/relatorio-agostinho.md`)

- **Dois sermões, nenhuma glosa**: arquivo 046 = sermo 1 (vv. 1–10, PL 36, 322–333; imposto pelos
  bispos presentes), 047 = sermo 2 (vv. 11–28, PL 36, 333–341). O NPNF (`1801035`) traz os dois,
  numerados em seguida (1–12 e 13–27).
- **Colunas do PL sem o PDF**: o texto 7329 do Corpus Corporum tem as quebras `[page 0323]`; basta
  alinhar o começo de cada parágrafo do augustinus.it (letras normalizadas, *j→i*, *v→u*, janelas de
  25 caracteres, porque o OCR do Corpus erra: «cruet» por *eruet*).
- **Não baixar de novo**: as 140 obras do Corpus (texto PL) estão no scratchpad da conversa
  `94b210f9-de88-4ff1-a06d-f01e9346d6d5` (`scratchpad/dl/aug/<obra>_<texto>.txt`), dentro de
  `%LOCALAPPDATA%\Temp\claude\C--Users-geren-OneDrive-Documentos-Onedrive-do-Gere-Software-MEU-taioe\`
  (só no notebook; a pasta temporária pode ser limpa). Procurar ali antes de baixar.
- `aug2txt.py`: o número do parágrafo às vezes vem como `<A NAME>2</A></B>.`; e, ao tirar as
  notas, juntar `</I><I>` (senão sobra `* *` e `! **`).
- Pistas temáticas: «Dic animae meae: Salus tua ego sum» (Sl 34,3) é dos versículos que ele mais
  usa: *Confissões* I, 5, 5 e IX, 1, 1; En. in Ps. 32, II, s. 2, 17; 38, 20; 85, 9; Sermo 163, 12;
  Sermo 312, 3; Ep. 177, 1. «Omnia ossa mea dicent: Domine, quis similis tibi?» (Sl 34,10):
  *Confissões* V, 1, 1; VIII, 1, 1; IX, 1, 1; Sermo 224, 1 (aos recém-batizados); Sermo 46, 17;
  Ep. 149, 34. *In Io.* 10 foi pregado depois do canto do Sl 34 (vv. 13, 15, 16, 20, 27).
  O cilício/saco = a carne mortal de Cristo: En. in Ps. 29, II, 21; 34, s. 2, 3; 68, s. 1, 15.
  «Martyrem non facit poena, sed causa»: En. in Ps. 34, s. 2, 1 e 13; Sermões 275, 1 e 327, 1
  (estes com o Sl 42,1).

## Cartas de São Paulo

Tudo em `paulo.md` (o mapa das cartas: as obras de cada carta, a tabela das homilias de Crisóstomo e a pré-pesquisa de 2Cor 3–13).

## 6. Salmo 35 da Vulgata (= Sl 36; 2026-10-19, `salmos/036/relatorio-agostinho.md`)

- **Uma só *enarratio***, sermão ao povo: arquivo 048, PL 36, 341–354 (texto 342–354), vv. 2–13, sem
  comentar o título. NPNF `1801036` (16 §§, resumido). O [v 8.] do augustinus.it está em «Homines et
  iumenta», que no hebraico é o fim do v. 7; o resto coincide.
- **augustinus.it, outras obras** (todas com cópia no Internet Archive, `web/2016id_/`; NNN = ordem do
  arquivo, conferir o `<TITLE>`):
  - *Tratados sobre João*: `latino/commento_vsg/omelia_NNN_testo.htm`, **NNN = número do tratado** (013 = 13).
  - Cartas: `latino/lettere/lettera_NNN_testo.htm`, **NNN = número da carta + 1** a partir de certo ponto
    (`lettera_131` = Ep. 130; `lettera_130` = Ep. 129).
  - Sermões: `latino/discorsi/discorso_NNN_testo.htm`, pela lista de `discorsi/sommario.htm`
    (`grep -o 'discorso_[0-9]*_testo.htm">[^<]*'`): Sermo 23 = 029, 225 = 296, 233 = 328, 255 = 353,
    284 = 398, 306 = 433.
  - Opúsculos: `latino/<pasta>/<pasta>_libro.htm` (a página `<pasta>.htm` é só a moldura):
    `agone_cristiano`, `santa_verginita`.
- **Notas de Migne**: `(Psal. XXXV, n)` deu 108 notas em 30 obras; com o script `ctx.py` (scratchpad
  `a645f7af…/pesq-agostinho/scripts/`) cada ocorrência sai com obra, livro/tratado/sermão, parágrafo e
  coluna. Cuidado: a janela de 25 letras para achar a coluna final dá falso positivo em fórmulas
  repetidas («qui fecit caelum et terram»): procurar o fim **depois** do começo.
- Pistas temáticas (servem para outros salmos):
  - «Apud te est fons vitae, et in lumine tuo videbimus lumen» (Sl 35,10) é dos versículos que ele mais
    cita: *Confissões* IX, 10, 23 (Óstia) e XIII, 16, 19; *De Trinitate* VII, 3, 4; *In Io.* 13, 5;
    25, 17; 26, 4; 34, 3–5; Sermões 23, 225, 233, 284, 306; Ep. 130, 27; En. in Ps. 41, 2; 120, 5.
    Tema recorrente: aqui a fonte e a luz estão separadas, em Deus são uma coisa só.
  - «Homines et iumenta salvos facies… filii autem hominum» = Adão (homem, não filho de homem) e Cristo
    (Filho do homem): En. in Ps. 35, 12; Sermões 23, 11 e 233, 3; Ep. 140, 22; *In Io.* 34, 3–4. Deus
    cuida dos animais × «de bobus cura non est Deo»: En. in Ps. 145, 13–14.
  - Os mártires «ébrios» que não reconhecem a família (Sl 35,9 e Sl 22,5 «calix inebrians»): En. in
    Ps. 35, 14; Sermo 284, 2. A «sóbria embriaguez»: *De agone christiano* 9, 10.
  - «Non veniat mihi pes superbiae» = «ab occultis meis munda me» (Sl 18,13): En. in Ps. 18, 13;
    35, 17; o pé que se move é a soberba: En. in Ps. 120, 5; *De sancta virginitate* 52, 53 («pede
    humilitatis»); *In Io.* 25, 16–17.
  - Montes = apóstolos e pregadores, nuvens = pregadores (Sl 35,6–7 e Sl 120,1): En. in Ps. 35, 8–9;
    120, 4; *Confissões* XIII, 15, 18; Ep. 140, 71.
  - Não há citação do Sl 35 na *Cidade de Deus*, nem dos vv. 2–3 fora da *enarratio*.

## Por livro

O que é de um livro só (quem comenta que capítulo, o que se achou em cada um) fica no mapa do livro: `numeros.md`, `salmos.md`, `paulo.md`. Aqui ficam o acesso às fontes e o que vale para a Bíblia inteira (20/10/2026).
