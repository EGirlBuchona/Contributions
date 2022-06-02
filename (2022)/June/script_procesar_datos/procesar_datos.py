# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Procesar Datos en Python

import pandas as pd

def procesar_archivo_csv(ruta_archivo):
    try:
        datos = pd.read_csv(ruta_archivo)
        resumen = {
            "Número de filas": datos.shape[0],
            "Número de columnas": datos.shape[1],
            "Columnas": list(datos.columns),
            "Tipos de datos": datos.dtypes.to_dict(),
            "Estadísticas descriptivas": datos.describe().to_dict()
        }
        
        print("Resumen del archivo CSV:")
        for clave, valor in resumen.items():
            print(f"{clave}: {valor}")
        
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo CSV a procesar: ")
    procesar_archivo_csv(ruta_archivo)
