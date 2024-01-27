#Ejemplo de implementación de una función switch en python
#Deprecated, en python 3.10 ya dispone de "match" lo mismo que un "switch"

def menu():

    while True:        
        print("1.- Primera opcion")
        print("2.- Segunda opcion")
        print("3.- Salir")
        opcion = input("Elige una opción del menú o 3 para salir : ")
        print('OPCION = ', opcion)
        if opcion == '1':
            print("Has elegido la opcion 1")
        elif opcion == '2':
            print("Has elegido la opcion 2")
        elif opcion == '3':
            print("SALIENDO...")
            break 
        
menu()
        
