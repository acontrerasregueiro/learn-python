class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"

animales =[Perro("Max"), Gato("Luna"), Vaca("Daisy")]       

for animal in animales:
    nombre = animal.nombre
    sonido = animal.hacer_sonido() 
    print(f"{nombre} hace : {sonido}")