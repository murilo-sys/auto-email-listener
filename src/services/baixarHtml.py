import requests


def baixarHtml(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }  # Evita que alguns servidores bloqueiem a requisição

    # Faz a requisição HTTP
    response = requests.get(url, headers=headers)

    # Verifica se a conexão foi bem-sucedida (status 200)
    if response.status_code == 200:

        # Define a codificação para lidar corretamente com acentos
        response.encoding = response.apparent_encoding

        # Retorna o texto da consulta
        return response.text

    else:

        return
