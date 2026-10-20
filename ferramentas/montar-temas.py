"""Monta os comentários de um capítulo (por trecho e tema) a partir dos achados da pesquisa.

    python -I -X utf8 ferramentas/montar-temas.py <livro> <cap>             # grava conteudo/<livro>/<ccc>.json
    python -I -X utf8 ferramentas/montar-temas.py <livro> <cap> --mostrar   # só mostra, para ler antes
    python -I -X utf8 ferramentas/montar-temas.py <livro> <cap> --refazer   # refaz também os itens já publicados

Entradas, em pesquisa/<livro>/<ccc>/:
- achados-*.json (formato em pesquisa/COMO-PESQUISAR.md);
- temas.json, a escolha e a ordem: {"<trecho>": [{"id", "titulo", "versiculos": [..], "resumo",
  "itens": ["<id do achado>", {"id": "<id do achado>", "texto": "…", "passagem": "…"}, …]}]}.
  Um item pode ser só o id ou um objeto que troca campos do achado (texto, obra, passagem, autor).
  Sem "versiculos", vale a união dos versículos dos achados, dentro do trecho.

O autor e o «sobre» vêm de ferramentas/autores.json (o mesmo nome e a mesma descrição em todos os
capítulos); autor novo entra lá antes, com "oriental": true ou false. Item já publicado (mesmo id)
guarda o que tem (texto revisto, `revisto`, `aviso_corte`), a não ser com --refazer.
No fim mostra a conta: comentários, temas, achados de fora e quantos são de Padres orientais.
"""
import glob, json, os, re, sys

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from formato import gravar  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith('--')]
if len(args) != 2:
    sys.exit(__doc__)
livro, cap = args[0], f'{int(args[1]):03d}'
MOSTRAR, REFAZER = '--mostrar' in sys.argv, '--refazer' in sys.argv
PESQ = os.path.join(RAIZ, 'pesquisa', livro, cap)
ARQ = os.path.join(RAIZ, 'conteudo', livro, f'{cap}.json')
AUTORES = json.load(open(os.path.join(RAIZ, 'ferramentas', 'autores.json'), encoding='utf-8'))
ID = re.compile(r'^[a-z0-9][a-z0-9._-]{0,60}$')
problemas = []

achados = {}
for f in sorted(glob.glob(os.path.join(PESQ, 'achados-*.json'))):
    for a in json.load(open(f, encoding='utf-8')):
        if a['id'] in achados:
            problemas.append(f'achado repetido: {a["id"]} ({os.path.basename(f)})')
        achados[a['id']] = a
temas_arq = os.path.join(PESQ, 'temas.json')
if not os.path.exists(temas_arq):
    sys.exit(f'falta {temas_arq}')
T = json.load(open(temas_arq, encoding='utf-8'))
cap_json = json.load(open(ARQ, encoding='utf-8'))
trechos = cap_json['trechos']
ultimo = max(int(v['v']) for v in cap_json['texto'] if 'v' in v and str(v['v']).isdigit())
faixa = {t['id']: (t['de'], (trechos[i + 1]['de'] - 1) if i + 1 < len(trechos) else ultimo) for i, t in enumerate(trechos)}

publicados = {}
for com in (cap_json.get('comentarios') or {}).values():
    for t in com.get('temas', []):
        publicados['tema:' + t['id']] = t
        for it in t['itens']:
            publicados[it['id']] = it


def limpar(texto, onde):
    # nota do pesquisador entre colchetes, no fim ou no meio («[conferir na imagem]», «[Texto da edição…]»)
    for m in re.finditer(r'\s*\[(?!Sobre |…|\.\.\.)[^\]]{12,}\]', texto):
        problemas.append(f'{onde}: tirada a nota do pesquisador {m.group(0).strip()[:70]!r}')
    texto = re.sub(r'\s*\[(?!Sobre |…|\.\.\.)[^\]]{12,}\]', '', texto)
    texto = texto.replace('[...]', '[…]').replace('nalguns', 'em alguns').replace('nalgumas', 'em algumas')
    return texto.strip()


def nome_autor(a, onde):
    nome = a['autor']
    e = AUTORES.get(nome)
    if e is None:
        problemas.append(f'{onde}: autor fora de ferramentas/autores.json: {nome!r} (acrescentar com "sobre" e "oriental")')
        return nome, {'sobre': '', 'oriental': False}
    if e.get('usar'):
        return e['usar'], AUTORES[e['usar']]
    return nome, e


def item(ref, tr):
    troca = ref if isinstance(ref, dict) else {}
    i = troca.get('id', ref)
    if i not in achados:
        problemas.append(f'trecho {tr}: achado que não existe: {i}')
        return None, False
    a = dict(achados[i], **{k: v for k, v in troca.items() if k != 'id'})
    if 'texto' in troca:
        a['traducao_pt'] = troca['texto']
    iid = i.lower()
    if not ID.match(iid):
        problemas.append(f'id que o conferir recusa: {i}')
    autor, e = nome_autor(a, iid)
    passagem = a.get('passagem', '').strip()
    if passagem in ('', '—', '-'):
        passagem = a.get('edicao') or 'texto inteiro no link'
    elif a.get('edicao') and a['edicao'] not in passagem:
        passagem += f" ({a['edicao']})"
    link = (a.get('fonte_url') or a.get('link') or '').replace('http://', 'https://')
    out = {'id': iid, 'autor': autor}
    if e.get('sobre'):
        out['sobre'] = e['sobre']
    out.update({'obra': a['obra'], 'passagem': passagem, 'texto': limpar(a['traducao_pt'], iid), 'link': link,
                'original': a.get('original', '')})
    if iid in publicados and not REFAZER:
        out = publicados[iid]
    return out, e.get('oriental', False)


usados, comentarios, n_or, n = [], {}, 0, 0
por_trecho = {}
for tr, temas in T.items():
    if tr not in faixa:
        problemas.append(f'trecho que não existe no capítulo: {tr}')
        continue
    a, b = faixa[tr]
    lista = []
    for t in temas:
        itens, vv, o = [], set(), 0
        for ref in t['itens']:
            i = ref['id'] if isinstance(ref, dict) else ref
            if i in usados:
                problemas.append(f'achado usado duas vezes: {i}')
            usados.append(i)
            it, oriental = item(ref, tr)
            if it:
                itens.append(it)
                o += oriental
                vv.update(v for v in (achados[i].get('versiculos') or []) if isinstance(v, int) and a <= v <= b)
        if not 2 <= len(itens) <= 8:
            problemas.append(f'tema {t["id"]}: {len(itens)} comentário(s) (o normal é de 2 a 8)')
        tema = {'id': t['id'], 'titulo': t['titulo'], 'versiculos': t.get('versiculos') or sorted(vv) or list(range(a, b + 1)),
                'resumo': t['resumo'], 'itens': itens}
        antigo = publicados.get('tema:' + t['id'])
        if antigo and not REFAZER:
            for k in ('titulo', 'resumo', 'revisto'):
                if k in antigo:
                    tema[k] = antigo[k]
        lista.append(tema)
        n += len(itens)
        n_or += o
        por_trecho[tr] = por_trecho.get(tr, [0, 0])
        por_trecho[tr][0] += len(itens)
        por_trecho[tr][1] += o
    comentarios[tr] = {'temas': lista}

if MOSTRAR:
    for tr, c in comentarios.items():
        for t in c['temas']:
            print(f'\n######## trecho {tr} | {t["id"]} | {t["titulo"]} | vv. {t["versiculos"]}\n{t["resumo"]}')
            for i in t['itens']:
                print(f'\n== {i["id"]} | {i["autor"]} | {i["obra"]} | {i["passagem"]}\n{i["texto"]}')
else:
    cap_json['comentarios'] = comentarios
    gravar(ARQ, cap_json)

fora = sorted(set(achados) - set(usados))
print(f'\n{n} comentários em {sum(len(c["temas"]) for c in comentarios.values())} temas, de {len(achados)} achados'
      + ('' if MOSTRAR else f'; gravado em conteudo/{livro}/{cap}.json'))
if n:
    print(f'orientais: {n_or} de {n} ({round(100 * n_or / n)}%); por trecho: '
          + ', '.join(f'{tr}: {o}/{t}' for tr, (t, o) in por_trecho.items()))
print(f'achados de fora: {len(fora)}' + (f' ({", ".join(fora[:40])}{"…" if len(fora) > 40 else ""})' if fora else ''))
if problemas:
    print('\nPROBLEMAS:\n- ' + '\n- '.join(problemas))
    sys.exit(1)
