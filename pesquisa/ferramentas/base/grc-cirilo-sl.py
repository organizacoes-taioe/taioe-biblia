"""São Cirilo de Alexandria, Expositio in Psalmos (PG 69, 717–1273): um arquivo por salmo.

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-cirilo-sl.py
PDF do khazarzar (cache/base/grc/), limpo com gregos-limpar.py. Cabeçalhos «ΨΑΛΜΟΣ ΛΒʹ.» (LXX; o OCR perde o ϛ, a koppa
sai como «ς» e às vezes falta o ʹ). Onde o cabeçalho falta, o começo vem do primeiro versículo citado (_grc.descobrir).
É uma cadeia (ed. Mai): trechos entre colchetes têm origem não explicada no PDF, as siglas «(A f. 175)» são dos
manuscritos, e várias glosas repetem Basílio e Teodoreto. O texto vai só até o começo do Sl 119 da LXX (col. 1273).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-cirilo-sl.py'
URL = _grc.khz('Cyril of Alexandria_PG 68-77', 'Expositio in Psalmos.pdf')
t = _grc.texto(URL, 'cirilo-ps')
RX = r'ΨΑΛΜΟΣ\s*([Α-Ωςϛ Ϛʹ]{1,9})'
d = _grc.descobrir(t, RX)
_grc.avisos(d['avisos'])
print('achados só pelo versículo:', d['achados'], '| sem rastro:', d['nao'])
print('começo sem o 1º versículo à vista:', _grc.verificar(t, d['starts']))
ini = dict(d['ini'])
if d['bloco9b']:
    ini[9.5] = d['bloco9b']
# o prefácio («ΠΡΟΟΙΜΙΟΝ») fica de fora: é geral, não é de nenhum salmo

_grc.produzir(
    SCRIPT, 'cirilo-expositio-in-psalmos', 'São Cirilo de Alexandria, Expositio in Psalmos',
    'São Cirilo de Alexandria (c. 376–444)', 'Expositio in Psalmos (Ἐξήγησις εἰς τοὺς Ψαλμούς)', URL, t, ini,
    cobre_fn=lambda h, pres, corpo: ('excertos de cadeia (ed. Mai) sobre o salmo; não cobre todos os versículos; trechos entre '
                                    'colchetes têm origem incerta e várias glosas repetem Basílio e Teodoreto'),
    motivo_ausente=lambda h: 'a cadeia não traz este salmo (o texto da PG 69 acaba no Sl 119 da LXX)')
