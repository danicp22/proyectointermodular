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
      user="dani",
      password="Dani12345;",
      database="portafolioexamen"
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



- A continuacion se muestra un ejercicio, que, gracias a la libreria flask y mysql.connector, permite conectar un archivo python, con una base de datos y poder abrirla en la web con un archivo html:
```
# Programa multifuncion
# v0.1 Daniel Calve Pardo
# Este programa esta conectado a una base de datos creada previamente, y a un archivo python, en el archivo python se añade la informacion, la cual se guarda en la base de datos, y este programa lo que hace es que lo muestra en la web.





import mysql.connector                                # Importo el conector a base de datos
from flask import Flask                               # Importo la libreria flask

conexion = mysql.connector.connect(
  host="localhost",
  user="dani",
  password="Dani12345&",
  database="portafolioexamen"
  )                                                   # Me conecto a la base de datos

cursor = conexion.cursor()                # Creo un cursor
app = Flask(__name__)                     # Creo una aplicación Flask (web)

@app.route("/")                           # Atrapo la ruta raiz (/)
def holamundo():                          # Defino una funcion
  cursor.execute("SELECT * FROM vista_piezas;")  # Pido el contenido de la vista

  filas = cursor.fetchall()                 # Lo guardo en una lista
  ########### AQUI PONGO EL INICIO HASTA EL MAIN
  cadena = ''' 
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portafolio trimestral</title>
    <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #e6e6e6;
    }
    header, footer {
      background-color: #7da7df;
      color: white;
      text-align: center;
      padding: 10px;
    }
    main {
      padding: 20px;
    }
    article {
      background-color: white;
      margin-bottom: 15px;
      padding: 10px;
      border-radius: 5px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }
    article div {
        flex: 1;
    }
    article img {
      width: 100%;
      max-width: 300px;
      display: block;
      margin: 10px 0;
      border-radius: 5px;
    }
    </style>
</head>
<body>
    <header>
        <h1>Daniel Calve Pardo</h1>
        <p>daniel@hola.com</p>
    </header>
    <main>
  '''                               # Creo una cadena vacia
  ########### AQUI PONGO LO QUE SE REPITE
  for fila in filas:                        # Para cada elemento de la lista
    cadena += '''
      <article>
        <h3>'''+fila[0]+'''</h3>
        <p>'''+fila[1]+'''</p>
        <p>'''+str(fila[2])+'''</p>
        <p>'''+fila[3]+'''</p>
        <img src="static/examen.webp">
      </article>
  '''
  ########### AQUI PONGO EL FINAL
  cadena += ''' 
    </main>
    <footer>
        <a href="https://instagram.com/daaani_.222">Instagram</a>
        <a href="https://github.com/danicp22">GitHub</a>
        <p>© 2025 Daniel Calve Pardo. Todos los derechos reservados.</p>
    </footer>
    
</body>
</html>
  '''
  return cadena                             # Devuelvo la cadena como HTML en la web

if __name__ == "__main__":                # Si este es el archivo principal
    app.run(debug=True)                   # Ejecuta la web

```



- Este ejercicio es muy util para el mundo de la informatica, ya que facilita mucho el trabajo del programador, introducir datos a una base de datos desde python es muy interesante, pero si encima podemos añadirle html para que tenga un aspecto visual en una web, es increible. Este ejercicio me ha ayudado a entender cómo se puede separar la lógica de inserción de datos de la lógica de visualización, y cómo se puede generar HTML dinámico a partir de los datos almacenados. Además, he reforzado el uso de rutas en Flask y la importancia de estructurar bien el código para que sea claro y funcional.