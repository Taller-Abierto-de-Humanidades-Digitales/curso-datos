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

# Introducción a la manipulación de datos

Después de dos semanas relativamente tranquilas, entramos a la parte más retadora del proceso: la manipulación de datos. En realidad es un mal nombre que se le ha asignado al proceso de limpiar, normalizar y preparar los datos para que puedan ser analizados y visualizados correctamente. En inglés existe otro término para este proceso que es *data wrangling* [^footnote1], el cual es prácticamente intraducible, pero podríamos entenderlo de manera muy literal como "pelear con los datos". El análisis de datos es una disciplina relativamente nueva (es apenas una ciencia decimonónica {cite}`mayer-schonberger_big_2013`) y más lo es la ciencia de datos masivos. Por esa razón muchos términos que usaremos aquí (como limpieza o manipulación) tienen un carácter polisémico derivado de su novedad y la necesidad que ha tenido la comunidad científica y técnica de nombrarlos de alguna manera.

```{admonition} ¿Análisis de datos o estadística?
:class: tip
Saldemos desde ahora esa duda: la ciencia del análisis de datos es una disciplina que está fuertemente relacionada con la estadística, pero no es una rama de esta. En la ciencia de datos también intervienen el cálculo, el álgebra, la ciencia de la computación, e incluso áreas de las humanidades como la lingüística. Por ello se denomina a la ciencia de datos como un área interdisciplinar.
```

Oviamente no podremos abordar todas las técnicas necesarias para realizar una manipulación de datos, pero sí las necesarias para iniciar con la visualización de datos.

## Notas

[^footnote1]: Además del trabajo de {cite}`mckinney_python_2018`, un buen camino para empezar a profundizar en este tema es el libro de {cite}`mcgregor_practical_2022`.
