# El float acepta numeros decimales, sino, hay error al ingresarlos
cel = float(input('Por favor, ingrese temperatura en Celsius: ')) 
far = (1.8 * cel) + 32
kel = cel + 273.15
print('La temperatura en Farenheit es: ' + str(far) + ', y en Kelvin es: ' + str(kel))