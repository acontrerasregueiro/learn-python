'''
Necesitamos una Agenda para almacenar los nombres y los teléfonos de las personas.
Necesitamos un menú infinito para añadir, borrar y visualizar todo.
Se puede borrar por nombre o por teléfono, previa elección.

Debe utilizarse un diccionario.
No podrá haber usuarios repetidos.
Añade un control con try-except para mostrar un error en pantalla si seleccionan una opción no
existente.
En el apartado de visualizar, debe mostrarse al final la cantidad de contactos.

'''

agenda = {}

def buscar_contacto(nombre,telefono):
    """Función que busca un contacto en la agenda"""
    
def borrar_contacto():
    """Función para eliminar un contacto de la agenda"""
    nombre= input("Introduzca el nombre del contacto a borrar: ")
    if nombre.isalpha():
        if nombre in agenda:
            agenda.pop(nombre)
        else:
            print("\nNo se encuentra en la agenda")
    else:
        print("Valor no válido")
    #main()

def anadir_contacto():
    """Funcion para añadir contactos a la agenda"""
    global agenda
    print("Introduzca el nuevo contacto")
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono del contacto: ")
    if nombre not in agenda:
        if nombre.isalpha() and telefono.isdigit():
            agenda[nombre] = telefono
        else:
            print("\n--- Error introduzca datos válidos ---\n")
    else:
        print("\n--- Contacto duplicado ---\n")

def ver_agenda():
    """Función para visualizar la agenda"""
    #global agenda
    print('\n')
    for clave,valor in agenda.items():
        print(f'Nombre {clave} : Teléfono: {valor}')
    print(f'Total de contactos: {len(agenda)}\n')

def main():
    """Funcion principal"""
    while True:
        print("""\nSelecciona una opción:
            1) Añadir contacto
            2) Borrar contacto
            3) Ver la agenda
            4) Salir
            """)
        opcion = input('Elija una opción del menú: ')
        match opcion:
            case "1": anadir_contacto()
            case "2": borrar_contacto()
            case "3": ver_agenda()
            case "4": quit()
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
