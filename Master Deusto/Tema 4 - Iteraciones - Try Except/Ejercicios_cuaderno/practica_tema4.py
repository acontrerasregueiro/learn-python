
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

def main():
    """Función principal"""
    while True:
        print('''Bienvenido, que desea realizar:\n
        1.- Añadir colores
        2.- Mostrar listado de colores
        3.- Añadir usuario
        4.- Mostrar un listado de usuarios 
        5.- Eliminar usuario
        6.- Asignar colores
        7.- Salir\n''')

        opcion = input("Elija la opción correspondiente: ")

        match opcion:
            case('1'):
                anadir_colores()
            case('2'):
                print(sorted(colores))
            case('3'):
                print(colores)
            case('4'):
                print(colores)
            case('5'):
                print(colores)
            case('6'):
                print(colores)
            case('7'):
                quit()
            case(_):
                print("\nERROR, introduzca una opción válida\n")

if __name__ == "__main__":
    main()
