// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Generador de Contraseñas en C#

using System;

namespace GeneradorPasswords
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bienvenido al Generador de Contraseñas");
            Console.Write("Ingrese la longitud deseada para la contraseña: ");

            if (int.TryParse(Console.ReadLine(), out int longitud) && longitud > 0)
            {
                string contraseña = GenerarPassword(longitud);
                Console.WriteLine($"Contraseña generada: {contraseña}");
            }
            else
            {
                Console.WriteLine("Entrada no válida. Por favor, ingrese un número entero positivo.");
            }
        }

        static string GenerarPassword(int longitud)
        {
            const string caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
            Random random = new Random();
            char[] password = new char[longitud];

            for (int i = 0; i < longitud; i++)
            {
                password[i] = caracteres[random.Next(caracteres.Length)];
            }

            return new string(password);
        }
    }
}
