# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestor de Inventarios con SQLite

import sqlite3

def crear_tabla():
    with sqlite3.connect("inventarios.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        print("Tabla creada o ya existente.")

def agregar_producto(nombre, cantidad, precio):
    with sqlite3.connect("inventarios.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
        conexion.commit()
        print(f"Producto '{nombre}' agregado con éxito.")

def listar_productos():
    with sqlite3.connect("inventarios.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        print("\nInventario:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: ${producto[3]:.2f}")

def actualizar_producto(id_producto, cantidad, precio):
    with sqlite3.connect("inventarios.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?", (cantidad, precio, id_producto))
        conexion.commit()
        print(f"Producto con ID {id_producto} actualizado con éxito.")

def eliminar_producto(id_producto):
    with sqlite3.connect("inventarios.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        print(f"Producto con ID {id_producto} eliminado con éxito.")

if __name__ == "__main__":
    crear_tabla()

    while True:
        print("\nGestor de Inventarios")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
        elif opcion == "5":
            print("Saliendo del gestor de inventarios.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
