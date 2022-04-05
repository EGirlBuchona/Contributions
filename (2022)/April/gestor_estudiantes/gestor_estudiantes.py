# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestor de Estudiantes

estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estudiantes.append({"nombre": nombre, "edad": edad})
    print("Estudiante agregado exitosamente.")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado exitosamente.")
            return
    print("Estudiante no encontrado.")

def modificar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a modificar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            nueva_edad = int(input("Ingrese la nueva edad: "))
            estudiante["edad"] = nueva_edad
            print("Estudiante modificado exitosamente.")
            return
    print("Estudiante no encontrado.")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

def menu():
    while True:
        print("\nGestor de Estudiantes")
        print("1. Agregar estudiante")
        print("2. Eliminar estudiante")
        print("3. Modificar estudiante")
        print("4. Mostrar estudiantes")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            eliminar_estudiante()
        elif opcion == "3":
            modificar_estudiante()
        elif opcion == "4":
            mostrar_estudiantes()
        elif opcion == "5":
            print("Saliendo del gestor.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
