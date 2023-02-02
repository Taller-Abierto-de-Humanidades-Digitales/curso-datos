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

# Segmentar la información

```{code-cell} ipython
:tags: ["remove-cell"]
import pandas as pd

try:
  covid_nacional = pd.read_csv('../data/casos_nacionales_covid-19_2022_semestre1.csv')
except FileNotFoundError:
  covid_nacional = pd.read_csv('../datos/casos_nacionales_covid-19_2022_semestre1.csv')

covid_nacional.rename(columns={
    "entidad_nac": "entidad_nacimiento",
    "entidad_res": "entidad_residencia",
    "municipio_res": "municipio_residencia"
}, inplace=True)

areas_inegi = pd.read_csv('../data/AGEEML_2022842026272.csv')

areas_inegi.rename(
    columns={'Nom_Mun':'municipio_residencia'}, # recordemos que cambiamos el nombre de la columna en el ejercicio anterior
    inplace=True)
```

No necesariamente es el primer paso para la limpieza de datos, pero es relevante filtrar la información para tener solamente aquella que nos sea de utilidad.

En el ejercicio de unión del dataframe, el resultado fue de un conjunto de datos con 59 columnas. Como vimos, algunas de estas no son particularmente útiles para nuestro análisis e incluso pueden derivar en errores.

Vamos entonces a segmentar la información de cada uno de nuestros dataframes para trabajar únicamente con la información que nos interesa para el ejercicio, básicamente, las variables con información socioeconómica.

```{admonition} Una aclaración
:class: tip
Obviamente este es un ejemplo de segmentación con unas variables que son de interés. Pero podrías querer en cambio revisar las correlaciones entre enfermedades previas y contagios o defunciones por Covid, en ese caso, las variables socioeconómicas no serían tan relevantes.
```

En el caso de `covid_nacional` nos interesa:

- `sexo`
- `edad`
- `entidad_nacimiento`
- `municipio_residencia`
- `indigena`
- `nacionalidad`
- `migrante`
- `pais_nacionalidad`
- `fecha_ingreso`
- `fecha_sintomas`
- `fecha_def`

Y para el caso de `areas_inegi` únicamente nos interesa:

- `municipio_residencia`
- `Lat_Decimal`
- `Lon_Decimal`

Y de este caso nos interesa además solamente las filas correspondan a la `Cve_Loc` igual a `1`.

## Segmentar por nombre de columna

Esta es una forma muy sencilla de segmentar la información. Simplemente, creamos una lista con las columnas que queremos y las asignamos a un nuevo dataframe, así:

```{code-cell} ipython
muestra_covid = covid_nacional[['sexo', 'edad', 'entidad_nacimiento', 'municipio_residencia', 'indigena', 'nacionalidad', 'migrante', 'pais_nacionalidad', 'fecha_ingreso', 'fecha_sintomas', 'fecha_def']]
muestra_covid.head()
```

En este caso, únicamente necesitamos indicar las columnas que queremos. Incluso podemos aprovechar y modificar el orden de aparición de las columnas.

```{admonition} ¡Cuidado!
:class: warning
La lista de columnas en `pandas` se hace en corchetes rectos dobles:

`[['item1', 'item2', 'item3']]`

Si lo haces de la forma tradicional (con corchetes rectos simples), tendrás un error
```

## Segmentar por columna y condición

En este caso, combinaremos el método `.loc` con la segmentación en columnas, así:

```{code-cell} ipython
geolocalizacion = areas_inegi.loc[areas_inegi['Cve_Loc'] == 1, ['municipio_residencia', 'Lat_Decimal', 'Lon_Decimal']]
geolocalizacion.head()
```

Este es un método bastante poderoso de `pandas` ya que nos ahorra varios pasos. En una misma línea, hacemos la búsqueda por coincidencia (`.loc`) y luego, separada por una coma, indicamos las columnas que queremos que regrese.

```{admonition} ¿por qué esta lista no tiene corchetes dobles?
:class: tip
Cuando le decimos a `pandas` que nos devuelva una serie de columnas, en realidad estamos usando un método `.loc`, aunque no lo declaremos de forma explícita. De hecho, podríamos decir:

`df.loc[:,'col1', 'col2', 'col3']`

Y sería el mismo resultado que 

`df[['col1', 'col2', 'col3']]`

```

Tenemos ahora dos conjuntos de datos mucho más manejables que antes. Con esto podremos pasar al siguiente paso, que consiste en lidiar con datos vacíos.
