"""Roda, em ordem, todos os scripts de pré-pesquisa de Números (pesquisa/ferramentas/base/*-num.py) e depois monta os índices BASE.md.

    python -I -X utf8 pesquisa/ferramentas/base/num-tudo.py

Cada script baixa a obra UMA vez para pesquisa/cache/base/numeros/ (fora do git) e grava numeros/<ccc>/base/<autor>-<obra>.md; refazer é rápido
(só lê o cache). A ordem não importa, exceto que pistas-ausentes-num.py (os arquivos _ausentes-numeros.md e _pistas-numeros.md) vem por último,
porque confere quais arquivos existem. Mapa das obras: pesquisa/fontes/numeros.md.
"""
import os, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))  # raiz do repositório (onde se roda o base-indice.py)
SCRIPTS = ['lat-rabano-num', 'lat-isidoro-num', 'lat-pseudobeda-num', 'lat-ruperto-num', 'lat-bruno-num', 'lat-hugo-num', 'lat-paterio-num',
           'lat-agostinho-num', 'lat-origenes-num', 'lat-lapide-num', 'grc-teodoreto-num', 'grc-cirilo-num', 'grc-procopio-num',
           'grc-nissa-num', 'grc-origenes-num', 'sir-efrem-num', 'pistas-ausentes-num']
for s in SCRIPTS:
    print('==', s, flush=True)
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(AQUI, s + '.py')], cwd=RAIZ)
    if r.returncode:
        raise SystemExit(f'{s} falhou ({r.returncode})')
print('== base-indice --todos', flush=True)
subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(AQUI, '..', 'base-indice.py'), '--todos'], cwd=RAIZ, check=True)
