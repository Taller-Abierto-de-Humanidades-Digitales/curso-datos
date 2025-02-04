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

# Crear un cuaderno para practicar con código

Para hacer las cosas más simples poner rápidamente manos a la obra, vamos a crear un cuaderno en Google Colab para importar, procesar y visualizar nuestros datos.

```{note}
No necesitaremos instalar ningún programa. El único pre-requisito es tener una cuenta de Google.
```

## Google Colab

Google Colab es una herramienta gratuita de Google que permite escribir y ejecutar código directamente en tu navegador.[^jupyter] Este programa nos será de mucha utilidad para trabajar con nuestros datos.

La creación de nuestro primer cuaderno en Google Colab es muy sencilla.

Primero, vamos al siguiente enlace: [https://colab.research.google.com/](https://colab.research.google.com/). Si no has ingresado a la cuenta de Google podrás usar la aplicación, pero no podrás guardar los cambios. Por ello es importante que ingreses a la cuenta de Google desde el botón Acceder. Si ya habías ingresado a tu cuenta de Google es posible que simplemente te aparezca una pantalla como la siguiente:

```{image} ../_static/imgs/crear-carpeta/colab_ini.png
:width: 800px
:align: center
```

El siguiente paso consiste en crear un nuevo cuaderno de Google Colab. Para ello, solamente debemos hacer clic en el botón Nuevo cuaderno.

Se abrirá una ventana con el nuevo cuaderno:

```{image} ../_static/imgs/crear-carpeta/nuevo_cuaderno.png
:width: 800px
:align: center
```

Para finalizar, solamente nos resta cambiar el título del cuaderno a nuestra elección.

```{image} ../_static/imgs/crear-carpeta/cambiar_nombre.gif
:width: 800px
:align: center
```

## Antes de empezar, familiaricémonos con el cuaderno de Google Colab

Para poder seguir este curso cómodamente, tenemos que familiarizarnos con algunos elementos del Google Colab:

### Celdas

Las celdas son las partes de nuestro cuaderno que nos permiten escribir código o texto. El texto lo utilizamos para escribir comentarios, explicar los pasos que estamos ejecutando, etc. Es muy similar a lo que presentamos en esta página (que de hecho, está hecha en [JupyterBook](https://jupyterbook.org/en/stable/intro.html)). Las celdad de código permiten escribir y ejecutar código. En nuestro caso, usaremos el lenguaje de programación Python [^Python].

Veámos rápidamente su funcionamiento a través del siguiente video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/knmpMpFrw94" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Menú principal

Ahora exploremos el menú principal de Google Colab. Vamos a centrarnos en las funciones principales del menú, las que nos interesan para nuestras actividades, pero siéntete en libertad de explorar todos los elementos del menú para ver cómo funcionan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6nTrSLLskAE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Archivos

Una parte importantísima de Google Colab se refiere a la gestión de archivos. En el siguiente video te mostramos su funcionamiento básico. Centrémonos por lo pronto en estos aspectos:

- La manera en que podemos subir archivos a Google Colab.
- Añadir una unidad de Drive para conservar nuestros archivos y no se pierdan cuando se reinicie el entorno de ejecución.

<iframe width="560" height="315" src="https://www.youtube.com/embed/B_XvWBC35XA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Compartir tu cuaderno de Google Colab

Finalmente, vamos a compartir nuestro cuaderno de Google Colab. Estos cuadernos funcionan de la misma manera que un documento compartido de Google Drive, por lo que solamente debemos hacer clic en el botón Compartir. En el siguiente video te mostramos como compartir nuestro cuaderno.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mK6NjqGhFEE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Comparte tu cuaderno

Como un ejercicio práctico, comparte en el foro <a href="https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso-datos/discussions/new?category=actividades&title=Actividad%20Google%20Colab&body=El%20contenido%20de%20tu%20%20actividad." target="_blank"> Google Colab</a> de la primera semana el cuaderno que has creado. Solamente copia el enlace público (*solo lectura*) en el foro para que los demás participantes lo puedan consultar.

Solamente unos requisitos básicos:

- incluye al menos una celda de texto
- incluye al menos una celda de código
- incluye una ruta a un documento de texto en Google Drive
- en una celda, escribe el código que muestre que es posible leer el archivo de texto

Obviamente tu creatividad es el límite, así que si quieres incluir alguna otra maravilla que hayas realizado (subir una imagen en una celda de texto, etc.), no dudes en hacerlo.

## Notas

[^jupyter]: El sistema que utiliza Google Colab se denomina [Jupyter Notebook](https://es.wikipedia.org/wiki/Proyecto_Jupyter#Jupyter_Notebook). Si deseas profundizar un poco más en su uso puedes consultar el siguiente [video](https://youtu.be/6Vr9ZUntCyE) de Leonardo Kuffo.

[^Python]: Es un lenguaje de programación de alto nivel, que se utiliza para escribir código de programación. [Ver entrada en Wikipedia](https://es.wikipedia.org/wiki/Python)
