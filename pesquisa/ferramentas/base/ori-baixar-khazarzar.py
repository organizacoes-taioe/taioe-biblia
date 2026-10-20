"""Baixa do khazarzar (texto digital da PG) as obras do grupo «orientais gregos não clássicos» que ainda não
estão convertidas e as converte em texto com ferramentas/gregos-limpar.py.

Uso (da pasta biblia/):
    python -I -X utf8 pesquisa/ferramentas/base/ori-baixar-khazarzar.py

Grava em pesquisa/cache/base/ori/grc/pdf/ e .../txt/<Autor>__<Obra>.txt (fora do git).
Macário, Máximo (PG 91, «ΑΠΑΝΤΑ»), Paládio e as cartas de Teodoro Estudita já estão convertidos em outras
pastas temporárias (ver fontes/gregos.md); aqui só o que faltava.
"""
import os, subprocess, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_gregos_comum as O

OBRAS = [
    ('Theodorus Studita_PG 99', ['Homilia in nativitatem Mariae.pdf', 'Iambi de variis argumentis.pdf']),
    ('Symeonis Junioris_PG 120', ['Catechesae.pdf', 'Catecheses et Gratiae.pdf', 'Epistulae.pdf', 'Theologica.pdf']),
    ('Gregorius Palamas_PG 150-151', ['tomos 1..pdf', 'tomos 2..pdf']),
    ('Gregorius Palamas Thessalonicensis Metropolita_PG 150-151', ['tomos 1.pdf', 'tomos 2.pdf']),
]
LIMPAR = os.path.join(O.RAIZ, 'ferramentas', 'gregos-limpar.py')


def main():
    txt = os.path.join(O.CACHE, 'txt')
    os.makedirs(txt, exist_ok=True)
    for pasta, arqs in OBRAS:
        if arqs is None:
            continue
        aut = pasta.split('_')[0].split()[0][:6]
        for a in arqs:
            url = O.KHZ + urllib.parse.quote(pasta) + '/' + urllib.parse.quote(a)
            nome = f'{aut}__{pasta.split("_")[0][-6:].strip()}_{a}'.replace(' ', '_')
            try:
                pdf = O.baixar(url, 'pdf/' + nome)
            except Exception as e:
                print('FALHOU', url, e)
                continue
            out = os.path.join(txt, nome[:-4] + '.txt')
            if not os.path.exists(out):
                subprocess.run([sys.executable, '-I', '-X', 'utf8', LIMPAR, pdf, out], stdout=subprocess.DEVNULL)
            print('ok', out)


if __name__ == '__main__':
    main()
