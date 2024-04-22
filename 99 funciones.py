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
def validate(lista: str, eleccion: list):
    while eleccion not in lista:
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
    return eleccion # Retorna la elección

def esta_presente(elemento: str, lista: list): 
    return elemento in lista #Retorna true or false







#Valida numero mayor a cero y da True o False
def validar_numero(numero: int):
    return numero > 0








#Valida que el texto solo tenga letras, retorna True o false
def validar_texto(texto: str):
    return texto.isalpha()

def validar_texto(texto: str):
        if not texto.isalpha():
            raise ValueError("El nombre debe contener solo letras")
        return texto











# Escribir dentro de la instancia de una lista
class Persona:
    pass
m = Persona()

ingresados = []

if m in ingresados: # Si la instancia m está en ingresado
    indice = ingresados.index(m) # obtiene el indice (ubicación)
    ingresados[indice] += m #suma (lo definido en += ) a la instancia del indice