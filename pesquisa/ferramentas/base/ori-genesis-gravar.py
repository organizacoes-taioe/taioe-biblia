"""Gênesis, grupo orientais, pesquisa do capítulo: grava em genesis/<ccc>/base/ os trechos de obras NOVAS escolhidos à mão
(lista ITENS, por capítulo). Feito na pesquisa de Gn 2 (2026-10-25) sem mexer em gen-orientais-gravar.py, que outra tarefa
estende para Gn 3–50; o formato dos itens é o mesmo.

Uso (da pasta biblia/):
    python3 -I pesquisa/ferramentas/base/ori-genesis-gravar.py 2      # grava os itens de Gn 2

Dois tipos de item:
- 'corpus': o texto sai do Digital Syriac Corpus (cache de gen-orientais-corpus.py), blocos a..b do texto n, com vogais;
- 'texto': o texto vai escrito aqui, conferido na imagem da edição antiga (archive.org). Para o siríaco de Bedjan (Jacó de
  Sarug), sem texto digital, vai a transcrição feita da imagem, SEM VOGAIS, a conferir antes de publicar.
Páginas do archive.org usadas aqui: Bedjan III, page/n = p. + 19; Assemani III (syr-3), page/n = p. + 76; Triódio de Veneza
(1876), page/n = p. + 8; Eucológio de Veneza (1862), page/n = p. + 16.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ori_siriaco_comum as C  # noqa: E402

RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))
C.SC = os.path.join(RAIZ, 'cache', 'genesis', 'orientais', 'sc', 'data', 'tei')
HOJE = '2026-10-25'
SCRIPT = 'pesquisa/ferramentas/base/ori-genesis-gravar.py'
EFREM = 'Santo Efrém, o Sírio (c. 306–373), diácono de Nísibis e Edessa, Doutor da Igreja'
AFRAATES = 'Afraates, o Sábio Persa (c. 270–c. 345), bispo, o mais antigo Padre siríaco'
JACO = ('São Jacó (Tiago) de Sarug (c. 451–521), bispo de Batnan, poeta (santo nas Igrejas siríacas, também a maronita e a '
        'siro-católica)')
BEDJAN = 'https://archive.org/details/homiliaeselectae03jaco/page/n{}/mode/1up'
ASSEM3 = 'https://archive.org/details/assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-3/page/n{}/mode/1up'

ITENS = {2: [
    dict(tipo='corpus', n=13, a=19, b=26, arquivo='afraates-demonstracao-13',
         titulo='Afraates, Demonstração 13 (Sobre o sábado), §§ 10–13',
         campos=dict(Autor=AFRAATES,
                     Obra='Demonstrações, 13: Sobre o sábado (ܬܚܘܝܬܐ ܕܫܒܬܐ)',
                     Passagem='Dem. 13, §§ 10–13',
                     Edição='J. Parisot, Patrologia Syriaca I/1 (Paris 1894), col. 561–574 (siríaco e latim; § 11 na col. '
                            '563–566, § 13 na col. 569–574); texto do Digital Syriac Corpus',
                     Fonte='https://syriaccorpus.org/13',
                     Cobre='Gn 2,2-3: Deus não se cansou nem trabalhou (§ 10–11; «só Adão ele fez com as suas mãos, e não está '
                           'escrito que se cansou»); se Deus, que não se cansa, descansou, quanto mais quem está sob o trabalho '
                           'e a servidão (§ 11); o sábado em que Deus se compraz: fazer a sua vontade, para entrar no sábado do '
                           'descanso, em que o céu e a terra descansam (§ 13, com Is 28,12; 56,4-5; Hb 4,9). Os §§ 1–9 (o sábado '
                           'não justifica; foi dado para o descanso de servos e animais; não foi dado a Adão porque antes do '
                           'pecado não havia fadiga, § 4) ficaram de fora do corte',
                     Língua='syr')),
    dict(tipo='corpus', n=533, a=9, b=12, arquivo='efrem-contra-marciao',
         titulo='Santo Efrém, Contra Marcião I (refutações em prosa)',
         campos=dict(Autor=EFREM,
                     Obra='Refutações em prosa: Contra Marcião I (ܡܐܡܪܐ ܕܠܘܩܒܠ ܡܪܩܝܘܢ)',
                     Passagem='blocos 9–12 do corpus (o palimpsesto B. M. add. 14623 tem lacunas, marcadas com * * *)',
                     Edição='C. W. Mitchell, A. A. Bevan e F. C. Burkitt, S. Ephraim\'s Prose Refutations of Mani, Marcion and '
                            'Bardaisan II (Londres 1921), siríaco p. 60–61 (paginado da direita para a esquerda: '
                            'p. 61 = page/n375), tradução inglesa p. xxix–xxx '
                            '(https://archive.org/details/cu31924092341670/page/n375/mode/1up, reimpressão); texto do Digital '
                            'Syriac Corpus',
                     Fonte='https://syriaccorpus.org/533',
                     Cobre='Gn 2,17 e 3,22-24 contra Marcião: Adão viveu 930 anos fora da cerca da árvore da vida, e nenhum '
                           '«outro deus» o fez entrar; Deus decretou com justiça «no dia em que dela comeres, certamente '
                           'morrerás», para advertir Adão com amor; depois, voltou-se para a bondade e temperou a dureza da '
                           'justiça: Adão não morreu naquele dia, viveu 930 anos, e agora vive na vida eterna',
                     Língua='syr')),
    dict(tipo='corpus', n=202, a=8, b=11, arquivo='liber-graduum-memra-15',
         titulo='Liber Graduum (Livro dos Degraus), memra 15 (Sobre o desejo conjugal de Adão), § 3',
         campos=dict(Autor='Liber Graduum (Livro dos Degraus), obra ascética siríaca anônima (séc. IV–V)',
                     Obra='Liber Graduum, memra 15: Sobre o desejo do casamento que veio a Adão',
                     Passagem='memra 15, § 3',
                     Edição='M. Kmosko, Liber Graduum (Patrologia Syriaca I/3, Paris 1926), col. 339–342 (siríaco e latim; '
                            'https://archive.org/details/PatrologiaSyriacaIIILiberGraduum_201603); texto do Digital Syriac '
                            'Corpus',
                     Fonte='https://syriaccorpus.org/202',
                     Cobre='Gn 2,25: Adão e Eva nus como crianças de peito, que não sabem o que é nudez e não se envergonham, '
                           'porque não há desejo mau no coração; só o coração puro fica assim diante do outro; Mt 18,3 '
                           '(«se não vos tornardes como crianças»). O resto do memra sustenta que o desejo conjugal veio depois '
                           'do pecado: tese própria da obra, fora do corte usado',
                     Língua='syr')),
    dict(tipo='texto', arquivo='efrem-hinos-paraiso',
         titulo='Santo Efrém, Hinos sobre o Paraíso (ed. romana, latim de Assemani)',
         campos=dict(Autor=EFREM,
                     Obra='Hinos sobre o Paraíso (madrashe «De Paradiso Eden»), na edição romana: Sermo III e Sermo XII',
                     Passagem='Sermo III, começo (Assemani III, p. 569); Sermo XII, fim (p. 597–598)',
                     Edição='J. S. Assemani, S. Ephraem Syri Opera omnia syriace et latine III (Roma 1743), p. 562–598 (os 12 '
                            'primeiros dos 15 hinos; o siríaco ao lado não foi transcrito); a edição crítica de E. Beck (CSCO '
                            '174–175, 1957) tem direito autoral',
                     Fonte=ASSEM3.format(645),
                     Cobre='Gn 2,9.16-17: a árvore do conhecimento no meio do paraíso, guardada pelo temor; Adão entendeu no '
                           'único preceito que nem devia pisar a área dela (III); a serpente ouviu o preceito e persuadiu o '
                           'lavrador a colher os frutos verdes: colhidos no tempo maduro, seriam de vida; as duas árvores, da '
                           'vida e do conhecimento, as duas coisas que tornam o homem semelhante a Deus (XII). O latim é '
                           'paráfrase em prosa de um texto em versos',
                     Língua='la (tradução latina de 1743; o siríaco está na mesma página)'),
         corpo='''> Latim conferido na imagem. O siríaco da edição romana (serto miúdo, na coluna da esquerda) não foi transcrito.

## Sermo III, começo (p. 569, A; ''' + ASSEM3.format(645) + ''')

Arborem scientiae Deus in medio Paradisi plantavit, custodes dedit horrorem & metum, qui areolam, in qua posita erat,
tuerentur. Duo sibi Adamus imperata praesensit in illo unico praecepto, quo ipsi & conjugi vetitae arboris fructus decerpere
& comedere cautum fuerat; intellexit enim non modo eam arborem sibi esse magnopere verendam, sed etiam ejus aream, nec proinde
sibi fas esse eo pedem inferre.

(Segue, em B–D: a serpente soube por Eva o que era o paraíso; o fruto da árvore, «chave da justiça», abriria os olhos dos
transgressores; os olhos dos primeiros pais estavam abertos para o que viam e fechados para a glória do santuário e para a
própria nudez.)

## Sermo XII, p. 597, E–F (''' + ASSEM3.format(673) + ''')

Id porro erat, quo indice serpenti, qui protoplastum decepit, occulta veritas patuisset? Tum ille serpens, respondit, arcanum
didicit, quod tamen ipse sibi ex ingenua sua sapientia compertum credi volebat, audivitque Deum Adamo caventem, ne arborem
scientiae boni & mali contingeret; hujusmodi praeceptum audivit veterator nequissimus, & probe intellexit, indeque incauto
agricolae fraudem machinatus est, suasitque, ut immaturos fructus carperet; inde factum, ut poma, quae maturo tempore
decerpta vitalia & salutaria fuissent, perverso temporis ordine sibi mortifera evaderent. Veritatem callide texit, quippe qui
non ignoraret suis contraria promissis eventura protoplastis mandatum violantibus.

## Sermo XII, p. 598, A–D (''' + ASSEM3.format(674) + ''')

Beneficium scilicet, si eo praeter legem utaris, maleficium fecisti.

Oziam regem sequere templi penetralia impie temerantem, Pontificatum infelix quaerebat, regnum amisit. Adamus quaestum
meditabatur, sua conduplicavit damna. Agnoscite, Fratres, expressam in adytis templi arboris vetitae aream, & in thure ab
Ozia incenso pomum ab Adamo decerptum; lepra punitus Rex, ignominiosa denudatione protoplastus. [...]

Geminas rerum Conditor sevit arbores in Paradiso, arborem vitae, & arborem scientiae, binos videlicet omnium bonorum fontes.
Duae nimirum sunt res, quae hominem Deo similem faciunt, vita morte immunis, & ab errore libera sapientia.
'''),
    dict(tipo='texto', arquivo='jaco-de-sarug-veu-de-moises',
         titulo='São Jacó de Sarug, Sobre os véus no rosto de Moisés (memra 79 de Bedjan)',
         campos=dict(Autor=JACO,
                     Obra='Memra «Sobre os véus no rosto de Moisés» (ܥܠ ܫܘܫܦܐ ܕܒܐܦܝ ܡܘܫܐ)',
                     Passagem='Bedjan III, memra 79: p. 288–289 (Gn 2,24) e p. 299 (Gn 2,21-22)',
                     Edição='P. Bedjan, Homiliae selectae Mar-Jacobi Sarugensis III (Paris–Leipzig 1907), só siríaco; '
                            'transcrição feita da imagem, sem vogais (o OCR do archive.org só serviu para achar as páginas)',
                     Fonte=BEDJAN.format(318),
                     Cobre='Gn 2,24 lido como mistério de Cristo e da Igreja (Ef 5,31-32): Moisés escreveu «deixará o homem '
                           'seu pai e sua mãe» sob o véu dos nomes «homem» e «mulher»; Paulo tirou o véu (p. 288–289, só pelo '
                           'OCR); Gn 2,21-22: o lado do Esposo aberto na cruz, de onde sai a esposa; Cristo dormiu na cruz como '
                           'Adão no seu sono; Eva, mãe dos viventes em figura, e o batismo, mãe da vida (p. 299, lido na imagem)',
                     Língua='syr (transcrição da imagem, sem vogais, a conferir)'),
         corpo='''## p. 299, linhas 9–20 (''' + BEDJAN.format(318) + ''')

ܗܐ ܬܪܝܥ ܓܒܗ ܕܚܬܢܐ ܘܢܦܩܬ ܟܠܬܐ ܡܢܗ:
ܘܫܠܡܬ ܨܘܪܬܐ ܕܚܘܐ ܘܐܕܡ ܗܝ ܕܪܫܝܡܐ܀
ܡܢ ܠܘܩܕܡ ܓܝܪ ܨܪ ܐܢܘܢ ܘܪܫܡ ܐܢܘܢ:
ܠܒܝܬ ܐܕܡ ܒܕܡܘܬ ܨܘܪܬܐ ܕܝܚܝܕܝܗ܀
ܕܡܟ ܒܙܩܝܦܐ ܐܝܟ ܕܕܡܟ ܗܘܐ ܒܫܢܬܐ ܐܕܡ:
ܘܬܪܥܘܗܝ ܠܓܒܗ ܘܢܦܩܬ ܡܢܗ ܒܪܬ ܢܘܗܪܐ܀
ܡܝ̈ܐ ܘܕܡܐ ܠܨܘܪܬܐ ܕܥܘ̈ܠܐ ܐܠܗ̈ܝܐ:
ܕܢܗܘܘܢ ܝܪ̈ܬܐ ܠܐܒܐ ܕܪܚܡ ܠܝܚܝܕܝܗ܀
ܐܡܐ ܕܟܠ ܕܚܝ ܐܝܬܝܗ ܚܘܐ ܒܕܡܘܬܐ:
ܘܡܢ ܗܝ ܐܡܐ ܕܚ̈ܝܐ ܐܠܐ ܡܥܡܘܕܝܬܐ܀
ܐܢܬܬܗ ܕܐܕܡ ܡܝ̈ܘܬܐ ܝܠܕܐ ܦܓܪ̈ܢܝܐ:
ܘܗܕܐ ܒܬܘܠܬܐ ܝܠܕܐ ܚ̈ܝܐ ܘܪ̈ܘܚܢܝܐ܀

(Linhas 1–8 da mesma página, só pelo OCR: as palavras da profecia estavam veladas; veio o Esposo, descobriu-lhes o rosto e
as iluminou; houve a festa de núpcias e a esposa entrou na câmara nupcial. Na linha 14, «ܘܬܪܥܘܗܝ ܠܓܒܗ» foi lido com
dificuldade: conferir.)

## p. 288–289, só pelo OCR (''' + BEDJAN.format(307) + ''')

Moisés pôs no seu livro «deixará o homem seu pai e sua mãe e se unirá à sua mulher, e os dois serão um só», e falava, com os
nomes de homem e mulher, de Cristo e da sua Igreja; o povo não era digno de ouvir o mistério às claras, e Moisés o velou com
uma figura; Paulo, depois de ver, tirou o véu e mostrou ao mundo de quem era a imagem («ܣܡ ܒܟܬܒܗ ܕܢܫܒܘܩ ܓܒܪܐ ܠܐܒܘܗܝ
ܘܠܐܡܗ … ܕܒܟܠܬܗܘܢ ܡܫܝܚܐ ܘܥܕܬܗ ܢܬܡܠܠ ܗܘܐ», OCR da p. 288). Transcrever da imagem se for usar.
'''),
    dict(tipo='texto', arquivo='triodio-1876-sabado-santo',
         titulo='Triódio bizantino (Veneza 1876): Sábado Santo, Matinas',
         campos=dict(Autor='Liturgia bizantina (Triódio)',
                     Obra='Τριῴδιον κατανυκτικόν: Grande e Santo Sábado, Matinas, os Louvores (Αἶνοι)',
                     Passagem='idiómela dos Louvores, tom 2, e o Δόξα, tom pl. 2 («Τὴν σήμερον μυστικῶς»)',
                     Edição='Τριῴδιον κατανυκτικόν (Veneza 1876), p. 411; o mesmo texto no AGES (Triodion, Grande Sábado, '
                            'Matinas: Lauds1, Lauds2 e LaudsGlory). O Δόξα se canta também nas Vésperas da véspera',
                     Fonte='https://archive.org/details/triodion-katanyktikon-periechon-hapasan/page/n419/mode/1up',
                     Cobre='Gn 2,2-3: «E Deus abençoou o sétimo dia»: Moisés prefigurava o sábado abençoado em que o Filho '
                           'descansou de todas as suas obras, guardando o sábado na carne pela morte; o Rei dos séculos '
                           '«sabatiza» no sepulcro e nos dá um novo sábado',
                     Língua='grc'),
         corpo='''## Idiómela dos Louvores, tom 2 (p. 411, coluna da esquerda)

Σήμερον συνέχει τάφος, τὸν συνέχοντα παλάμῃ τὴν Κτίσιν, καλύπτει λίθος, τὸν καλύψαντα ἀρετῇ τοὺς οὐρανούς· ὑπνοῖ ἡ ζωή,
καὶ ᾍδης τρέμει, καὶ Ἀδὰμ τῶν δεσμῶν ἀπολύεται. Δόξα τῇ σῇ οἰκονομίᾳ, δι᾽ ἧς τελέσας πάντα σαββατισμὸν αἰώνιον,
ἐδωρήσω ἡμῖν, τὴν παναγίαν ἐκ νεκρῶν σου Ἀνάστασιν.

Τί τὸ ὁρώμενον θέαμα; τίς ἡ παροῦσα κατάπαυσις; Ὁ Βασιλεὺς τῶν αἰώνων, τὴν διὰ πάθους τελέσας οἰκονομίαν, ἐν τάφῳ
σαββατίζει, καινὸν ἡμῖν παρέχων σαββατισμόν. Αὐτῷ βοήσωμεν· Ἀνάστα ὁ Θεὸς κρίνων τὴν γῆν, ὅτι σὺ βασιλεύεις εἰς τοὺς
αἰῶνας, ὁ ἀμέτρητον ἔχων τὸ μέγα ἔλεος.

## Δόξα, tom pl. 2 (p. 411, coluna da direita)

Τὴν σήμερον μυστικῶς, ὁ μέγας Μωϋσῆς προδιετυποῦτο λέγων· Καὶ εὐλόγησεν ὁ Θεός, τὴν ἡμέραν τὴν ἑβδόμην· τοῦτο γάρ ἐστι
τὸ εὐλογημένον Σάββατον, αὕτη ἐστὶν ἡ τῆς καταπαύσεως ἡμέρα, ἐν ᾗ κατέπαυσεν ἀπὸ πάντων τῶν ἔργων αὐτοῦ, ὁ Μονογενὴς
Υἱὸς τοῦ Θεοῦ, διὰ τῆς κατὰ τὸν θάνατον οἰκονομίας, τῇ σαρκὶ σαββατίσας· καὶ εἰς ὃ ἦν, πάλιν ἐπανελθών, διὰ τῆς
Ἀναστάσεως, ἐδωρήσατο ἡμῖν ζωὴν τὴν αἰώνιον, ὡς μόνος ἀγαθὸς καὶ φιλάνθρωπος.
'''),
    dict(tipo='texto', arquivo='eucologio-1862-matrimonio',
         titulo='Eucológio bizantino (Veneza 1862): ofício da coroação (matrimônio)',
         campos=dict(Autor='Liturgia bizantina (Eucológio)',
                     Obra='Εὐχολόγιον τὸ μέγα: Ἀκολουθία τοῦ στεφανώματος (o rito da coroação, o matrimônio bizantino)',
                     Passagem='3ª oração do sacerdote, antes da coroação («Ὁ Θεὸς ὁ ἅγιος, ὁ πλάσας ἐκ χοὸς τὸν ἄνθρωπον»); '
                              'a 2ª («Εὐλογητὸς εἶ, Κύριε… ὁ τοῦ μυστικοῦ καὶ ἀχράντου γάμου ἱερουργός») cita Gn 2,18-24 por extenso',
                     Edição='Εὐχολόγιον τὸ μέγα (Veneza 1862), p. 246; o mesmo texto no AGES (Euchologion, Wedding, Key0212 e '
                            'Key0213)',
                     Fonte='https://archive.org/details/euchologion-to-mega/page/n262/mode/1up',
                     Cobre='Gn 2,7.18.21-24: Deus modelou o homem do pó, edificou a mulher da sua costela e a uniu a ele como '
                           'auxiliar que lhe corresponda, porque lhe aprouve que o homem não estivesse só sobre a terra; é Deus '
                           'quem une a mulher ao marido (Pr 19,14 LXX); «coroa-os numa só carne»',
                     Língua='grc'),
         corpo='''## 3ª oração (p. 246)

Ὁ Θεὸς ὁ ἅγιος, ὁ πλάσας ἐκ χοὸς τὸν ἄνθρωπον, καὶ ἐκ τῆς πλευρᾶς αὐτοῦ ἀνοικοδομήσας γυναῖκα, καὶ συζεύξας αὐτῷ βοηθὸν
κατ᾽ αὐτόν, διὰ τὸ οὕτως ἀρέσαι τῇ σῇ μεγαλειότητι, μὴ μόνον εἶναι τὸν ἄνθρωπον ἐπὶ τῆς γῆς· αὐτὸς καὶ νῦν, Δέσποτα,
ἐξαπόστειλον τὴν χεῖρά σου ἐξ ἁγίου κατοικητηρίου σου, καὶ ἅρμοσον τὸν δοῦλόν σου (τόνδε) καὶ τὴν δούλην σου (τήνδε),
ὅτι παρὰ σοῦ ἁρμόζεται ἀνδρὶ γυνή. Σύζευξον αὐτοὺς ἐν ὁμοφροσύνῃ· στεφάνωσον αὐτοὺς εἰς σάρκα μίαν· χάρισαι αὐτοῖς
καρπὸν κοιλίας, εὐτεκνίας ἀπόλαυσιν.

## 2ª oração, começo (p. 245–246; pelo AGES, não conferido na imagem)

Εὐλογητὸς εἶ, Κύριε ὁ Θεὸς ἡμῶν, ὁ τοῦ μυστικοῦ καὶ ἀχράντου γάμου ἱερουργὸς καὶ τοῦ σωματικοῦ νομοθέτης, ὁ τῆς ἀφθαρσίας
φύλαξ, καὶ τῶν βιοτικῶν ἀγαθὸς οἰκονόμος· αὐτὸς καὶ νῦν, Δέσποτα, ὁ ἐν ἀρχῇ πλάσας τὸν ἄνθρωπον, καὶ θέμενος αὐτὸν ὡς
βασιλέα τῆς κτίσεως, καὶ εἰπών· «Οὐ καλὸν εἶναι τὸν ἄνθρωπον μόνον ἐπὶ τῆς γῆς· ποιήσωμεν αὐτῷ βοηθὸν κατ᾽ αὐτόν»· καὶ
λαβὼν μίαν τῶν πλευρῶν αὐτοῦ, ἔπλασας γυναῖκα, ἣν ἰδὼν Ἀδὰμ εἶπε· «Τοῦτο νῦν ὀστοῦν ἐκ τῶν ὀστῶν μου καὶ σὰρξ ἐκ τῆς
σαρκός μου· αὕτη κληθήσεται γυνή, ὅτι ἐκ τοῦ ἀνδρὸς αὐτῆς ἐλήφθη αὕτη· ἕνεκεν τούτου καταλείψει ἄνθρωπος τὸν πατέρα
αὐτοῦ καὶ τὴν μητέρα, καὶ προσκολληθήσεται πρὸς τὴν γυναῖκα αὐτοῦ, καὶ ἔσονται οἱ δύο εἰς σάρκα μίαν»· καὶ «οὓς ὁ Θεὸς
συνέζευξεν, ἄνθρωπος μὴ χωριζέτω»· […]
'''),
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
