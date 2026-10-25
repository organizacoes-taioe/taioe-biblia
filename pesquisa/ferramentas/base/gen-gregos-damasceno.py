"""São João Damasceno, Expositio fidei (Exposição exata da fé ortodoxa), os capítulos sobre a criação (Kotter 16–26 = II, 2–12).

    python3 -I pesquisa/ferramentas/base/gen-gregos-damasceno.py [capítulos]      (padrão: 1; ex.: 1-3)

Baixa UMA vez o PDF da khazarzar «John of Damascus_PG 94-96/Expositio fidei.pdf» (ed. Kotter, Die Schriften des Johannes von
Damaskos II, 1973: capítulos 1–100 numerados de seguida; o PDF é apagado depois da conversão). Não é comentário versículo por
versículo, mas segue a ordem de Gn 1: a criação por bondade (16), os anjos (17–18), a criação visível (19), o céu (20), a luz e os
luzeiros (21), o ar (22), as águas (23), a terra, as plantas e os animais (24), o paraíso (25, Gn 2) e o homem (26, imagem e
semelhança, Gn 1,26–27 e 2,7). Tabela MAPA: Gn 1 = 16, 19–24, 26; Gn 2 = 25–26.
Na PG: 94, 864–928 (De fide orthodoxa II, 2–12; colunas não vêm no PDF).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
URL = G.khz('John of Damascus_PG 94-96', 'Expositio fidei.pdf')
MAPA = {1: [16, 19, 20, 21, 22, 23, 24, 26], 2: [25, 26]}


def main():
    caps = G.capitulos()
    t = G.texto_pdf(URL, 'damasceno-expositio-fidei', colunas_pg=False)
    pos = {}
    for m in re.finditer(r'(?<=[\s.;·»])(\d{1,3}) (?=Περὶ )', t):
        n = int(m.group(1))
        if n not in pos and (not pos or n > max(pos)):
            pos[n] = m.start()
    ns = sorted(pos)
    for cap in caps:
        quais = [n for n in MAPA.get(cap, []) if n in pos]
        if not quais:
            G.ausente(cap, f'São João Damasceno, Expositio fidei: nada sobre Gn {cap} nos capítulos da criação (16–26).')
            continue
        partes = []
        for n in quais:
            a = pos[n]
            prox = [m for m in ns if m > n]
            b = pos[prox[0]] if prox else len(t)
            partes.append(f'**[cap. {n} (Kotter) = II, {n - 14}]** ' + t[a:b].strip())
        campos = {
            'Autor': 'São João Damasceno (c. 675–749)',
            'Obra': 'Expositio fidei (Exposição exata da fé ortodoxa; De fide orthodoxa)',
            'Passagem': 'caps. ' + ', '.join(str(n) for n in quais) + ' (Kotter) = livro II, ' + ', '.join(str(n - 14) for n in quais),
            'Edição': 'PG 94, 864–928 (as colunas não vêm no PDF); texto da ed. Kotter (1973)',
            'Fonte': URL,
            'Cobre': {1: 'a criação na ordem de Gn 1 (bondade de Deus, céu, luz, luzeiros, águas, terra) e o homem à imagem (cap. 26)',
                      2: 'o paraíso (cap. 25) e o homem (cap. 26)'}.get(cap, ''),
            'Oriental': 'sim',
            'Língua': 'grc',
        }
        nota = ('Edição moderna (Kotter): para citar, conferir com a PG 94 (domínio público). A numeração «II, n» é a das '
                'edições antigas (livro II = caps. 15–44 de Kotter).')
        G.gravar(cap, 'damasceno-expositio-fidei', 'São João Damasceno, Expositio fidei', campos, '\n\n'.join(partes), nota, SCRIPT)
    G.registrar()


if __name__ == '__main__':
    main()
