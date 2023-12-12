#Ejercicios y métodos de diccionarios

jugadores = {
    #'clave' : 'valor',
    '1': 'Valdes',
    '2': 'Puyol',
    '3': 'Xavi',
    '4': 'Guardiola',
    '8': 'Iniesta',
    '10': 'Messi'
}

print(jugadores['1'])
print(jugadores)

#Si no se encuentra la clave se genera automáticamente

jugadores['11'] = 'Dembele'   # Como no está en el diccionario la key ['11'] la crea
print(jugadores)
#Se pueden modificar
jugadores['11'] = 'Ronaldo'
print(jugadores)

#Iterar diccionario y obtener las claves o valores

#Obtener las claves
for clave in jugadores: 
    print(clave)

#Obtener los valores asignados a esa clave
for clave in jugadores:
    print(jugadores[clave])

#Obtener todo
for clave in jugadores:
    print('el Número del jugador es {0} y el nombre es {1}'.format(clave,jugadores[clave]))
