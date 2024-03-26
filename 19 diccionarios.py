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