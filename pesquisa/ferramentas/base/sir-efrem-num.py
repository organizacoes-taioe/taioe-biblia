"""Santo Efrém, o Sírio (atribuído), «In quartum Pentateuchi librum, qui Numeri dicitur, Explanatio» (Assemani, Roma 1737, t. I,
p. 250 ss.), por capítulo de Números. Tradução latina de uma cadeia siríaca.

    python -I -X utf8 pesquisa/ferramentas/base/sir-efrem-num.py

Baixa UMA vez o OCR do archive.org «assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-1» (Ephraem Syri Opera omnia Syriace/Latine, t. I;
texto em https://archive.org/download/assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-1/…_djvu.txt) e grava
numeros/<ccc>/base/efrem-in-numeros.md. O volume traz o siríaco em colunas e o latim ao lado; o OCR do siríaco é lixo (cortado aqui) e o do
latim usa o «s longo» (ſ lido como «f»: «fcripturientium»), que o script normaliza só para achar as palavras-chave, deixando o texto como saiu.
A explicação a Números vai da linha «CAP. I» (~46977) à de «IN DEUTERONOMIUM» (~50470) do OCR. Como o texto não marca o capítulo do livro
bíblico, o script o atribui por palavras-chave (nomes e termos do episódio) em unidades de ~1500 caracteres, com a ordem do livro preservada
(programação dinâmica); resultado aproximado. Efrém não escreveu comentário autêntico a Números: o «comentário» da ed. romana vem de cadeias
siríacas; tratar como «atribuído».
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _numeros_comum as C
import urllib.parse as up

ID = 'assemani-et-alii-1732-1746-ephraem-syri-opera-omnia-syr-1'
URL = f'https://archive.org/details/{ID}'
OCR = f'https://archive.org/download/{ID}/' + up.quote('Assemani et alii 1732-1746 - Ephraem Syri opera omnia Syr 1_djvu.txt')
p = C.baixar(OCR, 'efrem_djvu.txt', minimo=100000)
L = C.ler(p).split('\n')

a0 = next(i for i in range(46900, 47100) if re.match(r'^\s*CA\s*DP?\.?\s*I\.?\s*$', L[i]) or re.match(r'^\s*CAP\.\s*$', L[i]))
a1 = next(i for i in range(a0 + 100, len(L)) if re.match(r'^\s*IN DEUTERONOMIUM', L[i]))


def latim(l):
    letras = sum(c.isalpha() for c in l)
    if not letras:
        return False
    ascii_ = sum(c.isascii() and c.isalpha() for c in l)
    return ascii_ / letras >= 0.8


linhas = [(i, l) for i, l in enumerate(L[a0:a1], start=a0) if (not l.strip()) or latim(l)]
# unidades de ~1500 caracteres, cortadas em linha em branco
unid, ini, acum, buf = [], None, 0, []
for i, l in linhas:
    if ini is None:
        ini = i
    buf.append(l)
    acum += len(l) + 1
    if acum >= 1500 and not l.strip():
        unid.append((ini, i + 1, '\n'.join(buf)))
        ini, acum, buf = None, 0, []
if buf:
    unid.append((ini if ini is not None else a1 - 1, a1, '\n'.join(buf)))

cap_de = C.atribuir_dp([u[2] for u in unid], longo_s=True, primeiro=1)
por = {}
for (a, b, t), cap in zip(unid, cap_de):
    por.setdefault(cap, []).append((a, b, t))

# número da página impressa: o OCR traz «NUMEROS. | pag. 250» e «257 i NUMEROS:» em alguns cabeçalhos; usamos interpolação simples
n_arq = 0
for cap in C.CAPS:
    if cap not in por:
        continue
    tr = por[cap]
    txt = re.sub(r'\n{3,}', '\n\n', '\n\n'.join(t.strip() for a, b, t in tr)).strip()
    campos = {
        'Autor': 'Santo Efrém, o Sírio (c. 306–373), atribuído',
        'Obra': 'In quartum Pentateuchi librum, qui Numeri dicitur, Explanatio (ed. Assemani: Opera omnia Syriace et Latine, t. I)',
        'Passagem': f'{C.cap_nm(cap)}; {len(tr)} unidade(s) de ~1500 caracteres do OCR (atribuição aproximada, ver Nota)',
        'Edição': f'Assemani, Ephraem Syri Opera omnia, t. I (Roma 1737), pp. ~{250 + int((tr[0][0] - a0) / (a1 - a0) * 22)}–{250 + int((tr[-1][1] - a0) / (a1 - a0) * 22)} (estimadas; o comentário a Números ocupa pp. 250–272)',
        'Fonte': URL,
        'Cobre': 'as unidades de texto atribuídas a este capítulo (só o latim; o siríaco do OCR é ilegível); pode faltar ou sobrar meia página nas pontas',
        'Oriental': 'sim',
        'Língua': 'la',
        'Baixado': f'{C.DATA}, por pesquisa/ferramentas/base/sir-efrem-num.py',
    }
    nota = ('Tradução latina (Assemani) de um comentário siríaco a Números que a edição romana atribui a Efrém e que vem de cadeias: tratar como «atribuído». '
            'OCR do archive.org (' + OCR + '): usa o «s longo» (lido como «f»), tem erros de letras e o siríaco foi removido. Efrém ensina por tipos: Josué e '
            'Caleb como profetas, Moisés que intercede por amor. A divisão por capítulo é heurística (palavras-chave, em ordem): conferir nas imagens. '
            'Obras de Efrém em siríaco (hinos, Comentário ao Diatessaron): fora deste levantamento; ver a pista em _pistas-numeros.md.')
    C.gravar(cap, 'efrem-in-numeros', 'Santo Efrém (atribuído), Explanatio in Numeros', campos, txt, nota)
    n_arq += 1
    print(f'Nm {cap:2d}: {len(tr)} unid., {len(txt)//1024 or 1} KB')
print(n_arq, 'arquivos;', 'unidades:', len(unid), '; sem texto:', [c for c in C.CAPS if c not in por])
C.finalizar()
