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

# Manipulación básica de un dataframe

En esta sección, veremos algunas técnicas incluidas en la librería `pandas` que nos permitiran localizar, filtrar, ordenar y agrupar datos. Para aquellos familiarizados con la sintaxis de SQL, `pandas` les puede parecer un poco extraño al principio (pues no existe una sintaxis como ``SELECT * FROM `table` WHERE `column` = `value` ``), pero, como explica {cite}`mckinney_python_2018` en su capítulo 10, con Python y `pandas` es posible hacer cualquier operación que realiza una consulta SQL y además lo puede hacer de una forma más "expresiva".

## Contenidos de la sección

```{tableofcontents}
```
