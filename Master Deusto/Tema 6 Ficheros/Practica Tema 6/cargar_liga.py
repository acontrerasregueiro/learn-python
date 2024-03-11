"""
    En este módulo realizaremos todas las operaciones de visionado y
    guardado de datos para el software de la liga
"""#Importamos main para volver al menu principal
from practica_tema_6 import main 
from settings import (espana,alemania,italia,austria,inglaterra)

def cargar_liga(liga):
    while True:
        print(" Liga de ", liga)
        print('''  Mostrando datos de la liga de , ", liga "\n
        1.- Mostrar datos
        2.- Guardar a txt
        0.- Volver\n''')

        opcion = input("Elija la opción correspondiente: ")

        match opcion:
            case('1'):
                mostrar_datos("España")
            case('2'):
                guardar_datos("Alemania")
            case('0'):
                main()
            case(_):
                print("\nERROR, introduzca una opción válida\n")    

