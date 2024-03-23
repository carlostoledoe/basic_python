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