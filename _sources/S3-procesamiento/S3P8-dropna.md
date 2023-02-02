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

# Manejar datos nulos

```{code-cell} ipython
:tags: ["remove-cell"]
import pandas as pd

muestra_covid = pd.read_csv('../data/muestra_covid.csv')
geolocalizacion = pd.read_csv('../data/geolocalizacion.csv')
```

Los datos nulos corresponden a información que no se consignó, ya fuese en la creación del archivo o en la entrada de datos. Nuevamente, esta es una decisión de diseño del modelo de datos y no todos los casos son iguales, así que hay que tener en cuenta que no todos los conjuntos de datos requerirán las mismas acciones.

## `dropna()`

Esta función elimina los valores nulos de un conjunto de datos. Su sintaxis es:

```python
df.dropna()
```

Por ejemplo, si la aplicamos a los datos de `muestra_covid` tendremos el siguiente resultado:

```{code-cell} ipython
sin_nulos = muestra_covid.dropna()
print(sin_nulos.shape)
sin_nulos.head()
```

Ahora tenemos un conjunto de datos más sintetizado. Demasiado sintético diría yo. El inconveniente con usar este método de manera simple es que cualquier fila que contenga un valor nulo será eliminada. Por lo tanto, solamente tendremos 783 casos en los que toda la información es válida. 

Una solución menos "radical" podría ser eliminar los valores nulos solamente de una columna, por ejemplo, `municipio_residencia`:

```{code-cell} ipython
sin_nulos = muestra_covid.dropna(subset=['municipio_residencia'])
print(sin_nulos.shape)
sin_nulos.head()
```

En este caso tendremos un número un tanto más significativo de casos (149,707).

Aparentemente hemos perdido mucha información, pero en realidad hemos segmentado el conjunto de datos para seleccionar solamente aquellos que podamos representar en un mapa. Como conservamos nuestro conjunto de datos original, incluso nuestro dataframe segmentado (`muestra_covid`), no debemos preocuparnos por perder la información de sexo, edad, etc; que no esté asociada a una ubicación geográfica.

## `fillna()`

Otra función para lidiar con valores nulos es `fillna()`. Esta función reemplaza los valores nulos por un valor específico. Su sintaxis es:

```python
df.fillna(valor)
```

Ciertas operaciones en `pandas` no pueden lidiar con datos nulos, pero no siempre (como vimos arriba) podemos eliminar esos campos. Por esa razón, esta función permite llenar estos campos con un valor constante con el que podremos trabajar posteriormente. 

```{admonition} Una aclaración
:class: tip
Aunque podemos asignar cualquier valor a `fillna()` es importante que seamos coherentes con el tipo de dato de la columna que estamos transformando. Por ejemplo, si la columna `fecha_diagnostico` es de tipo `int64`, entonces `fillna()` debe ser de tipo `int64`. 

Además, en todos los casos, el valor debe ser similar a un valor nulo. Por ejemplo, `0` o `'N/A'` son valores que pueden reemplazar a un valor nulo. 
```

Al igual que en `dropna()` si usamos un valor indistintamente de la columna, se reemplazarán todos los valores nulos de todo el dataframe:

```{code-cell} ipython
nulos_reemplazados = muestra_covid.fillna('N/A')
nulos_reemplazados.head()
```

En este caso, el reemplazo en `municipio_residencia` es claro, pero en `fecha_def` puede llevar a errores (por ejemplo, cuando tratemos de cambiar los valores de `fecha_def` a `datetime64[ns]`). Otro inconveniente es que no es posible establecer una fecha `0` (recuerda lo que dijimos al respecto en la sección dedicada a [variables cuantitativas y cualitativas](../S2-estructuras-preparacion/S2P5-operaciones-datos.md) sobre las escalas de intervalo). Por lo que en este caso, la decisión más adecuada podría ser reemplazar únicamente los valores nulos de la columna `municipio_residencia` con `'NO APLICA'`.

```{code-cell} ipython
nulos_reemplazados = muestra_covid.fillna({'municipio_residencia': 'NO APLICA'}) # usamos 'NO APLICA' como valor pues es el que se utiliza en el dataset original para otras categorías
nulos_reemplazados.head()
```

## ¿Cómo saber cuáles columnas tienen valores nulos?

En conjuntos grandes de datos, es posible que no identifiquemos un valor nulo hasta el momento que nos encontremos con un mensaje de error. Por esta razón, es probable que queramos obtener las columnas que tengan valores nulos antes de proceder con un dataframe. Para ello, podemos usar la función `isnull()` aplicada a una columna en específico, combinada con el método `.loc`:

```{code-cell} ipython
es_nula = muestra_covid.loc[muestra_covid['fecha_def'].isnull()]
es_nula
```

Puedes combinar este método con un loop para obtener una lista de las columnas que contienen valores nulos:

```{code-cell} ipython
nulas = []
for col in muestra_covid:
    if muestra_covid[col].isnull().any(): # la función `any()` devuelve `True` si alguna de las filas contiene un valor nulo
        nulas.append(col)
nulas
```

Este loop lo puedes aplicar a cualquier dataframe, sin importar la cantidad de columnas que tenga.
