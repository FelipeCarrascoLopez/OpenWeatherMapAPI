# app.py (backend)

import requests
from flask import Flask, render_template
import json

app = Flask(__name__)

def obtener_informacion_10_paises():
    url = 'https://restcountries.com/v3.1/all'
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Manejar errores HTTP

        datos_paises = respuesta.json()[:10]  # Obtener solo los primeros 10 países

        # Imprimir la respuesta completa en formato JSON
        print("Respuesta completa:")
        print(json.dumps(datos_paises, indent=2))  # Imprimir en formato JSON con sangría

        return datos_paises

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

@app.route('/')
def index():
    # Ejemplo de uso
    informacion_paises = obtener_informacion_10_paises()
    
    return render_template('index.html', countries_data=informacion_paises)

if __name__ == '__main__':
    app.run(debug=True)
