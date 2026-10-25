"""São Teófilo de Antioquia, Ad Autolycum II, 10–32: o primeiro comentário cristão aos seis dias e ao começo do Gênesis.

    python3 -I pesquisa/ferramentas/base/gen-gregos-teofilo.py [capítulos]      (padrão: 1; ex.: 1-11)

Texto: First1KGreek (OpenGreekAndLatin), tlg1725.tlg001.perseus-grc2.xml = ed. J. C. T. Otto, Corpus apologetarum VIII
(Jena, 1861, domínio público), baixado UMA vez para pesquisa/cache/genesis/gregos/f1k/. Para ler capítulo por capítulo na
internet há também a BKV (Friburgo), https://bkv.unifr.ch/works/cpg-1107/versions/ad-autolycum/divisions/<n> (II,10 = 27 …
II,18 = 35), mas com o texto de Grant (Oxford 1970), que difere em pouco (em II,18 Grant lê «ἰδίων ἔργον χειρῶν», Otto
«ἀΐδιον ἔργον χειρῶν»). Na PG: 6, 1023–1168 (livro II: 1047–1104).

Cada capítulo de Ad Autolycum II vai para os capítulos do Gênesis que ele cita (grupos de 4 palavras em comum com a LXX de
Rahlfs: pelo menos 2 perto do capítulo corrente, 5 se longe) e, sem citação, para o do capítulo anterior.
Gn 1 = II, 10–18 (o 11 cita Gn 1–2,3 inteiro; o 19 resume 2,1–8).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
XML = 'https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/master/data/tlg1725/tlg001/tlg1725.tlg001.perseus-grc2.xml'
FONTE = 'https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/data/tlg1725/tlg001/tlg1725.tlg001.perseus-grc2.xml'
BKV = 'https://bkv.unifr.ch/works/cpg-1107/versions/ad-autolycum/divisions/'
DE, ATE = 10, 32


def capitulos_livro2():
    t = G.ler(G.baixar(XML, 'f1k/teofilo-grc2.xml', minimo=100000))
    b = re.search(r'<div[^>]*subtype="book"[^>]*n="2"[^>]*>(.*?)(?=<div[^>]*subtype="book"[^>]*n="3")', t, re.S).group(1)
    out = {}
    for n, c in re.findall(r'<div[^>]*subtype="chapter"[^>]*n="(\d+)"[^>]*>(.*?)</div>', b, re.S):
        c = re.sub(r'<note.*?</note>', '', c, flags=re.S)
        c = re.sub(r'<pb[^>]*n="v\.2\.p\.(\d+)"[^>]*/>', r' [Otto, p. \1] ', c)
        c = re.sub(r'<[^>]+>', '', c)
        out[int(n)] = re.sub(r'\s+', ' ', c).strip()
    return out


def main():
    caps_pedidos = G.capitulos()
    caps2 = capitulos_livro2()
    ult, por_cap = 1, {}
    for n in range(DE, ATE + 1):
        if n not in caps2:
            continue
        cont = G.capitulos_citados(caps2[n])
        # perto do capítulo corrente bastam 2 grupos; longe (citação solta, como Gn 5,2 = 1,27), 5
        cs = sorted(c for c, k in cont.items() if (k >= 2 and ult - 1 <= c <= ult + 3) or k >= 5) or [ult]
        for c in cs:
            por_cap.setdefault(c, []).append(n)
        ult = max([c for c in cs if c <= ult + 3] or [ult])
    print('  Ad Autolycum II:', {c: v for c, v in sorted(por_cap.items())})
    for cap in caps_pedidos:
        ns = por_cap.get(cap)
        if not ns:
            G.ausente(cap, f'São Teófilo de Antioquia, Ad Autolycum II: não comenta Gn {cap} (o comentário vai de Gn 1 a Gn 11).')
            continue
        partes = [f'**[II, {n}]** (BKV: {BKV}{n + 17}) {caps2[n]}' for n in ns]
        campos = {
            'Autor': 'São Teófilo de Antioquia (séc. II)',
            'Obra': 'A Autólico (Ad Autolycum), livro II',
            'Passagem': 'II, ' + (f'{ns[0]}' if len(ns) == 1 else f'{ns[0]}–{ns[-1]}'),
            'Edição': 'PG 6, 1047–1104 (livro II); texto da ed. Otto, Corpus apologetarum VIII (1861)',
            'Fonte': FONTE,
            'Cobre': 'os capítulos do livro II que citam este capítulo do Gênesis',
            'Oriental': 'sim',
            'Língua': 'grc',
        }
        nota = ('[Otto, p. n] = página da ed. Otto. O link da BKV ao lado de cada capítulo abre o mesmo trecho no texto de Grant '
                '(1970), com tradução alemã, inglesa e francesa ao lado.')
        G.gravar(cap, 'teofilo-ad-autolycum', 'São Teófilo de Antioquia, Ad Autolycum II', campos, '\n\n'.join(partes), nota, SCRIPT)
    G.registrar()


if __name__ == '__main__':
    main()
