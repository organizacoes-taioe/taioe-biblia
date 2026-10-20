"""Roda, em ordem, todos os grc-*.py (Padres gregos nos Salmos) e fecha com grc-fechar.py.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-tudo.py
Os PDFs (khazarzar) e o OCR (archive.org) são baixados UMA vez para pesquisa/cache/base/grc/ (fora do git), com 1 s de
pausa entre pedidos; uma segunda rodada não baixa nada. Antes de gravar, apaga os arquivos que estes scripts criam
(só os deles: teodoreto-, atanasio-, eusebio-, basilio-, pseudo-basilio-, crisostomo-, pseudo-crisostomo-, cirilo-,
origenes-selecta-, origenes-fragmenta-, gregorio-nissa-) para não sobrar salmo antigo.
"""
import glob, os, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
SALMOS = os.path.normpath(os.path.join(AQUI, '..', '..', 'salmos'))
PADROES = ['teodoreto-interpretatio-in-psalmos', 'atanasio-expositiones-in-psalmos', 'eusebio-commentaria-in-psalmos',
           'basilio-homiliae-super-psalmos', 'pseudo-basilio-homilia-in-psalmum-*', 'crisostomo-*', 'pseudo-crisostomo-*',
           'cirilo-expositio-in-psalmos', 'origenes-selecta-in-psalmos', 'origenes-fragmenta-in-psalmos',
           'gregorio-nissa-in-inscriptiones-psalmorum']
for p in PADROES:
    for f in glob.glob(os.path.join(SALMOS, '*', 'base', p + '.md')):
        os.remove(f)
SCRIPTS = ['grc-teodoreto-sl.py', 'grc-atanasio-sl.py', 'grc-eusebio-sl.py', 'grc-basilio-sl.py', 'grc-crisostomo-sl.py',
           'grc-cirilo-sl.py', 'grc-origenes-selecta-sl.py', 'grc-origenes-fragmenta-sl.py', 'grc-nissa-sl.py',
           'grc-didimo-pistas.py', 'grc-ia-pistas.py', 'grc-fechar.py']
for s in SCRIPTS:
    print('=====', s, flush=True)
    subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(AQUI, s)], check=True)
