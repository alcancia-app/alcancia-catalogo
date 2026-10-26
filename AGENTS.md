# Catálogo de recetas de Alcancía — guía

> Para personas y para cualquier IA de programación. `CLAUDE.md` y `GEMINI.md` solo importan este archivo.

Este repo guarda las **recetas** de la comunidad para [Alcancía](https://github.com/alcancia-app/alcancia): JSON de solo datos que
dicen cómo leer la cartola de un banco o billetera. El formato y la validación viven en el repo de Alcancía (`recetas/README.md` y
`bin/recetas.py`, función `validar`); este catálogo no tiene código propio salvo `herramientas/revisar.py`.

## Reglas
- Una receta por archivo en `recetas/<id>.json`, válida según `recetas.validar` (lo revisa `.github/workflows/revisar.yml` bajando el
  código de Alcancía).
- **Nada personal:** ni cartolas, ni montos, nombres, RUT, correos o números de cuenta. `herramientas/revisar.py` busca patrones típicos.
- Textos en español (de Chile neutro). Commits con autor `@users.noreply.github.com`.

## Revisar un aporte (issue o pull request)
1. Leer el JSON entero. Alerta roja: cualquier cosa que no sea una receta (scripts, enlaces raros, workflows).
2. `python3 herramientas/revisar.py ruta/a/receta.json` (necesita el código de Alcancía al lado: `ALCANCIA=../alcancia`).
3. Que `reconocer.encabezados` sean nombres de columna genéricos, no datos de una persona.
4. Si viene de un issue creado desde la app, pasar el JSON a `recetas/<id>.json` en un PR y cerrar el issue agradeciendo.
Nunca se junta nada sin la aprobación de quien mantiene el proyecto.
