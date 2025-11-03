- En el desarrollo web moderno, es común utilizar frameworks ligeros como **Flask** para crear aplicaciones dinámicas. Este ejercicio simula un pequeño blog personal llamado **JOCARSAblog**, que muestra artículos almacenados en un archivo JSON. El objetivo es generar una página web que se actualiza automáticamente con el contenido del archivo, sin necesidad de modificar el HTML manualmente.

- Este tipo de aplicación es útil para proyectos personales, blogs educativos o incluso como base para sistemas más complejos.





- 1. Importación de módulos

```- 
from flask import Flask
import json
```

- `Flask`: se importa el framework que permite crear la aplicación web.
- `json`: se usa para leer el archivo `blog.json`, que contiene los artículos del blog en formato estructurado.

- 2. Creación de la aplicación

```
aplicacion = Flask(__name__)
```

- Se crea una instancia de Flask llamada `aplicacion`.
- El parámetro `__name__` indica que este archivo es el principal del proyecto.

- 3. Definición de la ruta principal

```
@aplicacion.route("/")
def raiz():
```

- Se define la ruta raíz (`"/"`), que es la página principal del sitio.
- La función `raiz()` se ejecuta cuando el usuario accede a esa ruta.

- 4. HTML base como cadena

```
cadena =  '''
    &lt;!doctype html&gt;
    ...
    &lt;main&gt;
'''
```

- Se crea una cadena que contiene el HTML de la página.
- Importante: los símbolos `&lt;` y `&gt;` representan `<` y `>` en HTML. Esto parece un error: deberían usarse los símbolos reales para que el navegador interprete correctamente el HTML.

- 5. Lectura del archivo JSON

```
archivo = open("blog.json",'r')
contenido = json.load(archivo)
```

- Se abre el archivo `blog.json` en modo lectura.
- Se carga su contenido como una lista de diccionarios con `json.load`.

Ejemplo de contenido del archivo:

```
[
  {
    "titulo": "Primer post",
    "fecha": "2025-11-01",
    "autor": "Daniel",
    "contenido": "Bienvenidos a mi blog personal."
  }
]
```

- 6. Generación dinámica de artículos

```
for linea in contenido:
    cadena += '''
      &lt;article&gt;
        &lt;h3&gt;'''+linea['titulo']+'''&lt;/h3&gt;
        &lt;time&gt;'''+linea['fecha']+'''&lt;/time&gt;
        &lt;p&gt;'''+linea['autor']+'''&lt;/p&gt;
        &lt;p&gt;'''+linea['contenido']+'''&lt;/p&gt;
      &lt;/article&gt;
      '''
```

- Se recorre cada entrada del JSON.
- Por cada artículo, se añade un bloque HTML con su título, fecha, autor y contenido.
- Se usa concatenación de cadenas para insertar los valores dinámicamente.

- 7. Cierre del HTML

```
cadena += '''
    &lt;/main&gt;
    &lt;footer&gt;(c)2025 Daniel Calve Pardo&lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
  '''
```

- Se cierra el contenido principal y se añade un pie de página con el nombre del autor.

- 8. Retorno de la cadena

```
return cadena
```

- Se devuelve la cadena HTML como respuesta a la ruta principal.


- 9. Ejecución de la aplicación

```
if __name__ == "__main__":
  aplicacion.run(debug=True)
```

- Si el archivo se ejecuta directamente, se inicia el servidor Flask en modo `debug`, lo que permite ver errores y recargar automáticamente.



- A continuación se muestra un ejercicio que, gracias a Flask y a la lectura de archivos JSON, genera una página web que muestra artículos de un blog de forma dinámica:

```
from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena =  '''
    <!doctype html>
    <html lang="es">
      <head>
        <title>Daniblog</title>
        <meta charset="utf-8">
        <style>
          body{background:steelblue;color:white;font-family:sans-serif;}
          header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
          header,footer{text-align:center;}
          main{color:black;}
        </style>
      </head>
      <body>
        <header><h1>JOCARSAblog</h1></header>
        <main>
    '''
    
    archivo = open("blog.json",'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
          <article>
            <h3>'''+linea['titulo']+'''</h3>
            <time>'''+linea['fecha']+'''</time>
            <p>'''+linea['autor']+'''</p>
            <p>'''+linea['contenido']+'''</p>
          </article>
          '''
    
    cadena += '''
        </main>
        <footer>(c)2025 Daniel Calve Pardo</footer>
      </body>
    </html>
    '''
  
    return cadena
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
```



Este ejercicio demuestra cómo crear una aplicación web básica con Flask que genera contenido dinámico a partir de un archivo JSON. Se ha utilizado HTML embebido en Python, lo cual es útil para proyectos pequeños. 
