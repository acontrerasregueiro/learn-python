#Ejercicios y métodos de diccionarios
#Un Dicionario en la parte 'valor' puede contener cualquier otro tipo de datos,
#Es decir puede tener otro diccionario, una lista, entero, cadena,etc...


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

 
#Métodos

jugadores.clear()  #Elimina EL CONTENIDO del diccionario
print(jugadores)

'''
del jugadores      #Con del eliminamos el diccionario       
print(jugadores)
'''

jugadores = {
    #'clave' : 'valor',
    '1': 'Valdes',
    '2': 'Puyol',
    '3': 'Xavi',
    '4': 'Guardiola',
    '8': 'Iniesta',
    '10': 'Messi' 
}
print(jugadores)
#Método get devuelve el valor cuya clave coincide con el parámetro pasado
print(jugadores.get('1'))
#SI SE ESPECIFICA EL SEGUNDO PARAMETRO Y NO ENCUENTRA UN VALOR ASOCIADO A ESA CLAVE NOS LO DEVUELVE
print(jugadores.get('50','NOT FOUND'))  

#Método items()
print(jugadores.items())
#Si lo pasamos a una lista con list() podemos iterarlos
lista= list(jugadores.items())
print(lista[2])
#Y acceder a sus elementos por separados
print(lista[2][0])
print(lista[2][1]) 
print(type(lista))

#Metodo pop() y popitem()
#Elimina un elemento aleatorio, si le pasamos argumento elimina el elemento de esa posicion
jugadores.popitem()
print(jugadores)
print(jugadores.values())
#print(jugadores.keys())

claves= list(jugadores.keys())
print(claves[0])
# Método update si existe la clave actualiza ese valor,
# Si no existe la crea 

jugadores.update({  
    #'clave' : 'valor',
    '1': 'Valdes',
    '29': 'Puyol',
    '39': 'Xavi',
    '49': 'Guardiola',
    '89': 'Iniesta',
    '109': 'Messi',
    '9': 'Busquets' 
})
print(jugadores)

#Método pop() elimina el par clave:valor especificado en el argumento

jugadores.pop('1')
print(jugadores)

dic = dict(
Nombre="Josep",
Tel=688777555,
Material=["PC", "Teclado", "WebCam"]
)
print("fromkeys")
#fromkeys() - Esta función nos ayuda a generar un diccionario a partir de las clave
variables = ('Nombre', 'Tel', 'Material')
dic = dict.fromkeys(variables)
print(dic)
dic = dict.fromkeys(variables, "Rellenar")
print(dic)
print("\n")
