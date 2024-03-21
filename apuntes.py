# #string multilinea con '''
# nombre = '''Juan
# Manuel
# Pérez
# Toro'''
# print(nombre)





# #Concatenando
# print('Carlos ' + 'Santana')
# print('Carlos ' * 3)





# #Salto de linea
# print("hola\na\ntodos")






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
# Tu apellido es: {apellido}
# ''')






# #Otra forma de interpolar sin usar f
# nombre = 'Carlos'
# apellido = 'Santana'
# print("Mi nombre es {} {}" .format(nombre, apellido))








# #Interpolando, no se usa f
# nombre = input('¿Cuál es tu nombre? \n'); apellido = input('¿Cúal es tu apellido? \n')
# print ('''
# Tu nombre es:   {}
# Tu apellido es: {}
# '''.format(nombre, apellido))







# #Valor no valido o error
# while True:
#     try:
#         numero = int(input('Dime un número: '))
#         print(f'El número ingresado es {numero}.')
#         break  # Si se ingresa un número correctamente, se rompe el bucle.
#     except ValueError:
#         print('Eso no es un número válido. Intenta de nuevo.')
# print ('Correcto!!')









# #Tipos de variables:
# variable = "Hola Mundo"
# print(type(variable))  # Salida: <class 'str'>

# numero = 42
# print(type(numero))  # Salida: <class 'int'>

# flotante = 4.32
# print(type(flotante)) # Salida: <class 'bool'>

# lista = [1, 2, 3]
# print(type(lista))  # Salida: <class 'list'>

# booleano = False
# print(type(booleano)) # Salida: <class 'bool'>






# #Métodos de string
# print('Nirvana canta '.count('an')) #Cuenta cuantas veces sale an
# print(len('Grupo musical de metal  5')) #Cuenta llos carácteres inculuido espacios
# print('santana'.upper()) #Todas en máyusculas
# print('HolA cOmo EstÁS '.lower()) #Todas en minúsculas
# print('carlos santana'.title()) #Mayúscula las primeras letras
# print('hola a todos'.capitalize()) #la primera letra
# print(' Hola a todo, cómo están '.strip()) #elimina los espacios al final o al principio
# print('Hola mundo'.replace('o', 'x')) #reemplaza las ocurrencias
# print(' -> '.join(['papel', 'piedra', 'tijera'])) #Une elementos con el string






# #Separador de palabra usando espacio
# texto = "Hola, ¿cómo estás?"
# palabras = texto.split()  # El separador por defecto es el espacio en blanco
# print(palabras)  # Salida: ['Hola,', '¿cómo', 'estás?']






# #Separador usando un #
# aaa = "carlos#santana#cantante#de#musica"
# separado = aaa.split('#')  # Usando la coma como separador
# print(separado)







# def validarPassword(password): #Acoplar funciones para hacer más fácil revisar, arreglar
#     #Validamos que sea de largo al menos sea 6
#     if len(password) < 6:
#         print('Su contraseña debe contener al menos 6 caracteres')
#     elif password == '12345678':
#         print('Este password es muy sencillo. Elija otro')
#     elif password == '87654321':
#         print('Este password es muy sencillo. Elija otro')
#     elif ("'" in password) or ("*" in password) or ("-" in password):
#         print("No puede usar especial dentro de su password")
#     else:
#         print('Contraseña correcta')

# #Le pido la nueva contraseña la usuario
# password = input('Ingrese una contraseña: ')

# #Valido la contraseña con la función "validarPassword"
# validarPassword(password)





# import getpass

# def validarPassword(password): #Acoplar funciones para hacer más fácil revisar, arreglar
#     #Validamos que sea de largo al menos sea 6
#     if len(password) < 6:
#         print('Su contraseña debe contener al menos 6 caracteres')
#         return False
#     elif password == '12345678':
#         print('Este password es muy sencillo. Elija otro')
#         return False
#     elif password == '87654321':
#         print('Este password es muy sencillo. Elija otro')
#         return False
#     elif ("'" in password) or ("*" in password) or ("-" in password):
#         print("No puede usar especial dentro de su password")
#         return False
#     else:
#         print('Contraseña correcta')
#         return True

# def main():
# # esCorrecta = False
# # while esCorrecta != True:
#     while True:
#         # 1. Le pido la nueva contraseña la usuario
#         password = getpass.getpass('Ingrese una contraseña: ')
#         print(f'Password ingresado: {password}')
#         # Valido la contraseña con la función "validarPassword"
#         esCorrecta = validarPassword(password) 
#         # Si la contraseña es incorretca, repite el ciclo. Si está bien, salgo del ciclo con break
#         if esCorrecta:
#             break # Salir del ciclo
#     print('Bienvenido!') # Fuera del ciclo

# main()







# numero = None
# while numero is None:
#     try:
#         numero = int(input("Ingresa un número: "))
#     except ValueError:
#         print("Eso no es un número válido.")




# import sys
# def sigma():
#     numero = int(sys.argv[1])
#     i = 1 #inicar iterador
#     suma = 0
#     while i <= numero: #condición
#         suma += i
#         i += 1 #Incremento
#     print(suma) 
# sigma()





# def sigmafor():
#     suma = 0
#     for i in range(1, 101, 1): #el for se ocupa con range: inicio, final+1, salto
#         suma += i
#     print(suma)
# sigmafor()





# for letra in 'hola como estas':
#     print(letra)
