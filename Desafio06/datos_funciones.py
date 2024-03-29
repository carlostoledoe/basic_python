# import sys
# umbral = int(sys.argv[1])

# if len(sys.argv) > 2:
#     if sys.argv[2] == 'menor':
#         mayor_menor = 'menor'
#     else:
#         print('Lo sentimos, no es una operación válida')
#         sys.exit()
# else:
#     mayor_menor = 'mayor'

# def filtro(umbral, mayor_menor = 'mayor'):
#     precios = {
#     'Notebook': 700000,
#     'Teclado': 25000,
#     'Mouse': 12000,
#     'Monitor': 250000,
#     'Escritorio': 135000,
#     'Tarjeta de Video': 1500000
#     }
#     productos_filtrados = []
#     if mayor_menor == 'mayor':
#         for producto, precio in precios.items():
#             if precio > umbral:
#                 productos_filtrados.append(producto)
#         impresion_productos = ', '.join(productos_filtrados)
#         print(f'Los productos mayores al umbral son: {impresion_productos}')
#     else:
#         for producto, precio in precios.items():
#             if precio < umbral:
#                 productos_filtrados.append(producto)
#         impresion_productos = ', '.join(productos_filtrados)
#         print(f'Los productos menores al umbral son: {impresion_productos}')

# filtro(umbral, mayor_menor)








# velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
# 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

# def mediciones(velocidad):
#     totales = 0
#     for valores in velocidad:
#         totales += valores
#     promedio = totales / len(velocidad)
#     posiciones = []
#     for pos, val in enumerate(velocidad):
#         if val > promedio:
#             posiciones.append(pos)
#     print(posiciones)

# mediciones(velocidad)







# def factorial(numero):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado

# def productoria(lista_valores):
#     producto = 1
#     for i in lista_valores:
#         producto *= i
#     return producto

# def calcular(fact_1, prod_1, fact_2):
#     resultado_factorial1 = factorial(fact_1)
#     resultado_productoria = productoria(prod_1)
#     resultado_factorial2 = factorial(fact_2)
#     print(f'El factorial de {fact_1} es {resultado_factorial1}')
#     print(f'La productoria de {prod_1} es {resultado_productoria}')
#     print(f'El factorial de {fact_2} es {resultado_factorial2}')

# calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)