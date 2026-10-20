"""Grava em base/ os trechos siríacos escolhidos (lista curada abaixo), e as pistas e ausências orientais.

    python -I -X utf8 pesquisa/ferramentas/base/ori-siriaco-gravar.py

Antes: ori-siriaco-buscar.py (gera cache/base/ori/siriaco-achados.tsv, de onde saem as pistas). Os trechos vêm do
Digital Syriac Corpus (TEI; texto siríaco de domínio público, edição digital CC BY 4.0). Cada item da lista ITENS diz
o texto (n.º do corpus), os blocos (linhas de poema ou parágrafos) e o capítulo. Para estender a outro capítulo:
rodar a busca, ler o contexto dos achados e acrescentar itens aqui. Os textos de cada autor que já viraram base/ ficam
fora das pistas do mesmo capítulo.
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_siriaco_comum as C

EFREM = 'Santo Efrém, o Sírio (c. 306–373), diácono de Nísibis e Edessa, Doutor da Igreja (1920)'
AFRAATES = 'Afraates, o Sábio Persa (c. 270–c. 345), bispo, o mais antigo Padre siríaco, venerado nas Igrejas siríacas'
JACO = ('São Jacó (Tiago) de Sarug (c. 451–521), bispo de Batnan, venerado como santo nas Igrejas siríacas '
        '(inclusive a maronita e a siro-católica)')
NARSAI = ('Narsai (c. 399–c. 502), mestre da escola de Nísibis, da Igreja do Oriente; louvou Diodoro, Teodoro e '
          'Nestório: escritor eclesiástico, usar com essa indicação e nunca em ponto cristológico')
LIBER = 'Liber Graduum (Livro dos Degraus), obra ascética siríaca anônima (séc. IV–V): escritor eclesiástico'
FILOXENO = ('Filoxeno de Mabug (c. 440–523), bispo miafisita, adversário de Calcedônia: escritor eclesiástico; '
            'só os textos ascéticos, com essa indicação')

ED = {
    'parisot': ('J. Parisot, Aphraatis Sapientis Persae Demonstrationes (Patrologia Syriaca I/1, Paris 1894), com tradução '
                'latina ao lado; archive.org/details/patrologiasyriac01graf'),
    'bedjan1': 'P. Bedjan, Homiliae selectae Mar-Jacobi Sarugensis, vol. I (Paris 1905); archive.org/details/homiliaeselectae01jaco',
    'budge': ('E. A. W. Budge, The Discourses of Philoxenus, Bishop of Mabbôgh, vol. I (Londres 1894), siríaco; '
              'tradução inglesa no vol. II; archive.org (buscar «discourses of philoxenus»)'),
    'mingana': 'A. Mingana, Narsai doctoris Syri homiliae et carmina, vol. I (Mossul 1905); archive.org/details/narsaihomiliaeetcarmina1',
    'narsai82': 'manuscrito (a transcrição do Digital Syriac Corpus indica os fólios); ed. impressa: Mingana II (1905), archive.org/details/MinganaNarsaiVol2',
    'kmosko': 'M. Kmosko, Liber Graduum (Patrologia Syriaca I/3, Paris 1926), siríaco e latim; archive.org/details/PatrologiaSyriacaIIILiberGraduum_201603',
    'beck_nat': ('E. Beck, Des heiligen Ephraem des Syrers Hymnen De Nativitate (CSCO 186, Lovaina 1959): edição moderna, '
                 'por isso só a estrofe; edição antiga de domínio público para conferir: Lamy, Hymni et sermones II (1886), '
                 'archive.org/details/sanctiephraemsy02lamygoog'),
    'beck_nis': ('E. Beck, Des heiligen Ephraem des Syrers Carmina Nisibena II (CSCO 240, Lovaina 1963): edição moderna, por '
                 'isso só as estrofes; edição antiga de domínio público, com latim: G. Bickell, S. Ephraemi Syri Carmina '
                 'Nisibena (Leipzig 1866), archive.org/details/carminanisibenaa00ephr'),
}

# (livro, cap, texto, primeiro bloco, último bloco, arquivo, autor, obra, passagem, edição, cobre)
ITENS = [
    ('numeros', 17, 549, 'sec:17', None, 'efrem-hinos-natividade.md', EFREM, 'Hinos sobre a Natividade (Madrashe ʿal Yalda), 1',
     'Hino 1, estrofe 17 (a vara de Aarão que floresce, Nm 17,23, figura da Virgem)', 'beck_nat', 'só a estrofe que retoma Nm 17,23'),
    ('numeros', 17, 293, 'sec:6', None, 'efrem-carmina-nisibena.md', EFREM, 'Hinos de Nísibis (Carmina Nisibena), 39',
     'Hino 39, estrofe 6 (fala a Morte: o turíbulo de Aarão entre os mortos e os vivos, Nm 17,11-13; a Cruz)', 'beck_nis',
     'só a estrofe que retoma Nm 17,11-13'),
    ('numeros', 20, 344, 0, None, 'jaco-sarug-sobre-aarao.md', JACO, 'Memra sobre Aarão, o sacerdote',
     'a morte de Aarão no monte Hor (Nm 20,22-29), memra inteiro', 'bedjan1', 'Nm 20,22-29, memra inteiro'),
    ('numeros', 20, 11, 'sec:9', None, 'afraates-demonstracoes.md', AFRAATES, 'Demonstrações (Taḥwyata), 11: Sobre a circuncisão',
     'Dem. 11, § 9 (Moisés e Edom, Nm 20,14-21)', 'parisot', 'só a seção que reconta Nm 20,14-21'),
    ('numeros', 21, 343, 0, None, 'jaco-sarug-serpente-de-bronze.md', JACO, 'Memra sobre a serpente de bronze que Moisés ergueu no deserto',
     'Nm 21,4-9 (e Jo 3,14), memra inteiro', 'bedjan1', 'Nm 21,4-9, memra inteiro'),
    ('numeros', 21, 82, 0, None, 'narsai-serpente-de-bronze.md', NARSAI, 'Memra sobre a serpente de bronze',
     'Nm 21,4-9, memra inteiro', 'narsai82', 'Nm 21,4-9, memra inteiro'),
    ('numeros', 24, 549, 'sec:4', 'sec:6', 'efrem-hinos-natividade.md', EFREM, 'Hinos sobre a Natividade (Madrashe ʿal Yalda), 1',
     'Hino 1, estrofes 4–6 (a estrela de Jacó, Nm 24,17: «a profecia que Balaão falou, hoje é a sua interpretação»)', 'beck_nat',
     'só as estrofes que retomam Nm 24,17'),
    ('numeros', 24, 345, 262, 290, 'jaco-sarug-sobre-a-estrela.md', JACO, 'Memra sobre a estrela que os magos viram',
     'Bedjan I, pp. 96–97: os magos acham nos seus livros a profecia de Balaão (Nm 24,17)', 'bedjan1',
     'só o trecho sobre Nm 24,17 (o memra inteiro é sobre Mt 2)'),
    ('numeros', 25, 293, 'sec:5', 'sec:7', 'efrem-carmina-nisibena.md', EFREM, 'Hinos de Nísibis (Carmina Nisibena), 39',
     'Hino 39, estrofes 5–7 (fala a Morte: a lança de Fineias, Zambri e Cozbi, a praga detida, Nm 25,6-9; o turíbulo de Aarão; a lança de Cristo)',
     'beck_nis', 'só as estrofes que retomam Nm 25,6-9'),
    ('numeros', 25, 4, 'sec:14', None, 'afraates-demonstracoes.md', AFRAATES, 'Demonstrações (Taḥwyata), 4: Sobre a oração',
     'Dem. 4, § 14 (o zelo de Fineias contado como oração, Nm 25,7-13 e Sl 106,30-31)', 'parisot', 'só a seção sobre Nm 25,7-13'),
    ('numeros', 25, 377, 23, 26, 'filoxeno-discursos.md', FILOXENO, 'Discursos sobre a vida cristã, 4: Sobre a fé e a simplicidade',
     'Discurso 4 (só caíram em Baal-Fegor os nascidos no Egito, Nm 25,1-9; 26,64-65)', 'budge', 'só o trecho sobre Nm 25'),
    ('salmos', 38, 380, 23, 23, 'filoxeno-discursos.md', FILOXENO, 'Discursos sobre a vida cristã, 7: Sobre o temor de Deus',
     'Discurso 7: o temor de Deus nas palavras de Davi (Sl 38,4-15 e 39,3-13 da Peshitta, em sequência)', 'budge',
     'só citações dos vv. 4–14, numa reflexão sobre o temor de Deus'),
    ('salmos', 39, 380, 23, 23, 'filoxeno-discursos.md', FILOXENO, 'Discursos sobre a vida cristã, 7: Sobre o temor de Deus',
     'Discurso 7: o temor de Deus nas palavras de Davi (Sl 38 e 39 da Peshitta, em sequência)', 'budge',
     'só citações dos vv. 3–4 e 10–12 (o mesmo parágrafo está em salmos/038)'),
    ('salmos', 41, 20, 'sec:4', None, 'afraates-demonstracoes.md', AFRAATES, 'Demonstrações (Taḥwyata), 20: Sobre o cuidado dos pobres',
     'Dem. 20, § 4 (Davi e a aliança com os pobres: Sl 41,2-4)', 'parisot', 'só a seção sobre os vv. 2–4'),
    ('salmos', 45, 87, 156, 190, 'narsai-dedicacao-da-igreja.md', NARSAI, 'Memra sobre a dedicação da Igreja',
     'Mingana I, pp. 161–162: a Igreja, filha do rei à direita do Esposo (Sl 45,10-15)', 'mingana', 'só o trecho sobre os vv. 10–15'),
    ('salmos', 50, 15, 'sec:7', None, 'afraates-demonstracoes.md', AFRAATES, 'Demonstrações (Taḥwyata), 15: Sobre a distinção dos alimentos',
     'Dem. 15, § 7 (Deus não come carne de touros: Sl 50,13-15)', 'parisot', 'só a seção sobre os vv. 13–15'),
    ('salmos', 50, 2, 'sec:6', None, 'afraates-demonstracoes.md', AFRAATES, 'Demonstrações (Taḥwyata), 2: Sobre o amor',
     'Dem. 2, § 6 (os sacrifícios rejeitados antes de Cristo: Sl 50,13-14)', 'parisot', 'só a seção sobre os vv. 13–14'),
    ('salmos', 50, 374, 3, 3, 'filoxeno-discursos.md', FILOXENO, 'Discursos sobre a vida cristã, 1: Prólogo',
     'Discurso 1 («Que tens tu a ver com o meu livro?»: Sl 50,16-17, ouvir e fazer)', 'budge', 'só o parágrafo sobre os vv. 16–17'),
    ('2corintios', 3, 201, 'sec:2', None, 'liber-graduum.md', LIBER, 'Memra 14: Sobre os justos e os perfeitos',
     'Memra 14, § 2 (os perfeitos andam «de glória em glória» no Espírito e veem o Senhor «como num espelho», no coração: 2Cor 3,18)',
     'kmosko', 'só a seção que retoma 3,18'),
]


def blocos_de(blocos, ini, fim):
    if isinstance(ini, str):
        s0 = ini.split(':')[1]; s1 = (fim or ini).split(':')[1]
        secs = [b[3] for b in blocos]
        ordem = []
        for s in secs:
            if s not in ordem:
                ordem.append(s)
        dentro = ordem[ordem.index(s0):ordem.index(s1) + 1]
        return [i for i, b in enumerate(blocos) if b[3] in dentro]
    fim = len(blocos) - 1 if fim is None else fim
    return list(range(ini, fim + 1))


def texto(blocos, idx):
    out, pag, sec = [], None, None
    for i in idx:
        p, tipo, tx, s = blocos[i]
        if s and s != sec:
            out.append(f'\n§ {s}\n' if tipo == 'p' else f'\n[estrofe {s}]')
            sec = s
        if p and p != pag:
            out.append(f'[p. {p}]')
            pag = p
        if tx and not re.fullmatch(r'\d+', tx):
            out.append(tx)
    return '\n'.join(out).strip()


def main():
    juntos = collections.OrderedDict()
    for (livro, cap, n, ini, fim, arq, autor, obra, pas, ed, cobre) in ITENS:
        meta, blocos = C.ler_tei(n)
        idx = blocos_de(blocos, ini, fim)
        corpo = texto(blocos, idx)
        ch = (livro, cap, arq)
        juntos.setdefault(ch, []).append(dict(n=n, autor=autor, obra=obra, pas=pas, ed=ED[ed], cobre=cobre, corpo=corpo,
                                             titulo_corpus=meta['titulo'].split(' - ')[0]))
    for (livro, cap, arq), itens in juntos.items():
        a = itens[0]
        obras = '; '.join(dict.fromkeys(i['obra'] for i in itens))
        campos = {
            'Autor': a['autor'],
            'Obra': obras,
            'Passagem': ' | '.join(i['pas'] for i in itens),
            'Edição': '; '.join(dict.fromkeys(i['ed'] for i in itens)),
            'Fonte': ' ; '.join(f"https://syriaccorpus.org/{i['n']}" for i in itens),
            'Cobre': ' | '.join(i['cobre'] for i in itens),
            'Língua': 'syr',
        }
        corpo = []
        for i in itens:
            if len(itens) > 1:
                corpo.append(f"## {i['obra']} — {i['pas']}\n\nFonte: https://syriaccorpus.org/{i['n']} ({i['titulo_corpus']})\n")
            corpo.append(i['corpo'] + '\n')
        nome = 'São Jacó de Sarug' if a['autor'] == JACO else ('Liber Graduum' if a['autor'] == LIBER else a['autor'].split(' (')[0])
        nota = ('Texto siríaco da edição digital do Digital Syriac Corpus (CC BY 4.0; texto de base em domínio público): '
                'citar a fonte. [p. N] = página (ou fólio) da edição/manuscrito indicado no TEI; § = seção; '
                '[estrofe N] = estrofe do hino.')
        p = C.gravar(livro, cap, arq, f'{nome}, {obras}', campos, '\n'.join(corpo), nota=nota, script='ori-siriaco-gravar.py')
        print('gravado', os.path.relpath(p, C.RAIZ))
    base = collections.defaultdict(set)
    for (livro, cap, n, *_r) in ITENS:
        base[(livro, cap)].add(n)
    for c in range(17, 37):
        base[('numeros', c)].add(231)  # Dionísio (ori-siriaco-dionisio.py)
    for c in range(37, 61):
        base[('salmos', c)].add(238)
    pistas(base)


# --- pistas -----------------------------------------------------------------------------------------------
NOMES = {
    'Ephrem the Syrian': 'Santo Efrém', 'Aphrahat': 'Afraates', 'Jacob of Serugh': 'Jacó de Sarug', 'Narsai': 'Narsai',
    'Isaac of Nineveh': 'Isaac de Nínive', 'Philoxenos of Mabbug': 'Filoxeno de Mabug', 'Liber Graduum': 'Liber Graduum',
    'Dionysius bar Salibi': 'Dionísio bar Salibi', 'Timothy II': 'Timóteo II (católico da Igreja do Oriente, séc. XIV)',
    'Ishoʿyahb III of Adiabene': 'Ishoʿyahb III (católico da Igreja do Oriente, séc. VII)', 'Titus of Bostra': 'Tito de Bostra (versão siríaca)',
    'John the Solitary': 'João, o Solitário (de Apameia)', 'Abraham of Nathpar': 'Abraão de Nathpar (monge da Igreja do Oriente)',
    'Moshe bar Kepha': 'Moisés bar Kepha (siro-ortodoxo, séc. IX)', 'Joseph Hazzaya': 'José Hazzaya (Igreja do Oriente, séc. VIII; escritos condenados pelo católico Timóteo I)',
    'Thomas of Edessa': 'Tomás de Edessa (Igreja do Oriente)', 'Rabbula of Edessa': 'Rábula de Edessa', 'Papa bar Aggai': 'Papa bar Aggai (carta apócrifa)',
}
FORA = ('Barlaha', 'Gregorius bar Hebraeus')  # cartas sobre a tradução do Saltério (citam títulos) e a História eclesiástica
LIVRO = {'nm': 'numeros', 'sl': 'salmos', '2cor': '2corintios'}
ISHODAD_2COR = {3: '3696–3821 (II Cor. II.16–IV.4 e seguinte)', 4: '3696–3821', 5: '3821–3877 (II Cor. V.2–VI.7)',
                6: '3821–3932 (II Cor. V.2–VIII.2)', 7: '3877–3932 (II Cor. VI.7–VIII.2)', 8: '3877–3992',
                9: '3932–3992 (II Cor. VIII.6–IX.6 e seguinte)', 10: '3992–4048 (II Cor. X.1–XI.25)', 11: '3992–4101',
                12: '4048–4210 (II Cor. XI.25–XIII.4)', 13: '4158–4210 (II Cor. XII.7–XIII.4 e seguinte)'}
FIXAS = {
    'nm': [
        '- Isho`dad de Merv (c. 850, Igreja do Oriente, seguidor de Teodoro de Mopsuéstia), Comentário a Números: só na ed. '
        'Vosté–Van den Eynde (CSCO 156, Syr. 67, 1955), com direito: só pista, não baixado.',
        '- Teodoro bar Koni (séc. VIII, Igreja do Oriente), Liber scholiorum, mimrā sobre o Pentateuco: ed. Scher (CSCO 55, 1910), '
        'domínio público, https://archive.org/details/liberscholiorumt00theo (OCR siríaco ilegível: ler na imagem). Só pista.',
        '- Jacó de Sarug: o Digital Syriac Corpus tem só 39 dos ~195 memre de Bedjan; conferir o índice dos vols. II–V '
        '(https://archive.org/details/homiliaeselectae02jaco … 05jaco) para outro memra sobre o episódio. Não conferido.',
    ],
    'sl': [
        '- Isho`dad de Merv, Comentário aos Salmos: ed. Van den Eynde (CSCO 433–434, 1981), com direito: só pista.',
        '- Daniel de Salah (séc. VI, miafisita), comentário aos Salmos: em grande parte inédito; ed. parcial moderna (CSCO), com direito: só pista.',
    ],
    '2cor': [
        '- Isho`dad de Merv (c. 850, Igreja do Oriente, seguidor de Teodoro de Mopsuéstia: SÓ PISTA), comentário a 2 Coríntios: '
        'ed. M. D. Gibson, The Commentaries of Isho`dad of Merv V (Cambridge 1916), domínio público; inglês em '
        'https://archive.org/details/commentariesofis0005isho_h2o7 (no `_djvu.txt`, linhas {L}); siríaco em '
        'https://archive.org/details/commentariesofis0005isho (cabeçalhos «II CORINTHIANS»).',
    ],
}


def pistas(base_por_cap):
    tsv = os.path.join(C.CACHE, 'ori', 'siriaco-achados.tsv')
    linhas = [l.rstrip('\n').split('\t') for l in open(tsv, encoding='utf-8')]
    grupos = collections.defaultdict(lambda: collections.defaultdict(lambda: {'vs': set(), 'locs': set(), 'titulo': '', 'autor': ''}))
    for n, autor, titulo, ref, pag, sec, ib, ng in linhas:
        if autor in FORA:
            continue
        livro, cv = ref.split(' ')
        c, v = (int(x) for x in cv.split(','))
        if int(n) in base_por_cap.get((LIVRO[livro], c), set()):
            continue
        g = grupos[(livro, c)][int(n)]
        g['vs'].add(v); g['titulo'] = titulo.split(' - ')[0]; g['autor'] = autor
        g['locs'].add(f'p. {pag}' if pag else (f'§ {sec}' if sec else f'bloco {ib}'))
    caps = set(grupos) | {(k, c) for k, (i, j) in (('nm', (17, 25)), ('sl', (37, 50)), ('2cor', (3, 7))) for c in range(i, j + 1)}
    for livro, c in sorted(caps):
        out = [f'# Pistas orientais (siríacas): {LIVRO[livro]} {c}', '',
               'Citações achadas pela Peshitta no Digital Syriac Corpus (ori-siriaco-buscar.py), ainda não lidas; conferir',
               'cada uma (achado automático: 3–4 palavras seguidas; pode ser coincidência). Depois, fontes fora do corpus.', '']
        for n, g in sorted(grupos.get((livro, c), {}).items(), key=lambda x: -len(x[1]['vs'])):
            nome = NOMES.get(g['autor'], g['autor'])
            locs = ', '.join(sorted(g['locs']))[:80]
            out.append(f"- {nome}, {g['titulo']} ({locs}): v. {', '.join(map(str, sorted(g['vs'])))} — https://syriaccorpus.org/{n}")
        for f in FIXAS[livro]:
            out.append(f.replace('{L}', ISHODAD_2COR.get(c, '?')))
        pasta = os.path.join(C.RAIZ, LIVRO[livro], f'{c:03d}', 'base')
        os.makedirs(pasta, exist_ok=True)
        with open(os.path.join(pasta, '_pistas-orientais.md'), 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(out) + '\n')
    print('pistas gravadas em', len(caps), 'capítulos')


if __name__ == '__main__':
    main()
