#!/usr/bin/env bash
# =========================================================================
#  publier.sh : publie le site en ne régénérant QUE ce qui a changé
#
#  Utilisation (terminal de VS Code, dans le dossier SiteWeb) :
#     ./publier.sh           publication rapide (pages modifiées seulement)
#     ./publier.sh --tout    rendu complet puis publication (≈ 3 min)
#     ./publier.sh --essai   montre ce qui serait régénéré, sans publier
#
#  Le script retient le dernier commit publié dans .derniere-publication
#  (fichier local, ignoré par Git). Il régénère les .qmd modifiés depuis,
#  copie dans _site les PDF / images ajoutés ou modifiés, puis lance
#  « quarto publish gh-pages --no-render ».
#  Si _quarto.yml, styles.css ou index.qmd ont changé, tout est régénéré
#  (le menu et l'apparence concernent toutes les pages).
# =========================================================================
set -euo pipefail
cd "$(dirname "$0")"

REF_FICHIER=".derniere-publication"
MODE="${1:-}"

rendu_complet() { echo "→ Rendu complet du site…"; quarto render; }

if [[ "$MODE" == "--tout" || ! -f "$REF_FICHIER" || ! -d _site ]]; then
    [[ "$MODE" == "--essai" ]] && { echo "Rendu complet nécessaire (première fois ou _site absent)."; exit 0; }
    rendu_complet
else
    REF="$(cat "$REF_FICHIER")"
    # Fichiers modifiés depuis la dernière publication (commités ou non) + nouveaux fichiers
    mapfile -t MODIFIES < <( { git diff --name-only "$REF" --; git ls-files --others --exclude-standard; } | sort -u )
    mapfile -t SUPPRIMES < <( git diff --name-only --diff-filter=D "$REF" -- )

    if printf '%s\n' "${MODIFIES[@]}" | grep -qE '^(_quarto[^/]*\.yml|styles\.css|index\.qmd|_nouvel-onglet\.html)$'; then
        [[ "$MODE" == "--essai" ]] && { echo "Configuration ou apparence modifiée : rendu complet nécessaire."; exit 0; }
        rendu_complet
    else
        PAGES=(); FICHIERS=()
        for f in "${MODIFIES[@]}"; do
            [[ -f "$f" ]] || continue
            case "$f" in
                _*|*/_*|.*) ;;                                   # fichiers internes (non publiés)
                *.qmd) PAGES+=("$f") ;;
                *.pdf|*.png|*.jpg|*.jpeg|*.svg|*.gif|*/tp-informatique/*.py) FICHIERS+=("$f") ;;
            esac
        done
        if [[ "$MODE" == "--essai" ]]; then
            echo "Pages à régénérer (${#PAGES[@]}) :";   printf '   %s\n' "${PAGES[@]}"
            echo "Fichiers à copier (${#FICHIERS[@]}) :"; printf '   %s\n' "${FICHIERS[@]}"
            echo "Fichiers à retirer (${#SUPPRIMES[@]}) :"; printf '   %s\n' "${SUPPRIMES[@]}"
            exit 0
        fi
        for f in "${PAGES[@]}"; do echo "→ $f"; quarto render "$f" > /dev/null; done
        for f in "${FICHIERS[@]}"; do mkdir -p "_site/$(dirname "$f")"; cp "$f" "_site/$f"; done
        for f in "${SUPPRIMES[@]}"; do
            case "$f" in
                *.qmd) rm -f "_site/${f%.qmd}.html" ;;
                *) rm -f "_site/$f" ;;
            esac
        done
        [[ ${#PAGES[@]} -eq 0 && ${#FICHIERS[@]} -eq 0 && ${#SUPPRIMES[@]} -eq 0 ]] && echo "Aucune modification depuis la dernière publication."
    fi
fi

echo "→ Publication sur GitHub Pages…"
quarto publish gh-pages --no-render --no-prompt
git rev-parse HEAD > "$REF_FICHIER"
echo "✔ Site publié."
