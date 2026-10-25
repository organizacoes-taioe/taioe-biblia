"""Santo Ambrósio: as obras sobre o Gênesis (Hexaemeron, De paradiso, De Cain et Abel, De Noe, De Abraham, De Isaac,
De Iacob, De Ioseph, De benedictionibus patriarcharum) e a carta 43 (o homem criado por último), por capítulo.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-ambrosio.py 1        (ou 1-50)

Baixa uma vez os textos do Corpus Corporum (PL 14–16) para pesquisa/cache/genesis/latinos/ e grava
genesis/<ccc>/base/ambrosio-<obra>.md. Gn 1: o Hexaemeron inteiro (os nove sermões em seis livros, PL 14,
123–274; ele acaba com o descanso de Gn 2,2) e a carta 43 a Horontiano (29 na numeração de Faller–Zelzer,
CSEL 82), sobre por que o homem foi criado por último. Obra que cobre um capítulo só (De Cain et Abel = Gn 4)
vai inteira; a que cobre vários capítulos é cortada pelos lemas (gen-latinos-comum.py), e o corte deve ser
conferido: Ambrósio cita o versículo no meio do sermão, não em lema. Rodado até agora só para Gn 1 (25/10/2026).
Desde 25/10, De Abraham, De Isaac, De Iacob e De Ioseph NÃO se cortam pelos lemas (o corte achava só 1 versículo de Gn 13 e
nada de Gn 18–25 no De Abraham, que trata Mamre, Sodoma e o sacrifício de Isaac): cada «CAPUT» da obra vai para os capítulos
do Gênesis da tabela POR_CAPUT (lidos no argumento de Migne e nas notas «(Gen. XXII, 1)» de cada capítulo; conferir), e o
capítulo do Gênesis que nenhum «CAPUT» trata vai para _ausentes-latinos.md.
"""
import importlib.util, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

AUTOR = 'Santo Ambrósio (c. 339–397)'
# idno, arquivo, título da obra, PL, capítulos do Gênesis
OBRAS = [
    (6958, 'ambrosio-hexaemeron.md', 'Hexaemeron (livros I–VI, os nove sermões)', 14, [1]),
    (21375, 'ambrosio-de-paradiso.md', 'De paradiso', 14, [2, 3]),
    (6948, 'ambrosio-de-cain-et-abel.md', 'De Cain et Abel', 14, [4]),
    (21361, 'ambrosio-de-noe.md', 'De Noe', 14, [6, 7, 8, 9]),
    (6947, 'ambrosio-de-abraham.md', 'De Abraham', 14, list(range(12, 26))),
    (6949, 'ambrosio-de-isaac.md', 'De Isaac vel anima', 14, list(range(21, 28))),
    (6950, 'ambrosio-de-iacob.md', 'De Iacob et vita beata', 14, list(range(25, 50))),
    (21359, 'ambrosio-de-ioseph.md', 'De Ioseph', 14, list(range(37, 51))),
    (6952, 'ambrosio-de-benedictionibus.md', 'De benedictionibus patriarcharum', 14, [49]),
]
# idno -> {n.º de ordem do «CAPUT» na obra (1 = o primeiro título CAPUT do texto): (rótulo, capítulos do Gênesis)}
POR_CAPUT = {
    6947: {1: ('I, 1', []), 2: ('I, 2', [12]), 3: ('I, 3', [13, 14, 15]), 4: ('I, 4', [16, 17]), 5: ('I, 5', [18]),
           6: ('I, 6', [18, 19]), 7: ('I, 7', [20, 21]), 8: ('I, 8', [22]), 9: ('I, 9', [23, 24]), 10: ('II, 1', [12]),
           11: ('II, 2', [12]), 12: ('II, 3', [12]), 13: ('II, 4', [12]), 14: ('II, 5', [13]), 15: ('II, 6', [13]),
           16: ('II, 7', [13, 14]), 17: ('II, 8', [14, 15]), 18: ('II, 9', [15]), 19: ('II, 10', [15, 17]), 20: ('II, 11', [17])},
    6949: {1: ('1', [21, 22, 24]), 3: ('3', [24]), 4: ('4', [25, 26]), 5: ('5', [25, 27]), 6: ('6', [24]), 7: ('7', [27])},
    6950: {8: ('II, 1', [27, 28]), 9: ('II, 2', [25, 27]), 10: ('II, 3', [27]), 11: ('II, 4', [27, 28, 29]), 12: ('II, 5', [31]),
           13: ('II, 6', [32, 33]), 14: ('II, 7', [32, 34, 35]), 15: ('II, 8', [42, 43, 45, 46, 47]), 16: ('II, 9', [48, 49])},
    21359: {1: ('1', [37]), 2: ('2', [37]), 3: ('3', [37]), 4: ('4', [37, 39]), 5: ('5', [39]), 6: ('6', [39, 40]),
            7: ('7', [41]), 8: ('8', [42]), 9: ('9', [43]), 10: ('10', [43]), 11: ('11', [44]), 12: ('12', [45]),
            13: ('13', [45]), 14: ('14', [46])},
}


def tirar_ausente(cap, rotulo):
    """Tira de _ausentes-latinos.md a linha antiga deste rótulo (o corte por lemas a punha por engano)."""
    p = os.path.join(C.pasta_base(cap), '_ausentes-latinos.md')
    if not os.path.exists(p):
        return
    txt = open(p, encoding='utf-8').read()
    novo = '\n'.join(l for l in txt.split('\n') if not l.startswith(f'- {rotulo}:'))
    if not re.search(r'^- ', novo, flags=re.M):
        os.remove(p)
    elif novo != txt:
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(novo)


def por_caput(cap, idno, arq, obra, pl, gs):
    b = C.bruto(idno)
    pars = C.L.limpar_pl(b)
    hs = [i for i, p in enumerate(pars) if re.match(r'^CAPUT (PRIMUM|[IVXL]+)\.$', p['t'])]
    rotulo = f'Santo Ambrósio, {obra}'
    partes = []
    for k, (rot, cs) in sorted(POR_CAPUT[idno].items()):
        if cap in cs:
            ini = hs[k - 1]
            fim = hs[k] if k < len(hs) else len(pars)
            partes.append((ini, fim, f'Cap. {rot}'))
    if not partes:
        tirar_ausente(cap, rotulo)
        C.registrar_ausente(cap, rotulo, f'não comenta este capítulo (nenhum dos capítulos da obra; obra sobre Gn {gs[0]}–{gs[-1]}).')
        print(f'  Gn {cap}: {obra}: nada')
        return
    tirar_ausente(cap, rotulo)
    meta = {'titulo': rotulo, 'autor': AUTOR, 'obra': obra, 'pl': pl, 'fonte': C.url_cc(idno), 'script': 'gen-latinos-ambrosio.py',
            'passagem': f'Gn {cap}: ' + '; '.join(sub.replace('Cap.', 'cap.') for a, z, sub in partes),
            'cobre': 'os capítulos da obra que tratam este capítulo do Gênesis (tabela POR_CAPUT; conferir), inteiros, com o '
                     'argumento de Migne no começo'}
    C.gravar_partes(cap, arq, meta, pars, partes, b)


caps = C.capitulos_args(__doc__)
for cap in caps:
    for idno, arq, obra, pl, gs in OBRAS:
        if idno in POR_CAPUT:
            if cap >= 3 and gs[0] <= cap <= gs[-1]:
                por_caput(cap, idno, arq, obra, pl, gs)
            continue
        if cap not in gs:
            continue
        b = C.bruto(idno)
        pars = C.L.limpar_pl(b)
        meta = {'titulo': f'Santo Ambrósio, {obra}', 'autor': AUTOR, 'obra': obra, 'pl': pl,
                'fonte': C.url_cc(idno), 'script': 'gen-latinos-ambrosio.py'}
        if len(gs) == 1:
            meta.update(passagem=f'Gn {cap}' + (' (e 2,1–2, o descanso, no fim do livro VI)' if cap == 1 else ''),
                        cobre='a obra inteira')
            C.gravar_partes(cap, arq, meta, pars, [(0, len(pars), None)], b)
        else:
            C.por_lema(idno, None, None, [cap], dict(meta, arquivo=arq, rotulo=f'Santo Ambrósio, {obra}',
                       cobre='os parágrafos que citam o capítulo (corte pelos lemas, conferir)'), cap0=gs[0])
    if cap == 1:   # carta 43 a Horontiano: por que o homem foi criado por último
        b = C.bruto(21400)
        pars = C.L.limpar_pl(b)
        a, z = C.secao(pars, r'^EPISTOLA XLIII\.', r'^EPISTOLA XLIV\.')
        C.gravar_partes(1, 'ambrosio-epistola-43.md', {
            'titulo': 'Santo Ambrósio, Carta 43, a Horontiano', 'autor': AUTOR,
            'obra': 'Epistulae, classis I, 43 (29 em Faller–Zelzer, CSEL 82/1)',
            'passagem': 'Gn 1,26–31: por que o homem foi criado depois de todas as coisas',
            'pl': 16, 'fonte': C.url_cc(21400), 'script': 'gen-latinos-ambrosio.py', 'cobre': 'a carta inteira'},
            pars, [(a, z, None)], b)
