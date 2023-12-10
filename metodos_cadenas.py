#Ejemplos de métodos para cadenas de texto

cadena = "hola mundo"
#         0123456789    Posiciones dentro de la cadena

print(len(cadena))                      #Obtenemos la longitud de la cadena

print(cadena.count('o'))                #Cuenta cuantas subcadenas hay en nuestra caedna
print(cadena.count('O'))                #No hay ninguna  subcaedna 'O' en nuestro ejemplo
print('Imprimiendo cadena.count desde la 0 a la 3 = ',cadena.count('o',0,3))

print(cadena.find('ola'))               #Encuentra subcadena en cadena y devuelve la posición
print(cadena.find('und'))
print(cadena.find('Hey'))               #Devuelve -1 si la subcadena no está en cadena

print(cadena.upper())                   #Pasa a mayúsculas
print(cadena.lower())                   #Pasa a minúsculas
print(cadena.title())                   #Pasa a mayúsculas la primera cadena de cada palabra
print(cadena.capitalize())              #Pasa a mayúsculas la primera letra de la cadena
                                        
#METODO REPLACE                                        
print(cadena.replace('aasdasdas','Hey'))#Al no encontrarlo devuelve la cadena original
print(cadena.replace('hola', 'hey'))  

cadena2 =  "hola hola hola mundo"
print(cadena2.replace('hola','hey'))
print(cadena2.replace('hola','hey',1))
print(cadena2.replace('hola','hey',2))

cadena_con_espacios = "    cade   na  con  es paci os  "
print(cadena_con_espacios.lstrip())     #Elimina espacios en blanco por la izquierda
print(cadena_con_espacios.rstrip())     #Por la derecha
print(cadena_con_espacios.strip())      #A la derecha y a la izquierda

print(cadena_con_espacios.split())      #Devuelve un array con las palabras que tenía el string
cadena_con_separador = "cade-na-con-guión-como-separador"
print(cadena_con_separador.split(sep='-'))  #Si le pasamos el parametro sep = 'valor', separa las palabras cuando encuentra el separador
print(cadena_con_separador.split('-'))


#Metodo Join
lista = '|'.join(cadena_con_espacios)
print(lista)

#Concatenar cadenas
nombre = "Adrian"
apellido = "Contreras"
print (nombre + ' ' + apellido)
#Multiplicación de cadenas
print(nombre *3)

#LOS STRINGS SON INMUTABLES POR LO TANTO EL SIGUIENTE EJEMPLO NO ES VALIDO Y GENERA ERROR
#nombre[1] = 'B'
#print(nombre)