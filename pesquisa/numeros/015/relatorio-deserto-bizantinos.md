# Números 15: relatório da frente «Padres do deserto, ascetas gregos e hinografia bizantina»

Pesquisa de 2026-10-20. Resultado: 5 excertos em `achados-deserto-bizantinos.json` (2 com relevância 3,
2 com 2, 1 com 1; trecho 2: 1, trecho 3: 1, trecho 5: 3; trechos 1 e 4: nada). Textos gregos e pistas em
`textos/deserto-bizantinos-15.md`. Nenhum repete os achados gregos (Cirilo, Teodoreto, Procópio,
Crisóstomo, Basílio, Máximo, Isidoro, Damasceno, Nissa).

## Onde se procurou

- **Patrologia Graeca, item `PatrologiaGraeca` do Internet Archive**: este item tem OCR **grego legível**
  (ao contrário dos `bim_early-english-books…`, cujo grego sai em letras latinas). Baixados os `_djvu.txt`
  dos vols. 34 (Macário), 40 (Asterio, abade Isaías…), 65 (*Apophthegmata*, Marcos o Eremita, Diádoco),
  79 (Nilo), 86/1–2, 87/3 (Mosco, Sofrônio), 88 (Clímaco e escólios, Doroteu, Cosme Indicopleustes), 89
  (Anastásio Sinaíta, Antíoco), 97 (André de Creta), 98 (Germano, Cosme de Maiúma), 99 (Teodoro Estudita),
  100, 106, 118–119 (Ecumênio), 120 (Simeão NT, Nicetas Estetatos), 123–125 (Teofilacto), 128–129
  (Eutímio), 150–151 (Cabásilas, Palamas), 155 (Simeão de Tessalônica). Busca sem acentos (com χ=κ, por
  causa do OCR) por κρασπεδ-, ὑακινθ-, κλῶσμα, συλλέγ- ξύλα / ξύλα + σάββατ- / λιθοβολ- + σάββατ-,
  ἀπαρχ- + φύραμα, ἐν χειρὶ ὑπερηφανίας, ἀκουσι-/ἄγνοια + νόμος/θυσία/Μωϋσῆς, «ἐν τοῖς Ἀριθμοῖς».
  Páginas localizadas pelo `hocr_pageindex` do item e conferidas na imagem (BookReaderImages).
  Scripts em `scratchpad/ag-deserto/scripts/` (`gn.py` busca com cache normalizado; `pagina.py` acha o
  n da página; `img.py` baixa a imagem; `orig.py` mostra o texto acentuado em volta).
- **Cache da frente oriental do Nm 16** (`…/ee6e9730…/scratchpad/pesq-orientais/`): Evergetinos I–IV
  (grego), PG 65/88/89 em OCR latino, Efrém greco-latino (Assemani), Barsanúfio e João (grego da
  azbyka, parcial), Budge (*Paradise*), e os livros litúrgicos (AGES: Menaion dos 12 meses, Triódio com o
  Grande Cânon, Pentecostário, Octoeco, Eucológio, Horológio). Busca latina por *fimbri-*, *hyacinth-*,
  *ligna* + *sabbat-*, *manu superbiae*, *per ignorantiam* + *lex/sacrificium*, *primitiae* + *massa/conspersio*.
- **Filocalia grega** (6 vols., archive.org `philokalia_202101`): só busca (edição moderna; os textos
  são antigos, mas não se guardou nada).
- **Pitra** (*Analecta sacra* I–V, Romano 1888) e PG 97 (André de Creta) já em `cache/base/ori/grc/ia/`.

## O que se achou (os melhores)

| Autor, obra | Onde | Trecho | O que diz |
|---|---|---|---|
| **São Nilo de Ancira**, Sermão sobre Lc 22,36, cap. 10 | PG 79, 1277D–1280A | 5 | **O melhor achado.** As franjas de jacinto: «como a franja é o começo da veste, o temor do Senhor é o começo da sabedoria»; é preciso tecê-lo em toda «ponta» da virtude, porque os cumes são escorregadios e levam à soberba; lembra que foi Deus quem deu a sabedoria de tecer a veste. O pão ázimo que não incha no fogo. Rel. 3. |
| **São Germano de Constantinopla**, Ep. IV a Tomás de Claudiópolis (lida em Niceia II) | PG 98, 172D–173B | 5 | As franjas como argumento a favor das **imagens dos santos**: se a Lei dava um fio azul para lembrar os mandamentos, muito mais as imagens para contemplar o fim da vida dos santos e imitar a sua fé (Hb 13,7). Leitura que nenhum outro Padre faz. Rel. 3. |
| **Santo André de Creta**, Hom. I sobre a Natividade de Maria | PG 97, 809D–812A | 2 | Adão oferece a Deus **Maria como primícia** da massa humana, «a que não se misturou com toda a massa», e por ela se faz o **pão** (Cristo) para a recriação do gênero humano: a linguagem é a de Nm 15,20 LXX (ἀπαρχὴ φυράματος, ἄρτος) mais que a de Rm 11,16. Rel. 2. |
| **Teofilacto de Ocrida**, sobre Mt 23,5 | PG 123, 396D–397A | 5 | Os fios «cor de jacinto ou escarlates»: Deus não queria só um lembrete; o filactério na mão manda praticar, e o **vermelho das franjas anuncia que devemos ser marcados com o sangue de Cristo**. Próprio dele (Crisóstomo não diz isso). Rel. 2. |
| **Antíoco de São Sabas**, *Pandectes*, hom. 44 (Sobre a soberba) | PG 89, 1572B–D | 3 | Nm 15,30 citado entre as provas: a soberba não é natural, é imagem do demônio rebelde; «quem age de mão levantada será exterminado». Só citação comentada pelo contexto. Rel. 1. |

## O que não existe ou não se achou

- **Trecho 1 (vv. 1–16) e trecho 4 (o homem da lenha)**: nada nos ascetas, nos *Apophthegmata*
  (alfabética, PG 65; sistemática no Evergetinos), em Doroteu, Clímaco e escólios, Marcos, Diádoco, Nilo,
  Barsanúfio (parcial), Mosco, Anastásio, Teodoro Estudita, Simeão NT, Palamas, Cabásilas, na Filocalia,
  nem na hinografia. As únicas «lenhas» dos ditos são do abade Longino catando lenha na praia
  (Evergetinos III; PG 65), sem relação. Anastásio Sinaíta, *Hexaemeron* VII (só latim), fala do sábado
  espiritual (não carregar o fardo do pecado, não acender o fogo da concupiscência) sem citar o homem da lenha.
- **Pecado por ignorância × de soberba (vv. 22–31)**: Marcos o Eremita trata dos pecados «involuntários»
  (todo involuntário nasce de um voluntário), Doroteu e Barsanúfio também, mas **nenhum cita Nm 15**.
  Anastásio Sinaíta, *Perguntas e respostas* (PG 89, pág. n305 do vol. 089), argumenta do pecado por
  ignorância que exige sacrifício para o pecado consciente, mas cita **Lv 5,17**: pista, não achado.
- **Hinografia bizantina** (AGES: Menaion, Triódio, Pentecostário, Octoeco, Eucológio, Horológio; Grande
  Cânon de André de Creta; Romano em Pitra; Cosme de Maiúma, PG 98): **nenhum uso de Nm 15**. A mulher
  que toca a orla (Mt 9,20) aparece muito (Grande Cânon, ode 5 e 9, quinta-feira da 5ª semana; Triódio
  d052 e d054; prece antes da Comunhão do Horológio, «como a Hemorroíssa… tocando a orla»; 11 de
  janeiro, São Teodósio; 12 de julho, Santa Verônica = a Hemorroíssa), mas nenhum hino liga a orla às
  franjas da Lei. «Φύραμα» é muito frequente nos theotokia («a Virgem divinizou a massa dos mortais»),
  sem a primícia de Nm 15. As liturgias de São Tiago e de Crisóstomo pedem perdão dos pecados «voluntários
  e involuntários, conhecidos e por ignorância» e «das ignorâncias do povo» (Hb 9,7), sem Nm 15.
- **Isaac de Nínive em grego, Romano «Sobre a Hemorroíssa»**: não procurados a fundo (Isaac não está na
  PG; o kontákion da Hemorroíssa só em edição moderna).
- **Evágrio**: não usado.

## Cuidados

- **Nilo**: o sermão sobre Lc 22,36 está entre as obras autênticas de Nilo na PG 79 (a seção «Spuria»
  começa logo depois); conferir a atribuição numa clave moderna (CPG) antes de publicar. Edição de
  Migne, grego e latim; transcrição conferida na imagem.
- **Germano**: o começo do parágrafo (as imagens como modelo de virtude) vem do OCR grego, que está
  limpo; a frase das franjas foi conferida na imagem. O texto reproduz «Εἰ δὴ κατὰ Μωσέα νομοθεσία» sem
  artigo, como está impresso.
- **André de Creta**: «ἡ μὴ φυραθεῖσα δι' αὐτῆς ἀρτοποιεῖται» é ambíguo (a nota de Combefis entende:
  das primícias tiradas da massa em Maria se forma o pão, Cristo). A tradução segue essa leitura sem
  forçar.
- **Teofilacto**: posterior a 1054, escritor eclesiástico bizantino (usado por Santo Tomás na *Catena
  aurea*); apresentar como tal. Os fios «escarlates» não estão em Nm 15 (só o jacinto): é o dado que ele
  usa para a leitura cristológica.
- **Antíoco**: relevância 1; só se faltar texto para o trecho 3.

## Só pista (Nm 15)

- **Cosme Indicopleustes**, *Topografia cristã*, fim do livro I (PG 88, 132C–133A; vol. 088, pág. n70):
  cita Nm 15,38–41 inteiro contra quem segue as próprias ideias. Autor da tradição antioquena, ligado à
  Igreja do Oriente: **só pista**.
- **Eutímio Zigabeno**, sobre Mt 23,5 (PG 129, pág. n304): o fio de jacinto costurado na orla para
  lembrar os mandamentos; repete Crisóstomo.
- **André de Creta**, Hom. II sobre a Dormição (PG 97, pág. n628): Rm 11,16 aplicado ao corpo da Mãe de
  Deus, «primícia da massa adâmica divinizada em Cristo». **Doroteu**, *Instrução* I (PG 88, 1621):
  Cristo tomou «a primícia da nossa massa». **Simeão NT**, *Theologica*; **Cabásilas**, *Vida em Cristo* II
  (PG 150); **Palamas** (vol. 150–151): a mesma fórmula, sem Nm 15.

## Pistas para outros capítulos de Números

| Cap. | Autor, obra | Onde | O que diz |
|---|---|---|---|
| Nm 21 (serpente de bronze) | *Apophthegmata*, abade Poimen sobre o abade Nisteroos, 1 | PG 65, vol. 065, pág. n175 | «como a serpente de bronze que Moisés fez para curar o povo, assim era o ancião: tinha toda virtude e, calado, curava a todos» |
| Nm 21 | São Germano, *Sobre o termo da vida* | PG 98, vol. 098, pág. n62 | a serpente de bronze e a providência (diálogo sobre o termo da vida) |
| Nm 21 | PG 98 (autor a conferir; homilia sobre a Cruz?) | vol. 098, pág. n128 | «a elevação da serpente de bronze no deserto prefigurou o mistério da Cruz» |
| Nm 21 | São Teodoro Estudita, *Antirrhetici* (Ezequias quebra a serpente) | PG 99, vol. 099, pág. n191 | por que Ezequias destruiu a serpente de bronze; contra os iconoclastas |
| Nm 25 (Fineias) | São Nilo, *Peristeria*? (vol. 079, pág. n138) | PG 79 | Zambri é o adultério interior; Fineias, «a palavra sacerdotal», mata-o com a lança do ensinamento temível |
| Nm 25 | São Teodoro Estudita | PG 99, vol. 099, pág. n369 | «o grande Fineias de Deus», Cristo, ficou de pé e fez a expiação pela Cruz, e cessou o flagelo |
| Nm 22–24 (Balaão) | Teodoro Estudita, cartas; Antíoco, *Pandectes* (vários) | PG 99 e 89 | menções (Balaão que não pôde falar contra a vontade de Deus) |

Todas as páginas acima são do item https://archive.org/details/PatrologiaGraeca (o n da página do
volume indicado), com OCR grego pesquisável.
