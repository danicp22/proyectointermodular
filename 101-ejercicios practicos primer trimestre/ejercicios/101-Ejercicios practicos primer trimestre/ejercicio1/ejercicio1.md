- En el desarrollo web moderno, los frameworks permiten crear aplicaciones de forma rápida y estructurada. Flask es un microframework de Python que facilita la creación de servidores web ligeros y funcionales. Es ideal para aprender los fundamentos del backend, crear APIs, y generar contenido dinámico en páginas HTML. Este ejercicio te guía en la creación de tu primer servidor Flask, mostrando cómo generar contenido HTML desde Python.


- Primero se importa el módulo Flask desde la librería flask, que es el núcleo del framework: `from flask import Flask`

- A continuación, se crea una instancia de Flask llamada aplicacion, que representa el servidor web. Se le pasa __name__ como argumento para que Flask sepa dónde buscar recursos:
```
aplicacion = Flask(__name__)
```

- Luego se define una ruta principal ("/") usando el decorador @aplicacion.route("/"). Esta ruta se ejecuta cuando el usuario accede a la raíz del sitio web:
```
@aplicacion.route("/")
def raiz():
    return "Esto es HTML desde Flask"
```

- Finalmente, se arranca el servidor con aplicacion.run(debug=True), que inicia el servidor en modo depuración para facilitar el desarrollo:
```
if __name__ == "__main__":
    aplicacion.run(debug=True)
```


- Para ejecutar el servidor, se abre una terminal y se ejecuta el archivo app.py con el comando: `python app.py`



- A continuacion se muestra un ejercicio en el que se utiliza flask para mostrar un html en navegador:
```
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>Prueba de Flask</title>
        <style>
          h1{color:red;}
        </style>
      </head>
      <body>
        <h1>Bienvenido a mi sitio web</h1>
  '''
      
  for dia in range(1,31):
    cadena += '<div>'+str(dia)+'</div>' 
      
  cadena += '''
      </body>
    </html>
  '''
  return cadena

if __name__ == "__main__":
  aplicacion.run(debug=True)

```




- Este ejercicio te permite dar tus primeros pasos con Flask, aprendiendo a crear un servidor web básico y generar contenido HTML dinámico desde Python. Es una base excelente para construir aplicaciones más complejas, como blogs, paneles de control, o APIs REST. Además, te familiariza con conceptos clave como rutas, renderizado de contenido y ejecución de servidores locales.