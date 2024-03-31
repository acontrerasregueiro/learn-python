import sqlite3
import importado_de_datos

importado_de_datos.cargar_datos()
importado_de_datos.cargar_idioma_continente()
conn = sqlite3.connect('canciones.db')
print("'CONEXION ESTABLECIDA CORRECTAMENTE")

cursor = conn.cursor()

#Creamos la BBDD

cursor.execute("""CREATE TABLE IF NOT EXISTS canciones(titulo TEXT, 
               autor TEXT,ano DATE,semanas INT,pais TEXT,continente TEXT,
               idioma TEXT)""")



cursor.executemany('INSERT INTO canciones values(?,?,?,?,?,?,?)',importado_de_datos.canciones)

cursor.execute('SELECT * FROM canciones WHERE semanas > 18')


total = cursor.fetchall()
for cancion in total:
    print(cancion)
cursor.close()
#cursor.execute("""INSERT INTO canciones""")
