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
    print(f'Ciudad : {clima[0]}')
    print(f'Temperatura : {clima[1]}')
    print(f'Clima : {clima[2]} \n')

    