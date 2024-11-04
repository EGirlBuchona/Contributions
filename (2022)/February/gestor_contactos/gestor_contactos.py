# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestor de Contactos en Python

contactos = {}

def agregar_contacto(nombre, telefono, email):
    contactos[nombre] = {"telefono": telefono, "email": email}
    print(f"Contacto '{nombre}' agregado exitosamente.")

def editar_contacto(nombre):
    if nombre in contactos:
        telefono = input("Nuevo teléfono: ")
        email = input("Nuevo correo electrónico: ")
        contactos[nombre] = {"telefono": telefono, "email": email}
        print(f"Contacto '{nombre}' actualizado.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print("Contacto no encontrado.")

def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {contactos[nombre]['telefono']}")
        print(f"Email: {contactos[nombre]['email']}")
    else:
        print("Contacto no encontrado.")

def mostrar_menu():
    print("\nGestor de Contactos")
    print("1. Agregar contacto")
    print("2. Editar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agregar_contacto(nombre, telefono, email)
        elif opcion == "2":
            nombre = input("Nombre del contacto a editar: ")
            editar_contacto(nombre)
        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "5":
            print("Saliendo del gestor de contactos.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
