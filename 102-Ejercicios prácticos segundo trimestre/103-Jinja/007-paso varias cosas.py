from flask import Flask, render_template
import mysql.connector
################################## MYSQL ##################################################
conexion = mysql.connector.connect(   
    host="localhost",
    user="dani",
    password="Dani12345&",
    database="portafolioexamen"
)

cursor = conexion.cursor()                                
# ------------------------------ Esto envia las tablas-------------------------------------
cursor.execute("SHOW TABLES;")                               
tablas = []                                                
filas = cursor.fetchall()                                 
for fila in filas:                                          
    tablas.append(fila[0])                                   
# ----------------------------- Esto envia las cabeceras de las tablas --------------------
cursor.execute("SHOW COLUMNS in piezasportafolio;")                               
columnas = []                                                  
filas = cursor.fetchall()                                    
for fila in filas:                                            
    columnas.append(fila[0])                                    
################################## MYSQL ##################################################


app = Flask(__name__)


@app.route("/")
def inicio(): 
    return render_template(
        "backoffice.html",
        mis_tablas = tablas,
        mis_columnas = columnas
        ) 


if __name__ == "__main__":
    app.run(debug=True)