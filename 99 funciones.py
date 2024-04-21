# Calular año, semana y día
def calculadora_dias(dias):
    anos = dias // 365
    semanas = (dias % 365) // 7
    dias_restantes = (dias % 365) % 7
    return anos, semanas, dias_restantes







#consulta básica API
import requests
import json

def request_get(url): 
    return json.loads(requests.get(url).text) 








# Validar opciones (elección en una lista)
def validate(lista, eleccion):
    while eleccion not in lista:
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
    return eleccion # Retorna la elección

def esta_presente(elemento, lista): 
    return elemento in lista #Retorna true or false







#Valida numero mayor a cero y da True o False
def validar_numero(numero: int):
    return numero > 0