#Ejemplo creacion tabla, introduccion y mostrado de datos SQLite

import sqlite3


#Creamos la conexión
conn = sqlite3.connect('grupos.db')
print('Conexion establecida correctamente')

#Creamos el cursor
cursor = conn.cursor()

#Creamos la tabla
cursor.execute('''
               CREATE TABLE IF NOT EXISTS rock (nombre,miembros)
               ''')

#Introducimos un valor en la Tabla
cursor.execute("INSERT INTO rock VALUES('KISS',4)")

#Introducimos varios registros a la vez
valores =[('Bon Jovi',5),('ACDC',4),('Muse',3),('The Cult',4)]
cursor.executemany('INSERT INTO rock values (?,?)',valores)

#Comprobamos que se hayan introducido los datos
cursor.execute('SELECT * FROM rock')
lineas = cursor.fetchall()
#Mostramos la información
for registro in lineas:
    print(registro)
    
conn.commit()
conn.close()
