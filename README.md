# Catálogo de recetas de Alcancía

Las **recetas** le enseñan a [Alcancía](https://github.com/alcancia-app/alcancia) a leer la cartola de cada banco o billetera del
mundo: qué columna es la fecha, cuál la descripción, cuál el monto y cómo vienen escritos los números. Son archivos JSON de **solo
datos** (nunca código) y las hace la comunidad. *(English below.)*

## Agregar tu banco (sin programar)
1. En Alcancía, agrega la cartola de tu banco. Si todavía no sabe leerla, deja que tu IA aprenda.
2. Si los movimientos se ven bien, marca **«Compartir la receta con la comunidad»**: se abre aquí un issue con **solo la receta**
   (nombres de columnas y formatos), nunca tus movimientos.
3. Alguien de la comunidad la revisa y la suma a [`recetas/`](recetas/).

¿Prefieres escribirla a mano? El formato está en
[alcancia/recetas/README.md](https://github.com/alcancia-app/alcancia/blob/main/recetas/README.md). Abre un
[issue de receta](https://github.com/alcancia-app/alcancia-catalogo/issues/new?template=receta.yml) o un pull request con
`recetas/<id>.json`.

## Reglas
- **Nunca subas tu cartola** ni pegues movimientos, montos, nombres, RUT o números de cuenta, ni siquiera "para probar". Si hace
  falta un ejemplo, inventa dos o tres filas que respeten las columnas.
- Una receta por archivo, llamada como su `id` (`cl-banco-ejemplo.json`). El `id` empieza con el código del país.
- Cada receta pasa por `recetas.validar` de Alcancía (lo revisa GitHub en cada pull request).
- Las recetas que alguien probó con una cartola real llevan `"notas": "Probada con cartola real (mes/año)"`. Las de este catálogo pueden
  pasar a venir incluidas en la app.

## Licencia
Las recetas son de dominio público ([CC0 1.0](LICENSE)): cualquiera puede usarlas, también otras apps de finanzas.

---

¿Un problema de seguridad? Avísanos en privado: [`SECURITY.md`](SECURITY.md).

## English
Community-made **recipes** that teach [Alcancía](https://github.com/alcancia-app/alcancia) how to read bank and wallet statements
from anywhere in the world. Recipes are data-only JSON files. Share yours from the app (only the recipe is shared, never your
transactions) or open a recipe issue / pull request. Never upload real statements or personal data. Public domain (CC0 1.0).
