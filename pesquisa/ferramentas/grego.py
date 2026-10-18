"""Texto grego do Novo Testamento, com lemas e morfologia, para conferir o original.

Fonte: MorphGNT, edição SBLGNT (o texto da SBL Greek New Testament, com a análise do MorphGNT),
https://github.com/morphgnt/sblgnt (arquivos <nn>-<Livro>-morphgnt.txt). O texto da SBLGNT segue a
licença da SBL e a análise é CC BY-SA 3.0: por isso os arquivos ficam só no cache
(pesquisa/cache/morphgnt/, fora do git) e são lidos como dado. Os sinais ⸀ ⸂ ⸃ marcam lugares
com variantes no aparato da SBLGNT (não se anotam variantes: só servem para saber que há uma).

Uso (da pasta biblia/, com Python 3 puro, sem pip):

    python pesquisa/ferramentas/grego.py --baixar                    # baixa os 27 livros que faltarem
    python pesquisa/ferramentas/grego.py --ref "2Cor 1,3-7"          # o trecho, palavra por palavra
    python pesquisa/ferramentas/grego.py --ref "2Cor 1,22" --corrido  # só o texto, sem análise
    python pesquisa/ferramentas/grego.py --lema παράκλησις           # todas as ocorrências no NT
    python pesquisa/ferramentas/grego.py --lema παρακαλέω --livro 2Cor --contar
    python pesquisa/ferramentas/grego.py --lema ἀρραβών --saida /caminho/arrabon.tsv

- Referências em português (Mt, Mc, Lc, Jo, At, Rm, 1Cor, 2Cor, Gl, Ef, Fl, Cl, 1Ts, 2Ts, 1Tm,
  2Tm, Tt, Fm, Hb, Tg, 1Pd, 2Pd, 1Jo, 2Jo, 3Jo, Jd, Ap). A numeração da SBLGNT coincide com a da
  Nova Vulgata quase sempre (exceções conhecidas: 2Cor 13,12-13; 3Jo 14-15; Ap 12,18).
- --lema compara sem acentos e sem maiúsculas (παρακαλεω acha παρακαλέω).
- --saida grava em UTF-8 (no Windows, o «>» do PowerShell grava UTF-16).
"""

import argparse
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

CACHE = Path(__file__).resolve().parents[1] / "cache" / "morphgnt"
URL = "https://raw.githubusercontent.com/morphgnt/sblgnt/master/{}-morphgnt.txt"

# número do MorphGNT, nome do arquivo, abreviação em português, chave do projeto antigo
LIVROS = [
    (61, "Mt", "Mt", "mateus"), (62, "Mk", "Mc", "marcos"), (63, "Lk", "Lc", "lucas"),
    (64, "Jn", "Jo", "joao"), (65, "Ac", "At", "atos"), (66, "Ro", "Rm", "romanos"),
    (67, "1Co", "1Cor", "1corintios"), (68, "2Co", "2Cor", "2corintios"), (69, "Ga", "Gl", "galatas"),
    (70, "Eph", "Ef", "efesios"), (71, "Php", "Fl", "filipenses"), (72, "Col", "Cl", "colossenses"),
    (73, "1Th", "1Ts", "1tessalonicenses"), (74, "2Th", "2Ts", "2tessalonicenses"),
    (75, "1Ti", "1Tm", "1timoteo"), (76, "2Ti", "2Tm", "2timoteo"), (77, "Tit", "Tt", "tito"),
    (78, "Phm", "Fm", "filemon"), (79, "Heb", "Hb", "hebreus"), (80, "Jas", "Tg", "tiago"),
    (81, "1Pe", "1Pd", "1pedro"), (82, "2Pe", "2Pd", "2pedro"), (83, "1Jn", "1Jo", "1joao"),
    (84, "2Jn", "2Jo", "2joao"), (85, "3Jn", "3Jo", "3joao"), (86, "Jud", "Jd", "judas"),
    (87, "Re", "Ap", "apocalipse"),
]

CLASSE = {"A-": "adj", "C-": "conj", "D-": "adv", "I-": "interj", "N-": "subst", "P-": "prep",
          "RA": "art", "RD": "dem", "RI": "interr/indef", "RP": "pron", "RR": "rel", "V-": "verbo",
          "X-": "partíc"}
PESSOA = {"1": "1ª", "2": "2ª", "3": "3ª"}
TEMPO = {"P": "pres", "I": "imperf", "F": "fut", "A": "aor", "X": "perf", "Y": "mais-q-perf"}
VOZ = {"A": "ativa", "M": "média", "P": "passiva"}
MODO = {"I": "ind", "D": "imper", "S": "subj", "O": "opt", "N": "infin", "P": "partic"}
CASO = {"N": "nom", "G": "gen", "D": "dat", "A": "acus", "V": "voc"}
NUM = {"S": "sg", "P": "pl"}
GEN = {"M": "m", "F": "f", "N": "n"}


def sem_acento(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c)).replace("ς", "σ")


def livro(abrev):
    a = sem_acento(abrev.replace(" ", ""))
    for n, arq, pt, chave in LIVROS:
        if a in (sem_acento(pt), arq.lower(), chave):
            return n, arq, pt
    sys.exit(f"livro desconhecido: {abrev}")


def arquivo(n, arq):
    caminho = CACHE / f"{n}-{arq}-morphgnt.txt"
    if not caminho.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(URL.format(f"{n}-{arq}")) as r:
            caminho.write_bytes(r.read())
    return caminho


def palavras(n, arq):
    for linha in arquivo(n, arq).read_text(encoding="utf-8").splitlines():
        bcv, cl, an, texto, _, _, lema = linha.split(" ")
        yield int(bcv[2:4]), int(bcv[4:6]), cl, an, texto, lema


def analise(cl, an):
    p = [CLASSE.get(cl, cl)]
    pe, te, vo, mo, ca, nu, ge, gr = an
    for cod, tab in ((pe, PESSOA), (te, TEMPO), (vo, VOZ), (mo, MODO), (ca, CASO), (nu, NUM), (ge, GEN)):
        if cod != "-":
            p.append(tab.get(cod, cod))
    if gr == "C":
        p.append("compar")
    elif gr == "S":
        p.append("superl")
    return " ".join(p)


def faixa(ref):
    m = re.match(r"\s*(\d?\s*[^\d\s,]+)\s*(\d+)(?:,(\d+)(?:-(\d+))?)?\s*$", ref)
    if not m:
        sys.exit(f"referência inválida: {ref}")
    n, arq, pt = livro(m.group(1))
    cap = int(m.group(2))
    v1 = int(m.group(3)) if m.group(3) else 1
    v2 = int(m.group(4)) if m.group(4) else (v1 if m.group(3) else 999)
    return n, arq, pt, cap, v1, v2


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baixar", action="store_true")
    ap.add_argument("--ref")
    ap.add_argument("--corrido", action="store_true")
    ap.add_argument("--lema")
    ap.add_argument("--livro")
    ap.add_argument("--contar", action="store_true")
    ap.add_argument("--saida")
    a = ap.parse_args()
    linhas = []
    if a.baixar:
        for n, arq, _, _ in LIVROS:
            arquivo(n, arq)
        linhas.append(f"{len(LIVROS)} livros em {CACHE}")
    if a.ref:
        n, arq, pt, cap, v1, v2 = faixa(a.ref)
        atual, corrido = None, []
        for c, v, cl, an, texto, lema in palavras(n, arq):
            if c != cap or not v1 <= v <= v2:
                continue
            if v != atual:
                if corrido:
                    linhas.append(" ".join(corrido))
                    corrido = []
                linhas.append(f"\n{pt} {c},{v}")
                atual = v
            if a.corrido:
                corrido.append(texto)
            else:
                linhas.append(f"  {texto:<22} {lema:<18} {analise(cl, an)}")
        if corrido:
            linhas.append(" ".join(corrido))
    if a.lema:
        alvo = sem_acento(a.lema)
        so = livro(a.livro)[0] if a.livro else None
        total = {}
        for n, arq, pt, _ in LIVROS:
            if so and n != so:
                continue
            for c, v, cl, an, texto, lema in palavras(n, arq):
                if sem_acento(lema) == alvo:
                    total[pt] = total.get(pt, 0) + 1
                    if not a.contar:
                        linhas.append(f"{pt} {c},{v}\t{texto}\t{analise(cl, an)}")
        linhas.append(f"total: {sum(total.values())} ({', '.join(f'{k} {v}' for k, v in total.items())})")
    saida = "\n".join(linhas) + "\n"
    if a.saida:
        Path(a.saida).write_text(saida, encoding="utf-8")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(saida)


if __name__ == "__main__":
    main()
