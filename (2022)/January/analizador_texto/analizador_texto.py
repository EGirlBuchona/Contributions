# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Analizador de Texto en Python

import re

def analizar_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            palabras = texto.split()
            caracteres = len(texto)
            frases = re.split(r'[.!?]', texto)
            frases = [frase for frase in frases if frase.strip()]

            print(f"Análisis del archivo: {nombre_archivo}")
            print(f"Número de palabras: {len(palabras)}")
            print(f"Número de caracteres: {caracteres}")
            print(f"Número de frases: {len(frases)}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo a analizar: ")
    analizar_texto(nombre_archivo)
