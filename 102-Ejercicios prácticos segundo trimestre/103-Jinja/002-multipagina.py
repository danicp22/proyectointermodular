# Importo libreria flask para crear web
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def inicio():   
    # Renderizo una plantilla llamada index.html
    return render_template("inicio.html")

@app.route("/sobremi")
def sobremi():   
    # Renderizo una plantilla llamada index.html
    return render_template("sobremi.html")

@app.route("/contacto")
def contacto():   
    # Renderizo una plantilla llamada index.html
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)