"""São Tomás de Aquino, In psalmos Davidis expositio (Postilla super Psalmos): Sl 1-54 da Vulgata, em latim.

    python -I -X utf8 pesquisa/ferramentas/base/lat-tomas.py [--so 32 37 ...]   (números hebraicos)

Corpus Thomisticum (https://www.corpusthomisticum.org/cpsNN.html, ed. de Parma 1863 digitalizada por
R. Busa e E. Alarcón; as páginas são ISO-8859-1). Páginas: cps01 = Sl 1; cps02 = 2-10; cps11 = 11-20;
cps21 = 21-30; cps31 = 31-40; cps41 = 41-50; cps51 = 51; cps52 = 52-54 (cps00 = prólogo, não entra).
Cada parágrafo é `<P TITLE="Super Psalmo N n. M">` com número de referência `[86786]`. A obra é uma
«reportatio» (Reginaldo de Piperno) e acaba no Sl 54 (Vulgata): os demais salmos vão para _ausentes.
Cache em pesquisa/cache/base/tom/. Direitos: Tomás é domínio público; a digitalização leva a nota
«© 2019 Fundación Tomás de Aquino quoad hanc editionem» (registrada no campo Nota).
"""
import sys, os, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat_comum as L

PAGINAS = {1: 'cps01', **{n: 'cps02' for n in range(2, 11)}, **{n: 'cps11' for n in range(11, 21)},
           **{n: 'cps21' for n in range(21, 31)}, **{n: 'cps31' for n in range(31, 41)},
           **{n: 'cps41' for n in range(41, 51)}, 51: 'cps51', 52: 'cps52', 53: 'cps52', 54: 'cps52'}
ROTULO = 'São Tomás de Aquino, Postilla super Psalmos'
TOM = os.path.join(L.CACHE, 'tom')


def pagina(nome):
    p = os.path.join(TOM, nome + '.html')
    L.baixar(f'https://www.corpusthomisticum.org/{nome}.html', p)
    return open(p, 'rb').read().decode('latin-1')


def texto_par(x):
    x = re.sub(r'</?I>', '*', x, flags=re.I)
    x = re.sub(r'\*\s*\*', ' ', x)
    x = re.sub(r'<BR\s*/?>', ' ', x, flags=re.I)
    x = re.sub(r'<[^>]+>', '', x)
    x = html.unescape(x).replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', x).strip()


def cortar_paginas():
    """{n_vulgata: [(ref, 'n. M', texto)]}"""
    out = {}
    for nome in sorted(set(PAGINAS.values())):
        h = pagina(nome)
        for m in re.finditer(r'<P TITLE="Super Psalmo (\d+) n\. (\d+)">\s*<A NAME="(\d+)"><SPAN CLASS="ref">\[\d+\][^<]*</SPAN></A>(.*?)</P>', h, re.S):
            n, k, ref, corpo = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
            out.setdefault(n, []).append((ref, k, texto_par(corpo)))
    return out


def main(so=None):
    sec = cortar_paginas()
    n_arq, tot = 0, 0
    for h in L.hebraicos_alvo():
        if so and h not in so:
            continue
        vs = L.vulgata_de_hebraico(h)
        tem = [v for v in vs if v in sec]
        if not tem:
            L.registrar_ausente(h, ROTULO, 'não comentou este salmo (a Postilla vai só até o Sl 54 da Vulgata = Sl 55 hebr.).')
            continue
        L.limpar_ausente(h, ROTULO)
        blocos = []
        for v in tem:
            pars = [f'**n. {k}** [{ref}] {t}' for ref, k, t in sec[v]]
            corpo = '\n\n'.join(pars)
            blocos.append(corpo if len(vs) == 1 else f'## Salmo {v} (Vulgata)\n\n{corpo}')
        corpo = '\n\n'.join(blocos)
        v0 = tem[0]
        fonte = f'https://www.corpusthomisticum.org/{PAGINAS[v0]}.html#{sec[v0][0][0]}'
        refs = f"parágrafos [{sec[tem[0]][0][0]}]–[{sec[tem[-1]][-1][0]}]"
        passagem = L.nota_numeracao(h)
        tam = L.gravar_base(h, 'tomas-postilla-super-psalmos.md', ROTULO, 'São Tomás de Aquino (1225–1274)',
                            'In psalmos Davidis expositio (Postilla super Psalmos; reportatio de Reginaldo de Piperno)',
                            passagem, f'ed. de Parma, 1863 (Corpus Thomisticum), {refs}', fonte,
                            'o salmo inteiro', corpo, 'lat-tomas.py',
                            nota='Digitalização do Corpus Thomisticum («© 2019 Fundación Tomás de Aquino quoad hanc editionem»); '
                                 'o texto de Tomás é domínio público. *itálico* = citação bíblica; [número] = referência do Corpus Thomisticum.')
        n_arq += 1
        tot += tam
    print(f'[lat-tomas.py] arquivos gravados: {n_arq}; {tot/1024:.0f} KB; salmos (Vulgata) achados: {len(sec)}')
    falt = [v for v in range(1, 55) if v not in sec]
    print('  Vulgata 1-54 sem trecho:', falt or 'nenhum')


if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--so') + 1:]} if '--so' in sys.argv else None
    main(so)
