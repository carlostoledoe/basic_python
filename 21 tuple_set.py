# dias = ('lun', 'mar', 'mier') #la tupla es innmutable
# dias[2] = 'jue'  #TypeError: 'tuple' object does not support item assignment (no se puede mutar una tupla)

# dias = tuple(list(dias) + ['jue'])

# dias  += ('jojo', 'jeje') #no modifica, sino que crea una y la asigna la reasigna a dias
# print(dias)








# votacion = ['Trump', 'Biden', 'Biden', 'Putin', 'Biden', 'Trump', 'Biden', 'Pedro Pascal', 'Pikachu', 'Trump', 'Putin']
# #votacion = list(set(votacion))
# votacion.sort()
# print(votacion) #me dice cuales son las opciones

# '''
# Quiero armar algo así:
# {
#     'Trump': 45,
#     'Biden': 40
#     ...
# }
# '''

# resultados = {}
# for voto in votacion:
#     if voto in resultados.keys():
#         resultados[voto] += 1
#     else:
#         resultados[voto] = 1
# print(resultados)





