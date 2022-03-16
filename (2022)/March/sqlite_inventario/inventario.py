# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Sistema de Inventario con SQLite en Python

import sqlite3

def conectar():
    return sqlite3.connect('inventario.db')

def crear_tabla():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        ''')
        conn.commit()

def agregar_producto(nombre, cantidad, precio):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)', (nombre, cantidad, precio))
        conn.commit()

def mostrar_inventario():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        print("Inventario:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: ${producto[3]:.2f}")

def actualizar_producto(id_producto, cantidad, precio):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?', (cantidad, precio, id_producto))
        conn.commit()

def eliminar_producto(id_producto):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
        conn.commit()

def menu():
    crear_tabla()
    while True:
        print("\nSistema de Inventario")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(nombre, cantidad, precio)
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
