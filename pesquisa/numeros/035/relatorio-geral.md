# Números 35: relatório da pesquisa (todos os grupos)

Pesquisa de 2026-11-15 (p3536). Numeração: Nova Vulgata (= Vulgata; no hebraico, os mesmos versículos).
Entregues: `achados-geral.json` (18 achados: trecho 1 = 2, trecho 2 = 7, trecho 3 = 8, trecho 4 = 1) e, em `textos/`, os originais que não estão em `base/`:
`ambrosio-fuga-35.md`, `gregorio-hom-ez-35.md`, `bernardo-conv-35.md`, `ruperto-deut-35.md`, `antonio-sermones-35.md` e `origenes-hom-num-28-35.md` (este conferido nas imagens do GCS 30, pp. 283–284).
Nenhum autor novo: todos já estão em `ferramentas/autores.json`. Orientais: Cirilo (3 achados), Teodoreto (1) e Orígenes (1, conforme o cadastro).

## Os achados, em uma linha

Trecho 1 (vv. 1–8, as cidades dos levitas):
- **Ambrósio**, *De fuga saeculi* II, 6–7: as cidades de refúgio cabem aos levitas porque o ministro de Deus é um fugitivo do mundo, que renuncia até aos seus.
- **Cirilo**, *De adoratione* (PG 68, 864–865): os levitas sem herança ficam com o necessário, e a eles se confiam as cidades de refúgio: modelo do cuidado da Igreja pelos presos (Hb 13,3).

Trecho 2 (vv. 9–15, as cidades de refúgio):
- **Orígenes**, *Hom.* XXVIII, 2: as cidades de refúgio, sombra de um lugar preparado por Deus; só quem pecou sem saber foge para lá.
- **Ambrósio**, *De fuga saeculi* II, 5: a lei ensina a fugir do mundo.
- **Ambrósio**, *De fuga saeculi* II, 9: a misericórdia que conhece a nossa fraqueza e oferece vários refúgios.
- **Bernardo**, *De conversione* XXI, 37: «correi às cidades de refúgio»; onde o pecado abundou, superabunda a graça.
- **Santo Antônio**, sermão do 3º domingo da Quaresma, § 6: o nome de Maria, cidade de refúgio até para quem pecou de propósito.
- **Santo Antônio**, sermão do 1º domingo do Advento, § 8: as cinco chagas de Cristo são as cidades de refúgio; na cruz, Cristo acolhe sob as suas asas.
- **Bruno de Segni**, cap. XXXV: voluntário é quem não muda de vontade; o arrependido já pecou «sem querer» e pode refugiar-se.

Trecho 3 (vv. 16–29):
- **Agostinho**, *Quaest. in Hept.* IV, 65: «ele o matará» não dá licença ao vingador; só o já julgado pode ser morto.
- **Cirilo**, *De adoratione* VIII (PG 68, 580): a lei tempera o castigo do involuntário com humanidade.
- **Ruperto**, *In Deut.* I, 5: o machado que escapa da mão; a correção áspera que mata o amigo no amor.
- **Ruperto**, *In Deut.* I, 5: a quem não desagrada o que fez, de nada serve a morte de Cristo.
- **Rábano**, *In Num.* IV, 12: quem leva o irmão à morte da alma é homicida; quem pecou por descuido tem refúgio na Igreja.
- **Gregório Magno**, *Hom. in Ezech.* I, 6, 15: o homicida que volta livre com a morte do sumo sacerdote é o gênero humano libertado por Cristo.
- **Teodoreto**, *Quaest. in Num.* L: por que esperar a morte do sumo sacerdote (Melquisedeque; a ira dos parentes se apaga).
- **Cirilo**, *De adoratione* VIII (PG 68, 581): somos homicidas da própria alma por fraqueza; a alma esteve como numa cidade de refúgio até a morte de Cristo e a descida aos infernos.

Trecho 4 (vv. 30–34):
- **Rábano**, *In Num.* IV, 12: polui a terra quem escandaliza e mata espiritualmente o próximo; só a penitência a limpa e Deus não habita onde reina a imundície.

## Como se procurou

- `base/` do capítulo lido inteiro (Agostinho, Bruno, Cirilo, Paterius, Rábano, Ruperto, Teodoreto, Lápide; Efrém atribuído e Procópio só no latim do OCR, sem excerto).
- Corpus Corporum (782 obras latinas já em cache, `~/.cache/taioe-nm23/latinos/clean`): busca por «civitas/urbs refugii», «fugitivorum», `Num. XXXV`, «mortem pontificis/sacerdotis», «donec moriatur», «cognatus occisi», «ultor sanguinis», «suburbana», «polluere terram»: todos os acertos lidos no contexto (Ambrósio, Jerônimo, Agostinho, Gregório, Ruperto, Bernardo, Lombardo, Gerhoh, Comestor, Pedro Damião).
- Santo Antônio de Pádua (cache `numeros20-modernos/antonio`), Lourenço de Bríndisi, Belarmino, Granada, Sales e Bossuet por «refugii/asyl/Num. XXXV».
- Tomás (*Suma* I-II q. 98–105, II-II q. 61–78 e *Super Hebr.*) baixado do Corpus Thomisticum: nenhuma citação de Nm 35.
- Imagens do GCS 30 (archive.org, página P = imagem n(P+36)) para Orígenes.
- Greek: Cirilo e Teodoreto do texto da PG (PDF khazarzar) que já está em `base/`.
- Cada `original` foi cortado por script do texto baixado, com `[...]` nos cortes.

## O que não existe ou não serviu

- Orígenes não tem homilia só deste capítulo, mas a *Hom.* XXVIII, 2–3 (Nm 33,50–35) trata das cidades de refúgio (entrou). Sobre a morte do sumo sacerdote, Orígenes não diz nada no *Numeros*.
- **Jerônimo**, *Adv. Iov.* II, 33 (PL 23, 331A): fala dos fugitivos «até que morra o Sumo Sacerdote e, descendo aos infernos, liberte as almas»; só serve dentro da discussão com Joviniano sobre os graus de mérito (reserva).
- **Pedro Lombardo**, *Collectanea in Hebr.* (PL 192, 118B) e *Sent.* (col. 795): a morte de Cristo como a morte do sumo sacerdote «em cuja morte os que mataram sem saber eram absolvidos»; repete Gregório e Cirilo (reserva).
- **Gerhoh**, *Com. in Psalmos* (PL 193, 1715A): citação de Nm 35,28, sem comentário próprio.
- **Ruperto**, *In Minor. Prophetas* (Os 6,8, PL 168, 98C): Galaad devia ser cidade de refúgio e virou antro de assassinos; só contexto do profeta (reserva).
- **Bruno**, *Exp. in Num.* XXXV: o resto (as mil passos de arredores, as três cidades como fé, esperança e caridade, o parente como o Samaritano) é número por número; só entrou a leitura de «voluntário».
- **Rábano**, cap. XI: etimologia das seis cidades (Bosor = angústia, Gaulon = revolvimento…), cópia de Orígenes (*Hom. in Jos.*); alegoria nome por nome, não entrou. Os dois achados de Rábano (cap. XII) são o que lhe é próprio na edição de Migne (sem notas de fonte neste trecho; sabe-se que ele compila).
- **Procópio** (PG 87) e **Efrém atribuído** (Assemani I): só no latim do OCR; Procópio tem a mesma ideia de Cirilo (a morte de Cristo, grande sacerdote, solta os que estavam nos infernos). Não entraram; o texto de Efrém no OCR tem «s longo» e siríaco ilegível.
- **Lápide**: reúne as razões do asilo (a ira dos parentes se abranda; o pontífice figura Cristo; o asilo na Igreja) e a história do direito de asilo; modelo moderno, sem acrescentar aos Padres; o OCR exigiria conferir nas imagens (reserva).
- **Belarmino**, *De controversiis* (tomo III, *De Sanctorum beatitudine* I): «nós somos exilados, a pátria é o paraíso, o sacerdote magno é Cristo, após cuja morte já se abre o acesso aos filhos»; bom e curto, mas o volume (`operaomnia03bell_0_djvu.txt`, linha 16145) não tem as páginas marcadas e a imagem não foi conferida (reserva).
- **Siríacos**: Afraates (*Dem.* 3, §4, Nm 35,30: Jezabel e as duas testemunhas contra Nabot, jejum de iniquidade), Liber Graduum e Tito de Bostra (versão siríaca, Nm 35,33): pistas do `_pistas-orientais.md` conferidas só por alto, sem excerto útil. Isho`dad, Teodoro bar Koni, Bar Salibi e Jacó de Sarug: proibidos no site ou não conferidos.
- **Papas, liturgia, Catecismo e São Josemaria**: nenhuma citação de Nm 35 (`_pistas-escriva.md` vazio; o Lecionário não lê este capítulo).
- **Tomás**: nada de Nm 35 na *Suma* (I-II q. 98–105 e II-II q. 61–78) nem no *Super Hebr.* 6,18 («qui confugimus»: cita só o Sl 89 e Pr 18).

## Para outros capítulos

- **Nm 36**: ver o relatório de Nm 36 (Tomás, *S. Th.* I-II q. 105 a. 2: a lei das herdeiras que casam na própria tribo).
- **Dt 19** (cidades de refúgio, de novo): Ruperto, *In Deut.* I, 5 (PL 167, 921C–922A): três cidades = fé, esperança e caridade, equidistantes, e a «verdade da penitência»; Gerhoh e Lombardo (acima).
- **Js 20** (cidades de refúgio, Hom. XXIII de Orígenes sobre Josué, citada por Rábano): Bosor, Ramot, Gaulon…; não baixada.
