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

# Tipos de datos

Lo primero que tenemos que tener en cuenta es que los datos se clasifican en diversos tipos, los cuales determinan lo que podemos hacer con ellos, o mejor, sus escalas de medición.

## Tipos de datos básicos en Python

Los tipos de datos básicos en Python son:

- `int`: números enteros
- `float`: números decimales
- `bool`: valores lógicos (verdadero o falso)
- `str`: cadenas de texto (cadenas de caracteres)
- `list`: listas (arrays)
- `dict`: diccionarios (objetos con claves y valores)
- `tuple`: tuplas (arrays de elementos que no se pueden modificar)

Un mismo conjunto de datos puede tener varios tipos de datos, por ejemplo:

```{code-cell} ipython
:tags: ["remove-cell"]
!pip install pandas
```

```{code-cell} ipython
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

ejemplo1
```

Como verás, el conjunto de datos permite cualquier tipo incorporado en sus columnas. La coherencia de los datos depende de las restricciones que hayan sido impuestas para la creación de los datos. Por ejemplo, si los datos fueron incorporados a través de un modelo de base de datos los tipos de datos seguramente estarán claramente definidos por la arquitectura de la base; pero si los datos fueron volcados manualmente en una hoja de cálculo,pueden ser ambiguos.

## ¿Por qué es relevante el tipo de datos?

Para aclarar más lo anterior. Supongamos que nos encontramos con el siguiente conjunto de datos:

```{code-cell} ipython
ejemplo2 = pd.DataFrame(
    {"Nombre": ["Andrea", "Berenice", "Carlos"], 
    "Edad": ["34", "51", "26"]})

ejemplo2
```

A simple vista, los datos parecen adecuados y no hay ningún error evidente. El problema es que no podríamos procesarlos de manera adecuada. Si quisiera hacer un promedio de la edad de los alumnos tendría el siguiente error:

```{code-cell} ipython
promedio = sum(ejemplo2.Edad)/len(ejemplo2.Edad)
```

Este es un error de tipo (`TypeError`) que indica que estamos intentando ejecutar una operación incorrecta (sumar y dividir) con un tipo de dato incompatible.

Cuando trabajamos con `pandas` esto puede conllevar otros problemas como el siguiente:

```{code-cell} ipython
ejemplo2["Edad"].mean()
```

Sabemos que el promedio de 34, 51 y 26 no puede ser 115,042; no obstante, `pandas` realiza una operación con nuestros datos y nos devuelve el promedio incorrecto. En este ejemplo sabemos exactamente el valor que debe devolver el promedio, por lo que inmediatamente entendemos que debemos corregir nuestra operación para obtener el resultado correcto, pero en grandes conjuntos de datos podría llevar a un error.

Por esta razón, debemos asegurarnos de que los datos que se procesan son compatibles para realizar las mediciones que se requieran. En la tercera parte del curso veremos como hacer esto, que es básicamente lo que les muestro a continuación:

```{code-cell} ipython
ejemplo2["Edad"] = ejemplo2["Edad"].astype(int)
ejemplo2["Edad"].mean()
```

En este caso, el promedio ya se puede calcular de manera correcta porque el tipo de dato es adecuado: `int`.
