# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script de Backup Automático en Python

import os
import zipfile
import datetime

def hacer_backup(carpeta_origen, carpeta_destino):
    """Crea un backup en formato ZIP de los archivos en la carpeta de origen."""
    fecha_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_backup = f"backup_{fecha_actual}.zip"
    ruta_backup = os.path.join(carpeta_destino, nombre_backup)

    with zipfile.ZipFile(ruta_backup, "w") as archivo_zip:
        for carpeta_raiz, _, archivos in os.walk(carpeta_origen):
            for archivo in archivos:
                ruta_completa = os.path.join(carpeta_raiz, archivo)
                archivo_zip.write(ruta_completa, os.path.relpath(ruta_completa, carpeta_origen))

    print(f"Backup creado exitosamente en {ruta_backup}")

if __name__ == "__main__":
    carpeta_origen = input("Ingrese la ruta de la carpeta a respaldar: ")
    carpeta_destino = input("Ingrese la ruta de la carpeta de destino: ")
    hacer_backup(carpeta_origen, carpeta_destino)
