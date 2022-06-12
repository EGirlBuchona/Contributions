# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Generar Resúmenes de Texto en Python

import re
from collections import Counter

def procesar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()

        palabras = re.findall(r'\b\w+\b', texto.lower())
        oraciones = re.split(r'[.!?]', texto)
        parrafos = texto.split('\n\n')

        resumen = {
            "Número de palabras": len(palabras),
            "Número de oraciones": len([oracion for oracion in oraciones if oracion.strip()]),
            "Número de párrafos": len([parrafo for parrafo in parrafos if parrafo.strip()]),
            "Palabras más comunes": Counter(palabras).most_common(5)
        }

        print("\nResumen del archivo de texto:")
        for clave, valor in resumen.items():
            print(f"{clave}: {valor}")

    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    ruta = input("Ingrese la ruta del archivo de texto: ")
    procesar_archivo(ruta)
