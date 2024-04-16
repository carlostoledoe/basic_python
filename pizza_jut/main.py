import os
import time
import string as s
from masa import cambiar_tipo_masa
from salsa import agregar_salsa
from add import agregar_ingredientes
from remove import quitar_ingredientes
from show import mostrar_ingredientes

pizza_base = {
    'masa': 'Masa Tradicional',
    'salsa': 'Salsa de Tomate',
    'ingredientes': []
}

def menu():
    os.system('clear')
    print('\n                *** Bienvenido a Pizza Jut ***')
    while True:
        try:
            opcion = int(input(s.principal))
            if opcion == 1:
                eleccion = input(s.tipo_de_masa)
                cambiar_tipo_masa(pizza_base, eleccion)
            elif opcion == 2:
                eleccion = input(s.salsa)
                agregar_salsa(pizza_base, eleccion)
            elif opcion == 3:
                eleccion = int(input(s.ingredientes_disponibles))
                agregar_ingredientes(pizza_base, eleccion)
            elif opcion == 4:
                quitar_ingredientes(pizza_base)
            elif opcion == 5:
                print('Ordenar')
            elif opcion == 6:
                mostrar_ingredientes(pizza_base)
            elif opcion == 0:
                print('Saliendo del programa...')
                exit(time.sleep(1))

        except ValueError:
            print('     **** Opción no valida ****')



if __name__ == '__main__':  
    menu()