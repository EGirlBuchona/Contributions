# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Descargar Contenido Web

import requests
import os

def descargar_contenido(urls, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    for i, url in enumerate(urls):
        try:
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                archivo_nombre = os.path.join(carpeta_destino, f"contenido_{i + 1}.html")
                with open(archivo_nombre, 'w', encoding='utf-8') as archivo:
                    archivo.write(respuesta.text)
                print(f"Contenido de {url} descargado y guardado en {archivo_nombre}")
            else:
                print(f"No se pudo descargar contenido de {url}. Código de estado: {respuesta.status_code}")
        except Exception as e:
            print(f"Error al intentar descargar {url}: {e}")

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://wikipedia.org",
        "https://github.com"
    ]
    carpeta_destino = "contenidos_descargados"
    descargar_contenido(urls, carpeta_destino)
