#Este módulo realiza la carga de datos en la BBDD 
import sqlite3
import importado_de_datos

def carga_datos_automatico():
    importado_de_datos.cargar_datos()   #Cargamos los datos por webscrapping
    importado_de_datos.cargar_idioma_continente()  #Añadimos idioma y continente
    
    conn = sqlite3.connect('canciones.db')
    print("'CONEXION ESTABLECIDA CORRECTAMENTE")

    cursor = conn.cursor()

    #Creamos la BBDD
    cursor.execute("""CREATE TABLE IF NOT EXISTS mejorescanciones(titulo TEXT, 
                autor TEXT,ano INT,semanas INT,pais TEXT,continente TEXT,
                idioma TEXT)""")

    #Introducimos los datos previamente extraidos
    cursor.executemany('INSERT INTO mejorescanciones values(?,?,?,?,?,?,?)',importado_de_datos.canciones)

    total = cursor.fetchall()
    for elemento in total:
        print(elemento)
    
    #Confirmamos datos, mostramos y cerramos conexión    
    conn.commit()
    cursor.execute('SELECT * FROM mejorescanciones')
    cursor.close()

