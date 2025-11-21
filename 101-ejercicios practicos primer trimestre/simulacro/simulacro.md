- En este ejercicio he desarrollado un programa que conecta una base de datos MySQL con una aplicación web creada con Flask. El objetivo es mostrar en una página web los datos que previamente se han insertado desde otro archivo Python. Este tipo de solución es muy útil en proyectos donde se necesita visualizar información almacenada en una base de datos, como catálogos de productos, listados de usuarios o inventarios. Además, permite separar la lógica de inserción de datos (en un archivo) de la lógica de visualización (en otro), lo que mejora la organización del proyecto.



1.  Importaciones necesarias:
    ```
    import mysql.connector
    from flask import Flask
    ```
    *   `mysql.connector`: permite conectar Python con una base de datos MySQL.
    *   `Flask`: es el microframework que usamos para crear la aplicación web.

2.  Conexión a la base de datos:
    ```
    conexion = mysql.connector.connect(
      host="localhost",
      user="portafolioceac",
      password="Dani123456&amp;",
      database="portafolio"
    )
    ```
    Aquí se establece la conexión con la base de datos `portafolio` usando las credenciales proporcionadas.

3.  Creación del cursor y de la app Flask:
    ```
    cursor = conexion.cursor()
    app = Flask(__name__)
    ```
    *   El cursor permite ejecutar consultas SQL.
    *   `Flask(__name__)` inicializa la aplicación web.

4.  Ruta principal de la web:
    ```
    @app.route("/")
    def holamundo():
    ```
    Esta función se ejecuta cuando el usuario accede a la raíz del sitio web (`/`).

5.  Consulta a la base de datos:
    ```
    cursor.execute("SELECT * FROM vista_piezas;")
    filas = cursor.fetchall()
    ```
    Se recuperan todos los registros de la vista `vista_piezas`.

6.  Generación del HTML:
    *   Se construye una cadena HTML que contiene:
        *   Un encabezado con tu nombre y correo.
        *   Un `main` con artículos generados dinámicamente a partir de los datos de la base.
        *   Un pie de página con tu firma.
    *   Cada `fila` representa una pieza, y se muestra con su nombre, descripción, precio e imagen.

7.  Ejecución de la app:
    ```
    if __name__ == "__main__":
        app.run(debug=True)
    ```
    Esto lanza el servidor web en modo debug para desarrollo.





- A continuación se muestra un ejercicio que, gracias a la conexión con una base de datos y al uso de Flask, permite mostrar en una página web los datos almacenados en una tabla o vista SQL. Es ideal para proyectos donde se necesita una interfaz visual para consultar información:

```
import mysql.connector
from flask import Flask

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="Dani123456&amp;",
  database="portafolio"
)

cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")
def holamundo():
  cursor.execute("SELECT * FROM vista_piezas;")
  filas = cursor.fetchall()

  cadena = ''' 
    <!doctype html>
<html lang="es">
  <head>
    <title>Examen</title>
    <meta charset="utf-8">
    <style>
      html,body{background:grey;font-family:sans-serif;}
      header,main,footer{
        background:white;
        padding:20px;
        width:800px;
        margin:auto;
        text-align:center;
      }
      main{
        display:grid;
        grid-template-columns:auto auto auto;
        gap:20px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Daniel Calve Pardo</h1>
      <h2>daniel@example.com</h2>
    </header>
    <main>
  '''
  for fila in filas:
    cadena += '''
      <article>
        <p>'''+fila[0]+'''</p>
        <h3>'''+fila[2]+'''</h3>
        <p>'''+str(fila[3])+'''</p>
        <img src="'''+fila[4]+'''">
      </article>
  '''
  cadena += ''' 
    </main>
    <footer>
      (c) 2025 Daniel Calve Pardo
    </footer>
  </body>
</html>
  '''
  return cadena

if __name__ == "__main__":
    app.run(debug=True)
```




- Este ejercicio me ha servido para integrar una base de datos con una aplicación web usando Flask. Me ha ayudado a entender cómo se puede separar la lógica de inserción de datos de la lógica de visualización, y cómo se puede generar HTML dinámico a partir de los datos almacenados. Además, he reforzado el uso de rutas en Flask y la importancia de estructurar bien el código para que sea claro y funcional.