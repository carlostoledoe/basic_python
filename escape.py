from math import sqrt

#Solicitud de dataos
print('-'*34)
print ('Calculadora de velocidad de escape')
print('-'*34)
r = float(input('Ingrese el radio en Kilómetros: '))
g = float(input('Ingrese la constante g: '))

#Cálculos
ve = sqrt(2 * g * (r * 1000))

#Presentación
print(f'La velocidad de Escape es {round(ve, 2)} [m/s]')
