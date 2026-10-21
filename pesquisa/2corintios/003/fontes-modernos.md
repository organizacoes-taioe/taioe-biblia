# Fontes modernas para 2Cor 3 (grupo «modernos»): só o que é novo

Complementa `../001/fontes-modernos.md`, `../002/fontes-modernos.md` e `../../fontes/paulo.md` § 4. Pesquisa de
2026-10-20.

## 1. Varredura dos Papas em 25 segundos (em vez de 12 minutos)

- Pré-filtro com `grep -rlZ -i -E` sobre o HTML **bruto** dos ~7.100 documentos do cache de Nm 14
  (`…/639cd05d-…/scratchpad/dl/fr/docs`, `pp/docs`, `leo/docs`) e dos documentos maiores baixados em 2Cor 1–2
  (`…/7b3b5d55-…/scratchpad/mod/docs`, italiano; `…/c528d87d-…/scratchpad/mod2/docs`, latim), com a sigla tolerante
  a etiquetas: `Cor(\s|<[^>]*>|&nbsp;)*3(\s|<[^>]*>|&nbsp;)*,` mais frases do capítulo em italiano («lettera uccide»,
  «gloria in gloria», «viso scoperto», «inchiostro», «tavole di carne», «c'è libertà», «capacità viene da Dio»,
  «lettera di Cristo», «Signore è lo Spirito», «ministero dello Spirito») e em latim («littera occidit», «ibi
  libertas», «revelata facie», «a claritate in claritatem», «sufficientia nostra», «velamen»). Deu 275 arquivos em
  22 s; só esses são limpos em Python (`scan.py` no scratchpad desta conversa, `…/9acafcb3-…/scratchpad/modernos/`).
  O `grep` devolve caminhos `/c/...`: trocar por `C:/...` antes de abrir no Python.
- O cache **não tem discursos** (*speeches*), como já se sabia: os discursos vieram pelo Clerus (abaixo).

## 2. Clerus, perícope de 2Cor 3

- Página de citações do capítulo inteiro (o Clerus trata 2Cor 3,1-18 como uma perícope só):
  https://www.clerus.org/bibliaclerusonline/en/9abuypc.htm (link no ícone `title="2Co 3,1-18"` de `bnh.htm`).
- Rendeu o que a varredura não dá: o **Denzinger** (DS 377, Orange can. 7; DS 893, Vienne, *Ad nostrum*, erro 3;
  DS 1690, Trento sessão XIV cap. 8; DS 3807, *Mystici Corporis*), os **discursos** de Bento XVI (Cúria, 22/12/2008;
  Bernardins, 12/09/2008, que está numa página junto com uma entrevista de avião) e de João Paulo II (1983, 1987,
  1990, 1998, 2002) e o Lecionário francês. Script: `clerus/get.py` (baixa as páginas em paralelo e mostra o
  contexto de cada «2Co 3,x»).
- **Denzinger latino do Clerus, mapa de páginas** (para achar um DS sem o link): `dvj` ≈ DS 615–688, `dvl` ≈ 680–756,
  `dvm` ≈ 757–797, **`dvk` ≈ 850–993 (Vienne, DS 891–898)**, `dvn` ≈ 844–1209, **`dvo` ≈ 979–1264 (Vienne, censura DS
  899)**, `dvv` = Trento sessão XIV (DS 1690). As páginas se sobrepõem e não seguem a ordem do DS: procurar o número.

## 3. Santos

- **Santa Elisabete da Trindade**: os *Souvenirs* de 1913 (Carmelo de Dijon, domínio público), com as cartas e o
  «Dernière retraite de Laudem gloriae» inteiros, têm OCR no archive.org:
  https://archive.org/details/soeurlisabethd00li (`_djvu.txt`). Página do livro = `page/<n>` no leitor. O texto foi
  retocado pela priora (Madre Germana); a edição crítica (C. De Meester, 1979–1980) tem direitos e não está na
  internet. Ela cita muito 2Cor 3,18 («de clarté en clarté»): pp. 146, 238, 274, 278.
- **São Francisco de Sales**: o *Index scripturaire* (t. XXVII, p. 296; imagem já renderizada em
  `…/c528d87d-…/scratchpad/fs27_288.png`) dá para 2Cor 3: v. 2-3 I, 199; v. 5 IV, 117.142.232; V, 253; VII, 52.115.163.190;
  VIII, 5; IX, 58.85.135; XXII, 49; XXVI, 303; v. 6 V, 253; VII, 95.101; XXIII, 183; v. 7 VIII, 221.277; IX, 251.358;
  v. 13 VIII, 221; v. 14 VIII, 274; v. 15 VIII, 66; v. 17 XII, 279; v. 18 IV, 168; IX, 21; XIV, 234. Deslocamentos do
  PDF: t. IV, página do livro + 93 (índice de página `\f` = livro + 92); t. XII e XIV, achar pelo número impresso no
  topo (`A n n é e 1604 279`). O índice às vezes erra por uma página (IV, 168 está na p. 172).
- **São João da Cruz**: o `jc.txt` da DCO tem só uma citação de 2Cor 3: *Subida* II, 19, 5 (3,6). Nenhuma de 3,18
  («de claridad en claridad», «misma imagen», «transformamur» não aparecem).
- **Santo Afonso**: na concordância do IntraText, `sufficientes`, `sufficientia` e `idoneos` acham 2Cor 3,5-6 em 8 obras;
  `occidit` e `vivificat` só dão outros textos (Jo 6,63; 1Sm 2,6); `velamen`, `speculantes`, `transformamur`,
  `atramento`, `ministratio` não acham 2Cor 3. Script: `…/7b3b5d55-…/scratchpad/py/afonso.py <pasta-cache> <palavras>`.
- **Santa Teresinha**: *Story of a Soul* (Project Gutenberg 16772, anotado): nenhuma citação de 2Cor 3.
- **São Josemaria**: o cache `pontos.json` (4.546 pontos) da pré-pesquisa está em
  `…/4d741f60-…/scratchpad/wt3/pesquisa/cache/base/escriva/pontos.json` (campos `obra`, `rotulo`, `url`,
  `paragrafos`): permite busca de frases em espanhol sem baixar o site.

## 4. Liturgia

- **Vatican News** confirma as leituras dos dias de semana (ver `liturgia-2cor-3.md`); o 8º domingo do ano B é raro
  e não tem data recente.
- **Liturgia das Horas, índice não-bíblico de catholic-resources**: o nome do dia vem **depois** da leitura na tabela
  convertida em texto; conferir pelo número da página (1ª leitura p. N, 2ª leitura p. N+1).
- **Divinum Officium**: a cópia latina está em `…/7b3b5d55-…/scratchpad/mod/do/divinum-officium-master/web/www/`;
  `grep -rn "^!2 Cor 3"` dá Missal e Breviário em segundos.
