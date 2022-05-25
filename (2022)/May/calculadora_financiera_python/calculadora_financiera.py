# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Calculadora Financiera en Python

def calcular_interes_simple(capital, tasa, tiempo):
    return capital * (tasa / 100) * tiempo

def calcular_interes_compuesto(capital, tasa, tiempo):
    return capital * ((1 + (tasa / 100)) ** tiempo - 1)

def calcular_pago_prestamo(principal, tasa, plazo):
    tasa_mensual = tasa / (12 * 100)
    return principal * tasa_mensual / (1 - (1 + tasa_mensual) ** -plazo)

if __name__ == "__main__":
    while True:
        print("\nCalculadora Financiera")
        print("1. Cálculo de Interés Simple")
        print("2. Cálculo de Interés Compuesto")
        print("3. Cálculo de Pago de Préstamo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            capital = float(input("Ingrese el capital: "))
            tasa = float(input("Ingrese la tasa de interés (%): "))
            tiempo = float(input("Ingrese el tiempo en años: "))
            print(f"Interés Simple: {calcular_interes_simple(capital, tasa, tiempo):.2f}")
        
        elif opcion == "2":
            capital = float(input("Ingrese el capital: "))
            tasa = float(input("Ingrese la tasa de interés (%): "))
            tiempo = float(input("Ingrese el tiempo en años: "))
            print(f"Interés Compuesto: {calcular_interes_compuesto(capital, tasa, tiempo):.2f}")
        
        elif opcion == "3":
            principal = float(input("Ingrese el monto del préstamo: "))
            tasa = float(input("Ingrese la tasa de interés anual (%): "))
            plazo = int(input("Ingrese el plazo en meses: "))
            print(f"Pago mensual del préstamo: {calcular_pago_prestamo(principal, tasa, plazo):.2f}")
        
        elif opcion == "4":
            print("Saliendo de la calculadora financiera.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
