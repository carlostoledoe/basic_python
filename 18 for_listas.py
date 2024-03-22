# lista1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] #Lista por extensión
# lista2 = [num for num in range(0, 20, 2)] #Lista por comprehensión






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






# def crear_enlaces():
#     nombres = ['Home', 'Quienes Somos', 'Contacto']
#     enlaces = ['<a href="#">' + nombre + '</a>' for nombre in nombres]
#     print(enlaces)
# crear_enlaces()





# #Para filtrar
# grande = ['andrea', 'olga', 'armando', 'pedro', 'anastasia', 'orlando']
# grupo = [nombre for nombre in grande if len(nombre) > 5] #los que tiene más de 5 letras
# print(grupo)






# ping = [120, 50, 600, 30, 90, 10, 200, 0, 500]
# resultado = ['Bien' if ping <= 90 else 'mal' for ping in ping]
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







