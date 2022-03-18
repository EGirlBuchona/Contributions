# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script de Gestión de Tiempo en Python

from datetime import datetime
import time

tareas = {}

def iniciar_tarea(nombre_tarea):
    if nombre_tarea in tareas:
        print(f"La tarea '{nombre_tarea}' ya está en curso.")
    else:
        tareas[nombre_tarea] = datetime.now()
        print(f"Tarea '{nombre_tarea}' iniciada.")

def finalizar_tarea(nombre_tarea):
    if nombre_tarea not in tareas:
        print(f"La tarea '{nombre_tarea}' no ha sido iniciada.")
    else:
        inicio = tareas.pop(nombre_tarea)
        fin = datetime.now()
        duracion = fin - inicio
        print(f"Tarea '{nombre_tarea}' finalizada.")
        print(f"Duración: {duracion}")
        return nombre_tarea, duracion

def generar_reporte(tiempos):
    print("\n--- Reporte de Tiempo ---")
    for nombre, duracion in tiempos:
        print(f"Tarea: {nombre} - Duración: {duracion}")
    print("-------------------------")

def menu():
    tiempos = []
    while True:
        print("\nGestión de Tiempo")
        print("1. Iniciar Tarea")
        print("2. Finalizar Tarea")
        print("3. Generar Reporte")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_tarea = input("Nombre de la tarea: ")
            iniciar_tarea(nombre_tarea)
        elif opcion == '2':
            nombre_tarea = input("Nombre de la tarea a finalizar: ")
            resultado = finalizar_tarea(nombre_tarea)
            if resultado:
                tiempos.append(resultado)
        elif opcion == '3':
            generar_reporte(tiempos)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
