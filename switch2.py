#Ejemplo de implementación switch con try except para un menu
#Deprecated. Ya disponemos de match que sería el switch en Python

def menu(opcion):

    if opcion == '1':
        print(f'Has elegido la opcion {opcion}')
    elif opcion == '2':
        print(f'Has elegido la opcion {opcion}')    
    elif opcion == '3':
        print('Saliendo...')
        quit()        

#menu()
while(True):
    print("""Selecciona una opción:
    1) Añadir
    2) Borrar
    3) Salir""")
    opcion = input()
    #try:
    menu(opcion)
    #except Exception as a:
    #  print("Seleccione una opción válida")#Gestionar más concretamente

