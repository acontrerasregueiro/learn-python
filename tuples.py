#EJEMPLOS DE TUPLAS
#Son inmutables lo que significa que 
#           NO SE PUEDE
#MODIFICAR ELEMENTOS INDIVIDUALES

tupla = (1,2,tuple(),'hi',34,[1,5,'perico'],True)
print(tupla[-1])
print(tupla[0:3])
#REVISAR ESTO, EJEMPLO DE INMUTABILIDAD
#No se puede modificar los elementos individuales
#Pero sí la tupla en su totalidad
tupla =(3,4,5)
print(tupla)

#Continuamos con ejemplos

ciudades_clima = (('Buenos Aires',25,'Soleado'),  ('Barcelona',20,'Nublado'),('Paris',15,'Lluvioso'))
print(ciudades_clima[0])            #Primer elemento de la tupla
print(ciudades_clima[0][1])         #Primer elemento del primer elemento de la tupla anidada
print(ciudades_clima[0][0][1])      #Segundo carácter del string 'Buenos Aires' del primer elemento de la tupla anidada (Output letra u de Buenos aires)
print(ciudades_clima[0][2][0])      #Primer carácter del string de la primera tupla contenida en ciudades_clima en la posición dos 'Soleado'

for clima in ciudades_clima:
    print(f'Ciudad : {clima[0]}')       #La primera posición de la tupla anidada corresponde a la ciudad
    print(f'Temperatura : {clima[1]}')  #La segunda a la temperatura
    print(f'Clima : {clima[2]} \n')     #La tercera es el tipo de clima


#Asignacion múltiple a variables con tuplas
a,b,c = ('adri','javi','miriam')
print(a)
print(b)
print(c)

#Métodos Count() e Index()
tupla =(1,2,3,4,1,5,6,7,1,9)
print(tupla.count(1))
print(tupla.count(4))

#Método index(valor,[inicio,fin]), indica EL INDICE DE LA PRIMERA COINCIDENCIA

print(tupla.index(4))   #En nuestra tupla 4 está en la posición tupla[3]
print(tupla.index(1))   #Muestra el indice del primer 1 encontrado en la tupla tupl[0]
print(tupla.index(1,3)) #Buscar buscamos a partir de la 3º posición, el indice del siguiente en la tupla es 4
print(tupla.index(1,5,9)) #Podemos poner rango de posiciones donde buscar

print(tupla.index(19))  #SI NO LO ENCUENTRA NOS DEVUELVE VALUEERROR: X NOT IN TUPLE