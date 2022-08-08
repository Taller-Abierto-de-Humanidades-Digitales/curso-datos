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

# Describir la fuente de datos con la función `describe()`

[Previamente vimos cómo identificar los tipos de datos de pandas con el método `dtypes`](../S2-estructuras-preparacion/S2P4-dtypes.md). Ahora veremos un método muy sencillo para 'describir' de manera muy preliminar lo que podemos hacer con nuestra fuente de datos.

## La función describe()

De acuerdo con la [documentación de pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html?highlight=describe#pandas.DataFrame.describe), la función `describe()` realiza una descripción estadística de nuestros datos. Incluye aquellos "que resumen las medidas de tendenca central, dispersión y forma de una fuente de datos, descartando los valores nulos (`NaN`)".

Esta es una función muy sencilla de utilizar y a la vez muy poderosa, puesto que puede realizar sus análisis tanto en valores numéricos como de objeto, incluso de datos mixtos.

Veámos qué sucede cuando utilizamos nuestra fuente de datos de ejemplo.

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

ejemplo1.describe()
```

Vemos cómo `pandas` selecciona las dos columnas numéricas ('Edad' y 'Promedio') para hacer la descripción del dataframe. Las operaciones resultantes son el conteo de los valores, la media, la desviación estándar, el valor mínim y el valor máximo, sí como el percentil bajo (25) y el percentil alto (75). El percentil 50 es igual que la mediana.

Si queremos obtener una descripción más amplia, que incluya todas las columnas sin importar su tipo de datos, simplemente añadimos el argumento `include='all'`:

```{code-cell}
ejemplo1.describe(include='all')
```

Vemos que en este caso incluye otros valores como `top`, que corresponde al valor más común; `unique` que representa la cantidad de valores únicos, y `freq` que representa la fecuencia del valor más común. Para los valores de timestamp también serán mostrados el primer y último valor.

Ahora realicemos el ejercicio con nuestra fuente de datos de ejemplo.

```{code-cell}
:tags: ["remove-cell"]
covid_nacional = pd.read_csv('../datos/casos_nacionales_covid-19_2022_semestre1.csv')
```

```{code-cell}
import pandas as pd
covid_nacional.describe()
```

Al igual que en nuestro dataframe de ejemplo, `pandas` solamente selecciona los valores numéricos: `Unnamed: 0` (que corresponde al índice de los datos) y `edad`. Veámos ahora qué información nos muestra cuando incluímos el parámetro `include='all'`.

```{code-cell}
covid_nacional.describe(include='all')
```

Como vemos es una tabla con todas las columnas de nuestro dataframe. Reliza una revisión rápida del resultado para que puedas observar algunos detalles del conjunto de datos que podrían ser útiles. Por ejemplo, es claro que en la columna `sexo` es mayor la frecuencia de casos en mujeres (733,991 casos sobre 1'323,501). También, si vemos la columna `entidad_nac` vemos que de las 33 entidades nacionales incluidas, la mayor frecuencia (por mucho) está representada por casos de la Ciudad de México (1'052,272 del total de los casos).

Para mejorar la legibilidad, podemos segmentar la descripción por unas cuantas columnas, por ejemplo:

```{code-cell}
covid_nacional[['origen', 'sector', 'sexo', 'entidad_nac', 
       'tipo_paciente', 'fecha_ingreso', 'fecha_sintomas', 'fecha_def']].describe(include='all')
```

En este caso, podemos incluso narrar un poco nuestros datos, ya que encontramos que la mayoría de pacientes fueron ambulatorios, mujeres, de la Ciudad de México, que la mayor parte de reportes provienen de unidades por fuera de las USMER (Unidades de Salud Monitoras de Enfermedad Respiratoria Viral). También podemos afirmar que la mayoría de los reportes de síntomas se dieron el 10 de enero, la mayoría de ingresos el 12 de enero y la mayor cantidad de defunciones el 29 de enero.

Como habrás notado, todavía estamos en una fase muy descriptiva. Esto nos permite tener una perspectiva de lo que podemos obtener de nuestro conjunto de datos, lo que nos facilitará la tarea de planear qué transformaciones requeriremos en nuestros datos para poderlos visualizar correctamente.

## Actividad

Usando el método `describe()` analiza los datos que seleccionaste y responde en el [foro](https://formaciondocente.bunam.unam.mx:8091/moodle/fdocente/mod/forum/view.php?id=645) lo siguiente:

- ¿Qué columnas brindan información significativa para analizar?
- ¿Qué te gustaría descubrir de tu fuente de datos?
- ¿Es suficiente con tu fuente de datos? ¿Necesitas una fuente de datos adicional?

Responder estas preguntas te ayudará a entender tu fuente de datos y qué puedes lograr con ella.
