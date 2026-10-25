"""Santo Agostinho, Quaestiones in Heptateuchum I (Quaestiones in Genesim) e Locutiones in Heptateuchum I (Locutiones de
Genesi), PL 34, por capítulo do Gênesis.

    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-quaestiones.py [capítulos]     (padrão: 3-50; ex.: 4 ou 4-11)
    python3 -I -X utf8 pesquisa/ferramentas/base/gen-agostinho-quaestiones.py --tabela        (só mostra capítulo -> questões)

Baixa UMA vez (gen_agostinho_comum.obter_cc, cache em pesquisa/cache/genesis/agostinho/cc/) os textos 7312 (Quaestiones) e
7311 (Locutiones) do Corpus Corporum (https://mlat.uzh.ch/browser/cps_2.AugHip.QuInHe e .../cps_2.AugHip.LoInHe), o texto
dos Maurinos (= PL 34) com as colunas da PL, e grava em genesis/<ccc>/base/:
  - agostinho-quaestiones-in-heptateuchum-1.md: as questões cujo versículo-título é deste capítulo (173 questões no livro I,
    de Gn 4,17 a Gn 50,22; o Gn 1–3 Agostinho deixou de fora, «de quibus alias disseruimus»: os livros sobre o Gênesis);
  - agostinho-locutiones-in-heptateuchum-1.md: as entradas deste capítulo (notas de gramática sobre a Vetus Latina; começam
    em Gn 1,14).
Como corta (no modelo de lat-agostinho-num.py): cada questão começa com o número romano numa linha («II.») e a referência da
Vulgata entre colchetes na seguinte («[Ib. V, 25.]»; a primeira, «QUAEST. I. [GEN. cap. IV, V\\ 17.]»; a última, «CLXXIII
[Ib. L, 22.]»); o capítulo é o do colchete (algarismo romano), mesmo quando a questão volta atrás (a q. 24 trata Gn 10,21
depois das de Gn 11). Nas Locutiones, «[Ib. 8.]» sem capítulo continua no último capítulo citado. As notas de rodapé de Migne
(«1: (Gen. V, 4)») e as marcas «[col. 0549]» ficam no texto. Capítulos da Vulgata = os nossos, salvo Vulg. 31,55 = 32,1 e
Vulg. 32,1-32 = 32,2-33 (nenhuma questão cai na divisa).
Gn 1 e 2: o script também grava, se pedido (as Locutiones têm entradas de Gn 1–3); a pré-pesquisa de 25/10 rodou só 3-50.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_agostinho_comum as A  # noqa: E402

SCRIPT = os.path.basename(__file__)
IDQ, IDL = 7312, 7311
URLQ = 'https://mlat.uzh.ch/browser/cps_2.AugHip.QuInHe'
URLL = 'https://mlat.uzh.ch/browser/cps_2.AugHip.LoInHe'
URL_AUG_Q = 'https://www.augustinus.it/latino/questioni_ettateuco/quest_ettateuco_1_libro.htm'
ROM = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
COL_RE = re.compile(r'^\[col\. (\w+)\]$')


def romano(s):
    s = s.upper().replace('.', '').strip()
    n = 0
    for i, c in enumerate(s):
        v = ROM[c]
        n += -v if i + 1 < len(s) and ROM[s[i + 1]] > v else v
    return n


def capitulos(argv):
    if not argv:
        return list(range(3, 51))
    out = []
    for parte in ','.join(argv).split(','):
        if '-' in parte:
            a, b = parte.split('-', 1)
            out.extend(range(int(a), int(b) + 1))
        elif parte.strip():
            out.append(int(parte))
    return sorted(set(c for c in out if 1 <= c <= 50))


def linhas_cc(idno):
    """Texto do Corpus sem o cabeçalho, com as marcas de página da PL viradas em «[col. 0549]» numa linha própria."""
    t = A.obter_cc(idno)
    i = t.find('######')
    if i >= 0:
        t = t[t.find('\n', i) + 1:]
    t = re.sub(r'^-{5,}\[page (\w+)\]-{5,}\s*$', lambda m: f'[col. {m.group(1)}]', t, flags=re.M)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip('\n').split('\n')


def ultima_col(L, i):
    for j in range(i, -1, -1):
        m = COL_RE.match(L[j].strip())
        if m:
            return m.group(1)
    return None


def cortar(L, a, b):
    """Linhas a..b-1, com a coluna em vigor no começo, sem brancos nas pontas e sem o recuo do Corpus."""
    seg = [l.strip() for l in L[a:b]]
    while seg and not seg[0]:
        seg.pop(0)
    while seg and not seg[-1]:
        seg.pop()
    if seg and not COL_RE.match(seg[0]):
        c = ultima_col(L, a)
        if c:
            seg.insert(0, f'[col. {c}]')
    return '\n'.join(seg)


def colunas(txt):
    ns = [int(re.match(r'\d+', c).group(0)) for c in re.findall(r'\[col\. (\w+)\]', txt)]
    return (min(ns), max(ns)) if ns else (None, None)


def edicao(txt, csel):
    a, b = colunas(txt)
    if a is None:
        return f'PL 34; {csel}'
    return f'PL 34, {a}' + (f'–{b}' if b != a else '') + f'; {csel}'


def livro1(L, titulo_re):
    a0 = next(i for i, l in enumerate(L) if re.match(titulo_re, l.strip()))
    a1 = next(i for i, l in enumerate(L) if i > a0 and re.match(r'LIBER SECUNDUS\.', l.strip()))
    return a0, a1


def quaestiones():
    """{cap: [(n.º da questão, referência, texto)]}"""
    L = linhas_cc(IDQ)
    a0, a1 = livro1(L, r'LIBER PRIMUS\. Quaestiones in Genesim')
    # o colchete varia: «[GEN. cap. IV, V\ 17.]», «[Ib. V, 25.]», «[Ib XXVIII, 18.]», «[In XXV, 1.]», «[Ib. 28, 2.]»
    ref = re.compile(r'^\[(?:GEN\. cap\.|Ib\.?|In)\s*([IVXLC]+|\d+)[,.]\s*(?:V\\\s*)?([^\]]*)\]')
    ini = []
    for i in range(a0, a1):
        s = L[i].strip()
        mi = re.match(r'^(?:QUAEST\.\s*)?([IVXLC]+)\.?(?:\s+(\[.*))?$', s)
        if not mi:
            continue
        if mi.group(2):                      # «QUAEST. I. [GEN. …]», «CLXXIII [Ib. L, 22.]»
            linha_ref = mi.group(2)
        else:                                # o número sozinho; o colchete na linha seguinte
            prox = next((L[j].strip() for j in range(i + 1, min(i + 3, a1)) if L[j].strip()), '')
            if not prox.startswith('['):
                continue
            linha_ref = prox
        m = ref.match(linha_ref)
        if not m:
            print('  aviso: referência ilegível:', linha_ref[:60])
            continue
        c = int(m.group(1)) if m.group(1).isdigit() else romano(m.group(1))
        outros = [romano(x) for x in re.findall(r'\bet ([IVXLC]+),', m.group(2))]      # «XXXIII, 5, et XXXIV, 25»
        ini.append((i, romano(mi.group(1)), [c] + outros, f'{m.group(1)}, {m.group(2).strip().rstrip(".")}'))
    por = {}
    fins = [x[0] for x in ini[1:]] + [a1]
    for k, ((c, num, caps, r), fim) in enumerate(zip(ini, fins), start=1):
        if num != k:
            print(f'  aviso: questão {k} com o número {num} no texto ({r})')
        for cap in dict.fromkeys(caps):
            por.setdefault(cap, []).append((k, r, cortar(L, c, fim)))
    return por, len(ini)


def locutiones():
    """{cap: (n.º de entradas, texto)}: as entradas seguidas de um capítulo formam um bloco só."""
    L = linhas_cc(IDL)
    a0, a1 = livro1(L, r'LIBER PRIMUS\. Locutiones de Genesi')
    ref = re.compile(r'\[(?:Gen\. cap\.|Ibid\.|Ib\.?|In\.?)?\s*(?:([IVXLC]+)[,.]\s*(?:V\\\s*)?)?(\d+)')     # também «[In 5.]», «[In. 35.]»
    ini, cap = [], None
    for i in range(a0, a1):
        s = L[i].strip()
        m = ref.match(s) if s.startswith('[') else None
        if m:
            if m.group(1):
                cap = romano(m.group(1))
            ini.append((i, cap))
    blocos = {}
    fins = [x[0] for x in ini[1:]] + [a1]
    for (i, c), fim in zip(ini, fins):
        b = blocos.setdefault(c, [])
        b.append(cortar(L, i, fim))
    return {c: (len(v), '\n'.join(v)) for c, v in blocos.items()}


INI, FIM = '<!-- automático: gen-agostinho-quaestiones -->', '<!-- fim do automático -->'


def ausentes(cap, linhas):
    """Grava as linhas no bloco automático deste script em genesis/<ccc>/base/_ausentes-agostinho.md (o resto do
    arquivo, escrito à mão ou por outro script, fica)."""
    p = os.path.join(A.RAIZ, 'genesis', f'{cap:03d}', 'base', '_ausentes-agostinho.md')
    velho = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    resto = re.sub(re.escape(INI) + r'.*?' + re.escape(FIM) + r'\n?', '', velho, flags=re.S).strip()
    if not linhas and not resto:
        if os.path.exists(p):
            os.remove(p)
        return
    if not resto.startswith('# '):
        resto = (f'# Ausentes: Santo Agostinho (Gn {cap})\n\n' + resto).strip()
    bloco = INI + '\n' + '\n'.join(f'- {l}' for l in linhas) + '\n' + FIM if linhas else ''
    tit, _, corpo = resto.partition('\n')
    txt = tit + '\n\n' + (bloco + '\n\n' if bloco else '') + corpo.strip()
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt.strip() + '\n')


def main():
    args = sys.argv[1:]
    Q, nq = quaestiones()
    LO = locutiones()
    if args[:1] == ['--tabela']:
        print(f'Quaestiones I: {nq} questões')
        for c in range(1, 51):
            print(f'Gn {c:2d}: Q {[k for k, r, t in Q.get(c, [])]}  L {LO.get(c, (0, ""))[0]}')
        return
    caps = capitulos(args)
    gq = gl = 0
    for cap in caps:
        qs = Q.get(cap, [])
        if qs:
            corpo = '\n\n'.join(f'**[Quaestiones in Heptateuchum I, q. {k}: Gen. {r}]**\n\n{t}' for k, r, t in qs)
            ks = [k for k, r, t in qs]
            A.gravar(cap, 'agostinho-quaestiones-in-heptateuchum-1.md',
                     'Santo Agostinho, Quaestiones in Heptateuchum I (Gênesis)',
                     'Quaestiones in Heptateuchum, livro I (Quaestiones in Genesim)',
                     f'Gn {cap}; Quaest. in Hept. I, ' + (f'q. {ks[0]}' if len(ks) == 1 else 'qq. ' + ', '.join(map(str, ks))),
                     edicao(corpo, 'CSEL 28/2 (Zycha, 1895)'), f'{URLQ} (texto do Corpus Corporum, idno {IDQ}); versão italiana ao lado em {URL_AUG_Q}',
                     'todas as questões de Agostinho sobre este capítulo (a referência entre colchetes é da Vulgata)',
                     corpo, SCRIPT,
                     'questões curtas e literais, escritas por volta de 419; a numeração das questões é a da ordem do livro I; '
                     'notas de rodapé de Migne («1: (Gen. V, 4)») e colunas «[col. …]» no texto')
            gq += 1
        lo = LO.get(cap)
        if lo:
            n, corpo = lo
            A.gravar(cap, 'agostinho-locutiones-in-heptateuchum-1.md',
                     'Santo Agostinho, Locutiones in Heptateuchum I (Gênesis)',
                     'Locutiones in Heptateuchum, livro I (Locutiones de Genesi)',
                     f'Gn {cap}; Locutiones in Hept. I, {n} entrada' + ('s' if n > 1 else ''),
                     edicao(corpo, 'CSEL 28/1 (Zycha, 1894)'), f'{URLL} (texto do Corpus Corporum, idno {IDL})',
                     'todas as entradas deste capítulo (só gramática e idiomatismos da Vetus Latina e da LXX)',
                     corpo, SCRIPT,
                     'as «Locutiones» são notas de gramática sobre as expressões estranhas da versão latina que Agostinho lia; '
                     'só servem para ver como ele lia o versículo; «[Ib. 8.]» sem capítulo continua no último capítulo citado')
            gl += 1
        linhas = []
        if not qs:
            antes = max((k for c, v in Q.items() if c < cap for k, r, t in v), default=None)
            linhas.append('Santo Agostinho, Quaestiones in Heptateuchum I: nenhuma questão sobre Gn %d' % cap + (
                ' (o livro começa em Gn 4,17; no prólogo ele deixa de fora Gn 1–3, «de quibus alias disseruimus», PL 34, 547–548).'
                if cap <= 3 else f' (passa da q. {antes} à q. {antes + 1}).'))
        if not lo:
            linhas.append(f'Santo Agostinho, Locutiones in Heptateuchum I: nenhuma entrada sobre Gn {cap}.')
        ausentes(cap, linhas)
    print(f'{gq} arquivos Quaestiones; {gl} arquivos Locutiones (de {len(caps)} capítulos pedidos)')


if __name__ == '__main__':
    main()
