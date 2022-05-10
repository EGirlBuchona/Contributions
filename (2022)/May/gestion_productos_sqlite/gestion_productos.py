# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestión de Productos en SQLite con Python

import sqlite3

class GestionProductos:
    def __init__(self, db_name="productos.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def agregar_producto(self, nombre, precio, cantidad):
        self.cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)", 
                            (nombre, precio, cantidad))
        self.conn.commit()
        print(f"Producto '{nombre}' agregado exitosamente.")

    def ver_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        for producto in productos:
            print(producto)

    def actualizar_producto(self, id_producto, nombre=None, precio=None, cantidad=None):
        if nombre:
            self.cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nombre, id_producto))
        if precio:
            self.cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (precio, id_producto))
        if cantidad:
            self.cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id_producto))
        self.conn.commit()
        print(f"Producto con ID {id_producto} actualizado exitosamente.")

    def eliminar_producto(self, id_producto):
        self.cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        self.conn.commit()
        print(f"Producto con ID {id_producto} eliminado exitosamente.")

    def cerrar_conexion(self):
        self.conn.close()

if __name__ == "__main__":
    gestion = GestionProductos()
    while True:
        print("\nGestión de Productos")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            gestion.agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            gestion.ver_productos()
        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío si no desea cambiar): ")
            precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")
            cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
            gestion.actualizar_producto(id_producto, nombre or None, float(precio) if precio else None, int(cantidad) if cantidad else None)
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            gestion.eliminar_producto(id_producto)
        elif opcion == "5":
            gestion.cerrar_conexion()
            print("Saliendo de la gestión de productos.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
