// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Aplicación de Consola en C# para Operaciones Matemáticas

using System;

namespace AplicacionConsola
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bienvenido a la aplicación de operaciones matemáticas.");
            Console.WriteLine("Seleccione una operación: ");
            Console.WriteLine("1. Suma");
            Console.WriteLine("2. Resta");
            Console.WriteLine("3. Multiplicación");
            Console.WriteLine("4. División");
            
            int opcion = int.Parse(Console.ReadLine());
            Console.Write("Ingrese el primer número: ");
            double num1 = double.Parse(Console.ReadLine());
            Console.Write("Ingrese el segundo número: ");
            double num2 = double.Parse(Console.ReadLine());

            double resultado = 0;
            switch (opcion)
            {
                case 1:
                    resultado = num1 + num2;
                    Console.WriteLine($"Resultado de la suma: {resultado}");
                    break;
                case 2:
                    resultado = num1 - num2;
                    Console.WriteLine($"Resultado de la resta: {resultado}");
                    break;
                case 3:
                    resultado = num1 * num2;
                    Console.WriteLine($"Resultado de la multiplicación: {resultado}");
                    break;
                case 4:
                    if (num2 != 0)
                    {
                        resultado = num1 / num2;
                        Console.WriteLine($"Resultado de la división: {resultado}");
                    }
                    else
                    {
                        Console.WriteLine("Error: División por cero.");
                    }
                    break;
                default:
                    Console.WriteLine("Opción inválida.");
                    break;
            }
        }
    }
}
