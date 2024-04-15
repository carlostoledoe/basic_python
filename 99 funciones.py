# Calular año, semana y día
def calculadora_dias(dias):
    anos = dias // 365
    semanas = (dias % 365) // 7
    dias_restantes = (dias % 365) % 7
    return anos, semanas, dias_restantes







#consulta básica
import requests
import json

def request_get(url): 
    return json.loads(requests.get(url).text) 









