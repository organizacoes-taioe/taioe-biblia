"""Hugo de São Vítor: Adnotationes in Pentateuchon (parte do Gênesis) e, para Gn 1–3, o De sacramentis, por capítulo.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-hugo.py 1        (ou 1-50)

Baixa uma vez os textos 11054 (Adnotationes elucidatoriae in Pentateuchon, PL 175, 29–86;
https://mlat.uzh.ch/browser/cps_2.HuDeSVi.AdInPe) e 11082 (De sacramentis christianae fidei, PL 176, 173–618;
https://mlat.uzh.ch/browser/cps_2.HuDeSVi.DeSac3) e grava genesis/<ccc>/base/hugo-adnotationes-in-pentateuchon.md
(o capítulo sai do lema, gen-latinos-comum.py) e, só para Gn 1–3, genesis/<ccc>/base/hugo-de-sacramentis.md:
Gn 1 = livro I, parte I (o Hexameron, caps. 1–30), parte II, cap. 1 (o homem, último no tempo e primeiro na causa)
e parte VI, caps. 1–2 (a imagem e a semelhança); Gn 2 = parte VI, caps. 3–15 (alma, paraíso, preceito);
Gn 3 = parte VII (a queda).
"""
import importlib.util, os
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

caps = C.capitulos_args(__doc__)
IDA = 11054
ba = C.bruto(IDA)
pa = C.L.limpar_pl(ba)
# cap. II–VI: proêmio e os seis dias (Gn 1); cap. VII: uma nota por capítulo do Gênesis, marcada «(GEN. N.)»
g_ini = C.achar(pa, r'^CAP\. II\.-- De nomine primi libri')
c7 = C.achar(pa, r'^CAP\. VII\.-- Adnotationes elucidatoriae', g_ini)
marcas = {}
for i in range(c7 + 1, len(pa)):
    m = C.re.search(r'\(GEN(?:ES)?\.\s*([IVXL]+)\.?\)', pa[i]['t'], C.re.I)
    if m:
        marcas.setdefault(C.L.de_romano(m.group(1).upper()), i)
    elif C.re.search(r'(?:De nomine Exodi|IN EXODUM|Exod(?:i|us)\b.*CAP\.)', pa[i]['t']) and pa[i]['tit']:
        marcas.setdefault('fim', i)
        break
fim_g = marcas.pop('fim', None) or C.achar(pa, r'De nomine Levitici', c7) or len(pa)
ordem = sorted(set(list(marcas.values()) + [fim_g]))
for cap in caps:
    if cap == 1:
        partes = [(g_ini, c7, 'Caps. II–VI: o nome do livro, a intenção de Moisés, a matéria, os seis dias'),
                  (c7, ordem[0], 'Cap. VII: notas sobre Gn 1')]
    elif cap in marcas:
        a = marcas[cap]
        partes = [(a, min(i for i in ordem if i > a), None)]
    else:
        C.registrar_ausente(cap, 'Hugo de São Vítor, Adnotationes in Pentateuchon', 'sem nota sobre este capítulo.')
        continue
    C.gravar_partes(cap, 'hugo-adnotationes-in-pentateuchon.md', {
        'titulo': 'Hugo de São Vítor, Adnotationes elucidatoriae in Pentateuchon',
        'autor': 'Hugo de São Vítor (c. 1096–1141)',
        'obra': 'Adnotationes elucidatoriae in Pentateuchon (Gênesis)',
        'passagem': f'Gn {cap}', 'pl': 175, 'fonte': C.url_cc(IDA), 'script': 'gen-latinos-hugo.py',
        'cobre': 'as notas literais sobre o capítulo',
    }, pa, partes, ba)

IDS = 11082
b = C.bruto(IDS)
pars = C.L.limpar_pl(b)
p1 = C.secao(pars, r'PARS PRIMA\. HEXAMERON', r'PARS SECUNDA')
p2 = C.secao(pars, r'PARS SECUNDA\. DE CAUSA CREATIONIS', r'^CAP\. II\. De causis primordialibus')
p6 = C.secao(pars, r'PARS SEXTA\. DE CREATIONE HOMINIS', r'PARS SEPTIMA')
p6a = (p6[0], C.achar(pars, r'^CAP\. III\. De creatione et origine animae', p6[0]))
p6b = (p6a[1], p6[1])
p7 = C.secao(pars, r'PARS SEPTIMA\. DE LAPSU', r'PARS OCTAVA')
PARTES = {1: [(p1[0], p1[1], 'Livro I, parte I: o Hexameron'),
              (p2[0], p2[1], 'Livro I, parte II, cap. 1: por que o homem foi criado por último'),
              (p6a[0], p6a[1], 'Livro I, parte VI, caps. 1–2: a imagem e a semelhança')],
          2: [(p6b[0], p6b[1], 'Livro I, parte VI, caps. 3 em diante: a alma, o paraíso, o preceito')],
          3: [(p7[0], p7[1], 'Livro I, parte VII: a queda')]}
for cap in caps:
    if cap not in PARTES:
        continue
    C.gravar_partes(cap, 'hugo-de-sacramentis.md', {
        'titulo': 'Hugo de São Vítor, De sacramentis christianae fidei',
        'autor': 'Hugo de São Vítor (c. 1096–1141)',
        'obra': 'De sacramentis christianae fidei, livro I',
        'passagem': f'Gn {cap}: ' + '; '.join(s for _, _, s in PARTES[cap]),
        'pl': 176, 'fonte': C.url_cc(IDS), 'script': 'gen-latinos-hugo.py',
        'cobre': 'as partes da obra sobre o capítulo (não é comentário versículo a versículo)',
    }, pars, PARTES[cap], b)
