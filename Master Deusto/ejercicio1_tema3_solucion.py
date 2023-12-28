
#Inicializamos variable, el juego comienza con la ronda 1
from re import A


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
#Jugador 1 tira los 3 dardos
puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_1, ronda)))
puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_1, ronda)))
puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_1, ronda)))
print(puntuacion[Nombre_Jugador_1])
#Jugador 2
puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_2, ronda)))
puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_2, ronda)))
puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_2, ronda)))
print(puntuacion[Nombre_Jugador_2])
#Jugador 3
puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_3, ronda)))
puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_3, ronda)))
puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_3, ronda)))
print(puntuacion[Nombre_Jugador_3])
#Jugador 4
puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_4, ronda)))
puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_4, ronda)))
puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
    'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_4, ronda)))
print(puntuacion[Nombre_Jugador_4])

#Chequeamos si ha finalizado el juego
if puntuacion[Nombre_Jugador_1] <= 0 or puntuacion[Nombre_Jugador_2] <= 0 or puntuacion[Nombre_Jugador_3] <= 0 or puntuacion[Nombre_Jugador_4] <= 0:
    terminado = True
    print('El juego ha finalizado en la ronda nº ' + str(ronda))

elif  (terminado == False):
    print('Continuamos a la ronda 2')  
    ronda = 2
    #Jugador 1 tira los 3 dardos
    puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_1, ronda)))
    puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_1, ronda)))
    puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_1, ronda)))
    print(puntuacion[Nombre_Jugador_1])
    #Jugador 2
    puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_2, ronda)))
    puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_2, ronda)))
    puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_2, ronda)))
    print(puntuacion[Nombre_Jugador_2])
    #Jugador 3
    puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_3, ronda)))
    puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_3, ronda)))
    puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_3, ronda)))
    print(puntuacion[Nombre_Jugador_3])
    #Jugador 4
    puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_4, ronda)))
    puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_4, ronda)))
    puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
        'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_4, ronda)))
    print(puntuacion[Nombre_Jugador_4])
    
    #Comprobamos puntuaciones
    if puntuacion[Nombre_Jugador_1] <= 0 or puntuacion[Nombre_Jugador_2] <= 0 or puntuacion[Nombre_Jugador_3] <= 0 or puntuacion[Nombre_Jugador_4] <= 0:
        print('El juego ha finalizado en la ronda nº ' + str(ronda))
        terminado = True
    else:
        print('Continuamos a la ronda 3')
        if  (terminado == False):  
            ronda = 3
        #Jugador 1 tira los 3 dardos
        puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_1, ronda)))
        puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_1, ronda)))
        puntuacion[Nombre_Jugador_1] = puntuacion[Nombre_Jugador_1] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_1, ronda)))
        print(puntuacion[Nombre_Jugador_1])
        #Jugador 2
        puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_2, ronda)))
        puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_2, ronda)))
        puntuacion[Nombre_Jugador_2] = puntuacion[Nombre_Jugador_2] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_2, ronda)))
        print(puntuacion[Nombre_Jugador_2])
        #Jugador 3
        puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_3, ronda)))
        puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_3, ronda)))
        puntuacion[Nombre_Jugador_3] = puntuacion[Nombre_Jugador_3] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_3, ronda)))
        print(puntuacion[Nombre_Jugador_3])
        #Jugador 4
        puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 1 :'.format(Nombre_Jugador_4, ronda)))
        puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 2 :'.format(Nombre_Jugador_4, ronda)))
        puntuacion[Nombre_Jugador_4] = puntuacion[Nombre_Jugador_4] - int(input(
            'Introduce la puntuación total de {0} en la ronda {1} dardo 3 :'.format(Nombre_Jugador_4, ronda)))
        print(puntuacion[Nombre_Jugador_4])
            
        #Comprobamos puntuaciones
        if puntuacion[Nombre_Jugador_1] <= 0 or puntuacion[Nombre_Jugador_2] <= 0 or puntuacion[Nombre_Jugador_3] <= 0 or puntuacion[Nombre_Jugador_4] <= 0:
            print('El juego ha finalizado en la ronda nº ' + str(ronda))
        #Si nadia ha ganado se termina el juego (ronda 3)
        else:
            print("JUEGO FINALIZADO SIN GANADOR")
