from flask import Flask, render_template, request  # Tomo parametros de la url

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/envio")
def envio():
    nombre = request.args.get("nombre")
    apellidos = request.args.get("apellidos")
    print(nombre,apellidos)
    return "Mira en la consola si ha pasado algo" 

if __name__ == "__main__":
    app.run(debug=True)