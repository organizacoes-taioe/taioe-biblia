"""Junta, em cada salmo, as linhas de ausentes e de pistas que os scripts grc-*.py guardaram.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-fechar.py     (rodar DEPOIS de todos os grc-*.py)
Lê cache/base/grc/ausentes/*.json e cache/base/grc/pistas/*.json e grava, para cada salmo hebraico (menos 33–36),
salmos/<ccc>/base/_ausentes-gregos.md e _pistas-gregos.md (apagando os que não têm linha). Em seguida roda
ferramentas/base-indice.py --todos.
"""
import glob, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

ORDEM = ['grc-teodoreto-sl.py', 'grc-atanasio-sl.py', 'grc-eusebio-sl.py', 'grc-basilio-sl.py', 'grc-crisostomo-sl.py',
         'grc-cirilo-sl.py', 'grc-origenes-selecta-sl.py', 'grc-origenes-fragmenta-sl.py', 'grc-nissa-sl.py',
         'grc-didimo-pistas.py', 'grc-ia-pistas.py']
TITULO = {'ausentes': '# Ausentes (Padres gregos)', 'pistas': '# Pistas (Padres gregos)'}

for tipo in ('ausentes', 'pistas'):
    dados = {}
    for s in ORDEM:
        p = os.path.join(_grc.CACHE, tipo, s + '.json')
        if os.path.exists(p):
            for h, linhas in json.load(open(p, encoding='utf-8')).items():
                dados.setdefault(int(h), []).extend(linhas)
    n = 0
    for h in _grc.conjunto_hebr():
        pasta = os.path.join(_grc.SALMOS, f'{h:03d}', 'base')
        arq = os.path.join(pasta, f'_{tipo}-gregos.md')
        if h in dados:
            os.makedirs(pasta, exist_ok=True)
            with open(arq, 'w', encoding='utf-8', newline='\n') as f:
                f.write(TITULO[tipo] + '\n\n' + '\n'.join(dados[h]) + '\n')
            n += 1
        elif os.path.exists(arq):
            os.remove(arq)
    print(f'{tipo}: {n} salmos com arquivo')
subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(_grc.RAIZ, 'ferramentas', 'base-indice.py'), '--todos'],
               check=True)
