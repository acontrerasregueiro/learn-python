#Fichero con la funcion y comprobaciones para añadir personas

def anadir_cancion():
    #Guardaremos los datos de la canción a añadir en un diccionario
    nueva_cancion = {}
    #Titulo
    while True:
        titulo = input("Introduzca el titulo de la cancion: ")
        if isinstance(titulo,str):
            nueva_cancion["titulo"] = titulo.strip().title()
            break                       
        else:
            print("Introduzca un nombre válido")
            continue
    #Grupo
    while True:
        grupo = input("Introduzca el grupo: ")
        #eliminamos los espacios para comprobar que sean sólo letras
        if grupo.replace(" ","").isalpha():
            nueva_cancion["grupo"] = grupo.strip().title()
            break                       
        else:
            print("Introduzca una población válido")
            continue
    #Genero
    while True:
        genero = input("Introduzca el genero: ")
        if genero.replace(" ","").isalpha():
            nueva_cancion["genero"] = genero.strip().upper()
            print(nueva_cancion) 
            break                       
        else:
            print("Introduzca un pais válido")
            continue    
    return nueva_cancion