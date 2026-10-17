"""Grava um capítulo da Bíblia Taioé em JSON legível: um versículo, uma nota ou um comentário por linha.

    python ferramentas/formato.py conteudo/salmos/033.json   (reformata no lugar)
"""
import json, sys

def dump(o, nivel=0):
    pad = ' ' * nivel
    if isinstance(o, dict):
        if all(not isinstance(v, (dict, list)) or (isinstance(v, list) and all(isinstance(x, str) for x in v)) for v in o.values()):
            return json.dumps(o, ensure_ascii=False)
        itens = [f'{pad} {json.dumps(k, ensure_ascii=False)}: {dump(v, nivel + 1).lstrip()}' for k, v in o.items()]
        return '{\n' + ',\n'.join(itens) + f'\n{pad}}}'
    if isinstance(o, list):
        if not o:
            return '[]'
        if all(not isinstance(x, (dict, list)) for x in o):
            return json.dumps(o, ensure_ascii=False)
        return '[\n' + ',\n'.join(pad + ' ' + dump(x, nivel + 1).lstrip() for x in o) + f'\n{pad}]'
    return json.dumps(o, ensure_ascii=False)

def gravar(caminho, dados):
    with open(caminho, 'w', encoding='utf-8', newline='\n') as f:
        f.write(dump(dados) + '\n')

if __name__ == '__main__':
    for p in sys.argv[1:]:
        gravar(p, json.load(open(p, encoding='utf-8')))
