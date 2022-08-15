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

# Combinar fuentes de datos

En las bases de datos relacionales, combinar tablas es una de las tareas más comunes y necesarias. Por lo general, la información se divide para hacerla más fácil de gestionar y por ello al recuperarla necesitamos combinarlas para obtener un resultado coherente en una sola tabla.

Para este ejercicio necesitaremos dos fuentes de datos, así que aprovecharé el "Catálogo Único de Claves de Áreas Geoestadísticas Estatales, Municipales y Localidades" que proveé el [INEGI](https://www.inegi.org.mx/app/ageeml/) para obtener las coordenadas geográficas de los municipios que se anotan en el conjunto de datos por Covid.

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
```

```{code-cell} ipython
import pandas as pd
ruta_areas_inegi = '../data/AGEEML_2022842026272.csv'
areas_inegi = pd.read_csv(ruta_areas_inegi)
print(areas_inegi.shape)
areas_inegi.head()
```

Verás que nuestro nuevo conjunto de datos contiene 300,083 filas y 19 columnas. Además de los datos correspondientes a las coordenadas geográficas tenemos otros datos como la altitud, el total de población (total y por sexos), el total de viviendas habitadas, entre otros datos relacionados con claves de entidades.

Tenemos como dato común los municipios de residencia de los casos por Covid y el nombre del municipio (`Nom_Mun`) de los datos del INEGI. Ya que aprendimos a renombrar las columnas, aprovechemos para renombrar las columnas de las coordenadas de tal manera que podamos crear una columna común sobre la cual hacer la unión.

```{code-cell} ipython
areas_inegi.rename(
    columns={'Nom_Mun':'municipio_residencia'}, # recordemos que cambiamos el nombre de la columna en el ejercicio anterior
    inplace=True)
areas_inegi.head()
```

Ahora sí podremos empezar a "jugar" con nuestros datos para lograr un conjunto de datos con la información de geolocalización.

## "Inner" merge

De manera predeterminada, `pandas` combina nuestros datos con una unión "inner", es decir, que encuentra la información común de ambos conjuntos de datos y excluye la que no está en ambos. Podemos representar lo anterior a través de este diagrama de Venn:

```{image} ../_static/imgs/merges/inner.jpeg
:align: center
```

Para hacer la unión de nuestros datos usaremos la siguiente sintaxis:

```python
pd.merge(left, right, how='inner')
```

Lo cual se traduce en:

```{code-cell} ipython
inner_merge = pd.merge(covid_nacional, areas_inegi, how='inner', on='municipio_residencia')
inner_merge.head()
```

Pero ¡este no es el resultado que esperábamos! ¿Por qué nos regresa una tabla vacía pero con 59 columnas?

Esto es fácil de identificar: `pandas` no encuentra datos comunes porque la información del conjunto de datos de `covid_nacional` está escrito en mayúsculas sostenidas y la información del conjunto de datos de `areas_inegi` está escrito en mayúsculas y minúsculas. Más adelante veremos con mayor detalle como "normalizar" nuestros datos para evitar estas inconsistencias.

Por lo pronto, podemos transformar nuestros datos a minúsculas en la columna `municipio_residencia` tanto en `covid_nacional` como en `areas_inegi` para que podamos hacer la unión. Afortunadamente, ambos conjuntos de datos conservan la acentuación gráfica de los datos, lo que nos facilita su unificación.

```{code-cell} ipython
covid_nacional['municipio_residencia'] = covid_nacional['municipio_residencia'].str.lower()
areas_inegi['municipio_residencia'] = areas_inegi['municipio_residencia'].str.lower()
```

Ahora, apliquemos nuevamente la unión a nuestro conjunto de datos. Pero primero, vamos a reducir nuestro conjunto de datos para hacerlo más manejable.

```{admonition} ¿Por qué reducimos los datos?
:class: tip
Al experimentar con grandes conjuntos de datos es altamente recomendable ser amable con los recursos computacionales. Si hacemos estos ejercicios directamente con todo el conjunto de datos nos tomará más tiempo y estaremos expuestos a errores de memoria.
```

```{code-cell} ipython

covid_nacional_tm = covid_nacional[:100] # reducimos el conjunto de datos a 100 filas

inner_merge = pd.merge(covid_nacional_tm, areas_inegi, how='inner', on='municipio_residencia')
print(inner_merge.shape)
inner_merge.head()
```

Ahora estamos enfrentándonos a otro problema: ¡el resultado de la unión son 624 filas! ¿Por qué? Esto se debe a que los datos de `municipio_residencia` no están asociados con un campo único. Esto lo podemos ver aquí:

```{code-cell} ipython
areas_inegi.loc[areas_inegi['municipio_residencia'] == 'chalco']
```

Al hacer el merge, el conjunto de datos se multiplica por las coincidencias, encontrándonos así con una tabla que nos da información inconsistente.

```{admonition} ¡importante!
:class: tip
Un error común al hacer un merge es terminar con un conjunto de datos mucho mayor del esperado. Esto se debe a que provienen de fuentes diferentes y no se puede predecir con exactitud cuántos datos se obtendrán.
Por esta razón es **fundamental** asegurarse de que el conjunto de datos resultante sea el esperado. Una manera práctica de hacerlo es valiéndose del módulo shape. Si el resultado es un número inconsistente (por ejemplo, que 100 casos de Covid se convirtieran en 624) debemos revisar dónde se encuentra el error. 

Lastimosamente no existe una fórmula que abarque todos los casos, así que este es un paso que depende en buena medida de nuestra capacidad para detectar errores.
```

Tendremos finalmente que hacer una depuración de los datos de `areas_inegi_tm` para que coincida con nuestros datos. Encontramos que el registro de datos de `covid_nacional` usa como `municipio_residencia` el nombre principal del municipio, en este caso, coincide con la clave `1` del campo `Cve_Loc` en `areas_inegi`. Segmentaremos nuestro conjunto de datos valiéndonos del método `.loc` y podremos hacer nuevamente nuestro 'inner merge'

```{code-cell} ipython
# segmentamos nuestro conjunto de datos de areas_inegi
areas_inegi_tm = areas_inegi.loc[areas_inegi['Cve_Loc'] == 1]

# realizamos nuestro merge
inner_merge = pd.merge(covid_nacional_tm, areas_inegi_tm, how='inner', on='municipio_residencia')
print(inner_merge.shape)
inner_merge.head()
```

¡Eureka! Tenemos una tabla con el resultado esperado. ¿Cómo lo sabemos? (15 filas parece un número sospechoso) Porque coincide con el número de valores no nulos que nos regresa la columna `municipio_residencia` en `covid_nacional_tm`.

```{code-cell} ipython
covid_nacional_tm['municipio_residencia'].value_counts()
```

## Outer Merge

La unión "hacia afuera" es todo lo contrario a un "inner merge". En este caso, combinamos todos los campos de `covid_nacional` con todos los campos de `areas_inegi`, incluyendo aquellos que no coincidan. Así lo vemos en un diagrama de Venn:

```{image} ../_static/imgs/merges/outer.jpeg
:align: center
```

Apliquemos un "outer merge" a nuestro ejemplo anterior para ver los resultados:

```{code-cell} ipython
outer_merge = pd.merge(covid_nacional_tm, areas_inegi_tm, how='outer', on='municipio_residencia')
print(outer_merge.shape)
outer_merge.head()
```

Vemos que el resultado son 2,564 filas. Es una cantidad bastante grande, pero no es un error. Lo que sucede en este caso, es que se combinan los datos que coincide con los valores de `municipio_residencia` y se combinan los datos que no coinciden. Donde no hay coincidencias, las celdas se llenan con valores nulos.

Para nuestro ejemplo, una unión hacia afuera no es útil. Pero supongamos que tenemos un conjunto de datos de estudiantes con las calificaciones del primer trimestre:

```{code-cell} ipython
estudiantes_trimestre1 = pd.DataFrame(
    {'Nombre': ["Andrea", "Berenice", "Carlos"],
     'Calificaciones_T1': [10, 8, 9]})
estudiantes_trimestre1
```

Ahora, queremos agregar las calificaciones de otro conjunto de datos correspondiente al segundo trimestre:

```{code-cell} ipython
estudiantes_trimestre2 = pd.DataFrame(
    {'Nombre': ["Andrea", "Berenice", "Carlos"],
     'Calificaciones_T2': [9, 7, 8]})
estudiantes_trimestre2
```

En este caso, un 'outer merge' es indicado:

```{code-cell} ipython
outer_merge = pd.merge(estudiantes_trimestre1, estudiantes_trimestre2, how='outer', on='Nombre')
outer_merge
```

## A modo de cierre

Es necesario que selecciones tu método de unión de acuerdo a la lógica de tus datos. Revisa los resultados de tus combinaciones y ajusta los datos para que lleguen al resultado esperado. En ocasiones esto no es un proceso simple, tienes que reducir los datos y hacerlos manejables para que sea mucho más sencillo llegar a encontrar el error. Todas estas son prácticas que debes tener en cuenta y que no dependen del lenguaje de programación que estes utilizando.

## Para saber más

Existen otros métodos de unión de conjuntos de datos como el 'left merge' y el 'right merge', el método 'join' o la concatenación ('concat'). Para no extendernos más, quisiera sugerirles el capítulo 2 del libro de {cite}`stepanek_thinking_2020` donde se explica de manera sintética cómo utilizar estos métodos.
