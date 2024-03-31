import sqlite3

conn = sqlite3.connect('canciones.db')
print("'CONEXION ESTABLECIDA CORRECTAMENTE")

cursor = conn.cursor()

#Creamos la BBDD

cursor.execute("""CREATE TABLE IF NOT EXISTS canciones(titulo TEXT, 
               autor TEXT,ano DATE,semanas INT,pais TEXT,idioma TEXT,
               continente TEXT)""")

cursor.execute("""INSERT INTO canciones""")
