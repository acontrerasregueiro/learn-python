def añadir():
    print("Funcion añadir")
    
def borrar():
    print("Funcion borrar")
    
def visualizar():
    print("Funcion Visualizar")
    
def salir():
    quit()
    
def switch(opcion):
    diccionario = {
    "1": "añadir()",
    "2": "borrar()",
    "3": "visualizar()",
    "4": "salir()"
    }
    print(diccionario.get(opcion))
    print(diccionario.values)
    #La función eval() toma una única cadena de texto como argumento y la evalúa como código Python.
    return eval(diccionario.get(opcion))

while(True):
    print("""Selecciona una opción:
    1) Añadir
    2) Borrar
    3) Visualizar
    4) Salir""")
    opcion = input()
    try:
      continuar = switch(opcion)
    except Exception as a:
      print("Seleccione una opción válida")#Gestionar más concretament