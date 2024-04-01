import sqlite3
import time

def consultar_listado():
    #Muestra todo el listado
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()    
    cursor.execute('SELECT * FROM mejorescanciones')
    total = cursor.fetchall()
    for elemento in total:
        print(elemento)
    conn.close()

def cancion_antigua():
    #Muestra la canción  más antigua
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()    
    cursor.execute('''SELECT * FROM mejorescanciones 
               ORDER BY ano ASC''')
    total = cursor.fetchall()
    
    print(f'Titulo : \t',total[0][0])
    print(f'Autor : \t',total[0][1])
    print(f'Año : \t\t',total[0][2])
    print(f'Semanas : \t',total[0][3])
    time.sleep(4)
    conn.close()

def artitas_mas_semanas():
    #Muestra el artista con más semanas en el número 1
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()    
    cursor.execute('''SELECT autor FROM mejorescanciones 
               ORDER BY semanas DESC''')
    total = cursor.fetchall()
    print(f'\nAutor : ',total[0][0])

    time.sleep(4)
    conn.close()
    
def pais_mas_artistas():
    #Devuelve el artias con mayores semanas como Nº1
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()    
    cursor.execute('''SELECT pais,
                   COUNT(*) as veces 
                   FROM mejorescanciones 
                   GROUP BY pais
                   ORDER BY veces DESC''')

    total = cursor.fetchone()

    print("El pais con más artistas como Nº1 es : ", total[0] + 
          " con ", str(total[1]) + " artistas")

    time.sleep(4)
    conn.close()

def canciones_por_idioma():
    #Nos muestra el total de canciones por idioma
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()    
    cursor.execute('''SELECT idioma,
                   COUNT(*) as veces 
                   FROM mejorescanciones 
                   GROUP BY idioma
                   ORDER BY veces DESC''')

    total = cursor.fetchall()
    print("Listado de canciones por cada idioma : \n")
    for elemento in total:
        #print("Idioma : ", total[0] + " con ", str(total[1]) + " canciones")
        print(elemento[0] + ': '  + str(elemento[1]))
    time.sleep(4)
    conn.close()

def continente_mas_listado():
    #Nos muestra el cotinente más listado
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()    
    cursor.execute('''SELECT continente,
                   COUNT(*) as veces 
                   FROM mejorescanciones 
                   GROUP BY continente
                   ORDER BY veces DESC''')

    total = cursor.fetchone()
    print("El continente más veces listado es: ", total[0] + 
        " con ", str(total[1]) + " veces")

    time.sleep(4)
    conn.close()

def cancion_mayor_tiempo():
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()    
    cursor.execute('''SELECT titulo,semanas
                   FROM mejorescanciones 
                   ORDER BY semanas DESC''')
    
    total = cursor.fetchone()
    #Calculamos el porcentaje y redondeamos a dos dígitos
    porcentaje = round(((total[1] * 100) / 52),2)  
            
    print("La cancion con mayor porcentaje de semanas en el numero 1 es :\n")
    print(f'{total[0]} con un {porcentaje}% en el año')

    time.sleep(4)
    conn.close()  

def eliminar_tabla():
    #Función para eliminar la bbdd donde almacenamos los datos
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS mejorescanciones')
    conn.commit()
    conn.close()