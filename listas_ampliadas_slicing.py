nombres = ['adri', 'javi','raul', 'gonzalo']
for nombre in nombres:
    print(nombre)

for nombre in nombres[1:3]:
    print(nombre)

for nombre in nombres[:3]:
    print(nombre)

for nombre in nombres[-1:]:
    print(nombre)
#OJO SIN EMBARGO SI NO PONEMOS LOS DOS PUNTOS 
for nombre in nombres[-2]:
    print(nombre)


for nombre in nombres[0:len(nombres):2]:
    print(nombre)

for nombre in nombres[-1:len(nombres):1]:
    print(nombre)

# COMO COPIAR UNA LISTA
# SI ASIGNAMOS SIN PONER INDICES APUNTAN AL MISMO SITIO
# PERO NO SE COPIA EN UNA VARIABLE NUEVA. LO COMPROBAMOS A CONTINUACION
nombres_2 = nombres
print(nombres_2)

nombres_2.append('Roi')
nombres.append('Pedrito')
# AMBAS TIENEN LA MISMA LISTA
print(nombres_2)
print(nombres)

# MODO CORRECTO DE COPIAR UNA LISTA
print("MODO CORRECTO")
print(nombres)
del nombres_2
nombres_2 = nombres[:]
nombres_2.append('Jorge')
print(nombres_2)
print(nombres)
