# Aide-mémoire (ce fichier n'apparaît pas sur le site : il commence par « _ »)

## Où est quoi ?
- `_quarto.yml`            : configuration + menu du haut
- `index.qmd`              : page d'accueil (les 3-4 images cliquables)
- `<niveau>/index.qmd`     : liste des chapitres du niveau + bacs blancs
- `<niveau>/chapitres/`    : une page par chapitre (lien vers le cours + PDF)
- `<niveau>/cours/`        : tes cours .qmd (et leurs images-cours)
- `<niveau>/2025-DS-eval/` : tes PDF (un sous-dossier par chapitre)

## Ajouter un PDF
1. [Disque] copier le PDF dans `<niveau>/<année>-DS-eval/<chapitre>/`
2. [VS Code] ouvrir `<niveau>/chapitres/<chapitre>.qmd`, ajouter une ligne `- [Titre](../<année>-DS-eval/<chapitre>/fichier.pdf)`
3. [VS Code] tester : `quarto preview` dans le terminal
4. [VS Code] Contrôle de code source : message → Valider → Synchroniser
5. [Terminal VS Code] `quarto publish gh-pages`

## Ajouter / modifier un cours
Même chose, avec le .qmd dans `<niveau>/cours/<chapitre>/`.
