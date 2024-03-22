'''
Necesito preguntarle al usuario como se llama en
la vida real, y en Github

<li class="nav-item">
    <a class="nav-link" href="https://github.com/USUARIO">NOMBRE_USUARIO</a>
</li>
'''

nombre = input('Hola, ¿cómo te llamas? ')
github = input('¿Cuál es tu nombre de usuario en Github? ')
#enlace = '<li class="nav-item"> <a class="nav-link" href="https://github.com/' + github + '">' + nombre + '</a></li>'

#Interpolando con string multilinea
enlace = f'''
<li class="nav-item">
    <a class="nav-link" href="https://github.com/{github}">{nombre}</a>
</li>
'''
print(enlace)





#Otro ejemplo
texto = input('¿Qué texto quiere que tenga el botón?: \n')
clase = input('¿Qué clase quiere que tenga el botón?: \n')

boton = f'<buton type="button" class="btn btn-{clase}">{texto}</button>'
print(boton)