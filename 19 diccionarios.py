# def mostrar_semana():
#     #semana es una variable del tipo diccionario
#     semana = {
#         'lunes': 2,
#         'martes': 2,
#         'miercoles': 4,
#         'jueves': 4,
#         'viernes': 2
#     }
#     print(semana['miercoles'])

#     for llave, valor in semana.items(): #items lo tranforman en interable, ya que el diccionario no es iterable
#         if valor == 2:
#             print(f'el dia {llave} fue un dia CORTO')
#         else:
#             print(f'el dia {llave} fue un dia LARGO')
# mostrar_semana()






# def mostrar_personajes():
#     nombre = input('Ingrse el nombre de un personaje: ')
#     planeta = input('Ingrese el planeta de un personaje: ')
#     poder = input('Ingrse el la habilidad del personaje: ')
#     moral = input('Ingresar si es bueno o malo: ')

#     personaje = {
#         'nombre': nombre,
#         'planeta': planeta,
#         'poder': poder,
#         'es_bueno': True if moral == 'bueno' else False
#     }
#     for llave, valor in personaje.items(): #llave es el primero y valor es lo segundo
#         print(f'El valor de {llave} es {valor}')
# mostrar_personajes()






# destinos = [
#     {
#         'nombre': 'Argentina',
#         'prefijo': 54,
#         'cuidades': ['BS AS', 'Cordova', 'Mendoza', 'Jumin']
#     },
#     {
#         'nombre': 'Suecia',
#         'prefijo': 47,
#         'ciudades': ['Estocolmo', 'Gotermburno', 'Malmo', 'Kiruna']
#     }
# ]
# print(destinos[1]['ciudades'][2])







# #llave vs valor (para la llave mejor usar string)
# perro = {
#     'raza': 'cocker',
#     'nombre': 'Joe',
#     'edad': 8
# }
# for llave, valor in perro.items():
#     print(f'La llave {llave} tiene el valor {valor}') #iterar el diccionario

# print(perro['raza']) #Ver el valor de la llave raza (coker)
# perro['nombre'] = 'Rocky' #Cambio de nombre, se sobrescribe
# perro['dueño'] = 'José' #agregar una nueva llave y valor . La llave debe ser única
# print(perro)

# del perro['dueño'] #Elimina la clave
# print(perro)

# datos_perro = {'talla': 'mediano', 'vacunas': ['octuple', 'antirrabica']} #diccionario adicional

# perro.update(datos_perro) #Es como concatenar. Puede pidar los datos
# print(perro)









# auto = {
#     'marca': 'mazda',
#     'modelo': '3',
#     'motor': 2000
# }

# auto.update({
#     'color': 'rojo',
#     '4x4': False
# })

# print(auto)






# #Un diccionario
# perro = {
#     'raza': 'cocker',
#     'nombre': 'Joe',
#     'edad': 8
# }

# #Agregando llaves
# perro['tiene dueno'] = True
# perro['vacuna'] = ['Atirrabica', 'Octuple']

# print(perro)

# #Iterando por llave
# for llave in perro.keys():
#     print(llave)

# #Iterando por values
# for valor in perro.values():
#     print(valor)

# #Iterando por ambos (lista de pares)
# for k, v in perro.items():
#     print(f'El valor de la llave {k} es:')
#     print(v)






#generador range(0, 100, 1)
#Solo se materializan cuando se acceden a ellas




# print(perro['raza'])
# print(perro.get('tamaño', 'no definido')) #para errores.

# print(perro)












# lista = [3, 4, 5.3, 10, 21, 3.1]
# print(min(lista))
# print(sum(lista))
# print(sum(lista) /len(lista))




# #Convertir un diccinario en una lista (array):
# nueva = list({'raza': 'cocker', 'nombre': 'Joe', 'edad': 8}.items())
# print(nueva)







# #Iterando
# letras = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five'
# }
# for k, v in letras.items():
#     print(f'{k} es en ingles {v}')







# claves = ['nombre','apellido','edad','altura']
# valores = ['Juan','Pérez', 33, 1.75]
# print({k:v for k,v in zip(claves, valores)})






# alternativas = ['nombre','apellido','edad','altura']
# letras = ['A','B','C','D']
# for l, a in zip(letras, alternativas):
#     print(f'{l}. {a}')





# #Acceder al la lista y al diccionario
# lista = [25, 31, "hola"]
# print(lista[2]) # Se accede por la posición

# diccionario = {
#     "a": 25,
#     "b": 31,
#     "c": "hello",
#     "c": "chao" # Cuando la clave está duplicada, toma el útimo valor
# }
# print(diccionario['c']) # Se accede por la clave





# #Agregando y modificando elementos
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': "hello",
# }
# diccionario['d'] = 'Chao' #Se agrega d
# diccionario['c'] = 'Hola' #Modifica c
# del diccionario['a']  #Elimino la clave a sin mostrarlo
# print(diccionario.pop('b')) #Muestro el valor eliminado
# diccionario_b = {
#     'e': 'feo',
#     'f': 'malo',
#     'g': 'bueno'
# }
# diccionario.update(diccionario_b) #Uniendo diccionarios
# print(diccionario)





# #Métodos
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': "hello",
#     'e': 'feo',
#     'f': 'malo',
#     'g': 'bueno'
# }
# print(diccionario.keys()) #Muestra una LISTA con solo las llaves
# print(diccionario.values()) #Muestra una LISTA con solo las llaves
# print(diccionario.items()) #Muestra una LISTA con pares clave-valor
# lista_diccionario = list(diccionario.items()) #Transforma en lista
# print(lista_diccionario)





# #Get
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': "hello",
#     'e': 'feo',
#     'f': 'malo',
#     'g': 'bueno'
# }
# consulta = input('Ingrese un dato: ')
# print(diccionario.get(f'{consulta}', 'No se encuentra')) #Muestra el valor, sino, No se encuentra






# #Convertir un diccionario en una lista
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': "hello",
#     'e': 'feo',
#     'f': 'malo',
#     'g': 'bueno'
# }
# new_dicc = list(diccionario.items()) # Cada par (clave, valor) será una tupla:
# print(new_dicc)






# #Convertir una lista en diccionario
# lista = [('a', 25), ('b', 31), ('c', 'hello'), ('e', 'feo'), ('f', 'malo'), ('g', 'bueno')]
# new_lista = dict(lista)
# print(new_lista) # diccionario






# #Caso de no elegir una clave en opciones
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': 'hello',
#     'd': 'feo',
#     'e': 'malo',
#     'f': 'bueno'
# }
# print('''
#     Elija una opción:
#     a: 25
#     b: 31
#     c: hello
#     d: feo
#     e: malo
#     f: bueno''')
# opcion = input('> ')
# respuesta = diccionario.get(opcion, 'otra cosa que no está')
# print(f'Su respuesta fue: {respuesta}')






# # Elegir un valor random de una clave elegida
# import random

# opciones = {
#     'bas':  [1,2,3],
#     'inter': [4,5,6],
#     'avan': [7,8,9]
# }

# eleccion = input('Elija una opción (bas, inter, avan): ')
# num = random.choice(opciones[eleccion])
# print(num)











# # Sacar los datos de una lista que están en diccionario
# import json

# usuarios = [
# {"nombre": "Page", "apellido": "Stappard", "email": "pstappard0@java.com", "genero": "Bigender"},
# {"nombre": "Alli", "apellido": "Truckell", "email": "atruckell1@lulu.com", "genero": "Agender"},
# {"nombre": "Nissy", "apellido": "Dell Casa", "email": "ndellcasa2@godaddy.com", "genero": "Female"}
# ]

# for usuario in usuarios:
#     # for k, v in usuario.items():
#     #     if k == 'nombre':
#     #         nombre = v
#     #     if k == 'apellido':
#     #         apellido = v
#     #     if k == 'email':
#     #         email = v
#     #     if k == 'genero':
#     #         genero = v
    
#     nombre = usuario.get('nombre')
#     apellido = usuario.get('apellido')
#     email = usuario.get('email')
#     genero = usuario.get('genero')
    
#     print(f'name: {nombre} || lastname: {apellido} || email: {email} || genre: {genero} ')