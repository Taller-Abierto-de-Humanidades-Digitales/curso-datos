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

# `to_csv`

Después de realizar todas las operaciones, podemos guardar el resultado en un archivo csv para reutilizarlo o compartirlo. `Pandas` incluye una función que facilita esta tarea, el único requisito consiste en indicar el nombre del archivo y la ruta donde se guardará.

Vamos a asegurar que tenemos el conjunto de datos que requerimos, con la información limpia, procesada y transformada.

```{code-cell} ipython
:tags: ["remove-cell"]
import pandas as pd

muestra_covid = pd.read_csv('../data/muestra_covid.csv')
geolocalizacion = pd.read_csv('../data/geolocalizacion.csv')
```

Utilizaremos los conjuntos de datos que [segmentamos previamente](../S3-procesamiento/S3P7-segmentar.md) y los uniremos siguiendo lo que observamos en la sección [combinar fuentes de datos](../S3-procesamiento/S3P5-union-df.md).

```{code-cell} ipython
covid_clean = pd.merge(muestra_covid, geolocalizacion, how='inner', on='municipio_residencia')
```

Llenamos los valores nulos con 'NO APLICA' para que no sean considerados en el análisis. Dejaremos como valores nulos los correspondientes a `fecha_def` para poder hacer la transformación de fechas.

```{code-cell} ipython
covid_clean.fillna({'municipio_residencia': 'NO APLICA', 'pais_nacionalidad': 'NO APLICA'}, inplace=True)
```

Transformamos los valores de las columnas `['fecha_ingreso', 'fecha_sintomas', 'fecha_def']` a `datetime64[ns]`.

```{code-cell} ipython
columnas = ['fecha_ingreso', 'fecha_sintomas', 'fecha_def']
for columna in columnas:
    muestra_covid[columna] = pd.to_datetime(muestra_covid.loc[:, columna])

muestra_covid.dtypes
```

Y con esto tenemos listo nuestro conjunto de datos para guardarlo en un archivo csv.

```{code-cell} ipython
ruta = '../data/covid_clean.csv'
covid_clean.to_csv(ruta, index=False) # Recuerda modificar la ruta a tu Drive. Debe ser algo como '/content/drive/MyDrive/Tu Directorio/elnombredetucsv.csv'
```

Y para comprobar que lo hicimos correctamente:

```{code-cell} ipython
pd.read_csv(ruta)
```

¡Excelente! Ya estás listo para entregar la actividad de cierre de esta semana y proceder a la visualización de datos.
