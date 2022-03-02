# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script de Manejo de Archivos en Python

import os
import shutil

def crear_carpeta_si_no_existe(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def organizar_archivos(ruta_carpeta):
    # Diccionario de tipos de archivos y sus extensiones
    tipos_archivos = {
        "Documentos": [".pdf", ".docx", ".txt"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Música": [".mp3", ".wav"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Otros": []
    }

    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            carpeta_destino = "Otros"

            # Determinar el tipo de archivo
            for tipo, extensiones in tipos_archivos.items():
                if extension in extensiones:
                    carpeta_destino = tipo
                    break

            # Crear la carpeta destino si no existe y mover el archivo
            ruta_destino = os.path.join(ruta_carpeta, carpeta_destino)
            crear_carpeta_si_no_existe(ruta_destino)
            shutil.move(ruta_archivo, os.path.join(ruta_destino, archivo))
            print(f"Moviendo {archivo} a {carpeta_destino}")

if __name__ == "__main__":
    ruta_carpeta = input("Ingrese la ruta de la carpeta a organizar: ")
    organizar_archivos(ruta_carpeta)
    print("Organización completada.")
