#Ejemplos range() function
#Range(inicio,fin -1,incremento)


for value in range(1,6):
    print(value)

numbers = range(8)
print(numbers)          #Output "range(0,8)"
print(list(numbers))    #Output [0, 1, 2, 3, 4, 5, 6, 7]

pares = list(range(2,11,2)) 
print(pares)

#Ejemplo 
cuadrados = []
for valor in range(1,11):
    cuadrados.append(valor ** 2)
print(cuadrados)
del cuadrados
