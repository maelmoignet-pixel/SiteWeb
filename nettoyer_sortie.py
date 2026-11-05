"""Post-render : retire du site fabriqué les copies des anciennes versions fabriquées (_site, _site_offline).
Quarto les recopiait à cause des règles « resources » de _quarto.yml (qui valent à toutes les profondeurs)."""
import os, shutil
from pathlib import Path
out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
if out.name in ("_site", "_site_offline") and out.is_dir():
    for d in ("_site", "_site_offline"):
        if (out / d).is_dir():
            shutil.rmtree(out / d); print(f"[nettoyage] {out.name}/{d} retiré")
