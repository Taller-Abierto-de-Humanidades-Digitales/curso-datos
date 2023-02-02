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

# Selección de datos

Una operación fundamental cuando trabajamos con datos consiste en seleccionar los datos que nos interesan. Por ejemplo, en los datos de casos de Covid que hemos utilizados, podremos seleccionar de ellos cuáles corresponden a mujeres y a partir de allí realizar otras operaciones de datos. Es un ejemplo simple, pero es una operación común que vamos a realizar continuamente.

## El método `.loc`

Este es la forma más intuitiva de realizar una selección en nuestro conjunto de datos. Lo que se consigue con este método es filtrar por coincidencias en una columna a partir de las condiciones que se especifiquen. Por ejemplo:

```{code-cell}
:tags: ["remove-cell"]
import pandas as pd
try:
  covid_nacional = pd.read_csv('../data/casos_nacionales_covid-19_2022_semestre1.csv')
except FileNotFoundError:
  covid_nacional = pd.read_csv('../datos/casos_nacionales_covid-19_2022_semestre1.csv')
```

```{code-cell}
casos_mujeres = covid_nacional.loc[covid_nacional['sexo'] == 'MUJER']
casos_mujeres.head()
```

En este caso, le dijimos a `pandas` que busque en la columna `sexo` los valores que sean iguales a `MUJER` y los muestre. Como habrás notado, el operador `==` indica igualdad. Este es un operador lógico, por lo que no es necesario que el valor a comparar sea numérico. Podemos utilizar el mismo método para localizar un valor numérico, por ejemplo, las mujeres que tengan edad de 25 años:

```{code-cell}
mujeres_25 = casos_mujeres.loc[casos_mujeres['edad'] == 25]
mujeres_25
```

```{admonition} Para resaltar
:class: tip
* Nota que en el caso del valor numérico no lo incluimos entre paréntesis. Eso es fundamental porque, como recordarás, en la columna `edad` el tipo de dato es numérico (`int64`).
* Para evitar procesar todo el dataframe nuevamente, lo que hicimos fue acotar el *grupo* que hicimos con el primer resultado (`casos_mujeres`). 
```

En ocasiones, vamos a querer descartar un valor en particular de una columna que contiene muchos elementos. Por ejemplo, en la columna `entidad_nac` (entidad de nacimiento de la persona) podemos querer seleccionar los valores que no sean `CIUDAD DE MÉXICO`:

```{code-cell}
entidad_nac_no_cdmx = casos_mujeres.loc[casos_mujeres['entidad_nac'] != 'CIUDAD DE MÉXICO']
entidad_nac_no_cdmx
```

Esta forma de seleccionar información es muy relevante cuando solamente nos interesa una parte de la información del conjunto de datos para analizar. Por ejemplo, si queremos averiguar los casos por un Estado en un conjunto de datos nacional, o las cifras nacionales en uno global.

### Método `.loc` en múltiples columnas

Los casos anteriores son bastante simples, y si te das cuenta, lo que hicimos fue hacer tres grupos para llegar al resultado deseado. `Pandas` nos ofrece la posibilidad de hacer una selección en múltiples columnas. Por ejemplo, si queremos seleccionar los casos de mujeres de 25 años de edad, nacidas en México, y que no sean de CDMX:

```{code-cell}
casos_mujeres_25_mexico = casos_mujeres.loc[(casos_mujeres['edad'] == 25) & (casos_mujeres['entidad_nac'] == 'MÉXICO') & (casos_mujeres['entidad_nac'] != 'CIUDAD DE MÉXICO')]
casos_mujeres_25_mexico
```

Si observas con atención, notarás que lo que hicimos fue encadenar varias peticiones en una sola. Para ello nos servimos del operador `&` ('and') que es un operador lógico [^footnote1].

O, los casos que corresponden a mujeres **o** migrantes. En este caso usaremos el operador `|`:

```{code-cell}
casos_mujeres_migrantes = covid_nacional.loc[(covid_nacional['sexo'] == 'MUJER') | (covid_nacional['migrante'] == 'SI')]
print(f'total casos: {casos_mujeres_migrantes.shape[0]}')
casos_mujeres_migrantes.head()
```

Notarás que se regresa una cantidad diferente de filas dependiendo del condicional. Esto simplemente se debe a que estamos utilizando un operador lógico. Así, `pandas` selecciona la información según lo siguiente[^footnote2]:

* busca (`loc`) las filas en la columna `sexo` que cumplen con la condición `'MUJER'` y con la condición `'SI'` en la columna `migrante`. Todas las filas que no cumplan con esa condición en ambas columnas serán descartadas.
* busca las filas de la columnna `sexo` que cumplan con la condición `'MUJER'` o las filas de la columna `migrante` que cumplan con la condición `'SI'`. En este caso, solamente descarta las filas que no cumplan con una de las condiciones. Por esa razón nos devolverá todos los casos donde aparezca `'MUJER'` en la columna `sexo` y todos los casos donde aparezca `'SI'` en la columna `migrante`.

## El método `.iloc`

El método `.iloc` permite seleccionar filas y columnas por su índice. Por ejemplo, si quisiera seleccionar las tres primeras filas del conjunto de datos:

```{code-cell}
tres_filas = covid_nacional.iloc[:3]
tres_filas
```

Ahora, podríamos seleccionar las columnas 1 a 5 de las filas 1 a 3:

```{code-cell}
filas_columnas = covid_nacional.iloc[:3, 1:5]
filas_columnas
```

En información muy bien estructurada, este método permite acceder a información sin preocuparnos por el tipo de dato o la forma en la cual fue escrita la celda. En general, si la información es creada a través de un gestor de base de datos el método `.iloc` puede ser muy útil. Es además más rápido que el método `.loc`, puesto que no tiene que buscar coincidencias sino seleccionar información dentro de una matriz.

## Notas

[^footnote1]: En Python el posible utilizar el operador lógico `and`, pero en `pandas` no es permitido. Si quieres profundizar sobre esto puedes consultar el artículo de [Àlex Escolà Nixon en Towards Data Science](https://towardsdatascience.com/bitwise-operators-and-chaining-comparisons-in-pandas-d3a559487525).

[^footnote2]: En este curso no podemos profundizar en lógica y teoría de conjuntos, pero puedo recomendar el primer capítulo del libro de {cite}`juola_six_2017` para una introducción bastante comprensible de la lógica. Para la teoría de conjuntos, el capítulo de {cite}`flanders_gentle_2019` es una introducción sencilla y completa.
