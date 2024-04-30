import sys
import pygame

class AllienInvasion:
    """Clase general para manejar activos y comportamiento del juego"""
    
    def __init__(self):
        """Iniciamos el juego y creamos recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((1200,800))  #Resolucion
        pygame.display.set_caption("Allien Invasion")   #Titulo
        self.bg_color = (230,230,230)   #Background color
        
    def run_game(self):
        """Bucle inicial para lanzar el juego"""
        while True:
            #Escuchamos eventos de raton y teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color) #Redibujamos la pantalla en cada vuelta del loop
            #Mostramos la pantalla
            pygame.display.flip()
            self.clock.tick(60)  #Intentamos que corra a 60FPS

if __name__ == '__main__':
    #Creamos una instancia del juego y la ejecutamos
    ai = AllienInvasion()
    ai.run_game()