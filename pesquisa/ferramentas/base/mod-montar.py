"""Monta, para cada salmo (hebraico) de 1 a 150 menos 33–36, os arquivos de base/ das fontes MODERNAS:

    python -I -X utf8 pesquisa/ferramentas/base/mod-montar.py            # todos
    python -I -X utf8 pesquisa/ferramentas/base/mod-montar.py 23 130     # só estes

Saída em pesquisa/salmos/<ccc>/base/:
  liturgia.md            onde o salmo é rezado (Liturgia das Horas, Lecionário, Missal e Breviário antigos)
  _pistas-modernos.md    audiências e documentos papais que o comentam (só pistas, com URL) e parágrafos do Catecismo
  _ausentes-modernos.md  o que se conferiu que não existe
(afonso-salmi.md vem de mod-afonso-salmi.py.) Pré-requisitos, nesta ordem:
  mod-papas.py baixar / baixar-docs / analisar;  mod-catecismo.py baixar / indice;  mod-liturgia.py baixar / construir.
"""
import json, os, re, sys, time

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
MOD = os.path.join(RAIZ, 'cache', 'base', 'modernos')
SCRIPT = 'pesquisa/ferramentas/base/mod-montar.py (dados de mod-papas.py, mod-catecismo.py, mod-liturgia.py)'
HOJE = time.strftime('%Y-%m-%d')
EXCLUIDOS = (33, 34, 35, 36)
NOME = {'john-paul-ii': 'São João Paulo II', 'benedict-xvi': 'Bento XVI', 'francesco': 'Papa Francisco', 'leo-xiv': 'Leão XIV'}
TIPO = {'audiences': 'audiência', 'encyclicals': 'encíclica', 'apost_exhortations': 'exortação apostólica',
        'apost_letters': 'carta apostólica'}
CCC_BASE = 'https://www.vatican.va/archive/cathechism_po/index_new/'


def carrega(p):
    return json.load(open(os.path.join(MOD, p), encoding='utf-8'))


def vulgata_de(h):
    if h <= 8 or h >= 148:
        return [h]
    if h in (9, 10):
        return [9]
    if h == 116:
        return [114, 115]
    if h in (114, 115):
        return [113]
    if h == 147:
        return [146, 147]
    return [h - 1]


def limpa_titulo(t):
    t = t or ''
    t = re.sub(r'\b(PAPA|Video|ZH_TW|La Santa Sede)\b', '', t)
    t = re.sub(r'\[\s*(Multimedia)?\s*\]|_{3,}', '', t)
    if 'Il testo qui di seguito' in t or 'Il Santo Padre non ha potuto' in t:
        return ''
    t = re.sub(r'\s+', ' ', t).strip(' "-:')
    if len(t) > 130:
        t = t[:127].rsplit(' ', 1)[0] + '…'
    return t


def arquivo_ccc(par, arquivos):
    for a in arquivos:
        m = re.search(r'_(\d+)-(\d+)_po', a)
        if m and int(m.group(1)) <= par <= int(m.group(2)):
            return a
    return ''


def cab_arquivo(h, cobre):
    vul = vulgata_de(h)
    v = ' e '.join(str(x) for x in vul)
    return [
        '- Autor: Liturgia da Igreja',
        '- Obra: Usos litúrgicos do salmo (Liturgia das Horas, Lecionário da Missa, Missal e Breviário antigos)',
        '- Passagem: Sl %d (hebraico) = Sl %s (Vulgata)' % (h, v),
        '- Edição: Liturgia das Horas (1971, saltério de quatro semanas); Ordo Lectionum Missae (1981); Missale Romanum e Breviarium Romanum até 1962',
        '- Fonte: https://catholic-resources.org/LoH/Psalter-Index.html ; https://catholic-resources.org/Lectionary/ ; https://github.com/DivinumOfficium/divinum-officium',
        '- Cobre: ' + cobre,
        '- Oriental: não',
        '- Língua: pt/la',
        '- Baixado: %s, por pesquisa/ferramentas/base/mod-liturgia.py e mod-montar.py' % HOJE,
    ]


def refs_lh(it):
    t = it['trecho'].strip()
    if not t:
        return ''
    if t.startswith(':'):
        return ' (vv. ' + t[1:].strip() + ')'
    return ' (' + t + ')'


def incipit(txt, n=11):
    ps = re.sub(r'\s+', ' ', txt).strip().split(' ')
    return ' '.join(ps[:n]) + ('…' if len(ps) > n else '')


def montar_liturgia(h, L):
    vul = vulgata_de(h)
    linhas = ['# Liturgia da Igreja, Usos litúrgicos do salmo']
    cab = cab_arquivo(h, 'onde o salmo é rezado: saltério de quatro semanas, salmo responsorial da Missa, propers do Missal e saltério do Breviário até 1962')
    linhas += cab + ['']
    linhas += ['Itens marcados «a confirmar» não foram conferidos. A numeração dos itens do Missal e do Breviário antigos é a da Vulgata',
               '(os versículos do Divinum Officium contam o título); a do saltério de quatro semanas e do Lecionário é a hebraica.', '']
    # --- Liturgia das Horas
    linhas += ['## Liturgia das Horas (1971, saltério de quatro semanas)', '']
    lh = L['lh']
    if not lh:
        linhas += ['- Não consta do índice do saltério de Felix Just. a confirmar.', '']
    for it in lh:
        if 'omitido' in it['lugar']:
            linhas.append('- **Omitido da Liturgia das Horas** (salmo imprecatório; também fora do saltério: Sl 58, 83 e 109).')
        else:
            linhas.append('- %s%s.' % (it['lugar'][0].upper() + it['lugar'][1:], refs_lh(it)))
    if lh and not any('omitido' in x['lugar'] for x in lh):
        linhas += ['', 'Antífonas latinas da *Liturgia Horarum*: a confirmar (sem fonte aberta que se consiga raspar; ver `_mapa-modernos.md`).']
    linhas.append('')
    # --- Lecionário
    linhas += ['## Missa: salmo responsorial (Lecionário, Ordo Lectionum Missae de 1981)', '']
    lect = L['lect']
    if not lect:
        linhas += ['- Não é salmo responsorial de nenhuma Missa dominical, solene ou ferial nas tabelas conferidas. a confirmar para a Vigília Pascal e as Missas rituais.', '']
    grupos = {}
    for it in lect:
        grupos.setdefault(it['grupo'], []).append(it)
    for g, lst in grupos.items():
        linhas += ['**%s**' % g, '']
        vistos = set()
        for it in lst:
            k = (it['celebracao'], it['versos'])
            if k in vistos:
                continue
            vistos.add(k)
            olm = ' (OLM %s)' % it['olm'] if it['olm'] else ''
            vv = ', vv. ' + it['versos'] if it['versos'] else ''
            linhas.append('- %s%s: Sl %d%s' % (it['celebracao'], olm, h, vv))
        linhas.append('')
    if lect:
        linhas += ['Refrão (versículo-refrão do Lecionário, em latim e na tradução da CNBB): a confirmar; o Lecionário da CNBB tem direito autoral (só citação curta).', '']
    # --- Missal antigo
    linhas += ['## Missal romano antigo (até 1962): intróito, gradual, tracto, ofertório, comunhão', '']
    ms = L['missa']
    if not ms:
        linhas += ['- Nenhum uso nos propers do Missal de 1962 (Divinum Officium, pastas Tempora, Sancti e Commune).', '']
    for it in ms:
        txt = incipit(it['texto']) if it['texto'] else ''
        linhas.append('- %s [%s]: %s, Sl %d da Vulgata, vv. %s%s' % (it['titulo'], it['arquivo'], it['parte'], it['vulg'], it['versos'],
                                                                  (': «' + txt + '»') if txt else ''))
    if ms:
        linhas.append('')
    # --- Breviário antigo
    linhas += ['## Breviário romano antigo (Pio V, 1568; Pio X, 1911): onde o salmo cai na semana', '']
    of = L['oficio']
    extras = []
    if h == 95:
        extras.append('Invitatório de todas as Matinas, todos os dias (Sl 94 da Vulgata, *Venite, exsultemus*), no Breviário de Pio V e no de Pio X; na Liturgia das Horas, o invitatório ordinário.')
    if not of and not extras:
        linhas += ['- Não consta na distribuição semanal do Divinum Officium. a confirmar (pode aparecer nos próprios de santos e do Tempo).', '']
    for e in extras:
        linhas.append('- ' + e)
    ordem = {'Pio V (Tridentino)': 0, 'Pio X (1911)': 1}
    of = sorted(of, key=lambda x: (ordem.get(x['saltério'], 2), ))
    for it in of:
        tr = ' (vv. %s)' % it['trecho'] if it['trecho'] else ''
        ant = ' Antífona: «%s»' % it['antifona'].replace(' * ', ' ') if it['antifona'] else ''
        if it['antifona'] and it['saltério'].startswith('Pio V') and it['hora'].startswith('Matinas'):
            ant = ''
        linhas.append('- %s: %s, %s%s.%s' % (it['saltério'], it['hora'], it['dia'], tr, ant))
    linhas += ['', 'Antífonas das Matinas do Breviário de Pio V: ver as do Divinum Officium (`Psalterium/Psalmi/Psalmi matutinum.txt`) ou a *Traduzione* de Afonso (`base/afonso-salmi.md`, que traz o dia e o noturno). Próprios de santos e do Tempo no Ofício: não varridos.']
    return '\n'.join(linhas) + '\n'


def monta_papas(h, papas):
    ciclo, outros = [], []
    for d in papas:
        if not d.get('texto_ok', True):
            continue
        if h in d['ciclo_salmos']:
            ciclo.append(d)
        elif d['cita'].get(str(h), 0) >= 3 and not d['ciclo_salmos']:
            outros.append(d)
        elif d['cita'].get(str(h), 0) >= 3 and d['ciclo_salmos'] and h not in d['ciclo_salmos']:
            outros.append(d)
    return ciclo, outros


def montar_pistas(h, papas, ccc_ind, ccc_arqs, vd):
    vul = vulgata_de(h)
    ciclo, outros = monta_papas(h, papas)
    L = ['# Pistas modernas: Sl %d (hebraico) = Sl %s (Vulgata)' % (h, ' e '.join(str(x) for x in vul)), '',
         'Textos com direito autoral (Libreria Editrice Vaticana): não guardados, só o endereço. Todos os endereços abriam em %s.' % HOJE, '']
    L += ['## Catequeses do ciclo sobre os salmos e cânticos de Laudes e Vésperas (2001–2006)', '']
    if ciclo:
        for d in ciclo:
            lei = (' (leitura: %s)' % d['leitura']) if d['leitura'] else ''
            L.append('- %s, audiência geral de %s, «%s»%s: catequese dedicada a este salmo, no ciclo de Laudes e Vésperas '
                     '(o documento usa a numeração da Vulgata; título e texto em italiano, original). %s'
                     % (NOME[d['papa']], d['data'], limpa_titulo(d['titulo']), lei, d['url']))
    else:
        L.append('- Nenhuma. (ver `_ausentes-modernos.md`)')
    L += ['', '## Outras audiências e documentos que comentam o salmo (citam-no 3 vezes ou mais)', '']
    if outros:
        outros.sort(key=lambda d: (-d['cita'].get(str(h), 0), d['data']))
        for d in outros[:25]:
            t = limpa_titulo(d['titulo'])
            L.append('- %s, %s de %s%s: cita o Sl %d %d vezes (comenta-o ou se apoia nele). %s'
                     % (NOME[d['papa']], TIPO.get(d.get('tipo', 'audiences'), 'documento'), d['data'],
                        (' «' + t + '»') if t else '', h, d['cita'][str(h)], d['url']))
        if len(outros) > 25:
            L.append('- … e mais %d documentos com 3 ou mais citações (ver `cache/base/modernos/papas/indice.json`).' % (len(outros) - 25))
    else:
        L.append('- Nenhum encontrado. (ver `_ausentes-modernos.md`)')
    # Catecismo
    L += ['', '## Catecismo da Igreja Católica (parágrafos que citam o salmo)', '']
    cit = ccc_ind.get(str(h), [])
    if cit:
        vistos = set()
        for c in sorted(cit, key=lambda c: (c['par'], c['ver'])):
            k = (c['par'], c['ver'])
            if k in vistos:
                continue
            vistos.add(k)
            arq = arquivo_ccc(c['par'], ccc_arqs)
            como = 'nota de rodapé' if c['via'] == 'nota' else 'no próprio texto'
            vv = ', v. ' + c['ver'] if c['ver'] else ''
            L.append('- § %d: Sl %d%s (%s). %s%s' % (c['par'], h, vv, como, CCC_BASE, arq))
    else:
        L.append('- Nenhum. (ver `_ausentes-modernos.md`)')
    return '\n'.join(L) + '\n', ciclo, outros, cit


def montar_ausentes(h, ciclo, outros, cit, L, tem_afonso):
    out = ['# Ausentes (fontes modernas): Sl %d' % h, '']
    if not ciclo:
        out.append('- Nenhuma catequese de São João Paulo II ou Bento XVI no ciclo sobre os salmos e cânticos de Laudes e Vésperas (28/03/2001 a 15/02/2006) trata este salmo: conferidos os títulos e as leituras («Lettura: Sal …») de todas as audiências gerais de 2001 a 2006 nos índices anuais de vatican.va.')
    if not outros:
        out.append('- Nenhuma audiência geral de São João Paulo II (2001–2005), Bento XVI (2005–2013), Francisco (2013–2025) ou Leão XIV (2025–2026), nem encíclica, exortação ou carta apostólica desses Papas, cita este salmo 3 vezes ou mais (contagem por «Sal/Salmo N» no texto italiano). Não varridos: audiências de João Paulo II de 1978 a 2000, Angelus, homilias, mensagens e discursos.')
    if not cit:
        out.append('- Nenhum parágrafo do Catecismo da Igreja Católica cita este salmo (lidas as notas e o texto dos 28 arquivos em português europeu de vatican.va).')
    if not L['lect']:
        out.append('- Não é salmo responsorial de domingo, solenidade ou dia de semana nas tabelas de Felix Just (Lecionário de 1981).')
    if any('omitido' in x['lugar'] for x in L['lh']):
        out.append('- A Liturgia das Horas omite este salmo (salmo imprecatório).')
    if not L['missa']:
        out.append('- Nenhum uso nos propers do Missal de 1962 (intróito, gradual, tracto, ofertório, comunhão) no Divinum Officium.')
    if not tem_afonso:
        out.append('- Santo Afonso: sem texto (ver mod-afonso-salmi.py).')
    if len(out) == 2:
        out.append('- (nada a registrar: todas as fontes modernas trazem algo)')
    return '\n'.join(out) + '\n'


def main(alvos):
    papas = carrega('papas/indice.json')
    for d in papas:
        d['texto_ok'] = True
    ccc = carrega('catecismo/indice.json')
    arqs = sorted(f for f in os.listdir(os.path.join(MOD, 'catecismo')) if f.endswith('_po.html'))
    lit = carrega('liturgia.json')
    n = 0
    for h in alvos:
        if h in EXCLUIDOS:
            continue
        d = os.path.join(RAIZ, 'salmos', '%03d' % h, 'base')
        os.makedirs(d, exist_ok=True)
        L = lit[str(h)]
        open(os.path.join(d, 'liturgia.md'), 'w', encoding='utf-8', newline='\n').write(montar_liturgia(h, L))
        pistas, ciclo, outros, cit = montar_pistas(h, papas, ccc, arqs, None)
        open(os.path.join(d, '_pistas-modernos.md'), 'w', encoding='utf-8', newline='\n').write(pistas)
        tem_afonso = os.path.exists(os.path.join(d, 'afonso-salmi.md'))
        open(os.path.join(d, '_ausentes-modernos.md'), 'w', encoding='utf-8', newline='\n').write(
            montar_ausentes(h, ciclo, outros, cit, L, tem_afonso))
        n += 1
    print('montados:', n)


if __name__ == '__main__':
    alvos = [int(x) for x in sys.argv[1:]] or list(range(1, 151))
    main(alvos)
