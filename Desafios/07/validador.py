
def validate(opciones, eleccion):
        if eleccion not in opciones:
            print('Opción no válida, ingrese una de las opciones válidas: ')
            for i in opciones:
                print(f'{i}')
            eleccion = input('> ')
            validate(opciones, eleccion)
        return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
