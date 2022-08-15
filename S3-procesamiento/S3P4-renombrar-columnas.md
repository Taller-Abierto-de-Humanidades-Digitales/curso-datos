# Renombrar columnas

Un problema común de las fuentes de datos abiertas está relacinado con la forma en la cuales están nombradas las columnas. Es usual recurrir a abreviaturas, pero también es común que las categorías estén marcadas en forma de códigos. En nuestro caso, la mayoría de columnas son lo suficientemente descriptivas para que no sea necesario renombrarlas. Sin embargo, podríamos darles un nombre aún más descriptivo, en particular a las columnas `["entidad_nac","entidad_res","municipio_res]`.

La sintaxis para renombrar una columna es:

```python
df.rename(columns={'columna_original':'nuevo_nombre'}, inplace=True)
```

El parámetreo `inplace` es opcional, pero si no se especifica debe asignarse el resultado a una nueva variable, de otra manera parecerá que el renombre no tuvo éxito.

Como muchas operaciones en `pandas` podemos valernos de un diccionario para modificar aplicar una serie de cambios a las columnas. Sirvámonos de nuestro ejemplo de datos:

```{code-cell} ipython
:tags: ["remove-cell"]
try:
  covid_nacional = pd.read_csv('../data/casos_nacionales_covid-19_2022_semestre1.csv')
except FileNotFoundError:
  covid_nacional = pd.read_csv('../datos/casos_nacionales_covid-19_2022_semestre1.csv')
```

```{code-cell} ipython
# Renombrar columnas
covid_nacional.rename(columns={
    "entidad_nac": "entidad_nacimiento",
    "entidad_res": "entidad_residencia",
    "municipio_res": "municipio_residencia"
}, inplace=True)
covid_nacional.head()
```

## ¿Por qué modificar las columnas desde el programa en lugar de hacerlo directamente en el csv?

En primer lugar, porque podemos cometer un error al renombrar el archivo original, por ejemplo, borrar un coma y modificar la separación de las columnas. También, al guardar nuevamente el conjunto de datos podemos cambiar su codificación y perder algunos datos. Además, si la fuente de datos se actualiza aplicamos el código a un nuevo archivo ya no funcionará porque no encontrará correctamente los nombres de las columnas. Y finalmente, porque es mucho más fácil modificar el código que modificar el archivo original; un archivo muy grande puede ser lento para abrir y más para modificar, por eso es mucho más rápido hacerlo directamente desde nuestro programa.
