# Escolhas de tradução da Bíblia Taioé

O registro das escolhas que valem para a Bíblia inteira, para que a tradução fique coerente de
capítulo em capítulo. Ler antes de preparar cada capítulo (`CAPITULO.md`, etapa 1). Cada linha
diz de onde a escolha veio; «a confirmar» é o que espera a resposta do Gere em `/admin/biblia/`.

As regras do projeto antigo (`Software MEU/biblia/CLAUDE.md`, «Tradução») continuam valendo:
português do Brasil contemporâneo; base no hebraico e no grego, na divisão da Nova Vulgata;
fórmulas dos profetas («o Senhor Deus», «oráculo do Senhor»); falas sem aspas, depois de
dois-pontos; nada de mesóclise. **Uma mudou** (o Gere, 17/10): a tradução segue sempre o original,
mesmo onde a NV segue o grego ou o latim, e sem nota de variante; a NV dá só a divisão de capítulos
e versículos, que se segue à risca. No Novo Testamento, o grego de base é o texto crítico (Nestle-Aland
28; a edição SBL, em `pesquisa/ferramentas/grego.py`): 2Cor 1,12 «com a santidade e a sinceridade de
Deus», não «simplicidade» (2Cor 1, aprovado).

## Forma

- Deus é tratado por «tu»; os imperativos plurais com «vós» («Exultai», «Louvai»).
- YHWH = «o Senhor». Adonai YHWH = «o Senhor Deus».
- Salmos: numeração hebraica no título, com a grega e latina entre parênteses: «Salmo 33 (32)».
- Expressão citada dentro do versículo, entre aspas angulares: «haja em mim o «sim, sim» e o «não, não»»
  (2Cor 1,17, pedido do Gere, 18/10).
- Citação no meio da frase, que continua depois dela, também entre aspas angulares, como na Nova
  Vulgata: 2Cor 4,6 (Deus, que disse: «Das trevas brilhe a luz», foi quem brilhou…) e 4,13 (… está
  escrito: «Eu cri, por isso falei», também nós cremos…). A fala que fecha a frase continua sem
  aspas, depois dos dois-pontos (2Cor 4).

## Nomes próprios: os da liturgia do Brasil

Regra do Gere (Nm 12, 17/10): «Para nomes, busque sempre a escolha usada na liturgia do Brasil.»
Vale para pessoas, povos e lugares, também nos comentários dos Padres.

- Fonte: o lecionário da CNBB, o mesmo texto da *Liturgia diária* da Canção Nova
  (liturgia.cancaonova.com/pb/liturgia/<semana>-<dia>[-n]/, os endereços se repetem com -2, -3…) e
  da *Palavra do dia* do Vatican News em português (vaticannews.va/pt/palavra-do-dia/AAAA/MM/DD.html,
  por data, o caminho mais fácil). Achar a data em que o capítulo é lido (o calendário das leituras
  dos dias de semana, ano I e ano II) e conferir os nomes ali.
- Nome que a liturgia não lê no capítulo: procurar em outra leitura do lecionário onde ele apareça;
  se não houver, fica a forma do projeto antigo, com a ortografia de hoje, e a lista vai para o
  `revisao.registro` do capítulo.
- Já fixados: Maria (a irmã de Moisés; nunca «Míriam»), etíope, Faran, Cades, Caleb, Enac, Negueb,
  Josué filho de Num (como no lecionário; Nm 14, escolha do Gere), os amalecitas, hititas, jebuseus, amorreus e cananeus, os descendentes e os
  filhos de Enac, Hori, Tânis, Abimelec (Nm 13 e Sl 34, aprovados); Jefoné, a comunidade (Nm 14);
  Paulo, Timóteo, Silvano, Corinto, Acaia (2Cor 1); Tito, Trôade, Satanás (2Cor 2). Ásia, Macedônia, Judeia, o mar Vermelho e Horma,
  que a liturgia não lê nesses capítulos, ficaram como no projeto antigo (aprovado). Os doze exploradores de Nm 13,4–15,
  que a liturgia não lê, ficaram como no projeto antigo (aprovado). Coré, Datã, Abiram, On, Isaar,
  Caat, Felet e Eliab (Nm 16), que a liturgia não lê, ficaram como no projeto antigo (aprovado).

## Vocabulário

| original | tradução | observação | origem |
|---|---|---|---|
| *hesed* | misericórdia | sem nota de língua | Sl 33 |
| *'ashrê* | feliz (AT) | «bem-aventurado» fica para o grego *makários* do NT | projeto antigo |
| *tsaddiqim* / *yesharim* | os justos / os retos | | projeto antigo |
| *tsedaqá umishpat* | a justiça e o direito | o par sempre junto, nesta ordem | Sl 33 |
| *'emuná* | fidelidade | | projeto antigo |
| *kinnor* | cítara | | projeto antigo |
| *nebel* | harpa | Sl 33,2 saía «saltério» e 144,9 «lira»: corrigir ao entrar o 144 | Sl 33, aprovado |
| *shir hadash* | cântico novo | | projeto antigo |
| *teruá* | aclamação | conferir os lugares em que saiu «júbilo»; Sl 33,3 «tocai com arte, entre aclamações» | Sl 33, aprovado |
| *ruah* | sopro / espírito / vento, pelo contexto | Sl 33,6 «sopro», com nota da leitura trinitária | Sl 33, aprovado |
| *tseva'* (dos céus) | exército | | projeto antigo |
| *tehom* | abismo | | projeto antigo |
| *ned* | dique | as águas «como um dique» (Êx 15,8; Sl 33,7; 78,13) | Sl 33 |
| *'etsá* / *mahshavá* | desígnio / plano | | projeto antigo |
| *benê adam* | os filhos dos homens | sem nota | Sl 33 |
| *nahalá* | herança | | projeto antigo |
| *yir'at YHWH*, *yerê'ayw* | o temor do Senhor, os que o temem | nunca «respeitar»; sem nota | Sl 33 |
| *nefesh* | «alma» quando é o interior da pessoa (quem sente, ama, deseja, se angustia, tem sede, espera, louva, e «de todo o coração e de toda a alma»); nos outros casos, pelo sentido: vida, o pronome, pessoa ou alguém, desejo, garganta, fôlego, ser vivo, morto | o teste: o verbo diz o que se passa dentro da pessoa? Gn 2,7 e Sl 16,10 ficam «alma». Sl 33,19 «livrá-los da morte», 33,20 «A nossa alma espera». Estudo em `revisao/estudos/nefesh.md` | estudo, opção C, aprovada |
| *'ezer* / *maguen* | auxílio / escudo | | projeto antigo |
| *gibbor* | valente | | projeto antigo |
| *Miryam* | Maria | como na liturgia; nunca «Míriam» (corrigir Êx 15,20–21, 1Cr, Mq ao entrarem) | Nm 12, aprovado |
| *anav*, *anavim* | humilde, os humildes | como nos Salmos; «mansos» só no Sl 37,11 (Mt 5,5); o grego *praus* do NT continua «manso» | Nm 12, aprovado |
| *kushi*, *Kush* | etíope, Etiópia | como na liturgia; sem nota sobre Cuxe | Nm 12, aprovado |
| *tsaraat* | lepra | sem nota | Nm 12, aprovado |
| *temuná* | figura | como em Dt 4,12.15 e Êx 20,4 | Nm 12, aprovado |
| *ohel moed* | tenda do encontro | as 10 vezes de «tenda da reunião» (1Rs, 1–2Cr) mudam ao entrar | Nm 12, aprovado |
| *amad* (Sl 33,9.11) | firmar-se / permanecer firme | o eco entre os dois versos | Sl 33, aprovado |
| *'edá* / *qahal* | comunidade / assembleia | as duas juntas: «a assembleia da comunidade» (Nm 14,5); a tradução de partida diz «assembleia» para as duas (91 vezes em Números) | Nm 13, aprovado |
| *nasi* | chefe | também para os estrangeiros (Moab, Madiã); nunca «príncipe» (68 vezes em Números, a mudar) | Nm 13, aprovado |
| *zavat halav udvash* | «(terra) que mana leite e mel» | em toda a Bíblia, embora a liturgia diga «onde corre»: mudar no Êxodo, em Jeremias, Ezequiel, Baruc e no Eclesiástico ao entrarem | Nm 13, aprovado (escolha dele, não a recomendada) |
| *kefir* | leão jovem | o leão novo, já caçador; Sl 104,21 «leõezinhos» muda ao entrar | Sl 34, aprovado |
| *nefilim* | gigantes | como em Gn 6,4 e na liturgia | Nm 13, aprovado |
| *'ayin be'ayin* | olho no olho | diferente de «face a face» (*panim el panim*, Êx 33,11) e de «boca a boca» (Nm 12,8); Is 52,8 | Nm 14, aprovado |
| *taf* / *banim* | os pequenos / os filhos | Nm 14,3.31 «os pequenos», 14,33 «os vossos filhos» | Nm 14, aprovado |
| *'erek appayim verav-hesed* | lento para a ira e rico em misericórdia | como em Êx 34,6; «até a terceira e a quarta geração», sem crase | Nm 14,18, aprovado |
| *'olá*, *zevah shelamim*, *reah nihoah* | oferta queimada, sacrifício de comunhão, aroma agradável | como no Levítico e no Êxodo; Números («sacrifício pelo fogo», «sacrifício pacífico», «odor suave») muda ao entrar | Nm 15, aprovado |
| *bishgagá* | por inadvertência | o pecado sem intenção (Nm 15,22–29), como no Levítico; não «por ignorância» | Nm 15, aprovado |
| *beyad ramá* | de mão levantada | com a nota curta «Isto é, de propósito e às claras, em desafio ao Senhor» (Nm 15,30); o eco com Êx 14,8 | Nm 15, aprovado |
| *ger* | o estrangeiro que mora (entre vós) | como no Levítico; Números dizia «que peregrina» | Nm 15, aprovado |
| *tekhelet* | púrpura violeta | como no Êxodo; Números dizia «púrpura violácea» | Nm 15, aprovado |
| *zaná* (a infidelidade a Deus) | prostituir-se | sem atenuar (Nm 15,39 «atrás dos quais vos prostituís»), como em Lv 17,7 e Êx 34,15 | Nm 15, aprovado |
| *mishkan* | a Morada (do Senhor) | a tenda santa onde o Senhor habita; nunca «tabernáculo» (23 vezes em Números, 61 no Êxodo, a mudar) nem «santuário», que fica para *miqdash* | Nm 16,9, aprovado |
| *mahtá* | turíbulo | «incensário» no Levítico (10,1; 16,12) e «incensórios» em 1Rs 7,50 mudam ao entrarem | Nm 16, aprovado |
| *'edá* de um rebelde | o seu grupo | «Coré e o seu grupo» (Nm 16,5; 17,5) | Nm 16, aprovado |
| *nasa 'avon*, *nasa ḥet* | carregar a iniquidade, carregar pecado | Nm 18,1.22.23.32, como em Nm 14,34 («carregareis as vossas iniquidades»); o projeto antigo diz às vezes «levar» | Nm 18 |
| *mishmeret* | encargo; «cumprir o encargo» | Nm 18,3–5.8, como em Nm 3,7 | Nm 18 |
| *mattaná* (os levitas, o sacerdócio) | dom | Nm 18,6 «são um dom para vós, entregues ao Senhor»; 18,7 «um serviço que eu vos dou como dom» | Nm 18 |
| *terumá*, *harim* | oferta, separar | Nm 15,19–21 e Nm 18 («a oferta do Senhor», «separareis dele… o dízimo do dízimo»); o Levítico do projeto antigo diz «oferta elevada» (Lv 7,14.32–34): mudar ao entrar | Nm 15, aprovado; Nm 18 |
| *tenufá* | oferenda movida | como no Levítico do projeto antigo (Lv 7,30–34); «oferta agitada» em Números (6,20; 8,11–21) muda ao entrar | Nm 18 |
| *ḥoq 'olam* / *ḥuqqat 'olam* | direito perpétuo / lei perpétua | o primeiro é a parte que cabe ao sacerdote (Nm 18,8.11.19, como no Levítico); o segundo, a lei (Nm 15,15; 18,23) | Nm 18 |
| *reshit* / *bikkurim* | primícias / primeiros frutos | duas palavras diferentes (Nm 18,12–13) | projeto antigo |
| *mashḥá* (Nm 18,8) | porção | a parte das ofertas que cabe ao sacerdote | Nm 18 |
| *ḥeleq* (na partilha) | parte | «eu sou a tua parte e a tua herança» (Nm 18,20), como no Deuteronômio («parte nem herança») e no Sl 16,5; Sl 119,57; 142,6 e Lm 3,24 («porção») mudam ao entrarem | Nm 18, a confirmar |
| *ḥerem* | anátema | «consagrado por anátema» (Nm 18,14), com nota curta; Lv 27 («interdito») e Js 6–7 («votado ao extermínio») mudam ao entrarem | Nm 18, a confirmar |
| *ne'um* | oráculo | também fora dos profetas: Sl 36,2 «A transgressão é oráculo para o ímpio» | Sl 36, aprovado |
| *tehom rabbá* | o grande abismo | como em Gn 7,11, Is 51,10 e Am 7,4 | Sl 36, aprovado |
| *re'e 'emuná* | alimenta-te da fidelidade | Sl 37,3, como a Nova Vulgata (*pascere fide*) | Sl 37, aprovado |
| *tsinná* | broquel | junto com *maguen* («escudo»), Sl 35,2; Sl 91,4 «escudo e couraça»: conferir ao entrar | Sl 35, aprovado |
| *'ed hamas* | testemunha falsa | Dt 19,16; Êx 23,1 «dar falso testemunho»; Sl 35,11 | Sl 35, aprovado |
| *psychḗ* | como *nefesh* (opção C): «alma» quando é o interior da pessoa; nos outros casos, pelo sentido | 2Cor 1,23 «Invoco a Deus por testemunha, pela minha vida» | 2Cor 1, aprovado |
| *synergós* | cooperador | 2Cor 1,24 «cooperadores da vossa alegria»; uniformizar Rm 16 e Fl 2,25; 4,3 ao entrarem | 2Cor 1, aprovado |
| *en prosṓpōi Christoû* | na presença de Cristo | 2Cor 2,10, como em 4,6 («no rosto de Cristo»); não «na pessoa de Cristo» | 2Cor 2, aprovado |
| *hikanós* | capaz | 2Cor 2,16 «E quem é capaz disto?», que 3,5–6 retoma («capazes… a nossa capacidade»); nunca «idôneo» | 2Cor 2, aprovado |
| *kapēleúō* | fazer comércio | 2Cor 2,17 «fazem comércio da palavra de Deus»; não «negociar» | 2Cor 2, aprovado |
| *epitimía* | punição | a imposta pela comunidade (2Cor 2,6); não «repreensão» | 2Cor 2, aprovado |
| *palaiá diathḗkē* | a antiga aliança | 2Cor 3,14 «na leitura da antiga aliança», em contraste com a «nova aliança» do v. 6; não «Antigo Testamento» | 2Cor 3, aprovado |
| *katoptrízomai* | contemplar como num espelho | 2Cor 3,18 «contemplando como num espelho a glória do Senhor»; não «refletindo» | 2Cor 3, aprovado |
| *diakonía*, *diákonos* | ministério, ministro | 2Cor 3,3–9; *parrēsía* = «franqueza» (3,12) | 2Cor 3, aprovado |
| *ho theòs toû aiōnos toútou* | o deus deste mundo | 2Cor 4,4, como no lecionário e em Gl 1,4 e Ef 2,2; em 1Cor 1–2 a tradução de partida diz «século» (ver as inconsistências) | 2Cor 4 |
| *ekkakéō* | desanimar | 2Cor 4,1.16 «não desanimamos; pelo contrário…» (o mesmo *allá* nos dois), como Ef 3,13 | 2Cor 4 |
| *nékrōsis* | o morrer (de Jesus) | 2Cor 4,10, ao lado de «a vida de Jesus»; *thánatos* (vv. 11–12) é «a morte»; a Vulgata diz *mortificationem* | 2Cor 4, a confirmar |
| *diaphtheírō* (o homem exterior) | desgastar-se | 2Cor 4,16 «se vá desgastando»; não «corromper», que hoje soa como corrupção moral | 2Cor 4 |
| *hyperbolḗ* | grandeza extraordinária; «acima de toda medida» | 2Cor 4,7 «a grandeza extraordinária do poder»; 4,17 *kath' hyperbolḗn eis hyperbolḗn* | 2Cor 4 |

## Inconsistências conhecidas, para corrigir quando o capítulo entrar

- Hades = «abismo» em Ap 1,18, mas «morada dos mortos» em Ap 6,8; 20,13–14 e At 2,27.
- Sl 144,9 «lira de dez cordas» → «harpa de dez cordas» (escolha do Sl 33,2).
- *Nefesh*: aplicar a opção C em cada capítulo que entrar (o projeto antigo traz «alma» 249 vezes, muitas onde é vida ou pessoa).
- «Míriam» no Êxodo, em 1 Crônicas e em Miqueias → «Maria».
- *Synergós*: «colaborador» em Rm 16 e Fl 2,25; 4,3 → «cooperador», como em 1Cor 3,9 e 2Cor 1,24; 6,1; 8,23 (2Cor 1, aprovado).
- «Nun» → «Num» (o pai de Josué) em Êxodo, Deuteronômio, Josué e onde mais aparecer.
- *Aiṓn* = «século» em 1Cor 1,20; 2,6–8 («os príncipes deste século»), mas «mundo» em 2Cor 4,4, Gl 1,4 e Ef 2,2: decidir com o Gere ao entrar 1 Coríntios («século» hoje se entende como cem anos).
