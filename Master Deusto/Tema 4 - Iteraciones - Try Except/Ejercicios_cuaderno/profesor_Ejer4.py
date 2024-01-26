agenda = {}
def añadir():
    global agenda
    Nombre = input("Añade un nombre para el contacto: ")
    if(agenda.get(Nombre) != None):
        print("El nombre ya existe, se modifica el teléfono.")    
    Teléfono = input("Añade el teléfono del contacto: ")
    agenda[Nombre] = Teléfono
    return True
def borrar():
    global agenda
    esNombre = input("¿Desea borrar por nombre o por teléfono? N o T: ")
    if(esNombre == "N"):
        para_borrar = input("¿Qué nombre deseas borrar? ")
        if(agenda.get(para_borrar) != None):
            print("Se ha borrado el usuario ->", para_borrar,"-",agenda.pop(para_borrar))
        else:
            print("El usuario no existe")
    elif(esNombre == "T"):
            para_borrar = input("¿Qué teléfono deseas borrar? ")
          
            if(para_borrar in agenda.values()):
                key = next((k for k in agenda if agenda[k] == para_borrar), None)
                print("Se ha borrado el usuario ->", key,"-",agenda.pop(key))
    else:
            print("Función desconocida, vuelva a intentarlo")
    return True
def visualizar():
    global agenda
    i = 0
    for clave,valor in agenda.items():
         print("Contacto: ",clave,"--> Telefono:", valor)
         i+=1
    
    print("{} Contactos en la agenda".format(i))
    return True
def switch(opcion):
    diccionario = {
    "1": "añadir()",
    "2": "borrar()",
    "3": "visualizar()"
    }
    return eval(diccionario.get(opcion))
while(True):
    print("""Selecciona una opción:
    1) Añadir
    2) Borrar
    3) Visualizar""")
    opcion = input()
    try:
      continuar = switch(opcion)
    except Exception as a:
      print("Seleccione una opción válida")#Gestionar más concretamente