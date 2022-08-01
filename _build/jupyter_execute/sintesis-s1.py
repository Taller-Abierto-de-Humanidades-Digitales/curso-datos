#!/usr/bin/env python
# coding: utf-8

# # ¿Qué aprendimos esta semana?
# 
# Vamos a repasar los objetivos de la primera semana de este curso.
# 
# * Creaste un cuaderno en Google Colab, editar celdas de texto y código, y realizar importaciones de archivos de texto.
# * Compartiste públicamente un cuaderno de Google Colab.
# * Buscaste una fuente de datos en los repositorios públicos de datos abiertos.
# * Seleccionaste una fuente de datos teniendo en cuenta su descripción, creadores, rango de tiempo y tipo de archivo.
# * Importaste la fuente de datos a tu Google Drive y de allí a tu Google Colab utilizando Python.
# 
# ## ¿Qué aprendiste de programación en Python esta semana?
# 
# Si seguiste detenidamente los pasos de esta primera semana, habrás aprendido algunas habilidades básicas de programación.
# 
# ### Sintáxis básica
# 
# Python es un lenguaje con una sintaxis muy sencilla. Básicamente comprende los siguientes aspectos:
# 
# #### Indentación
# 
# Cada bloque de código se escribe con espacios o tabuladores. Por ejemplo:

# In[1]:


if 5 > 2:
    print("5 es mayor que 2")


# Nota que hay cinco espacios entre la primera instrucción `if 5 > 2:` y la segunda instrucción `print("5 es mayor que 2")`. Si utilizamos otro "formato" vamos a encontrar un error:

# In[2]:


if 5 > 2: 
print("5 es mayor que 2")


# #### Comentarios
# 
# Los comentarios son una forma de documentar el código.

# In[3]:


# Este es un comentario
print("Hola mundo")


# Como ves, los comentarios se escriben con un `#` y seguido del texto. El programa no los ejecuta y sirven solamente para anotar el código.
# 
# ### Variables
# 
# Las variables son una forma de almacenar información.

# In[4]:


nombre = "Juan"
edad = 30
distancia = 3.7
kilometros = True
print(nombre)
print(edad)
print(distancia)
print(kilometros)


# Las variables se declaran con un nombre y se asignan un valor.
# 
# #### Tipos de datos
# 
# * `nombre` es una variable de tipo `str` (string) que almacena una cadena de texto.
# * `edad` es una variable de tipo `int` (entero) que almacena un número entero.
# * `distancia` es una variable de tipo `float` (flotante) que almacena un número con decimales.
# * `kilometros` es una variable de tipo `bool` (booleano) que almacena un valor booleano.
# 
# ### Manejo de archivos
# 
# El manejo de archivos básico en Python se realiza a través de estas dos funciones:
# 
# * `open()` permite abrir un archivo para lectura o escritura.
# * `read()` permite leer el contenido de un archivo.
# 
# La función `open()` recibe dos parámetros:
# 
# * `file` es el nombre del archivo que se quiere abrir.
# * `mode` es el modo de apertura del archivo.
# 
# Si queremos abrir un archivo para lectura, el modo de apertura es `r`.

# In[5]:


archivo = open("file_samples/ejemplo-1.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()


# Si queremos abrir un archivo para escritura, el modo de apertura es `w`.

# In[6]:


archivo = open("file_samples/ejemplo-2.txt", "w")
archivo.write("Hola mundo")
archivo.close()


# Existen otros modos de apertura, como `a` para agregar contenido al archivo y `x` para crear un archivo nuevo si no existe. En este momento, es suficiente con conocer el modo general de lectura y escritura de archivos.
# 
# ### Importar librerías o módulos
# 
# Los módulos son una forma de organizar un conjunto de funciones y clases que pueden ser utilizadas en un programa.

# In[7]:


import math
print(math.pi)


# 
# * `math` es el nombre del módulo que contiene las funciones matemáticas.
# * `pi` es el nombre de la función que contiene el valor de `math.pi`.
# 
# ## ¿Qué aprendiste de datos abiertos esta semana?
# 
# Reconociste que los datos abiertos son una forma de acceder a una fuente de datos proveniente de instituciones gubernamentales, relacionadas primordialmente con el diagnóstico y aplicación de políticas públicas.
# 
# ### Formatos de archivo
# 
# El formato de archivo primordial en los datos abiertos es el CSV (comma-separated values). Sin embargo, es posible que la información se suba en otros formatos como XLSX, JSON, XML, etc.
# 
# * `csv` es un formato de archivo para archivos de texto que contienen datos separados por comas.
# 
# ### Metadatos
# 
# El metadato es una forma de almacenar información que describe una fuente de datos. Por ejemplo:
# 
# * `descripción` es una descripción de la fuente de datos.
# * `creadores` son los autores de la fuente de datos.
# * `rango de tiempo` es un rango de tiempo que describe el periodo de tiempo que abarca la fuente de datos.
# * `tipo de archivo` es el tipo de archivo que contiene la fuente de datos.
