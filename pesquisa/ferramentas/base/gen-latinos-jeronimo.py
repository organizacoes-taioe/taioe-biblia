"""São Jerônimo, Quaestiones hebraicae in Genesim, por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-jeronimo.py 1        (ou 1-50)

Baixa uma vez o texto 7160 do Corpus Corporum (PL 23, 935–1010; https://mlat.uzh.ch/browser/cps_2.HieStr.QuHeInG)
e grava genesis/<ccc>/base/jeronimo-quaestiones-hebraicae.md. Migne marca o começo de cada capítulo com o título
«(CAP. N)» ou, do cap. XXII em diante, com «(Cap. N.--Vers. v.)» no começo do parágrafo; Jerônimo só comenta os versículos em que o hebraico difere do grego ou do latim (em Gn 1, os vv. 1, 2 e
10). A edição crítica (de Lagarde, CCSL 72, 1959) tem direitos: não guardar.
"""
import importlib.util, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

caps = C.capitulos_args(__doc__)
IDNO = 7160
b = C.bruto(IDNO)
pars = C.L.limpar_pl(b)
ini = {}
for i, p in enumerate(pars):
    # «(CAP. III)» (título) nos primeiros capítulos; depois só «(Cap. XXIV.--Vers. 2.)» no começo do parágrafo
    m = re.match(r'^(?:\[col\. \w+\] )?(?:\d+ )?\((?:CAP|Cap)\. ([IVXL]+)[.)]', p['t'])
    if m:
        ini.setdefault(C.L.de_romano(m.group(1)), i)
ordem = sorted(ini.items(), key=lambda x: x[1])
for cap in caps:
    if cap not in ini:
        C.registrar_ausente(cap, 'São Jerônimo, Quaestiones hebraicae in Genesim', 'não tem questão sobre este capítulo.')
        print(f'  Gn {cap}: nada')
        continue
    a = ini[cap]
    z = min([i for c, i in ordem if i > a] or [len(pars)])
    C.gravar_partes(cap, 'jeronimo-quaestiones-hebraicae.md', {
        'titulo': 'São Jerônimo, Quaestiones hebraicae in Genesim',
        'autor': 'São Jerônimo (c. 347–420)',
        'obra': 'Liber Hebraicarum quaestionum in Genesim',
        'passagem': f'Gn {cap}',
        'pl': 23, 'fonte': C.url_cc(IDNO), 'script': 'gen-latinos-jeronimo.py',
        'cobre': 'só os versículos em que Jerônimo discute o hebraico',
    }, pars, [(a, z, None)], b)
