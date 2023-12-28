def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("GO!")
        print("Fin de la función", numero)

cuenta_atras(5)

x = 31
y = 12
def funcion():
    global x
    x = 10
    print(f'x vale {x}')
    print(f'y vale {y}')
funcion()
print(x)

for i in range (1,6):
    if i == 3:
        continue
    print(i)
    

print(False * 'asd')