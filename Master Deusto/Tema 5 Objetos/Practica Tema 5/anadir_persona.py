#Fichero con la funcion y comprobaciones para añadir personas

def anadir_persona():
    #Guardaremos los datos de la persona a añadir en un diccionario
    nuevo_usuario = {}
    #Nombre y apellidos
    while True:
        nombre = input("Introduzca el nombre y apellidos de la persona: ")
        if isinstance(nombre,str):
            nuevo_usuario["nombre"] = nombre.strip().title()
            print(nuevo_usuario) 
            break                       
        else:
            print("Introduzca un nombre válido")
            continue
    #Dni
    while True:
        dni = input("Introduzca el DNI, recuerde introducir la letra: ")
        if dni.isalnum() and len(dni) == 9:
            if dni[-1].isalpha and dni[0:8].isalpha:
                nuevo_usuario["dni"] = dni.strip().upper()
                print(nuevo_usuario) 
                break                       
            else:
                print("Introduzca un DNI válido")
                continue
        else:
            print("Introduzca un DNI válido")
            continue
    #Poblacion
    while True:
        poblacion = input("Introduzca la población: ")
        #eliminamos los espacios para comprobar que sean sólo letras

        if poblacion.replace(" ","").isalpha():
            nuevo_usuario["poblacion"] = poblacion.strip().title()
            print(nuevo_usuario) 
            break                       
        else:
            print("Introduzca una población válido")
            continue
    #Pais
    while True:
        pais = input("Introduzca el pais: ")
        if pais.replace(" ","").isalpha():
            nuevo_usuario["pais"] = pais.strip().upper()
            print(nuevo_usuario) 
            break                       
        else:
            print("Introduzca un pais válido")
            continue    
    return nuevo_usuario