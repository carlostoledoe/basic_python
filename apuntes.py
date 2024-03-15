# #string multilinea con '''
# nombre = '''Juan
# Manuel
# Pérez
# Toro'''
# print(nombre) 







# # Transformar integer o float
# inte = int(input('Ingrese un número (integer): \n ')) 
# floa = float(input('Ingrese un número (float): \n ')) 
# print ('Nunmero integer: ' + str(inte))
# print ('Nunmero float: ' + str(floa))





# #Uso de comilla simple en string
# etiqueta = '''<a hred="#">Región O'higgins</a>'''
# etiquete = """<a hred="#">Región O'higgins</a>"""
# etiqueti = '<a hred="#">Región O\'higgins</a>'
# print(etiqueta)
# print(etiquete)
# print(etiqueti)





# #Interpolando
# nombre = input('¿Cuál es tu nombre? \n'); apellido = input('¿Cúal es tu apellido? \n')
# print (f'''
# Tu nombre es:   {nombre}
# TU apellido es: {apellido}
# ''')





#Operadores booleanos
'''
Operación     Significado

<             estrictamente menor que
<=            menor o igual que
>             estrictamente mayor que
>=            mayor o igual que
==            igual que
!=            diferente que
is            igualdad a nivel de identidad (Son el mismo objeto)
is not        desigualdad a nivel de identidad (no son el mismo objeto)
'''
# proposicion = not ((10 > 2 + 2) and (5 < 3 or 6 > 1))
# #                       true           false   true
# #                       true            true
# #                               true
# #                               False
# print(proposicion)





# #Valor no valido o error
# while True:
#     try:
#         numero = int(input('Dime un número: '))
#         print(f'El número ingresado es {numero}.')
#         break  # Si se ingresa un número correctamente, se rompe el bucle.
#     except ValueError:
#         print('Eso no es un número válido. Intenta de nuevo.')
# print ('Correcto!!')





# Reducir decimales Usando round()
numero = 3.14159
reducido = round(numero, 2)
print(reducido)  # Salida: 3.14





#Raiz cuadrada
from math import sqrt
sqrt(81) #9.0
#Una alternativa es elevar al exponente 0.5:
81 ** 0.5 #9.0




