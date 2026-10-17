"""Texto hebraico do Antigo Testamento, com lemas Strong e morfologia, para conferir o original.

Fonte: Open Scriptures Hebrew Bible (morphhb), Westminster Leningrad Codex com lemas e morfologia,
licença CC BY 4.0, https://github.com/openscriptures/morphhb (arquivos wlc/<Livro>.xml).
Os arquivos baixados ficam em pesquisa/cache/morphhb/ (fora do git) e são lidos só como dado.

Uso (da pasta biblia/, com Python 3 puro, sem pip):

    python pesquisa/ferramentas/hebraico.py --baixar                 # baixa os 39 livros que faltarem
    python pesquisa/ferramentas/hebraico.py --ref "Sl 33,19"         # o versículo, palavra por palavra
    python pesquisa/ferramentas/hebraico.py --ref "Sl 33,18-22"      # um trecho
    python pesquisa/ferramentas/hebraico.py --lema 5315              # todas as ocorrências de nefesh
    python pesquisa/ferramentas/hebraico.py --lema 5315 --livro Sl --contar
    python pesquisa/ferramentas/hebraico.py --lema 5315 --formato tsv --saida /caminho/nefesh.tsv

- Referências em português (Gn, Êx, Lv, … Sl, … Ml; também sem acento: Ex, Jo para Jó) ou OSIS
  (Gen, Exod, Ps…). Capítulo e versículo são os do texto hebraico (Massorético), que às vezes
  diferem da Nova Vulgata (ex.: Jl 3–4, Ml 3, títulos dos salmos); a numeração dos Salmos é a hebraica.
- --lema aceita o número Strong (5315) ou o lema com prefixo (H5315). O morphhb põe prefixos
  (b/, l/, c/…) e homônimos («5315 a»): a busca compara só o número.
- No ketiv/qere, vale o qere (a leitura).
- --saida grava em UTF-8 (no Windows, o «>» do PowerShell grava UTF-16).
- A transliteração é simples e aproximada (sem diacríticos), só para ler depressa; para citar,
  conferir à mão.
"""

import argparse
import json
import re
import sys
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

CACHE = Path(__file__).resolve().parents[1] / "cache" / "morphhb"
URL = "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/{}.xml"
NS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"

# OSIS, abreviação em português, chave do projeto antigo (Software MEU/biblia/livros/<chave>.js)
LIVROS = [
    ("Gen", "Gn", "genesis"), ("Exod", "Êx", "exodo"), ("Lev", "Lv", "levitico"),
    ("Num", "Nm", "numeros"), ("Deut", "Dt", "deuteronomio"), ("Josh", "Js", "josue"),
    ("Judg", "Jz", "juizes"), ("Ruth", "Rt", "rute"), ("1Sam", "1Sm", "1samuel"),
    ("2Sam", "2Sm", "2samuel"), ("1Kgs", "1Rs", "1reis"), ("2Kgs", "2Rs", "2reis"),
    ("1Chr", "1Cr", "1cronicas"), ("2Chr", "2Cr", "2cronicas"), ("Ezra", "Esd", "esdras"),
    ("Neh", "Ne", "neemias"), ("Esth", "Est", "ester"), ("Job", "Jó", "jo"),
    ("Ps", "Sl", "salmos"), ("Prov", "Pr", "proverbios"), ("Eccl", "Ecl", "eclesiastes"),
    ("Song", "Ct", "cantico"), ("Isa", "Is", "isaias"), ("Jer", "Jr", "jeremias"),
    ("Lam", "Lm", "lamentacoes"), ("Ezek", "Ez", "ezequiel"), ("Dan", "Dn", "daniel"),
    ("Hos", "Os", "oseias"), ("Joel", "Jl", "joel"), ("Amos", "Am", "amos"),
    ("Obad", "Ab", "abdias"), ("Jonah", "Jn", "jonas"), ("Mic", "Mq", "miqueias"),
    ("Nah", "Na", "naum"), ("Hab", "Hab", "habacuc"), ("Zeph", "Sf", "sofonias"),
    ("Hag", "Ag", "ageu"), ("Zech", "Zc", "zacarias"), ("Mal", "Ml", "malaquias"),
]
OSIS_PT = {o: p for o, p, _ in LIVROS}
OSIS_CHAVE = {o: c for o, _, c in LIVROS}


def _sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)).lower()


ALIAS = {}
for _o, _p, _c in LIVROS:
    for _a in (_o, _p, _c):
        ALIAS[_sem_acento(_a)] = _o
ALIAS["jo"] = "Job"  # Jó (João não está no AT)


def livro_osis(nome):
    o = ALIAS.get(_sem_acento(nome.strip()))
    if not o:
        sys.exit(f"Livro desconhecido: {nome}")
    return o


def baixar(osis=None):
    CACHE.mkdir(parents=True, exist_ok=True)
    for o, _, _ in LIVROS:
        if osis and o != osis:
            continue
        destino = CACHE / f"{o}.xml"
        if destino.exists() and destino.stat().st_size > 0:
            continue
        print(f"baixando {o}...", file=sys.stderr)
        with urllib.request.urlopen(URL.format(o), timeout=60) as r:
            dados = r.read()
        if not dados.lstrip().startswith(b"<?xml"):
            sys.exit(f"Resposta inesperada para {o}")
        destino.write_bytes(dados)


# ---------------------------------------------------------------- leitura

def _palavra(w):
    lema = w.get("lemma", "")
    numeros = []
    for parte in lema.split("/"):
        tok = parte.strip().split(" ")[0]
        if tok.isdigit():
            numeros.append(tok)
    return {
        "texto": (w.text or "").replace("/", ""),
        "partes": (w.text or "").split("/"),
        "lema": lema,
        "strong": numeros,
        "morph": w.get("morph", ""),
    }


def versiculos(osis):
    """Gera (cap, vers, [palavras], texto) de um livro."""
    arq = CACHE / f"{osis}.xml"
    if not arq.exists():
        baixar(osis)
    raiz = ET.parse(arq).getroot()
    for v in raiz.iter(NS + "verse"):
        _, cap, ver = v.get("osisID").split(".")
        palavras, pedacos = [], []
        filhos = list(v)
        i = 0
        while i < len(filhos):
            el = filhos[i]
            tag = el.tag.replace(NS, "")
            if tag == "w":
                p = _palavra(el)
                if el.get("type") == "x-ketiv" and i + 1 < len(filhos) and filhos[i + 1].tag == NS + "note":
                    qere = [x for x in filhos[i + 1].iter(NS + "w")]
                    if qere:
                        p = _palavra(qere[0])
                        for extra in qere[1:]:
                            palavras.append(_palavra(extra))
                            pedacos.append(" " + palavras[-1]["texto"])
                        p["ketiv"] = (el.text or "").replace("/", "")
                    i += 1
                palavras.append(p)
                pedacos.append(" " + p["texto"])
            elif tag == "seg":
                t = el.text or ""
                pedacos.append(t)
            i += 1
        texto = "".join(pedacos).replace("־ ", "־").strip()
        yield int(cap), int(ver), palavras, texto


# ---------------------------------------------------------------- transliteração simples

# Letras: א alef ... ת tav; sinais: ְ sheva, ֱ-ֳ hatafs, ִ hiriq,
# ֵ tsere, ֶ segol, ַ patah, ָ qamats, ֹ holam, ֻ qubuts,
# ּ dagesh/mappiq, ׁ ponto do shin, ׂ ponto do sin.
CONS = {
    "א": "'", "ב": "v", "ג": "g", "ד": "d", "ה": "h", "ו": "v",
    "ז": "z", "ח": "h", "ט": "t", "י": "y", "ך": "kh", "כ": "kh",
    "ל": "l", "ם": "m", "מ": "m", "ן": "n", "נ": "n", "ס": "s",
    "ע": "'", "ף": "f", "פ": "f", "ץ": "ts", "צ": "ts", "ק": "q",
    "ר": "r", "ש": "sh", "ת": "t",
}
DUROS = {"ב": "b", "ך": "k", "כ": "k", "ף": "p", "פ": "p"}
VOG = {
    "ַ": "a", "ָ": "a", "ֶ": "e", "ֵ": "e", "ִ": "i", "ֹ": "o",
    "ֺ": "o", "ֻ": "u", "ֲ": "a", "ֱ": "e", "ֳ": "o", "ׇ": "o",
}
SHEVA, DAGESH, SIN, HOLAM = "ְ", "ּ", "ׂ", "ֹ"
ALEF, HE, VAV, YOD, HET, AYIN, SHIN = "א", "ה", "ו", "י", "ח", "ע", "ש"
LIXO = re.compile("[֑-ֽֿ֯׀׃-׆]")  # acentos, meteg, sof pasuq
YHWH = "יהוה"


def transliterar(heb):
    """Transliteração simples e aproximada, sem diacríticos: נַפְשָׁם → nafsham."""
    s = LIXO.sub("", heb).replace("־", "-")  # maqaf vira hífen
    saida = []
    for palavra in re.split(r"(\s+|-)", s):
        if not palavra or palavra.isspace() or palavra == "-":
            saida.append(palavra)
            continue
        grupos = []  # [letra, sinais]
        for c in palavra:
            if c in CONS:
                grupos.append([c, ""])
            elif grupos:
                grupos[-1][1] += c
        if "".join(g[0] for g in grupos).endswith(YHWH):
            pref = transliterar("".join(l + m for l, m in grupos[:-4])) if len(grupos) > 4 else ""
            saida.append(pref + "YHWH")
            continue
        out, sheva_ant = "", False
        for k, (l, m) in enumerate(grupos):
            inicio, fim = k == 0, k == len(grupos) - 1
            vog = "".join(VOG.get(x, "") for x in m)
            dobrada = DAGESH in m and not inicio and l not in (HE, VAV) and out[-1:] in tuple("aeiou")
            if l == VAV and (m == HOLAM or (HOLAM in m and not vog.replace("o", ""))) and not inicio:
                out += "o"; sheva_ant = False; continue
            if l == VAV and m == DAGESH:
                out += "u"; sheva_ant = False; continue
            if l == YOD and not m and out.endswith(("i", "e")):
                continue
            if l == HE and fim and not m:
                continue
            if l == ALEF and not vog:
                sheva_ant = False; continue
            if l == SHIN:
                cons = "s" if SIN in m else "sh"
            elif DAGESH in m and l in DUROS:
                cons = DUROS[l]
            else:
                cons = CONS[l]
            if l in (ALEF, AYIN) and inicio:
                cons = ""
            if dobrada:
                cons = cons + cons if len(cons) == 1 else cons
            if SHEVA in m:
                vocal = not fim and (inicio or dobrada or sheva_ant or out in ("u", "ve", "be", "le", "ke"))
                vog = "e" if vocal else ""
                sheva_ant = not vocal
            else:
                sheva_ant = False
            if fim and l in (HET, AYIN) and "ַ" in m:  # patah furtivo
                out += "a" + cons; continue
            out += cons + vog
        saida.append(out)
    return "".join(saida)


# ---------------------------------------------------------------- referências

def parse_ref(texto):
    m = re.match(r"\s*(\d?\s*[^\d\s,]+)\s*(\d+)(?:[,:.](\d+)(?:\s*[-–]\s*(\d+))?)?\s*$", texto)
    if not m:
        sys.exit(f"Referência inválida: {texto}")
    o = livro_osis(m.group(1).replace(" ", ""))
    cap = int(m.group(2))
    v1 = int(m.group(3)) if m.group(3) else None
    v2 = int(m.group(4)) if m.group(4) else v1
    return o, cap, v1, v2


def ref_pt(osis, cap, ver):
    return f"{OSIS_PT[osis]} {cap},{ver}"


# ---------------------------------------------------------------- comandos

def cmd_ref(args, escrever):
    o, cap, v1, v2 = parse_ref(args.ref)
    for c, v, palavras, texto in versiculos(o):
        if c != cap or (v1 is not None and not (v1 <= v <= v2)):
            continue
        escrever(f"{ref_pt(o, c, v)}  {texto}")
        escrever(f"  {transliterar(texto)}")
        for p in palavras:
            k = f"  [ketiv {p['ketiv']}]" if "ketiv" in p else ""
            escrever(f"    {p['texto']:<14} {transliterar(p['texto']):<16} {p['lema']:<14} {p['morph']}{k}")
        escrever("")


def cmd_lema(args, escrever):
    alvo = re.sub(r"\D", "", args.lema)
    livros = [livro_osis(args.livro)] if args.livro else [o for o, _, _ in LIVROS]
    linhas, contagem = [], {}
    for o in livros:
        for c, v, palavras, texto in versiculos(o):
            for i, p in enumerate(palavras):
                if alvo in p["strong"]:
                    contagem[o] = contagem.get(o, 0) + 1
                    linhas.append({
                        "ref": ref_pt(o, c, v), "osis": f"{o}.{c}.{v}", "posicao": i + 1,
                        "forma": p["texto"], "translit": transliterar(p["texto"]),
                        "lema": p["lema"], "morph": p["morph"], "versiculo": texto,
                    })
    if args.contar:
        for o in livros:
            if o in contagem:
                escrever(f"{OSIS_PT[o]}\t{contagem[o]}")
        escrever(f"total\t{sum(contagem.values())}")
        return
    if args.formato == "json":
        escrever(json.dumps(linhas, ensure_ascii=False, indent=1))
    elif args.formato == "tsv":
        cols = ["ref", "osis", "posicao", "forma", "translit", "lema", "morph", "versiculo"]
        escrever("\t".join(cols))
        for l in linhas:
            escrever("\t".join(str(l[k]) for k in cols))
    else:
        for l in linhas:
            escrever(f"{l['ref']:<10} {l['forma']:<12} {l['translit']:<14} {l['morph']:<16} {l['versiculo']}")
        escrever(f"total: {len(linhas)}")


def main():
    ap = argparse.ArgumentParser(description="Texto hebraico (morphhb) com lemas Strong.")
    ap.add_argument("--baixar", action="store_true", help="baixa os livros que faltarem no cache")
    ap.add_argument("--ref", help='versículo ou trecho, ex.: "Sl 33,19" ou "Gn 2,4-7"')
    ap.add_argument("--lema", help="número Strong, ex.: 5315")
    ap.add_argument("--livro", help="limitar --lema a um livro")
    ap.add_argument("--contar", action="store_true", help="só a contagem por livro")
    ap.add_argument("--formato", choices=["texto", "tsv", "json"], default="texto")
    ap.add_argument("--saida", help="arquivo de saída (UTF-8)")
    args = ap.parse_args()

    destino = open(args.saida, "w", encoding="utf-8", newline="\n") if args.saida else None
    if not destino:
        sys.stdout.reconfigure(encoding="utf-8")

    def escrever(s):
        print(s, file=destino or sys.stdout)

    if args.baixar:
        baixar()
    if args.ref:
        cmd_ref(args, escrever)
    if args.lema:
        cmd_lema(args, escrever)
    if not (args.baixar or args.ref or args.lema):
        ap.print_help()
    if destino:
        destino.close()


if __name__ == "__main__":
    main()
