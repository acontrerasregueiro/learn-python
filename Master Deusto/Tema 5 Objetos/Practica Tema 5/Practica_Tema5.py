
import datos_defecto as cargar
import classes as clase
import anadir_persona as nueva_persona
import anadir_cancion as nueva_cancion

def main():
    """Menú principal"""
    while True:
        print("""\nSelecciona una opción:
            1) Añadir persona
            2) Cargar y mostrar datos por defecto
            3) Salir
            """)
        opcion = input('Elija una opción del menú: ')
        match opcion:
            case "1":
                persona = nueva_persona.anadir_persona()
                cancion = nueva_cancion.anadir_cancion()
                favorita = clase.Favoritas(persona,cancion)
                favorita.mostrar_favorita()
            case "2": cargar.cargar()    #Carga datos para testear
            case "3": quit()
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()