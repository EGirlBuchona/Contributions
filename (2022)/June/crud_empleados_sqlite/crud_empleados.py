# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: CRUD de Empleados en SQLite

import sqlite3

def crear_tabla():
    with sqlite3.connect("empleados.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                puesto TEXT NOT NULL,
                salario REAL NOT NULL
            )
        """)
        print("Tabla 'empleados' creada o ya existente.")

def agregar_empleado(nombre, puesto, salario):
    with sqlite3.connect("empleados.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)", (nombre, puesto, salario))
        conexion.commit()
        print(f"Empleado '{nombre}' agregado con éxito.")

def listar_empleados():
    with sqlite3.connect("empleados.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleados")
        empleados = cursor.fetchall()
        print("\nLista de Empleados:")
        for empleado in empleados:
            print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Puesto: {empleado[2]}, Salario: ${empleado[3]:.2f}")

def actualizar_empleado(id_empleado, nombre, puesto, salario):
    with sqlite3.connect("empleados.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE empleados SET nombre = ?, puesto = ?, salario = ? WHERE id = ?", (nombre, puesto, salario, id_empleado))
        conexion.commit()
        print(f"Empleado con ID {id_empleado} actualizado con éxito.")

def eliminar_empleado(id_empleado):
    with sqlite3.connect("empleados.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM empleados WHERE id = ?", (id_empleado,))
        conexion.commit()
        print(f"Empleado con ID {id_empleado} eliminado con éxito.")

if __name__ == "__main__":
    crear_tabla()

    while True:
        print("\nGestión de Empleados")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del empleado: ")
            puesto = input("Puesto del empleado: ")
            salario = float(input("Salario del empleado: "))
            agregar_empleado(nombre, puesto, salario)
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            id_empleado = int(input("ID del empleado a actualizar: "))
            nombre = input("Nuevo nombre: ")
            puesto = input("Nuevo puesto: ")
            salario = float(input("Nuevo salario: "))
            actualizar_empleado(id_empleado, nombre, puesto, salario)
        elif opcion == "4":
            id_empleado = int(input("ID del empleado a eliminar: "))
            eliminar_empleado(id_empleado)
        elif opcion == "5":
            print("Saliendo del gestor de empleados.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
