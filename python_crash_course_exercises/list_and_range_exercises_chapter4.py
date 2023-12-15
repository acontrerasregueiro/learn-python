#4.3 to 4.9 Page 60

#4.3 Cuenta hasta 21
for valor in range(0,21):
    print(valor)

#4.4 Lista desde 0 hata 1000000
numeros = []
for valor in range(1,1000001):
    numeros.append(valor)
print(numeros)

#4.5 Utiliza min, max y sum con la lista anterior
print(min(numeros))
print(max(numeros))
print(sum(numeros))

#4.6 Numeros impares del 0 al 20
for valor in range(1,21,2):
    print(valor)

# 4.7 Multiplos de 3 desde el 3 al 30
print('Multiplos de 3 : ')
for multiplo in range(3,30):
    if multiplo % 3 == 0:
        print(multiplo)

# 4.8 Cubos
for valor in range(1,11):
    cubo = valor ** 3
    print(f' El cubo de {valor} es {cubo}')

# 4.9 Cubo mediante list comprehension
cubo = [valor ** 3 for valor in range(1, 11)]
print(cubo)

# 4.10 Slicing listas
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
nombres = ['adri', 'javi','raul', 'gonzalo']
bicicletas.extend(nombres)      #Ampliamos la lista
print(bicicletas)
print('Las primeras posiciones son : {}'.format(bicicletas[0:3]))
print('Las tres del medio son : {}'.format(bicicletas[3:6]))
# OJO ATENCION A LA SINTAXIS DE INDICES NEGATIVOS
print('Las tres ultimas posiciones son : {} '.format(bicicletas[-1:-4:-1]))

# 4.11
pizzas = ['Peperonni','Barbacoa','Carbonara','Calabresa']
pizzas.append('Hawaiana')
pizzas.insert(2,'Paisana')
friend_pizzas = pizzas[:]
friend_pizzas.append('Mediterranea')
print(pizzas)
print(friend_pizzas)
