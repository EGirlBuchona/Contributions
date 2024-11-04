# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script de Inserción en SQLite en Python

import sqlite3
import csv

def crear_tabla():
    """Crea la tabla de ejemplo si no existe."""
    conexion = sqlite3.connect("mi_base_datos.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER,
            correo TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def insertar_datos(csv_file):
    """Inserta datos desde un archivo CSV a la base de datos."""
    conexion = sqlite3.connect("mi_base_datos.db")
    cursor = conexion.cursor()
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO datos (nombre, edad, correo)
                VALUES (:nombre, :edad, :correo)
            ''', row)
    conexion.commit()
    conexion.close()
    print("Datos insertados exitosamente.")

if __name__ == "__main__":
    crear_tabla()
    insertar_datos("datos.csv")
