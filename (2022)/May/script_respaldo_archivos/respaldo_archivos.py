# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Respaldo de Archivos en Python

import os
import shutil
from datetime import datetime

def realizar_respaldo(directorio_origen, directorio_destino):
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    directorio_respaldo = os.path.join(directorio_destino, f"respaldo_{fecha_actual}")
    
    try:
        shutil.copytree(directorio_origen, directorio_respaldo)
        print(f"Respaldo completado exitosamente en: {directorio_respaldo}")
    except Exception as e:
        print(f"Ocurrió un error al realizar el respaldo: {e}")

if __name__ == "__main__":
    directorio_origen = input("Ingrese la ruta de la carpeta a respaldar: ")
    directorio_destino = input("Ingrese la ruta donde se almacenará el respaldo: ")
    realizar_respaldo(directorio_origen, directorio_destino)
