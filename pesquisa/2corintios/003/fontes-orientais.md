# Orientais sobre 2 Coríntios: o que se aprendeu no cap. 3 (só o novo)

Complementa `../../fontes/orientais.md` (2026-10-20). Pesquisa de 2026-10-20/21.

## Endereços e números de página conferidos

| Fonte | O que se aprendeu |
|---|---|
| Efrém, comentário às cartas (`commentariiinepi00ephruoft`) | Nas imagens do archive.org o índice `page/nN` **não** é o `leafNum` do `_page_numbers.json`: p. 90 = `n107`, 91 = `n108`, 92 = `n109`, 93 = `n110` (p. 114 = `n131`). Fórmula para 2Cor: `n` = página + 17. O OCR desse trecho estava bom; as letras trocadas do `base/` se resolvem na imagem em minutos. |
| Lamy, *Hymni et sermones* I (`sanctiephraemsy00lamygoog`) | Sem `_page_numbers.json`; colunas (siríaco ímpar, latim par) = `n` × 2 − 189 e − 188 (col. 111–112 = `n150`, 211–212 = `n200`). O *Sermão sobre Nosso Senhor* ocupa as col. ~150–270; §§ 29–32 = col. 209–218 (Moisés, o véu, Paulo cego). O «inside.php» (busca no livro) desse item não responde. |
| PG 65, *Apophthegmata* (`patrologiaecursu65mignuoft`) | A busca no livro (`https://ia800104.us.archive.org/fulltext/inside.php?item_id=…&doc=…&path=/25/items/…&q=…`) funciona **no latim** de Cotelier; o número de página que ela devolve é o `n` + 1 (Pambo 12 deu 190 e está em `n189` = col. 371–372). |
| PG 34, Macário (`bim_early-english-books-1641-1700_1860_34`, `_djvu.txt`) | O grego do OCR é inútil, o latim é bom e traz os cabeçalhos de coluna («513 HOMILLE. — HOM. V. 514»); achar o lugar pelo latim e tirar a coluna do cabeçalho anterior. Hom. 5, 10 = c. 513–514; 25, 1 = 667–668; 38, 2 = 759–760; 47, 1 = 795–796. |
| Menaion de agosto (Veneza, Phoinix, 1889, ed. Bartolomeu Kutlumusiano) | `https://archive.org/details/menaion-tou-ianouariou-etc-4` («Том 8» = agosto; a série 1889 começa em janeiro). Nas páginas do ofício da Transfiguração, `n` = página + 8 (p. 37 = `n45`; p. 34 = `n42`). O `_hocr_searchtext.txt.gz` + `_hocr_pageindex.json.gz` acham a página de qualquer frase grega; o «inside.php» não aceita grego. Arquivos com nome «Mēnaion_tou_Ianouariou_etc(4)»: codificar a URL. |
| AGES (`r.zip` no cache da conversa do Nm 16, `ee6e9730-…\pesq-orientais\bizantinos\dl_ageszip`) | Cada ofício traz `poet` e `acrostic` por cânon: dá a atribuição (Transfiguração: cânon 1 de Cosme, acróstico «Χριστὸς ἐνὶ σκοπιῇ σέλας ἄπλετον εἴδεος ἧκε»; cânon 2 de João Damasceno, «Μωσῆς Θεοῦ πρόσωπον ἐν Θαβὼρ εἶδε»). |
| Parisot, Afraates (`patrologiasyriac01graf`) | Latim legível; Dem. 21, 10 perto do marcador de coluna 960. |
| Kmosko, *Liber Graduum* (`PatrologiaSyriacaIIILiberGraduum_201603`, `_djvu.txt`) | O índice bíblico do fim (linha ~76200 do OCR) dá as colunas: 2Cor 3,18 em 35, 327, 419, 439. O corpus (corpus 188–218) não traz colunas. |

## Caches reaproveitáveis (fora do git, no Temp do Claude)

- `…\ee6e9730-…\scratchpad\pesq-orientais\dl\tei\` — os 632 TEI do Digital Syriac Corpus; convertidos em texto, com
  índice de autor e título (`_indice.tsv`), em `…\9acafcb3-…\scratchpad\orientais\sc\` pelo script
  `orientais\scripts\corpus.py`; `sbusca.py` busca frases sem vogais em todo o corpus e dá página e seção.
- `…\ee6e9730-…\pesq-orientais\dl\ia\` — OCR de Lamy I–IV, ed. romana siríaco-latina II–III (`syr2.txt`, `syr3.txt`),
  Bickell, Didascália, Isho`dad. `…\deserto\pgdigital\` — PG 65, 88, 89 (OCR) e os hOCR. `…\armenios\dl_ws\` — Narek
  (*Matean*), Shnorhali (alguns hinos) do Wikisource armênio.
- `…\94b210f9-…\scratchpad\g12\txt\Macari__*.txt` — Macário inteiro do khazarzar, já em texto.

## Armadilhas

- A pista automática «Isaac de Nínive, Discurso 5, p. 73: v. 16» é falso positivo (ܢܬܦܢܐ ܠܘܬ ܡܪܝܐ vem de Ez/Jr).
  «ܐܝܟ ܕܒܡܚܙܝܬܐ» dá quase sempre 1Cor 13,12, não 2Cor 3,18: ler o contexto.
- No Bash do Windows, heredoc longo com aspas e grego/siríaco quebra («unexpected EOF»): escrever o script com a
  ferramenta de arquivo e só rodá-lo.
- As Homilias de Macário do khazarzar seguem Dörries; a numeração das homilias coincide com a PG, a dos capítulos às
  vezes não (a PG 34 divide em I, II, III… dentro da homilia).
