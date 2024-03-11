import cargar_liga as liga

def main():
    """ Menu Operaciones"""
    while True:
        print('''       Bienvenido al sistema gestor de ligas\n
        De que liga quiere cargar los datos:\n
        1.- Liga Española
        2.- Liga Alemana
        3.- Liga Austriaca
        4.- Liga Inglesa
        5.- Liga Italiana
        0.- Salir\n''')

        opcion = input("Elija la opción correspondiente: ")

        match opcion:
            case('1'):
                liga.cargar_liga(espana)
            case('2'):
                liga.cargar_liga(alemania)
            case('3'):            
                liga.cargar_liga(austria)
            case('4'):
                liga.cargar_liga(inglaterra)
            case('5'):
                liga.cargar_liga(italia)
            case('0'):
                quit()
            case(_):
                print("\nERROR, introduzca una opción válida\n")

if __name__ == "__main__":
    main()