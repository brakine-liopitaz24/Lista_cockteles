##################################
######## Importar librerias ######
##################################

from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

##################################
######## Inicializar aplicacion ##
##################################

app = Flask(__name__)

##################################
######## Obtener API #############
##################################

# Construir la URL de la API 
url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a'
# Realizar la solicitud GET a la API
respuesta = requests.get(url)

##################################
######## Definir rutas ###########
##################################

@app.route('/', methods=['GET', 'POST'])
def index():
    # Construir la URL de la API 
    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a'
    # Realizar la solicitud GET a la API
    respuesta = requests.get(url)
    data = respuesta.json()

    # Obtén la lista de cócteles
    cocktails = data.get('drinks', [])

    # Renderiza la plantilla HTML con la lista de cócteles
    return render_template('index.html', cocktails=cocktails)

@app.route('/cocktail/<string:id>')
def cocktail_detail(id):
    # Realizar una solicitud a la API para obtener detalles del cóctel específico
    url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}"
    response = requests.get(url)
    data = response.json()
    cocktail = data.get('drinks', [])[0] if data.get('drinks') else None

    # Renderizar la plantilla de detalles del cóctel
    return render_template('cocktail_detail.html', cocktail=cocktail)

##################################
######## Ejecutar app ############
##################################

if __name__ == '__main__':
    app.run(port=5000, debug=True)
