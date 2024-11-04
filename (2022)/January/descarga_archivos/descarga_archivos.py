# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script de Descarga de Archivos en Python

import requests
import os

def descargar_archivo(url, carpeta_destino):
    """Descarga un archivo desde una URL a la carpeta destino."""
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        
    nombre_archivo = url.split("/")[-1]
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)

    try:
        print(f"Descargando {nombre_archivo} desde {url}...")
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si hubo un error en la descarga

        with open(ruta_archivo, "wb") as archivo:
            archivo.write(respuesta.content)
        print(f"Archivo descargado exitosamente en {ruta_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

if __name__ == "__main__":
    url = input("Ingrese la URL del archivo a descargar: ")
    carpeta_destino = input("Ingrese la carpeta de destino: ")
    descargar_archivo(url, carpeta_destino)
