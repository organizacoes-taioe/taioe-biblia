"""São Tomás de Aquino, Super II ad Corinthios (Corpus Thomisticum): corta por capítulo (3 a 13).

    python -I -X utf8 pesquisa/ferramentas/base/la-tomas-2cor.py            # capítulos 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/la-tomas-2cor.py 3 4

Baixa https://www.corpusthomisticum.org/c2c.html UMA vez (ISO-8859-1) para pesquisa/cache/base/paulo/tomas_c2c.html.
Cada lição é um parágrafo `<P TITLE="Super II Cor., cap. 3 l. 1">` com o número de referência do Corpus
Thomisticum ([87701]…); o script mantém o número e a lição, e marca o itálico (citações bíblicas) com *…*.
O Corpus Thomisticum não traz a numeração da edição Marietti: citar por capítulo e lição, com o número [n].
O prólogo («pr.») não entra (é do cap. 1).
"""
import os, re, sys, html
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

URL = 'https://www.corpusthomisticum.org/c2c.html'


def limpar(frag):
    frag = re.sub(r'<SPAN CLASS="ref">.*?</SPAN>', '', frag, flags=re.S)
    frag = re.sub(r'</?I>', '*', frag, flags=re.I)
    frag = re.sub(r'<[^>]+>', '', frag)
    frag = html.unescape(frag)
    frag = frag.replace('*  *', ' ').replace('* *', ' ')
    return re.sub(r'\s+', ' ', frag).strip()


def main():
    caps = [int(a) for a in sys.argv[1:]] or CAPS
    t = ler(baixar(URL, 'tomas_c2c.html'), 'latin-1')
    por_cap = {}
    for m in re.finditer(r'<P TITLE="Super II Cor\., cap\. (\d+) l\. (\d+)"><A NAME="(\d+)">(.*?)</P>', t, flags=re.S):
        cap, lic, num, resto = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        por_cap.setdefault(cap, []).append((lic, num, limpar(resto)))
    saidas = []
    for cap in caps:
        licoes = por_cap[cap]
        corpo = '\n\n'.join(f'## Lectio {lic} [{num}]\n\n{txt}' for lic, num, txt in licoes)
        campos = {
            'Autor': 'São Tomás de Aquino (1225–1274)',
            'Obra': 'Super II ad Corinthios lectura (Super epistolas S. Pauli)',
            'Passagem': f'2Cor {cap}, lições 1–{len(licoes)}',
            'Edição': 'Corpus Thomisticum (Opera omnia, ed. Marietti e Busa; sem numeração Marietti)',
            'Fonte': URL, 'Cobre': f'o capítulo inteiro, em {len(licoes)} lições (cada lição é um parágrafo só)',
            'Oriental': 'não', 'Língua': 'la'}
        nota = ('Texto do Corpus Thomisticum, parágrafo = lição, com o número de referência entre colchetes; '
                '*itálico* = citação bíblica. Citar por capítulo e lição.')
        saidas.append(gravar(cap, 'tomas-super-2cor.md', 'São Tomás de Aquino, Super II ad Corinthios', campos, corpo, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
