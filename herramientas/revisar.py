"""Revisa las recetas del catálogo: válidas según Alcancía y sin datos personales. Solo biblioteca estándar.

Uso: ALCANCIA=../alcancia python3 herramientas/revisar.py [recetas/*.json]
"""
import glob
import json
import os
import re
import sys

ALCANCIA = os.environ.get("ALCANCIA", os.path.join(os.path.dirname(__file__), "..", "..", "alcancia"))
sys.path.insert(0, os.path.join(ALCANCIA, "bin"))
import recetas  # noqa: E402

# Lo que nunca debería aparecer en una receta: RUT, correos, números largos (cuentas, tarjetas), montos con decimales.
SOSPECHOSO = re.compile(r"\b\d{1,2}\.?\d{3}\.?\d{3}-[\dkK]\b|[\w.+-]+@[\w-]+\.[\w.]+|\d{8,}|\b\d{1,3}(?:[.,]\d{3})+[.,]\d{2}\b")


def revisar(ruta):
    problemas = []
    try:
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
        r = json.loads(texto)
    except (OSError, ValueError) as e:
        return [f"no es JSON válido: {e}"]
    problemas += recetas.validar(r)
    if isinstance(r, dict) and os.path.basename(ruta) != f"{r.get('id')}.json":
        problemas.append(f"el archivo debe llamarse {r.get('id')}.json")
    if m := SOSPECHOSO.search(texto):
        problemas.append(f"parece traer un dato personal o un monto: «{m.group(0)}»")
    return problemas


if __name__ == "__main__":
    archivos = sys.argv[1:] or sorted(glob.glob("recetas/*.json"))
    malos = 0
    for a in archivos:
        p = revisar(a)
        print(("✗ " if p else "✓ ") + a + ("" if not p else "\n    " + "\n    ".join(p)))
        malos += bool(p)
    print(f"{len(archivos)} recetas revisadas, {malos} con problemas.")
    sys.exit(1 if malos else 0)
