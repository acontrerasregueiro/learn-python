import sqlite3

#Conectamos a la BBDD
conn =sqlite3.connect('PelisFestival.db')
print("CONEXION ESTABLECIDA CORRECTAMENTE")

#Creamos el cursor
cursor = conn.cursor()

#Creamos la tabla
cursor.execute('''
               CREATE TABLE IF NOT EXISTS peliculas (nombre,año,oscars,nominaciones)
               ''')
valores = [('Titanic',1997, 11, 14),  
           ('Ben-Hur',1959, 11, 12), 
           ('El retorno del Rey',2003, 11, 11),
           ('Lo que el viento se llevó',1939, 10, 13),
           ('West Side Story',1961, 10, 11),
           ('El paciente inglés',1996, 9, 12),
           ('Gigi',1958, 9, 9),
           ('El último emperador',1987, 9, 9),
           ('De aquí a la eternidad',1953, 8, 13),
           ('La ley del silencio',1954, 8, 12)] 
#Insertamos registros a la vez con executemany
cursor.executemany('INSERT INTO peliculas values(?,?,?,?)', valores)

#Mostramos los datos para confirmar que estén introducidos
#cursor.execute("SELECT * FROM peliculas")
#peliculas = cursor.fetchall()
#print(peliculas[0])
#for pelicula in peliculas:
#    print(pelicula)

#Pelicula más galardonada
cursor.execute("SELECT * FROM peliculas ORDER BY oscars DESC")
peliculas = cursor.fetchall()
print('PELÍCULA MÁS GALARDONADA ',peliculas[0])

#Película más galardonada de los años 90
cursor.execute('''SELECT * FROM peliculas 
               WHERE año >= 1990 and año<2000
               ORDER BY oscars DESC''')
peliculas = cursor.fetchall()
print('PELÍCULA MÁS GALARDONADA DE LOS 90',peliculas[0])

#Película más galardonada anterior a los 90
cursor.execute('''SELECT * FROM peliculas 
               WHERE año < 1990 
               ORDER BY oscars DESC''')
peliculas = cursor.fetchall()
print('PELÍCULA MÁS GALARDONADA ANTERIOR A LOS 90',peliculas[0])

#Película con menos nominaciones

cursor.execute('''SELECT * FROM peliculas 
               ORDER BY nominaciones ASC''')
peliculas = cursor.fetchall()
print('PELÍCULA CON MENOS NOMINACIONES',peliculas[0])

#TOP 10 porcentaje de galardones sobre nominaciones
cursor.execute('''SELECT * FROM peliculas''')
peliculas = cursor.fetchall()
for registro in peliculas:
    porcentaje = registro[2]/registro[3]* 100
    porcentaje = round(porcentaje,0)
    if porcentaje >= 90:
        print('PELÍCULA EN EL TOP 10 DE OSCAR SOBRE NOMINACIONES',registro[0])
        
#Cerramos la conexión

conn.close()