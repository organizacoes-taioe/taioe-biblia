"""Biblia Clerus (Congregação para o Clero): o que cita cada salmo (Catecismo, Verbum Domini, etc.).

    python -I -X utf8 pesquisa/ferramentas/base/mod-clerus.py baixar    # percorre os capítulos dos Salmos e as páginas de citações
    python -I -X utf8 pesquisa/ferramentas/base/mod-clerus.py analisar  # monta cache/base/modernos/clerus/indice.json

Estrutura (RSV, numeração HEBRAICA): http://www.clerus.org/bibliaclerusonline/en/zr.htm é o índice do livro dos
Salmos; cada página-capítulo (gyt.htm = Sl 1–24, depois o link «Next») traz, para cada salmo, um ícone
`<a href=9abtadh.htm><img src=c.gif title="Ps 8,1-9">` com a página de citações do salmo. Essa página lista, por
obra, os números citados: «Catechism Cath. Church: 292 703», «Verbum Domini EN: 8 20», «GENERAL AUDIENCE 2001: 38 39»
(número do documento no Clerus, não é data), Padres, Missal. Aqui só se lê o que é útil para a pré-pesquisa:
o Catecismo (números de parágrafo) e a Verbum Domini (números de parágrafo).
ARMADILHA (conferida em 2026-10-20): os números do Catecismo no Clerus NÃO são os parágrafos do Catecismo; vêm
deslocados de 1 a 6 (Sl 22,15 aparece em «114», e é o § 112; Sl 130,1 em «2565», e é o § 2559). Não usar para citar
parágrafo: a pré-pesquisa lê as notas do próprio Catecismo (mod-catecismo.py). O Clerus também mistura a numeração da
Vulgata na mesma página. Serve só para ver, por salmo, que obras o citam (Padres, Missal, audiências).
Uma requisição por vez, pausa de 1 s; cache em pesquisa/cache/base/modernos/clerus/ (fora do git).
"""
import html, json, os, re, sys, time, urllib.request

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CACHE = os.path.join(RAIZ, 'cache', 'base', 'modernos', 'clerus')
BASE = 'http://www.clerus.org/bibliaclerusonline/en/'
UA = {'User-Agent': 'Mozilla/5.0 (pesquisa Biblia Taioe)'}


def pega(arq):
    p = os.path.join(CACHE, arq)
    if os.path.exists(p):
        return open(p, encoding='latin-1').read()
    os.makedirs(CACHE, exist_ok=True)
    for i in range(3):
        try:
            req = urllib.request.Request(BASE + arq, headers=UA)
            b = urllib.request.urlopen(req, timeout=60).read()
            open(p, 'wb').write(b)
            time.sleep(1)
            return b.decode('latin-1')
        except Exception:
            time.sleep(3)
    return ''


def baixar():
    pag = 'gyt.htm'
    cits = {}  # n -> [arquivo,...]
    vistos = set()
    while pag and pag not in vistos:
        vistos.add(pag)
        h = pega(pag)
        if 'Psalms (RSV)' not in h:
            break
        for arq, tit in re.findall(r'<a href=(\w+\.htm)[^>]*><img src=c\.gif[^>]*title="(Ps [^"]*)"', h):
            n = int(re.match(r'Ps (\d+)', tit).group(1))
            cits.setdefault(n, [])
            if (arq, tit) not in cits[n]:
                cits[n].append((arq, tit))
        m = re.search(r'<a href=(\w+\.htm)><img title=Next', h)
        pag = m.group(1) if m else None
        print('capítulo', len(vistos), 'psalmos até agora', len(cits), flush=True)
    json.dump({str(k): v for k, v in cits.items()}, open(os.path.join(CACHE, 'links.json'), 'w'), indent=0)
    for n in sorted(cits):
        for arq, tit in cits[n]:
            pega(arq)
    print('páginas de citações baixadas:', sum(len(v) for v in cits.values()))


def texto(h):
    h = re.sub(r'<script.*?</script>', '', h, flags=re.S)
    h = html.unescape(re.sub(r'<[^>]+>', ' ', h))
    return re.sub(r'\s+', ' ', h)


def numeros_apos(t, rotulo):
    """«Catechism Cath. Church: 292 703 Anthony_Sermons:» → [292, 703]"""
    m = re.search(re.escape(rotulo) + r':?\s*((?:\d+\s*)+)', t)
    return [int(x) for x in m.group(1).split()] if m else []


def analisar():
    links = json.load(open(os.path.join(CACHE, 'links.json')))
    out = {}
    for n, lst in links.items():
        cat, vd, partes = set(), set(), []
        for arq, tit in lst:
            t = texto(open(os.path.join(CACHE, arq), encoding='latin-1').read())
            c = numeros_apos(t, 'Catechism Cath. Church')
            v = numeros_apos(t, 'Verbum Domini EN')
            cat |= set(c)
            vd |= set(v)
            partes.append({'arq': arq, 'tit': tit, 'cat': c, 'vd': v})
        out[n] = {'catecismo': sorted(cat), 'verbum_domini': sorted(vd), 'paginas': partes}
    json.dump(out, open(os.path.join(CACHE, 'indice.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(len(out), 'salmos;', sum(1 for v in out.values() if v['catecismo']), 'com Catecismo')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'baixar':
        baixar()
    elif cmd == 'analisar':
        analisar()
    else:
        print(__doc__)
