# Parámetro es cuando defino la función y 
# el argumento es lo que le paso cuando invoco a esta
# Principio DRY: Don't Repeat Yourself





# def buenos_modales(nombre = 'Anonimo'): #Valor por defecto cuando está sin argumento (nombre = parámetro, entrada)
#     hola = 'Buenos dias ' + nombre
#     chao = 'Nos vemos, ' + nombre
#     return hola, chao # es una tupla

# #Desempaquetar la tupla
# saludo, adios = buenos_modales('Cristian') 
# '''
# palabras = buenos_modales('Matias')
# saludo = palabras[0]
# adios = palabras[1]
# '''
# print(saludo)
# print(adios)




# # Función que solo imprime el menú y puede ser reutilizado
# def imprimir_menu():
#     print('Opciones: ')
#     print('1) De acuerdo')
#     print('2) En desacuerdo')
#     print('3) No me interesa')
# imprimir_menu() # Invocar a la función






# # Retorno de dos valores (Tupla)
# def cuadrado_cubo(base):
#     cuadrado = base**2
#     cubo = base**3
#     return cuadrado, cubo
# # Desempaquetadp
# valor_cuadrado, valor_cubo = cuadrado_cubo(2)
# print(valor_cuadrado)
# print(valor_cubo)








