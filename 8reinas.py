import random
import numpy as np

def buscar_reinas():
    global tablero
    global filas_no_validas
    global columnas_no_validas
    for fila in range(0,8):
        for columna in range(0,8):
            if tablero[fila][columna] == 1:
                print('encontrada reina en posición : ', fila, columna)
                if not fila in filas_no_validas:                    
                    filas_no_validas.append(fila)                    
                if not columna in columnas_no_validas:
                    columnas_no_validas.append(columna)
                
    print('FILAS NO VALIDAS :', filas_no_validas)
    print('COLS NO VALIDAS :', columnas_no_validas)
#Creamos tablero
tablero = np.zeros((8,8))
reinas_colocadas = 0
filas_no_validas = []
columnas_no_validas =[]
    
def colocar_reina():    
    global reinas_colocadas
    global tablero
    #Primera reina colocada
    if reinas_colocadas == 0:
        
        fila = random.randint(0,7)      
        columna = random.randint(0,7)
        reinas_colocadas +=1
        tablero[fila][columna] = 1
        print('Colocada PRIMERA reina en ', fila, columna)
        print('Numero de reinas colocadas ', reinas_colocadas)
        print(tablero)
        colocar_reina()
                
    else:
                
        if reinas_colocadas < 8:
            
                
            reinas_colocadas +=1
            tablero[fila][columna] = 1                
            print('Colocada REINA en ', fila, columna)
            print('Numero de reinas colocadas ', reinas_colocadas)
            print(tablero)
            colocar_reina()
                            
colocar_reina()
buscar_reinas()
print(tablero)





