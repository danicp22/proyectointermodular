- En el desarrollo de aplicaciones web, uno de los patrones arquitectónicos más utilizados es el Modelo-Vista-Controlador (MVC). Este patrón permite separar la lógica de negocio, la interfaz de usuario y el control de flujo, facilitando el mantenimiento y la escalabilidad del código. En esta práctica, aprenderás a implementar una aplicación web sencilla con Flask, un microframework de Python, que carga y muestra datos personales desde un archivo JSON. Esta estructura simula un pequeño sistema MVC, ideal para comprender cómo se conectan los distintos componentes.




A continuación, se detallan los pasos para construir la aplicación:

1.  Instalación de Flask
    Asegúrate de tener Flask instalado. Si no lo tienes, ejecuta:
    ```
    pip install flask
    ```

2.  Creación del modelo (archivo JSON)
    Crea un archivo llamado `curriculum.json` que contendrá los datos personales del usuario. Este archivo actúa como el modelo, ya que almacena la información que se mostrará.

3.  Creación de la vista (HTML)
    El archivo `curriculum.html` representa la vista. Utiliza placeholders de Jinja2 (`{{ }}`) para insertar dinámicamente los datos del modelo.

4.  Creación del controlador (Python con Flask)
    El archivo `curriculum.py` actúa como el controlador. Se encarga de:
    *   Leer los datos del archivo JSON.
    *   Cargar la plantilla HTML.
    *   Renderizar la vista con los datos del modelo.

5.  Ejecución de la aplicación
    Ejecuta el archivo `curriculum.py` y accede a `http://127.0.0.1:5000/` para ver el resultado.





- A continuación se muestra un ejercicio que, gracias al uso del patrón MVC, carga datos personales desde un archivo JSON y los muestra en una página web con Flask:

Archivo `curriculum.json`:

```
{
  "datos personales":{
    "nombre":"Jose Vicente",
    "apellidos":"Carratalá Sanchis",
    "email":"info@jocarsa.com",
    "telefono":"620891718",
    "direccion":"La calle de Jose Vicente",
    "codigo_postal":"46000 Valencia"
  },
  "experiencia":"",
  "formacion":""
}
```

Archivo `curriculum.html`:
```
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
    <style>
      html{background:grey;font-family:sans-serif;}
      body{background:white;margin:auto;min-height:200px;display:flex;width:600px;}
      #izquierda{flex:1;background:darkblue;padding:20px;}
      #derecha{flex:4;background:white;padding:20px;}
    </style>
  </head>
  <body>
    <div id="izquierda"></div>
    <div id="derecha">
      <h1>{{nombre}} {{apellidos}}</h1>
      <p>{{email}}</p>
      <ul>
        <li>{{telefono}}</li>
        <li>{{direccion}}</li>
        <li>{{codigo_postal}}</li>
      </ul>
    </div>
  </body>
</html>
```


Archivo `curriculum.py`:

```
from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/")
def cv():
    with open("curriculum.json", encoding="utf-8") as f:
        data = json.load(f)
    dp = data["datos personales"]

    with open("curriculum.html", encoding="utf-8") as f:
        html = f.read()

    return render_template_string(html, **dp)

if __name__ == "__main__":
    app.run(debug=True)
```





Este ejercicio te ha permitido comprender cómo aplicar el patrón MVC en una aplicación web sencilla con Flask. Has aprendido a separar los datos (modelo), la presentación (vista) y la lógica de control (controlador), lo que facilita la organización del código y su mantenimiento. Además, has practicado la lectura de archivos JSON y la renderización dinámica de plantillas HTML. Esta base te será muy útil para proyectos más complejos en el futuro.

