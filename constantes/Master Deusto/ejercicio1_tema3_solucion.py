
#Inicializamos variable, el juego comienza con la ronda 1
Nombre_Jugador_1 = input('Introduce el nombre del primer jugador: ')
Nombre_Jugador_2 = input('Introduce el nombre del segundo jugador: ')
Nombre_Jugador_3 = input('Introduce el nombre del tercer jugador: ')
Nombre_Jugador_4 = input('Introduce el nombre del cuarto jugador: ')

#Utilizaremos un diccionario para almacenar nombre y puntuación de cada jugador, partimos de 121 y vamos restando
puntuacion = {}
#Inicializamos pares clave/valor
puntuacion[Nombre_Jugador_1] = 121
puntuacion[Nombre_Jugador_2] = 121
puntuacion[Nombre_Jugador_3] = 121
puntuacion[Nombre_Jugador_4] = 121

#Primera ronda
terminado = False
ronda = 1
Puntos_Jugador_1 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_1, ronda)))
Puntos_Jugador_2 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_2, ronda)))
Puntos_Jugador_3 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_3, ronda)))
Puntos_Jugador_4 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_4, ronda)))

puntuacion[Nombre_Jugador_1] = 121 - Puntos_Jugador_1
puntuacion[Nombre_Jugador_2] = 121 - Puntos_Jugador_2
puntuacion[Nombre_Jugador_3] = 121 - Puntos_Jugador_3
puntuacion[Nombre_Jugador_4] = 121 - Puntos_Jugador_4

#Chequeamos si ha finalizado el juego
if puntuacion[Nombre_Jugador_1] <= 0 or puntuacion[Nombre_Jugador_2] <= 0 or puntuacion[Nombre_Jugador_3] <= 0 or puntuacion[Nombre_Jugador_4] <= 0:
    terminado = True
    print('El juego ha finalizado en la ronda nº ' + str(ronda))

if  (terminado == False):
    print('Continuamos a la ronda 2')  
    ronda = 2
    Puntos_Jugador_1 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_1, ronda)))
    Puntos_Jugador_2 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_2, ronda)))
    Puntos_Jugador_3 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_3, ronda)))
    Puntos_Jugador_4 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_4, ronda)))

    #Actualizamos puntuaciones
    puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - Puntos_Jugador_1
    puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - Puntos_Jugador_2
    puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - Puntos_Jugador_3
    puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - Puntos_Jugador_4
    #Comprobamos puntuaciones
    if puntuacion[Nombre_Jugador_1] <= 0 or puntuacion[Nombre_Jugador_2] <= 0 or puntuacion[Nombre_Jugador_3] <= 0 or puntuacion[Nombre_Jugador_4] <= 0:
        print('El juego ha finalizado en la ronda nº ' + str(ronda))
        terminado = True
    else:
        print('Continuamos a la ronda 3')

if  (terminado == False):  
    ronda = 3
    Puntos_Jugador_1 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_1, ronda)))
    Puntos_Jugador_2 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_2, ronda)))
    Puntos_Jugador_3 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_3, ronda)))
    Puntos_Jugador_4 = int(input('Introduce la puntuación total de {0} en la ronda {1} :'.format(Nombre_Jugador_4, ronda)))

    #Actualizamos puntuaciones
    puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - Puntos_Jugador_1
    puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - Puntos_Jugador_2
    puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - Puntos_Jugador_3
    puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - Puntos_Jugador_4
    #Comprobamos puntuaciones
    if puntuacion[Nombre_Jugador_1] <= 0 or puntuacion[Nombre_Jugador_2] <= 0 or puntuacion[Nombre_Jugador_3] <= 0 or puntuacion[Nombre_Jugador_4] <= 0:
        print('El juego ha finalizado en la ronda nº ' + str(ronda))
    #Si nadia ha ganado se termina el juego (ronda 3)
    else:
        print("JUEGO FINALIZADO SIN GANADOR")
