#EJEMPLOS ASIGNACION DE VARIABLES

x = 1
print(type(x))
print(x)

x,y = 1,2
print(' X = ',x ,' Y = ', y )

#EJEMPLO ASIGNANDO A TODAS EL MISMO VALOR
x = y = z = 20
print(x,y,z)

#CURIOSIDAD
#EJEMPLO DE ASIGNACION MULTIPLE
x = 4
y = 5
x,y = y,x
print(x,y)

#ERROR DE DEBEN ASIGNAR TANTOS VALORES COMO VARIABLES
'''x,y,z = 1,2,3,4
print(x,y,z)'''

#EJEMPLO 'del'
'''
x = 'a'
del x
print(x)
'''
