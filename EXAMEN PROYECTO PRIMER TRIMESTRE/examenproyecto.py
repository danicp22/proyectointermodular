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