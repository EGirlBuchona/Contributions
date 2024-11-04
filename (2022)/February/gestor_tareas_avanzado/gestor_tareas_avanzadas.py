# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestor de Tareas Avanzado en Python

tareas = []

def agregar_tarea(titulo, descripcion, etiqueta):
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "etiqueta": etiqueta,
        "completada": False
    }
    tareas.append(tarea)
    print("Tarea añadida exitosamente.")

def mostrar_tareas(filtro_etiqueta=None, completadas=None):
    for tarea in tareas:
        if (filtro_etiqueta is None or tarea["etiqueta"] == filtro_etiqueta) and \
           (completadas is None or tarea["completada"] == completadas):
            print(f"Título: {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Etiqueta: {tarea['etiqueta']}")
            print(f"Completada: {'Sí' if tarea['completada'] else 'No'}")
            print("-" * 20)

def completar_tarea(titulo):
    for tarea in tareas:
        if tarea["titulo"] == titulo:
            tarea["completada"] = True
            print(f"Tarea '{titulo}' marcada como completada.")
            return
    print("Tarea no encontrada.")

def eliminar_tarea(titulo):
    global tareas
    tareas = [tarea for tarea in tareas if tarea["titulo"] != titulo]
    print(f"Tarea '{titulo}' eliminada exitosamente.")

if __name__ == "__main__":
    while True:
        print("\nGestor de Tareas Avanzado")
        print("1. Agregar tarea")
        print("2. Mostrar todas las tareas")
        print("3. Mostrar tareas por etiqueta")
        print("4. Mostrar tareas completadas")
        print("5. Completar tarea")
        print("6. Eliminar tarea")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            etiqueta = input("Etiqueta: ")
            agregar_tarea(titulo, descripcion, etiqueta)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            filtro_etiqueta = input("Ingrese la etiqueta a filtrar: ")
            mostrar_tareas(filtro_etiqueta=filtro_etiqueta)
        elif opcion == "4":
            mostrar_tareas(completadas=True)
        elif opcion == "5":
            titulo = input("Título de la tarea a completar: ")
            completar_tarea(titulo)
        elif opcion == "6":
            titulo = input("Título de la tarea a eliminar: ")
            eliminar_tarea(titulo)
        elif opcion == "7":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
