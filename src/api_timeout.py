import requests

def buscar_usuario(id):

    response = requests.get(f"https://api.exemplo.com/user/{id}")

    # BUG: não trata timeout
    return response.json()
