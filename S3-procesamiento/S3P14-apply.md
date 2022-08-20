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

# El método `apply()`

```{code-cell} ipython
:tags: ["remove-cell"]
import pandas as pd

muestra_covid = pd.read_csv('../data/muestra_covid.csv')
geolocalizacion = pd.read_csv('../data/geolocalizacion.csv')
```

Habrás notado que utilizamos el método `apply()` para realizar una transformación a [datos numéricos](../S3-procesamiento/S3P10-tonumeric.md) pero evitamos hacerlo en la transformación a [`datetime`](../S3-procesamiento/S3P11-todatetime.md). Esto se debe a que el método `apply()` es básicamente un `for loop` sobre una serie de filas de datos. En este sentido, no toda operación puede valerse de esta función para hacer una transformación. En este sentido, es muy útil el capítulo 6 del libro de {cite}`stepanek_thinking_2020`.

`apply()` es particularmente útil cuando lo utilizamos para realizar operaciones repetitivas a través de una función. Por ejemplo, construyamos una función simple para determinar el año de nacimiento de cada persona de `muestra_covid` tomando como base la edad:

```{code-cell} ipython
def calcular_edad(edad):
    return 2022 - edad
```

Así, podemos crear una columna que se llame `año_nacimiento` en la que se guarde el resultado de aplicar esta función a la columna `edad`.

```{code-cell} ipython
muestra_covid['año_nacimiento'] = muestra_covid.edad.apply(calcular_edad)
```

Este es un ejemplo muy simple (que tal vez no amerite el uso de `apply()`) pero permite ejemplificar cómo podría ser utilizado este método.

```{admonition} Otros usos
:class: tip
Uno de los usos más recurridos de `apply()` es combinarlo con la función `groupby()`. Un interesante ejemplo de cómo realizar esta aplicación está dado en el artículo {cite}`whorton_applying_2021`.
```
