# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gráfico de Datos desde CSV

import matplotlib.pyplot as plt
import csv

def leer_datos_csv(archivo_csv):
    datos = []
    with open(archivo_csv, "r") as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector)  # Leer encabezado
        for fila in lector:
            datos.append([float(valor) for valor in fila])
    return encabezado, datos

def graficar_datos(encabezado, datos):
    plt.figure(figsize=(10, 6))
    for i in range(1, len(encabezado)):
        valores = [fila[i] for fila in datos]
        plt.plot(valores, label=encabezado[i])

    plt.xlabel("Índice")
    plt.ylabel("Valores")
    plt.title("Gráfico de Datos desde CSV")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    archivo_csv = input("Ingrese la ruta del archivo CSV: ")
    encabezado, datos = leer_datos_csv(archivo_csv)
    graficar_datos(encabezado, datos)
