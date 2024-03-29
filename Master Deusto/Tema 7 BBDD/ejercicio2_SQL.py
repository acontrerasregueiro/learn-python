import sqlite3

conn =sqlite3.connect('mascotas.db')
print("'CONEXION ESTABLECIDA CORRECTAMENTE")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS mascotas(nombre TEXT, propietario TEXT,
               animal TEXT,chip BIT, edad INT, piso BIT, operado BIT)
               ''')
datos = [('Manolo','Patricia','Gato',1,10,1,0),('Uka','Patricia','Gato',1,15,1,1),
                   ('Cá','Raul','Periquito',0,2,1,0),('Leviathan','Patxi','Hamster',0,2,1,0),
                   ('Samantha','Patricia','Tortuga',0,12,0,0)]
                   
cursor.executemany('INSERT INTO mascotas values(?,?,?,?,?,?,?)',datos)

cursor.execute('SELECT * FROM mascotas')
mascotas = cursor.fetchall()
for mascota in mascotas:
    print(mascota)

conn.close()