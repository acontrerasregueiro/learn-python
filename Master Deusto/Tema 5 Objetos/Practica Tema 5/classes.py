#En este modulo definimos las clases necesarias 
class Cancion():
    def __init__(self, titulo, grupo, genero):
        self.titulo = titulo
        self.grupo = grupo
        self.genero = genero

class Persona():
    
    def __init__(self,dni,nombre,apellido,apellido_2,poblacion,pais):
        self.dni = dni
        self.nombre = nombre
        self.poblacion = poblacion
        self.pais = pais

class Favoritas(Persona,Cancion):
    
    def __init__(self,persona,cancion):
        self.dni = persona["dni"]
        self.nombre = persona["nombre"]
        self.poblacion = persona["poblacion"]
        self.pais = persona["pais"]
        self.titulo = cancion["titulo"]
        self.grupo = cancion["grupo"]
        self.genero = cancion["genero"]
        
    def mostrar_favorita(self):
        print("*************************************\n")
        print(f"Nombre : {self.nombre}\n")
        print(f"DNI :\t {self.dni}\n")
        print(f"Lugar :\t {self.poblacion}, {self.pais}\n")
        print(f"Gustos : {self.titulo}, de {self.grupo}, género {self.genero}\n")