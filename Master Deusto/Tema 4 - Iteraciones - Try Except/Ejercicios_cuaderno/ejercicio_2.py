"""
ENUNCIADO:
    
En una empresa quieren implantar un seguro privado, y van a aplicar un descuento relativo al
tiempo que están empleados con un contrato indefinido. Si tienen cualquier otro tipo de
contrato, no obtendrán ningún descuento.
El descuento aplicable es de un 5% por año trabajado hasta obtener un máximo del 50%; pero si
llevan más de 19 años y tiene más de 2 hijos, se le aplica un 70%, y si tiene menos hijos se
queda con el 50%.
Quieren realizar un programa para que puedan comprobar qué tipo de descuento se les puede
aplicar.
Ejercicio 2
Avisa en todos los casos por pantalla.

"""

def calcular_descuento(indefinido,años,hijos):
    
    if indefinido == False:
        return 0
    elif años > 19 and hijos > 2:
        return 70
    elif años > 19 and hijos < 2:
        return 50
    else:
        if años * 5 >= 50:
            return 50
        else:
            return años * 5    

indefinido = input("Tiene usted contrato indefinido (s/n)")
print(indefinido)
if indefinido == 's' or indefinido == 'n':
    print(f'{indefinido}')
    años = int(input("Cuantos años lleva usted en la empresa"))
    hijos = int(input("Cuantos hijos tiene usted"))
    descuento = calcular_descuento(indefinido,años,hijos) 
    print('Su descuento es del {0} por ciento'.format(descuento))
else:
    print('Debes introducir un valor válidos')
        
         
