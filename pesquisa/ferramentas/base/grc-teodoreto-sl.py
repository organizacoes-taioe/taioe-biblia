"""Teodoreto de Ciro, Interpretatio in Psalmos (PG 80, 857–1997): um arquivo por salmo (todos).

uso: python -I -X utf8 pesquisa/ferramentas/base/grc-teodoreto-sl.py
Baixa o PDF do khazarzar UMA vez (cache/base/grc/), limpa com gregos-limpar.py, acha os cabeçalhos
«ΕΡΜΗΝ. ΤΟΥ ΛΒʹ ΨΑΛΜΟΥ» (numeração da LXX; o OCR perde o ϛ e a koppa: «Ν ʹ» = 56, «Αʹ» depois do 89
= 91, e o 141 vem sem «ΕΡΜΗΝ.») e grava salmos/<ccc>/base/teodoreto-interpretatio-in-psalmos.md.
O salmo hebraico h usa a numeração da LXX (_grc.lxx_de_hebr); 9–10, 114–115 repetem o mesmo texto.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _grc

SCRIPT = 'grc-teodoreto-sl.py'
URL = _grc.khz('Theodoretus of Cyrrhus_PG 80-84', 'Interpretatio in Psalmos.pdf')

t = _grc.texto(URL, 'teodoreto-ps')
c = []
for m in re.finditer(r'(?:ΕΡΜΗΝ(?:ΕΙΑ)?\.?\s+ΤΟΥ\s*([Α-ΩϚϛς]{1,5}\s?ʹ?)|([Α-ΩϚϛς]{1,5}\s?ʹ))\.?\s*ΨΑΛΜΟΥ', t):
    b = m.group(1) or m.group(2)
    c.append((m.start(), _grc.num_grego(b), b))
starts, probs = _grc.alinhar(c, fix={})
for p in probs:
    print('AVISO:', p)

_grc.produzir(
    SCRIPT, 'teodoreto-interpretatio-in-psalmos',
    'Teodoreto de Ciro, Interpretatio in Psalmos', 'Teodoreto de Ciro (c. 393–c. 460)',
    'Interpretatio in Psalmos (Ἑρμηνεία εἰς τοὺς Ψαλμούς)', URL, t, starts,
    cobre_fn=lambda h, pres, corpo: 'o salmo inteiro, versículo por versículo (sentido histórico e espiritual)')
