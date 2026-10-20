"""Comentários latinos a 2 Coríntios na Patrologia Latina (Corpus Corporum, Zurique): corta por capítulo (3 a 13).

    python -I -X utf8 pesquisa/ferramentas/base/la-corpus-corporum-2cor.py              # todas as obras, caps. 3 a 13
    python -I -X utf8 pesquisa/ferramentas/base/la-corpus-corporum-2cor.py ambrosiaster 3 4   # uma obra, alguns capítulos

Obras (chave: texto no Corpus Corporum, PL): ambrosiaster (6985, PL 17), atao (9440, PL 134), haimo (9079,
PL 117), sedulio (8761, PL 103), lanfranco (10364, PL 150), bruno (10482, PL 153), herve (11182, PL 181),
lombardo (11467, PL 192). Cada texto é baixado UMA vez, de
    https://mlat.uzh.ch/php_modules/download.php?idno=<texto>&type=file-txt
para pesquisa/cache/base/paulo/cc_<texto>.txt. O arquivo traz a obra inteira (todas as cartas de Paulo, menos
no Ambrosiaster, que é um texto por carta); aqui se recorta só 2 Coríntios.

Como corta: o título de capítulo («CAPUT III.») abre o capítulo e o seguinte fecha. No Ambrosiaster, Haimo,
Sedúlio, Lanfranco (texto da carta com glosas + «COMMENTARIUS»), Bruno, Hervé e Lombardo isso basta. Em Atão
os capítulos só existem como nota de Migne «(CAP. III.)»: o capítulo começa na chamada [N] dessa nota.
Mantém as colunas da PL (as linhas «-----[page 0275C]-----» do Corpus viram «[col. 275C]») e as notas de
Migne; as notas que o corte deixou no capítulo vizinho voltam para o capítulo a que pertencem (bloco final).
"""
import os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paulo_comum import *

URL = 'https://mlat.uzh.ch/php_modules/download.php?idno={id}&type=file-txt'
ROM = {'PRIMUM': 1, 'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
       'X': 10, 'XI': 11, 'XII': 12, 'XIII': 13}

OBRAS = {
    'ambrosiaster': dict(id=6985, pl=17, arq='ambrosiaster-in-2cor.md',
                         autor='Ambrosiaster (escritor eclesiástico do séc. IV, Roma; a tradição o pôs entre as obras de Santo Ambrósio)',
                         obra='Commentaria in epistolam ad Corinthios secundam', ini=None, fim=None,
                         cobre='o capítulo inteiro, versículo por versículo (único comentário latino antigo contínuo às cartas de Paulo na PL)'),
    'atao': dict(id=9440, pl=134, arq='atao-expositio-2cor.md',
                 autor='Atão de Vercelli (c. 885–961)', obra='Expositio epistolarum S. Pauli (2 Coríntios)',
                 ini=r'^\s+EPISTOLA SECUNDA AD CORINTHIOS\.', fim=r'INCIPIT EXPOSITIO IN EPISTOLAM AD GALATAS',
                 cobre='o capítulo inteiro'),
    'haimo': dict(id=9079, pl=117, arq='haimo-expositio-2cor.md',
                  autor='Haimo de Auxerre (séc. IX; a PL o publica como «Haimo de Halberstadt»)',
                  obra='Expositio in D. Pauli epistolas (2 Coríntios)',
                  ini=r'^\s+IN EPISTOLAM II AD CORINTHIOS\.', fim=r'^\s+IN EPISTOLAM AD GALATAS\.',
                  cobre='o capítulo inteiro'),
    'sedulio': dict(id=8761, pl=103, arq='sedulio-collectanea-2cor.md',
                    autor='Sedúlio Escoto (séc. IX)', obra='Collectanea in omnes B. Pauli epistolas (2 Coríntios)',
                    ini=r'^\s+III\. IN EPISTOLAM II AD CORINTHIOS\.', fim=r'^\s+IV\. IN EPISTOLAM AD GALATAS\.',
                    cobre='o capítulo inteiro (breve; quase tudo é Ambrosiaster e Pelágio)'),
    'lanfranco': dict(id=10364, pl=150, arq='lanfranco-commentarius-2cor.md',
                      autor='Lanfranco de Cantuária (c. 1005–1089)',
                      obra='Commentarius in omnes epistolas Pauli (2 Coríntios, com glosas)',
                      ini=r'^\s+EPISTOLA B\. PAULI APOSTOLI AD CORINTHIOS SECUNDA', fim=r'^\s+EPISTOLA B\. PAULI APOSTOLI AD GALATAS',
                      cobre='o capítulo inteiro (texto da carta com glosas e depois «COMMENTARIUS»; só as notas LANFR. são dele, AMBROS. = Ambrosiaster)'),
    'bruno': dict(id=10482, pl=153, arq='bruno-cartuxo-expositio-2cor.md',
                  autor='São Bruno, o Cartuxo (c. 1030–1101; a autoria do comentário paulino é discutida)',
                  obra='Expositio in epistolas Pauli (2 Coríntios)',
                  ini=r'^\s+EPISTOLA II AD CORINTHIOS\.', fim=r'^\s+IN EPISTOLAM AD GALATAS\.',
                  cobre='o capítulo inteiro (texto da Vulgata entre « » e depois EXPOSITIO)'),
    'herve': dict(id=11182, pl=181, arq='herve-commentaria-2cor.md',
                  autor='Hervé de Bourg-Dieu (séc. XII; a PL o publica como Santo Anselmo)',
                  obra='Commentaria in epistolas Pauli (2 Coríntios)',
                  ini=r'^\s+IN EPISTOLAM II AD CORINTHIOS\.', fim=r'^\s+IN EPISTOLAM AD GALATAS\.',
                  cobre='o capítulo inteiro (o mais extenso dos medievais; copia Ambrosiaster e Gregório sem aviso)'),
    'lombardo': dict(id=11467, pl=192, arq='lombardo-collectanea-2cor.md',
                     autor='Pedro Lombardo (c. 1100–1160)', obra='Collectanea in epistolas Pauli (2 Coríntios)',
                     ini=r'^\s+IN EPISTOLAM II AD CORINTHIOS\.', fim=r'^\s+IN EPISTOLAM AD GALATAS\.',
                     cobre='o capítulo inteiro (compilação: [Ambrosius], [Augustinus] etc. marcados no texto)'),
}


def carregar(chave):
    o = OBRAS[chave]
    caminho = baixar(URL.format(id=o['id']), f"cc_{o['id']}.txt")
    return ler(caminho).split('\n')


def recorte(linhas, o):
    ini = 0
    if o['ini']:
        ini = next(i for i, l in enumerate(linhas) if re.search(o['ini'], l))
    fim = len(linhas)
    if o['fim']:
        fim = next(i for i, l in enumerate(linhas) if i > ini + 20 and re.search(o['fim'], l))
    return ini, fim


def inicios_capitulos(linhas, ini, fim, chave):
    """Devolve (lista de (cap, indice_de_linha), linhas possivelmente alteradas)."""
    marcas = {}
    if chave == 'atao':
        notas = {}
        for l in linhas[ini:fim]:
            m = re.match(r'^\s+(\d+): \(CAP\. ([IVX]+)\.?\)', l)
            if m:
                notas[ROM[m.group(2)]] = m.group(1)
        for cap, n in notas.items():       # a chamada [N] pode estar no meio de uma linha: parte-a ali
            for i in range(ini, fim):
                k = linhas[i].find(f'[{n}]')
                if k >= 0:
                    if k > 0 and linhas[i][:k].strip():
                        linhas[i:i + 1] = [linhas[i][:k], linhas[i][k:]]
                        fim += 1
                    break
        marcas = {}
        for cap, n in notas.items():
            for i in range(ini, fim):
                if linhas[i].startswith(f'[{n}]'):
                    marcas[cap] = i
                    break
    else:
        for i in range(ini, fim):
            m = re.match(r'^\s*(?:\d+\s+)?CAPUT\s+(PRIMUM|[IVX]+)\b', linhas[i])
            if m and ROM[m.group(1)] not in marcas:
                marcas[ROM[m.group(1)]] = i
    return marcas, fim


def converter_paginas(seg, col_antes):
    """Troca as linhas -----[page 0275C]----- por [col. 275C]; devolve o texto e as colunas inicial e final."""
    out, cols = [], []
    for l in seg:
        m = re.match(r'^-+\[page (\w+)\]-+\s*$', l)
        if m:
            col = m.group(1).lstrip('0')
            cols.append(col)
            out.append(f'[col. {col}]')
        else:
            out.append(l)
    return out, (cols[-1] if cols else col_antes)


def coluna_antes(linhas, i):
    for k in range(i, -1, -1):
        m = re.match(r'^-+\[page (\w+)\]-+\s*$', linhas[k])
        if m:
            return m.group(1).lstrip('0')
    return '?'


def numeros_de_coluna(c):
    return int(re.match(r'\d+', c).group(0)) if c and re.match(r'\d', c) else None


def main():
    args = sys.argv[1:]
    chaves = list(OBRAS)
    caps = CAPS
    if args and args[0] in OBRAS:
        chaves = [args[0]]
        args = args[1:]
    if args:
        caps = [int(a) for a in args]
    saidas = []
    for chave in chaves:
        o = OBRAS[chave]
        linhas = carregar(chave)
        ini, fim = recorte(linhas, o)
        marcas, fim = inicios_capitulos(linhas, ini, fim, chave)
        faltam = [c for c in range(1, 14) if c not in marcas]
        if faltam:
            print(f'AVISO {chave}: capítulos sem início: {faltam}')
        ordem = sorted(marcas.items(), key=lambda kv: kv[1])
        limites = {}
        for k, (cap, i) in enumerate(ordem):
            limites[cap] = (i, ordem[k + 1][1] if k + 1 < len(ordem) else fim)
        # chamadas de nota por capítulo e notas de rodapé de cada segmento
        chamadas = {}
        for cap, (a, b) in limites.items():
            ch = set()
            for l in linhas[a:b]:
                if not re.match(r'^\s+\d+: ', l):
                    ch.update(re.findall(r'\[(\d+)\]', l))
            chamadas[cap] = ch
        dono = {}
        for cap, ch in chamadas.items():
            for n in ch:
                dono.setdefault(n, cap)
        for cap in caps:
            if cap not in limites:
                continue
            a, b = limites[cap]
            seg = linhas[a:b]
            proprias, deslocadas = [], []
            exportadas = []
            for l in seg:
                m = re.match(r'^\s+(\d+): ', l)
                if m and m.group(1) not in chamadas[cap] and dono.get(m.group(1), cap) != cap:
                    exportadas.append(l)      # pertence ao capítulo vizinho: sai daqui
                    continue
                proprias.append(l)
            # notas que o corte deixou no capítulo vizinho e que pertencem a este
            for cap2, (a2, b2) in limites.items():
                if cap2 == cap:
                    continue
                for l in linhas[a2:b2]:
                    m = re.match(r'^\s+(\d+): ', l)
                    if m and m.group(1) in chamadas[cap] and m.group(1) not in chamadas[cap2]:
                        deslocadas.append(l)
            col0 = coluna_antes(linhas, a)
            corpo_linhas, col1 = converter_paginas(proprias, col0)
            corpo = '\n'.join(corpo_linhas)
            corpo = re.sub(r'\n{3,}', '\n\n', corpo).strip('\n')
            corpo = f'[col. {col0}]\n\n' + corpo
            if deslocadas:
                corpo += '\n\n[Notas de Migne deste capítulo que o texto do Corpus põe no capítulo vizinho]\n' + '\n'.join(deslocadas)
            n0, n1 = col0, col1
            ed = f"PL {o['pl']}, {n0}" + (f'–{n1}' if n1 and n1 != n0 else '')
            campos = {
                'Autor': o['autor'], 'Obra': o['obra'], 'Passagem': f'2Cor {cap}',
                'Edição': ed, 'Fonte': URL.format(id=o['id']), 'Cobre': o['cobre'],
                'Oriental': 'não', 'Língua': 'la'}
            nota = ('Texto revisto da PL de Migne no Corpus Corporum (Zurique); [col. n] marca o começo da coluna da PL. '
                    'Chamadas [n] e notas «n: (…)» são as de Migne (referências bíblicas); o título do capítulo e os '
                    'algarismos soltos (169, 170…) vêm da digitalização.')
            saidas.append(gravar(cap, o['arq'], f"{o['autor'].split(' (')[0]}, {o['obra']}", campos, corpo, nota))
    resumo(saidas)


if __name__ == '__main__':
    main()
