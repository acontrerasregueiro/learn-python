
colores = ['amarillo', 'azul', 'verde', 'rojo']
usuarios =[{'Nombre':'Josep'}, {'Nombre':'Claudio'},
           {'Nombre':'Isabel'}, {'Nombre':'Sheila'}]

def test():
    usuarios[0]['telefono'] = 1
    print(usuarios)

def buscar_en_array(valor,array):
    '''Esta funcion le pasamos un valor y un array 
    y nos devuelve True si valor se encuentra en array
    o false en caso contrario'''
    if valor in array:
        return True
    else:
        return False

def anadir_usuario():
    pass

def asignar_colores():
    pass

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
    """ Muestra por pantalla los usuarios ordenado por la clave 'Nombre'"""
    ordenados = sorted(usuarios,key=lambda x:x['Nombre'])
    print(ordenados)

def anadir_usuarios():
    """Función para añadir usuarios a la agenda"""
    listado_nombres = []
    for user in usuarios:
        listado_nombres.append(user['Nombre'])
    while True:
        usuario = input("Introduzca un nombre de usuario: ")
        if usuario.isalpha():
            if usuario in listado_nombres:
                print("El usuario ya existe")
            else:
                usuario_a_anadir = {'Nombre': usuario}                    
                usuarios.append(usuario_a_anadir)
                print(usuarios)
                break
        else:
            print("Introduzca un usuario válido")
            continue
def main():
    """Función principal"""
    while True:
        print('''Bienvenido, que desea realizar:\n
        1.- Añadir colores
        2.- Mostrar listado de colores
        3.- Ordenar colores alfabéticamente
        4.- Añadir usuario
        5.- Mostrar un listado de usuarios alfabéticamente 
        6.- Eliminar usuario
        7.- Asignar colores
        8.- Salir\n''')

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
                print(colores)
            case('8'):
                quit()
            case(_):
                print("\nERROR, introduzca una opción válida\n")

if __name__ == "__main__":
    main()
