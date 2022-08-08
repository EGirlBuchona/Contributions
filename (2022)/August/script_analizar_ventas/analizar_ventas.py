# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Análisis de Ventas en Python

import csv
from collections import Counter

def analizar_ventas(csv_file):
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            total_ventas = 0
            productos = []
            
            for row in reader:
                total_ventas += float(row["Total"])
                productos.append(row["Producto"])

            promedio_ventas = total_ventas / len(productos)
            producto_mas_vendido = Counter(productos).most_common(1)[0]

            print(f"Total de Ventas: ${total_ventas:.2f}")
            print(f"Promedio de Ventas: ${promedio_ventas:.2f}")
            print(f"Producto Más Vendido: {producto_mas_vendido[0]} ({producto_mas_vendido[1]} unidades)")

    except Exception as e:
        print(f"Error al analizar las ventas: {e}")

if __name__ == "__main__":
    print("Análisis de Ventas")
    archivo_csv = "ventas.csv"
    analizar_ventas(archivo_csv)
