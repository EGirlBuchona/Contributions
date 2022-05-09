# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Análisis de Logs en Python

import re
from collections import Counter

def analizar_logs(ruta_log):
    try:
        with open(ruta_log, "r") as archivo:
            logs = archivo.readlines()

        errores = [linea for linea in logs if "ERROR" in linea]
        accesos = [linea for linea in logs if "ACCESO" in linea]

        reporte = {
            "total_lineas": len(logs),
            "total_errores": len(errores),
            "total_accesos": len(accesos),
            "errores_frecuentes": Counter([re.search(r"ERROR.*", linea).group() for linea in errores])
        }

        print("\nReporte de Logs:")
        for clave, valor in reporte.items():
            print(f"{clave}: {valor}")

    except FileNotFoundError:
        print("El archivo de log especificado no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    ruta_log = input("Ingrese la ruta del archivo de logs: ")
    analizar_logs(ruta_log)
