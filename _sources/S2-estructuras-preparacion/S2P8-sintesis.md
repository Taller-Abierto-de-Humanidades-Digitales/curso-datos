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

# ¿Qué aprendimos esta semana?

En esta semana nos familiarizamos mucho más con nuestro conjunto de datos. Pasamos de una descripción por metadatos a una descripción por tipos de datos y aplicamos la estadística descriptiva para hacer nuestras primeras interpretaciones.

## ¿Qué aprendiste de programación en Python esta semana?

### Tipos de datos

Conociste tres tipos de datos nuevos:

- `list`: listas (arrays)
- `dict`: diccionarios (objetos con claves y valores)
- `tuple`: tuplas (arrays de elementos que no se pueden modificar)

### Operaciones

Realizar operaciones en Python es bastante sencillo:

```{code-cell}
suma = 1 + 2
resta = 2 - 1
multiplicacion = 2 * 3
division = 3 / 2
modulo = 3 % 2
potencia = 2 ** 3

print(suma, resta, multiplicacion, division, modulo, potencia)
```

Asimismo, Python incluye algunas funciones que nos permiten realizar operaciones con valores que se encuentran en una lista como la suma:

```{code-cell}
lista = [1, 2, 3, 4, 5]
suma = sum(lista)
suma
```

También es de suma utilidad la función `len` que nos permite obtener el número de elementos de una lista:

```{code-cell}
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
longitud
```

Esta función regresa un valor entero, por lo que podemos combinar estas dos operaciones para obtener el promedio de una lista:

```{code-cell}
lista = [1, 2, 3, 4, 5]
promedio = sum(lista) / len(lista)
promedio
```
