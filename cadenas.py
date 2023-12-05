#EJEMPLOS DE ACCESO A CADENAS DE TEXTO

#Las cadenas de texto van desde la posicion 0 hasta n-1
cadena = "Hola Mundo"
#         0123456789    Posiciones dentro de la cadena.

#cadena[inicio:fin -1:incremento]

print(cadena)               #Hola Mundo
print(cadena[0])            #H
print(cadena[0:1])          #H
print(cadena[0:7:2])        #Hl u    Muestra posiciones 0 = H,2 = l,4 = ' ',  6 = u
print(cadena[-2])           #Comenzamos desde el final

print(cadena[::1])          #Si no ponemos inicio o fin se supone que es desde el primer elemento hasta el ultimo
print(cadena[::2])          #En este caso mostramos las posiciones 0,2,4,6,8 "Hl ud"
print(cadena[::-1])         #En este caso mostramos las posiciones 9,8,7,6,5,4,3,2,1,0  Comenzando desde el final ya que incremento es negativo
print(cadena[::-2])         #En este caso mostramos las posiciones 9,7,5,3,1 "Hl ud" 
print(cadena[5::1])         #Si no ponemos "fin" recorre toda la cadena desde la posicion inio
print(cadena[1::3])         #Muestra desde inicio hasta el fin una letra cada 3 (Posiciones 1,4,7)  "o n"




