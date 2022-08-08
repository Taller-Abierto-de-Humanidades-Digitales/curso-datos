---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Variables cuantitativas y cualitativas

Ya vimos en la sección anterior que identificar el tipo de datos es fundamental para comprender las mediciones u operaciones que podremos realizar con los datos.

Vamos a intentar detallar un poco más lo anterior. En general, tendemos a asociar los datos cuantitativos con los valores numéricos, en tanto los cualitativos serían valores de texto. Por ejemplo:

```{code-cell}
:tags: ["remove-cell"]
!pip install pandas
!pip install numpy
```

```{code-cell}
valores_cualitativos = ['Pedro', 'Luisa', 'Argemiro']
valores_cuantitativos = [1, 2, 3]
```

Sin embargo, no todo dato numérico es un valor cuantitativo. Por ejemplo:

```{code-cell}
valores_numericos_cualitativos = {'num pasaporte': '12345', 'numero de tarjeta de identidad': '123456789'}
```

Sumar, restar o promediar números de identificación no tiene mucho sentido, por ello debemos considerar que en nuestros conjuntos de datos no solamente es el tipo de dato de Python el que tenemos que considerar, además debemos valorar si estos datos son cuantitativos o cualitativos.

## Escalas de medición por variable

Las escalas de medición nos indican las operaciones posibles que podemos realizar con los datos, según sean estos cualitativos o cuantitativos.

### Escalas de medición para variables cualitativas

Las escalas de medición para variables cualitativas son las siguientes:

- **Nominal:** En este caso, podemos ordenar los valores de manera alfabética, a través de categorías o identificadores, pero solamente indicamos que son valores distintos.

```{code-cell}
import pandas as pd

df_nominal = pd.DataFrame({'nombre': valores_cualitativos, 'sexo': ['H', 'M', 'H']})
df_nominal.sort_values(by='sexo', inplace=True)

df_nominal
```

- **Ordinal:** Este tipo de valores también pueden ser ordenados alfabéticamente, pero la diferencia es que hay una distinción de nivel entre los valores. El ejemplo más claro de este tipo es la escala de Likert:

```{code-cell}
df_ordinal = pd.DataFrame({'nombre': valores_cualitativos, 'satisfaccion': ['5', '4', '1']})
df_ordinal.sort_values(by='satisfaccion', inplace=True)

df_ordinal
```

En ambos casos podemos ordenar los datos y además realizar cálculos de frecuencias, por ejemplo:

```{code-cell}
import numpy as np
lista_escala = np.random.randint(1, 6, size=100) # 100 valores aleatorios entre 1 y 5
print(pd.value_counts(lista_escala).sort_index())
```

También podemos calcular modas y medianas con tipos numéricos:

```{code-cell}
print(pd.value_counts(lista_escala).sort_index().mode())
print(pd.value_counts(lista_escala).sort_index().median())
```

### Escalas de medición para variables cuantitativas

Las escalas de medición para variables cuantitativas son las siguientes:

- **Intervalo:** Las escalas de intervalo nos ayudan a medir el "espacio" entre dos valores. En este ámbito podemos calcular los intervalos de fechas, o de temperatura. En estos cálculos no es relevante sumar la temperatura de ayer con la de hoy, ese es un dato falso; en cambio, podemos calcular si ayer fue un día menos cálido que hoy.

```{code-cell}
df_intervalo = pd.DataFrame({'dia': ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'], 'temperatura': [25, 20, 22, 24, 25, 25, 25]})
print(round(df_intervalo['temperatura'].mean(), 2))
print(df_intervalo['temperatura'].min())
print(df_intervalo['temperatura'].max())
```

En nuestro ejemplo, la temperatura máxima es 25, la mínima es 20 y la media es 23.71.

El sentido del valor del intervalo está asociado con la inexistencia de una ausencia de valores. Podemos decir que entre ayer y hoy pasaron 24 horas, pero no podemos afirmar que ayer fuera el día cero, o que antes de ayer no hubiese tiempo. Con la temperatura es similar, puede que la temperatura de enero sea la mitad de la de junio, pero no quiere decir que en enero no hubiese temperatura.

Otro aspecto relevante en este tipo de escala es que hay valores negativos (por la misma razón que no hay un cero absoluto).

- **Razón o proporción:** En este tipo de escala, los valores sí representan un cero absoluto, es decir, la ausencia de valor. Ejemplos típicos de estos valores son: la altura, el dinero, la población, la edad, entre otras. Identificar una escala de proporción está relacionado con saber si es lógico que un valor tenga un cero (incluso si hay un vlor negativo). Por ejemplo, decir que una persona tiene 0 pesos es totalmente posible, es decir, hay una ausencia de dinero. No es lo mismo que decir que hay 0 grados centígrados, ya que en ese caso no hay una ausencia de temperatura, tanto es así que hay 32° Fahrenheit, o 273.15 Kelvin. Tener 0 pesos en cambio no significa que tengamos un valor diferente en dólares o euros, por ejemplo.

En términos de medidas de proporción, podemos aplicar las mismas operaciones que en los intervalos, además de dividir y multiplicar un valor. Matemáticamente también podemos multiplicar y dividir una escala de intervalo (25 grados Celcius por 2 = 50 grados Celcius, por ejemplo), pero esta relación no es lógica. 50 grados centígrados es el doble de 25 grados, pero no es el doble de calor que hay en 25 grados. Tiene sentido numéricamente, pero no en términos de la termodinámica.

## En síntesis

Las escalas de medición son muy relevantes al momento de hacer nuestro análisis, en parte porque determinan el tipo de operaciones estadísticas que podemos realizar con los datos, y sobre todo porque nos permiten identificcar si esas operaciones son lógicas o no. Esto es algo que una librería como `pandas` no puede realizar de manera automática, puesto que solamente puede saber si un dato pertenece a un tipo específico. En ese mismo sentido, tendremos en cuenta que hay operaciones que no representan la realidad aunque estadísticamente sean correctas.

## Para saber más

Las escalas de medición están muy relacionadas con los tipos de datos, pero son solamente la punta del iceberg en lo que se puede hacer con los datos. Para los propósitos de nuestro curso, es suficiente con acercarse a algún manual o libro de texto para estadística básica {cite}`bruce_practical_2020,humberto_estadistica_2015,hernandez_conceptos_2006`. También recomendaría el libro *The art of statistics* de David Spiegelhalter, en particular los tres primeros capítulos {cite}`spiegelhalter_art_2021`.
