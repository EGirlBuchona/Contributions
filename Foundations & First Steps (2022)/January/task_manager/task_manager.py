# task_manager.py

def mostrar_tareas(tareas):
    """Función que muestra las tareas actuales."""
    if not tareas:
        print("No tienes tareas pendientes.")
    else:
        print("Tareas:")
        for idx, tarea in enumerate(tareas, 1):
            print(f"{idx}. {tarea}")


def agregar_tarea(tareas):
    """Función que agrega una tarea a la lista."""
    tarea = input("Escribe una nueva tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")


def eliminar_tarea(tareas):
    """Función que elimina una tarea por su número."""
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        idx = int(input("Escribe el número de la tarea que quieres eliminar: "))
        tarea_eliminada = tareas.pop(idx - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
    except (IndexError, ValueError):
        print("Número de tarea inválido.")


def menu():
    """Función principal que muestra el menú y gestiona las opciones."""
    tareas = []
    while True:
        print("\nGestor de Tareas")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida, por favor elige una opción correcta.")


if __name__ == "__main__":
    menu()
