#En este modulo definimos las clases necesarias 

class Persona():
    
    def __init__(self,dni,nombre,apellidos,apellido_2,poblacion,pais):
        dni = self.dni
        nombre = self.nombre
        apellido = self.apellido
        apellido_2 = self.apellido_2
        poblacion = self.poblacion
        pais = self.pais
        

class Cancion():
    def __init__(self, titulo, grupo, genero):
        titulo = self.titulo
        grupo = self.grupo
        genero = self.genero

class Favoritas(Persona,Cancion):
    
    def __init__(self):
        Persona.__init__(self, dni, nombre, apellido, apellido_2, poblacion, pais)
        Cancion.__init__(self, titulo, grupo, genero)
    
    def mostrar_favorita(self):
        print("La cancion favorita de {} es {}." .format(self.dni,self.titulo))            
