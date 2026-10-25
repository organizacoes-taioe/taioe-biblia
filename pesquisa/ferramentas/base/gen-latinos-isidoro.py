"""Santo Isidoro, Quaestiones in Vetus Testamentum: In Genesin (31 capítulos por assunto), por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-isidoro.py 1        (ou 1-50)

Baixa uma vez o texto 21433 do Corpus Corporum (PL 83, 207–288; https://mlat.uzh.ch/browser/cps_2.IsiHis.QuInVeT)
e grava genesis/<ccc>/base/isidoro-quaestiones-in-genesin.md. Isidoro não vai versículo a versículo: os capítulos
dele são episódios, quase só alegoria tirada de Agostinho, Orígenes, Ambrósio e Gregório. A tabela MAPA diz que
capítulos de Isidoro tratam de que capítulo do Gênesis (pelos títulos).
"""
import importlib.util, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

MAPA = {1: [1, 2, 3], 2: [1, 2], 3: [2], 4: [3], 5: [3], 6: [4, 5], 7: [6, 7, 8], 8: [9], 9: [10, 11],
        10: [12], 11: [14], 12: [15], 13: [16, 17], 14: [18], 15: [19], 16: [20], 17: [21], 18: [22],
        19: [24], 20: [25], 21: [26], 22: [26], 23: [25, 27], 24: [28], 25: [29, 30], 26: [31], 27: [32],
        28: [34, 35], 29: [38], 30: [37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50], 31: [49]}
caps = C.capitulos_args(__doc__)
IDNO = 21433
b = C.bruto(IDNO)
pars = C.L.limpar_pl(b)
a0, z0 = C.secao(pars, r'^IN GENESIN', r'^IN EXODUM')
ini = {}
for i in range(a0, z0):
    m = re.match(r'^CAPUT ([IVXL]+)\.', pars[i]['t'])
    if m:
        ini.setdefault(C.L.de_romano(m.group(1)), i)
ordem = sorted(ini.values())
for cap in caps:
    sel = [n for n, gs in MAPA.items() if cap in gs and n in ini]
    if not sel:
        C.registrar_ausente(cap, 'Santo Isidoro, Quaestiones in Genesin', 'nenhum capítulo sobre este capítulo do Gênesis.')
        print(f'  Gn {cap}: nada')
        continue
    partes = []
    for n in sel:
        a = ini[n]
        z = min([i for i in ordem if i > a] or [z0])
        partes.append((a, z, None))
    C.gravar_partes(cap, 'isidoro-quaestiones-in-genesin.md', {
        'titulo': 'Santo Isidoro, Quaestiones in Vetus Testamentum: In Genesin',
        'autor': 'Santo Isidoro de Sevilha (c. 560–636)',
        'obra': 'Mysticorum expositiones sacramentorum seu Quaestiones in Vetus Testamentum, In Genesin',
        'passagem': f'Gn {cap}: cap. ' + ', '.join(C.romano(n) for n in sel) + ' de Isidoro',
        'pl': 83, 'fonte': C.url_cc(IDNO), 'script': 'gen-latinos-isidoro.py',
        'cobre': 'os capítulos de Isidoro sobre este trecho (alegoria)',
    }, pars, partes, b)
