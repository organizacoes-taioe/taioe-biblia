"""Latinos: os trechos que comentam um capítulo do Gênesis dentro de obras que não comentam o livro (sermões,
tratados, cartas, a Suma), um arquivo base/ por obra. A tabela TRECHOS diz, para cada capítulo, onde estão.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-avulsos.py 1

Por enquanto só Gn 1 (25/10/2026, achados na pesquisa do capítulo). Para outro capítulo, acrescentar à tabela as
passagens achadas (regex do primeiro parágrafo e do primeiro parágrafo que já não entra). Fontes: Corpus Corporum
(PL; baixa uma vez para pesquisa/cache/genesis/latinos/), Corpus Thomisticum (Suma) e Wikisource (Santa Catarina).
"""
import html, importlib.util, json, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

S = 'gen-latinos-avulsos.py'
# cap: [(idno, arquivo, meta, [(ini_rx, fim_rx, depois_rx, subtítulo)])]
TRECHOS = {1: [
    (7631, 'leao-sermoes.md', {
        'titulo': 'São Leão Magno, Sermões 12 e 27', 'autor': 'São Leão Magno (c. 400–461)',
        'obra': 'Tractatus (Sermones) 12 (do jejum do décimo mês, 1) e 27 (do Natal, 7)', 'pl': 54,
        'passagem': 'Sermão 12, 1 (Gn 1,26: o homem feito para imitar o seu Autor); Sermão 27, 4–6 (Gn 1,14–16: o '
                    'sol e a lua, criaturas; o culto do sol nos degraus de São Pedro; Gn 1,26)',
        'cobre': 'só os parágrafos sobre Gn 1'},
     [(r'^Si fideliter, dilectissimi, atque sapienter creationis', r'^CAP\. II\.$', None, 'Sermão 12, 1'),
      (r'^CAP\. IV\.$', r'^SERMO XXVIII', r'SERMO XXVII \[', 'Sermão 27, 4–6')]),
    (21427, 'gregorio-moralia.md', {
        'titulo': 'São Gregório Magno, Moralia in Iob IX, 49', 'autor': 'São Gregório Magno (c. 540–604)',
        'obra': 'Moralia in Iob, livro IX, cap. 49, § 75 (sobre Jó 10,8)', 'pl': 75,
        'passagem': 'Gn 1,26: «Façamos»; o homem feito como por deliberação', 'cobre': 'o parágrafo'},
     [(r'Hominis praerogativa in rerum conditione', r'^CAPUT L \[', None, None)]),
    (6871, 'hilario-de-trinitate.md', {
        'titulo': 'Santo Hilário, De Trinitate IV e V', 'autor': 'Santo Hilário de Poitiers (c. 315–367)',
        'obra': 'De Trinitate, IV, 16–21 e V, 4–9', 'pl': 10,
        'passagem': 'Gn 1,6–7 («disse Deus… e fez Deus»: o Pai e o Filho) e 1,26–27 («Façamos… à nossa imagem»)',
        'cobre': 'os parágrafos sobre Gn 1'},
     [(r'^In historia creationis Deum non solitarium', r'^22\.$', None, 'Livro IV, 16–21'),
      (r'^Filius ex creandi virtute probatur', r'^10\.$', None, 'Livro V, 4–9')]),
    (44, 'tertuliano-de-baptismo.md', {
        'titulo': 'Tertuliano, De baptismo 1–4', 'autor': 'Tertuliano (c. 155–c. 230), escritor eclesiástico',
        'obra': 'De baptismo, caps. 1–4', 'pl': 1,
        'passagem': 'Gn 1,2 (o Espírito sobre as águas) e 1,20 (as águas produzem os primeiros viventes)',
        'cobre': 'caps. 1–4',
        'nota': 'Texto da PL; a edição crítica de Borleffs (CCSL 1, 1954) tem direitos. O PL lê «in qua nascimur» '
                '(1, 3), por «in aqua nascimur».'},
     [(r'^\[col\. 1197A\] Felix sacramentum aquae', r'^CAPUT V\.$', None, None)]),
    (61, 'tertuliano-adversus-hermogenem.md', {
        'titulo': 'Tertuliano, Adversus Hermogenem 19–34', 'autor': 'Tertuliano (c. 155–c. 230), escritor eclesiástico',
        'obra': 'Adversus Hermogenem, caps. 19–34', 'pl': 2,
        'passagem': 'Gn 1,1–2: contra a matéria eterna de Hermógenes («no princípio», «a terra era…»)',
        'cobre': 'caps. 19–34'},
     [(r'^CAPUT XIX\.$', r'^CAPUT XXXV\.$', None, None)]),
    (6894, 'zenao-tractatus.md', {
        'titulo': 'São Zenão de Verona, Tratados II, 1–4 (De Genesi)', 'autor': 'São Zenão de Verona (†c. 372)',
        'obra': 'Tractatus, livro II, 1–4 (De Genesi)', 'pl': 11,
        'passagem': 'Gn 1,1 (o princípio, contra o caos eterno) e 1,26 («Façamos»)', 'cobre': 'os quatro tratados'},
     [(r'^TRACTATUS PRIMUS\. De Genesi', r'TRACTATUS V\. De Fide', None, None)]),
    (7132, 'jeronimo-epistola-69.md', {
        'titulo': 'São Jerônimo, Carta 69, a Oceano, 6', 'autor': 'São Jerônimo (c. 347–420)',
        'obra': 'Epistulae, 69 (a Oceano), 6', 'pl': 22,
        'passagem': 'Gn 1,2.6–7.20: as águas da criação e o batismo', 'cobre': 'o parágrafo 6'},
     [(r'^Reddamus quod paulo ante promisimus', r'^7\.$', None, None)]),
    (6971, 'ambrosio-de-mysteriis.md', {
        'titulo': 'Santo Ambrósio, De mysteriis 3, 9', 'autor': 'Santo Ambrósio (c. 339–397)',
        'obra': 'De mysteriis, 3, 9', 'pl': 16,
        'passagem': 'Gn 1,2: o Espírito sobre as águas, figura do batismo', 'cobre': 'o parágrafo'},
     [(r'^Considera autem quam vetus mysterium', r'^Accipe aliud testimonium', None, None)]),
    (6813, 'lactancio-divinae-institutiones.md', {
        'titulo': 'Lactâncio, Divinae institutiones VII, 4–6', 'autor': 'Lactâncio (c. 250–c. 325), escritor eclesiástico',
        'obra': 'Divinae institutiones, livro VII, caps. 4–6', 'pl': 6,
        'passagem': 'Gn 1,26–31: o mundo feito para o homem, o homem para Deus', 'cobre': 'caps. 4–6'},
     [(r'^CAPUT IV\. Quod omnia in aliquem usum', r'^CAPUT VII\.', None, None)]),
    (11198, 'bernardo-de-gratia-et-libero-arbitrio.md', {
        'titulo': 'São Bernardo, De gratia et libero arbitrio 9', 'autor': 'São Bernardo de Claraval (1090–1153)',
        'obra': 'De gratia et libero arbitrio, cap. 9 (28–31)', 'pl': 182,
        'passagem': 'Gn 1,26: a imagem (o livre-arbítrio) e a semelhança', 'cobre': 'o capítulo 9'},
     [(r'^CAPUT IX\. Imaginem et similitudinem', r'^CAPUT X\. ', None, None)]),
    (11258, 'bernardo-in-cantica.md', {
        'titulo': 'São Bernardo, Sermões sobre o Cântico 80–82', 'autor': 'São Bernardo de Claraval (1090–1153)',
        'obra': 'Sermones super Cantica canticorum, 80–82', 'pl': 183,
        'passagem': 'Gn 1,26: a alma feita à imagem do Verbo; a semelhança coberta, não apagada, pelo pecado',
        'cobre': 'os três sermões'},
     [(r'^SERMO LXXX\. ', r'^SERMO LXXXIII\. ', None, None)]),
]}


def hildegarda(cap):
    if cap != 1:
        return
    b = C.bruto(11562)
    pars = C.L.limpar_pl(b)
    a = C.achar(pars, r'^Quia Deus mundum constituens et se ipsum glorificaverit')
    z = C.achar(pars, r'Igitur perfecti sunt coeli', a)
    while z > a and (pars[z - 1]['tit'] or len(pars[z - 1]['t']) < 400):   # título e sumário do cap. de Gn 2
        z -= 1
    C.gravar_partes(1, 'hildegarda-liber-divinorum-operum.md', {
        'titulo': 'Santa Hildegarda, Liber divinorum operum II, 1 (a quinta visão), 17–47',
        'autor': 'Santa Hildegarda de Bingen (1098–1179), Doutora da Igreja',
        'obra': 'Liber divinorum operum, parte II, visão 1 (a quinta da obra), caps. 17–47',
        'passagem': 'Gn 1,1–31 lido três vezes: ao pé da letra, da Igreja e da alma', 'pl': 197,
        'fonte': C.url_cc(11562), 'script': S, 'cobre': 'o comentário de Gn 1',
        'nota': 'Texto da PL; a edição crítica (Derolez–Dronke, CCCM 92, 1996) tem direitos.'},
        pars, [(a, z, None)], b)


def tomas(cap):
    if cap != 1:
        return
    blocos = []
    for pagina, prefixos in (('sth1065', [f'I q. {q} ' for q in range(65, 75)]), ('sth1090', ['I q. 93 '])):
        url = f'https://www.corpusthomisticum.org/{pagina}.html'
        t = open(C.baixar(url, os.path.join(C.CACHE, pagina + '.html')), encoding='latin-1').read()
        for m in re.finditer(r'<P TITLE="([^"]*)"[^>]*>(.*?)(?=<P |</BODY)', t, re.S | re.I):
            tit = m.group(1)
            if any((tit + ' ').startswith(p) for p in prefixos):
                s = html.unescape(re.sub(r'<[^>]+>', '', m.group(2)))
                blocos.append(re.sub(r'\s+', ' ', s).strip())
    C.gravar_base(1, 'tomas-summa-theologiae.md', 'São Tomás de Aquino, Summa theologiae I, q. 65–74 e 93',
                  'São Tomás de Aquino (1225–1274), Doutor da Igreja', 'Summa theologiae, I, q. 65–74 (a obra dos seis '
                  'dias) e q. 93 (o fim da produção do homem: a imagem e a semelhança)',
                  'Gn 1 inteiro (q. 65–74) e Gn 1,26–27 (q. 93)', 'ed. Leonina, t. 5 (1889); texto do Corpus Thomisticum',
                  'https://www.corpusthomisticum.org/sth1065.html e https://www.corpusthomisticum.org/sth1090.html',
                  'as questões inteiras', '\n\n'.join(blocos), S)


def catarina(cap):
    if cap != 1:
        return
    pag = 'Libro_della_divina_dottrina_(Caterina_da_Siena_-_Fiorilli)/Tractato_de_la_discrezione/Capitolo_XIII'
    api = f'https://it.wikisource.org/w/api.php?action=parse&page={pag}&prop=text&format=json'
    d = json.load(open(C.baixar(api, os.path.join(C.CACHE, 'catarina-dialogo-13.json')), encoding='utf-8'))
    t = d['parse']['text']['*']
    t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    t = re.sub(r'<span[^>]*class="numeropagina[^"]*"[^>]*>.*?</span>', '', t, flags=re.S)
    pars = [html.unescape(re.sub(r'<[^>]+>', '', p)).strip() for p in re.findall(r'<p>(.*?)</p>', t, re.S)]
    pars = [re.sub(r'\[p\. \d+ modifica\]', '', p).strip() for p in pars]
    i = next(k for k, p in enumerate(pars) if p.startswith('Alora l'))
    corpo = '\n\n'.join(p for p in pars[i:] if p)
    C.gravar_base(1, 'catarina-dialogo.md', 'Santa Catarina de Sena, Diálogo (Libro della divina dottrina), cap. 13',
                  'Santa Catarina de Sena (1347–1380), Doutora da Igreja', 'Il Dialogo della divina provvidenza '
                  '(Libro della divina dottrina), cap. 13', 'Gn 1,26 citado: «Facciamo l’uomo a la imagine e '
                  'similitudine nostra»; a Trindade e o amor que criou o homem', 'ed. M. Fiorilli, Bari, Laterza, '
                  '1912, pp. 30–33', 'https://it.wikisource.org/wiki/' + pag, 'o capítulo inteiro', corpo, S, lingua='it')


caps = C.capitulos_args(__doc__)
for cap in caps:
    for idno, arq, meta, partes in TRECHOS.get(cap, []):
        b = C.bruto(idno)
        pars = C.L.limpar_pl(b)
        sel = []
        for ini_rx, fim_rx, depois_rx, sub in partes:
            dep = C.achar(pars, depois_rx) if depois_rx else -1
            a, z = C.secao(pars, ini_rx, fim_rx, dep)
            sel.append((a, z, sub))
        C.gravar_partes(cap, arq, dict(meta, fonte=C.url_cc(idno), script=S), pars, sel, b)
    hildegarda(cap)
    tomas(cap)
    catarina(cap)
