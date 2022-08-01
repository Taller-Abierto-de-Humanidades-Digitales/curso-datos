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

# Importar datos a Google Colab

Con "importar datos" nos referimos a la manera en la que preparamos la fuente de datos para ser leída por nuestro programa.

Existen múltiples maneras de importar la información. Por ejemplo, podemos sencillamente utilizar el mismo método que usamos con nuestro archivo `ejemplo-1.txt`.

Descarga el archivo que quieras utilizar en el directorio de Drive en el que vayas a almacenar tus datos.

Como ejemplo, voy a utilizar los [casos nacionales de COVID-19 registrados diariamente durante el primer semestre de 2022](https://datos.cdmx.gob.mx/dataset/casos-asociados-a-covid-19/resource/e5f65f40-5904-492a-ae33-1ea98fb73d78?inner_span=True) compartidos por la Secretaría de Salud de Ciudad de México.

Descargo el archivo CSV en un directorio de mi computadora. Posteriormente lo subo a mi directorio de datos de Google Drive:

``` {image} ../_static/imgs/fuente-datos/subir_a_drive.gif
:width: 800px
:align: center
```

Volvemos a nuestro cuaderno de Google Colab. Me aseguro de haber activado Google Drive en mi Google Colab y busco el directorio en el cual está mi archivo. En mi caso: `'/content/drive/MyDrive/Colab Notebooks/curso_datos/casos_nacionales_covid-19_2022_semestre1.csv'`

```{image} ../_static/imgs/fuente-datos/ruta_archivo.png
:width: 800px
:align: center
```

Con esos pasos, podemos hacer la importación:

```python
datos = '/content/drive/MyDrive/Colab Notebooks/curso_datos/casos_nacionales_covid-19_2022_semestre1.csv'

with open(datos, 'r') as f:
  data = f.readlines(10) # agrego este argumento porque el archivo es muy extenso.

data
```

De esta manera hemos logrado incluir el archivo en nuestro cuaderno, pero será muy complejo manipularlo. Por esta razón, es preferible utilizar una librería que nos ayude a procesar estos datos. En nuestro caso, usaremos 'Pandas'

Para hacer que nuestro programa funcione, solamente debemos importar la librería:

`import pandas as pd`

Y posteriormente podremos abrir nuestro archivo desde Python:

```python
import pandas as pd

df = pd.read_csv(datos)
df.head()
```

Puedes ver el resultado de este ejercicio en el siguiente [enlace](https://colab.research.google.com/gist/jairomelo/dca189c897e87b74d5469906d7a9e1fb/mi-cuaderno-de-datos.ipynb)

``` {admonition} Problemas comunes
Este método funciona con archivos csv, no con archivos de texto o de Excel. Para replicar el ejercicio en este momento te recomendamos seleccionar una fuente de datos en ese formato. 

También es posible que surja un error al momento de ejecutar la importación. Intenta por esta semana con otra fuente de datos. La siguiente semana detallaremos algunas habilidades que te ayudarán a resolver ese problema.
```

Intenta replicar el ejercicio con un archivo que sea de tu interés y compártelo con los demás colegas en la siguiente actividad.
