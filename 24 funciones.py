def buenos_modales(nombre = 'Anonimo'): #Valor por defecto cuando está sin argumento (nombre = parámetro, entrada)
    hola = 'Buenos dias ' + nombre
    chao = 'Nos vemos, ' + nombre
    return hola, chao # es una tupla

# parámetro es cuando defino la función y el argumento es lo que le paso cuando invoco a esta

#Desempaquetar la tupla
saludo, adios = buenos_modales('Cristian') 
'''
palabras = buenos_modales('Matias')
saludo = palabras[0]
adios = palabras[1]
'''
print(saludo)
print(adios)

