import clase_persona as clase

cancion = clase.Cancion("Hola", "ACDC" , "Rock")
persona = clase.Persona("34898103L","Javier","Lopez" , "Lopez", "Madrid" ,
                       "España", cancion)


#favorita = clase.Favoritas("34898103L","Javier","Lopez" , "Lopez", "Madrid" ,
#                       "España","Hola", "ACDC" , "Rock")
#print(cancion.titulo)
""""""
def anadir_persona():
    pass

def anadir_cancion():
    pass

def ver_favoritas():
    pass

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
            case "1": anadir_persona()
            case "2": anadir_cancion()
            case "3": ver_favoritas()
            case "4": quit()
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()