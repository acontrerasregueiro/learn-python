"""
ENUNCIADO:
Escribir un menú infinito para acceder a casa.
Inicialmente por defecto:
contraseña = "12345"
El menú debe tener 3 opciones:
1.Modificar contraseña
Para modificar la contraseña, debe solicitar comprobar la anterior contraseña, y solicitar la
nueva dos veces para validar que coinciden.
2.Parar menú
Para desactivar el menú infinito, debe solicitar la contraseña y, si es válida, salir del bucle.
3.Entrar en casa
Solicitar la contraseña, mostrar por pantalla (Puedes pasar).
Ejercicio 3
Recomendamos utilizar la función switch() que hemos visto en el módulo. Y cada punto del
menú que sea una función.

"""
def modificar():
    global contraseña
    vieja_pass = input('Introduce la contraseña vieja')
    if vieja_pass == contraseña:
        nueva = input('Introduce la nueva contraseña')
        nueva2 = input('Repite la nueva contraseña')
        if nueva == nueva2:
            contraseña = nueva
            print("Contraseña cambiada con éxito")
        else:
            print("Lo siento las contraseñas no coinciden, no se ha podido modificar")
    else:
        print("Contraseña errónea")
def entrar():
    vieja_pass = input('Introduce la contraseña vieja')
    if vieja_pass == contraseña:
        print("Bienvenido , puedes pasar")

def salir():
    quit()

def accion(opcion):
    diccionario = {
    '1':'modificar()',
    '2':'salir()',
    '3':'entrar()'
    }
    return eval(diccionario.get(opcion))

contraseña = '12345'

while True:
    print("""
        1.-Modificar contraseña
        2.-Salir
        3.-Entrar en casa       
        """)
    try:
        opcion = input("Elija una opción : ")
        accion(opcion)
    except Exception:
        print("Introduce una opción válida")
    
          