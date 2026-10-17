# taioe-biblia

A **Bíblia Taioé**, em `taioe.com.br/biblia/`: tradução própria dos originais, com notas para o
leitor comum e os comentários dos Padres da Igreja e dos santos, organizados por tema, trecho por
trecho. Os capítulos entram um de cada vez. Worker da Cloudflare só com arquivos estáticos:
publica `public/` (só o prefixo `/biblia`, pelo contrato da origem do `taioe-hub`).

Ainda não anunciada: sem link no site, `noindex`, e um caminho em `/admin/`.

## Estrutura

- `conteudo/livros.json`: os livros, na ordem do cânon; `conteudo/<livro>/<ccc>.json`: um
  capítulo (texto, notas, trechos, comentários por tema e o que vai para a revisão).
- `ferramentas/`: Node e Python puros, sem dependências.
  - `importar.mjs <livro> <cap>`: traz o capítulo da tradução de partida (projeto `biblia`, fora daqui);
  - `conferir.mjs`: mesóclise, uso europeu, numeração, notas, comentários (o CI roda);
  - `gerar.mjs`: grava `public/biblia/` (o CI confere com `--conferir`);
  - `revisao.mjs`: monta a página de revisão do Gere (`/admin/biblia/`, conteúdo no `taioe-infra`);
  - `respostas.sh`: baixa as respostas dele e marca as aplicadas (workflow Respostas do `taioe-infra`);
  - `formato.py`: grava o JSON do capítulo legível (um versículo, nota ou comentário por linha).
- `pesquisa/`: o acervo dos comentários (textos de domínio público, excertos candidatos, catálogo
  das fontes). Não vai ao ar. Ver `pesquisa/COMO-PESQUISAR.md`.
- `CAPITULO.md`: como preparar um capítulo novo. `ESCOLHAS.md`: as escolhas de tradução que valem
  para a Bíblia inteira. `revisao/aprendizado.md`: o que as revisões do Gere ensinaram.

## Páginas

`/biblia/` (início) · `/biblia/<livro>/` · `/biblia/<livro>/<cap>/` (texto e notas) ·
`/biblia/<livro>/<cap>/comentarios/` (temas; com vários trechos, `.../comentarios/<trecho>/`) ·
`.../comentarios/<tema>/` (os comentários do tema).

## Rodar no computador

Na pasta `taioe`: `python hub/ferramentas/servir.py` e abrir http://localhost:8777/biblia/.

## Deploy

Workers Builds, a cada push na `main`: comando de build vazio, deploy com `npx wrangler deploy`;
nas outras branches, `npx wrangler versions upload`. Sempre `wrangler.jsonc`, nunca TOML.
