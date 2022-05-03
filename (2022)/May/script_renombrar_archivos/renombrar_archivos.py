# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Renombrar Archivos en Python

import os

def renombrar_archivos(directorio, patron, nuevo_nombre):
    try:
        archivos = os.listdir(directorio)
        contador = 1
        for archivo in archivos:
            if patron in archivo:
                extension = os.path.splitext(archivo)[1]
                nuevo_archivo = f"{nuevo_nombre}_{contador}{extension}"
                ruta_vieja = os.path.join(directorio, archivo)
                ruta_nueva = os.path.join(directorio, nuevo_archivo)
                os.rename(ruta_vieja, ruta_nueva)
                print(f"Renombrado: {archivo} a {nuevo_archivo}")
                contador += 1
    except FileNotFoundError:
        print("El directorio especificado no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    directorio = input("Ingrese el directorio donde están los archivos: ")
    patron = input("Ingrese el patrón a buscar en los nombres de archivo: ")
    nuevo_nombre = input("Ingrese el nuevo nombre base para los archivos: ")
    renombrar_archivos(directorio, patron, nuevo_nombre)
