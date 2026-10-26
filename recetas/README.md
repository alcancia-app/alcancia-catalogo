# Recetas

Una receta por archivo: `recetas/<id>.json`. El formato completo está en
[alcancia/recetas/README.md](https://github.com/alcancia-app/alcancia/blob/main/recetas/README.md).

Para probar una receta en tu computador sin guardar nada:
```bash
cp cl-mi-banco.json ~/Alcancia/.alcancia/recetas/
python3 bin/importar.py vista mi-cartola.csv /tmp/vista.json && cat /tmp/vista.json   # desde el código de Alcancía
```
