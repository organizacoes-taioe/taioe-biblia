"""Cassiodoro, Complexiones in epistolas apostolorum (PL 70, 1339–1342), parte sobre 2 Coríntios: caps. 3 a 13.

    python -I -X utf8 pesquisa/ferramentas/base/la-cassiodoro-2cor.py            # capítulos 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/la-cassiodoro-2cor.py 3 4

Só resumos de blocos de versículos (20 parágrafos para a carta inteira, cada um com o rótulo «--III, 7.»), que o
Corpus Corporum (Zurique) publica como texto 7917:
    https://mlat.uzh.ch/php_modules/download.php?idno=7917&type=file-txt
Baixa UMA vez para pesquisa/cache/base/paulo/cc_7917.txt. O capítulo N recebe os blocos rotulados com N e, como o bloco
anterior costuma passar para o capítulo seguinte (o bloco «II, 12» chega a III,2-6), também o último bloco rotulado com N-1.
Serve pouco (resumo), mas é do séc. VI e é de graça.
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

URL = 'https://mlat.uzh.ch/php_modules/download.php?idno=7917&type=file-txt'
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11,
       'XII': 12, 'XIII': 13}


def blocos(L):
    ini = next(i for i, l in enumerate(L) if re.match(r'^\s+EPISTOLA SECUNDA AD CORINTHIOS\.', l))
    fim = next(i for i, l in enumerate(L) if i > ini and re.match(r'^\s+EPISTOLA AD GALATAS\.', l))
    seg = L[ini + 1:fim]
    out = []          # (cap do rótulo, rótulo, linhas)
    atual = None
    col = None
    for l in seg:
        m = re.match(r'^-+\[page (\w+)\]-+\s*$', l)
        if m:
            if m.group(1)[-1].isalpha():
                col = m.group(1).lstrip('0')
                if atual is not None:
                    atual[2].append(f'[col. {col}]')
            continue
        m = re.match(r'^\s*(?:\d+\.)?\s*--([IVX]+), (\d+)\.', l)
        if m:
            rotulo = f'{m.group(1)}, {m.group(2)}'
            atual = [ROM[m.group(1)], rotulo, []]
            atual[2].append(f'[col. {col}]' if col else '')
            out.append(atual)
            atual[2].append(l.strip().lstrip('0123456789. ').strip())
            continue
        if atual is not None and not re.fullmatch(r'\s*\d+\.\s*', l):
            atual[2].append(l.rstrip())
        elif atual is None and l.strip():
            pass
    return out


def main():
    caps = [int(a) for a in sys.argv[1:]] or CAPS
    L = ler(baixar(URL, 'cc_7917.txt')).split('\n')
    bl = blocos(L)
    saidas = []
    for cap in caps:
        proprios = [b for b in bl if b[0] == cap]
        anterior = [b for b in bl if b[0] == cap - 1][-1:]
        escolhidos = anterior + proprios
        if not escolhidos:
            continue
        partes = []
        for b in escolhidos:
            txt = re.sub(r'\n{2,}', '\n', '\n'.join(x for x in b[2] if x.strip() != ''))
            partes.append(f'## Bloco «{b[1]}»' + (' (começa no capítulo anterior e passa a este)' if b[0] == cap - 1 else '') + '\n\n' + txt)
        cols = re.findall(r'\[col\. (\w+)\]', '\n'.join(partes))
        ed = 'PL 70, ' + (cols[0] + (f'–{cols[-1]}' if cols[-1] != cols[0] else '') if cols else '1339–1342')
        campos = {
            'Autor': 'Cassiodoro (c. 485–c. 580)', 'Obra': 'Complexiones in epistolas apostolorum (II ad Corinthios)',
            'Passagem': f'2Cor {cap}', 'Edição': ed, 'Fonte': URL,
            'Cobre': 'só resumos dos blocos de versículos ' + '; '.join(b[1] for b in escolhidos),
            'Oriental': 'não', 'Língua': 'la'}
        nota = 'Resumos curtos de Cassiodoro, um por bloco de versículos; o rótulo «III, 7» é capítulo, versículo. Texto do Corpus Corporum.'
        saidas.append(gravar(cap, 'cassiodoro-complexiones-2cor.md', 'Cassiodoro, Complexiones in epistolas apostolorum (2 Coríntios)',
                             campos, '\n\n'.join(partes), nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
