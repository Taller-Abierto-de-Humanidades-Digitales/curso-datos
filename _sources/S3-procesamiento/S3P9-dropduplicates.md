---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Eliminar duplicados

Un conjunto de datos puede tener duplicados, es decir, registros que tienen los mismos valores en todas sus columnas. Para eliminar estos duplicados, se puede utilizar la función `drop_duplicates()`, por ejemplo, lo puedo usar en el siguiente código:

```{code-cell} ipython
:tags: ["remove-cell"]
import pandas as pd

muestra_covid = pd.read_csv('../data/muestra_covid.csv')
geolocalizacion = pd.read_csv('../data/geolocalizacion.csv')
```

```{code-cell} ipython
print(f'Antes de eliminar duplicados: {muestra_covid.shape}')
sin_duplicados_mc = muestra_covid.drop_duplicates()
print(f'Después de eliminar duplicados: {sin_duplicados_mc.shape}')
```

¡No se eliminó ningún caso! Esto se debe a que no existen duplicados en nuestro conjunto de datos.

Veamos un caso de ejemplo solamente para que puedas ver como funciona la función `drop_duplicates()`.

Si tenemos el siguiente listado de estudiantes:

```{code-cell} ipython
estudiantes= pd.DataFrame(
    {'Nombre': ["Andrea", "Berenice", "Carlos", "Camila", "Guadalupe", "Andrea", "Jorge", "Berenice", "Carlos"],
     'Calificaciones': [10, 8, 9, 7, 6, 10, 8, 9, 7]})
estudiantes
```

Podemos filtrar un nuevo conjunto de datos eliminando los duplicados:

```{code-cell} ipython
sin_duplicados_estudiantes = estudiantes.drop_duplicates()
print(f'Estudiantes con duplicados: {estudiantes.shape}')
print(f'Estudiantes sin duplicados: {sin_duplicados_estudiantes.shape}')
sin_duplicados_estudiantes
```

No era sencillo identificar a simple vista (incluso en un conjunto de datos tan pequeño) que `Andrea` estaba duplicada en el conjunto de datos. En un conjunto de datos grande, en particular uno construido a partir de la unión de dos conjuntos de datos, esta función puede ser de muchísima utilidad.

```{admonition} Sin embargo
:class: warning
Es relevante tener en cuenta que si eliminamos un identificador que pueda filtrar a un caso único (por ejemplo, números de identificación de usuarios), es posible que se eliminen filas de manera errónea.
```

```{admonition} Importante
:class: tip
Esta función no elimina coincidencias en una columna, para ello podemos utilizar el método `.loc`.
```
