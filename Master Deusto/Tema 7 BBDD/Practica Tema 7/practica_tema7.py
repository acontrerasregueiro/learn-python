#En este módulo realizamos las operaciones de insercion de datos
import bbdd  

#Menú principal de la aplicación

def main():
    
    while(True):
        print("\n*** Welcome to best songs Database ***")
        print("""
            1.- Introducción automática de datos
            2.- Consultar el listado
            3.- Canción más antigua del listado
            4.- Artista con mayores semanas en el número 1
            5.- Pais con mas artistas del listado
            6.- Cuantas canciones hay de cada idioma
            7.- Continente con más apariciones en el listado
            8.- Canción con mayor porcentaje de tiempo en el número 1
            9.- Salir
            """)
        opcion = input("Que desea realizar :")

        match opcion:
            case('1'):
                pass
            case('2'):
                pass
            case('3'):
                pass
            case('4'):
                pass
            case('5'):
                pass
            case('6'):
                pass
            case('7'):
                pass
            case('8'):
                pass
            case('9'):
                print("Muchas gracias, esperamos verte de nuevo pronto")
                quit()
            case (_):
                print('Introduzca una opción válida')
            

if __name__ == "__main__":
    main()