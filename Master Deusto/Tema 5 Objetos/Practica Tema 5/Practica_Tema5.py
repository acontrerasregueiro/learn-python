

import classes as clase
import anadir_persona as nueva_persona
import anadir_cancion as nueva_cancion

cancion = clase.Cancion("Hola", "ACDC" , "Rock")
persona = clase.Persona("34898103L","Javier","Lopez" , "Lopez", "Madrid" ,
                       "España")


#favorita = clase.Favoritas(persona,cancion)
#print(favorita.dni)
#print(favorita.titulo)
#favorita.mostrar_favorita()

def ver_favoritas():
    pass

def cargar_datos():
    pass

def main():
    """Funcion principal"""
    while True:
        print("""\nSelecciona una opción:
            1) Añadir persona
            2) Añadir cancion
            3) Ver favoritas
            4) Cargar datos por defecto
            5) Salir
            """)
        opcion = input('Elija una opción del menú: ')
        match opcion:
            case "1": 
                nueva_persona.anadir_persona()
                nueva_cancion.anadir_cancion()
            #case "2": anadir_cancion()
            case "3": ver_favoritas()
            case "4": cargar_datos()    #Carga datos para testear
            case "5": quit()
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()