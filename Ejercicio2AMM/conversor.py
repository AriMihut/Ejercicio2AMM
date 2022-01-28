from Ejercicio2AMM.Ejercicio2AMM.monedas import Dolar, Libra, Yen


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
    try:
        return int(input())
    except ValueError:
        return None


def mostrar_cantidad_en_euros(cantidad_en_euros):
    print(f'La cantidad en euros es:  {cantidad_en_euros}')


if __name__ == '__main__':
        mostrar_menu_principal()
        opcion_menu_principal = leer_opcion('Elija una opción: ')
        if  opcion_menu_principal in range(1, 4):
            pedir_cantidad()
            cantidad = leer_cantidad()
            if opcion_menu_principal == 1:
                dolar = Dolar()
                mostrar_cantidad_en_euros()
            elif opcion_menu_principal == 2:
                libra = Libra()
            elif opcion_menu_principal == 3:
                yen = Yen()
        elif opcion_menu_principal == 0:
            exit(0)
        else:
            print('Opción no válida!')
