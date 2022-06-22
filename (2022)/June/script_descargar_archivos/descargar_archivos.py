# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Descargar Archivos en Python

import os
import requests

def descargar_archivo(url, carpeta_destino):
    try:
        respuesta = requests.get(url, stream=True)
        respuesta.raise_for_status()
        
        nombre_archivo = os.path.join(carpeta_destino, url.split("/")[-1])
        
        with open(nombre_archivo, "wb") as archivo:
            for chunk in respuesta.iter_content(chunk_size=8192):
                archivo.write(chunk)
        
        print(f"Archivo descargado: {nombre_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {url}: {e}")

def main():
    lista_urls = input("Ingrese la ruta del archivo con las URLs: ").strip()
    carpeta_destino = input("Ingrese la carpeta de destino: ").strip()

    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"Carpeta creada: {carpeta_destino}")
    
    try:
        with open(lista_urls, "r") as archivo:
            urls = archivo.readlines()
        
        for url in urls:
            url = url.strip()
            if url:
                descargar_archivo(url, carpeta_destino)
    except FileNotFoundError:
        print("El archivo con las URLs no fue encontrado. Verifique la ruta.")

if __name__ == "__main__":
    main()
