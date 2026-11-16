# Salmo 45 (44 da LXX e da Vulgata): relatório da pesquisa geral

Pesquisa de 2026-11-15 (conversa p44, lote dos Sl 38–47). Todos os grupos: Padres gregos e latinos,
medievais, Magistério, liturgia e santos modernos. Resultado: **33 achados** em `achados-geral.json`
(de 10 autores), cobrindo todos os versículos de 1 a 18.

## Numeração

- Os `versiculos` seguem a nossa numeração (o título é o v. 1), que aqui coincide com a da Vulgata e a da
  LXX («Eructavit», v. 2; «Audi, filia», v. 11; «Omnis gloria», v. 14). Só o número do salmo muda: 45 hebr.
  = 44 LXX/Vulgata. Os Padres citam «Salmo 44».
- Os gregos leem o título («para os que serão transformados», «o amado») como a transformação do cristão e o
  salmo como cântico de Cristo e da Igreja; os latinos, como epitalâmio de Cristo e da Igreja (Agostinho,
  Jerônimo, Tomás), com a aplicação às virgens consagradas e, depois, a Maria.

## O que entrou

| autor | obra e passagem | achados |
|---|---|---|
| São Basílio Magno | Homilia sobre o Sl 44 LXX (PG 29, 388–416) | 7: a «transformação» do título (v. 1); o «arroto» da alma alimentada pela Palavra (v. 2); o poder da encarnação, «ó valente» (v. 4); a vara de retidão que corrige e consola (v. 7); o óleo da alegria é o Espírito (v. 8); a glória por dentro e a veste de palavra e obra (v. 14); as virgens que vão com alegria (vv. 15–16) |
| Santo Agostinho | Enarrationes, Sl 44 (PL 36, 493–516) | 7: Cristo belo em toda parte, inclusive na cruz (v. 3); a flecha que derruba Saulo (v. 6); odeia o que fizeste, ama o que Deus fez (v. 8); ouve para ver (v. 11); a beleza que ele mesmo fez (v. 12); os bispos, pais que a Igreja gera (v. 17); a cidade que no céu se conhece (v. 18) |
| São João Crisóstomo | Exposições sobre os Salmos, Sl 44 LXX (PG 55, 182–203), §§ 4, 11, 12 | 6: Cristo se fez maldição para nos dar bênção (v. 3); esquece o povo e a casa do pai (v. 11); o esposo, senhor e pai (vv. 11–12); a beleza é a da alma (v. 14); a virgem crucificada e alegre (vv. 15–16); a estéril, mãe de muitos (v. 17) |
| São Jerônimo | Cartas 22 (a Eustóquio, 1) e 65 (a Principia, explicação do Sl 44; PL 22) | 4: «Audi, filia» como saída da terra e do pai (vv. 11–12); o mais belo e o desfigurado de Isaías (v. 3); a rainha à direita é a Igreja (v. 10); virgens, viúvas e continentes ao tálamo do rei (vv. 15–16) |
| Teodoreto de Ciro | Interpretação dos Salmos, Sl 44 LXX (PG 80, 1189–1197) | 3: o perfume da paixão e as igrejas de marfim (v. 9); o rosto da Igreja é Cristo (v. 13); as franjas de ouro são os carismas (v. 14) |
| São João Paulo II | Audiências gerais de 29/09 e 06/10/2004 (Salmo 44, ciclo de Laudes e Vésperas) | 2 (citação curta): beleza e justiça (vv. 3, 5, 8); as vestes, sinal da luz interior (vv. 14–15) |
| São Tomás de Aquino | Postilla super Psalmos, Sl 44, n. 9 | 1: a glória por dentro, de três modos (v. 14) |
| Cassiodoro | Expositio Psalmorum, Sl 44, Vers. 13 | 1: bela porque o Esposo a uniu a si (vv. 12–13) |
| Santo Ambrósio | *De virginibus* I, 36–37 (PL 16, 199) | 1: reino, ouro e beleza da virgem consagrada (vv. 7, 10) |
| São Josemaria Escrivá | *É Cristo que passa*, n. 178 | 1: a liturgia da Assunção aplica a Maria «o rei se enamorou da tua beleza» (vv. 12, 14) |

Autores novos: nenhum (todos já estão em `ferramentas/autores.json`).

## Correções de OCR e de transcrição nos originais

Todas deliberadas, só de letra; o resto é substring exata do texto guardado:
- Basílio: «ἐφρό νουνὡςνήπιος» → «ἐφρόνουν ὡς νήπιος» (v. 1);
- Teodoreto: «Ἐκ κλησίᾳ» → «Ἐκκλησίᾳ» (v. 13);
- Jerônimo, Carta 65, 8: «sidercum» → «sidereum»;
- marcas de coluna, números de página da edição e números de notas de Migne foram tirados dos latinos; as
  marcas «[PG n]» dos gregos também.

## Como se procurou

- `base/`: lidos por inteiro Basílio (a homilia toda) e as seções do Sl 45 em Crisóstomo (§§ 4, 11, 12),
  Teodoreto (quase todo), Agostinho (§§ 1, 3–7, 14–18, 25–26, 30–33), Tomás (n. 1, 2, 9) e Cassiodoro
  (vv. 2, 10–13). Jerônimo, Carta 65, lida nos §§ 5–10, 15–16 e 19–21; Jerônimo (Cartas 22 e 65) e Ambrósio
  (*De virginibus*) vieram do Corpus Corporum (PL; textos guardados em `textos/`).
- **Não lidos por inteiro, por economia**: Crisóstomo §§ 1–3, 5–10 e 13; Atanásio; Cirilo; Orígenes
  (Selecta e fragmentos); Eusébio; Belarmino (OCR sujo); Bruno de Segni e Bruno Cartuxo; Haimo;
  pseudo-Beda; pseudo-Jerônimo; Arnóbio; Lombardo; Afonso. Podem ter o que dizer sobre os vv. 2, 4–5, 9 e 18.
- Citações em outras obras: busca das notas «(Psal. XLIV, n)» em ~830 textos da PL (Bernardo, Gerhoh, Bruno de
  Asti, Gregório Magno, Jerônimo, Ambrósio, Honório etc.); só se guardou o que não repetia o que já havia
  (Ambrósio, *De virginibus*). Os trechos de Bernardo (por exemplo, *De laudibus Virginis Matris*, que cita o v. 3) não
  foram lidos com vagar e não entraram.
- Papas: 2 audiências de João Paulo II (baixadas de vatican.va para `pesquisa/cache/salmos38-47/p44/`);
  o Catecismo não cita o salmo. Escrivá: só o n. 178 de *É Cristo que passa* (o n. 164 só cita o v. 2 de passagem).
  Outros Papas: nenhum comenta o salmo (ver `base/_ausentes-modernos.md`).

## O que não existe

- Ambrósio, *Enarrationes in XII psalmos*, não comentou o Sl 44 Vulgata; Hilário também não.
- Basílio comentou o salmo (a homilia usada). Gregório de Nissa só cita o título.

## Para outros capítulos e pistas

- **Crisippo de Jerusalém** (séc. V, Homilia sobre a Mãe de Deus) aplica os vv. 11–12 à Anunciação a Maria; é
  citado por João Paulo II na audiência de 06/10/2004, n. 5 (*Testi mariani del primo millennio*, I, pp. 605–606).
  O texto grego não foi obtido. Autor novo se alguém o achar (oriental).
- Bernardo cita o v. 11 em *De consideratione*, *In festo S. Martini* e nos *Sermones in Cantica* (PL 182–184);
  não lidos, ficam como pista (aplicação ao pastor e à alma esposa).
- Jerônimo, Carta 65, §§ 9–14 e 21–22 (graça nos lábios, trono e unção, a «Tiro» e a posteridade) não entraram
  por já haver o mesmo em Agostinho e Crisóstomo; podem servir ao Sl 45 se faltar algum versículo.
- Hb 1,8-9 cita os vv. 7–8: não pesquisado nos comentários a Hebreus.
