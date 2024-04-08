# JSON : JavaScript Object Notation
# curl hace solicitudes a una api dese el terminal
# Otra forma es la web Yarc
# Es por Python


# 200 OK: La solicitud ha tenido éxito.
# 201 Created: Se ha creado un nuevo recurso como resultado de la solicitud (por ejemplo, después de una petición PUT).
# 204 No Content: La solicitud se ha completado con éxito, pero la respuesta no tiene contenido (aunque los encabezados pueden ser útiles).
# 400 Bad Request: La solicitud contiene una sintaxis no válida o el servidor no puede cumplirla.
# 401 Unauthorized: El cliente debe proporcionar credenciales de autenticación.
# 404 Not Found: El recurso solicitado no existe en el servidor.
# 500 Internal Server Error: Hubo un error interno en el servidor


# json.loads  para trasnformar de JSON (texto) a un diccionario de Python
# json.dumps  para transformar desde un diccionario Python a JSON (texto)



import requests
import json
import pdb



# # Consulta básica
# url = 'https://reqres.in/api/users'
# response = requests.get(url)
# users_data = json.loads(response.text)
# print(users_data)




# url = 'https://anapioficeandfire.com/api/characters/583'
# response = requests.get(url)
# # print(response.text) # Imprime solo texto, ya que llega como texto
# jon_snow = json.loads(response.text) # Lo transforma en un diccionario
# print('Estos son los apodos de Jon Snow:')
# for apodo in jon_snow['aliases']:
#     print(apodo)







# #Requerimiento simple
# def request_get(url): 
#     return json.loads(requests.get(url).text) 

# url = 'https://reqres.in/api/users'

# users_data = request_get(url)
# print(json.dumps(users_data, indent=4))










# #Posteo
# url = 'https://jsonplaceholder.typicode.com/posts'
# data = {
#     'userID': 1,
#     'title': 'hola',
#     'body': 'Este es mi primer posteo desde Python'
# }
# data = json.dumps(data)
# headers = {
#     'Content-Type': 'application/json'
# }
# response = requests.post(url, headers, data) #Envía la información, post
# print(response)
# print(response.text)
# #pdb.set_trace() #response.status_code // response.text










# def probar_put():
#     url = 'https://jsonplaceholder.typicode.com/posts/20' #Debe incluir la ID
#     data = {
#         'userId': 2,
#         'title': 'Articulo Modificador',
#         'body': 'Este es la corrección'
#     }
#     # data = json.dumps(data)
#     # requests.put(): Esta función acepta un argumento adicional llamado json, que te permite pasar 
#     # directamente un diccionario (o cualquier objeto serializable) como datos. Internamente, 
#     # requests se encargará de convertirlo a JSON antes de enviar la solicitud PUT.

#     response = requests.put(url, json=data) #Put acepta dos argumentos posicionales, no header
#     print(response.status_code)

# if __name__ == '__main__':
#     probar_put()