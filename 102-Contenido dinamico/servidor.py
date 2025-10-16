from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    #################### Este es el primer bloque
    cadena = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Document</title>
        <meta charset="UTF-8">
        <style>
            body{background: steelblue;color: steelblue;font-family: sans-serif;}
            header,main,footer{background: white;padding: 20px;margin: auto;width: 600px;}
            header,footer{text-align: center;}
            main{color: black;}
        </style>  
    </head>
    <body>
        <header><h1>DANIBLOG</h1></header>
        <main>
        '''
        ################## Este es otro bloque 
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
            ################ Este es otro bloque
    cadena += '''
        </main>
        <footer>(c)2025 Daniel Calve Pardo</footer>
    </body>
</html>
''' 

    return cadena 

#Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)