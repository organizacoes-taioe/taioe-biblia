# Números 15: relatório da pesquisa nos Padres orientais não gregos (siríacos, armênios, coptas, etíopes)

Pesquisa de 2026-10-20. O «Efrém atribuído» da edição romana (*In Numeros*, vv. 20, 32–36 e 38) já está em
`achados-gregos.json` e em `base/efrem-in-numeros.md`: não foi repetido. Os Padres do deserto e os bizantinos ficaram com
outra frente.

## Resultado

3 achados em `achados-orientais.json`, todos siríacos e todos sobre o sábado e as franjas (vv. 32–40); o siríaco está em
`textos/siriacos-franjas-15.md`, com o contexto, o latim de Lamy e as notas de transcrição.

| trecho | autor, obra | rel. | o que diz |
|---|---|---|---|
| 5 | **São Jacó de Sarug**, Memra 78 (sobre os dois bodes de Lv 16), Bedjan III, p. 286 | 3 | Deus tratava o povo esquecido como a uma criança e o cercava de lembretes: «por causa do sábado, atou franjas nos mantos deles […]; nas pontas das vestes o desenhou em miniatura, para que se lembrassem do santo sábado» |
| 4 | **Santo Efrém (atribuído)**, *Hinos sobre Juliano Saba* 20, 13 (Lamy III, col. 913–914) | 2 | porque um homem esqueceu o sábado e recolheu lenha, amarraram franjas nas vestes: o hino liga o v. 32 ao v. 38 |
| 5 | **Santo Efrém**, *Sermão sobre Nosso Senhor* § 32 (Lamy I, col. 221–222) | 2 | Deus pôs sinais nos corpos dos cegos (a cegueira de Paulo) e os mandou aos anciãos «que faziam sinais nas pontas dos seus mantos; mas dos sinais dos mantos eles não se lembraram». Usa a expressão exata da Peshitta em Nm 15,38 |

Os dois primeiros recolhem a mesma tradição (também rabínica: Rashi liga as franjas ao homem da lenha) e dão ao capítulo uma
leitura de conjunto: o pecado contra o sábado nasce do esquecimento, e as franjas são o remédio de Deus contra ele. O de Jacó
é o melhor dos três.

Siríaco transcrito da imagem; leituras incertas, que convém um siriacista conferir antes de publicar:

- Jacó: ܒܙܥܘܪܝܬܐ («em miniatura»; o OCR lê ܒܙܚܘܪܝܬܐ, mas troca ܥ por ܚ nesta palavra em todo o Bedjan) e ܩܪܝܐ («o dia
  solene»).
- Juliano Saba: ܐܣܪܘ («amarraram»), uma palavra mal impressa. O latim de Lamy, «fimbrias alligare», confirma o sentido.
- Sermão sobre Nosso Senhor: o trecho termina em «não se lembraram». Na frase seguinte («e os sinais do corpo, não os
  entenderam», no latim de Lamy), uma palavra não se leu com segurança e ficou de fora.

## Onde se procurou

- **Digital Syriac Corpus** (cache `pesquisa/cache/base/sc/`): a busca por n-gramas da Peshitta de Nm 15, com uma cópia de
  `ori-siriaco-buscar.py` que grava fora do cache comum. Depois, buscas por palavra-chave, sem vogais:
  - ܨܘܨܝܬܐ (franjas), ܬܟܠܬܐ (púrpura violeta), ܟܢܦܐ junto de ܡܪܛܘܛܐ ou ܢܚܬܐ (a orla do manto);
  - ܩܝܣܐ junto de ܫܒܬܐ (a lenha e o sábado), ܐܝܕܐ ܪܡܬܐ («de mão levantada»), ܛܘܥܝܝ junto de ܨܒܝܢܐ (erro e vontade);
  - ܚܚܘܪܬܐ e ܐܨܘܬܐ (o bolo e a massa), ܪܫܝܬܐ junto de ܓܒܝܠܬܐ (Rm 11,16), ܢܡܘܣܐ ܚܕ (uma só lei).

  Só deram citação solta ou fórmula comum, fora o que se lista em «Pistas» e em «Anotado».
- **Jacó de Sarug, Bedjan I–V** (archive.org `homiliaeselectae01jaco` … `05jaco`). **Descoberta de método: o OCR siríaco
  desses cinco volumes é aproveitável** (vocalizado, com erros previsíveis). O catálogo `fontes/orientais.md` diz que só há
  imagem: convém corrigir. Para buscar, basta tirar as vogais (script em `scratchpad/ag-orientais/bedgrep.py`). O achado
  saiu daí. Também se conferiu o memra sobre a mulher do fluxo de sangue (Bedjan V, pp. 538–540): é a orla do manto de Cristo,
  sem alusão às franjas da Lei.
- **Efrém em latim**: a busca no OCR latino cobriu Lamy I–IV, a ed. romana siríaco-latina II–III (Assemani/Benedetti),
  Bickell (*Carmina Nisibena*) e o *Comentário ao Diatessarão* (Aucher–Moesinger, 1876, do armênio:
  `evangeliiconcor00ephrgoog`). Termos procurados: fimbria, hyacinth*, ligna junto de sabbat*, primitiae junto de massa ou
  conspersio, per superbiam, per ignorantiam. O siríaco dos dois achados de Efrém foi transcrito da imagem de Lamy.
- **Comentário ao Diatessarão**, sobre a mulher que toca a orla do manto (cap. VII): Efrém fala da fé que «furta» a cura, da
  orla que cura onde os médicos falharam, da rocha ferida por Moisés e da comunhão («se ela tocou a orla com temor, quanto
  mais nós ao tocar o Corpo»). **Não retoma Nm 15**: nada sobre as franjas da Lei nem o violeta. Não virou achado. O texto
  siríaco (Chester Beatty 709, ed. Leloir 1963/1990) tem direito autoral; o armênio (Veneza, 1836) e o latim de 1876 são de
  domínio público.
- **Didascália siríaca** (Gibson, 1903): nada de Nm 15. Pista para Nm 18: o cap. 8–9 cita Nm 18,1–32 por extenso e aplica as
  primícias e os dízimos ao bispo.
- **Armênio**:
  - Gregório de Narek, *Livro das Lamentações*: o texto inteiro, da hy.wikisource (`Մատեան_Ողբերգութեան`, `action=raw`). O
    único eco é a oração 18, sobre a mulher do fluxo de sangue («onde não há orla de manto feito por mãos»): Mt 9,20, sem
    Nm 15.
  - Nerses Shnorhali, *Carta encíclica*: o latim de Cappelletti (1829, `bub_gb_ia0i_jyJALAC`) e o grabar com latim
    (`ShnorhaliGrabarLatin`), sem nada de Nm 15.
  - *Yačaxapatum* (atribuído a São Gregório Iluminador, `Yachakhapatum`): o OCR armênio é ruim demais para buscar.
  - **digilib.aua.am**, de onde vieram os textos armênios do Nm 16, ficou fora do ar o dia todo (502).
  - O poema bíblico de Shnorhali, *Jesus, Filho único do Pai* (Յիսուս Որդի), que reconta o Pentateuco, não se achou em
    edição antiga digitalizada; só a tradução francesa moderna (`jsusfilsuniquedu0000ners`, com direito).
- **Copta**: Shenute, *Œuvres* (Amélineau, I–II, francês) não tem nada de Nm 15. A busca cobriu frange, houppe, hyacinthe,
  bois junto de sabbat, prémices e main levée; as «franges» de lá são as de mantos e véus. Pacômio: as edições das *Vidas*
  são modernas, e não se procurou.
- **Etíope, e a liturgia síria, armênia e copta**: não conferidas. O *Fenqitho* de Mossul e o *Breviarium Chaldaicum* só
  têm OCR siríaco ruim e não têm índice bíblico. Nada indica um uso litúrgico de Nm 15 nesses ritos.

## Pistas (fora da comunhão com Roma: não entram no site)

- **Dionísio bar Salibi**, *Comentário literal a Números*, sobre Nm 15 (https://syriaccorpus.org/231; o siríaco está em
  `textos/siriacos-franjas-15.md`):
  - os sacrifícios mostram que a pena de Nm 14 não anulou a promessa feita aos pais;
  - o bolo das primícias era separado para o pobre e o estrangeiro;
  - «de mão levantada» é o gesto de quem ameaça e insulta o outro, levantando a mão;
  - o homem da lenha continuou a recolher mesmo quando o povo lhe dizia que parasse, e desprezou o aviso;
  - ele seria **Salfaad** (a tradição judaica que o põe como pai das filhas de Nm 27). Foi apedrejado para que a Lei se firmasse
    e não fosse desprezada; mas, como não agira por maldade, Deus deu depois a herança às filhas dele;
  - logo depois do apedrejamento vêm as franjas: «o fio de púrpura violeta que os judeus põem na orla dos mantos, para que,
    ao vê-lo, se lembrem da Lei».

  Essa leitura (a lenha, e depois as franjas) é a mesma de Jacó e do hino de Juliano Saba.
- **Filoxeno de Mabug**, *Discurso* 7 (https://syriaccorpus.org/380): o homem da lenha, apedrejado por toda a comunidade,
  numa lista de castigos do deserto que ensinam o temor de Deus.
- **Moisés bar Kepha**, *Sobre a alma* (https://syriaccorpus.org/474): cita Nm 15,27, «se uma alma pecar», como argumento
  sobre a alma; não comenta o versículo.

## Anotado, sem virar achado

- **Afraates**, *Demonstração* 13, sobre o sábado (https://syriaccorpus.org/13). Não cita o homem da lenha. Diz que o sábado
  «não foi posto como coisa de morte e de vida, nem de justiça e de pecado, mas dado para o descanso» (§ 2), e que os
  sacerdotes no templo, no sábado, «racham lenha e acendem fogo» sem profaná-lo (§ 12). Pode servir de contraponto se o Gere
  quiser um texto sobre o sábado no trecho 4. O siríaco está em `textos/siriacos-franjas-15.md`.
- *Liber Graduum*, Isaac de Nínive, Efrém (*Hinos de Nísibis*, *da Natividade*, *Discursos a Hipácio*) e Narsai: nada
  sobre as franjas, a lenha, o pecado «de mão levantada» ou as primícias da massa (Rm 11,16).

## O que não existe (para não procurar de novo)

- Comentário siríaco seguido de Nm 15 em domínio público: só o de Dionísio bar Salibi, que é pista. O de Isho`dad de Merv
  está na CSCO, com direito.
- Efrém autêntico não comenta Números; o comentário ao Diatessarão não liga a mulher que toca a orla a Nm 15,38.
- Nos 39 memre do Digital Syriac Corpus e nos ~195 de Bedjan, Jacó de Sarug só toca Nm 15 no memra 78.

## Pistas para outros capítulos de Números

- **Nm 18**: a *Didascália*, caps. 8–9 (Gibson, pp. 46–48: https://archive.org/details/didascaliaaposto00gibsuoft). Cita
  Nm 18 por extenso e passa as primícias, os dízimos e a parte dos levitas ao bispo, aos presbíteros e aos pobres; é bom
  candidato para o trecho das primícias de Nm 18.
- **Nm 20–21 e outros**: os cinco volumes de Bedjan podem ser buscados por palavra, sem vogais, com `bedgrep.py`. Antes de
  cada capítulo de Números, vale buscar os nomes e as palavras-chave do episódio (ex.: ܡܝ̈ܐ ܕܡܨܘܬܐ, ܚܘܝܐ ܕܢܚܫܐ, ܒܠܥܡ,
  ܦܝܢܚܤ). O corpus tem só 39 memre, e o OCR de Bedjan cobre os outros.
- **Nm 27** (as filhas de Salfaad): Dionísio bar Salibi identifica o homem da lenha de Nm 15 com Salfaad (só pista).
- **Hinos sobre Juliano Saba 20** (Lamy III, col. 911–916): o hino inteiro compara Juliano Saba a Moisés no Sinai, com a
  serpente de bronze (estr. 18: Nm 21,8-9) e o «deixa-me, e os destruirei» (estr. 17: Ex 32,10).
