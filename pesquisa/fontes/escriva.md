# São Josemaria Escrivá (1902–1975): obras no escriva.org

Para todos os livros da Bíblia. O Gere tem **autorização do Opus Dei** para usar os textos de São
Josemaria, bastando pôr o link do escriva.org (`direitos`: «autorizado pelo Opus Dei»). Trabalha-se sobre o
**original espanhol**; a tradução para o português é nossa. Primeiro uso: 2026-10-20 (Sl 33–36, Nm 12–16,
2Cor 1–2). O **índice bíblico completo** (livro → capítulo → versículo → obra, ponto e URL) está em
`escriva-indice.md`, gerado pelo script.

## O site

- Endereço: `https://escriva.org/<língua>/<obra>/…`; o espanhol é `es` (há também `pt-br`, `pt-pt`, `en`,
  `it`, `la`…; o seletor de língua de cada página dá o endereço equivalente, com outro *slug* de capítulo).
- **Índice da obra**: `/es/<obra>/` lista as introduções (`/es/<obra>/intro/<slug>/`) e os capítulos.
- **Capítulo**: `/es/<obra>/<slug-do-capítulo>/` traz **todos** os pontos ou parágrafos do capítulo, cada um
  com o número, o texto, as notas de rodapé e o bloco «Referencias a la Sagrada Escritura». Por isso basta
  baixar os capítulos (242 páginas, ~30 MB), e não os ~4500 pontos.
- **Ponto**: `/es/<obra>/<n>/` (ex.: https://escriva.org/es/es-cristo-que-pasa/7/). É o link a citar.
  Nas **Cartas**, `<n>` é a ordem global no volume, e o rótulo é outro: https://escriva.org/es/cartas-1/44/ é
  «Carta nº 2, 21». O script tira o endereço do próprio capítulo (`<a href="/es/<obra>/<n>/" id="ref-…">`).
- **Índice bíblico do site**: `/es/scriptural-reference-index/` → `/es/scriptural-reference/<livro>/`
  (livro numerado de 0 = Gênesis, na ordem da Nova Vulgata; 22 = Salmos, 53 = 2 Coríntios). **Não tem
  Números** (nem Josué, Juízes, Rute…): o que houver desses livros só aparece pelas notas.
- Também há `/es/subject-index/` (índice de matérias), que não foi usado.
- O site responde 403 a pedidos sem cabeçalhos de navegador comuns (`User-Agent`, `Accept`); com eles,
  abre normalmente. `robots.txt` só proíbe busca, RSS e sitemap.

## As obras (15), com o slug

| obra (espanhol) | slug | em português | pontos | citações |
|---|---|---|---|---|
| Camino (1939) | `camino` | Caminho | 999 | 195 |
| Surco (1986) | `surco` | Sulco | 1000 | 173 |
| Forja (1987) | `forja` | Forja | 1055 | 271 |
| Es Cristo que pasa (1973), 18 homilias | `es-cristo-que-pasa` | É Cristo que passa | 187 | 663 |
| Amigos de Dios (1977), 18 homilias | `amigos-de-dios` | Amigos de Deus | 316 | 623 |
| Amar a la Iglesia (1986), 3 homilias | `amar-a-la-iglesia` | Amar a Igreja | 50 | 59 |
| Conversaciones con Mons. Escrivá de Balaguer (1968) | `conversaciones` | Questões atuais do cristianismo | 123 | 123 |
| Santo Rosario (1934) | `santo-rosario` | Santo Rosário | 22 | 15 |
| Via Crucis (1981) | `via-crucis` | Via-Sacra | 14 | 63 |
| En diálogo con el Señor (ed. crítica), meditações | `en-dialogo-con-el-se%C3%B1or` | Em diálogo com o Senhor | 122 | 269 |
| Cartas I (ed. crítica), cartas 1–4 | `cartas-1` | Cartas I | 205 | 350 |
| Cartas II (ed. crítica), cartas 5–8 | `cartas-2` | Cartas II | 242 | 224 |
| Carta 29 | `carta-29` | Carta 29 | 60 | 88 |
| Josemaría Escrivá de Balaguer y la Universidad (discursos) | `josemaria-escriva-de-balaguer-y-la-universidad` | — | 8 | 7 |
| La Abadesa de las Huelgas (1944, tese de direito) | `la-abadesa-de-las-huelgas` | A Abadessa de Las Huelgas | 115 | 0 |

«Citações» = referências bíblicas brutas achadas (antes de juntar por ponto e capítulo).

## Numeração e formato das citações

- **Salmos**: Escrivá cita pela **Vulgata** (grega e latina): «Ps XXXV» dele = **Sl 36 hebraico**; «Ps XXXIII,
  9» = Sl 34,9. Regra: Vulgata 10–112 e 116–145 = hebraico − 1; Vulg. 9 = Sl 9–10; 113 = 114–115;
  114–115 = 116; 146–147 = 147. Tudo o que está em `escriva-indice.md` e nas pistas já está em número
  **hebraico**, com o da Vulgata entre colchetes.
- As notas variam de obra para obra:
  - *Es Cristo que pasa*, *Amigos de Dios*, *Amar a la Iglesia*: sigla latina e capítulo romano
    («Ps XXXII, 5», «Ioh XIV, 9», «2 Cor II, 15»), Vulgata;
  - *Conversaciones*: sigla latina e arábico («Ps 33, 4»), Vulgata;
  - *En diálogo con el Señor* e as *Cartas* (edições críticas): sigla espanhola e hebraico com a Vulgata
    entre colchetes ou parênteses («Sal 35[34],13», «Sal 27(26),4», «2 Co 1,3»);
  - *Camino*, *Surco*, *Forja*, *Santo Rosario*, *Via Crucis*: sem notas; às vezes a referência vem entre
    parênteses no texto («(Lc XXIII,46)»), e o índice do site cobre o resto.
- O **índice do site** numera os Salmos como a edição de cada obra: Vulgata em todas, menos nas Cartas
  (hebraico). Conferido em 2026-10-20 comparando, ponto a ponto, o índice com as notas (ex.: ECP 1, nota
  «Ps XXIV, 4», índice «Salmos 24, 4»; Cartas I 44, nota «Sal 35[34],13», índice «Salmos 35, 13»).
- Há erros de digitação nas notas da edição online de *En diálogo con el Señor* («Jn 26,23», «Lc 28,1»);
  quando o índice do site traz o mesmo versículo com outro capítulo, vale o do site.

## Como o índice foi montado (`ferramentas/base/mod-escriva.py`)

1. `baixar`: os índices das 15 obras e as 242 páginas de capítulo e de introdução, uma por vez, pausa de 1 s,
   para `cache/base/escriva/html/` (fora do git).
2. `analisar`: divide cada capítulo em pontos (`cache/base/escriva/pontos.json`) e junta três fontes de
   referência: o bloco do site, as notas de rodapé e as referências entre parênteses no texto
   (`citacoes.json`). Resultado: 4546 pontos e parágrafos, 3123 referências.
3. `indice`: grava `escriva-indice.md` (2658 entradas ponto × capítulo; as introduções editoriais ficam de fora).
4. `pistas <livro> <de> <até> …` (ou sem números: todos os capítulos que já têm `base/`): grava
   `<livro>/<ccc>/base/_pistas-escriva.md` com o texto espanhol de cada ponto (nas homilias e cartas, só os
   parágrafos que trazem a nota).
5. `sem-ref <livro> <de> <até>`: procura o latim da Vulgata Clementina (drbo.org, cache em
   `cache/base/escriva/vulgata/`) em pontos sem referência ao capítulo (4 palavras seguidas). Somou-se uma
   busca de frases em espanhol («gustad y ved», «buen olor de Cristo», «fuente de vida», «cara a cara»…).
   O que se confirmou à mão entra na lista `MANUAIS` do script e sai no índice como «sem ref.».

## O que se achou nos capítulos da primeira rodada (2026-10-20)

- Sl 33: só ECP 7 (v. 5, numa cadeia de versículos sobre a misericórdia). Sl 34: AD 52 (v. 2), Conversaciones
  123 (v. 4), ECP 7 (v. 8), Forja 1031 (v. 9). Sl 35: Cartas I, Carta 2, 21 (v. 13). **Sl 36: nada.**
- **Números: Escrivá não cita o livro em nenhuma obra** (nem nota, nem índice do site, nem latim da Vulgata
  dos caps. 12–16 no texto). «Cara a cara» (Nm 12,8) aparece muitas vezes, mas sempre como expressão dele
  para a oração pessoal, nunca como citação.
- 2Cor 1: vv. 3 e 12 (3 pontos). 2Cor 2: v. 15, o «bonus odor Christi», em 12 pontos (dois sem referência:
  Caminho 842 e Cartas II, Carta 8, 51).
- Achados traduzidos: `salmos/033` a `036/achados-escriva.json`.

## Armadilhas

- Uma sigla só conta com maiúscula («Num», «Sal»): em minúscula, «números 809» (*La Abadesa*) ou «sal» davam
  falsos positivos.
- «Cara a cara», «leche y miel», «fuente de vida» são frases comuns dele: não tomar por citação sem conferir.
- As introduções das edições críticas (Cartas, *En diálogo*) são dos editores, não de Escrivá: ficam fora do
  índice (as pistas as mostram, se houver, marcadas «introdução»).
