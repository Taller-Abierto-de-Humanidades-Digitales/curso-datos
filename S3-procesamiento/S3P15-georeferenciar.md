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

# Georeferenciar

Ya vimos en el apartado dedicado a la [unión de dataframes](../S3-procesamiento/S3P5-union-df.md) como agregar la información de geolocalización de un conjunto de datos a otro. En este sentido, la complejidad radica simplemente en encontrar un listado o conjunto de datos que coincida con los espacios que queremos representar.

Lo que tenemos que garantizar simplemente es que la clave del nombre coincida con el lugar de geolocalización.

En datos globales, la geolocalización por países puede valerse de los códigos alpha-2 y alpha-3, que corresponden a una cadena de dos o tres letras que identifican el país.

En Python, una librería muy utilizada para realizar esta tarea es [`pycountry`](https://pypi.org/project/pycountry/).

Para usar esta librería en Google Colab, primero necesitamos instalarla de la siguiente manera:

```{code-cell} ipython
!pip install pycountry
```

Posteriormente podemos importarla y utilizarla:

```{code-cell} ipython
import pycountry
pycountry.countries.get(alpha_2='MX')
```

Nuestra fuente de datos de `covid_nacional` contiene información relacionada con el país de origen, disponible en la columna `pais_nacionalidad`, así que podremos transformar esa columna para obtener los datos de georeferenciación. 

Pero antes, veamos un ejemplo ideal:

```{code-cell} ipython
import pandas as pd
paises = pd.DataFrame({'Nombre': ['Andrea', 'Natalia', 'Guadalupe', 'Pedro', 'Joaquín', 'Julio', 'Luisa', 'Juan', 'Vicente'], 'País': ['Mexico', 'United States', 'Spain', 'France', 'Italy', 'Germany', 'China', 'Japan', 'Korea, Republic of']})
paises
```

En este caso, podemos utilizar un función para obtener el código alpha-2 de cada país a partir de su nombre en inglés:

```{code-cell} ipython
paises['alpha2'] = paises['País'].apply(lambda x: pycountry.countries.get(name=x).alpha_2)
paises
```

Con este dato (alpha_2 o alpha_3) tendremos la posibilidad de visualizar nuestra información en un mapa.

```{admonition} Función lambda
:class: tip
En este caso utilizamos una función lambda. Este es un concepto algo complicado, pero básicamente, es una función que utilizaremos una sola vez y de manera repetida en una serie de filas.
```

Obviamente, el inconveniente ahora será encontrar una opción para los casos en español. En este caso, incluyo esta función, modificada ligeramente a partir de esta respuesta dada en [StackOverflow](https://stackoverflow.com/a/62486395), con la cual podemos realizar esta conversión:

```{code-cell} ipython
import gettext

def map_country_code(country_name, language, iso):
    '''
    country_name: str. El nombre del país en español.
    language: str. El idioma en el que se desea obtener el código (p. ej: 'es').
    iso: str. Opciones posibles: 'alpha_2' o 'alpha_3'.
    '''
    try:
        if country_name is None:
            return None
        elif country_name == 'MÉXICO': # esta condición sintetiza el caso de México (reduce de 5 minutos a 6 segundos el tiempo de ejecución)
            if iso == 'alpha_2':
                return 'MX'
            elif iso == 'alpha_3':
                return 'MEX'
        spanish = gettext.translation('iso3166', pycountry.LOCALES_DIR, languages=[language])
        spanish.install()
        _ = spanish.gettext
        for english_country in pycountry.countries:
            country_name = country_name.lower()
            spanish_country = _(english_country.name).lower()
            if spanish_country == country_name:
                if iso == 'alpha_3':
                    return english_country.alpha_3
                elif iso == 'alpha_2':
                    return english_country.alpha_2
    except Exception as e:
        raise
```

Por lo pronto, solamente es relevante que con esta función puedes obtener el código alpha-2 o alpha-3 de un país en varios idiomas. Podemos probar que funciona de la siguiente manera:

```{code-cell} ipython
map_country_code('España', 'es', 'alpha_2')
```

Ahora, vamos a aplicarlo a nuestro conjunto de datos:

```{code-cell} ipython
muestra_covid['alpha3'] = muestra_covid['pais_nacionalidad'].apply(lambda x: map_country_code(x, 'es', 'alpha_3'))
muestra_covid['alpha2'] = muestra_covid['pais_nacionalidad'].apply(lambda x: map_country_code(x, 'es', 'alpha_2'))
muestra_covid.head()
```

Como verás, las soluciones no siempre vienen dadas de antemano. Ciertas situaciones requerirán de nuestra exploración y creatividad para resolver un problema o alcanzar el objetivo que estamos buscando.

La gran riqueza de la programación radica, precisamente, en la capacidad creativa que podemos tener con cada lenguaje.
