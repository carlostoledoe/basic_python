preguntas = [
    '¿Qué opina de eso?',
    '¿Votaría por Mario para CORE',
    '¿Sómos el curso favorito del profe?'
]
respuestas = []
dicc_respuestas = {
        '1': 'Muy de acuerdo',
        '2': 'En desacuerdo',
        '3': 'Ni acuerdo ni en desacuerdo',
        '4': 'De acuerdo',
        '5': 'Muy de acuerdo'
}

def preguntar(pregunta):
    print(pregunta)
    opciones = '''
        Seleccione una de las siguientes:
        1. Muy de acuerdo
        2. En desacuerdo
        3. Ni acuerdo ni en desacuerdo
        4. De acuerdo
        5. Muy de acuerdo
    '''
    eleccion = input(opciones)
    respuesta = dicc_respuestas.get(eleccion, 'N.S.N.R')
    respuestas.append({
        'pregunta': pregunta,
        'respuesa': respuesta
    })

def main():
    for pregunta in preguntas:
        preguntar(pregunta)
    print(respuestas)

main()