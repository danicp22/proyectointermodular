# Programa registros
# v0.1 Daniel Calve Pardo 2025
# Este programa permite crear, listar, actualizar y eliminar datos de una base de datos.





import mysql.connector    # Importamos la libreria

print("Bienvenidos a la aplicacion")


# Nos conectamos a la base de datos
conexion = mysql.connector.connect(  
    host="localhost",
    user="dani",
    password="Dani12345&",
    database="portafolioexamen"
)

cursor = conexion.cursor()

while True:                             # Creamos el bucle
    print("Selecciona una opcion:")
    print("1.-Crear un registro:")
    print("2.-Listar registros:")
    print("3.-Actualizar registro:")
    print("4.-Eliminar registro:")

    opcion = int(input("Elige tu opcion: "))  # Pedimos que elijan la opcion

    if opcion == 1:
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        id_categoria = input("Introduce la categoria: ")
        cursor.execute('''
            INSERT INTO piezasportafolio VALUES (
            NULL,
            "'''+titulo+'''",
            "'''+descripcion+'''",
            "'''+fecha+'''",
            '''+id_categoria+'''
            );
            ''')
        conexion.commit()
    
    elif opcion == 2:
        cursor.execute('''
      SELECT * FROM piezasportafolio;
    ''')
        filas = cursor.fetchall()

        for fila in filas:
            print(fila)
    
    elif opcion == 3:
        identificador = input("Introduce el id a actualizar: ")
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        id_categoria = input("Introduce la categoria: ")
        cursor.execute('''
            UPDATE piezasportafolio SET 
            titulo = "'''+titulo+'''",
            descripcion = "'''+descripcion+'''",
            fecha = "'''+fecha+'''",
            id_categoria = '''+id_categoria+'''
            WHERE id = '''+identificador+''';
            ''')
        conexion.commit()
    
    elif opcion == 4:
        id = input("Introduce el id a eliminar: ")
        cursor.execute('''
            DELETE FROM piezasportafolio
            WHERE id = '''+id+'''
            ''')
        conexion.commit()