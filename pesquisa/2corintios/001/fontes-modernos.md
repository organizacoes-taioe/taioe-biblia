# Fontes modernas para as cartas de São Paulo (grupo «modernos»)

Aprendido em 2Cor 1 (2026-10-18). Para juntar depois a `../../fontes/modernos.md`.

## 1. Os santos que comentam Paulo (e como achar o lugar)

- **São John Henry Newman**: muitos *Parochial and Plain Sermons* têm por texto um versículo de Paulo.
  Baixar as ~260 páginas do newmanreader (`https://www.newmanreader.org/works/parochial/volume<N>/sermon<M>.html`,
  `…/works/occasions/sermon<N>.html`, `…/works/subjects/sermon<N>.html`, `…/works/discourses/discourse<N>.html`;
  só `https://`) e procurar a referência como Newman escreve: **`2 Cor. i. 4`** (capítulo em romanos
  minúsculos, versículo em arábicos), e frases da King James («God of all comfort», «earnest of the Spirit»)
  e da Douai (nos sermões católicos: «God of all consolation», «weary even of life»). A cópia já baixada
  (com `.txt`) está no scratchpad da conversa de Nm 14 (`…/639cd05d-…/scratchpad/dl/newman/`), enquanto
  existir. Para 2Cor 1: PPS V,17 (1,12), PPS V,21 (1,4), *Occasions* 8 (1,3-4).
- **São Francisco de Sales**: o *Index scripturaire* do t. XXVII da edição de Annecy dá tudo (já descrito em
  `../../fontes/modernos.md` § 11). Para Paulo, a seção «DEUXIÈME ÉPITRE AUX CORINTHIENS» está na p. 296–297
  do índice (PDF p. 289); o `pdftotext` mistura as duas colunas: **renderizar a página** com PyMuPDF
  (`fitz`, `get_pixmap(dpi=110)`) e ler a imagem. A margem dos tomos traz «II Cor., i, 3-5». OCR ruim nos
  t. VII, IX, X, XX, XXIII, XXIV (letras separadas); o t. V (*Traité* II) não tem camada de texto.
  Baixar os PDFs com Python (`urllib`, trocando `'` por `%27` no nome do t. II), não com `xargs sh -c`.
- **Santo Afonso**: a concordância do IntraText cobre o latim que ele cita; Paulo aparece em latim da
  Vulgata (`consolatur`, `misericordiarum`, `pignus`). As páginas `_P*.HTM` são UTF-8, apesar do cabeçalho
  ISO-8859-1. Títulos certos das obras: `https://www.intratext.com/IXT/ITASA0000/_INDEX.HTM` (com o ano).
  Script de consulta: `afonso.py` no scratchpad desta conversa (letra → `_FA<c>.HTM` → página da palavra).
- **São João da Cruz**: o `.doc` da DCO (`jc.txt` já convertido no cache de Nm 14) cita «2 Cor. 1, 7».
  Buscar «Cor.» com o número do capítulo.
- **Concílio de Trento e Denzinger**: o Clerus tem o Denzinger latino inteiro com as referências bíblicas
  em links (`https://www.clerus.org/bibliaclerusonline/en/dvt.htm`, `dw5.htm`…); a página de citações de
  cada perícope (abaixo) aponta direto o número DS.
- **Catecismo Romano**: duas edições com OCR no archive.org (`bub_gb_bkmHNI7iSwgC`, Nápoles 1804;
  `bub_gb_qYtujvHLGqsC`); juntar as linhas (`tr -s ' \n' ' '`) antes do `grep`, porque o OCR quebra as palavras.

## 2. Biblia Clerus para o Novo Testamento

- Índice das cartas: `https://www.clerus.org/bibliaclerusonline/en/66c.htm` → «2Corinthians» = `dt.htm`
  (Romanos `03.htm`, 1Cor `bf.htm`, Gálatas `nv.htm`). Cada carta tem as perícopes em `bnh.htm` (2Cor), com
  o link de citações no fim de cada perícope (`href=9….htm`). 2Cor 1: `9abrv5a.htm` (1,1-2), `9aev3ma.htm`
  (1,3-11), `9asp0jn.htm` (1,12–2,4). Usar `https://` (o `http://` dá 301 e o `curl` sem `-L` grava a página
  de redirecionamento).
- A página de citações junta Catecismo (por número), concílios, Denzinger, encíclicas (pelo número do
  parágrafo), audiências e homilias (números internos do Clerus), Padres e o Lecionário francês. Para achar o
  documento papal, seguir o link (`<a href=bdo.htm#na>8116</a>`), não o número.

## 3. Varredura dos Papas (cache já pronto)

- O cache da conversa de Nm 14 tem o texto italiano de todos os documentos: `…/639cd05d-…/scratchpad/dl/fr/docs`
  (Francisco, 2.584), `pp/docs` (Bento XVI e João Paulo II, homilias e audiências, 4.169), `leo/docs`
  (Leão XIV, 352). Script: `papas.py` no scratchpad desta conversa (padrões regex sobre o HTML sem tags).
  **Caminhar com `os.walk` e só limpar o HTML dos arquivos em que o regex já casa no bruto**: limpar tudo
  leva mais de 2 minutos.
- O cache **não tem** encíclicas, exortações nem o Vaticano II. Baixados aqui (italiano, vatican.va) e
  varridos: *Salvifici doloris*, *Dives in misericordia*, *Reconciliatio et paenitentia*, *Dominum et
  vivificantem*, *Pastores dabo vobis*, *Pastores gregis*, *Christifideles laici*, *Redemptoris mater*,
  *Redemptor hominis*, *Veritatis splendor*, *Novo millennio ineunte*, *Ut unum sint*, *Redemptoris missio*,
  *Evangelii nuntiandi*, *Gaudete in Domino*, *Spe salvi*, *Deus caritas est*, *Sacramentum caritatis*,
  *Verbum Domini*, *Lumen fidei*, *Evangelii gaudium*, *Gaudete et exsultate*, *Dilexit nos*, *Spes non
  confundit*, *Misericordia et misera*, LG, PO, CD, DV, GS, SC, AA, AG. Falharam (URL errada, 3 KB):
  *Catechesi tradendae*, *Misericordiae vultus*, *Patris corde*: refazer pelo índice
  (`…/<papa>/it/<tipo>.index.html`).
- **As notas dos documentos às vezes dizem «Ibid. 1, 5»** (Salvifici doloris, nota 59): procurar também
  frases do versículo em italiano («abbondano le sofferenze di Cristo»), não só a sigla.
- Endereços: Francisco usa, nos anos mais recentes, `…/francesco/it/audiences/<AAAA>/documents/<AAAAMMDD>-udienza-generale.html`
  (ex.: 2024) e, nos primeiros, `papa-francesco_<AAAAMMDD>_udienza-generale.html`; Santa Marta em
  `…/francesco/it/cotidie/<AAAA>/documents/papa-francesco-cotidie_<AAAAMMDD>_<título>.html` (são resumos do
  *L'Osservatore Romano*); Leão XIV, homilias em `…/leo-xiv/it/homilies/<AAAA>/documents/<AAAAMMDD>-<título>.html`.
- Catequeses que comentam capítulos de Paulo: **Bento XVI, ciclo sobre São Paulo** (02/07/2008–04/02/2009:
  apostolado 10/09/2008, Igreja 15/10/2008, Espírito Santo 15/11/2006 no ciclo dos Apóstolos) e o **ciclo
  sobre a oração nas cartas de Paulo** (maio–junho de 2012: 30/05/2012 é sobre 2Cor 1; ver as vizinhas para
  Rm 8, 2Cor 12, Fl 2, Ef 1, Cl); **João Paulo II, catequeses sobre o Espírito Santo** (1989–1991) e sobre a
  Confirmação (1998); **Francisco, ciclo sobre o Espírito Santo** (2024–2025).

## 4. Liturgia para as cartas

- Lecionário da Missa: `https://catholic-resources.org/Lectionary/Index-Sundays.htm` e `…/Index-Weekdays.htm`
  (todas as perícopes do NT com o número do OLM e o dia); não há índice próprio das cartas.
- Ofício das Leituras (ciclo de um ano): `https://catholic-resources.org/LoH/OfficeOfReadings-Biblical-Index.html`
  dá a perícope por dia (2Cor: 16ª semana do Tempo Comum); `…/OfficeOfReadings-NonBiblical-Readings.html`, a
  2ª leitura de cada dia.
- O **Universalis** pelo WebFetch só mostra o dia corrente (ignora a data no endereço) e bloqueia o `curl`:
  serve só para conferir o que cai hoje. Para outros dias, procurar outro breviário (ibreviary, es.catholic.net).
- Missal e Breviário antigos: o tar do Divinum Officium (só as pastas latinas) e `grep -rn "^!2 Cor 1:"`; os
  textos do Comum dos santos do **Missal** também estão em `horas/Latin/Commune/` (seção `[Missa]`), não em
  `missa/Latin/Commune/`. Matinas do tempo depois da Epifania e depois de Pentecostes leem as cartas de
  Paulo em sequência (2Cor começa no 2º domingo depois da Epifania).
- IGMR (2002) em italiano: `https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_it.html`.
- *Divinae consortium naturae*: o endereço certo tem `divina-consortium`.
