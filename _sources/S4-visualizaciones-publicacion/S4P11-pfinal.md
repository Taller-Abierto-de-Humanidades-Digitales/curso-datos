# Proyecto final

En este momento, debes tener un cuaderno con muchísimos ejercicios y ejemplos de visualizaciones. Es posible que en este momento sea un poco caótico y difícil de seguir. Por esa razón, el proyecto final consiste en dar forma a este cuaderno para que pueda ser presentado y entendido por otras personas.

## Ordenar el cuaderno

El cuaderno de Google Colab debe tener un orden en los textos y las celdas de código, de tal manera que cualquier persona pueda replicar lo que has hecho. Para esto, es importante que:

- Los textos estén bien estructurados, con títulos y subtítulos que ayuden a entender el contenido.
- Los textos estén bien formateados, con negritas, cursivas, listas, etc.
- Los textos estén bien enlazados, con hipervínculos a otros textos y a otras visualizaciones.
- Los textos estén bien organizados, con imágenes, tablas, gráficas, etc.

También es relevante que las celdas de código estén bien organizadas y comentadas, de tal manera que cualquier persona pueda entender qué es lo que estás haciendo. Es relevante que exista una secuencialidad, que la celda que se encuentre en la posición superior del cuaderno sea la primera en ejecutarse y secuencialmente se vayan ejecutando las demás celdas. Para ello, prueba que el cuaderno se ejecuta secuencialmente desde el menú 'Entorno de ejecución' y seleccionando la opción 'Reiniciar y ejecutar todo'. Si todo funciona correctamente, entonces tu cuaderno está bien organizado :)

## Secciones recomendables del cuaderno final

El cuaderno final puede contener los siguientes aspectos:

- Presentas el origen de tu fuente de datos:
  - ¿De dónde proviene?
  - ¿Quién produjo esos datos?
  - La URL a los datos originales

- Realizas una descripción de tu fuente de datos:
  - A partir de los metadatos del proveedor (descripción cualitativa)
  - Aprovechando los métodos `dtypes` y `describe()`

- Realizas los procesos de manipulación necesarios para segmentar y limpiar la información (solamente cuando es necesario):
  - Se segmentan las columnas útiles para la visualización de datos
  - Se elimina o llena, si es pertinente, los datos nulos
  - Se eliminan, si es pertinente, los valores duplicados

- Transformas la información (solamente cuando es necesario):
  - Se unen, si es pertinente, conjuntos de datos para enriquecer la fuente de datos inicial
  - Se convierten los valores de objeto en numérico cuando es pertinente
  - Se convierten los valores de objeto en `datetime` cuando es necesaria
  - Se insertan valores de georeferenciación cuando es posible o pertinente
  
- Realizas una visualización con tus datos:
  - Realiza por lo menos una visualización (barra, línea, mapa o redes) con los datos analizados
  - Narra brevemente la visualización para que sea comprendida por los estudiantes o cualquier otra persona que la consulte.

## ¿Cómo presentar el cuaderno?

Simplemente comparte un enlace a tu cuaderno de Google Colab (un enlace público de solo lectura) en el espacio correspondiente al [taller final](https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso-datos/discussions/new?category=actividades&title=Actividad%20Proyecto%20final&body=El%20contenido%20de%20tu%20%20actividad).

Es importante asimismo que puedas comentar, retroalimentar y responder a las dudas de tus compañeros; para así darle vida al curso :)
