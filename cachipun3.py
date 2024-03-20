import random

# Diccionario que contiene las reglas del juego
reglas = {
    'piedra': {'piedra': 'Empate', 'papel': 'Perdiste!! Papel contra Piedra', 'tijera': 'Ganaste!!: Piedra contra Tijera'},
    'papel': {'piedra': 'Ganaste!!: papel contra piedra', 'papel': 'Empate', 'tijera': 'Perdiste!! Papel contra Tijera'},
    'tijera': {'piedra': 'Perdiste!! tijera contra piedra', 'papel': 'Ganaste!!: tijera contra papel', 'tijera': 'Empate'}
}

while True:
    jugada_usuario = input('Escriba su jugada:\n- Piedra \n- Papel \n- Tijera \n').lower()
    
    if jugada_usuario in reglas:
        break
    else:
        print('Jugada inválida. Por favor, elija entre Piedra, Papel o Tijera.')

jugada_cpu = random.choice(list(reglas.keys()))

print(f'Tú jugaste {jugada_usuario}')
print(f'Computadora eligió {jugada_cpu}')

# Determinar el resultado del juego usando el diccionario de reglas
print(reglas[jugada_usuario][jugada_cpu])
