# Gênesis 1: relatório do grupo «latinos» (25/10/2026)

Latinos antigos e medievais, menos Agostinho. Não havia pré-pesquisa do Gênesis: as obras foram baixadas
(Corpus Corporum = PL; Corpus Thomisticum; Wikisource), cortadas para `base/` e lidas nos trechos que comentam
Gn 1. Entregues **20 achados** em `achados-latinos.json`: trecho 1 = 5, trecho 2 = 3, trecho 3 = 3,
trecho 4 = 2, trecho 5 = 7. Ambrósio tem 8 (o *Hexaemeron* é o comentário latino de Gn 1 por excelência);
os outros 12 são de 9 autores.

## Como se procurou

1. Os textos da PL já baixados em conversas anteriores (scratchpads do taioe) foram copiados para
   `pesquisa/cache/genesis/latinos/`; os que faltavam vieram do Corpus Corporum, um por vez.
2. Varredura de todos eles pelas notas de Migne «(Gen. I, v)» / «(Genes. I, v)» e por 17 frases da Vulgata e da
   Vetus Latina («in principio fecit/creavit», «inanis et vacua / invisibilis et incomposita», «spiritus Dei
   ferebatur», «fiat lux», «dies unus», «fiat firmamentum», «congregentur aquae», «germinet terra»,
   «luminaria», «producant aquae», «cete grandia», «crescite et multiplicamini», «faciamus hominem», «ad
   imaginem et similitudinem», «masculum et feminam», «dominamini», «valde bona»).
3. Leitura dos comentários seguidos (Ambrósio, Beda, Ruperto, Hugo, Hildegarda, Tomás) e dos trechos
   achados nas outras obras; escolha dos melhores, um por ideia.
4. Os `original` saíram do texto limpo e foram conferidos como trechos exatos da fonte (só com as notas de
   Migne, as marcas de coluna e os números de página da edição anterior tirados); as correções estão abaixo.

## Scripts (reaproveitáveis para Gn 2–50)

Em `pesquisa/ferramentas/base/`, todos com o capítulo como parâmetro (`python3 -I -X utf8 … 2`, `… 2-11`) e o
uso no topo; rodados agora só para Gn 1. Para testar sem gravar na pasta, `GEN_LATINOS_SAIDA=<pasta>`.

| script | obra | como corta |
|---|---|---|
| `gen-latinos-comum.py` | biblioteca | baixa do Corpus Corporum, limpa a PL (`lat_comum.limpar_pl`), lê a Nova Vulgata do vatican.va e acha o capítulo de cada parágrafo pelo lema (4 palavras seguidas iguais à Vulgata) |
| `gen-latinos-ambrosio.py` | *Hexaemeron* (Gn 1), *De paradiso* (2–3), *De Cain* (4), *De Noe* (6–9), *De Abraham* (12–25), *De Isaac*, *De Iacob*, *De Ioseph*, *De benedictionibus*; carta 43 | obra de um capítulo vai inteira; as de vários, pelos lemas (conferir: Ambrósio cita no meio do sermão) |
| `gen-latinos-beda.py` | *In principium Genesis* (Gn 1–21) | lemas |
| `gen-latinos-ruperto.py` | *De Trinitate et operibus eius*, In Genesim I–IX | lemas |
| `gen-latinos-rabano.py` | *Commentaria in Genesim* | lemas |
| `gen-latinos-alcuino.py` | *Interrogationes in Genesin* | pergunta a pergunta, pela nota de Migne ou pelo lema |
| `gen-latinos-jeronimo.py` | *Quaestiones hebraicae in Genesim* | marcas «(CAP. N)» / «(Cap. N.--Vers. v.)» |
| `gen-latinos-isidoro.py` | *Quaestiones in Genesin* | tabela dos 31 capítulos de Isidoro |
| `gen-latinos-hugo.py` | *Adnotationes in Pentateuchon*; *De sacramentis* (Gn 1–3) | marcas «(GEN. N.)»; partes do livro I |
| `gen-latinos-avulsos.py` | trechos em obras que não comentam o livro | tabela por capítulo (por ora só Gn 1) |

Testados também com Gn 2, 3, 12, 22 e 49 (fora da pasta): os cortes saem coerentes.

## O que se achou

| autor | obra | onde | situação |
|---|---|---|---|
| Santo Ambrósio | *Hexaemeron* I–VI | PL 14, 123–274 | `base/ambrosio-hexaemeron.md`; 8 achados |
| Santo Ambrósio | Carta 43 (29 Faller–Zelzer), a Horontiano | PL 16, 1129–1135 | `base/`; reserva (o homem criado por último) |
| Santo Ambrósio | *De mysteriis* 3, 9 | PL 16, 391C–392A | `base/`; reserva (repete Tertuliano) |
| São Jerônimo | *Quaestiones hebraicae* (Gn 1,1.2.10) | PL 23, 938B–940A | `base/`; 1 achado |
| São Jerônimo | Carta 69, 6 | PL 22, 659–661 | `base/`; reserva (repete Tertuliano) |
| Tertuliano | *De baptismo* 1–4 | PL 1, 1197–1204 | `base/`; 2 achados |
| Tertuliano | *Adversus Hermogenem* 19–34 | PL 2, 214–229 | `base/`; técnico, sem achado |
| Lactâncio | *Divinae institutiones* VII, 4–6 | PL 6, 746–758 | `base/`; reserva |
| Santo Hilário | *De Trinitate* IV, 16–21; V, 4–9 | PL 10, 108–113; 132–135 | `base/`; reserva |
| São Zenão de Verona | Tratados II, 1–4 (*De Genesi*) | PL 11, 386–398 | `base/`; reserva |
| São Leão Magno | Sermões 12, 1 e 27, 4–6 | PL 54, 168–169; 218–221 | `base/`; 2 achados (o 27, 6 já foi usado em 2Cor 4: não repetir) |
| São Gregório Magno | *Moralia* IX, 49, 75 | PL 75, 900A–C | `base/`; 1 achado |
| São Beda | *In principium Genesis* I | PL 91, 12B–34C | `base/`; 1 achado |
| Alcuíno | *Interrogationes in Genesin* (perg. 26–41, 81) | PL 100, 519–525 | `base/`; respostas de uma linha, derivadas (Gregório, Agostinho) |
| Rábano Mauro | *Commentaria in Genesim* I | PL 107, 443–464 | `base/`; compilação, sem achado |
| Santo Isidoro | *Quaestiones in Genesin* I–II | PL 83, 209–216 | `base/`; só alegoria (de Agostinho), sem achado |
| Ruperto de Deutz | *In Genesim* I e II, 1–12 | PL 167, 199–257 | `base/`; 2 achados |
| Hugo de São Vítor | *De sacramentis* I, 1; I, 2, 1; I, 6, 1–2 | PL 176, 186–206; 264 | `base/`; 1 achado |
| Hugo de São Vítor | *Adnotationes in Pentateuchon* | PL 175, 32–38 | `base/`; notas secas, sem achado |
| São Bernardo | *De gratia et libero arbitrio* 9 | PL 182, 1016–1018 | `base/`; reserva (técnico) |
| São Bernardo | Sermões sobre o Cântico 80–82 | PL 183, 1166–1181 | `base/`; 1 achado |
| Santa Hildegarda | *Liber divinorum operum* II, 1, 17–47 | PL 197, 916–953 | `base/`; reserva |
| São Tomás | *Suma* I, q. 65–74 e 93 | Leonina 5; Corpus Thomisticum | `base/`; reserva |
| Santa Catarina de Sena | *Diálogo*, cap. 13 | ed. Fiorilli (1912), pp. 30–33 | `base/`; 1 achado |
| São Boaventura | *Breviloquium* II, 12 | Quaracchi V, 230 | pista (OCR) |

Quem não comenta Gn 1: `base/_ausentes-latinos.md` (Crisólogo, Máximo de Turim, Cesário na PL 67, Leão nas
cartas, Lactâncio no *De opificio Dei*). Pistas não seguidas: `base/_pistas-latinos.md` (Boaventura, Gregório
nas homilias sobre Ezequiel e os Evangelhos, Isidoro nas *Sententiae*, Pedro Lombardo, Comestor, Arnaldo de
Bonneval, Lápide, Glosa).

## Os 20 achados

1. **Trecho 1**: Jerônimo, «chocava» em vez de «pairava»: o Espírito que dá vida é Criador e Deus (3);
   Ruperto, o Espírito é o amor do Criador que se inclina sobre a criatura para uni-la a si (2); Tertuliano,
   as águas honradas pelo Espírito e o batismo (3); Hugo, a matéria primeiro informe ensina à alma a distância
   entre «ser» e «ser belo» (3); Ambrósio, «Faça-se a luz»: o construtor que começa pela luz, e o dizer de Deus
   que já é fazer (3).
2. **Trecho 2**: Ambrósio, a água que se junta quando Deus manda e o povo que não se junta (3); o mar, as ilhas
   dos monges e o canto do povo na Igreja como o fragor das ondas (3); a rosa sem espinhos (2).
3. **Trecho 3**: Leão, os cristãos que se curvavam ao sol nos degraus de São Pedro; sol e lua, criaturas para
   o homem contar o tempo (3); Ambrósio, as plantas antes do sol: não se tome por Deus o que veio depois dos
   dons de Deus; Cristo, Sol de justiça (3); Ambrósio, a lua que míngua e cresce, figura da Igreja que brilha
   com a luz de Cristo (3).
4. **Trecho 4**: Tertuliano, as águas deram os primeiros viventes; «nós, peixinhos» (3); Ambrósio, a baleia e
   a rã feitas no mesmo instante: Deus não se cansa no grande nem despreza o pequeno (3).
5. **Trecho 5**: Gregório, «Façamos»: o homem feito como depois de um conselho (3); Leão, feito à imagem para
   imitar o Autor, espelho da bondade de Deus (3); Ambrósio, «foste pintado por Deus: não apagues a pintura» (3);
   Bernardo, o pecado cobriu a semelhança, não a apagou (3); Ruperto, homem e mulher igualmente à imagem (2);
   Catarina, o amor com que Deus se enamorou da criatura, causa de tanta dignidade (3); Beda, o homem perdeu o
   domínio dos animais ao desobedecer a Deus, e nos santos a criação volta a obedecer (3).

Os cinco mais fortes: `catarina-dialogo-13-o-amor-que-criou-o-homem`, `leao-sermao-27-4-5-o-sol-criatura`,
`gregorio-moralia-9-49-75-facamos`, `ambrosio-hex-3-1-1-2-aguas-obedecem`, `bernardo-cantico-82-2-7-semelhanca-coberta`.

## Reserva (bons, mas fora para não repetir)

- Ambrósio, *Hex.* I, 5, 18 (PL 14, 131A–B): «fecit quasi bonus… quasi sapiens… quasi omnipotens»: Deus fez o
  mundo por vontade, não como a sombra que segue o corpo. Bom para «Deus cria por bondade», se faltar.
- Ambrósio, *Hex.* I, 7, 27 (PL 14, 137A–C): por que Deus primeiro fez e depois ornou: para que não se
  julgasse a matéria eterna, e para que o imitemos, fazendo primeiro e embelezando depois (mesmo tema de Hugo).
- Ambrósio, *Hex.* I, 8, 29 (PL 14, 138C–139B): a Trindade no começo da criação e o «Syrus… fovebat aquas»
  (o mesmo de Basílio, *Hex.* 2, 6, e de Jerônimo).
- Ambrósio, *Hex.* I, 10, 37–38 (PL 14, 144A–D): «dia um», não «primeiro»; o dia começa e acaba na luz.
- Ambrósio, *Hex.* III, 6, 26–27 (PL 14, 166B–167A): a primeira palavra de Deus ficou como lei da natureza;
  a erva nasceu antes do sol (o mesmo de Basílio, *Hex.* 5, 1, e do achado de IV, 1).
- Ambrósio, *Hex.* V, 24, 88 (PL 14, 240C–241A): o canto do galo e Pedro (as aves que ensinam o homem); bonito.
- Ambrósio, *Hex.* VI, 8, 45 (PL 14, 259C–260A): a alma, imagem de Deus, que num instante vai da Itália à
  Pérsia e à África.
- Ambrósio, carta 43, 3–8 (PL 16, 1130A–1131C): o homem criado por último como o amigo chamado ao banquete já
  pronto, e como o atleta que entra no estádio quando a coroa já está à vista (o mesmo de Nissa, *De opif.* 2).
- Hilário, *De Trinitate* IV, 16–18 (PL 10, 108C–111C): «disse Deus… e fez Deus» (o Pai e o Filho); «façamos» e
  «nossa imagem», não «nossas imagens»: nem solidão nem diferença em Deus.
- Zenão, Tratados II, 1, 1 (PL 11, 387A–388A): «Façamos… não diz: faze à tua, mas façamos à nossa… Um só homem é
  formado à imagem e semelhança de dois, e nele não se acha o que é de quem». Mais vivo que Hilário.
- Lactâncio, *Div. inst.* VII, 5, 3–4 e 6, 1 (PL 6, 749B–757C): o mundo para o homem, o homem para Deus; o rosto
  voltado para o céu; «Idcirco mundus factus est, ut nascamur…» (cadeia dos fins).
- Hugo, *De sacramentis* I, 2, 1 (PL 176, 205B–D): o homem, último no tempo e primeiro na causa; e I, 6, 2
  (264C): «imago secundum cognitionem veritatis, similitudo secundum amorem virtutis».
- Tomás, *Suma* I, q. 93, a. 4 (as três imagens: da criação, em todos; da graça, nos justos; da glória, nos
  bem-aventurados); q. 65, a. 2 (cada coisa feita porque é bom que exista; o universo ordenado a Deus);
  q. 70, a. 2 (Moisés fala dos astros só como úteis ao homem, para afastar da idolatria).
- Hildegarda, *Liber divinorum operum* II, 1, 43 (PL 197, 944C–946B): «Façamos o homem à nossa imagem, isto é,
  segundo a túnica que germinará no seio da Virgem»: o homem criado na forma da humanidade que o Filho havia de
  vestir. Original e cristológico; talvez para o tema da imagem, se o Gere quiser um quarto.
- Boaventura, *Breviloquium* II, 12 (Quaracchi V, 230): o mundo como livro em que se lê a Trindade.
- Gregório, *Hom. in Ev.* 29, 2: «omnis creaturae aliquid habet homo» (é sobre Mc 16,15).
- Alcuíno, perg. 9 e 41: o homem feito por último, como o dono que entra quando a casa está pronta; «muito bom»
  por causa do homem.
- Beda, *In principium Genesis* I (PL 91, 30A–B), sobre Gn 1,26: o homem é imagem de Deus naquilo em que excede
  os animais, a razão, «por meio da qual pode governar bem as coisas criadas».

## Sobreposições com os outros grupos (para a escolha final)

- Espírito sobre as águas: Jerônimo (o hebraico) e Ruperto (o amor) dizem o que Agostinho diz em
  `agostinho-gnlitt-1-18-36` (o Espírito que choca as águas, o amor de Deus); Basílio (*Hex.* 2, 6, o «sírio»)
  também. Ficar com um ou dois. Tertuliano (batismo) repete o tema de `liturgia-bencao-da-agua-espirito-sobre-as-aguas`
  (modernos); a bênção da água deriva dele.
- O sol: Leão e Ambrósio IV, 1 ao lado de `agostinho-sermo-190-1`, `bento-xvi-hom-20120407-os-luzeiros-nao-sao-deuses`
  e, nos gregos, Basílio e Teófilo. O de Leão (São Pedro) é único.
- Homem e mulher: Ruperto II, 7 diz o mesmo que `agostinho-trin-12-7-10` e *Gaudium et spes* 12 (modernos).
- A imagem que o pecado não apaga: Bernardo ao lado de `agostinho-trin-14-8-11`; o de Bernardo é mais vivo.
- A rosa sem espinhos: Ambrósio copia Basílio (*Hex.* 5, 6).
- O homem por último: a carta 43 de Ambrósio (reserva) repete Nissa, *De opificio hominis* 2.

## Correções nos originais (conferir na imagem da PL, se for preciso)

- Ambrósio, *Hex.* V, 2, 5: o Corpus Corporum traz «late palens»; corrigido para «late patens».
- Hugo, *De sacramentis* I, 1, 3: «expotulasset» → «expostulasset».
- Tertuliano, *De baptismo* 1, 3: o Corpus Corporum traz «in qua nascimur»; posto «in aqua nascimur» (a leitura
  de todas as edições). Em 3, 4, a pontuação da PL («edidit ne mirum sit, in Baptismo, si aquae animare,
  noverunt») foi acertada para «edidit, ne mirum sit in Baptismo, si aquae animare noverunt». O texto da The Latin
  Library é de outra edição (com «intinctorem moraturum» em 4, 1): ficou a PL.
- Ruperto, *In Gen.* I, 7–8: tirado o título do cap. VIII, que corta a frase no meio; Jerônimo: tirados os
  parênteses vazios onde a PL tinha letras hebraicas («MEREFETH ( )»).
- Tirados os números de página da edição anterior que Migne deixa no texto («42», «63», «78», «95», «96», «25»).

## Para o `autores.json`

Faltam: **Hugo de São Vítor** («cônego regular de São Vítor, em Paris (c. 1096–1141), teólogo»). Se entrarem da
reserva: São Zenão de Verona («bispo de Verona (†c. 372)»), Santa Hildegarda de Bingen («abadessa beneditina
(1098–1179), Doutora da Igreja»). Os `autor_id` novos usados: `hugo-sao-vitor`, `catarina-sena`.

## Para o catálogo `pesquisa/fontes/latinos.md` (ids do Corpus Corporum usados aqui)

Beda, *Hexaemeron* 8466 (`Beda.Hexaem2`); Alcuíno, *Interrogationes in Genesin* 21416 (`Alcuin.InEtReI`);
Rábano, *In Genesim* 8885 (`RabMau.CoInGe3`); Isidoro, *Quaestiones in VT* 21433 (`IsiHis.QuInVeT`), *Sententiae*
8218 (`IsiHis.Senten5`); Hugo, *Adnotationes in Pentateuchon* 11054 (`HuDeSVi.AdInPe`), *De sacramentis* 11082
(`HuDeSVi.DeSac3`); Hildegarda, *Liber divinorum operum* 11562 (`Hildeg.LiDiOpS`); Zenão, *Tractatus* 6894
(`ZenVer.Tracta2`); Tertuliano, *De baptismo* 44 (`Tertul.DeBap`), *Adv. Hermogenem* 61; Lactâncio, *Div. inst.*
II 6808 (`Lactan.DiInLiI2`), VII 6813 (`Lactan.DiInLiV3`), *De opificio Dei* 6823; Cesário, Sermões 7852;
Jerônimo, *Quaestiones hebraicae* 7160 (`HieStr.QuHeInG`); Leão, Sermões 7631 (`LeoI.Sermon9`); Ambrósio,
*Hexaemeron* 6958 (`AmbMed.Hexaem`). A Vulgata de Jerônimo na PL (7204, *Liber Genesis*) não marca os versículos e
pula capítulos: para cortar pelos lemas, usar a Nova Vulgata do vatican.va. Tomás: Corpus Thomisticum
`sth1065.html` (q. 65–74) e `sth1090.html` (q. 90–102). Santa Catarina: Wikisource, *Libro della divina
dottrina* (ed. Fiorilli), um capítulo por página.

## Para outros capítulos

- **Gn 2**: Ambrósio, *Hex.* VI, 10, 75–76 (PL 14, 272B–274A): «Fez o céu, não leio que tenha descansado… fez o
  homem, e então descansou, tendo a quem perdoar os pecados» (Gn 2,2; fortíssimo). Beda, *In principium
  Genesis* I (PL 91, 34–39): os seis dias como as seis idades do mundo (alegoria). Rábano I, 10 (o mesmo).
  Gregório, *Moralia* IX, 49, 75, segunda metade: o homem «modelado como que com cuidado» e erguido pelo sopro
  (Gn 2,7). Tertuliano, *De resurrectione carnis* 6: «quodcumque limus exprimebatur, Christus cogitabatur homo
  futurus» (Gn 2,7; não conferido aqui). Hildegarda, *LDO* II, 1, 48–49 (Gn 2,1–3). Alcuíno, perg. 1–8 e 42–59.
  Hugo, *De sacramentis* I, 6, 3–15. Ruperto, *In Gen.* II, 13 em diante (o sétimo dia). Ambrósio, *De paradiso*.
- **Gn 3**: Ambrósio, *Hex.* III, 11, 48 (a rosa e os espinhos) liga-se a Gn 3,18.
