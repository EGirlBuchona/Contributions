# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Comparar Archivos en Python

import difflib

def comparar_archivos(archivo1, archivo2):
    try:
        with open(archivo1, 'r', encoding='utf-8') as file1, open(archivo2, 'r', encoding='utf-8') as file2:
            contenido1 = file1.readlines()
            contenido2 = file2.readlines()
        
        diferencias = difflib.unified_diff(contenido1, contenido2, lineterm='')
        print("\n".join(diferencias))
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    print("Script para Comparar Archivos")
    archivo1 = input("Ingrese la ruta del primer archivo: ").strip()
    archivo2 = input("Ingrese la ruta del segundo archivo: ").strip()
    comparar_archivos(archivo1, archivo2)
