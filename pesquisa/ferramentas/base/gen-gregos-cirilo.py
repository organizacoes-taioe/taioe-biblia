"""São Cirilo de Alexandria, Glaphyra in Genesim (Glaphyra in Pentateuchum, livros I–VII; PG 69, 13–385), por capítulo.

    python3 -I pesquisa/ferramentas/base/gen-gregos-cirilo.py [capítulos]      (padrão: 1; ex.: 1-50)

Baixa UMA vez o PDF da khazarzar «Cyril of Alexandria_PG 68-77/Glaphyra in Pentateuchum.pdf» (texto da PG; «69.29»
-> «[PG 69, 29]»; o PDF é apagado depois da conversão) e grava genesis/<ccc>/base/cirilo-glaphyra-in-genesim.md.

A obra não comenta versículo por versículo: são episódios lidos como figura de Cristo, cada um com título («Περὶ τοῦ
Ἀδάμ», «Περὶ τοῦ Νῶε καὶ τῆς κιβωτοῦ»…). O script acha no corpo os títulos do índice inicial (só os do Gênesis, até
«Περὶ τῆς Μωσέως ὀπτασίας», que já é Êxodo) e dá a cada seção os capítulos que ela cita (grupos de 4 palavras em comum
com a LXX de Rahlfs; capítulos com pelo menos 3 grupos e 15% do mais citado). O índice não lista o «Περὶ τοῦ Ἀδάμ» (livro I),
que cita Gn 1,26–28 e trata de Gn 2–3; títulos do corpo que diferem do índice («τοῦ Χάμ», «Περὶ τοῦ πύργου») não são achados,
e o texto deles fica na seção anterior (Noé: Gn 6–11).
"""
import os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

SCRIPT = os.path.basename(__file__)
URL = G.khz('Cyril of Alexandria_PG 68-77', 'Glaphyra in Pentateuchum.pdf')


def secoes():
    t = G.texto_pdf(URL, 'cirilo-glaphyra-pentateuchum')
    t = unicodedata.normalize('NFC', t)
    fim_ind = t.find('Περὶ τῆς Μωσέως ὀπτασίας')
    titulos = re.findall(r'Περὶ [^.;]{3,90}\.', t[:fim_ind])
    titulos.insert(0, 'Περὶ τοῦ Ἀδάμ.')          # o índice não o lista (o livro I abre com o prólogo «Ὅτι διὰ πάσης…»)
    sem = lambda s: re.sub(r'[^α-ω]', '', G.sem_acento(s))
    corpo_ini = fim_ind + 40
    tt = G.sem_acento(t)
    # texto só com letras gregas (sem espaços nem pontuação) e o mapa de volta às posições do original
    mapa = [i for i, ch in enumerate(tt) if 'α' <= ch <= 'ω']
    tt_sem = ''.join(tt[i] for i in mapa)
    pos, de = [], next(k for k, i in enumerate(mapa) if i >= corpo_ini)
    for tit in titulos:
        k = tt_sem.find(sem(tit), de)
        if k < 0:
            continue
        pos.append((tit.strip(), mapa[k]))
        de = k + 1
    fim_gen = t.find('Περὶ τῆς Μωσέως ὀπτασίας', corpo_ini)
    out = []
    for j, (tit, a) in enumerate(pos):
        b = pos[j + 1][1] if j + 1 < len(pos) else fim_gen
        out.append((tit, a, b))
    return t, out


def main():
    caps_pedidos = G.capitulos()
    t, secs = secoes()
    por_cap = {}
    for tit, a, b in secs:
        cont = G.capitulos_citados(t[a:b])
        if not cont:
            continue
        mx = max(cont.values())
        cs = sorted(c for c, n in cont.items() if n >= 3 and n >= 0.15 * mx)
        for c in cs:
            por_cap.setdefault(c, []).append((tit, a, b))
        print(f'  {tit[:50]:50s} -> Gn {cs}')
    for cap in caps_pedidos:
        lst = por_cap.get(cap)
        if not lst:
            G.ausente(cap, f'São Cirilo de Alexandria, Glaphyra in Genesim: nenhuma seção sobre Gn {cap}'
                      + (' (o «Περὶ τοῦ Ἀδάμ» começa no paraíso, Gn 2–3).' if cap == 1 else '.'))
            continue
        partes = [f'## {tit} ({G.colunas(t, a, b, 69)})\n\n' + G.paragrafos(t[a:b]) for tit, a, b in lst]
        campos = {
            'Autor': 'São Cirilo de Alexandria (c. 376–444)',
            'Obra': 'Glaphyra in Genesim (Glaphyra in Pentateuchum, livros I–VII)',
            'Passagem': '; '.join(tit for tit, a, b in lst),
            'Edição': 'PG 69, 13–385 («[PG 69, n]» marca a virada de coluna)',
            'Fonte': URL,
            'Cobre': 'as seções que citam este capítulo (corte automático pelas citações da LXX: conferir)',
            'Oriental': 'sim',
            'Língua': 'grc',
        }
        G.gravar(cap, 'cirilo-glaphyra-in-genesim', 'São Cirilo de Alexandria, Glaphyra in Genesim', campos, '\n\n'.join(partes),
                 'Seções inteiras (uma seção cobre vários capítulos e pode repetir-se em mais de um arquivo).', SCRIPT)
    G.registrar()


if __name__ == '__main__':
    main()
