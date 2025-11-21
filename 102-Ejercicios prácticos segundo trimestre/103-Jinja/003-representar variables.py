from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def inicio():
    # mi_nombre es la variable que esta en python
    mi_nombre = "Daniel"   
    # nombre es la variable que lanzo a la pantalla
    return render_template("variable.html" ,nombre=mi_nombre)


if __name__ == "__main__":
    app.run(debug=True)