import math

proteina = float(input("Ingrese los gr de proteínas: \n"))
carbohidratos = float(input("Ingrese los gr de carbohidratos: \n"))
grasa = float(input("Ingrese los gramos de grasas: \n"))
alcohol = float(input("Ingrese los gramos de alcohol ingenido: \n"))

# calorias = 4 * (proteina + carbohidratos) + 9 * grasa
calorias = 4 * (proteina + carbohidratos) + 9 * grasa + 7 * alcohol

print(f'Las calorías totales del producto son: {calorias}')
print(f'Las calorías totales del producto son: {math.ceil(calorias)}')