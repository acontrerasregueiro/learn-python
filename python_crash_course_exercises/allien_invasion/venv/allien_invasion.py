import sys
import pygame

class AllienInvasion:
    """Clase general para manejar activos y comportamiento del juego"""
    
    def __init__(self):
        """Iniciamos el juego y creamos recursos"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Allien Invasion")
        
    def run_game(self):
        """Bucle inicial para lanzar el juego"""
        while True:
            #Escuchamos eventos de raton y teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Mostramos la pantalla
            pygame.display.flip()

if __name__ == '__main__':
    #Creamos una instancia del juego y la ejecutamos
    ai = AllienInvasion()
    ai.run_game()