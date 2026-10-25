"""Ruperto de Deutz, De Trinitate et operibus eius: In Genesim, livros I–IX, cortado por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-latinos-ruperto.py 1        (ou 1-50)

Baixa uma vez o texto 10873 do Corpus Corporum (PL 167, a Bíblia inteira de Ruperto, 5,6 MB;
https://mlat.uzh.ch/browser/cps_2.RupTui.DeTrEtO) e grava genesis/<ccc>/base/ruperto-in-genesim.md. Usa só o
começo do texto até «IN EXODUM COMMENTARIORUM». Os capítulos de Ruperto têm título e citam o lema; o capítulo do
Gênesis sai do lema (gen-latinos-comum.py). Os livros: I = Gn 1,1–23; II = 1,24–2,25; III = 3; IV = 3,24–10;
V = 12–18; VI = 18–25; VII = 25–28; VIII = 32–40; IX = 42–49 (os capítulos que faltam ficam em _ausentes).
"""
import importlib.util, os
AQUI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('gen_latinos_comum', os.path.join(AQUI, 'gen-latinos-comum.py'))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

caps = C.capitulos_args(__doc__)
C.por_lema(10873, r'COMMENTARIORUM IN GENESIM', r'IN EXODUM COMMENTARIORUM', caps, {
    'arquivo': 'ruperto-in-genesim.md',
    'titulo': 'Ruperto de Deutz, De Trinitate et operibus eius: In Genesim',
    'autor': 'Ruperto de Deutz (c. 1075–1129)',
    'obra': 'De Trinitate et operibus eius, In Genesim (livros I–IX)',
    'pl': 167, 'fonte': C.url_cc(10873), 'script': 'gen-latinos-ruperto.py',
    'rotulo': 'Ruperto de Deutz, In Genesim',
    'cobre': 'o capítulo, com os títulos de capítulo de Ruperto',
})
