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

# Fuentes de datos

¿Dónde podemos encontrar fuentes de datos? Realiza el ejercicio simple de hacer una búsqueda del término "datos abiertos" en Google u otro buscador. Cada resultado tendrá sus particularidades, pero en general verás que los primeros resultados serán "[Datos abiertos de México](https://datos.gob.mx/)" y "[Datos abiertos de Ciudad de México](https://datos.cdmx.gob.mx/)". Posteriormente encontraremos resultados de otros países o de instituciones específicas como el [Conacyt](https://www.siicyt.gob.mx/index.php/estadisticas/bases-de-datos-abiertas) o el [INEGI](https://www.inegi.org.mx/datosabiertos/).

En cada uno de estos repositorios encontraremos buscadores y colecciones que nos ayudarán a identificar los datos que han sido publicados.

## Tipos de archivos

Aunque la información puede encontrarse en diferentes formatos, no todos nos serán útiles para nuestro análisis. Algunas entidades comparten su información en formatos que son fáciles de leer y descargar, por ejemplo en PDF o en Word, pero esto representa una gran dificultad para procesar la información. Por otra parte, hay formatos que son un poco más manejables, pero todavía requerimos de pasos adicionales para acceder a la información, por ejemplo, Excel o sitios Web (HTML). Para este curso, priorizaremos los formatos recomendados para compartir datos abiertos: csv, json y xml.

``` {image} https://raw.githubusercontent.com/programminghistorian/opendataday-2021/8db99c7e7a86723954b5bb9baf080accc8f64c75/python-pandas-dash/imgs/tipos_de_archivo.jpg
:width: 800px
:align: center
```

```{admonition} Fuentes en Excel
Muchos de los datos se comparten en formato xlsx, propietario de Microsof Excel. Si bien no es recomendable, podemos acceder a los datos en formato xlsx ya sea mediante la simplificación de las tablas (por ejemplo, uniendo hojas) o eliminando encabezados y otros tipos de formatos. Veremos esto con más detalle en la siguiente semana. De esta manera, si hay un conjunto de datos representativo que pueda ser utilizado para tu proyecto y solamente se encuentre en formato xlsx, podrás utilizarlo.
```
