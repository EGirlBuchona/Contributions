# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestión de Productos con SQLite

import sqlite3

def conectar():
    return sqlite3.connect("productos.db")

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()

def agregar_producto(nombre, precio, cantidad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)", (nombre, precio, cantidad))
    conexion.commit()
    conexion.close()
    print("Producto agregado exitosamente.")

def mostrar_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}, Cantidad: {producto[3]}")

def actualizar_producto(id_producto, nuevo_precio, nueva_cantidad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET precio = ?, cantidad = ? WHERE id = ?", (nuevo_precio, nueva_cantidad, id_producto))
    conexion.commit()
    conexion.close()
    print("Producto actualizado exitosamente.")

def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    conexion.close()
    print("Producto eliminado exitosamente.")

# Ejemplo de uso
if __name__ == "__main__":
    crear_tabla()
    while True:
        print("\nGestión de Productos")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))
            actualizar_producto(id_producto, nuevo_precio, nueva_cantidad)
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente de nuevo.")
