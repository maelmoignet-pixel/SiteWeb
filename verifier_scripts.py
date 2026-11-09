#!/usr/bin/env python3
"""Garde-fou de publication : vérifie la syntaxe JavaScript des pages faites à la main (mode tableau, téléphone, Python…).
Une faute de syntaxe y casse tout le mode tableau : dans ce cas la publication est REFUSÉE (code de sortie 1)."""
import re, subprocess, sys, tempfile
from pathlib import Path
NODE = Path.home() / ".local/node/bin/node"
FICHIERS = ["_tableau.html", "_ma-seance.html", "_compteur.html", "_nouvel-onglet.html", "copie/index.html", "python/index.html", "sw.js", "python/worker.js"]
if not NODE.exists(): print("[vérification] node absent : vérification sautée"); sys.exit(0)
erreurs = 0
for f in FICHIERS:
    p = Path(f)
    if not p.exists(): continue
    s = p.read_text(encoding="utf-8")
    code = s if f.endswith(".js") else "\n;\n".join(x for x in re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", s, re.S) if x.strip())
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as t: t.write(code)
    r = subprocess.run([str(NODE), "--check", t.name], capture_output=True, text=True)
    if r.returncode: erreurs += 1; print(f"✗ FAUTE DE SYNTAXE dans {f} :\n" + "\n".join(r.stderr.splitlines()[:5]))
if erreurs: print("⛔ Publication refusée : corriger d'abord."); sys.exit(1)
print("[vérification] scripts du site : syntaxe correcte")
