# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestor de Notas en Consola en Python

notas = []

def agregar_nota():
    titulo = input("Título de la nota: ")
    contenido = input("Contenido de la nota: ")
    notas.append({"titulo": titulo, "contenido": contenido})
    print("Nota agregada exitosamente.\n")

def mostrar_notas():
    if not notas:
        print("No hay notas para mostrar.\n")
        return

    print("Listado de Notas:")
    for idx, nota in enumerate(notas, start=1):
        print(f"{idx}. {nota['titulo']}: {nota['contenido']}")
    print()

def eliminar_nota():
    mostrar_notas()
    try:
        indice = int(input("Ingrese el número de la nota a eliminar: ")) - 1
        if 0 <= indice < len(notas):
            notas.pop(indice)
            print("Nota eliminada exitosamente.\n")
        else:
            print("Número de nota inválido.\n")
    except ValueError:
        print("Por favor, ingrese un número válido.\n")

def main():
    while True:
        print("Gestor de Notas")
        print("1. Agregar Nota")
        print("2. Mostrar Notas")
        print("3. Eliminar Nota")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            mostrar_notas()
        elif opcion == "3":
            eliminar_nota()
        elif opcion == "4":
            print("Saliendo del gestor de notas.")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
