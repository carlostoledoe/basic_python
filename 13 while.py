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







