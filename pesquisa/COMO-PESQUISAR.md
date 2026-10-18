# Acervo de pesquisa da Bíblia Taioé

Comentários dos Padres da Igreja e dos santos sobre cada capítulo, guardados de modo que o
capítulo seguinte se pesquise mais depressa. Esta pasta não vai ao ar (só `public/` é publicado).

## Estrutura

- `fontes/<grupo>.md`: catálogo das obras que comentam livros inteiros (ex.: as *Enarrationes*
  de Agostinho, a *Expositio* de Cassiodoro): autor, obra, edição (PL/PG), que capítulos cobre,
  e o endereço exato do texto na internet, com o padrão de URL para achar os outros capítulos.
  É a primeira coisa a ler ao pesquisar um capítulo novo.
- `<livro>/<cap>/textos/<autor>-<obra>.md`: o texto inteiro (ou a parte que trata do capítulo),
  na língua original, com a referência e o link no topo. Só domínio público.
- `<livro>/<cap>/achados.json`: cada excerto candidato, no formato abaixo. É daqui que sai a
  seleção e a organização por temas.
- `<livro>/<cap>/relatorio-<grupo>.md`: o que se procurou, o que se achou, o que não existe
  (ex.: «Hilário não comentou este salmo»), para não procurar de novo.
- `ferramentas/hebraico.py`: o hebraico do AT (morphhb, com lemas Strong e morfologia; cache em
  `cache/morphhb/`, fora do git) para conferir o original: `--ref "Sl 33,19-20"` mostra o trecho
  palavra por palavra, `--lema 5315` lista as ocorrências de uma palavra (uso no topo do arquivo).
- `ferramentas/grego.py`: o grego do NT (MorphGNT sobre a SBLGNT, o texto crítico; cache em
  `cache/morphgnt/`, fora do git): `--ref "2Cor 1,3-7"` (palavra por palavra, ou `--corrido`),
  `--lema παράκλησις` (todas as ocorrências; compara sem acentos).
  Estudos de palavra (ex.: `estudos/nefesh/`) guardam aqui os dados; o texto vai para `revisao/estudos/`.

## Formato de `achados.json` (uma lista)

```json
{
  "id": "agostinho-en32-s1-8",
  "autor": "Santo Agostinho",
  "autor_id": "agostinho",
  "datas": "354–430",
  "titulo_autor": "bispo de Hipona, Doutor da Igreja",
  "obra": "Comentários aos Salmos (Enarrationes in Psalmos)",
  "passagem": "Sl 32, sermão 1, 8",
  "edicao": "PL 36, 283",
  "versiculos": [3],
  "lingua": "la",
  "original": "o trecho exato, na língua original",
  "fonte_url": "https://… (a página onde está o original)",
  "traducao_pt": "rascunho em português do Brasil",
  "temas": ["o cântico novo", "o júbilo sem palavras"],
  "resumo": "uma frase",
  "relevancia": 3,
  "direitos": "domínio público"
}
```

- `relevancia`: 3 = essencial (comentário clássico, bonito, que ilumina o leitor comum);
  2 = bom; 1 = só para registro.
- `direitos`: «domínio público», ou, para textos com direito autoral (Papas recentes, LEV),
  «citação curta»: aí o `original` tem no máximo duas ou três frases, e o resto fica só no link.

## Regras

- Só domínio público nos textos guardados: os originais antigos e traduções antigas (NPNF,
  séc. XIX). Nunca guardar traduções modernas com direito autoral (Fathers of the Church, Ancient
  Christian Writers, Paulus, Vozes…).
- Toda citação com passagem exata e link que abra o texto.
- Rascunho de tradução em português do Brasil contemporâneo, fiel ao original e legível pelo
  leitor comum. Nunca mesóclise (`far-se-á` → `há de fazer-se`); nada de uso europeu
  (facto, «estar a fazer»); nada de pronomes contraídos (mo, lho).
- A numeração dos Salmos nos Padres é a grega e latina (LXX/Vulgata): o nosso Sl 33 é o
  «Salmo 32» deles.
