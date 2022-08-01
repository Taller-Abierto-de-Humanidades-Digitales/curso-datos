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

# Seleccionar una fuente de datos

Las fuentes de datos corresponden a toda la información estructurada que podemos utilizar para nuestro análisis. Estos datos pueden haber sido obtenidos por nosotros directamente, o pueden haber sido generados por una institución o grupo de investigación. Debemos tener en cuenta que aunque los datos parezcan idénticos, cada fuente de datos es particular. Se dice comúnmente que los datos no mienten, pero la realidad es que incluso observando el mismo fenómeno social, podemos encontrarnos con datos diferentes.

En nuestro curso utilizaremos datos abiertos. De una manera muy sintética, los podemos definir como aquellos que son accesibles por cualquier ciudadanos, y que dan cuenta de acciones gubernamentales (sobre todo de programas de gobierno) tanto de diagnóstico como de intervención. El principio que se plantea con los datos abiertos es el de un gobierno transparente, que permita a cualquier ciudadano informarse detenidamente de las acciones del gobierno y de la situación del país.

La siguiente infografía es un resumen muy sencillo de lo que representan los datos abiertos:

``` {image} _static/imgs/fuente-datos/datos-abiertos-1.png
:width: 800px
:align: center
```

Como habrás visto, los datos abiertos son una fuente de datos particular y su construcción está asociada con una institución dedicada a la producción de dica información. Por lo tanto, es fundamental no tomar los datos abiertos como una fuente "natural" o "incontestable" de datos. Tampoco caer en la trampa de pensar en estos como datos "manipulados" o "tergiversados". Aquí lo relevante es la crítica a la fuente de datos, por ello, el primer paso para seleccionar una fuente de datos consiste en identificar los repositorios donde encontraremos fuentes de datos, para con ello tener una perspectiva clara de qué datos nos pueden ser útiles y cómo los podemos utilizar.

## Diferencia entre datos y estadísticas

Cuando exploremos las fuentes de datos es posible que encontremos en un mismo lugar información estadística y datos. En este curso trataremos directamente con datos, es decir, con información "en crudo". El procesamiento para llegar a la visualización consistirá precisamente en un análisis de datos que se representará gráficamente.

En síntesis podemos definir ambos términos así:

- Datos: piezas individuales de información factual registrada con un propósito específico. Por ejemplo, el registro de un estudiante en una escuela de educación básica.
- Estadísticas: son el resultado del análisis, interpretación y representación de los datos. Por ejemplo, la tendencia de deserción en una escuela de educación básica.

## Fuentes de datos o bases de datos

Para este curso no utilizaremos una base de datos, ni recurriremos a estos sistemas para recuperar la información. Una particularidad de los datos abiertos es que se prioriza su disponibilidad en formatos accesibles, interoperables y multiplataforma. Será más común hallar los datos en tablas (tipo Excel) o en archivos de texto (tipo CSV) que en bases de datos. Por ello, nos centraremos en métodos para recuperar los datos dese ese tipo de archivos, procesarlos y visualizarlos.
