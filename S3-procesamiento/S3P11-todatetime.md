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

# Cambiar datos a fechas

```{code-cell} ipython
:tags: ["remove-cell"]
import pandas as pd

muestra_covid = pd.read_csv('../data/muestra_covid.csv')
geolocalizacion = pd.read_csv('../data/geolocalizacion.csv')
```

Otra transformación común en los conjuntos de datos es aquella relacionada con los datos temporales. Vimos en la sección dedicada a los [tipos de datos](../S2-estructuras-preparacion/S2P4-dtypes.md) las diferencias entre los tipos temporales `datetime` y `timedelta`. Incluso realizamos un ejercicio de transformar dos columnas al tipo `datetime` y hacer un cálculo con ellas.

En ese caso, utilizamos la siguiente sintaxis:

```python
df['columna'] = pd.to_datetime(df['columna'])
```

Como en otras formas de transformación de datos, le solicitamos a `pandas` que transforme la 'Serie' o columna `columna` a un tipo `datetime`.

Para nuestro conjunto de datos `muestra_covid` requeriremos asegurarnos que tengamos datos de tipo `datetime` para las siguientes columnas

```python
fecha_ingreso           object
fecha_sintomas          object
fecha_def               object
```

Debido a que sabemos exactamente qué columnas queremos modificar, podemos pasarlas como una lista y luego transformarlas a `datetime`.

```{code-cell} ipython
columnas = ['fecha_ingreso', 'fecha_sintomas', 'fecha_def']
for columna in columnas:
    muestra_covid[columna] = pd.to_datetime(muestra_covid.loc[:, columna])

muestra_covid.dtypes
```

```{admonition} SettingWithCopyWarning
:class: tip
Esta advertencia se debe a que estamos intentando modificar una columna que es una copia del original. Como `pandas` no puede saber si esto era lo que realmente queríamos hacer, nos envía esa advertencia. Por lo pronto podemos pasarla por alto, pero si deseas profundizar en ello, podrías revisar la [documentación de `pandas`](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy).
```

Funcionó perfectamente, ¿no es así? Esto es porque el formato de fecha original tiene un formato identificable ('AAAA-MM-DD'), incluso si no tiene un formato tan explícito (por ejemplo 'AAAAMMDD'), `pandas` lo podría reconocer. 

Sin embargo, no todos los campos que pudieran ser de fecha pueden ser convertidos de manera automática. Por ejemplo, si tuviésemos un conjunto de datos como el siguiente:

```{code-cell} ipython
fecha = pd.DataFrame({'fecha': ['12 de enero de 2022', '15 de febrero de 2022']})
fecha
```

Al intentar transformarlo nos daría un error.

```{code-cell} ipython
fecha['fecha'] = pd.to_datetime(fecha['fecha'])
```

Notarás que tenemos un error `ParserError` porque `pandas` no puede reconocer la fecha a la que nos referimos, en buena medida porque no tiene un soporte de multilengua. En cambio si estuviese escrito en inglés, podría ser convertido.

```{code-cell} ipython
fecha = pd.DataFrame({'fecha': ['January 12 2022', 'February 26 2022']})
fecha['fecha'] = pd.to_datetime(fecha['fecha'])
fecha
```

En este momento, es suficiente con tener en cuenta estas advertencias. Si tu conjunto de datos pudo ser manipulada de manera correcta con los procesos que vimos anteriormente, estás listo para realizar la visualización de datos. Si quieres aprender un poco más o requieres de alguna transformación adicional, puedes pasar a la siguiente sección.
