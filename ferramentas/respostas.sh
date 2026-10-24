#!/usr/bin/env bash
# Respostas do Gere na revisão da Bíblia Taioé (/admin/pendencias/), pelo workflow Respostas do
# taioe-infra (a senha do banco fica só no GitHub).
#   bash ferramentas/respostas.sh exportar             → baixa da produção e imprime o caminho do JSON
#   bash ferramentas/respostas.sh marcar <arquivo>     → marca como lidas as respostas do arquivo
#                                                        (o mesmo JSON do exportar, ou só as aplicadas)
#   bash ferramentas/respostas.sh teste exportar|marcar …  → o mesmo, no projeto de teste
#   bash ferramentas/respostas.sh comentarios exportar|marcar …  → a página dos comentários
#                                                        («comentários dos Padres»; marcar com o
#                                                        .aplicadas.json do aplicar-comentarios.mjs)
set -euo pipefail
AMBIENTE=producao
PAGINA=biblia
while [ $# -gt 0 ]; do
  case "$1" in
    teste) AMBIENTE=teste; shift ;;
    comentarios) PAGINA=biblia-comentarios; shift ;;
    *) break ;;
  esac
done
export GH_TOKEN="$(gh auth token --user gereneto)"
R=organizacoes-taioe/taioe-infra
PASTA="${TEMP:-/tmp}/taioe-respostas"
mkdir -p "$PASTA"

rodar() {   # dispara o workflow e espera ele terminar; imprime o id
  local antes; antes=$(gh run list -R "$R" -w Respostas -L 1 --json databaseId -q '.[0].databaseId' 2>/dev/null || echo 0)
  gh workflow run Respostas -R "$R" "$@" >/dev/null
  local id="$antes" n=0
  while [ "$id" = "$antes" ] && [ $n -lt 30 ]; do sleep 3; n=$((n+1)); id=$(gh run list -R "$R" -w Respostas -L 1 --json databaseId -q '.[0].databaseId'); done
  gh run watch "$id" -R "$R" --exit-status >/dev/null || { echo "o workflow Respostas falhou: https://github.com/$R/actions/runs/$id" >&2; exit 1; }
  echo "$id"
}

case "${1:-}" in
  exportar)
    id=$(rodar -f acao=exportar -f pagina="$PAGINA" -f ambiente="$AMBIENTE")
    rm -rf "$PASTA/$PAGINA" && gh run download "$id" -R "$R" -n "respostas-$PAGINA-$AMBIENTE" -D "$PASTA/$PAGINA"
    echo "$PASTA/$PAGINA/respostas.json" ;;
  marcar)
    [ -f "${2:-}" ] || { echo "uso: respostas.sh marcar <arquivo.json>" >&2; exit 1; }
    # Em lotes de 250: o workflow_dispatch aceita no máximo 65 535 caracteres de entrada.
    node -e "const d=JSON.parse(require('fs').readFileSync(process.argv[1],'utf8'));const r=(d.respostas||d.lidas||[]).filter(x=>!x.lida).map(x=>({item:x.item,atualizado_em:x.atualizado_em}));for(let i=0;i<r.length;i+=250)console.log(JSON.stringify({pagina:process.argv[2],lidas:r.slice(i,i+250)}))" "$2" "$PAGINA" |
    while IFS= read -r dados; do
      rodar -f acao=marcar -f pagina="$PAGINA" -f ambiente="$AMBIENTE" -f dados="$dados" >/dev/null
    done
    echo "marcadas em $AMBIENTE" ;;
  *) echo "uso: respostas.sh [teste] [comentarios] exportar | marcar <arquivo.json>" >&2; exit 1 ;;
esac
