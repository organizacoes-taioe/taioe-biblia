"""São Gregório de Nissa no Gênesis: De opificio hominis (Sobre a criação do homem, 30 capítulos) e Apologia in Hexaemeron.

    python3 -I pesquisa/ferramentas/base/gen-gregos-nissa.py [capítulos]      (padrão: 1; ex.: 1-3)

Fontes (khazarzar, «Gregory of Nyssa_PG 44-46/»; baixadas UMA vez para pesquisa/cache/genesis/gregos/, PDF apagado depois):
  - De opificio hominis.pdf: texto da PG 44, 124–256; as colunas vêm como número solto no meio do texto («ἀλλοτριώ 132 σῃ»)
    e viram «[PG 44, 132]». Os capítulos («ΚΕΦΑΛΑΙΟΝ Εʹ.») vão para o capítulo do Gênesis pela tabela MAPA (pela leitura:
    1–18 e 22 sobre Gn 1 — o mundo pronto, «Façamos o homem», a imagem, «homem e mulher», «crescei»; 19–20 e 28–30 sobre Gn 2–3
    — o alimento e as árvores do paraíso, o «pó da terra» e o sopro).
  - Apologia in hexaemeron.pdf: PG 44, 61–124 (a mesma numeração de colunas); toda sobre Gn 1 (os seis dias, a luz, o
    firmamento, as águas de cima), em defesa do Hexaémeron de Basílio.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
PASTA = 'Gregory of Nyssa_PG 44-46'
URL_OPIF = G.khz(PASTA, 'De opificio hominis.pdf')
URL_APOL = G.khz(PASTA, 'Apologia in hexaemeron.pdf')
MAPA = {1: list(range(1, 19)) + [22], 2: [19, 20, 28, 29, 30], 3: [20]}
NUM = {'ΠΡΩΤΟΝ': 1}


def num_cap(s):
    s = re.sub(r'\s+', '', s.replace('∆', 'Δ').replace('ʹ', '').replace('.', ''))
    if s in NUM:
        return NUM[s]
    v = {'Α': 1, 'Β': 2, 'Γ': 3, 'Δ': 4, 'Ε': 5, 'Ϛ': 6, 'Σ': 6, 'Ζ': 7, 'Η': 8, 'Θ': 9, 'Ι': 10, 'Κ': 20, 'Λ': 30}
    s = s.upper().replace('ς', 'Ϛ').replace('Σ', 'Ϛ')
    try:
        return sum(v[c] for c in s)
    except KeyError:
        return None


def opificio():
    t = G.texto_pdf(URL_OPIF, 'nissa-opificio', colunas_pg=False, colunas_nuas=(44, 124, 256))
    pos = []
    esperado = 1
    # «ΚΕΦΑΛΑΙΟΝ Εʹ.», «ΚΕΦΑΛΑΙΟΝ. ΙΓʹ.», «ΚΕΦΑΛΑΙΟΝς ʹ.» (o «ϛ» colado), «ΚΕΦΑΛΑΙΟΝ Ι ʹ.» (o «ϛ» perdido)
    for m in re.finditer(r'ΚΕΦΑΛΑΙΟΝ\.?\s*([^\s.]{1,8}(?:\s+ʹ)?)\.?', t):
        n = num_cap(m.group(1))
        if n is None or n != esperado:      # o OCR às vezes perde o «ϛ»: aceita o seguinte da sequência
            if n is None or not (esperado <= n <= esperado + 1):
                n = esperado
        pos.append((n, m.start()))
        esperado = n + 1
    caps = {}
    for k, (n, a) in enumerate(pos):
        b = pos[k + 1][1] if k + 1 < len(pos) else len(t)
        caps[n] = (a, b)
    prologo = (0, pos[0][1])
    return t, caps, prologo


def gravar_opificio(cap, t, caps, prologo):
    quais = [n for n in MAPA.get(cap, []) if n in caps]
    if not quais:
        G.ausente(cap, 'São Gregório de Nissa, De opificio hominis: nenhum capítulo sobre Gn ' + str(cap) + '.')
        return
    partes = []
    if cap == 1:
        a, b = prologo
        partes.append('**[Carta a Pedro, prólogo]** ' + t[a:b].strip())
    for n in quais:
        a, b = caps[n]
        partes.append(f'**[cap. {n} · {G.colunas(t, a, b, 44)}]** ' + t[a:b].strip())
    a0, b0 = caps[quais[0]]
    ed = 'PG 44, 124–256 (as colunas de cada capítulo vêm entre colchetes; no texto, «[PG 44, n]» marca a virada de coluna)'
    campos = {
        'Autor': 'São Gregório de Nissa (c. 335–c. 395)',
        'Obra': 'De opificio hominis (Sobre a criação do homem)',
        'Passagem': f'caps. {", ".join(str(n) for n in quais)}' + (' e a carta-prólogo a Pedro' if cap == 1 else ''),
        'Edição': ed,
        'Fonte': URL_OPIF,
        'Cobre': {1: 'vv. 26–28 sobretudo (o homem feito por último, «Façamos», a imagem, «homem e mulher», o domínio, «crescei»); '
                     'cap. 1 sobre o mundo pronto (Gn 1 e 2,1–4)',
                  2: 'Gn 2,7–9.16–17 (o pó e o sopro; o alimento e as árvores do paraíso)',
                  3: 'Gn 3 (o fruto comido), só no cap. 20'}.get(cap, ''),
        'Oriental': 'sim',
        'Língua': 'grc',
    }
    nota = ('Capítulos escolhidos pela leitura (tabela MAPA do script). As palavras partidas na quebra de linha do PDF foram '
            'coladas por heurística: conferir na leitura.')
    G.gravar(cap, 'nissa-de-opificio-hominis', 'São Gregório de Nissa, De opificio hominis', campos, '\n\n'.join(partes), nota, SCRIPT)


def apologia():
    t = G.texto_pdf(URL_APOL, 'nissa-apologia', colunas_pg=False, colunas_nuas=(44, 61, 124))
    campos = {
        'Autor': 'São Gregório de Nissa (c. 335–c. 395)',
        'Obra': 'Apologia in Hexaemeron (Explicação apologética do Hexaémeron, ao irmão Pedro)',
        'Passagem': 'a obra inteira',
        'Edição': 'PG 44, 61–124 («[PG 44, n]» marca a virada de coluna)',
        'Fonte': URL_APOL,
        'Cobre': 'vv. 1–25 (tudo criado de uma vez «em princípio»; a luz antes do sol; o firmamento e as águas de cima); '
                 'física antiga: pouco para o leitor comum',
        'Oriental': 'sim',
        'Língua': 'grc',
    }
    G.gravar(1, 'nissa-apologia-in-hexaemeron', 'São Gregório de Nissa, Apologia in Hexaemeron', campos, t, None, SCRIPT)


def main():
    caps_pedidos = G.capitulos()
    t, caps, prologo = opificio()
    print(f'  De opificio: {len(caps)} capítulos ({min(caps)}–{max(caps)})')
    for cap in caps_pedidos:
        gravar_opificio(cap, t, caps, prologo)
        if cap == 1:
            apologia()
        else:
            G.ausente(cap, 'São Gregório de Nissa, Apologia in Hexaemeron: só Gn 1.')
    G.registrar()


if __name__ == '__main__':
    main()
