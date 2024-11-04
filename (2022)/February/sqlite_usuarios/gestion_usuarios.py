# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestión de Usuarios en SQLite en Python

import sqlite3

def conectar():
    return sqlite3.connect("usuarios.db")

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        edad INTEGER
                    )''')
    conexion.commit()
    conexion.close()

def crear_usuario(nombre, email, edad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)", (nombre, email, edad))
    conexion.commit()
    conexion.close()
    print("Usuario creado exitosamente.")

def leer_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexion.close()

def actualizar_usuario(id, nombre, email, edad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre = ?, email = ?, edad = ? WHERE id = ?", (nombre, email, edad, id))
    conexion.commit()
    conexion.close()
    print("Usuario actualizado exitosamente.")

def eliminar_usuario(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    print("Usuario eliminado exitosamente.")

if __name__ == "__main__":
    crear_tabla()
    while True:
        print("\nGestión de Usuarios")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            edad = int(input("Edad: "))
            crear_usuario(nombre, email, edad)
        elif opcion == "2":
            leer_usuarios()
        elif opcion == "3":
            id = int(input("ID del usuario a actualizar: "))
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            edad = int(input("Nueva edad: "))
            actualizar_usuario(id, nombre, email, edad)
        elif opcion == "4":
            id = int(input("ID del usuario a eliminar: "))
            eliminar_usuario(id)
        elif opcion == "5":
            print("Saliendo de la gestión de usuarios.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
