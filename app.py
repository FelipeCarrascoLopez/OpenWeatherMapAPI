import requests
import json  # Agregar esta línea

def obtener_informacion_pais(codigo_pais):
    url = f'https://restcountries.com/v3.1/alpha/{codigo_pais}'
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Manejar errores HTTP

        datos_pais = respuesta.json()

        # Imprimir la respuesta completa en formato JSON
        print("Respuesta completa:")
        print(json.dumps(datos_pais, indent=2))  # Imprimir en formato JSON con sangría

        # Continuar con el procesamiento de datos
        # ...

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

# Ejemplo de uso
codigo_pais = 'USA'  # Puedes cambiar esto a cualquier código de país que desees
informacion_pais = obtener_informacion_pais(codigo_pais)
