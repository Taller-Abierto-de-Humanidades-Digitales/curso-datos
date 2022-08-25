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

# Tipos de datos con pandas

Ya hemos visto los tipos básicos del lenguaje Python [^footnote1]. Ahora bien, la librería `pandas` también cuenta con una serie de tipos de datos que debemos tener en cuenta para poder realizar nuestras operaciones de análisis. Para complejizar un poco más lo anterior, los tipos de datos de `pandas` se sobreponen con los de otras librerías como `numpy` y `scipy`.

## Mapa de tipos de datos de `pandas`

Para entender un poco mejor los tipos de datos en `pandas`, veamos la siguiente tabla:

| tipo de dato pandas | tipo Python    | uso                                                           |
|---------------------|----------------|---------------------------------------------------------------|
| object              | str o mezclado | Valores de texto o mezcla de valores numéricos y no numéricos |
| int64               | int            | número enteros                                                |
| float64             | float          | números decimales                                             |
| bool                | bool           | valores de verdad y falsedad                                  |
| datetime64          | NA             | valores de fecha y tiempo                                     |
| timedelta[ns]       | NA             | valores de diferencia entre dos valores de datetime           |

Los tipos de datos int64 y float64 son préstamos de `numpy`. Aunque hay diferecias con los datos `int` y `float` de Python, realmente no afectan el análisis básico de datos que llevaremos a cabo en este curso [^footnote2]. En ese sentido, tenemos tres tipos de datos particulares de `pandas` que detallaremos a continuación.

### Tipo de dato `object`

El tipo de dato `object` es un tipo de dato que puede contener valores de texto o valores numéricos. Esto hace que sea uno de los tipos más confusos de `pandas` porque puede ser que comprenda una columna de texto, o una con datos numéricos que no se han declarado como int64 o float64, incluso diccionarios o listas.  Podríamos decir que en `pandas` todos los tipos de datos son `object` hasta que se declaren como uno de los tipos de datos específicos.

Volvamos a nuestro `ejemplo1` y ahora usemos el módulo `dtypes` para obtener el tipo de dato de cada columna:

```{code-cell}
import pandas as pd

ejemplo1 = pd.DataFrame(
    {"Nombre": ["Andrea", "Berenice", "Carlos"], # tipo de datos string
    "Edad": [34, 51, 26], # tipo de datos int
    "Registro": [True, False, True], # tipo de datos bool
    "Promedio": [9.5, 8.5, 10], # tipo de datos float
    "Origen": [
        {"Ciudad": "Ciudad de México", "Estado": "CDMX"}, 
        {"Ciudad": "Guadalajara", "Estado": "Jalisco"}, 
        {"Ciudad": "Toluca", "Estado": "Estado de México"}
        ], # tipo de datos dict 
    "Calificaciones": [(9, 8, 10), (8, 7, 9), (7, 6, 8)] # tipo de datos tuple
    })

ejemplo1.dtypes
```

Vemos que los datos están claramente detallados en el tipo de dato de cada columna. Ahora probemos el mismo método con la fuente de datos que usamos en la sección anterior:

```{code-cell} ipython
:tags: ["remove-cell"]
try:
  covid_nacional = pd.read_csv('../data/casos_nacionales_covid-19_2022_semestre1.csv')
except FileNotFoundError:
  covid_nacional = pd.read_csv('../datos/casos_nacionales_covid-19_2022_semestre1.csv')
```

```{code-cell} ipython
# modifiqué el nombre del dataframe a covid_nacional para mejor legibilidad
covid_nacional.dtypes
```

Verás que prácticamente todas las columnas son de tipo object. Esto se debe a que en conjuntos de datos grandes, `pandas` ahorra memoria y tiempo al no declarar los tipos de datos de cada columna. Por esa razón, es muy probable que nos encontremos con fuentes de datos de tipo object aunque su tipo en realidad sea entero, decimal o booleano.

### Tipo de dato datetime64

El tipo de dato `datetime64` es un tipo de dato que representa una fecha y una hora. El tipo de dato `datetime64` es un préstamo de `numpy` y es un tipo de dato que se puede usar para representar una fecha y una hora.

En nuestro ejemplo de datos por Covid 19, las fechas están representadas con el formato AAAA-MM-DD (por ejemplo: 2022-05-03). Para representar una fecha y una hora, podemos usar el formato `datetime64[ns]`. `pandas` incluye una función para convertir una cadena de texto a un tipo de dato `datetime64[ns]` llamada `to_datetime`. Usémosla en la columna 'fecha_ingreso' para ver el resultado

```{code-cell}
covid_nacional['fecha_ingreso'] = pd.to_datetime(covid_nacional['fecha_ingreso'])
covid_nacional['fecha_ingreso'].head()
```

En este caso el tipo de fecha es bastante simple (año, mes, día). Pero también es posible utilizar el tipo `datetime64` para estabecer la hora y los minutos de la fecha, incluso la unidad de tiempo coordinado (UTC) del dato.

```{code-cell}
covid_nacional['fecha_ingreso'] = pd.to_datetime(covid_nacional['fecha_ingreso'], utc=True)
covid_nacional['fecha_ingreso'].head()
```

En este ejemplo la librería agrega el valor de hora 00:00:00+00:00 al no tener otra referencia para representar la hora. Si hubiese una hora de origen, por ejemplo, la hora de ingreso de un paciente, podría ser relevante hacer esa operación.

### Tipo de dato timedelta[ns]

El tipo de dato `timedelta[ns]` es un tipo de dato que representa una diferencia de tiempo entre dos valores. Por ejemplo, la diferencia de tiempo en horas, días, minutos o segundos entre dos fechas. Por ejemplo, si queremos saber cuál es la diferencia de tiempo entre los síntomas y el ingreso del paciente a la institución de salud, podemos restar dos valores de `datetime` y obtendremos un valor de `timedelta`.

```{code-cell}
covid_nacional['fecha_sintomas'] = pd.to_datetime(covid_nacional['fecha_sintomas'], utc=True)
covid_nacional['diferencia_tiempo'] = covid_nacional['fecha_ingreso'] - covid_nacional['fecha_sintomas']
covid_nacional['diferencia_tiempo'].head()
```

Incluso podemos hacer alguna operación estadística simple, como hallar el promedio de estos valores de `timedelta`.

```{code-cell}
covid_nacional['diferencia_tiempo'].mean()
```

De manera muy rápida podemos afirmar que la diferencia de tiempo entre los síntomas y el ingreso del paciente es, en promedio, de un día y 19 horas.

## Actividad

En el [foro](https://github.com/MOOC-UNAM-Publico/curso-datos/issues/new?title=Actividad%20descripción%20con%20dtypes&body=El%20contenido%20de%20tu%20%20actividad), describe la forma de la fuente de datos:

* Número de filas
* Número de columnas
* Nombre de las columnas

Y, usando el módulo `dtypes` analiza los tipos de datos que tienes en tu DataFrame (int, float, object).

Comparte con los demás colegas la descripción de la fuente de datos y solamente con estos datos comenta qué posibilidades y retos encuentras con la fuente de información de por lo menos otros dos colegas.

## Notas

[^footnote1]: Los tipos básicos (primitivos o integrados) dependen de cada lenguaje. En ciertos lenguajes como Java existen tipos de datos como byte, short, long y double, que hacen más preciso el manejo de los datos. Una gran ventaja de Python es que sintetiza estos tipos de datos, que son un tanto más abstractos, en favor de la legibilidad. Para un listado completo de estos tipos de datos en Python puedes consultar la [documentación de Python](https://docs.python.org/es/3/library/stdtypes.html#types-and-values).

[^footnote2]: `pandas` usa este tipo de datos porque son computacionalmente más precisos que los de Python, lo cual hace más rápido procesar grandes cantidades de datos.

[^footnote3]: Este tipo de dato es similar a los 'factors' de R. Los factores son una forma de representar una variable categórica, en la que cada valor de la variable es una categoría.Sobre este tipo de datos puedes consultar la siguiente [página](https://swcarpentry.github.io/r-novice-inflammation/12-supp-factors/index.html).
