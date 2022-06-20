// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Calculadora Básica en C#

using System;

namespace CalculadoraBasica
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bienvenido a la Calculadora Básica");
            bool continuar = true;

            while (continuar)
            {
                Console.WriteLine("\nSeleccione una operación:");
                Console.WriteLine("1. Suma");
                Console.WriteLine("2. Resta");
                Console.WriteLine("3. Multiplicación");
                Console.WriteLine("4. División");
                Console.WriteLine("5. Salir");

                string opcion = Console.ReadLine();

                if (opcion == "5")
                {
                    continuar = false;
                    Console.WriteLine("Gracias por usar la calculadora. ¡Adiós!");
                    break;
                }

                Console.Write("Ingrese el primer número: ");
                if (!double.TryParse(Console.ReadLine(), out double numero1))
                {
                    Console.WriteLine("Entrada no válida. Intente nuevamente.");
                    continue;
                }

                Console.Write("Ingrese el segundo número: ");
                if (!double.TryParse(Console.ReadLine(), out double numero2))
                {
                    Console.WriteLine("Entrada no válida. Intente nuevamente.");
                    continue;
                }

                switch (opcion)
                {
                    case "1":
                        Console.WriteLine($"Resultado: {numero1} + {numero2} = {numero1 + numero2}");
                        break;
                    case "2":
                        Console.WriteLine($"Resultado: {numero1} - {numero2} = {numero1 - numero2}");
                        break;
                    case "3":
                        Console.WriteLine($"Resultado: {numero1} * {numero2} = {numero1 * numero2}");
                        break;
                    case "4":
                        if (numero2 == 0)
                        {
                            Console.WriteLine("Error: División entre cero no permitida.");
                        }
                        else
                        {
                            Console.WriteLine($"Resultado: {numero1} / {numero2} = {numero1 / numero2}");
                        }
                        break;
                    default:
                        Console.WriteLine("Opción no válida. Intente de nuevo.");
                        break;
                }
            }
        }
    }
}
