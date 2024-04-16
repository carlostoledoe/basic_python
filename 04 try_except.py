# #Valor no valido o error
# secreto = 3
# while True:
#     try:
#         numero = int(input('Adivina el número: '))
#         if numero == secreto:
#             break
#         else:
#             print('> Numero erroneo. Itenta de nuevo.')
#     except ValueError: 
#         print('> Eso no es un número. Intenta de nuevo.')
# print ('Correcto!!')




# #en caso que ingrese un string
# try: 
#     eleccion = int(input('Elija un número: '))
# except ValueError:
#     print(f'Debe ingresar solo números')
# else:
#     print(f'Correcto, ha eledigo el número {eleccion}')