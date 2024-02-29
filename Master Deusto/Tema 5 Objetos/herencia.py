class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        print("El vehículo está acelerando")
        
    def frenar(self):
        print("El vehículo está frenando")
    
class VehiculoElectrico:
    def __init__(self,marca,modelo,capacidad_bateria):
        Vehiculo.__init__(self,marca,modelo)
        self.capacidad_bateria = capacidad_bateria
    
    def cargar_bateria(self):
        print("Cargando Bateria")
    
    def acelerar(self):
        print("El vehículo eléctrico está acelerando")
        
class VehiculoHibrido(Vehiculo,VehiculoElectrico):
    def __init__(self, marca, modelo,capacidad_bateria,capacidad_tanque):
        Vehiculo.__init__(self,marca, modelo)
        VehiculoElectrico.__init__(self,marca,modelo,capacidad_bateria)
        self.capacidad_tanque = capacidad_tanque
    
    def recorrer_Distancia(self,distancia):
        consumo_bateria = distancia / 10
        if (consumo_bateria <= self.capacidad_bateria):
            self.capacidad_bateria = consumo_bateria
            print("El vehiculo hibrido ha recorrido la distancia de " , distancia ,"km") 
        else:
            print("Capacidad de bateria insuficiente")

#Creamos objeto

Vehiculo_hibrido = VehiculoHibrido("Toyota", "Prius", 50 , 40)

print(Vehiculo_hibrido.marca)
print(Vehiculo_hibrido.modelo)
Vehiculo_hibrido.acelerar()
Vehiculo_hibrido.frenar()