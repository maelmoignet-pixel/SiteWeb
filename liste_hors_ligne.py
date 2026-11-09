#!/usr/bin/env python3
"""Fabrique _site/hors-ligne.json : la liste de tout ce que l'iPad doit garder pour fonctionner sans réseau
(bouton « Préparer le hors ligne » du mode tableau). Lancé par publier.sh juste avant la publication.

Chaque fichier a une signature (taille + date) : l'iPad ne retélécharge que ce qui a changé.
On y ajoute les fichiers externes nécessaires : KaTeX (formules) et Python (Pyodide, matplotlib)."""
import json, os, sys
from pathlib import Path

site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
if site.name != "_site" or not site.is_dir():
    sys.exit(f"[hors ligne] dossier inattendu ({site}) : rien n'est fait")

IGNORER = ("gestion/", "copie/", "hors-ligne.json", "sw.js", "search.json")   # outils en ligne seulement
fichiers = []
for f in sorted(site.rglob("*")):
    if not f.is_file(): continue
    rel = f.relative_to(site).as_posix()
    if rel.startswith(IGNORER) or rel.startswith("_") or "/." in "/" + rel: continue
    st = f.stat()
    fichiers.append([rel, st.st_size, int(st.st_mtime)])

K = "https://cdn.jsdelivr.net/npm/katex@0.15.1/dist/"
polices = ["AMS-Regular", "Caligraphic-Bold", "Caligraphic-Regular", "Fraktur-Bold", "Fraktur-Regular", "Main-Bold", "Main-BoldItalic",
           "Main-Italic", "Main-Regular", "Math-BoldItalic", "Math-Italic", "SansSerif-Bold", "SansSerif-Italic", "SansSerif-Regular",
           "Script-Regular", "Size1-Regular", "Size2-Regular", "Size3-Regular", "Size4-Regular", "Typewriter-Regular"]
P = "https://cdn.jsdelivr.net/pyodide/v0.27.7/full/"
python = ["pyodide.js", "pyodide.asm.js", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json",
          "matplotlib-3.8.4-cp312-cp312-pyodide_2024_0_wasm32.whl", "contourpy-1.3.0-cp312-cp312-pyodide_2024_0_wasm32.whl",
          "numpy-2.0.2-cp312-cp312-pyodide_2024_0_wasm32.whl", "cycler-0.12.1-py3-none-any.whl", "six-1.16.0-py2.py3-none-any.whl",
          "fonttools-4.51.0-py3-none-any.whl", "kiwisolver-1.4.5-cp312-cp312-pyodide_2024_0_wasm32.whl", "packaging-24.2-py3-none-any.whl",
          "pillow-10.2.0-cp312-cp312-pyodide_2024_0_wasm32.whl", "pyparsing-3.1.2-py3-none-any.whl",
          "python_dateutil-2.9.0.post0-py2.py3-none-any.whl", "pytz-2024.1-py2.py3-none-any.whl", "matplotlib_pyodide-0.2.3-py3-none-any.whl"]
externes = [K + "katex.min.css", K + "katex.min.js"] + [K + "fonts/KaTeX_" + p + ".woff2" for p in polices] + [P + x for x in python]

total = sum(x[1] for x in fichiers)
(site / "hors-ligne.json").write_text(json.dumps({"fichiers": fichiers, "externes": externes}, separators=(",", ":")), encoding="utf-8")
print(f"[hors ligne] {len(fichiers)} fichiers ({total / 1e6:.0f} Mo) + {len(externes)} externes listés")
