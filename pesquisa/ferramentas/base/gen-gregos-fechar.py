"""Junta as listas de ausentes e de pistas que os scripts gen-gregos-*.py guardaram (pesquisa/cache/genesis/gregos/extras/*.json)
em genesis/<ccc>/base/_ausentes-gregos.md e _pistas-gregos.md.

    python3 -I pesquisa/ferramentas/base/gen-gregos-fechar.py [capítulos]      (padrão: os que aparecem nos .json)

Rodar depois dos outros (gen-gregos-basilio, -nissa, -crisostomo, -teodoreto, -cirilo, -teofilo, -origenes, -damasceno,
-severiano). A parte automática fica entre os marcadores «<!-- automático -->» e «<!-- fim do automático -->»; o que a pesquisa
do capítulo escreveu à mão no arquivo, fora dos marcadores, é mantido.
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_gregos as G

INI, FIM = '<!-- automático -->', '<!-- fim do automático -->'


def main():
    dados = {'ausentes': {}, 'pistas': {}}
    for p in sorted(glob.glob(os.path.join(G.CACHE, 'extras', '*.json'))):
        d = json.load(open(p, encoding='utf-8'))
        for tipo in dados:
            for cap, linhas in d.get(tipo, {}).items():
                dados[tipo].setdefault(int(cap), []).extend(linhas)
    caps = G.capitulos() if len(sys.argv) > 1 else sorted(set(dados['ausentes']) | set(dados['pistas']))
    for cap in caps:
        for tipo, titulo in (('ausentes', 'Ausentes (gregos)'), ('pistas', 'Pistas (gregos)')):
            linhas = dados[tipo].get(cap, [])
            p = os.path.join(G.pasta_base(cap), f'_{tipo}-gregos.md')
            manual = ''
            if os.path.exists(p):
                velho = G.ler(p)
                manual = re.sub(re.escape(INI) + r'.*?' + re.escape(FIM), '', velho, flags=re.S)
                manual = re.sub(r'^# .*\n', '', manual).strip()
            if not linhas and not manual:
                if os.path.exists(p):
                    os.remove(p)
                continue
            auto = '\n'.join(f'- {l}' for l in linhas) or '- (nada dos scripts)'
            txt = f'# {titulo}\n\n{INI}\n{auto}\n{FIM}\n'
            if manual:
                txt += '\n' + manual + '\n'
            with open(p, 'w', encoding='utf-8', newline='\n') as f:
                f.write(txt)
            print(f'  gravado genesis/{cap:03d}/base/_{tipo}-gregos.md ({len(linhas)} linhas automáticas)')


if __name__ == '__main__':
    main()
