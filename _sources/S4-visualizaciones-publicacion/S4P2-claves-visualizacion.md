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

# Bases para la visualización de datos

Como bien subrayan Dougherty e Ilyankou {cite}`dougherty_hands-data_2021` la clave de nuestras visualizaciones consiste en comparar dos o más variables. Por ejemplo, cantidad de contagios y tiempo; o defunciones y sexo. Decidir qué variables comparamos es relevante porque nos da la pauta para elegir el tipo de visualización que mejor se adapta a nuestro objetivo.

Aunque ya tengamos nuestros datos limpios, tendremos que realizar algunas operaciones para poderlos comparar. Esto es, requeriremos sumar, promediar, contar, hacer porcentajes, entre otras operaciones.

Afortunadamente, al ser acciones tan comunes, la mayoría de programas que trabajan con datos incluyen procesos para hacer esos cálculos. Te mostraremos algunos ejemplos de operaciones que podemos realizar con los datos de la pandemia que hemos limpiado anteriormente.

Notarás que no son los únicos cálculos posibles y que tal vez podríamos realizar otros si no hubiésemos descartados algunas columnas previamente. Esto es algo común en el análisis de datos. Tendrás que segmentar, ampliar o reducir tus datos, en el camino, tendrás que tomar decisiones que te ayudarán a enfocar tu análisis y no será extraño que regreses al conjunto de datos original para realizar nuevas operaciones.

## Sumar

Esta es una operación aritmética sumamente común. Por ejemplo, podemos querer establecer la cantidad de defunciones por día. Para ello, vamos a necesitar modificar nuestros datos para incluir un valor de 1 en cada fila donde se haya registrado un deceso (fecha_def):

```{code-cell} ipython3
:tags: [remove-cell]
ruta_datos = '../data/covid_clean.csv'
```

```{code-cell} ipython3
import pandas as pd
datos_covid = pd.read_csv(ruta_datos)
datos_covid['decesos'] = datos_covid['fecha_def'].apply(lambda x: 1 if pd.notnull(x) else 0)
```

Ahora, podremos agrupar por fecha y sumar las muertes:

```{code-cell} ipython3
muertes_diarias = datos_covid.groupby('fecha_def')['decesos'].sum().reset_index(name='fallecidos_diarios')
muertes_diarias.head()
```

## Promedio

Por ejemplo, un dato interesante que podríamos querer reconocer es el promedio de edad de las personas contagiadas por Covid-19 en el primer semestre de 2022. Aunque técnicamente podemos hacer este cálculo por nuestra cuenta (sumar todas las edades y dividir por el número de personas), es más fácil que `pandas` lo haga por nosotros.

```{code-cell} ipython3
datos_covid['edad'].mean()
```

Aquí estamos realizando un cálculo de promedio bastante simple (la cantidad por el total de elementos). Ahora, supongamos que queremos saber el promedio de edad por sexo:

```{code-cell} ipython3
promedio_es = datos_covid.groupby('sexo')['edad'].mean()
promedio_es
```

Como vemos es prácticamente indistinta la edad de mujeres y hombres con relación a sus contagios, esto podría indicar que no existe una correlación entre edad, sexo y contagio.

```{code-cell} ipython3
c_corr = datos_covid.sexo.str.get_dummies().corrwith(datos_covid.edad)
c_corr
```

El resultado de la correlación entre edad y sexo es prácticamente cero, muy alejada de cualquier valor que indique una correlación fuerte.

## Porcentaje

También podríamos calcular el porcentaje de infectados por país de origen (excluyendo México, obviamente):

```{code-cell} ipython3
datos_covid['pais_nacionalidad'] = datos_covid['pais_nacionalidad'].str.lower()
porcentaje_pais = datos_covid[datos_covid.pais_nacionalidad != 'méxico'].groupby('pais_nacionalidad').size() / datos_covid[datos_covid.pais_nacionalidad != 'méxico'].shape[0] * 100
# nombrar las columnas
porcentaje_pais.name = 'porcentaje'
porcentaje_pais.index.name = 'pais'
# ordenar por porcentaje
porcentaje_pais = porcentaje_pais.reset_index()
porcentaje_pais.sort_values(by='porcentaje', ascending=False, inplace=True)
porcentaje_pais.reset_index(drop=True, inplace=True)
porcentaje_pais[:10]
```

Ahora, hagamos el cálculo del porcentaje de contagios por país de origen teniendo en cuenta el tipo de migrante.

```{code-cell} ipython3
from functools import reduce # vamos a aprovechar la función reduce para hacer un merge de los dataframes

tipos_migracion = ['SI', 'NO', 'NO ESPECIFICADO']

# Esta es una larga lista de acciones que están escritas de una manera sintética

# 1. Filtrar por tipo de migración
dfs = [datos_covid[(datos_covid.migrante == tipo) & (datos_covid.pais_nacionalidad != 'méxico')].groupby('pais_nacionalidad').size() / datos_covid[(datos_covid.migrante == tipo) & (datos_covid.pais_nacionalidad != 'méxico')].shape[0] * 100 for tipo in tipos_migracion]

# 2. Renombrar las columnas
dfsname = []

for df, tipo in zip(dfs, tipos_migracion):
    df.name = tipo
    df.index.name = 'pais_nacionalidad'
    df = df.reset_index()
    df.sort_values(by=tipo, ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    dfsname.append(df)

# 3. Unir los dataframes
porcentaje_pais = reduce(lambda left, right: pd.merge(left, right, on='pais_nacionalidad', how='outer'), dfsname)
porcentaje_pais.fillna(0, inplace=True)
porcentaje_pais.sort_values(by='SI', ascending=False, inplace=True)
porcentaje_pais.reset_index(drop=True, inplace=True)
porcentaje_pais[:10]
```

Ahora tenemos un escenario más preciso. Ya no sabemos solamente cuántos contagios tenemos por país de origen, sino tenemos un valor que representa cuál es el porcentaje de cada uno de estas nacionalidad en el conjunto general de extranjeros. Además, podemos contrastar entre aquellos que son migrantes y aquellos que simplemente están de visita, o que no lo especificaron.

En esta tabla tenemos el dato ordenado por migrantes y solamente incluye el top 10 de países de origen. Pero hay sutilezas que podríamos explorar con mayor detalle, por ejemplo, de cuáles países se contagiaron mayor cantidad de visitantes que de migrantes, cuál es el orden de nacionalidad no especificada, etc. Es aquí donde la visualización de datos puede ayudarnos a entender mejor estas relaciones.

## En síntesis

Como verás, estas operaciones pueden ser más o menos complejas, dependiendo de los datos que tenemos disponibles y de lo que queremos hacer con ellos. Aunque estas líneas de código pueden ser ilegibles por momentos, es importante tener en cuenta que `pandas` es una herramienta muy poderosa que nos permite hacer análisis de datos de una manera muy sencilla.

Te recomiendo que intentes replicar algunos de los ejemplos que hemos visto aquí y que te desafíes a hacer tus propios análisis de datos.

¡Adelante!
