import requests
import json

#Consulta la api y la convierte en json
def request_get(url): 
    return json.loads(requests.get(url).text) 


# Crea un html a partir del template
def crear_html(template):
    with open('index.html', 'w') as f:
        return f.write(template)



# Url a consultar
url =  'https://aves.ninjas.cl/api/birds'
photos = request_get(url)



# Armado de la Card
card = ''
for photo in photos:
    card += f'''<div class="col-3">
                    <div class="card mt-3" style="width: 12rem;">
                        <img src="{photo['images']['thumb']}" class="card-img-top" alt="{photo['name']['english']}">
                        <div class="card-body">
                            <h5 class="card-title">{photo['name']['spanish']}</h5>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item"><strong>En ingles:</strong><em> {photo['name']['english']}</em></li>
                            <li class="list-group-item"><strong>En latín:</strong><em> {photo['name']['latin']}</em></li>
                        </ul>
                        <div class="card-body">
                            <a href="{photo['images']['full']}" class="card-link">Ver en grande</a>
                        </div>
                    </div>
                </div>'''


# Template HTML
html_template = f'''<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Aves Chile</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <h1>Aves Chile</h1>
            <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Enim aspernatur perspiciatis cumque aliquam alias perferendis voluptates. Sunt fuga inventore, nesciunt dolor sapiente, ab dignissimos voluptas unde eligendi asperiores, ad animi!</p>
            <div class="row">
                {card}
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
</html>'''

crear_html(html_template)