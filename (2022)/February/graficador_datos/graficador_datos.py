# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Graficador de Datos en Python

import matplotlib.pyplot as plt
import csv

def leer_datos_csv(nombre_archivo):
    x = []
    y = []
    try:
        with open(nombre_archivo, 'r') as archivo_csv:
            lector = csv.reader(archivo_csv)
            next(lector)  # Saltar encabezado
            for fila in lector:
                x.append(fila[0])
                y.append(float(fila[1]))
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
    except ValueError:
        print("Error: Los datos del archivo no son válidos.")
    return x, y

def graficar_datos(x, y, titulo="Gráfico de Datos", xlabel="Eje X", ylabel="Eje Y"):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    nombre_archivo = "datos.csv"
    x, y = leer_datos_csv(nombre_archivo)
    if x and y:
        graficar_datos(x, y, titulo="Ejemplo de Gráfico", xlabel="Tiempo", ylabel="Valor")
