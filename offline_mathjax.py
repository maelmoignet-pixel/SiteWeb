#!/usr/bin/env python3
"""
Post-render du profil "offline" (version 3) : rend les formules lisibles sans
internet, que les pages utilisent KaTeX ou MathJax.

- Repère dans les pages de _site_offline les liens internet vers KaTeX/MathJax.
- Télécharge la bibliothèque correspondante une seule fois (dans _offline_cache/).
- La copie dans _site_offline/libs/.
- Remplace les liens internet par des liens relatifs vers cette copie locale.
- Si aucun lien n'est trouvé, affiche un diagnostic.

Garde-fou : le script refuse de travailler sur un autre dossier que _site_offline.
"""
import os
import re
import shutil
import sys
import tarfile
import urllib.request
from pathlib import Path

CACHE = Path("_offline_cache")
MATHJAX_VERSION = "3.2.2"

# KaTeX : https://cdn.jsdelivr.net/npm/katex@0.13.11/dist/katex.min.js
LIEN_KATEX = re.compile(r"https?://cdn\.jsdelivr\.net/npm/katex@([\d.]+)/dist/")
# MathJax : toute adresse contenant "mathjax" et finissant par tex-….js
LIEN_MATHJAX = re.compile(
    r"https?://[^\"'\s<>]*?mathjax[^\"'\s<>]*?/(tex-[\w-]+\.js)[^\"'\s<>]*",
    re.IGNORECASE,
)

out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site_offline"))

# --- Garde-fou ---------------------------------------------------------------
if out.name != "_site_offline":
    print(f"[offline] Dossier de sortie inattendu ({out}) : rien n'est modifié.")
    sys.exit(0)
if not out.is_dir():
    print(f"[offline] {out} introuvable : rien n'est modifié.")
    sys.exit(0)


def recuperer(paquet, version, sous_dossier):
    """Télécharge (une seule fois) package/<sous_dossier> du paquet npm et
    renvoie le dossier local qui le contient."""
    dossier = CACHE / f"{paquet}-{version}"
    cible = dossier / sous_dossier
    if not cible.is_dir():
        print(f"[offline] Téléchargement de {paquet} {version}…")
        dossier.mkdir(parents=True, exist_ok=True)
        tgz = dossier / "paquet.tgz"
        urllib.request.urlretrieve(
            f"https://registry.npmjs.org/{paquet}/-/{paquet}-{version}.tgz", tgz)
        with tarfile.open(tgz) as tar:
            for m in tar.getmembers():
                if m.name.startswith(f"package/{sous_dossier}/") and m.isfile():
                    m.name = m.name[len("package/"):]
                    tar.extract(m, dossier)
        tgz.unlink()
    return cible


pages = [p for p in out.rglob("*.html") if "libs" not in p.relative_to(out).parts[:1]]
modifiees = 0
installes = set()

for page in pages:
    texte = page.read_text(encoding="utf-8")
    nouveau = texte

    # --- KaTeX ---------------------------------------------------------------
    for version in set(LIEN_KATEX.findall(nouveau)):
        dest = out / "libs" / f"katex-{version}" / "dist"
        if ("katex", version) not in installes:
            shutil.copytree(recuperer("katex", version, "dist"), dest, dirs_exist_ok=True)
            installes.add(("katex", version))
        relatif = os.path.relpath(dest, page.parent).replace(os.sep, "/") + "/"
        nouveau = re.sub(
            rf"https?://cdn\.jsdelivr\.net/npm/katex@{re.escape(version)}/dist/",
            relatif, nouveau)

    # --- MathJax -------------------------------------------------------------
    if LIEN_MATHJAX.search(nouveau):
        dest = out / "libs" / "mathjax" / "es5"
        if ("mathjax", MATHJAX_VERSION) not in installes:
            shutil.copytree(recuperer("mathjax", MATHJAX_VERSION, "es5"), dest, dirs_exist_ok=True)
            installes.add(("mathjax", MATHJAX_VERSION))
        relatif = os.path.relpath(dest, page.parent).replace(os.sep, "/") + "/"
        nouveau = LIEN_MATHJAX.sub(lambda m: relatif + m.group(1), nouveau)

    if nouveau != texte:
        page.write_text(nouveau, encoding="utf-8")
        modifiees += 1

libs = ", ".join(f"{p} {v}" for p, v in sorted(installes)) or "aucune"
print(f"[offline] Bibliothèques installées : {libs}")
print(f"[offline] {modifiees} page(s) mise(s) à jour dans {out}.")

# --- Diagnostic si rien n'a été trouvé ------------------------------------
if modifiees == 0:
    avec_formules = [p for p in pages if 'class="math' in p.read_text(encoding="utf-8")]
    print(f"[offline] DIAGNOSTIC : {len(avec_formules)} page(s) contiennent des formules.")
    if avec_formules:
        exemple = avec_formules[0]
        print(f"[offline] Page examinée : {exemple.relative_to(out)}")
        lignes = [l.strip() for l in exemple.read_text(encoding="utf-8").splitlines()
                  if re.search(r"mathjax|katex", l, re.IGNORECASE)]
        for l in lignes[:12]:
            print("   ", l[:220])
