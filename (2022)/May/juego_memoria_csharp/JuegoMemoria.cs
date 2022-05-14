// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Juego de Memoria en C#

using System;
using System.Collections.Generic;
using System.Threading;

namespace JuegoMemoria
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            List<int> secuencia = new List<int>();

            Console.WriteLine("Bienvenido al Juego de Memoria!");
            Console.WriteLine("Recuerda la secuencia de números y repítela correctamente.\n");

            while (true)
            {
                int nuevoNumero = random.Next(1, 10);
                secuencia.Add(nuevoNumero);

                Console.WriteLine("Secuencia:");
                foreach (int numero in secuencia)
                {
                    Console.Write(numero + " ");
                    Thread.Sleep(500);  // Pausa para que el jugador vea el número
                }
                
                Console.Clear();
                Console.WriteLine("Introduce la secuencia:");

                bool correcto = true;
                for (int i = 0; i < secuencia.Count; i++)
                {
                    int respuestaUsuario;
                    if (int.TryParse(Console.ReadLine(), out respuestaUsuario))
                    {
                        if (respuestaUsuario != secuencia[i])
                        {
                            correcto = false;
                            break;
                        }
                    }
                    else
                    {
                        correcto = false;
                        break;
                    }
                }

                if (!correcto)
                {
                    Console.WriteLine("Lo siento, has perdido. La secuencia era:");
                    Console.WriteLine(string.Join(" ", secuencia));
                    break;
                }
                else
                {
                    Console.WriteLine("¡Correcto! Prepárate para la siguiente ronda.");
                    Thread.Sleep(1000);
                    Console.Clear();
                }
            }

            Console.WriteLine("Gracias por jugar!");
        }
    }
}
