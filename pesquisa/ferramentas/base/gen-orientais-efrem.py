"""Pré-pesquisa do Gênesis, grupo orientais: Santo Efrém, Comentário ao Gênesis (Explanatio in Genesim).

O único texto do comentário autêntico em domínio público é a edição romana: J. S. Assemani e P. Benedetti, S. Ephraem
Syri Opera omnia syriace et latine, t. I (Roma 1737), p. 1-115 (siríaco do Vat. sir. 110 e tradução latina de
Benedetti ao lado). A edição crítica de R.-M. Tonneau (CSCO 152-153, 1955) tem direito autoral (no archive.org só
empréstimo: ingenesimetinexo0000ephr). O siríaco de Assemani é miúdo e o OCR é inútil: o script corta o LATIM
(OCR do archive.org, sem correção) e acrescenta, para cada capítulo, os trechos que já foram conferidos na imagem
(dicionário CONFERIDOS). Antes de publicar, conferir o latim na imagem da página e, se possível, o siríaco.

Uso (da pasta biblia/):
    python3 -I pesquisa/ferramentas/base/gen-orientais-efrem.py 1          # grava genesis/001/base/efrem-comentario-genesis.md
    python3 -I pesquisa/ferramentas/base/gen-orientais-efrem.py --ver 40 60 # mostra o começo de cada página (folhas 40-60)
                                                                         # para escolher as âncoras de um capítulo novo
Para um capítulo novo: rodar --ver, achar a frase latina que abre o capítulo e a que abre o seguinte, pôr as duas
em CORTES (expressões regulares sobre o OCR, que troca ſ por f e erra acentos) e rodar com o número do capítulo.
Página impressa = folha (page/nNN do archive.org) - 20 no começo do volume (n26 = p. 6, n38 = p. 18): conferir no
cabeçalho da imagem, porque pranchas e folhas soltas mudam a conta.
Cache (fora do git): pesquisa/cache/genesis/orientais/ (a1_search.txt.gz e a1_pageindex.json.gz, ~1,2 MB).
"""
import gzip, json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))  # pesquisa/
CACHE = os.path.join(RAIZ, 'cache', 'genesis', 'orientais')
ID = 'assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-1'
BASE_URL = 'https://archive.org/download/' + ID + '/Assemani%20et%20alii%201732-1746%20-%20Ephraem%20Syri%20opera%20omnia%20Syr%201'
PAG = 'https://archive.org/details/' + ID + '/page/n{}/mode/1up'
HOJE = '2026-10-25'
SCRIPT = 'pesquisa/ferramentas/base/gen-orientais-efrem.py'

# âncoras (regex sobre o OCR) do começo e do fim de cada capítulo do Gênesis no comentário
CORTES = {
    1: (r'N\s+principio\s+creavit\s+Deus\s+[fs]ub', r'Nunc\s+per-?\s*git\s+porro'),
}

# trechos já conferidos na imagem: capítulo -> [(folha, página, versículos, latim)]
CONFERIDOS = {
    1: [
        (26, 6, 'Gn 1,1', '''In principio creavit Deus substantiam Coeli, & substantiam Terrae: hoc est Coeli, & Terrae naturas vere existentes. Nemo ergo in opificio sex dierum allegoricas interpretationes quaerendas esse, contendat; sed neque fas est, ea quae discretis dierum spatiis condita dicuntur, uno temporis momento facta fuisse, affirmare: neque rursus existimare, ea esse nomina sine rebus, aut non ipsas res, quas illa propriè significant, designare, sed alias. Imo vero, sicut Coelum & Terram in principio creata fuisse legentes, intelligimus eadem fuisse verum Coelum & veram Terram, nec aliud quidpiam hisce vocabulis significari: ita reliquas etiam rerum ordinationes & opera quae secuta sunt, adeo vanas appellationes non esse credamus oportet; ut rerum naturas nominum proprietati planissimè consentire fateamur.

In principio creavit Deus Coelum & Terram. Hic sistito, quia cum Coelo Terraque nihil aliud conditum fuit. Ipsae quoque naturae hac die productae, nec dum prodierant; si enim Coelo Terraeque contemporaneae fuissent; utique id minime Moses reticuisset. Sed nec antequam conderentur, illas nominavit, ne nomina rebus antiquiora faceret. Hinc porrò planum fit, Coelum & Terram ex nihilo educta fuisse; quia nec dum erant aquae, aut spiritus, ignis, aut lux, aut nox: coelo quippe terraque recentiora sunt: Creaturae ergo sunt; quia illis posteriora sunt: neque sempiterna sunt; quia ante illa non fuerunt.

Indicata coeli terraeque creatione, Moses transit ad ea, quae inter firmamentum terraeque orbem velut in medio posita sunt: quae vero supra firmamentum summa obtinent, silentio praeterit. [...] Subdit itaque, terram fuisse tohu, & bohu, hoc est desertam, & vacuam, docens, vacuum & inane rerum substantiis antiquius esse; non quod vacuum rem esse credamus; sed ut inde nobis constet, solam terram extitisse; praeterea nihil.'''),
        (28, 8, 'Gn 1,2 (o «espírito» que pairava = o vento)', '''Dixerat: tenebrae erant super faciem abyssi. Nunc subdit: & spiritus Domini incubabat aquis. Etsi Interpretes nonnulli his verbis Spiritum Sanctum indicari crediderint, atque hinc colligant, eidem communem esse cum reliquis divinis personis naturam & virtutem rerum creatricem; nihilominus pii homines non ex iis, quae consentanea non sunt, Spiritui Sancto divinitatem asserunt, sed ex iis dumtaxat, quae de illo dicta fuisse, ipsis plane constiterit. Legimus enim spiritum Dei malum invasisse Saulem. Sed nec ad Spiritum Sanctum pertinere constat, quod de ejus incubatione hoc loco subjicitur. Quid enim ab ea incubatione primo die ex aquis factum est? Si autem eo die, quo aquis incubabat, nihil ex aquis factum est, die vero quinta, qua ex aquis pisces & volucres prodiere, spiritus aquis incubasse non dicitur; quis creatricem virtutem illi attribuat? qui quamvis aquis incubasse dicatur, nihil tamen ex illis produxisse dicitur eo die, quo incubabat. Ergo quemadmodum ex nubium effectu, qui umbra fuit, earundem creationem primo diei affigendam esse colligimus; ita ex effectu aëris, qui spiritus, seu ventus est, Mosen ejusdem creationem insinuare voluisse existimamus. [...] Caeterum quia aëri innatum est in spiritum seu ventum fluere, idcirco hic dicitur incubuisse aquis, hoc est, flasse. Spiritus ergo ille flabat super aquas, suamque a divino Opifice originem praedicabat. Post paulo, eodem nempe die, spirare desiit; quod pariter nubibus accidit, continuo atque die eodem evanescentibus.'''),
        (33, 13, 'Gn 1,2-5 (as trevas)','''Tenebrae etiam nec sempiternae sunt, nec aliquando coeperunt; sed umbra sunt; sicut Scriptura insinuat. Nec enim ante coelum, nec post nubes, sed una cum nubibus, & ex nubibus natae sunt; atque alteri substantiae haerent; quia propriam non habent; eaque deficiente, continuo deficiunt. Quod autem, altero desinente, pariter desinit, non extantibus aequiparatur: aliud quippe causa est, ut sit quod est. Tenebras ergo, quae nubes & Firmamentum sequuntur, primamque illam lucem, & solem fugiunt, quomodo sempiternas & a seipsis esse dicamus? nimirum alterum, quum panditur, illas parit, alterum, quum oritur, perimit. Si enim hoc producit, efficitque ut sint, & illud facit, ut non sint; quomodo sempiternae sint? Animadvertite, ut nubes & Firmamentum sub ipsam mundi constitutionem tenebras pepererunt, utque lux eodem die exorta continuo illas dissolvit. Si autem tenebras altera creatura condidit, & altera extinxit (altera quippe tenebras eadem hora perpetuo repraesentat, & altera, quo momento accidit illas evanescere, easdem discutit) affirmare cogimur, alteram tenebris initium, alteram finem dare. Si autem creaturae tenebras creant, & destruunt, sequitur ipsas esse creaturarum creaturam: quia pandente se umbra Firmamenti, tenebrae simul oppanduntur; sole autem exoriente, occidunt & evanescunt. Hoc tamen, quod perpetuo creaturis subditum cernimus, dogmata quaedam inimicum creaturarum constituunt: & quod nec propriam habet substantiam, sempiternum, & ex semetipso suspensum faciunt.
(À margem: «Taxat Manichaeos [...] August. contra Faustum».)'''),
        (35, 15, 'Gn 1,9-12', '''[...] Divino itaque imperio concitae illico in unum locum confluxere aquae. Terraeque superficies eadem nocte, atque momento eodem, quo praeparatos gurgites petebant aquae, siccata est.

His ita de nocte compositis, Deus, aperiente se die, jussit terram herbas & gramina omnis generis, pomiferarum item arborum varias species proferre. Et gramina quidem & herbae, etsi reputanti exactum ab ortu tempus, momentum vix excederent; at earundem subitum incrementum, & absolutionem intuenti, plurium mensium id opus esse videbatur. Arbores similiter, etsi nec unum a sua procreatione diem numerabant, contemplantibus tamen ipsarum perfectionem, & fructuum ex earum ramis pendentium copiam, & prae- [p. 16] stantiam, multorum annorum aetatem praeseferebant. Interim terra foenum animantibus, duos post dies in lucem prodituris parabat; & poma ferebant arbores Adae, & ejus Conjugi quarto abhinc die e Paradiso ejiciendis, futuram annonam.'''),
        (37, 17, 'Gn 1,16 (a lua; adultos e novos)', '''[...] Quamobrem tum ex loco, in quo luna posita fuit, tum ex ejusdem specie, & forma, sequitur illam creatam fuisse in eo statu, qualem habere solet die a coitu solis quintadecima.

Caeterum perinde ut arbores, plantae, terrestres & volucres bestiae, atque ipse homo adulti simul, & novelli dici poterant; adulti quidem, illorum speciem, staturam, & robur contemplanti; novelli vero, eorumdem aetatem supputanti: ita luna senescens, & crescens eadem die dici potuit: crescens quidem, quia eodem nata momento; senescens vero, quia plenum sinuata in orbem apparuit, qualis quinto decimo die praenitet.'''),
        (38, 18, 'Gn 1,26-27', '''Dixitque Deus. Cui? quemve alloquebatur Deus hic & alibi, quando Universum moliebatur? Patet Filio Patrem locutum fuisse, quum Evangelista scribat: Omnia per ipsum facta sunt & sine ipso nihil factum est: & quum Paulus de illo definiat, & dicat: In ipso condita sunt universa in coelis, & in terra, visibilia, & invisibilia.

Et ait Deus. Faciamus hominem ad imaginem nostram: ea scilicet potestate praeditum usque modo, ut nihil impediat, quo minus, si ipsi placeat, nobis parere possit, sui arbitrii jurisque. Qua autem in re Dei imago simus, Moses indicat subdens: ut praesit piscibus maris & volucribus ac bestiis atque universae terrae: potestate ergo & imperio, quod in terram resque terreno orbe comprehensas, homo accepit, imago Dei est, qui superis inferisque dominatur.

Quod subdit: masculum & foeminam fecit eos: ostendit in viro mulierem comprehensam, in costa scilicet eidem mox detrahenda. [...]'''),
        (39, 19, 'Gn 1,28', '''Benedixitque eis Deus & dixit: crescite & multiplicamini; & replete terram, & subjicite eam; & dominamini piscibus maris & volatilibus, & omni bestiae, quae movetur super terram. In hoc ergo terreno orbe protoplastae benedictionem accepere. Hunc nempe locum ipsis, antequam peccarent, habitandum destinaverat Deus; quia antequam peccarent, peccaturos praesciebat.

Crescite & multiplicamini, & replete terram, non Paradisum, ait, sed terram, & dominamini piscibus maris, & volatilibus, & omni bestiae. [...]

Sed enimvero quamquam Adam conditus, & benedictus fuerit, ut terrae & bestiis in ea positis dominaretur; nihilominus illi Deus in Paradiso domicilium fixit: sic suam ostendens praescientiam, quum homini benediceret; bonitatem, quum illi beatissimam sedem destinaret. In Paradisum namque Adamum transtulit, & in amoenissimo loco collocavit; ne illum deliciarum hortum non in gratiam hominis condidisse diceretur; & rursus ne ejus peccatum minime praescivisse crederetur, in hoc terreno orbe ei benedixit. Benedictionibus autem transgressionem antevertit; ne culpa hominis Dei benedictiones in cassum reciderent, atque universum in nihilum redigeret hominis stultitia, propter quem omnia pridem e nihilo Deo jubente prodierant. In Paradiso itaque hominem Deus non benedixit; quia tum locus, tum res ibidem positae susceperant benedictionem: benedixit autem Adae in hoc terreno orbe, ut benedictio, quam gratia anteferebat, maledictionem, a ju- [p. 20] stitia post paulo ferendam dilueret. Et quamquam Dei benedictio promissio fuerit, quae ante Adae e Paradiso exitum impleta non fuit; gratia tamen res fuit: eodem namque die in paradisum hominem transtulit, gloria & honore coronavit, & super ejus loci arbores constituit.'''),
    ],
}


def baixar(url, nome):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, nome)
    if not os.path.exists(p) or os.path.getsize(p) < 1000:
        urllib.request.urlretrieve(url, p)
    return p


def carregar():
    t = gzip.open(baixar(BASE_URL + '_hocr_searchtext.txt.gz', 'a1_search.txt.gz'), 'rt', encoding='utf-8').read()
    idx = json.load(gzip.open(baixar(BASE_URL + '_hocr_pageindex.json.gz', 'a1_pageindex.json.gz'), 'rt'))
    return t, idx


def folha(idx, pos):
    for i, (a, b, *_r) in enumerate(idx):
        if a <= pos < b:
            return i
    return None


def latino(linha):
    """Fica só com as linhas que parecem latim (o OCR do siríaco vira lixo)."""
    s = linha.strip()
    if len(s) < 4:
        return False
    toks = s.split()
    minusc = [w for w in toks if re.fullmatch(r"[a-zæœ&ſ]+-?[,.;:?!]?", w)]
    return len(toks) >= 3 and len(minusc) >= 0.5 * len(toks)


def cortar(t, idx, cap):
    ini, fim = CORTES[cap]
    m1 = next(m for m in re.finditer(ini, t) if folha(idx, m.start()) >= 21)
    m2 = next(m for m in re.finditer(fim, t) if m.start() > m1.start())
    blocos, atual = [], None
    pos = m1.start()
    for linha in t[m1.start():m2.start()].split('\n'):
        f = folha(idx, pos)
        pos += len(linha) + 1
        if not latino(linha):
            continue
        if f != atual:
            atual = f
            blocos.append(f'\n[folha n{f}, p. {f - 20} (conferir), {PAG.format(f)}]\n')
        blocos.append(linha.strip())
    return folha(idx, m1.start()), folha(idx, m2.start()), '\n'.join(blocos)


def gravar(cap):
    t, idx = carregar()
    f1, f2, corpo = cortar(t, idx, cap)
    conf = ''
    for f, p, vv, lat in CONFERIDOS.get(cap, []):
        conf += f'\n### {vv}: p. {p} ({PAG.format(f)})\n\n{lat}\n'
    campos = [
        ('Autor', 'Santo Efrém, o Sírio (c. 306–373), diácono de Nísibis e Edessa, Doutor da Igreja'),
        ('Obra', 'Comentário ao Gênesis (Explanatio in Genesim), siríaco do Vat. sir. 110 com a tradução latina de P. Benedetti'),
        ('Passagem', f'Gn {cap} (o comentário corrido de Efrém)'),
        ('Edição', f'J. S. Assemani e P. Benedetti, S. Ephraem Syri Opera omnia syriace et latine, t. I, Roma 1737, '
                   f'p. {f1 - 20}–{f2 - 20} (folhas n{f1}–n{f2} do archive.org). Edição crítica: R.-M. Tonneau, CSCO 152–153 '
                   f'(1955), com direito autoral'),
        ('Fonte', PAG.format(f1)),
        ('Cobre', f'o capítulo {cap} inteiro (latim); siríaco só na imagem'),
        ('Oriental', 'sim'),
        ('Língua', 'la (tradução latina de 1737; o original siríaco está ao lado, na mesma página, e não foi transcrito)'),
        ('Baixado', f'{HOJE}, por {SCRIPT}'),
    ]
    txt = '# Santo Efrém, Comentário ao Gênesis (Explanatio in Genesim)\n' + '\n'.join(f'- {k}: {v}' for k, v in campos)
    txt += ('\n\n> O latim de Benedetti é livre (às vezes parafraseia). Ao publicar, conferir o sentido no siríaco da '
            'mesma página (ou em Tonneau). Efrém lê a «ruḥa» de Gn 1,2 como **vento**, não como o Espírito Santo (p. 8).\n')
    if conf:
        txt += '\n## Trechos conferidos na imagem da página (ortografia normalizada: ſ → s, æ/œ → ae/oe)\n' + conf
    txt += '\n## Texto corrido (OCR do archive.org, só as linhas latinas, sem correção)\n' + corpo + '\n'
    pasta = os.path.join(RAIZ, 'genesis', f'{cap:03d}', 'base')
    os.makedirs(pasta, exist_ok=True)
    p = os.path.join(pasta, 'efrem-comentario-genesis.md')
    with open(p, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(txt)
    print('gravado', p, f'(folhas n{f1}–n{f2})')


def ver(a, b):
    t, idx = carregar()
    for f in range(a, b + 1):
        s, e = idx[f][0], idx[f][1]
        lat = [l.strip() for l in t[s:e].split('\n') if latino(l)]
        print(f'n{f} (p. {f - 20}?):', ' | '.join(lat[:3])[:200])


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '--ver':
        ver(int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) == 2 and sys.argv[1].isdigit():
        if int(sys.argv[1]) not in CORTES:
            sys.exit('capítulo sem âncoras em CORTES: rode --ver e acrescente as duas expressões')
        gravar(int(sys.argv[1]))
    else:
        print(__doc__)
