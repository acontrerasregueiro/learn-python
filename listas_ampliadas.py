
lista = ['javier', 3, 129,['raul',1,10e2]]
print(lista)
print(lista[2])
print(lista[3])

print(lista[3][0]) #Para acceder a una lista dentro de una lista
print(lista[0][2]) #Tener en cuenta que los string se acceden como una lista
print(lista[3][0][-1]) #Para acceder a una lista dentro de una lista, y leer el ultimo elemento del string en nuestro ejemplo

nueva_lista = [3,'abc',5e1]
print(nueva_lista)
lista.extend(nueva_lista) #A una lista se le puede extender otra lista, pero la agrega elemento a elemento.
#A la vieja lista se le añade elemento a elemento la nueva_lista con extend
print(lista)
lista.extend(range(0,3)) # Con extend se pueden anadir elementos que sean iterables
print(lista)
'''Por lo que el siguiente codigo genera error 
lista.extend(4)  YA QUE UN INT NO ES ITERABLE
print(lista)
'''

#metodo index()
indice_encontrado = lista.index('abc')
print(indice_encontrado)
#también se puede pasar un inicio y fin para buscar el indice
indice_encontrado = lista.index('abc',0,len(lista))
print(indice_encontrado)
indice_encontrado = lista.index('abc',3,6)
print(indice_encontrado)

lista2 = lista.copy()
print(lista2)
lista.clear()   #Elimina todos los elementos de una lista
print(lista)
