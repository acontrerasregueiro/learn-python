nombre = input('Introduzca su nombre :')
edad = input('Introduzca su edad :')

print('Bienvenido' , nombre + ' tienes', edad , 'años')
#EJEMPLOS F STRINGS

print(f'Bienvenido {nombre} tienes {edad} años')
print('Bienvenido {nombre} tienes {edad} años'.format(nombre  = 'adrian', edad=24))  #Sobreescribe el valor pero no lo almacena en nombre y edad
print('Bienvenido {0} tienes {1} años'.format(nombre,edad))  #Sobreescribe el valor pero no lo guarda
