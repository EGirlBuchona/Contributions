# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script de Limpieza de Directorios

import os
import time

def limpiar_directorio(directorio, dias):
    tiempo_actual = time.time()
    tiempo_limite = tiempo_actual - (dias * 86400)  # Días en segundos

    for carpeta_raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_raiz, archivo)
            tiempo_modificacion = os.path.getmtime(ruta_archivo)

            if tiempo_modificacion < tiempo_limite:
                try:
                    os.remove(ruta_archivo)
                    print(f"Eliminado: {ruta_archivo}")
                except PermissionError:
                    print(f"No se pudo eliminar: {ruta_archivo}")

if __name__ == "__main__":
    directorio = input("Ingrese la ruta del directorio a limpiar: ")
    dias = int(input("Ingrese el número de días para considerar los archivos antiguos: "))
    limpiar_directorio(directorio, dias)
