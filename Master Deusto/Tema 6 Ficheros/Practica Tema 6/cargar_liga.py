"""
    En este módulo realizaremos todas las operaciones de visionado y
    guardado de datos para el software de la liga
"""
import json
from practica_tema_6 import main  #Importamos main para volver al menu principal
import pandas as pd

def mostrar_datos(url):
   #Recibe por parametro la url del equipo del que queremos mostrar datos
   
    data = pd.read_json(url)
    print("*****************************")
    print(data['name'][0])
    print("Numero de equipos : ", len(data['clubs']))
    print("*****************************")
    
    for equipo in data['clubs']:

        if equipo['code'] != None:
            print(f" {equipo['name']} \t  {equipo['code']} ")
        else:
            print(f" {equipo['name']}")

def guardar_datos(url,pais): 
    #Funcion para guardar en un fichero la información de la url
    data = pd.read_json(url)
    nombre_fichero = pais + ".txt"
      
    with open(nombre_fichero,"w",encoding="utf-8") as fp:
        fp.writelines(data['name'][0]+ '\n')
        for equipo in data['clubs']:
            if equipo['code'] != None:
                fp.writelines(equipo['name'] + ',' + equipo['code']+'\n')
            else:
                fp.writelines(equipo['name'] + "\n")
            
def cargar_liga(liga,pais):    
    #Menu guardado o muestra de datos
    while True:
        print("*********************************************")
        print(f'''  Mostrando datos de la liga {pais}"\n
        1.- Mostrar datos
        2.- Guardar a txt
        0.- Volver\n''')

        opcion = input("Elija la opción correspondiente: ")

        match opcion:
            case('1'): 
                mostrar_datos(liga)
            case('2'):
                guardar_datos(liga,pais)
            case('0'):
                main()
            case(_):
                print("\nERROR, introduzca una opción válida\n")    

