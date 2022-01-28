def leer_opcion(texto):
    try:
        return int(input(texto))
    except ValueError:
        return None


def mostrar_menu_principal():
    print('''
CONVERSOR DE MONEDAS
1. Dólares
2. Libras
3. Yens
0. Salir    
        ''')


def pedir_cantidad():
    print('Indique la cantidad: ')


def leer_cantidad():
    pass


if __name__ == '__main__':
    while True:
        mostrar_menu_principal()
        opcion_menu_principal = leer_opcion('Elija una opción: ')
        if opcion_menu_principal == 1:
            pedir_cantidad()
            cantidad = leer_cantidad()

        elif opcion_menu_principal == 2:
            pedir_cantidad()
            cantidad = leer_cantidad()
        elif opcion_menu_principal == 3:
            pedir_cantidad()
            cantidad = leer_cantidad()
        elif opcion_menu_principal == 0:
            exit(0)
        else:
            print('Opción no válida!')
