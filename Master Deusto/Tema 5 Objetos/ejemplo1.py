#Iniciacion a POO

class Perro:
    
    especie = 'mamífero'
    #El método __ini__ es llamado al crear el objeto
    
    def __init__(self,nombre,raza):
        print(f"Creando perro {nombre}, {raza}")
        
        #Atributos de la instancia
        self.nombre = nombre
        self.raza = raza
        
    def ladra(self):
        print("Guau")
    
    def camina(self,pasos):
        print(f"Caminando {pasos} pasos")
        
miperro = Perro('Oli','Mastin')
miperro.camina(4)
miperro.ladra()

print(miperro.nombre)
        