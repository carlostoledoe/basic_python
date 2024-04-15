#Valor no valido o error
secreto = 3
while True:
    try:
        numero = int(input('Adivina el número: '))
        if numero == secreto:
            break
        else:
            print('> Numero erroneo. Itenta de nuevo.')
    except ValueError: 
        print('> Eso no es un número. Intenta de nuevo.')
print ('Correcto!!')
