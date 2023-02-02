# A ver datos 

Después de tantas horas de trabajo ha llegado el momento de crear nuestras visualizaciones 📊 📉

Gracias a las modificaciones que realizaste a la fuente de datos que seleccionaste, es ahora posible crear visualizaciones que nos permitan entender mejor los datos. En este curso te mostraremos cómo hacer algunas visualizaciones básicas con Python y las librerías `matplotlib`, `plotly`, `seaborn` y `networkx` [^footnote].

## Algunas claves para la visualización de datos

Es imposible cubrir en este corto curso todos los aspectos involucrados en la visualización de datos. De hecho, sería un tanto arrogante pretender hacerlo en unas cuantas líneas.

Las posibilidades de visualización son innumerables y con un mismo conjunto de datos es posible hacer múltiples visualizaciones. De hecho, esta decisión puede llevar a interpretaciones erróneas o malintencionadas.

La realidad es que las personas no leemos datos, sino gráficos. La asociación entre "presentar resultados" y gráficos es un asunto esencial en la política de la actualidad {cite}`engebretsen_political_2020`. De hecho, cuando genero una imagen con [DALL·E](https://openai.com/dall-e-2) (la inteligencia artifical que genera creaciones a partir de textos) con la clave "político mostrando resultados al público", el resultado es el siguiente:

```{figure} ../_static/imgs/visualizacion/dall-e.png
---
height: 400px
align: center
name: politico-mostrando-resultados-al-publico
---

Imagen generada por DALL-E con la clave “politician showing results to public”. Disponible en [https://labs.openai.com/](https://labs.openai.com/s/W5xUlz19fiqS4yzicu3D82D6) Created with [DALL·E](https://openai.com/dall-e-2), an AI system by OpenAI
```

De los millones de imágenes que toma DALL·E como referencia, un patrón frecuente con el que puede asociar "resultados", "público" y "político" está relacionado justamente con tener un gráfico en el fondo sustentando sus argumentos.

Esto nos da una idea de lo relevante que es utilizar datos hoy para la ciencia y la educación. E igualmente nos da una idea de lo importante que es hacerlo de manera adecuada.

Antes de comenzar con nuestro tema, quisiera recomendar algunos libros recientes que considero pueden ser de mucha utilidad en caso de que deseen profundizar en la visualización de datos:

- Un libro bastante accesible para aquellos que no provenimos del universo de la estadística es el escrito por Jonathan A. Schwabish, *Better data visualizations* {cite}`schwabish_better_2021`. Es una excelente e inteligible introducción a los principios de la visualización de datos, los tipos de gráficos y algunas guías para el diseño de las visualizaciones.
- Una publicación reciente, realizada por dos educadores que se han dedicado durante muchos años a la enseñanza con datos, es el libro *Hands-On Data Visualization* de Jack Dougherty e Ilya Ilyankou {cite}`dougherty_hands-data_2021`. Es un libro muy práctico, que parte de herramientas disponibles como Excel, Open Refine, Tableau, entre otras, para ir desde la recolección de los datos hasta su visualización. Sin duda un excelente complemento para este curso introductorio. Y lo mejor, es que existe una versión abierta disponible en [https://handsondataviz.org/](https://handsondataviz.org/).
- Ahora un *best-seller*: *Storytelling with data* de Cole Nussbaumer Knaflic {cite}`nussbaumer_knaflic_storytelling_2015` (hay versión en español {cite}`nussbaumer_knaflic_storytelling_2017`). Nussbauer fue analista de datos en el área comercial de Google, y de esta experiencia surgió este libro, el cual se ha convertido en uno de los más vendidos de los últimos años para la narración de datos. También tiene un interesante canal en [Youtube](https://www.youtube.com/c/storytellingwithdata) donde puedes seguir sus consejos para la visualización de datos.
- Finalmente, un libro algo más técnico: *Data visualization: exploring and explaining with data* {cite}`camm_data_2022`. Este es un libro de texto cuyo público principal son los estudiantes de estadística y ciencias de datos. En caso de querer entrar de lleno en esta área, es una muy buena opción.

Y sin más preámbulo, vamos a comenzar con nuestro tema.

## Notas

[^footnote]: `Networkx` no es una librería enfocada en la visualización de datos, pero es una herramienta muy útil para preparar información que luego pueda ser visualizada en programas como [Gephi](https://gephi.org/).
