#Ejemplos de listas y métodos

bicicletas = ['trek', 'cannondale', 'redline', 'specialized']

print(bicicletas)
print(bicicletas[0].upper())
message = f"mi primera bicicleta fue una {bicicletas[1].title()}"
print(message)


#AÑADIR DATOS A LISTA
bicicletas.append("mmr")    #Añade en la ultima posición
print(bicicletas)

bicicletas.insert(2,'motoretta')    #Con insert podemos  añadir el valor en una determinada posición
print(bicicletas)

#ELIMINAR DATOS DE LA LISTA
del bicicletas[4]           #Utilizando del si conocemos el indice el contenido no será utilizable nunca más
print(bicicletas)           

bicicletas.pop()            #Utilizando pop(indice) nos permite guardar el elemento en una variable para trabajar con el            
print(bicicletas)           #Si no se pasa el índice elimina la última posición
bicicleta_eliminada = bicicletas.pop(1)  #Si le pasamos el indice por parámetro elimina esa posición
print(bicicleta_eliminada)

bicicletas.remove('redline')    #Tambien podemos eliminar si conocemos el valor con el metodo remove(valor)
print(bicicletas)               #CUIDADO, SOLO ELIMINA LA PRIMERA COINCIDENCIA, SI SE REPITE RECORRER EN BUCLE PARA ELIMINAR TODAS.

#MODIFICAR ELEMENTOS DE UNA LISTA
bicicletas[0] = 'bh'
print(bicicletas)

#ORDENAR LISTAS
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)
bicicletas.sort()                       #Ordena alfabeticamente
print(bicicletas)
bicicletas.sort(reverse=True)         #Ordena alfabeticamente pero de la z a la a. 
print(bicicletas)
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
bicicletas.reverse()                    # Modifica la lista para mostrarla en el orden contrario
print(bicicletas)

#Si no queremos modificar la lista original debemos utilizar el metodo sorted(lista)
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(sorted(bicicletas))
