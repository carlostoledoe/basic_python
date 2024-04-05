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






#Operadores de asignación
#   a = 2 a toma el valor 2.
#   a += 2 a es incrementado en dos y asignado el valor resultante.
#   a -= 2 a es reducido en dos y asignado el valor resultante.
#   a *= 3 a es multiplicado por tres y asignado el valor resultante.
#   a /= 3 a es dividido por tres y asignado el valor resultante




#Contador:
# cont = cont + 1
# cont += 1

#Acumulador:
# acu = acu + valor
# acu += valor






# #Métodos disponibles para cada tipo de dato o escructura
# metodos = dir(list)
# for metodo in metodos:
#     print(metodo)








# Variables
# Python buscará si existe dicha variable en su propio scope; y en caso de existir utilizará dicho valor, 
# en caso contrario escalará a un ambiente superior
# La manera de poder utilizar una variable local en el ambiente global es mediante return,
# la que viene a ser la conexión entre el scope local de una función y el ambiente local.


# continent = 'South America'  #Definida en ambiente global
# def get_continent():
#     print(continent) # Contiente no está definida en el ambiente local o en su scope
# get_continent() 







# # Modificar una variable global desde un entorno local. NO recomendado
# continent = 'South America'

# def get_continent():
#     global continent
#     continent = 'Africa'

# get_continent()
# print(continent)










