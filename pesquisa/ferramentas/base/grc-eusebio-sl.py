"""Eusébio de Cesareia, Commentaria in Psalmos (PG 23, 66–1396: Sl 1–118; PG 24, 9–76: Sl 119–150).

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-eusebio-sl.py
Dois PDFs do khazarzar (cache/base/grc/): «Commentaria in Psalmos.pdf» (Sl 1–118, LXX) e «…_1.pdf» (Sl 119–150).
Os cabeçalhos são irregulares (título em maiúsculas + número, às vezes sem número), então o começo de cada salmo
é achado pelo primeiro versículo citado (régua: o Saltério da LXX, _grc.sequencial) e recuado até o cabeçalho em
maiúsculas; no PDF dos Sl 119–150 valem os cabeçalhos «ΨΑΛΜΟΣ ΡΙΘʹ». Numeração da LXX.
Só os Sl 51–95 (LXX) são comentário contínuo de Eusébio; o resto vem de cadeias (fragmentos dele misturados aos de
Orígenes, Dídimo, Apolinário, Teodoro de Mopsuéstia…): isso vai no campo «Cobre». O texto dos Sl 119–150 acaba no
meio do Sl 150,2.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-eusebio-sl.py'
PASTA = 'Eusebius Caesariensis_PG 19-24'
URL_A = _grc.khz(PASTA, 'Commentaria in Psalmos.pdf')
URL_B = _grc.khz(PASTA, 'Commentaria in Psalmos_1.pdf')
A = _grc.texto(URL_A, 'eusebio-ps')
B = _grc.texto(URL_B, 'eusebio-ps1')
SEP = '\n\n'
T = A + SEP + B
OFF = len(A) + len(SEP)

# Sl 1–118: pelo primeiro versículo citado
stA, naoA = _grc.sequencial(A, 118)
iniA = _grc.refinar(A, stA)
# Sl 119–150: cabeçalhos «ΨΑΛΜΟΣ ΡΙΘʹ»
c = [(m.start(), _grc.num_grego(m.group(1)), m.group(1)) for m in re.finditer(r'ΨΑΛΜΟΣ\s+([Α-ΩϚ]{1,5}\s?ʹ)', B)]
hB, probs = _grc.alinhar(c, total=150, inicio=119, maxgap=3)
_grc.avisos([p for p in probs if not p.startswith('FALTA')])
faltaB = [n for n in range(119, 151) if n not in hB]
stB, naoB = _grc.sequencial(B, 150, de=0, conhecidos=dict(hB), k=4)
stB = {n: p for n, p in stB.items() if n >= 119}
_r = _grc.refinar(B, {n: p for n, p in stB.items() if n not in hB})
iniB = {n: (hB[n] if n in hB else _r[n]) for n in stB}
print('Sl 1–118 sem rastro:', naoA, '| Sl 119–150 sem rastro:', [n for n in range(119, 151) if n not in stB])
print('Sl 119–150 achados só pelo versículo:', faltaB)

starts = {n: p for n, p in iniA.items()}
starts.update({n: p + OFF for n, p in iniB.items()})
falhas = _grc.verificar(T, {n: starts[n] for n in starts}, so_estes=None)
print('começo sem o 1º versículo à vista:', falhas)
# o primeiro salmo começa depois do prefácio («ΕΙΣ ΤΑΣ ΕΠΙΓΡΑΦΑΣ»): garantido pelo versículo


def cobre(h, pres, corpo):
    cont = [n for n in pres if 51 <= n <= 95]
    if cont and len(cont) == len(pres):
        return 'o salmo inteiro (Eusébio comenta de forma contínua os Sl 51–95); pode parar antes do fim em alguns salmos'
    return ('SÓ CADEIA: excertos de cadeia que levam o nome de Eusébio, misturados a trechos de outros autores '
            '(Orígenes, Dídimo, Apolinário…); atribuição insegura e pode parar antes do fim do salmo')


def fonte(h, pres):
    return URL_A if pres[0] <= 118 else URL_B


def edicao(h, pres, ini, fim):
    return _grc.titulo_edicao(T, ini, fim)


_grc.produzir(
    SCRIPT, 'eusebio-commentaria-in-psalmos', 'Eusébio de Cesareia, Commentaria in Psalmos',
    'Eusébio de Cesareia (c. 263–339)', 'Commentaria in Psalmos (Ἐξηγητικὰ εἰς τοὺς Ψαλμούς)', URL_A, T, starts,
    edicao_fn=edicao, cobre_fn=cobre, fonte_fn=fonte)
