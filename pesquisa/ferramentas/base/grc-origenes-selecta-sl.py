"""Orígenes, Selecta in Psalmos (PG 12, 1053–1686): um arquivo por salmo.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-origenes-selecta-sl.py
PDF do khazarzar «Origenes_PG 11-17/Selecta in Psalmos.pdf». Cabeçalhos «ΨΑΛΜΟΣ ΛΒʹ.» (LXX). São glosas de cadeia
(lemas terminados em «κ. τ. ἑ.»); boa parte é de Evágrio, e há trechos que Mühlenberg dá a Dídimo. A introdução geral
(«Διὰ τοὺς ἐπιγεγραμμένους ψαλμοὺς εἰς τὸ τέλος») fica de fora; o «Τόμος» sobre o Sl 1 entra no Sl 1.
O Sl 9 da LXX aparece em dois blocos: «ΨΑΛΜΟΣ Ιʹ (Κατὰ Ἑβρ.) Ἵνα τί, Κύριε» é o Sl 10 hebraico.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-origenes-selecta-sl.py'
URL = _grc.khz('Origenes_PG 11-17', 'Selecta in Psalmos.pdf')
t = _grc.texto(URL, 'origenes-sel')
RX = r'ΨΑΛΜΟΣ\s*([Α-Ωςϛ Ϛʹ]{1,9})'
d = _grc.descobrir(t, RX, bloco9b_rx=r'Ἵνα τί')
_grc.avisos(d['avisos'])
print('achados só pelo versículo:', d['achados'], '| sem rastro:', d['nao'], '| bloco 9b:', d['bloco9b'])
print('começo sem o 1º versículo à vista:', _grc.verificar(t, d['starts']))
ini = dict(d['ini'])
m = re.search(r'ΤΟΥ ΕΙΣ ΤΟΝ Αʹ ΨΑΛΜΟΝ ΤΟΜΟΥ', t)
if m and m.start() < ini[1]:
    ini[1] = m.start()
if d['bloco9b']:
    ini[9.5] = d['bloco9b']

_grc.produzir(
    SCRIPT, 'origenes-selecta-in-psalmos', 'Orígenes, Selecta in Psalmos',
    'Orígenes de Alexandria (c. 185–254)', 'Selecta in Psalmos (Ἐκ τῶν Ὠριγένους εἰς Ψαλμούς)', URL, t, ini,
    cobre_fn=lambda h, pres, corpo: ('só glosas de cadeia sobre trechos do salmo (lemas terminados em «κ. τ. ἑ.»); '
                                    'parte é de Evágrio ou de Dídimo; atribuição insegura'),
    motivo_ausente=lambda h: 'a coleção não traz este salmo')
