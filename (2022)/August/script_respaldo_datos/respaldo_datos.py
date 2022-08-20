# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Respaldo de Datos en Python

import os
import shutil
from datetime import datetime

def respaldar_datos(origen, destino):
    try:
        # Crear carpeta de respaldo si no existe
        if not os.path.exists(destino):
            os.makedirs(destino)

        # Obtener la lista de archivos en el directorio origen
        archivos = os.listdir(origen)
        for archivo in archivos:
            ruta_origen = os.path.join(origen, archivo)
            ruta_destino = os.path.join(destino, archivo)

            # Copiar archivo si es un archivo normal
            if os.path.isfile(ruta_origen):
                shutil.copy2(ruta_origen, ruta_destino)
                print(f"Respaldo completado para: {archivo}")

        print("\nRespaldo completado exitosamente.")
    except Exception as e:
        print(f"Error al realizar el respaldo: {e}")

if __name__ == "__main__":
    print("Script para Respaldo de Datos")
    origen = input("Ingrese la ruta de la carpeta de origen: ")
    destino = input("Ingrese la ruta de la carpeta de respaldo: ")

    # Agregar marca de tiempo al directorio de respaldo
    destino = os.path.join(destino, datetime.now().strftime("%Y%m%d_%H%M%S"))
    respaldar_datos(origen, destino)
