// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Juego del Ahorcado en C#

using System;
using System.Collections.Generic;

namespace JuegoAhorcado
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] palabras = { "computadora", "programacion", "ahorcado", "juego", "desarrollo" };
            Random random = new Random();
            string palabra = palabras[random.Next(palabras.Length)];
            HashSet<char> letrasCorrectas = new HashSet<char>();
            HashSet<char> letrasIncorrectas = new HashSet<char>();
            int intentosRestantes = 6;

            Console.WriteLine("Bienvenido al Juego del Ahorcado!");

            while (intentosRestantes > 0)
            {
                MostrarProgreso(palabra, letrasCorrectas);
                Console.WriteLine($"\nIntentos restantes: {intentosRestantes}");
                Console.Write("Ingrese una letra: ");
                char letra;

                if (char.TryParse(Console.ReadLine().ToLower(), out letra))
                {
                    if (palabra.Contains(letra))
                    {
                        letrasCorrectas.Add(letra);
                        if (PalabraCompleta(palabra, letrasCorrectas))
                        {
                            Console.WriteLine($"\n¡Felicidades! Has adivinado la palabra: {palabra}");
                            break;
                        }
                    }
                    else if (!letrasIncorrectas.Contains(letra))
                    {
                        letrasIncorrectas.Add(letra);
                        intentosRestantes--;
                    }
                    else
                    {
                        Console.WriteLine("Ya intentaste con esa letra. Prueba otra.");
                    }
                }
                else
                {
                    Console.WriteLine("Entrada no válida. Intente nuevamente.");
                }
            }

            if (intentosRestantes == 0)
            {
                Console.WriteLine($"\nLo siento, has perdido. La palabra era: {palabra}");
            }
        }

        static void MostrarProgreso(string palabra, HashSet<char> letrasCorrectas)
        {
            foreach (char letra in palabra)
            {
                if (letrasCorrectas.Contains(letra))
                {
                    Console.Write(letra + " ");
                }
                else
                {
                    Console.Write("_ ");
                }
            }
        }

        static bool PalabraCompleta(string palabra, HashSet<char> letrasCorrectas)
        {
            foreach (char letra in palabra)
            {
                if (!letrasCorrectas.Contains(letra))
                {
                    return false;
                }
            }
            return true;
        }
    }
}
