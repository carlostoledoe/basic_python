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





