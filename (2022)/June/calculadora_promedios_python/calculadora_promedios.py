# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Calculadora de Promedios en Python

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

def main():
    print("Calculadora de Promedios")
    numeros = []

    while True:
        entrada = input("Ingrese una calificación (o 's' para salir): ")
        
        if entrada.lower() == 's':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Ingrese un número o 's' para salir.")

    promedio = calcular_promedio(numeros)
    print(f"\nPromedio de las calificaciones ingresadas: {promedio:.2f}")

if __name__ == "__main__":
    main()
