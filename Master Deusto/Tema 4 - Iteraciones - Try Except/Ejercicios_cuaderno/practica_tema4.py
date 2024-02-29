import random
colores = ['amarillo', 'azul', 'verde', 'rojo']
usuarios =[{'Nombre':'Josep'}, {'Nombre':'Claudio'},
           {'Nombre':'Isabel'}, {'Nombre':'Sheila'}]

def buscar_en_array(valor,array):
    '''Esta funcion le pasamos un valor y un array 
    y nos devuelve True si valor se encuentra en array
    o false en caso contrario'''
    if valor in array:
        return True
    else:
        return False

def anadir_colores():
    """Función para añadir colores"""
    while True:
        color = input("Introduzca un color: ")
        if color.isalpha():
            if buscar_en_array(color.lower(),colores):
                print("El color ya se encuentra en la lista")
            else:
                colores.append(color.lower())
                break
        else:
            print("Introduzca un color válido")
            continue
    print("Listado de colores actual: ", colores)

def usuarios_ordenados():
    """Muestra por pantalla los usuarios alfabeticamente por la clave Nombre """
    listado_nombres = []
    for user in usuarios:
        listado_nombres.append(user['Nombre'])
    print(sorted(listado_nombres))


def anadir_usuarios():
    """Función para añadir usuarios a la agenda"""
    listado_nombres = []
    for user in usuarios:
        listado_nombres.append(user['Nombre'])
    while True:
        usuario = input("Introduzca un nombre de usuario: ")
        if usuario.isalpha():
            if usuario.title() in listado_nombres:
                print("El usuario ya existe")
            else:
                usuario_a_anadir = {'Nombre': usuario.title()}                    
                usuarios.append(usuario_a_anadir)
                print(usuarios)
                break
        else:
            print("Introduzca un usuario válido")
            continue
    #Necesitamos un color por usuario, comprobamos y anadimos si necesario    
    if (len(usuarios)) > len(colores):
        anadir_colores()

def asignar_colores():
    """Funcion para asignar un color a cada usuario"""
    global usuarios
    colores_sin_asignar = colores.copy()
    print(colores_sin_asignar)
    for i in range(len(usuarios)):
        indice = random.randint(0,len(colores_sin_asignar)-1)
        color_a_anadir = colores_sin_asignar[indice]
        usuarios[i]['Color'] = color_a_anadir
        print("Asignado el color {} al usuario {}".format(colores_sin_asignar[indice],usuarios[i]['Nombre']))
        del colores_sin_asignar[indice]

def eliminar_usuario():
    """Funcion para eliminar un usuario de la lista dado el índice"""
    while(True):   
        try:
            x = int(input("Introduce el valor de x : "))
            print("Introduce un valor entre 0 y ", len(usuarios))
            if (x <= len(usuarios) -1):
                del usuarios[x]
                break
            else:
                print("Índice no válido")
                continue
        except ValueError:
                print("Valor incorrecto")
        
def main():
    """Función principal"""
    while True:
        print('''Bienvenido, que desea realizar:\n
        1.- Añadir colores
        2.- Mostrar listado de colores
        3.- Ordenar colores alfabéticamente
        4.- Añadir usuario
        5.- Mostrar un listado de nombres usuarios alfabéticamente
        6.- Mostrar un listado de de todos los usuarios         
        7.- Asignar colores aleatoriamente
        8.- Eliminar usuario dado el índice
        9.- Salir\n''')

        opcion = input("Elija la opción correspondiente: ")

        match opcion:
            case('1'):
                anadir_colores()
            case('2'):
                print(colores)
            case('3'):
                colores.sort()
                print(colores)
            case('4'):
                anadir_usuarios()
            case('5'):
                usuarios_ordenados()
            case('6'):
                print(usuarios)
            case('7'):
                asignar_colores()
            case('8'):
                eliminar_usuario()
            case('9'):
                print("Cerrando aplicación, hasta otra...")
                quit()
            case(_):
                print("\nERROR, introduzca una opción válida\n")

if __name__ == "__main__":
    main()
