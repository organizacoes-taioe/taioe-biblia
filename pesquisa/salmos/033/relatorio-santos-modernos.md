# Salmo 33 (Vulgata 32): santos dos séculos XVI a XX — relatório

Pesquisa de 2026-10-17 (cerca de 40 min). 7 excertos em `achados-santos-modernos.json`. Afonso,
Magistério e Liturgia já estão em `achados-modernos.json` e `relatorio-modernos.md` (não mexidos).

## Método

Busca na web com as frases latinas e as traduções deu pouco: os buscadores não indexam as edições
antigas. O que funcionou foi baixar o texto OCR das edições antigas no archive.org
(`https://archive.org/download/<id>/<id>_djvu.txt`) e procurar (1) as referências na margem
(«Ps. XXXII», que o OCR estraga em `xxxn`, `xxxîi`, `Psaimi XXXII`) e (2) as palavras latinas raras
dos versículos (*chordarum*, *fallax*, *finxit*, *sigillatim*, *speravimus*, *sustinet*, *firmati*…).
Edições de 1684 têm o «s» longo, que o OCR lê como «f» (*falutem*, *fperavimus*): buscar com `[sf]`.
O link de página do archive.org (`/page/<pág. impressa>/mode/1up`) foi conferido pelo
`<id>_page_numbers.json`.

## Achados

- **São Francisco de Sales** (*Œuvres*, ed. de Annecy; t. III Introdução, IV–V Tratado do Amor de
  Deus, VI Colóquios, VII–X Sermões; ids `oeuvresdesaintfrNNfran`). Cinco usos, todos dos vv. 6 e 9:
  - Sermão de Pentecostes de 1593 (t. VII, p. 16): v. 6 em chave trinitária, os apóstolos como céus
    da Igreja e o Espírito como «suspiro de amor» do Pai. **O melhor.**
  - Sermão da Purificação de 1620 (t. IX, p. 250): «Deus diz como faz e faz como diz» (v. 9), daí o
    dever de juntar a obra ao bom propósito. **Ótimo para o leitor comum.**
  - *Tratado do Amor de Deus* II, 2 (t. IV, pp. 91–92): o «sopro da boca» como um só ato da vontade.
  - Esboço latino de 1612 (t. VIII, pp. 90–91): «dixit semel et factum est semper» e a imagem dos
    vidreiros que sopram o vidro (o sermão é sobre Jó 26,13; o salmo vem na margem).
  - Sermão de 10/03/1622 sobre Naim (t. X, p. 314): a palavra que criou é a que ressuscita.
  - Ficaram de fora: t. V, p. 302 (Tratado, cita Sl 32,8 numa lista sobre o trovão); t. VIII, p. 219
    (*decem chordarum*, só repete Belarmino: as cordas = os mandamentos). A *Introdução à vida devota*
    (t. III) e os *Colóquios* (t. VI) não citam o salmo. As Cartas (t. XI–XXI) não foram varridas.
- **São Cláudio de la Colombière**, sermão LIX «Du soin du salut» (*Sermons*, Lyon 1684, t. III,
  pp. 430–431; id `sermonsprchezd03laco`): vv. 10 e 16–17 com Saul, Golias e Absalão. **Ótimo.**
  Varridos também os 4 tomos de 1684 e os 7 da ed. de 1832 (`uvresdurpclauded0Nlaco`): nada sobre o
  v. 22 nem sobre outros versículos, apesar de ele ser o santo da confiança.
- **São John Henry Newman**, *Lectures on Justification*, lição 4 (pp. 98–99): «He spake, and it was
  done» (v. 9) e a palavra «com a obra colada a ela como sombra». **Ótimo**; escrito ainda anglicano
  (1838), dizer isso se for usar. Os textos do Newman Reader já estavam baixados no scratchpad, por
  outra pesquisa. Também: *Parochial and Plain Sermons* VI, 24 («The Mystery of the Holy Trinity»)
  cita o v. 6 numa lista de textos do AT sobre a Palavra e o Sopro (fraco, ficou só aqui).

## Procurado e não achado

- **São João da Cruz** (*Obras*, Toledo 1912, t. I–II: Subida, Noite, Cântico, Chama) e **Santa
  Teresa** (*Escritos*, BAE 53 e 55, 1861–62): nenhuma citação do salmo nem das palavras latinas.
- **Beato Columba Marmion**, *Le Christ dans ses mystères* (1922) e **Santa Elisabete da Trindade**
  (*Souvenirs*, 1913): nada.
- **Santa Teresinha**: o Wikisource francês tem a *Histoire d'une âme* (ed. 1912, páginas
  `Histoire d’une âme/…`), mas a API bloqueou por excesso de pedidos (HTTP 429) antes de varrer.
  **A conferir**; de memória, o «cantarei as misericórdias do Senhor» dela é o Sl 88, não este.
- **Não tentados** por falta de tempo: Santo Inácio, São Luís de Montfort (o texto do archive.org
  `amour-de-la-divine-sagesse` não tem OCR), Santa Margarida Maria (*Vie et œuvres*, 1876/1915,
  ids `vieetoeuvres01alac`, `vieetoeuvre01alac`, `vieetoeuvre03alac`), São Pio X e Santa Faustina
  (a Faustina tem direito autoral; parece que outra pesquisa já baixou o *Diário*).
- **São Roberto Belarmino** (santo e Doutor, 1542–1621) comenta o salmo inteiro na *Explanatio in
  Psalmos* (1611; id `bub_gb_7j0Mm5XItI4C`, OCR em duas colunas embaralhadas; tradução inglesa de
  O'Sullivan, 1866). Não entrou aqui porque é comentário corrido, e outra pesquisa já o tinha
  baixado no scratchpad; se ninguém o cobrir, é a fonte mais rica deste período.
