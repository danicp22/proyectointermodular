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