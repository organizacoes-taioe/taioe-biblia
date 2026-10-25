"""Pré-pesquisa do Gênesis, grupo orientais: grava em genesis/<ccc>/base/ os trechos escolhidos à mão (lista ITENS),
fora o Comentário de Efrém, que tem script próprio (gen-orientais-efrem.py).

Uso (da pasta biblia/):
    python3 -I pesquisa/ferramentas/base/gen-orientais-gravar.py 1      # grava os itens de Gn 1

Dois tipos de item:
- 'corpus': o texto sai do Digital Syriac Corpus (cache de gen-orientais-corpus.py), blocos a..b do texto n, com vogais;
- 'texto': o texto vai escrito aqui, conferido na imagem da edição antiga (archive.org). Para o siríaco de Bedjan
  (Jacó de Sarug), sem texto digital, vai a transcrição feita da imagem, SEM VOGAIS, a conferir antes de publicar.
Para outro capítulo, acrescentar em ITENS a chave do capítulo, com os mesmos campos.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ori_siriaco_comum as C  # noqa: E402

RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))
C.SC = os.path.join(RAIZ, 'cache', 'genesis', 'orientais', 'sc', 'data', 'tei')
HOJE = '2026-10-25'
SCRIPT = 'pesquisa/ferramentas/base/gen-orientais-gravar.py'
EFREM = 'Santo Efrém, o Sírio (c. 306–373), diácono de Nísibis e Edessa, Doutor da Igreja'
JACO = 'São Jacó (Tiago) de Sarug (c. 451–521), bispo de Batnan, poeta (santo nas Igrejas siríacas, também a maronita e a siro-católica)'
BEDJAN = 'https://archive.org/details/homiliaeselectae03jaco/page/n{}/mode/1up'

ITENS = {1: [
    dict(tipo='corpus', n=6, a=27, b=28, arquivo='afraates-demonstracao-6',
         titulo='Afraates, Demonstração 6 (Sobre os filhos da aliança), § 14',
         campos=dict(Autor='Afraates, o Sábio Persa (c. 270–c. 345), bispo, o mais antigo Padre siríaco',
                     Obra='Demonstrações, 6: Sobre os filhos da aliança (ܥܠ ܒܢܝ ܩܝܡܐ)',
                     Passagem='Dem. 6, § 14',
                     Edição='J. Parisot, Patrologia Syriaca I/1 (Paris 1894), col. 293–294 (siríaco e latim); texto do Digital Syriac Corpus',
                     Fonte='https://syriaccorpus.org/6',
                     Cobre='alusão a Gn 1,2 («pairava sobre as águas», ܡܪܚܦܐ ܥܠ ܡܝܐ) lida no batismo: na invocação dos sacerdotes, '
                           'o Espírito desce e paira sobre as águas; e Gn 2,7 (o primeiro nascimento, «alma vivente»)',
                     Língua='syr')),
    dict(tipo='corpus', n=14, a=66, b=72, arquivo='afraates-demonstracao-14',
         titulo='Afraates, Demonstração 14 (Exortação), §§ 33–36',
         campos=dict(Autor='Afraates, o Sábio Persa (c. 270–c. 345), bispo, o mais antigo Padre siríaco',
                     Obra='Demonstrações, 14: Exortação (ܬܚܘܝܬܐ ܕܦܝܣܐ)',
                     Passagem='Dem. 14, §§ 33–36 (o § 36 continua até a passagem de Josué)',
                     Edição='J. Parisot, Patrologia Syriaca I/1 (Paris 1894), Dem. 14; texto do Digital Syriac Corpus',
                     Fonte='https://syriaccorpus.org/14',
                     Cobre='Gn 1,6-10 e 1,14: as obras de Deus (o firmamento entre as águas, a terra seca, os luzeiros, o limite '
                           'do mar, § 34); todas as criaturas obedecem à ordem, e o homem desobedece; o mar fica no limite pela '
                           'palavra, não pela natureza, como mostrou o dilúvio (§ 36, com Jr 5,22-23)',
                     Língua='syr')),
    dict(tipo='corpus', n=574, a=0, b=117, arquivo='efrem-hino-natividade-26',
         titulo='Santo Efrém, Hinos sobre a Natividade, 26 (os dias da criação)',
         campos=dict(Autor=EFREM, Obra='Hinos sobre a Natividade (madrashe), 26 (NPNF II/13: hino 19; Lamy II, col. 493–500)',
                     Passagem='Hino 26, estr. 1–13 (estr. 3–9: um dia da criação em cada estrofe, lido no Natal)',
                     Edição='E. Beck, Des heiligen Ephraem des Syrers Hymnen de Nativitate (CSCO 186, 1959), pelo Digital Syriac '
                            'Corpus (CC BY); o mesmo hino em T. J. Lamy, Sancti Ephraem Syri Hymni et sermones II (Malines 1886), '
                            'col. 493–500, com latim (https://archive.org/details/sanctiephraemsy02lamygoog/page/n278/mode/1up)',
                     Fonte='https://syriaccorpus.org/574',
                     Cobre='Gn 1,3-31 (o 1º dia: a luz que rasga as trevas; 2º: o firmamento e as águas; 3º: os botões e as flores; '
                           '4º: os dois luzeiros que os insensatos adoraram; 5º: os répteis e o dragão; 6º: Adão, na sexta-feira) '
                           'e Gn 2,2-3 (o sétimo dia)',
                     Língua='syr')),
    dict(tipo='corpus', n=530, a=17, b=22, arquivo='efrem-discurso-a-hipacio-4',
         titulo='Santo Efrém, Quarto discurso a Hipácio (contra Mani)',
         campos=dict(Autor=EFREM, Obra='Discursos a Hipácio contra as falsas doutrinas (Refutações em prosa), IV',
                     Passagem='Discurso IV (blocos 17–22 do corpus)',
                     Edição='C. W. Mitchell, S. Ephraim\'s Prose Refutations of Mani, Marcion and Bardaisan I (Londres 1912), '
                            'siríaco p. 113–116, tradução inglesa p. lxxxv–lxxxvii (https://archive.org/details/proserefutations01ephruoft); '
                            'texto do Digital Syriac Corpus',
                     Fonte='https://syriaccorpus.org/530',
                     Cobre='Gn 1,14-18 e 1,26-28 contra os maniqueus: o sol e a lua são lâmpadas criadas para o nosso serviço, sem '
                           'palavra nem razão; o homem é maior que o sol; «à nossa imagem» = à imagem da autoridade de Deus, o '
                           'domínio sobre todos os animais, que eles tomaram sobre o homem depois do pecado',
                     Língua='syr')),
    dict(tipo='corpus', n=365, a=150, b=180, arquivo='jaco-de-sarug-sobre-o-amor-de-deus',
         titulo='São Jacó de Sarug, Sobre o amor de Deus e a reconciliação perfeita (memra 26 de Bedjan I)',
         campos=dict(Autor=JACO, Obra='Memra «Sobre o amor de Deus, que veio no seu amor renovar tudo, e sobre a reconciliação perfeita»',
                     Passagem='versos 150–180 do corpus (Bedjan I, p. 613–615)',
                     Edição='P. Bedjan, Homiliae selectae Mar-Jacobi Sarugensis I (Paris–Leipzig 1905), memra 26, p. 614; '
                            'texto do Digital Syriac Corpus (https://archive.org/details/homiliaeselectae01jaco)',
                     Fonte='https://syriaccorpus.org/365',
                     Cobre='Gn 1,26-27 aplicado: modelado à imagem do Filho, o homem só se parece com ele amando quem o odeia; '
                           'quem chama Deus de Pai mostre em si a semelhança do Unigênito',
                     Língua='syr')),
    dict(tipo='texto', arquivo='efrem-atribuido-hinos-epifania-8',
         titulo='Santo Efrém (atribuído), Hinos sobre a Epifania, 8, estr. 15–17',
         campos=dict(Autor='Santo Efrém, o Sírio (atribuído; E. Beck julga os hinos da Epifania de um efremiano posterior, '
                           'séc. V–VI)',
                     Obra='Hinos sobre a Epifania (o batismo), 8',
                     Passagem='Hino 8, estr. 16 (com 15 e 17 para o contexto)',
                     Edição='T. J. Lamy, Sancti Ephraem Syri Hymni et sermones I (Malines 1882), col. 85–86 (siríaco e latim; o '
                            'siríaco não foi transcrito); tradução inglesa de A. E. Johnston, NPNF II/13 (1898), hino 8, estr. 16',
                     Fonte='https://archive.org/details/sanctiephraemsy00lamygoog/page/n137/mode/1up',
                     Cobre='Gn 1,2 e 1,20-21: o Espírito que choca as águas, e as águas que dão à luz répteis, peixes e aves; o '
                           'Espírito Santo que choca as águas do batismo',
                     Língua='la e en (traduções antigas; siríaco na imagem de Lamy)'),
         corpo='''Latim de Lamy (col. 86):

16. In principio spiritus foecunditatis incubavit aquis; et illae conceperunt pepereruntque dracones, pisces et aves.
Spiritus sanctus incubavit aquis baptismi quae pepererunt mysticas aquilas, nempe virgines et Ecclesiae rectores, et
mysticos pisces, puros scilicet mediatores, et mysticos dracones, illos scilicet callidos qui simplices facti sunt sicut
columbae.

17. Adstat gladius Domini in aquis separans filios a patribus, gladius vivus sejungens vivos a mortuis. Qui baptizantur
fiunt virgines et sancti. [...]

Inglês de Johnston (NPNF II/13, https://www.newadvent.org/fathers/3704.htm, Hymn 8):

16. In the beginning the Spirit that brooded — moved on the waters; they conceived and gave birth — to serpents and
fishes and birds.— The Holy Spirit has brooded in Baptism, — and in mystery has given birth to eagles — Virgins and
Prelates;— and in mystery has given birth to fishes — celibates and intercessors; and in mystery of serpents, — lo!
The subtle have become simple as doves!

Siríaco (Lamy I, col. 85, primeiras linhas, lidas na imagem, a conferir): ܒܪܫܝܬ … ܪܘܚܐ ܡܪܚܦܢܝܬܐ / ܥܠ ܡܝܐ ܪܚܦܬ.
ܒܛܢܘ ܘܐܘܠܕܘ / … ܢܘܢܐ ܘܦܪܚܬܐ. / … ܪܚܦܬ ܒܡܥܡܘܕܝܬܐ / ܘܐܘܠܕܬ ܒܐܪܙܐ ܢܫܪܐ …'''),
    dict(tipo='texto', arquivo='jaco-de-sarug-hexaemeron',
         titulo='São Jacó de Sarug, Hexaémeron (memre sobre os seis dias da criação)',
         campos=dict(Autor=JACO, Obra='Hexaémeron: memre «Sobre a criação das criaturas» (ܕܥܠ ܬܘܩܢܐ ܕܒܪܝܬܐ), um por dia',
                     Passagem='1º dia (p. 23), 4º dia (p. 68–70), 6º dia (p. 108)',
                     Edição='P. Bedjan, Homiliae selectae Mar-Jacobi Sarugensis III (Paris–Leipzig 1907), só siríaco; o '
                            'ciclo abre o volume. Transcrição feita da imagem, sem vogais (o OCR do archive.org só serviu para '
                            'achar as páginas)',
                     Fonte=BEDJAN.format(89),
                     Cobre='Gn 1,2 (a ruḥa é vento criado, não o Espírito Santo: p. 23, só pelo OCR); Gn 1,14-17 (a lua que '
                           'cresce e míngua, figura da vida do homem, p. 68; o sol, lâmpada que Deus acende todo dia, p. 70); '
                           'Gn 1,26 (o mundo, cidade cheia de belezas onde se ergue a imagem do Rei, p. 108)',
                     Língua='syr (transcrição da imagem, sem vogais, a conferir)'),
         corpo=f'''## 4º dia, p. 70, linhas 6–16 ({BEDJAN.format(89)})

ܗܘܝܘ ܢܘܗܪܐ ܘܠܢܗܝܪ̈ܐ ܢܘܗܪܐ ܝܗܒ܀
ܟܠܝܘܡ ܝܗܒ ܢܘܗܪܐ ܠܫܡܫܐ ܕܢܬܓܐܐ ܒܗ:
ܘܐܠܘ ܐܗܡܝ ܕܠܐ ܢܬܠ ܠܗ ܚܫܘܟܐ ܗܘܐ ܠܗ܀
ܐܝܟ ܒܒܝܬܐ ܫܪܓܐ ܐܕܠܩ ܘܣܡ ܒܒܪܝܬܐ:
ܘܟܠܝܘܡ ܒܥܐ ܫܪܓܐ ܡܫܚܐ ܡܢ ܛܝܒܘܬܗ܀
ܗܘ ܪܡܐ ܒܗ ܢܘܗܪܐ ܟܠܝܘܡ ܘܡܕܒܪ ܠܗ:
ܕܢܗܘܐ ܣܦܘܩ ܢܘܗܪܗ ܠܥܠܡܐ ܕܣܝܡ ܕܢܢܗܪ ܒܗ܀
ܘܗܘ ܗܘ ܚܝܠܐ ܕܝܗܒ ܠܗ ܠܫܡܫܐ ܢܘܗܪܐ ܕܢܢܗܪ:
ܗܘ ܪܡܐ ܒܗ ܢܘܗܪܐ ܟܠܝܘܡ ܘܡܕܒܪ ܠܗ܀
ܘܠܢܗܝܪ̈ܐ ܟܠܗܘܢ ܗܟܢ ܚܝܠܗ ܐܩܝܦ:
ܘܡܢܗ ܫܩܠܝܢ ܘܗܝܕܝܢ ܝܗܒܝܢ ܢܘܗܪܐ ܠܐܪܥܐ܀

(Linhas 1–4 da mesma página, para o contexto: ܘܡܛܠܗܕܐ ܨܐܕܘܗܝ ܬܩܘܡ ܬܫܐܠ ܢܦܫܐ: ܟܕ ܚܝܪܐ ܒܗ ܘܣܟܝܐ ܒܗ ܘܢܗܝܪܐ ܒܗ܀
ܘܬܟܝܠܐ ܥܠܘܗܝ ܕܐܝܬܘܗܝ ܢܘܗܪܐ ܕܠܐ ܡܫܬܚܠܦ: ܘܟܠܡܢ ܕܣܡܝܟ ܥܠ ܬܘܟܠܢܗ ܡܢܗ ܢܗܪ܀ A linha 5 não foi lida com segurança.)

## 4º dia, p. 68 (a lua), só o assunto

A lua que cresce e míngua «pinta a figura» da infância, da juventude e da velhice; o jovem que brilha e se enche como a
lua deve lembrar que a velhice chega; e Deus «pintou para si uma imagem no sol», com luz cheia que não muda (p. 68–69).
Transcrever da imagem se for usar ({BEDJAN.format(87)}).

## 6º dia, p. 108, linhas 11–16 ({BEDJAN.format(127)})

ܡܕܝܢܬܐ ܕܟܠܗ ܡܠܝܐ ܫܘܦܪ̈ܐ ܒܢܐ ܐܠܗܐ:
ܘܕܢܩܘܡ ܗܘܐ ܒܗ ܝܘܩܢܗ ܕܡܠܟܐ ܟܐܢܘܬܐ ܗܘܬ܀
ܡܕܝܢܬ ܬܒܝܠ ܐܬܬܩܢܬ ܗܘܬ ܡܢ ܐܠܗܐ:
ܘܫܦܝܪ ܗܘܐ ܠܗ ܕܢܩܘܡ ܗܘܐ ܒܗ ܨܠܡ ܐܠܗܐ܀
ܐܦ ܙܕܩ ܗܘܐ ܕܒܒܢܝܢܐ ܬܡܝܗܐ ܕܒܪܐ:
ܢܬܬܨܝܪ ܨܠܡܗ ܘܒܗ ܢܫܬܒܚ ܡܢ ܚܙܝܐ܀

(Linhas 8–10, antes: … ܢܩܝܡ ܠܗ ܨܠܡܐ ܕܢܗܘܐ ܠܫܘܒܚܐ ܕܥܒܘܕܘܬܗ܀ ܘܒܗ ܢܬܚܙܘܢ ܟܠܗܘܢ ܫܘܦܪ̈ܐ ܕܒܪܘܝܘܬܗ: ܘܒܗ ܡܐ
ܕܥܒܕܗ ܢܬܬܢܝܚ ܡܪܝܐ ܡܢ ܬܘܩܢܘܗܝ܀ Linha 19: ܨܒܐ ܐܠܗܐ ܕܢܥܒܕܝܘܗܝ ܠܐܕܡ ܨܠܡܐ ܦܐܝܐ: …)

## 1º dia, p. 23 (só o OCR do archive.org, não conferido; {BEDJAN.format(42)})

ܗܘܐ ܚܫܘܟܐ ܘܢܫܒܬ ܪܘܚܐ ܠܥܠ ܡܢ ܡܝܐ: / ܪܘܚܐ ܒܪܝܬܐ ܠܘ ܩܕܝܫܬܐ ܐܝܟ ܕܐܣܬܒܪܬ܀ / ܪܘܚܗ ܕܡܪܝܐ ܩܪܗ̇ ܗܘܐ ܡܘܫܐ
ܐܝܟ ܕܠܡܐܡܪ: / ܒܪܝܬܗ ܕܡܪܝܐ ܕܡܪܚܦܐ ܗܘܬ ܥܠ ܒܪ̈ܝܬܗ܀ («Houve trevas, e um vento soprou sobre as águas: um vento
criado, não o Santo, como se pensou. Moisés o chamou "vento do Senhor", como se dissesse: a criatura do Senhor, que
pairava sobre as suas criaturas.»)'''),
    dict(tipo='texto', arquivo='diadoco-capitulos-gnosticos',
         titulo='São Diádoco de Fótice, Cem capítulos gnósticos, 4 e 89',
         campos=dict(Autor='São Diádoco (séc. V), bispo de Fótice, no Epiro, asceta',
                     Obra='Cem capítulos sobre a perfeição espiritual (Κεφάλαια γνωστικὰ ρ΄)',
                     Passagem='cap. 4 e cap. 89',
                     Edição='J. E. Weis-Liebersdorf, Sancti Diadochi episcopi Photicensis De perfectione spirituali capita '
                            'centum (Leipzig, Teubner, 1912), p. 6–8 e 124–126 (a PG 65, 1167–1212, só traz o latim)',
                     Fonte='https://archive.org/details/diadochouepiskop00diad_0/page/n133/mode/1up',
                     Cobre='Gn 1,26 («à nossa imagem, conforme a nossa semelhança»): a imagem, dada a todos e renovada no '
                           'batismo; a semelhança, que a graça vai pintando conosco, pelo amor',
                     Língua='grc'),
         corpo='''## Cap. 4 (p. 6–8; https://archive.org/details/diadochouepiskop00diad_0/page/n15/mode/1up)

Πάντες ἄνθρωποι κατ᾽ εἰκόνα ἐσμὲν τοῦ θεοῦ· τὸ δὲ καθ᾽ ὁμοίωσιν ἐκείνων μόνων ἐστὶ τῶν διὰ πολλῆς ἀγάπης τὴν
ἑαυτῶν ἐλευθερίαν δουλωσάντων τῷ θεῷ. Ὅτε γὰρ οὐκ ἐσμὲν ἑαυτῶν, τότε ὅμοιοί ἐσμεν τῷ ἡμᾶς ἑαυτῷ δι᾽ ἀγάπης
καταλλάξαντι· οὗπέρ τις οὐκ ἐπιτεύξεται, εἰ μὴ μὴ πτοεῖσθαι τὴν ἑαυτοῦ ψυχὴν περὶ τὴν τοῦ βίου εὔκολον δόξαν πείσοι.

## Cap. 89 (p. 124–126; https://archive.org/details/diadochouepiskop00diad_0/page/n133/mode/1up)

Δύο ἡμῖν καλὰ ἡ ἁγία χάρις διὰ τοῦ βαπτίσματος περιποιεῖ τῆς ἀναγεννήσεως, ὧντινων τὸ ἓν ἀπείρως τοῦ ἑνὸς
ὑπερβάλλει. Ἀλλὰ τὸ μὲν ἓν εὐθέως χαρίζεται· ἀνακαινίζει γὰρ ἡμᾶς ἐν αὐτῷ τῷ ὕδατι καὶ πάσας τὰς γραμμὰς τῆς
ψυχῆς, τοῦτ᾽ ἔστιν τὸ κατ᾽ εἰκόνα, λαμπρύνει πᾶσαν τὴν ῥυτίδα τῆς ἁμαρτίας ἡμᾶς ἀπονίπτουσα. Τὸ δὲ ἓν ἐκδέχεται,
ἵνα σὺν ἡμῖν ἐργάσηται, ὅπερ ἐστὶ τὸ καθ᾽ ὁμοίωσιν. Ὅταν οὖν ἄρξηται ὁ νοῦς ἐν πολλῇ αἰσθήσει γεύεσθαι τῆς
χρηστότητος τοῦ ἁγίου πνεύματος, τότε ὀφείλομεν εἰδέναι, ὅτι ἄρχεται ἡ χάρις ὥσπερ ἐπιζωγραφεῖν εἰς τὸ κατ᾽ εἰκόνα
τὸ καθ᾽ ὁμοίωσιν. Ὃν γὰρ τρόπον οἱ ζωγράφοι πρῶτον μὲν ἑνὶ χρώματι διαγράφουσι τὸ σχῆμα τοῦ ἀνθρώπου, χροιᾷ δὲ
τὴν χροιὰν κατ᾽ ὀλίγον ἐπανθίζοντες οὕτως τὸ τοῦ ὁμοιογραφομένου ἄχρι καὶ τῶν τριχῶν ἀποσῴζουσιν εἶδος· οὕτω καὶ
ἡ ἁγία χάρις τοῦ θεοῦ πρῶτον μὲν διὰ τοῦ βαπτίσματος εἰς τὸ ὅπερ ἦν, ὅτε ἐγένετο ὁ ἄνθρωπος, ῥυθμίζει τὸν κατ᾽
εἰκόνα. Ὅτε δὲ ἡμᾶς ἴδῃ ἐκ πάσης προθέσεως ἐπιθυμοῦντας τοῦ κάλλους τῆς ὁμοιώσεως καὶ ἑστῶτας γυμνούς τε καὶ
ἀπτοήτους εἰς τὸ αὐτῆς ἐργαστήριον, τότε ἀρετῇ τὴν ἀρετὴν ἐπανθίζουσα καὶ ἀπὸ δόξης εἰς δόξαν τὸ τῆς ψυχῆς εἶδος
ἀναφέρουσα τὸν χαρακτῆρα τῆς ὁμοιώσεως αὐτῇ περιποιεῖ. Ὥστε οὖν ἡ μὲν αἴσθησις δηλοῖ ἡμᾶς μορφοῦσθαι τὸ καθ᾽
ὁμοίωσιν· τὸ δὲ τέλειον τῆς ὁμοιώσεως ἐκ τοῦ φωτισμοῦ γνωσόμεθα. Πάσας μὲν γὰρ τὰς ἀρετὰς διὰ τῆς αἰσθήσεως ὁ
νοῦς κατὰ μέτρον τι καὶ ῥυθμὸν ἄρρητον προκόπτων ἀπολαμβάνει· τὴν δὲ πνευματικὴν οὐ δύναταί τις ἀγάπην κτήσασθαι,
εἰ μὴ ἐν πάσῃ πληροφορίᾳ φωτισθῇ παρὰ τοῦ ἁγίου πνεύματος. Ἐὰν γὰρ μὴ τελείως τὸ καθ᾽ ὁμοίωσιν διὰ τοῦ θείου φωτὸς
ἀπολάβῃ ὁ νοῦς, πάσας μὲν τὰς ἄλλας ἀρετὰς σχεδὸν ἔχειν δύναται, τῆς δὲ τελείας ἀγάπης ἔτι ἄμοιρος μένει. Ὅταν γὰρ
ὁμοιωθῇ τῇ τοῦ θεοῦ ἀρετῇ, ὡς χωρεῖ δὲ ὁ ἄνθρωπος, λέγω, ὁμοιωθῆναι θεῷ, τότε καὶ τῆς θείας ἀγάπης φέρει τὴν
ὁμοίωσιν. Ὡς γὰρ ἐπὶ τῶν ὁμοιογραφουμένων τὸ ἀνθηρότερον ὅλων τῶν χρωμάτων χρῶμα προστεθὲν τῇ εἰκόνι ἄχρι καὶ
τοῦ μειδιάσαι ἀποσῴζει τὴν τοῦ ὁμοιογραφομένου ὁμοιότητα, οὕτως καὶ ἐπὶ τῶν εἰς τὴν θείαν ὁμοίωσιν παρὰ τῆς θείας
χάριτος διαζωγραφουμένων ὁ φωτισμὸς τῆς ἀγάπης προστεθεὶς εἰς τὴν τοῦ καθ᾽ ὁμοίωσιν ὁλοκλήρως εὐπρέπειαν δηλοῖ
γενέσθαι τὸ κατ᾽ εἰκόνα. Οὔτε γὰρ ἀπάθειαν ἄλλη ἀρετὴ δύναται περιποιῆσαι τῇ ψυχῇ, εἰ μὴ ἀγάπη μόνη. Πλήρωμα γὰρ
ἅπαξ νόμου ἡ ἀγάπη. Ὥστε οὖν ἀνακαινοῦται μὲν ἡμέρᾳ καὶ ἡμέρᾳ ὁ ἔσω ἡμῶν ἄνθρωπος ἐν τῇ γεύσει τῆς ἀγάπης,
πληροῦται δὲ ἐν τῇ αὐτῆς τελειότητι.'''),
    dict(tipo='texto', arquivo='eucologio-evlogitaria-defuntos',
         titulo='Eucológio bizantino, Ofício dos defuntos: os «Evlogitaria» (tropários do Bendito sejas)',
         campos=dict(Autor='Liturgia bizantina (tropários anônimos do ofício dos defuntos e das Matinas do sábado)',
                     Obra='Ἀκολουθία νεκρώσιμος εἰς κοσμικούς, τὰ νεκρώσιμα Εὐλογητάρια (Eucológio; também no Horológio, Matinas)',
                     Passagem='2º e 3º tropários (entre os versos «Εὐλογητὸς εἶ, Κύριε»)',
                     Edição='Εὐχολόγιον τὸ μέγα (Veneza 1862), p. 407; o mesmo texto no AGES (Horologion, FuneralEvlog4–5)',
                     Fonte='https://archive.org/details/euchologion-to-mega/page/n423/mode/1up',
                     Cobre='Gn 1,26-27 (com 2,7 e 3,19): criado do nada e honrado com a imagem divina; a imagem que o pecado '
                           'não apaga («sou imagem da tua glória, ainda que traga as marcas das quedas»); a semelhança e a '
                           'beleza antiga a restaurar',
                     Língua='grc'),
         corpo='''Ὁ πάλαι μὲν ἐκ μὴ ὄντων πλάσας με, καὶ εἰκόνι σου θείᾳ τιμήσας, παραβάσει ἐντολῆς δὲ πάλιν με ἐπιστρέψας εἰς
γῆν ἐξ ἧς ἐλήφθην, εἰς τὸ καθ᾽ ὁμοίωσιν ἐπανάγαγε, τὸ ἀρχαῖον κάλλος ἀναμορφώσασθαι.
Εὐλογητὸς εἶ, Κύριε.
Εἰκών εἰμι τῆς ἀρρήτου δόξης σου, εἰ καὶ στίγματα φέρω πταισμάτων· οἰκτείρησον τὸ σὸν πλάσμα, Δέσποτα, καὶ
καθάρισον σῇ εὐσπλαγχνίᾳ· καὶ τὴν ποθεινὴν πατρίδα παράσχου μοι, Παραδείσου πάλιν ποιῶν πολίτην με.'''),
    dict(tipo='texto', arquivo='triodio-1876',
         titulo='Triódio bizantino (Veneza 1876): 1ª semana da Quaresma',
         campos=dict(Autor='Liturgia bizantina (Triódio)',
                     Obra='Τριῴδιον κατανυκτικόν: kontákion do Domingo da Ortodoxia (1º domingo da Quaresma); tropário da '
                          'Hora sexta dos dias da Quaresma',
                     Passagem='Domingo da Ortodoxia, Matinas, depois da ode 6 (kontákion, tom pl. 4); segunda-feira da 1ª semana, '
                              'Hora sexta (tropário, tom 2)',
                     Edição='Τριῴδιον κατανυκτικόν (Veneza 1876), p. 126 e p. 71; o mesmo texto no AGES (Triodion; Horologion, '
                            'Sixth Hour, LentTroparion)',
                     Fonte='https://archive.org/details/triodion-katanyktikon-periechon-hapasan/page/n134/mode/1up',
                     Cobre='Gn 1,26-27: o Verbo encarnado restaura a imagem manchada à antiga forma (kontákion); Gn 1,31 e 2,2: '
                           'no sexto dia e na sexta hora, Cristo pregou na cruz o pecado de Adão (tropário). Na mesma '
                           'segunda-feira da 1ª semana, as Vésperas leem Gn 1,1-13',
                     Língua='grc'),
         corpo='''## Kontákion do Domingo da Ortodoxia (p. 126; https://archive.org/details/triodion-katanyktikon-periechon-hapasan/page/n134/mode/1up)

Ὁ ἀπερίγραπτος Λόγος τοῦ Πατρός, ἐκ σοῦ Θεοτόκε περιεγράφη σαρκούμενος, καὶ τὴν ῥυπωθεῖσαν εἰκόνα εἰς τὸ ἀρχαῖον
ἀναμορφώσας, τῷ θείῳ κάλλει συγκατέμιξεν. Ἀλλ᾽ ὁμολογοῦντες τὴν σωτηρίαν, ἔργῳ καὶ λόγῳ ταύτην ἀνιστοροῦμεν.

## Tropário da Hora sexta, segunda-feira da 1ª semana (p. 71; https://archive.org/details/triodion-katanyktikon-periechon-hapasan/page/n79/mode/1up)

Ὁ ἐν ἕκτῃ ἡμέρᾳ τε καὶ ὥρᾳ, τῷ Σταυρῷ προσηλώσας, τὴν ἐν τῷ Παραδείσῳ τολμηθεῖσαν τῷ Ἀδὰμ ἁμαρτίαν, καὶ τῶν
πταισμάτων ἡμῶν τὸ χειρόγραφον διάρρηξον, Χριστὲ ὁ Θεός, καὶ σῶσον ἡμᾶς.'''),
    dict(tipo='texto', arquivo='nerses-shnorhali-confesso-com-fe',
         titulo='São Nerses Shnorhali, «Confesso com fé» (Հաւատով խոստովանիմ), orações 1 e 2',
         campos=dict(Autor='São Nerses Shnorhali, «o Gracioso» (1102–1173), católicos dos armênios, santo',
                     Obra='Հաւատով խոստովանիմ («Confesso com fé»), 24 orações, uma para cada hora do dia',
                     Passagem='orações 1 e 2',
                     Edição='Preces Sancti Nersetis Clajensis Armeniorum patriarchae viginti sex linguis editae (Veneza, '
                            'S. Lázaro, 1882), p. 1–2 (armênio) e p. 33–34 (latim); também no Wikisource armênio',
                     Fonte='https://archive.org/details/precessanctiners00arme_1/page/n19/mode/1up',
                     Cobre='Gn 1,1-4 rezado: a Trindade, «criador da luz e expulsador das trevas», expulsa as trevas do pecado e '
                           'da ignorância e ilumina a mente',
                     Língua='hy'),
         corpo='''Armênio (1882, p. 1–2):

1. Հաւատով խոստովանիմ եւ երկիր պագանեմ քեզ, Հայր եւ Որդի եւ Սուրբ Հոգի. անեղ եւ անմահ բնութիւն, արարիչ
հրեշտակաց եւ մարդկան եւ ամենայն եղելոց։ Ողորմեա քո արարածոց։

2. Հաւատով խոստովանիմ եւ երկիր պագանեմ քեզ՝ անբաժանելի լոյս. միասնական Սուրբ Երրորդութիւն եւ մի
Աստուածութիւն, արարիչ լուսոյ եւ հալածիչ խաւարի. հալածեա ՚ի հոգւոյ իմմէ զխաւար մեղաց եւ անգիտութեան, եւ
լուսաւորեա զմիտս իմ ՚ի ժամուս յայսմիկ՝ աղօթել քեզ ՚ի հաճոյս, եւ ընդունել ՚ի քէն զխնդրուածս իմ։ Եւ ողորմեա
ինձ բազմամեղիս։

Latim (1882, p. 33–34): 1. Fide confiteor et adoro te, Pater et Fili et Spiritus Sancte; increata et immortalis natura,
Angelorum hominumque et omnium entium creatrix. Tuarum miserere creaturarum. 2. Fide confiteor et adoro te, indivisibilis
Lux, Sancta consubstantialis Trinitas unaque Deitas, lucis creatrix ac tenebrarum dissipatrix; expelle a spiritu meo
peccatorum et ignorantiae tenebras, atque illumina in ista hora mentem meam, ut orem te in beneplacito tuo, atque a te mea
postulata percipiam. Porro miserere mei omnimode peccatoris.'''),
]}


def corpo_corpus(it):
    meta, blocos = C.ler_tei(it['n'])
    linhas, sec = [], None
    for pg, tipo, tx, s in blocos[it['a']:it['b'] + 1]:
        if tipo == 'head':
            continue
        if s != sec:
            sec = s
            linhas.append(f'\n§ {s}' + (f' (p. {pg})' if pg else ''))
        linhas.append(tx)
    return '\n'.join(linhas).strip()


def gravar(cap):
    pasta = os.path.join(RAIZ, 'genesis', f'{cap:03d}', 'base')
    os.makedirs(pasta, exist_ok=True)
    for it in ITENS[cap]:
        campos = dict(it['campos'])
        campos.setdefault('Oriental', 'sim')
        campos['Baixado'] = f'{HOJE}, por {SCRIPT}'
        ordem = ['Autor', 'Obra', 'Passagem', 'Edição', 'Fonte', 'Cobre', 'Oriental', 'Língua', 'Baixado']
        corpo = corpo_corpus(it) if it['tipo'] == 'corpus' else it['corpo']
        txt = f"# {it['titulo']}\n" + '\n'.join(f'- {k}: {campos[k]}' for k in ordem) + '\n\n' + corpo.strip() + '\n'
        p = os.path.join(pasta, it['arquivo'] + '.md')
        with open(p, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(txt)
        print('gravado', p)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit() and int(sys.argv[1]) in ITENS:
        gravar(int(sys.argv[1]))
    else:
        print(__doc__)
