#!/usr/bin/env python3
"""Post-render du profil « offline » : la version hors ligne (ouverte depuis des fichiers) ne peut pas lire les .json
(le navigateur bloque fetch sur file://). On livre donc à côté de chaque index.json un .js qui remplit window.__DONNEES.
Ajoute aussi, dans la version hors ligne SEULEMENT, les exercices découpés du manuel de Terminale (privé, droits
d'auteur : jamais dans le site en ligne ni dans le dépôt). Garde-fou : ne travaille que sur _site_offline."""
import json, os, shutil, sys
from pathlib import Path
out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site_offline"))
if out.name != "_site_offline" or not out.is_dir():
    print(f"[hors ligne] dossier inattendu ({out}) : rien n'est fait."); sys.exit(0)
def en_js(fichier_json, nom):
    d = fichier_json.read_text(encoding="utf-8")
    json.loads(d)   # contrôle
    fichier_json.with_suffix(".js").write_text(f"window.__DONNEES=window.__DONNEES||{{}};window.__DONNEES[{json.dumps(nom)}]={d};", encoding="utf-8")
n = 0
for niv in ("seconde", "premiere-spe", "premiere-tc"):
    f = out / niv / "exercices-sesamath" / "index.json"
    if f.exists(): en_js(f, f"{niv}/exercices-sesamath/"); n += 1
f = out / "automatismes" / "qcm.json"
if f.exists(): en_js(f, "automatismes/"); n += 1
lls = Path.home() / "Outils/manuels/terminale-lls"
if (lls / "index.json").exists():
    cible = out / "terminale-spe" / "exercices-lls"
    if cible.exists(): shutil.rmtree(cible)
    shutil.copytree(lls / "images", cible); shutil.copy(lls / "index.json", cible / "index.json")
    en_js(cible / "index.json", "terminale-spe/exercices-lls/"); n += 1
    print(f"[hors ligne] manuel de Terminale (privé) ajouté : {len(json.loads((lls / 'index.json').read_text()))} exercices")
print(f"[hors ligne] {n} fichiers de données livrés aussi en .js")
