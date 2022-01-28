def pedir_opcion_menu_principal():
    print('Escoja una opción: ')

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


if __name__ == '__main__':
    mostrar_menu_principal()
    pedir_opcion_menu_principal()
    opcion_menu_principal = leer_opcion()