"""Teodoreto de Ciro, Quaestiones in Octateuchum: Quaestiones in Genesin (PG 80, 77–225), por capítulo do Gênesis.

    python3 -I pesquisa/ferramentas/base/gen-gregos-teodoreto.py [capítulos]      (padrão: 1; ex.: 1-50)

Baixa UMA vez o PDF da khazarzar «Theodoretus of Cyrrhus_PG 80-84/Quaestiones in Octateuchum.pdf» (para
pesquisa/cache/genesis/gregos/, apagado depois da conversão) e grava genesis/<ccc>/base/teodoreto-quaestiones-in-genesim.md.

O PDF segue a edição moderna de Fernández Marcos–Sáenz-Badillos (Madri, 1979), SEM as colunas da PG: os números soltos no
texto (24, 25…) são páginas dessa edição. As perguntas vêm numeradas em algarismos romanos no corpo («XX Τί ἐστι τὸ "κατ'
εἰκόνα"; …»); o script as acha em sequência e dá a cada uma o capítulo do Gênesis cujas palavras ela cita (grupos de 4
palavras em comum com a LXX de Rahlfs, github.com/eliranwong/LXX-Rahlfs-1935), sem recuar; sem citação, fica no capítulo
da anterior. Gn 1 = perguntas I–XXI (a XXI, sobre a bênção do sétimo dia, é de Gn 2,3; conferido em 2026-10-25).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
URL = G.khz('Theodoretus of Cyrrhus_PG 80-84', 'Quaestiones in Octateuchum.pdf')
OCR_PG80 = 'https://archive.org/details/bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1860_80'
ROM = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def romano(s):
    n = 0
    for i, c in enumerate(s):
        v = ROM[c]
        n += -v if i + 1 < len(s) and ROM[s[i + 1]] > v else v
    return n


def rom(n):
    r = ''
    for v, s in ((100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            r += s
            n -= v
    return r


def perguntas():
    t = G.texto_pdf(URL, 'teodoreto-quaestiones-octateuchum', colunas_pg=False)
    a = t.find('QUAESTIONES IN GENESIN')
    b = t.find('QUAESTIONES IN EXODUM', a)
    seg = t[a:b if b > 0 else len(t)]
    pos, esp = [], 1
    for m in re.finditer(r'(?:(?<=[\s.;·»"])|^)([IVXLC]{1,7})\s+(?=[Α-ΩἈ-ῼ«"])', seg):
        try:
            n = romano(m.group(1))
        except KeyError:
            continue
        if n == esp or (esp < n <= esp + 2):
            pos.append((n, m.start()))
            esp = n + 1
    Q = {}
    for k, (n, p) in enumerate(pos):
        f = pos[k + 1][1] if k + 1 < len(pos) else len(seg)
        Q[n] = seg[p:f].strip()
    intro = seg[:pos[0][1]].strip() if pos else ''
    return Q, intro


def capitulos_das_perguntas(Q):
    """Capítulo de cada pergunta: o mais citado (sem recuar). Para avançar, 3 grupos de palavras em comum, ou menos se confirmado
    pela pergunta seguinte que cita alguma coisa (uma citação solta de outro capítulo não arrasta a sequência)."""
    ns = sorted(Q)
    brutos = {n: G.capitulos_citados(Q[n][:700]) for n in ns}
    ult, out = 1, {}
    for k, n in enumerate(ns):
        bons = {c: q for c, q in brutos[n].items() if c >= ult}
        c = ult
        if bons:
            melhor = max(bons, key=lambda c: (bons[c], -c))
            if melhor == ult or bons[melhor] >= 3:
                c = melhor
            else:
                seguinte = next((brutos[m] for m in ns[k + 1:] if brutos[m]), {})
                if seguinte and max(seguinte) >= melhor:
                    c = melhor
        out[n] = c
        ult = c
    return out


def main():
    caps = G.capitulos()
    Q, intro = perguntas()
    cap_de = capitulos_das_perguntas(Q)
    print(f'  Teodoreto: {len(Q)} perguntas sobre o Gênesis; Gn 1 = {[rom(n) for n, c in cap_de.items() if c == 1]}')
    for cap in caps:
        qs = [n for n in sorted(Q) if cap_de[n] == cap]
        if not qs:
            G.ausente(cap, f'Teodoreto, Quaestiones in Genesin: nenhuma pergunta sobre Gn {cap} (confirmar: o corte é automático).')
            continue
        partes = []
        if cap == 1 and intro:
            partes.append('**[prólogo a Hipácio]** ' + intro)
        partes += [f'**[pergunta {rom(n)}]** {Q[n]}' for n in qs]
        campos = {
            'Autor': 'Teodoreto de Ciro (c. 393–c. 460)',
            'Obra': 'Quaestiones in Octateuchum: Quaestiones in Genesin (Perguntas sobre o Gênesis)',
            'Passagem': 'perguntas ' + (rom(qs[0]) if len(qs) == 1 else f'{rom(qs[0])}–{rom(qs[-1])}'),
            'Edição': 'PG 80, 77–225 (as colunas não vêm no PDF); texto da ed. Fernández Marcos–Sáenz-Badillos, Madri 1979',
            'Fonte': URL,
            'Cobre': 'as perguntas e respostas sobre este capítulo',
            'Oriental': 'sim',
            'Língua': 'grc',
        }
        nota = ('O PDF segue a edição moderna de Fernández Marcos–Sáenz-Badillos (1979): usar para pesquisa e citar curto, ou conferir '
                'com a PG 80 (domínio público; colunas no OCR ' + OCR_PG80 + '). Os números soltos no texto são páginas dessa '
                'edição. O capítulo de cada pergunta vem das citações da LXX, automaticamente: conferir nas pontas.')
        G.gravar(cap, 'teodoreto-quaestiones-in-genesim', 'Teodoreto de Ciro, Quaestiones in Genesin', campos,
                 '\n\n'.join(partes), nota, SCRIPT)
    G.registrar()


if __name__ == '__main__':
    main()
