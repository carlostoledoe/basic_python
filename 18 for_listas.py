# lista1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] #Lista por extensión
# lista2 = [num for num in range(0, 20, 2)] #Lista por comprehensión






#Comprehension
# [fórmula for variable in iterable]
# Empezamos por el ciclo, ara cada variable en el iterable realiza la fórmula"





# n = 10
# lista_par = [2*i +2 for i in range(n)]
# print(lista_par)

# lista2 = [num for num in range(0, 20, 2)] #llega al 18
# print(lista2)







# def quina():
#     # lista = []
#     # for i in range(31): #(0,31,1)
#     #     if i % 5 == 0:
#     #         lista.append('QUINA')
#     #     else:
#     #         lista.append(i)
#     lista = ['QUINA' if i % 5 == 0 else i for i in range(31)] # Lista por comprehensión
#     print(lista)
# quina()






# valores = [0,4,5,6,7,8,9]
# divisibles = []
# for valor in valores:
#     if valor % 2 == 0:
#         divisibles.append('Divisible')
#     else:
#         divisibles.append('No Divisible')
# print(divisibles)






# #Lista por comprensión:
# # [expresión1 if condición1 else expresión2 for variable in iterable]
# valores = [0,4,5,6,7,8,9]
# lista = ['Divisble' if valor % 2 == 0 else 'No divisible' for valor in valores]
# print(lista)
# # Empezamos con el ciclo, entonces, para cada valor almacenado en nuestra lista de valores, 
# # vamos mostrar la palabra ‘Divisible’ si el valor módulo de 2 es igual a 0





# def crear_enlaces():
#     nombres = ['Home', 'Quienes Somos', 'Contacto']
#     enlaces = ['<a href="#">' + nombre + '</a>' for nombre in nombres]
#     print(enlaces)
# crear_enlaces()





# #Para filtrar
# grande = ['andrea', 'olga', 'armando', 'pedro', 'anastasia', 'orlando']
# grupo = [nombre for nombre in grande if len(nombre) > 5] #los que tiene más de 5 letras
# print(grupo)







# #Filtrar
# #[expresión for variable in iterable if condición ]
# lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
# lista2 = [valor for valor in lista if type(valor) is str]
# lista3 = [valor for valor in lista if isinstance(valor, str)]
# print(lista2)
# print(lista3)







# ping = [120, 50, 600, 30, 90, 10, 200, 0, 500]
# resultado = ['Bien' if ping <= 90 else 'mal' for ping in ping]
# print(resultado)




# #agrega los mayores e iguales a mil
# a = [100, 200, 1000, 5000, 10000, 10, 5000]
# b = [valor for valor in a if valor >= 1000]
# print(b)






# minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
# resultado = ['bien' if minuto <= 90 else 'mal' for minuto in minutos]
# print(resultado)





# seconds = [100, 50, 1000, 5000, 1000, 500]
# minuts = [numsec / 60 for numsec in seconds]
# print(minuts)





# nombres = ['Chingao', 'Florimar', 'Onur', 'Hernesto Lisama', 'Lazlo', 'Isaura']
# saludos = ['Hola ' + nombre for nombre in nombres ]
# print(saludos)





# rating = [50, 30, 45, 25, 55, 20]
# resultados = ['Bien ' if puntos >= 45 else 'mal' for puntos in rating ]
# print(resultados)







# def sigmafor():
#     suma = 0
#     for i in range(1, 101, 1): #el for se ocupa con range: inicio, final+1, salto
#         suma += i
#     print(suma)
# sigmafor()






# for letra in 'hola como estas':
#     print(letra)






# def visitar_ciudades():
#     ciudades = ['Puerto Montt', 'Talaca', 'Valdivia', 'Santiago', 'Viña del Mar']
#     for ciudad in ciudades:
#         print(f'Este año visitaré: {ciudad}')

# visitar_ciudades()





# ciudades = ['Puerto Montt', 'Talaca', 'Valdivia', 'Santiago', 'Viña del Mar']
# #                  0            1          2           3            4
# print(ciudades[3]) #Santiago





# def penultimo(lista):
#     largo = len(lista)
#     return print(lista[largo - 2])

# penultimo(['Feña', 'Vivi', 'Max', 'Carlos', 'Esteban'])






# ciudades = ['Puerto Montt', 'Talaca', 'Valdivia', 'Santiago', 'Viña del Mar', 'Villa Alemana', 'Quilpué']
# for indice, ciudad in enumerate(ciudades): #permite tomar el indice y nombre
#     frase =f'La ciudad {ciudad} está en la posición {indice}'
#     if indice % 2 == 0:
#         print(frase)






# texto = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme.'
# for num, letra in enumerate(texto):
#     print(f'El caracter {letra} está en la posición {num}')





# #Método zip
# prefijo = ['La','El','La','El']
# frutas = ['manzana', 'platano','frutilla','tomate']
# colores = ['verde','amarillo','roja','rojo']
# for p, fruta, color in zip(prefijo, frutas, colores):
#     print(f'{p} {fruta} es de color {color}')






# def visitar_cuidades():
#     ciudades = ['Puerto Montt', 'Talaca', 'Valdivia', 'Santiago', 'Viña del Mar', 'Villa Alemana', 'Quilpué']
#     for indice, ciudad in enumerate(ciudades): #permite tomar el indice y nombre
#         frase =f'La ciudad {ciudad} está en la posición {indice}'
#         if indice % 2 == 0:
#             print(frase)








# import sys
# def buscar():
#     palabra = sys.argv[1]
#     cuentos = ['En', 'un', 'lugar', 'de', 'la', 'Mancha,', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme,', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero,', 'adarga', 'antigua,', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']
#     encotrado = False
#     for indice, cuento in enumerate(cuentos):
#         if palabra == cuento:
#             encotrado = True
#             print(f'La palabra {cuento} está en la posición {indice}')
#     if encotrado == False:
#         print('La palabra no se encontró')
# buscar()







# import sys
# def buscar():
#     buscada = sys.argv[1]
#     palabras = ['En', 'un', 'lugar', 'de', 'la', 'Mancha,', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme,', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero,', 'adarga', 'antigua,', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']

#     la_encontramos = False #Flag o bandera (is_present)

#     for pos, palabra in enumerate(palabras):
#         if palabra == buscada:
#             frase = f'La palabra {buscada} está en la posción {pos}'
#             print(frase)
#             la_encontramos = True
#             break #para que no siga iterando y así ahorrar recursos
#     if not la_encontramos: # if la_encontramos == False:
#         print(f'La palabra {buscada} no fue encontrada')
# buscar()




# import sys
# def buscar(): #optimizado por Copilot
#     palabra = sys.argv[1]
#     cuentos = ['En', 'un', 'lugar', 'de', 'la', 'Mancha,', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme,', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero,', 'adarga', 'antigua,', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']
#     try:
#         indice = cuentos.index(palabra)
#         print(f'La palabra "{palabra}" está en la posición {indice}')
#     except ValueError:
#         print('La palabra no se encontró')
# buscar()






# #Romper comtraseña
# import sys
# from string import ascii_lowercase
# def fuerza_bruta ():
#     clave = (sys.argv[1]).lower()
#     intentos = 0
#     for letra in clave:
#         for caracter in ascii_lowercase:
#             intentos += 1
#             if letra == caracter:
#                 break
#     print(f'Se logró romper la contraseñanen {intentos} intentos')
# fuerza_bruta()






# #Listas paritiendo de atrás
# a = [1, 2, 3, 4, 5]
# print(a[-2]) # 4 es el penúltimo
# #a.reverse()
# print(a)

# b = a[1:4] #no incluye el último, como el range
# print(b)







# import sys
# def mostrar_agumentos():
#     for indice, palabra in enumerate(sys.argv):
#         print(f'En la posición {indice} está la palabra: {palabra} ')
# mostrar_agumentos()








# #Métodos
cuentos = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete']
# #print(dir(cuentos)) #Ver los métodos

# # El signo + concatena listas, pero append agrega cosas, cualquier cosa
# cuentos.append('siete coma cinco') #inserta al final
# cuentos.insert(2, 'tres coma cinco') #inserta en la posición 2
# cuentos.pop(3) #elimina y lo muestra
# cuentos.remove('seis') #lo borra
# cuentos.reverse() 
# cuentos.sort() #Ordena de mayor a menor o alfabéticamente
# cuentos.sort(reverse = True) #Ordena de menor a mayor
# cuentos = sorted([3,6,7,4,1])
# cuentos = sorted([3,6,7,4,1], reverse = True)
# print(cuentos.index('dos')) # la posición
# cuentos = cuentos + ['hoho', 'jiji', 'eaea']
# cuentos += ['hoho', 'jiji', 'eaea']
# cuentos = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete'] * 3
# cuentos[2] = 'hola'
print(cuentos)




# numero = [1, 2, 3, 4, 5]
# print(sum(numero)) #suma
# print(max(numero)) #el más grande
# print(min(numero)) #el menor







# #agregar un contador:
# #texto = 'Don Quijote de la Mancha​ es una novela escrita por el español Miguel de Cervantes Saavedra'
# texto = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete']
# for pos, letra in enumerate(texto):
#     print(f"La letra en la posición {pos} es la {letra}")






# #Transformar texto en lista
# texto = 'Don Quijote de la Mancha es una novela escrita por el español Miguel de Cervantes Saavedra'
# texto_list = texto.split(' ')
# print(texto_list)







# #unir varios iterables para usarlos con ZIP
# prefijo = ['La','El','La','El']
# frutas = ['manzana', 'platano','frutilla','tomate']
# colores = ['verde','amarillo','roja','rojo']

# for pref, frut, color in zip(prefijo, frutas, colores):
#     print(f'{pref} {frut} es de color {color}')






# def aleatorio(valor):
#     p = print
#     import random
#     lista = [1,2,3,4,5,6,7,8,9,0]
#     random.shuffle(lista)

#     for k, elemento in enumerate(lista):
#         if elemento == valor:
#             print(f'Encontrado en la posición {k}')
#             break
#         else:
#             p('No encotrado')
# aleatorio(3)







# #Tablas de multiplicar
# for numero1 in range(1, 10):
#     print('\n')
#     print(f'Tabla del {numero1}:')
#     for numero2 in range(10):
#         print(f'{numero1} x {numero2} = {numero1*numero2}')




# #Transforma una lista en string
# a = ', '.join(['uno','dos','tres','cuatro'])
# print(type(a))
# print(a)





# #Convertir una lista en diccionario
# lista = [('a', 25), ('b', 31), ('c', 'hello'), ('e', 'feo'), ('f', 'malo'), ('g', 'bueno')]
# new_lista = dict(lista)
# print(new_lista) # diccionario





# #crear una lista enumerada a partir de un la lisrta
# disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo', 'Jamón','Carne','Tocino','Queso']
# string_pregunta = [str(idx + 1) + '. ' + ingre for idx, ingre in enumerate(disponibles)]
# string_pregunta = '\n'.join(string_pregunta)
# string_pregunta += '\n'





# #Elección con not in
# opciones = [1,2,3,4,5,6,7,8,9,0]
# eleccion = int(input('Ingrese una opción: '))

# while eleccion not in opciones:
#     eleccion = int(input('Opción no válida, ingrese una de las opciones válidas: '))
# print(f'El numero {eleccion} está en la lista')
