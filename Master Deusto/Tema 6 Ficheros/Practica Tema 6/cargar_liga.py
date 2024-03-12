"""
    En este módulo realizaremos todas las operaciones de visionado y
    guardado de datos para el software de la liga
"""#Importamos main para volver al menu principal
from practica_tema_6 import main
import pandas as pd


def mostrar_datos(url):
   #leer un fichero en remoto con pandas
    info = pd.read_json(url)
    print(info['name'][0])
    
    for equipo in info['clubs']:
        print(equipo['name']) 
    
def cargar_liga(liga):
    global info

    while True:
        print(" Liga de ", liga)
        print('''  Mostrando datos de la liga de , ", liga "\n
        1.- Mostrar datos
        2.- Guardar a txt
        0.- Volver\n''')

        opcion = input("Elija la opción correspondiente: ")

        match opcion:
            case('1'): 
                mostrar_datos(liga)
            case('2'):
                guardar_datos(liga)
            case('0'):
                main()
            case(_):
                print("\nERROR, introduzca una opción válida\n")    

