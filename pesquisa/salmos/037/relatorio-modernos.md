# Salmo 37 (Vulgata 36, «Noli aemulari»): santos modernos, São Josemaria, Magistério e Liturgia — relatório

Pesquisa de 2026-10-20/21. **19 excertos** em `achados-modernos.json` (8 de relevância 3, 10 de relevância 2, 1 de
relevância 1), escolhidos para dizer coisas diferentes entre si. Textos de domínio público em `textos/`:
`newman-sermoes.md`, `sales-citacoes.md`, `joao-da-cruz-noite-escura.md`, `afonso-obras-asceticas.md`,
`liturgia-missal-e-breviario.md`. Numeração: neste salmo a da Vulgata coincide com a hebraica (o título faz parte do v. 1).
Nenhum autor novo: todos os nomes já estão em `ferramentas/autores.json`.

## 1. São Josemaria Escrivá (1 achado)

- **Cartas I, Carta 2, n. 26** (vv. 23–24), https://escriva.org/es/cartas-1/49/: o vaso de barro quebrado e consertado com
  grampos, mais bonito depois, e «el Señor le tiende su mano». Rel. 3.
- Procurado sem achar: as 15 obras do escriva.org foram baixadas de novo (242 capítulos, 4546 pontos; cópia do script
  `mod-escriva.py` com cache em `p-modernos/escriva/`, fora do WT) e varridas pelo latim e pelo espanhol dos versículos
  («Delectare in Domino», «deléitate», «Revela Domino», «encomienda al Señor tu camino», «Noli aemulari», «no te irrites»,
  «fui joven», «justo abandonado», «mansueti», «Os iusti», «la boca del justo», «Spera in Domino», «Custodi innocentiam»,
  «cedros del Líbano», «non collidetur», «tiende su mano»…). Só o ponto acima. («Iacta super Dominum curam tuam» é o Sl 55,23,
  não este salmo.)

## 2. Santos modernos (9 achados)

- **São Francisco de Sales** (2). Index scripturaire do t. XXVII (p. 234), «Ps. XXXVI»: VIII, 182; v. 3 XIX, 143; v. 20 XIII, 240,
  XVI, 53; v. 24 XVIII, 136, XX, 245; v. 27 X, 398, 424; v. 30 III, 228; v. 35 VIII, 181; v. 40 XIV, 119. Entraram: **carta à
  Sra. de la Valbonne** (XVIII, 135–136, v. 24: a mão de Deus debaixo dos que caem sem malícia, que os levanta sem que percebam;
  rel. 3) e ***Introduction* III, 26** (v. 30: a língua do justo, como a abelha, só lida com o mel de Deus). Os demais são citações
  de passagem ou remissões (detalhe em `textos/sales-citacoes.md`); XIX, 143 e XX, 245 não se acharam no OCR. **Sales não usa os
  vv. 4 e 5.**
- **São João da Cruz** (1): ***Noche oscura* II, 20, 2** (v. 4: o sétimo degrau do amor, a ousadia de quem se deleita em Deus e
  alcança o que pede; rel. 3). É a única citação do salmo nas obras (busca «Sal. 36»). As entradas do Clerus «Dark Night 2, 25»,
  «Ascent 3, 17», «Spiritual Canticle 39» são do Sl 37 da Vulgata (= 38 hebraico).
- **Santo Afonso** (3, fora da *Traduzione*, que está em `base/afonso-salmi.md`). Concordância do IntraText (*delectare* 14,
  *revela* 5, *collidetur*, *supponit*, *derelictum*, *mansueti*, *commodat*). O v. 4 é o versículo de Afonso para «só Deus contenta
  o coração» (nove obras dizem o mesmo): ficou ***Apparecchio alla morte* XXI, 3** (rel. 2). Entraram também ***Modo di conversare
  … con Dio*, n. 13** (v. 5: contar a Deus até as coisas miúdas, como a um amigo; rel. 3; a obra é «tirada de uma obrinha francesa»
  e ampliada por Afonso) e ***Pratica di amar Gesù Cristo* XII** (v. 11: o céu e, já aqui, a paz). Ficou só no texto: *La vera
  Sposa di Gesù Cristo* II, 9 (v. 24, as pequenas quedas que humilham), por repetir Sales e Escrivá.
- **São John Henry Newman** (3). Varrida a cópia local dos 1698 arquivos do newmanreader (de outra conversa). Entraram: **PPS I, 18
  «Obedience the Remedy for Religious Perplexity»**, sermão inteiro sobre o v. 34 (todo o salmo é um «Fret not thyself»; o remédio
  da perplexidade é obedecer; rel. 3); o **discurso do «Biglietto»** (12/05/1879), que termina com o v. 11 (rel. 3; **citado por São
  João Paulo II** na homilia do consistório de 21/02/2001); e ***Difficulties of Anglicans* I, 10, § 9** (1850: «Noli aemulari» e
  os vv. 16–17, 35–36 aplicados às crises da Igreja). Só citações: PPS I, 22; V, 16; VI, 14; VI, 19; VIII, 9; *Oxford University
  Sermons* 4; *Subjects of the Day* 18, 23, 26; *Arians*; *Essays* II (lista em `textos/newman-sermoes.md`).
- **Procurados sem resultado**: **Santa Teresa** (Vida, Caminho, Moradas e Fundações em espanhol, DCO: só «cae siete veces al día
  el justo», que é Pr 24,16); **Jean-Pierre de Caussade** (não canonizado; *L'abandon à la Providence divine*, tradução inglesa de
  1887 no archive.org: nenhuma citação do salmo); **Santa Faustina** (diário em inglês e espanhol, cópia local: nada; o polonês não
  foi visto). **Não procurados por falta de tempo ou de texto acessível**: Santo Inácio, São Cláudio de la Colombière, Santa
  Teresinha, São Carlos de Foucauld, São Pio de Pietrelcina, São Francisco Xavier, Bossuet (*Liber Psalmorum*, OCR ruim; ver
  `fontes/modernos.md` § 12), Vianney.

## 3. Magistério (3 achados)

- **Varredura do vatican.va** (italiano): 10.348 documentos (índices anuais de audiências, homilias, Angelus, cartas e *cotidie*
  de João Paulo II desde 1978, Bento XVI, Francisco e Leão XIV, mais encíclicas, exortações, cartas e motu proprio; mensagens e
  discursos ficaram de fora, porque os índices têm outro formato). Atenção: vatican.va escreve «<i>Sal</i> 37,3», com etiqueta no
  meio; o `grep` tem de aceitar `Sal(</i>)? *37`. Achados no Sl 37 hebraico (= 36 Vulg.):
  - **Francisco, audiência geral de 19/02/2020** («Beati i miti»): a bem-aventurança cita o Sl 37; os mansos não conquistam a
    terra, herdam-na. Rel. 3.
  - **Francisco, *Gaudete et exsultate* 74** (vv. 9.11): manso é quem espera no Senhor; possuir a terra é ver cumpridas as promessas.
    Rel. 2 (original espanhol).
  - **Francisco, Angelus de 01/11/2022** (v. 37): «l'uomo di pace avrà una discendenza». Rel. 2.
  - Só registro: Bento XVI, *Ecclesia in Medio Oriente* 10 («Solo l'umile gusterà le delizie di una pace insondabile», cfr Sal 37
    [36],11) e Angelus de 11/11/2012 (v. 3, tema da Jornada de Ação de Graças na Itália); João Paulo II, homilia do consistório de
    21/02/2001 (cita Newman, ver acima). A audiência de João Paulo II de 05/11/1986 («Sal 37,5») e a de 02/06/2004 são do Sl 37 da
    Vulgata (= 38 hebraico). O *cotidie* de 19/09/2016 («non irritarti…») é Pr 3,31, não o salmo.
- **Bento XVI, *Jesus de Nazaré* I** (a bem-aventurança dos mansos e o Sl 37): livro com direito autoral, fora da internet;
  **não se conseguiu conferir o texto** (nem em alemão, nem em tradução). Fica como pista para quem tiver o livro.
- Confirmado de novo: nenhuma catequese do ciclo das Laudes e Vésperas trata o salmo; o Catecismo não o cita (`_ausentes-modernos.md`).

## 4. Liturgia (6 achados)

- **Liturgia das Horas (1971)**: o salmo inteiro no **Ofício das Leituras da terça-feira da II semana**, em três partes; título
  «Sors malorum et iustorum», frase do NT Mt 5,5, antífonas dos vv. 5, 27 e 34 (latim conferido no Universalis, 27/10/2026). Texto
  da CNBB: a conferir no livro.
- **Missal de 2002** (Clerus, páginas do *Missale Romanum*, ed. typica tertia; varridas todas as páginas por «Ps 36»):
  - **Comum dos Doutores da Igreja, antífona de entrada 1: «In medio Ecclesiae…» (Eclo 15,5), «Vel: Ps 36,30-31 Os iusti meditábitur
    sapiéntiam, et lingua eius loquétur iudícium; lex Dei eius in corde ipsíus (T.P. allelúia)»** (p. 943). **Sim: o Sl 37,30–31 é
    antífona de entrada à escolha no Comum dos Doutores.** A mesma alternativa no Comum dos Santos, «Pro monachis et religiosis, A.
    Pro abbate» (p. 958).
  - Comum dos Mártires, fora do Tempo Pascal, formulário 3: entrada «Salus iustórum a Dómino…» (Cf. Ps 36,39) (p. 911).
  - Missas para diversas necessidades, n. 13 «Pro religiosis», A: entrada Ps 36,3-4 «Spera in Dómino… Delectáre in Dómino…» (p. 1102).
  - **Nenhuma antífona de comunhão do Missal de 2002 é tirada do Sl 37** (nem o v. 4, nem outro). As antífonas «Ne derelinquas me»
    (domingo XXXI do Tempo Comum, p. 481, e uma quarta-feira da Quaresma, p. 222) são do Sl 37 da Vulgata (= 38 hebraico).
- **Missal antigo (1570–1962)** (Divinum Officium; os comuns da Missa estão em `horas/Latin/Commune/`): intróito «Os justi» com o v. 1
  como salmo (Comum dos Confessores não pontífices), Gradual «Os justi» nos Doutores e em muitos santos; Gradual «Justus cum ceciderit,
  non collidetur: quia Dominus supponit manum suam» (vv. 24.26; Comum de um Mártir, Missa «Laetabitur»); intróito «Salus autem
  justorum» com o v. 1 (Comum de vários Mártires); gradual de São João Bosco (vv. 3–5); outros usos isolados em
  `textos/liturgia-missal-e-breviario.md` e `base/liturgia.md`.
- **Breviário antigo**: Matinas da segunda-feira (tridentino, antífonas dos vv. 1, 17, 37; versículo do v. 34); saltério de 1911,
  antífona «Revela Domino viam tuam»; versículo monástico «Delectare in Domino»; responsório com Mq 6,8 + v. 3. Rel. 1.
- **Lecionário (1981)**: refrão do OLM 321 (sexta-feira da 3ª semana, ano I) conferido no lecionário americano: v. 39a («The
  salvation of the just comes from the Lord»). O latim do Ordo e o texto da CNBB dos seis dias de semana ficam a conferir (o site da
  USCCB passou a bloquear depois da primeira página; o romanliturgy.org só tem os domingos).

## 5. Ferramentas (para repetir)

- Escrivá: copiar `pesquisa/ferramentas/base/mod-escriva.py` trocando `CACHE` por uma pasta do scratchpad, `baixar` + `analisar`
  (4 min), e procurar frases no `pontos.json`.
- Missal de 2002 no Clerus: páginas `gkz`, `gk0`…`gk5` (pp. 4–127), `gla`…`glz` (pp. 128–1119) e `gl0`…`gl5` (pp. 1120–1318),
  em `https://www.clerus.org/bibliaclerusonline/en/<código>.htm`; referência no texto como «Ps 36,30-31» (Vulgata).
- Divinum Officium: baixar só as pastas latinas (`codeload…tar.gz`, 19 MB); as linhas `!Ps 36:24` dão a referência.
- Francisco de Sales: o OCR do archive.org separa as palavras com dois espaços; normalizar os espaços antes de procurar.
