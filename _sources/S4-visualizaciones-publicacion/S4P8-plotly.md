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

# Gráficos con plotly

Ahora veremos cómo realizar las mismas operaciones de la sección previa, pero utilizando la librería `plotly`.

## `Plotly`

 Esta es una librería enfocada en la visualización para la web, en particular para realizar páneles interactivos. Para incluirla en tu Google Colab solamente deberás instalarla con el comando `!pip install plotly`. Plotly tiene varias opciones, pero usaremos su módulo `plotly.express` que es más sencilla de utilizar [^footnote].

```{code-cell} ipython3
:tags: [hide-output]
!pip install plotly
import plotly.express as px
```

Muy bien, ahora iniciemos la visualización de los datos de la sección previa. Primero, carguemos los datos de la sección previa.

```{code-cell} ipython3
:tags: [remove-cell]
import pandas as pd
ruta_datos = '../data/covid_clean.csv'
datos_covid = pd.read_csv(ruta_datos)
datos_covid['decesos'] = datos_covid['fecha_def'].apply(lambda x: 1 if pd.notnull(x) else 0)
muertes_diarias = datos_covid.groupby('fecha_def')['decesos'].sum().reset_index(name='fallecidos_diarios')
```

Ahora, grafiquemos los datos de muertes diarias en un gráfico de barras:

```{code-cell} ipython3
fig = px.bar(muertes_diarias, x='fecha_def', y='fallecidos_diarios')
fig.show()
```

¡Eso es todo! ¿Recuerdas en la sección anterior, que tuvimos que desplegar las diferentes acciones para poder obtener una visualización. Con esta librería, solamente necesitamos determinar nuestra fuente de datos, el eje de las `x` y el eje de las `y`. El tamaño de la figura se ajusta automáticamente a la ventana, aunque es posible modificarlo con el argumento `width` y `height`. También podemos agregar títulos, leyendas, etiquetas y cambiar el color de las barras. Si pasas el puntero del mouse sobre las líneas, podrás ver los valores de cada punto. Además, puedes hacer zoom y desplazarte por el gráfico.

```{code-cell} ipython3
fig = px.bar(muertes_diarias, x='fecha_def', y='fallecidos_diarios', 
             title='Muertes diarias por COVID-19 en México', 
             labels={'fecha_def':'Fecha', 'fallecidos_diarios':'Muertes diarias'},
             color='fallecidos_diarios')
fig.show()
```

En este caso el gráfico es mucho más atractivo, pero además tiene más componentes semánticos que nos permiten visualizar mejor la información. Por ejemplo, no sólo tenemos una línea más larga cuando corresponde a un mayor número de fallecimientos, sino que además el color nos ayuda a ver de una primera mirada cuáles son los días con mayores decesos.

Notemos además que es un gráfico que en principio es más preciso, puesto que evita crear márgenes y espacios innecesarios que pueden ayudar a malinterpretar la información. Ahora, probemos con un gráfico de líneas.

### Gráfico de líneas

Realicemos un gráfico de líneas con un poco más de formato que el que viene de manera predeterminada. Para enriquecer un gráfico, la manera más común consiste en hacerlo a través de la función `update_layout()` que nos permite cambiar varios elementos como el título, las etiquetas de los ejes, el tamaño de la fuente, etc. También podemos aprovechar la función `update_traces()` para cambiar el color de las líneas, el grosor, etc.

```{code-cell} ipython3
fig = px.line(muertes_diarias, x='fecha_def', y='fallecidos_diarios')
fig.update_layout(
    title="Muertes diarias por COVID-19 en México",
    xaxis_title="Fecha",
    yaxis_title="Muertes diarias",
    font=dict(
        family="Roboto, monospace",
        size=18,
        color="#7f7f7f" # <-- el color de la fuente se puede definir con un código hexadecimal. Para conocer más sobre los códigos de colores, puedes consultar https://htmlcolorcodes.com/es/
    )
)
# color de línea y ancho
fig.update_traces(line_color='#ff7f0e', line_width=2)
fig.show()
```

Ahora, probemos el mismo gráfico pero con una línea suavizada. Para ello, solamente debemos agregar el parámetro `line_shape='spline'` a la función `update_traces()`.

```{code-cell} ipython3
fig = px.line(muertes_diarias, x='fecha_def', y='fallecidos_diarios', 
              title="Muertes diarias por COVID-19 en México", 
              labels={'fecha_def':'Fecha', 'fallecidos_diarios':'Muertes diarias'})
fig.update_traces(line_color='#581845', line_width=2, line_shape='spline') # <-- línea suavizada
fig.show()
```

Ahora intentemos algo más "arriesgado", un gráfico de líneas con dos líneas, una para los contagios de mujeres y otro para hombres:

```{code-cell} ipython3
muertes_diarias_sexo = datos_covid.groupby(['fecha_def', 'sexo'])['decesos'].sum().reset_index(name='fallecidos_diarios')
fig = px.line(muertes_diarias_sexo, x='fecha_def', y='fallecidos_diarios', color='sexo')
fig.update_layout(
    title="Muertes diarias por COVID-19 en México",
    xaxis_title="Fecha",
    yaxis_title="Muertes diarias",
    font=dict(
        family="Roboto, monospace",
        size=18,
        color="#7f7f7f"
    )
)
fig.update_traces(line_width=2, line_shape='spline')
fig.show()
```

Como verás, este tipo de gráfico no es muy adecuado para este tipo de información, puesto que no es posible distinguir los valores de cada línea. Sin embargo, podemos hacer un gráfico de barras apiladas para ver la información de una manera más clara.

### Gráfico de barras apiladas

Para hacer este tipo de gráficos, usamos la misma sintaxis del gráfico de barras, pero agregamos el parámetro `barmode='stack'`:

```{code-cell} ipython3
fig = px.bar(muertes_diarias_sexo, x='fecha_def', y='fallecidos_diarios', color='sexo', barmode='stack')
fig.show()
```

### Gráficos de dispersión

Veámos qué tan bien se correlacionan las variables `edad` y `sexo` con el número de casos en nuestro conjunto de datos. Para ello, usaremos un gráfico de dispersión.

```{code-cell} ipython3
casos_edad_sexo = datos_covid.groupby(['edad', 'sexo']).size().reset_index(name='count')
fig = px.scatter(casos_edad_sexo, x='edad', y='count', color='sexo')
fig.show()
```

De hecho, podemos hacerlo un poco más interesante si agregamos una línea a nuestro gráfico de tal manera que combine lo mejor de ambos gráficos. Para ello, usamos la función `update_traces()` y agregamos el parámetro `mode='markers+lines'`.

```{code-cell} ipython3
fig = px.scatter(casos_edad_sexo, x='edad', y='count', color='sexo')
fig.update_traces(mode='markers+lines')
fig.show()
```

Y podemos hacerlo aún mejor, si cambiamos el tamaño del punto de acuerdo con el número de casos. Para ello, usamos el parámetro `size`.

```{code-cell} ipython3
fig = px.scatter(casos_edad_sexo, x='edad', y='count', color='sexo', size='count')
fig.show()
```

Lo mejor en este tipo de gráficos es que si quieres, puedes aislar una de las variables simplemente haciendo clic en su nombre en la leyenda que quieres ocultar. Realiza el ejercicio y has clic sobre la leyenda 'HOMBRE' y verás que el gráfico se actualiza automáticamente.

### Gráficos de dispersión 3D

Ahora, veamos cómo se comportan las variables `edad`, `sexo` y `decesos` en un gráfico de dispersión 3D.

```{code-cell} ipython3
fig = px.scatter_3d(casos_edad_sexo, x='edad', y='sexo', z='count', color='sexo', size='count')
fig.show()
```

Si arrastras el gráfico puedes hacerlo rotar para verlo desde diferentes ángulos. También puedes hacer clic en la leyenda para ocultar una de las variables.

```{admonition} Gráficos de dispersión 3D
:class: warning
Este tipo de gráficos tiene un gran impacto visual, pero son muy complejos de leer.

Mi recomendación sería que los uses solamente cuando no sea posible representar los datos en un gráfico de líneas o de dispersión 2D.
```

## Multi-gráficos

En ocasiones, es necesario mostrar más de un gráfico en una misma figura. Para ello, usamos la función `make_subplots()` y nos apoyaremos en el módulo `plotly.graph_objects`.

```{code-cell} ipython3
from plotly.subplots import make_subplots
import plotly.graph_objects as go
```

Este es un ejemplo sencillo para que entiendas cómo funciona:

```{code-cell} ipython3
fig = make_subplots(rows=2, cols=2, subplot_titles=("Gráfico 1", "Gráfico 2", "Gráfico 3", "Gráfico 4"))
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=1, col=2)
fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]), row=2, col=1)
fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]), row=2, col=2)
fig.update_layout(height=600, width=800, title_text="Multi-gráficos")
fig.show()
```

Presiento que ya sabes hacia donde vamos en este tutorial. Vamos a hacer un multi-gráfico con la relación entre decesos y enfermedades preexistentes.

Para ello vamos a necesitar un poco más de código y nos centraremos en solamente cuatro enfermedades: hipertensión, enfermedad cardiovascular, enfermedad renal crónica y tabaquismo.

```{code-cell} ipython3
:tags: [remove-cell]
datos_nacionales = '../data/casos_nacionales_covid-19_2022_semestre1.csv'
covid_nacional = pd.read_csv(datos_nacionales, encoding='utf-8')
```

Primero, tenemos que crear un nuevo dataframe para cada enfermedad.

```{code-cell} ipython3
hipertension = covid_nacional.loc[(covid_nacional['hipertension'] == 'SI') & (covid_nacional['fecha_def'].notnull())]
cardiovascular = covid_nacional.loc[(covid_nacional['cardiovascular'] == 'SI') & (covid_nacional['fecha_def'].notnull())]
renal_cronica = covid_nacional.loc[(covid_nacional['renal_cronica'] == 'SI') & (covid_nacional['fecha_def'].notnull())]
tabaquismo = covid_nacional.loc[(covid_nacional['tabaquismo'] == 'SI') & (covid_nacional['fecha_def'].notnull())]
```

Después podemos crear los grupos de datos para cada enfermedad.

```{code-cell} ipython3
# agrupar por edad y fecha de defunción
hipertension = hipertension.groupby(['edad', 'hipertension']).size().reset_index(name='count')
cardiovascular = cardiovascular.groupby(['edad', 'cardiovascular']).size().reset_index(name='count')
renal_cronica = renal_cronica.groupby(['edad', 'renal_cronica']).size().reset_index(name='count')
tabaquismo = tabaquismo.groupby(['edad', 'tabaquismo']).size().reset_index(name='count')
```

Y ahora, con cada grupo, podemos crear un gráfico de dispersión que mostraremos en una misma figura.

```{code-cell} ipython3
fig = make_subplots(rows=2, cols=2, subplot_titles=("Hipertensión", "Enfermedad cardiovascular", "Enfermedad renal crónica", "Tabaquismo"))
fig.add_trace(go.Scatter(x=hipertension['edad'], y=hipertension['count'], mode='markers'), row=1, col=1)
fig.add_trace(go.Scatter(x=cardiovascular['edad'], y=cardiovascular['count'], mode='markers'), row=1, col=2)
fig.add_trace(go.Scatter(x=renal_cronica['edad'], y=renal_cronica['count'], mode='markers'), row=2, col=1)
fig.add_trace(go.Scatter(x=tabaquismo['edad'], y=tabaquismo['count'], mode='markers'), row=2, col=2)
fig.update_layout(height=600, width=800, title_text="Relación entre edad, número de decesos y enfermedades preexistentes")

# actualizar los ejes
for i in range(1, 3):
    fig.update_yaxes(title_text="Número de decesos", row=1, col=i)
    fig.update_yaxes(title_text="Número de decesos", row=2, col=i)
    fig.update_xaxes(title_text="Edad", row=1, col=i)
    fig.update_xaxes(title_text="Edad", row=2, col=i)

fig.show()
```

Vemos en este caso que es más fácil leer este tipo de figura ya que podemos comparar a simple vista la correlacion entre número de decesos, edad y enfermedad preexistente. Sin embargo, no es una tarea perfecta ¿qué sucede si una persona tenía más de una enfermedad preexistente? ¿eso podría implicar una mayor relación entre edad y número de decesos? En realidad, podríamos continuar explorando estos datos, pero con las consideraciones anteriores es suficiente para este curso.

Como verás, las opciones son múltiples. Puedes cambiar el tamaño de la figura, el color de los puntos, el tipo de gráfico, etc. Lastimosamente, no podemos cubrir todas las opciones de gráficas, pero ya te estarás dando cuenta que en buena medida las posibilidades son muchísimas.

Con estos ejemplos, puedes emprender la tarea de crear tus propios gráficos, ya sea con `matplotlib` o con `plotly`. 

## Notas

[^footnote]: Para más información sobre plotly, puedes consultar su [documentación](https://plotly.com/python/).
