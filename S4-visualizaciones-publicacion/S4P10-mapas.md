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

# Mapas

La representación de datos en mapas ya implican una relación entre los valores que tenemos disponibles y las dimensiones geográficas de la información. Es importante señalar que nos referimos aquí a datos que pueden ser representados en un mapa, no a la representación del espacio en un plano o al análisis del espacio geográfico.

Desde la sección [combinar fuentes de datos](../S3-procesamiento/S3P5-union-df.md) hemos incorporado datos geográficos a nuestro conjunto de datos. Estos datos de geolocalización han sido incorporados tomando la información que nos brinda el INEGI y también mediante la incorporación de un estándar de códigos relacionados con las fronteras administrativas de los países (ISO 3166-1).

Gracias a esas dos estrategias de geolocalización de nuestros datos, podemos mostrar dos tipos de representaciones de datos en mapas. Para ello, también utilizaremos la librería `plotly`.

## Mapa de puntos

Para este ejemplo, usaremos los datos geolocalizados de los municipios de residencia de los casos por Covid-19 en México, tal como lo hicimos en la sección [combinar fuentes de datos](../S3-procesamiento/S3P5-union-df.md)

```{code-cell} ipython3
:tags: [remove-cell]
!pip install plotly
import plotly.express as px
import pandas as pd

casos_nacionales = pd.read_csv("../data/datos_mapa.csv", encoding="utf-8")
```

```{code-cell} ipython3
casos_nacionales.head()
```

Notarás que he depurado la fuente de datos para que tenga solamente las columnas necesarias y que ya realicé el conteo de los casos por municipio (`casos_nacionales['municipio_res'].value_counts().reset_index()`).

Ahora, simplemente es tarea de "dibujar" el mapa. Para eso, `plotly` cuenta con una función llamada `scatter_mapbox()` con la cual podemos hacer un mapa de puntos y, además, controlar el color y el tamaño de los puntos de acuerdo con un valor numérico. Veámos el código para hacer este mapa:

```{code-cell} ipython3
fig = px.scatter_mapbox(
    casos_nacionales, # <-- cargamos el conjunto de datos
    lat="Lat_Decimal", # <-- indicamos la columna con la latitud
    lon="Lon_Decimal", # <-- indicamos la columna con la longitud
    color='casos', # <-- indicamos la columna con el valor numérico para el color
    size='casos', # <-- indicamos la columna con el valor numérico para el tamaño del punto
    hover_name="municipio_residencia", # este parámetro permite indicar un texto que se mostrará al pasar el mouse sobre el punto
    hover_data=["casos"], # este parámetro permite indicar uno o varias columnas con datos que se mostrará al pasar el mouse sobre el punto
    color_continuous_scale=px.colors.cyclical.IceFire, # <-- indicamos el esquema de colores
    size_max=50, # <-- indicamos el tamaño máximo de los puntos
    zoom=4 # <-- indicamos el nivel de zoom inicial
    )

fig.update_layout(mapbox_style="open-street-map") # con este parámetro vamos a establecer el mapa base, en este caso, OpenStreetMap
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) # con este parámetro vamos a establecer los márgenes del mapa (0 en todos los lados)

fig.show() # <-- mostramos el mapa
```

Esta es una buena ilustración de cómo dibujar un mapa, aunque podría ser más preciso, por ejemplo, si en lugar de valores totales hiciéramos una representación por cada 100 mil habitantes. Para no atiborrarlos con código, les dejo simplemente el conjunto de datos con la tasa de incidencia por cada 100 mil habitantes [^footnote]:

```{code-cell} ipython3
:tags: [remove-cell]
casos_nacionales = pd.read_csv("../data/datos_mapa_tasa.csv", encoding="utf-8")
```

```{code-cell} ipython3
casos_nacionales.head()
```

Ahora, vamos a reutilizar el código del mapa anterior, solamente cambiando los valores de las columnas donde se indican los valores numéricos para el color y el tamaño de los puntos:

```{code-cell} ipython3
fig = px.scatter_mapbox(
    casos_nacionales, 
    lat="Lat_Decimal", 
    lon="Lon_Decimal",
    color='tasa_incidencia',
    size='tasa_incidencia',
    hover_name="municipio_residencia",
    hover_data=["casos", "Pob_Total", "tasa_incidencia"],
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=50,
    zoom=4
    )

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()
```

¡Es otro mapa! Con los valores totales, tal como los mostramos en el primer mapa, vemos una concentración de los casos en el centro del país, como es lógico, por la densidad poblacional. Al normalizar los datos para equilibrar esta variable, vemos que el mapa modifica su representación, mostrando una mayor incidencia en áreas que anteriormente parecían menos afectadas. Efectivamente, no es lo mismo 24,107 casos en una población de 1'643,623 habitantes (Ecatepec) que 154 casos en una población de 698 habitantes (Melchor Ocampo, Zacatecas).

Interesante, ¿no es así? Reitero, ambos mapas contienen información correcta, pero siempre hay que ser honestos con la manera en la que construimos nuestros datos y las falencias de nuestra representación. ¿Es posible que con un censo poblacional actualizado las representaciones fuesen diferentes? Tal vez, no podemos asegurar lo contrario. Como toda representación, incluso estadística, estamos haciendo una abstracción de la realidad, y esto simplemente refiere a que no podemos tener todos los parámetros en cuenta.

Ahora que ya nos divertimos con un mapa de puntos, vamos a ver un mapa coroplético.

## Mapas coropléticos

Los mapas coropléticos son mapas en los que se representan áreas geográficas con un color correspondiente a una escala definida por un valor numérico. Son como los mapas de divisiones administrativas tradicionales, pero en lugar de seleccionar el color por una convención o un criterio estilístico, este está determinado por una escala cuantitativa.

Recordemos que en la sección [georeferenciar](../S3-procesamiento/S3P15-georeferenciar.md) acotamos los valores para que nos mostraran los casos relacionados con el país de origen de las personas extranjeras contagiadas o atendidas en México. Ahora, vamos a hacer un mapa coroplético con esos datos:

```{code-cell} ipython3
:tags: [remove-cell]
mapa_extranjeros = pd.read_csv("../data/muestra_georef_covid.csv", encoding='utf-8')
mapa_extranjeros = mapa_extranjeros.loc[mapa_extranjeros['alpha3'] != 'MEX']
extranjeros = mapa_extranjeros.dropna(subset=['alpha3'])
# group by pais_nacionalidad, alpha3 y alpha2
grupoext = extranjeros.groupby(['pais_nacionalidad', 'alpha3', 'alpha2']).count().reset_index()

# rename column Unnamed: 0 to casos
grupoext.rename(columns={'Unnamed: 0': 'casos'}, inplace=True)

# drop columns
grupoext.drop(columns=['sexo','edad','entidad_nacimiento','municipio_residencia','indigena','nacionalidad','migrante','fecha_ingreso','fecha_sintomas','fecha_def'], inplace=True)
grupoext = grupoext.drop_duplicates(subset=['alpha3', 'alpha2'])
```

```{code-cell} ipython3
fig = px.choropleth(grupoext, locations='alpha3', locationmode='ISO-3', projection='natural earth', color='casos', hover_name='pais_nacionalidad', hover_data=['casos'], color_continuous_scale=px.colors.sequential.Greens)
fig.show()
```

Como vemos, el peso de Estados Unidos es tan grande, que prácticamente no se puede apreciar el resto de los países. Para poder verlos, vamos a restringir el rango de valores de la escala:

```{code-cell} ipython3
fig = px.choropleth(grupoext, locations='alpha3', locationmode='ISO-3', projection='natural earth', color='casos', hover_name='pais_nacionalidad', hover_data=['casos'], color_continuous_scale=px.colors.sequential.Greens, range_color=[0, 1000])
fig.show()
```

Los contrastes ahora son más evidentes, aunque es indispensable tener en cuenta que este gráfico puede llevar a errores, puesto que Estados Unidos queda por encima de la escala y esto puede llevar a interpretaciones erróneas. Podríamos ver qué sucede si aplicamos una escla logarítmica:

```{code-cell} ipython3
import numpy as np
fig = px.choropleth(grupoext, locations='alpha3', locationmode='ISO-3', projection='natural earth', color='casos', hover_name='pais_nacionalidad', hover_data=['casos'], color_continuous_scale=px.colors.sequential.Greens, color_continuous_midpoint=np.log(100))
fig.show()
```

Muy similar a la primera, ¿no es así? Existen diferentes posibilidades estadísticas para normalizar los datos, de manera tal que podamos compararlos mejor. En este caso, nuestros datos tienen tal variabilidad (la diferencia entre el valor mayor y el menor es tremenda) por lo que solamente en el caso de nuestro segundo mapa (en el que modificamos la escala para restringir el rango) podemos ver los datos de manera más clara.

## Mapas animados

Los mapas animados son mapas en los que se representan áreas geográficas con un color correspondiente a una escala definida por un valor numérico, pero en este caso, el color cambia a lo largo del tiempo. Es decir, en lugar de ver un mapa estático, podemos ver cómo cambia la situación en el tiempo.

Para hacer un mapa animado, tenemos que determinar una columna con datos temporales. En nuestro caso, vamos a usar la fecha de ingreso de los casos.

```{code-cell} ipython3
:tags: [remove-cell]
diario = extranjeros.groupby(['fecha_ingreso', 'pais_nacionalidad', 'alpha3', 'alpha2']).count().reset_index()
diario.rename(columns={'Unnamed: 0': 'casos'}, inplace=True)
diario.drop(columns=['sexo','edad','entidad_nacimiento','municipio_residencia','indigena','nacionalidad','migrante', 'fecha_sintomas','fecha_def'], inplace=True)
```

```{code-cell} ipython3
fig = px.choropleth(diario, locations="alpha3", color="casos", hover_name="pais_nacionalidad", projection="natural earth", animation_frame="fecha_ingreso", color_continuous_scale=px.colors.sequential.Plasma)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

Si das clic en el botón de play, podrás ver cómo cambia la situación en el tiempo. La escala de tiempo navega diariamente entre el 1 de enero y el 10 de junio, rango de fecha de los datos, mostrando una escala continua de colores.

Con estos ejemplos tendrás algunos elementos para poder seleccionar una representación de tus datos en un mapa. Esta es una de las representaciones más socorridas en la actualidad y es una de las más narrativas por la familiaridad que tenemos con las representaciones cartográficas.

No dejes de investigar estas visualizaciones y experimenta para encontrar una representación que te permita contar una historia con tus datos.

## Notas

[^footnote]: Este cálculo obviamente no es preciso, puesto que la población se calcula con base en el censo de 2020, pero por lo menos puede darnos un aproximado a la tasa actual.
