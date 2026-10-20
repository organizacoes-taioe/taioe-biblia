"""Monta o índice da pré-pesquisa de um capítulo (pesquisa/<livro>/<ccc>/BASE.md) a partir de base/.

    python -I -X utf8 pesquisa/ferramentas/base-indice.py salmos 37      # um capítulo
    python -I -X utf8 pesquisa/ferramentas/base-indice.py --todos         # todos os que têm base/

Lê o cabeçalho de cada base/<autor>-<obra>.md (as linhas «- Campo: valor» logo depois do título)
e junta os arquivos base/_ausentes-<grupo>.md e base/_pistas-<grupo>.md, que cada pesquisador
grava à parte (assim vários grupos trabalham no mesmo capítulo sem mexer no mesmo arquivo).
"""
import os, re, sys

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def cabecalho(caminho):
    titulo, campos = '', {}
    with open(caminho, encoding='utf-8') as f:
        for i, linha in enumerate(f):
            linha = linha.rstrip('\n')
            if i == 0:
                titulo = linha.lstrip('# ').strip()
                continue
            m = re.match(r'- ([A-Za-zÀ-ÿ ]+): (.*)', linha)
            if m:
                campos[m.group(1).strip().lower()] = m.group(2).strip()
            elif linha.strip() and campos:
                break
    return titulo, campos


def indice(livro, cap):
    pasta = os.path.join(RAIZ, livro, f'{int(cap):03d}')
    base = os.path.join(pasta, 'base')
    if not os.path.isdir(base):
        return None
    linhas, extras = [], {'ausentes': [], 'pistas': []}
    for nome in sorted(os.listdir(base)):
        p = os.path.join(base, nome)
        if nome.startswith('_'):
            m = re.match(r'_(ausentes|pistas)-', nome)
            if m:
                txt = open(p, encoding='utf-8').read().strip()
                txt = re.sub(r'^#.*\n+', '', txt)  # sem o título do arquivo parcial
                if txt:
                    extras[m.group(1)].append(txt)
            continue
        if not nome.endswith('.md'):
            continue
        titulo, c = cabecalho(p)
        tam = os.path.getsize(p) // 1024
        ori = 'sim' if c.get('oriental', '').lower().startswith('s') else ''
        linhas.append(f"| {titulo} | {c.get('passagem', '')} | {c.get('cobre', '')} | {ori} | [{nome}](base/{nome}) ({tam} KB) |")
    n_or = sum(1 for l in linhas if '| sim |' in l)
    out = [f'# Pré-pesquisa: {livro} {int(cap)}', '',
           'Gerado por `pesquisa/ferramentas/base-indice.py`; não editar à mão. Os textos estão em `base/`,',
           'na língua original, cortados para este capítulo. A pesquisa do capítulo parte daqui e procura o',
           'que não é óbvio (`CAPITULO.md`, etapa 6).', '',
           f'{len(linhas)} fontes, {n_or} orientais.', '',
           '| autor e obra | passagem | cobre | oriental | arquivo |', '|---|---|---|---|---|', *linhas]
    if extras['ausentes']:
        out += ['', '## Confirmado que não comentam este capítulo', '', *extras['ausentes']]
    if extras['pistas']:
        out += ['', '## Pistas (citações em outras obras, a seguir na pesquisa do capítulo)', '', *extras['pistas']]
    with open(os.path.join(pasta, 'BASE.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    return len(linhas)


if __name__ == '__main__':
    if sys.argv[1:] == ['--todos']:
        for livro in sorted(os.listdir(RAIZ)):
            d = os.path.join(RAIZ, livro)
            if not os.path.isdir(d) or livro in ('ferramentas', 'fontes', 'cache', 'estudos'):
                continue
            for cap in sorted(os.listdir(d)):
                if cap.isdigit():
                    n = indice(livro, cap)
                    if n is not None:
                        print(livro, cap, n, 'fontes')
    else:
        print(indice(sys.argv[1], sys.argv[2]), 'fontes')
