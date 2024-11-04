# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Sistema de Registro de Usuarios en Python

import hashlib

# Diccionario para almacenar los usuarios en memoria
usuarios = {}

def hash_password(password):
    """Devuelve un hash de la contraseña utilizando SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_usuario(nombre_usuario, password):
    """Registra un nuevo usuario."""
    if nombre_usuario in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[nombre_usuario] = hash_password(password)
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")

def autenticar_usuario(nombre_usuario, password):
    """Autentica un usuario verificando su nombre de usuario y contraseña."""
    if nombre_usuario in usuarios:
        hashed_password = hash_password(password)
        if usuarios[nombre_usuario] == hashed_password:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")

def main():
    while True:
        print("\nSistema de Registro de Usuarios")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_usuario = input("Ingrese un nombre de usuario: ")
            password = input("Ingrese una contraseña: ")
            registrar_usuario(nombre_usuario, password)
        elif opcion == "2":
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            autenticar_usuario(nombre_usuario, password)
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
