#Ejercicios de práctica "Python crash course"
#Chapter 3 Page 41 from 3.4 to 3.7

#3.4 Práctica listas pag 41-42
#Invita a 3 amigos acenar utilizando listas

amigos = [ 'juan', 'javier','federico']
print('hola, voy a invitar a mis amigos {0},{1} y {2} a cenar'.format(amigos[0].capitalize(), amigos[1].capitalize(), amigos[2].capitalize()))

#3.5 Elimina a un amigo e invita a otro 

print('Al final {0} no puede venir'.format(amigos[0].capitalize()))
amigos.remove('juan') #Eliminamos a juan de la lista.
amigos.append('victor')
print('Al final vamos a asisitir a la cena {0},{1},{2}'.format(amigos[0].capitalize(),amigos[1].capitalize(),amigos[2].capitalize()))

#3.6 Utiliza los métodos insert para añadir al inicio y en el medio de la lista y append para añadir al final

amigos.insert(0,'pedro')
print(amigos)
amigos.insert(round(len(amigos)/2), 'raul')
print(amigos)
amigos.append('leo')
print(amigos)

#3.7 Utiliza pop() para eliminar hasta que solo queden 2 comensales. Enviales un mensaje 
#Cuando queden dos comensales, eliminalos de la lista y haz un print para verificar que está vacia

amigo1_no_asiste = amigos.pop(2)
print('lo siento ' + amigo1_no_asiste + ' no puedes asistir')
amigo2_no_asiste = amigos.pop(-1)
print('lo siento ' + amigo2_no_asiste + ' no puedes asistir')
amigo3_no_asiste = amigos.pop(0)
print('lo siento ' + amigo3_no_asiste + ' no puedes asistir')
amigo4_no_asiste = amigos.pop(0)
print('lo siento ' + amigo4_no_asiste + ' no puedes asistir')

print('Al final los únicos que vamos a la cena somos {0},{1} y yo'.format(amigos[0].capitalize(), amigos[1].capitalize()))

del amigos[-1]  #Eliminamos al último elemento por el final
print(amigos)
del amigos[-1]  #Eliminamos el último elemento y comprobamos que la lista esta vacia
print(amigos)

#3.8 Pag 45

lugares = ['pontevedra','vigo','la coruñá','lugo','orense']
print(lugares)
print(sorted(lugares))          #Imprime la lista alfabeticamente utilizando sorted()
print(lugares)                  #Comprobamos que la lista inicial no ha sido modificada
print(sorted(sorted(lugares)))  #Imprime la lista alfabeticamente de la z a la a, sin modificar la lista inicial
print(lugares)
lugares.reverse()               #Ordena la lista en el sentido contrario
print(lugares)
lugares.reverse()               #Devuelve la lista a su orden original
print(lugares)
lugares.sort()                  #Ordena la lista alfabéticamente
print(lugares)             
lugares.sort(reverse=True)      #Ordena la lista alfabéticamente en el orden contrario de la z a la a
print(lugares)         

#3.9 Muestra la longitud de una lista
print(len(lugares))

#3.10 Utiliza todos los métodos y funciones vistos en el capitulo
#Realizado todo en ejercicios anteriores.