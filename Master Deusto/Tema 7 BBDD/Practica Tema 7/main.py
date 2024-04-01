#Menú principal de la aplicación

import bbdd #Módulo que realiza la carga automática de los datos en la BBDD 
import consultas #Moódulo en el que estan las consultas a la BBDD

def main():
    
    while(True):
        print("\n*** Welcome to best songs Database ***")
        print("""
            Si es la primera vez que abres la aplicacion
            comienza por realizar la introducción automática de datos\n  
            1.- Introducción automática de datos
            2.- Consultar el listado
            3.- Canción más antigua del listado
            4.- Artista con mayores semanas en el número 1
            5.- Pais con mas artistas del listado
            6.- Cuantas canciones hay de cada idioma
            7.- Continente con más apariciones en el listado
            8.- Canción con mayor porcentaje de tiempo en el número 1
            9.- Salir
            0.- Eliminar Tabla
            """)
        opcion = input("Que desea realizar :")

        match opcion:
            case('1'):
                bbdd.carga_datos_automatico()
            case('2'):
                consultas.consultar_listado()                
            case('3'):
                consultas.cancion_antigua()
            case('4'):
                consultas.artitas_mas_semanas()
            case('5'):
                consultas.pais_mas_artistas()
            case('6'):
                consultas.canciones_por_idioma()
            case('7'):
                consultas.continente_mas_listado()
            case('8'):
                consultas.cancion_mayor_tiempo()
            case('9'):
                print("Muchas gracias, esperamos verte de nuevo pronto")
                quit()
            case('0'):
                print("Eliminando BBDD..., requiere nueva introducción de datos")
                consultas.eliminar_tabla()
            case (_):
                print('Introduzca una opción válida')
            
if __name__ == "__main__":
    main()