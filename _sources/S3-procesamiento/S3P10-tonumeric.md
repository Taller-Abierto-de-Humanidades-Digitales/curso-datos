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

# Asegurar datos numéricos

Como vimos en la sección dedicada a [tipos de datos en `pandas`](../S2-estructuras-preparacion/S2P4-dtypes.md), los tipos de datos con los que podremos realizar operaciones son `int64` y `float64`. También vimos que en la mayoría de ocasiones, estos tipos pueden estar expresados en forma de tipo `object`. Incluso, algunos de estos datos están en forma de `string`.

```{admonition} Nota
:class: note
Para este apartado usaré datos de ejemplo porque nuestros conjuntos de datos `muestra_covid` y `geolocalizacion` no necesitan una transformación adicional.

Revisa tu conjunto de datos para saber si esta es una operación necesaria o no.
```

Al igual que en las operaciones anteriores, `pandas` incluye una función que permite convertir los datos a un tipo numérico.

```{code-cell}
import pandas as pd
s = pd.Series(["1", "2", "3", "4", "5"])
print(s.dtypes)
pd.to_numeric(s)
```

Notarás que cuando llamamos a la función `to_numeric`, los datos se convierten a tipo `int64` y de la misma manera lo puede hacer con cualquier columna que contenga datos numéricos. Sin embargo, no puede hacerlo con todo el dataframe al mismo tiempo, por ejemplo:

```{code-cell}
df = pd.DataFrame({"A": ["Camila", "Sebastián", "Santiago", "Jimena", "Hannah"], "B": ["1.5", "1.2", "2.3", "4.5", "5.6"], "C": ["1", "2", "3", "4", "5"]})
print(df.dtypes)
pd.to_numeric(df)
```

Lo anterior nos arroja un `TypeError` porque `pandas` estaba esperando una `Serie`, es decir, el conjunto de datos de una sola columna.

Para transformar estos datos podemos utilizar el método tradicional de `for loop` así:

```{code-cell}
for col in df.columns:
  try:
    df[col] = pd.to_numeric(df[col])
  except ValueError:
    pass

df.dtypes
```

El problema con este método es que es un poco lento. De hecho, en un conjunto de datos como `covid_nacional` tomaría muchos minutos y gastaría mucha memoria, tanto que podría simplemente bloquear la computadora.

En términos de eficiencia es mejor utilizar el método de `pandas` `apply()`. Veremos un poco más sobre el uso de este método en la sección dedicada a [`apply()`](../S3-procesamiento/S3P14-apply.md), pero por lo pronto veremos un ejemplo de como usarlo.

```{code-cell}
df = pd.DataFrame({"A": ["Camila", "Sebastián", "Santiago", "Jimena", "Hannah"], "B": ["1.5", "1.2", "2.3", "4.5", "5.6"], "C": ["1", "2", "3", "4", "5"]})
cols = df.columns.drop('A') # Eliminamos la columna que sabemos tiene valores de texto
df[cols] = df[cols].apply(pd.to_numeric)
df.dtypes
```

```{admonition} Observación
:class: tip
La conversión de datos numéricos, así como la de fechas, que veremos a continuación, es una operación que se realiza sobre una sola columna. Por esa razón es importante que hayas realizado previamente la [identificación de tipos de datos](../S2-estructuras-preparacion/S2P4-dtypes.md).
```
