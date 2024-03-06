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
        self.apellido = apellido
        self.apellido_2 = apellido_2
        self.poblacion = poblacion
        self.pais = pais

class Favoritas(Persona,Cancion):
    
    def __init__(self,persona,cancion):
        """Cancion.__init__(self, cancion.titulo, cancion.grupo, cancion.genero)
        Persona.__init__(self, persona.dni, persona.nombre, persona.apellido, persona.apellido_2
                         , persona.poblacion, persona.pais,cancion)"""
        #Cancion.__init__(self, titulo, grupo, genero)
        #Persona.__init__(self, dni, nombre, apellido, apellido_2, poblacion, pais,cancion)
        self.dni = persona.dni
        self.titulo = cancion.titulo
        
    def mostrar_favorita(self):
        print("La cancion favorita de {} es {}." .format(self.dni,self.titulo))            
""""""

cancion = Cancion("Hola", "ACDC" , "Rock")
persona = Persona("34898103L","Javier","Lopez" , "Lopez", "Madrid" ,
                       "España")

favorita = Favoritas(persona,cancion)
print(favorita.dni)
print(favorita.titulo)
favorita.mostrar_favorita()
#favorita.mostrar_favorita()"""