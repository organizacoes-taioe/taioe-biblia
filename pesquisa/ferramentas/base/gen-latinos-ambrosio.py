"""Santo Ambrósio: as obras sobre o Gênesis (Hexaemeron, De paradiso, De Cain et Abel, De Noe, De Abraham, De Isaac,
De Iacob, De Ioseph, De benedictionibus patriarcharum) e a carta 43 (o homem criado por último), por capítulo.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-ambrosio.py 1        (ou 1-50)

Baixa uma vez os textos do Corpus Corporum (PL 14–16) para pesquisa/cache/genesis/latinos/ e grava
genesis/<ccc>/base/ambrosio-<obra>.md. Gn 1: o Hexaemeron inteiro (os nove sermões em seis livros, PL 14,
123–274; ele acaba com o descanso de Gn 2,2) e a carta 43 a Horontiano (29 na numeração de Faller–Zelzer,
CSEL 82), sobre por que o homem foi criado por último. Obra que cobre um capítulo só (De Cain et Abel = Gn 4)
vai inteira; a que cobre vários capítulos é cortada pelos lemas (gen-latinos-comum.py), e o corte deve ser
conferido: Ambrósio cita o versículo no meio do sermão, não em lema. Rodado até agora só para Gn 1 (25/10/2026).
"""
import importlib.util, os
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
    (6949, 'ambrosio-de-isaac.md', 'De Isaac vel anima', 14, [24, 25, 26, 27]),
    (6950, 'ambrosio-de-iacob.md', 'De Iacob et vita beata', 14, list(range(27, 36))),
    (21359, 'ambrosio-de-ioseph.md', 'De Ioseph', 14, list(range(37, 51))),
    (6952, 'ambrosio-de-benedictionibus.md', 'De benedictionibus patriarcharum', 14, [49]),
]
caps = C.capitulos_args(__doc__)
for cap in caps:
    for idno, arq, obra, pl, gs in OBRAS:
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
