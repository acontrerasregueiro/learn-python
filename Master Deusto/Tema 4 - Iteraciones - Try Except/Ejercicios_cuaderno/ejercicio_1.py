"""
ENUNCIADO : 
Vamos a realizar una fiesta privada en un museo, y vamos a colocar un programa que contenga
una clave secreta, almacenada en una variable llamada password.
Vamos a ser tolerantes con las mayúsculas y minúsculas.
El usuario tendrá que teclear la contraseña por teclado, si no coincide, mostrará un mensaje
advirtiendo al usuario que no puede entrar; en caso contrario, le daremos la bienvenida al
museo.
Si el usuario puede entrar, solicitaremos la edad del usuario y comprobaremos si tieme más de
16 años.
No olvides dar las gracias al usuario siempre.

"""

clave_secreta = '1234'

password = input("Escribe la contraseña : ")

if password == clave_secreta:
    try:
        edad = int(input("Escribe la edad : "))
        if edad > 16:
            print("Bienvenido , puedes pasar\nMuchas gracias por visitarnos")
        else: print("Lo siento no puedes pasar debes ser mayor de 16 años")
    except ValueError:
        print("Debes introducir un número valido")
else:
    print("Clave incorrecta no puedes pasar")
