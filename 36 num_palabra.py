import sys, math

def num_palabra(num):
  primeros15 = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'cartorce', 'quince']

  if num <= 15:
    return primeros15[num]
  # dieci-algo
  elif num <= 19:
    unidades = num - 10
    return 'dieci' + num_palabra(unidades)
  # veinte
  elif num == 20:
    return 'veinte'
  # veinti-algo
  elif num <= 29:
    unidades = num - 20
    return 'veinti' + num_palabra(unidades)
  # algo y algo
  elif num <= 99:
    decenas = math.floor(num / 10)
    unidades = num - (decenas * 10)
    decenas_palabras = ['', '', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochencha', 'noventa']
    if unidades == 0:
      return decenas_palabras[decenas]
    return decenas_palabras[decenas] + ' y ' + num_palabra(unidades)
  elif num == 100:
    return 'cien'
  # ciento y algo
  elif num <= 199:
    resto = num - 100
    return 'ciento ' + num_palabra(resto)
  
  elif num <= 999:
    centenas_palabras = ['', '', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seisientos', 'setecientos', 'ochocientos', 'novecientos']
    centenas = math.floor( num / 100)
    resto = num - (centenas * 100)
    if resto == 0:
      return centenas_palabras[centenas]
    return centenas_palabras[centenas] + ' ' + num_palabra(resto)
  else:
    return 'no implementado'

print(num_palabra(int(sys.argv[1])))