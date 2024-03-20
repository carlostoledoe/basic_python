# '''
# Este programa muy sencillo, permite saludar al usuario por su nombre
# '''

# #1. Pido al usuario que ingrese su nombre
# nombre = input('Por favor ingrese su nombre: ')

# #2. Fabrico la varibale saludo
# saludo = 'Hola ' + nombre + ', gusto conocerte. ¿Qué edad tienes?'
# print(saludo)

# #3. Pregunto edad
# edad = int(input())
# age = str(edad)

# #4. Respuesta total
# print('Hola ' + nombre + ', tu edad es ' + age)




#Pido que ingrese su edad 
edad = input('Por favor, ingrese su edad: ')
edad = int(edad)

#Evalúo
if edad < 18:
	print ('Usted no puede votar')
elif edad < 65:
	print('Usted si puede votar')
elif edad < 120:
	print('Usted votó por Ohiggins')
else: #No se puede agregar despues del else
	print('Usted si puede votar y se puede saltar la fila')