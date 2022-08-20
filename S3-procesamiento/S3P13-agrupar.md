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

# Agrupar

```{code-cell} ipython
:tags: ["remove-cell"]
import pandas as pd

muestra_covid = pd.read_csv('../data/muestra_covid.csv')
geolocalizacion = pd.read_csv('../data/geolocalizacion.csv')
```

Las operaciones de agrupación suelen ser relevantes para analizar el comportamiento de los datos. En este caso, `pandas` regresa una 'serie' de datos con la información agrupada, por columna, de acuerdo con el criterio que nosotros consideremos relevante.

Por ejemplo, podemos agrupar nuestros datos por `sexo` y obtener un conteo de los valores:

```{code-cell} ipython
muestra_covid.groupby('sexo').count()
```

El resultado es un conteo que nos indica cuántos valores coinciden con la etiqueta `'HOMBRE'` y cuántos con `'MUJER'`.

Con valores numéricos, podemos realizar otras operaciones, por ejemplo, la media de edad:

```{code-cell} ipython
muestra_covid.groupby('sexo').edad.mean()
```

El resultado nos muestra la media de edad de los hombres y de las mujeres en todo nuestro conjunto de datos.

Igualmente lo podemos hacer con otras categorías. Por ejemplo:

```{code-cell} ipython
muestra_covid.groupby('indigena').edad.mean()
```

`groupby()` es una función muy útil y rápida para describir la información que tenemos, especialmente si es un conjunto de datos bastante grande.
