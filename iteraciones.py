# import getpass

# def validarPassword(password): #Acoplar funciones para hacer más fácil revisar, arreglar
#     #Validamos que sea de largo al menos sea 6
#     if len(password) < 6:
#         print('Su contraseña debe contener al menos 6 caracteres')
#         return False
#     elif password == '12345678':
#         print('Este password es muy sencillo. Elija otro')
#         return False
#     elif password == '87654321':
#         print('Este password es muy sencillo. Elija otro')
#         return False
#     elif ("'" in password) or ("*" in password) or ("-" in password):
#         print("No puede usar especial dentro de su password")
#         return False
#     else:
#         print('Contraseña correcta')
#         return True

# def main():
# # esCorrecta = False
# # while esCorrecta != True:
#     while True:
#         # 1. Le pido la nueva contraseña la usuario
#         password = getpass.getpass('Ingrese una contraseña: ')
#         print(f'Password ingresado: {password}')
#         # Valido la contraseña con la función "validarPassword"
#         esCorrecta = validarPassword(password) 
#         # Si la contraseña es incorretca, repite el ciclo. Si está bien, salgo del ciclo con break
#         if esCorrecta:
#             break # Salir del ciclo
#     print('Bienvenido!') # Fuera del ciclo
# main()








# numero = None
# while numero is None:
#     try:
#         numero = int(input("Ingresa un número: "))
#     except ValueError:
#         print("Eso no es un número válido.")



# import sys #Permite ingresar datos desde la consonla
# def sigma():
#     numero = int(sys.argv[1]) #Indica qué atributo tomará
#     i = 1 #inicar iterador
#     suma = 0
#     while i <= numero: #condición
#         suma += i
#         i += 1 #Incremento
#     print(suma) 
# sigma()







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







import sys
def buscar():
    buscada = sys.argv[1]
    palabras = ['En', 'un', 'lugar', 'de', 'la', 'Mancha,', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme,', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero,', 'adarga', 'antigua,', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']

    la_encontramos = False #Flag o bandera (is_present)

    for pos, palabra in enumerate(palabras):
        if palabra == buscada:
            frase = f'La palabra {buscada} está en la posción {pos}'
            print(frase)
            la_encontramos = True
            break #para que no siga iterando y así ahorrar recursos
    if not la_encontramos: # if la_encontramos == False:
        print(f'La palabra {buscada} no fue encontrada')
buscar()




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







