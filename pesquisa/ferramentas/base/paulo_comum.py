"""Funções comuns dos scripts de pré-pesquisa de 2 Coríntios (pesquisa/2corintios/<ccc>/base/).

Não se roda sozinho; os scripts `grc-*.py`, `la-*.py`, `ocr-*.py` desta pasta o importam:

    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # com `python -I` a pasta do script não entra sozinha
    from paulo_comum import *

Convenções (ver pesquisa/COMO-PESQUISAR.md, «Pré-pesquisa»):
  - o que se baixa vai UMA vez para pesquisa/cache/base/paulo/ (fora do git); refazer não baixa de novo;
  - uma requisição por vez, com pausa de 1 s;
  - `gravar()` escreve pesquisa/2corintios/<ccc>/base/<arquivo> com o cabeçalho exato.
"""
import os, re, sys, time, subprocess, urllib.request, urllib.error

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CACHE = os.path.join(RAIZ, 'cache', 'base', 'paulo')
LIVRO = os.path.join(RAIZ, '2corintios')
HOJE = '2026-10-20'
UA = 'Mozilla/5.0 (pesquisa Biblia Taioe; leitura de textos em dominio publico)'
CAPS = list(range(3, 14))   # capítulos de 2Cor cobertos por estes scripts

_ultima = [0.0]


def baixar(url, nome, pausa=1.0, binario=True):
    """Baixa `url` para o cache com o nome dado (se ainda não existir) e devolve o caminho."""
    os.makedirs(CACHE, exist_ok=True)
    destino = os.path.join(CACHE, nome)
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        return destino
    espera = pausa - (time.time() - _ultima[0])
    if espera > 0:
        time.sleep(espera)
    ultimo = None
    for tentativa in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                dados = r.read()
            _ultima[0] = time.time()
            with open(destino, 'wb') as f:
                f.write(dados)
            return destino
        except Exception as e:  # rede instável, 503 do archive.org etc.
            ultimo = e
            time.sleep(3 * (tentativa + 1))
    raise RuntimeError(f'falhou: {url}: {ultimo}')


def ler(caminho, codif='utf-8'):
    with open(caminho, encoding=codif, errors='replace') as f:
        return f.read()


def pdf_para_texto_grego(pdf, txt):
    """PDF da khazarzar -> texto limpo com [PG n, m] (usa pesquisa/ferramentas/gregos-limpar.py)."""
    if os.path.exists(txt) and os.path.getsize(txt) > 0:
        return txt
    limpar = os.path.join(RAIZ, 'ferramentas', 'gregos-limpar.py')
    subprocess.run([sys.executable, '-I', '-X', 'utf8', limpar, pdf, txt], check=True,
                   stdout=subprocess.DEVNULL)
    return txt


def script_nome():
    return os.path.basename(sys.argv[0]) if sys.argv and sys.argv[0] else 'script.py'


def gravar(cap, arquivo, titulo, campos, corpo, nota=None):
    """Grava base/<arquivo> do capítulo `cap` com o cabeçalho exato. Devolve o caminho."""
    pasta = os.path.join(LIVRO, f'{cap:03d}', 'base')
    os.makedirs(pasta, exist_ok=True)
    ordem = ['Autor', 'Obra', 'Passagem', 'Edição', 'Fonte', 'Cobre', 'Oriental', 'Língua']
    linhas = [f'# {titulo}']
    for k in ordem:
        linhas.append(f'- {k}: {campos[k]}')
    linhas.append(f'- Baixado: {HOJE}, por pesquisa/ferramentas/base/{script_nome()}')
    cab = '\n'.join(linhas)
    partes = [cab, '']
    if nota:
        partes += [f'> {nota}', '']
    partes.append(corpo.strip('\n'))
    caminho = os.path.join(pasta, arquivo)
    with open(caminho, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(partes) + '\n')
    return caminho


def resumo(caminhos):
    tot = 0
    for c in caminhos:
        tot += os.path.getsize(c)
        print(f'  {os.path.relpath(c, RAIZ)}: {os.path.getsize(c)//1024} KB')
    print(f'{len(caminhos)} arquivos, {tot//1024} KB')


ROMANOS = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
           10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII'}
