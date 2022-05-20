// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Gestor de Libros en C#

using System;
using System.Collections.Generic;

namespace GestorLibros
{
    class Libro
    {
        public string Titulo { get; set; }
        public string Autor { get; set; }

        public override string ToString()
        {
            return $"Título: {Titulo}, Autor: {Autor}";
        }
    }

    class GestorLibros
    {
        private List<Libro> libros = new List<Libro>();

        public void AgregarLibro(string titulo, string autor)
        {
            libros.Add(new Libro { Titulo = titulo, Autor = autor });
            Console.WriteLine("Libro agregado exitosamente.");
        }

        public void EliminarLibro(string titulo)
        {
            libros.RemoveAll(libro => libro.Titulo.Equals(titulo, StringComparison.OrdinalIgnoreCase));
            Console.WriteLine("Libro eliminado exitosamente.");
        }

        public void BuscarLibro(string titulo)
        {
            var encontrados = libros.FindAll(libro => libro.Titulo.Contains(titulo, StringComparison.OrdinalIgnoreCase));
            if (encontrados.Count > 0)
            {
                Console.WriteLine("Libros encontrados:");
                encontrados.ForEach(libro => Console.WriteLine(libro));
            }
            else
            {
                Console.WriteLine("No se encontraron libros con ese título.");
            }
        }

        public void ListarLibros()
        {
            if (libros.Count > 0)
            {
                Console.WriteLine("Lista de libros:");
                libros.ForEach(libro => Console.WriteLine(libro));
            }
            else
            {
                Console.WriteLine("No hay libros en la lista.");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            GestorLibros gestor = new GestorLibros();
            while (true)
            {
                Console.WriteLine("\nGestor de Libros");
                Console.WriteLine("1. Agregar libro");
                Console.WriteLine("2. Eliminar libro");
                Console.WriteLine("3. Buscar libro");
                Console.WriteLine("4. Listar libros");
                Console.WriteLine("5. Salir");
                Console.Write("Seleccione una opción: ");
                
                string opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        Console.Write("Título: ");
                        string titulo = Console.ReadLine();
                        Console.Write("Autor: ");
                        string autor = Console.ReadLine();
                        gestor.AgregarLibro(titulo, autor);
                        break;
                    case "2":
                        Console.Write("Título del libro a eliminar: ");
                        titulo = Console.ReadLine();
                        gestor.EliminarLibro(titulo);
                        break;
                    case "3":
                        Console.Write("Título del libro a buscar: ");
                        titulo = Console.ReadLine();
                        gestor.BuscarLibro(titulo);
                        break;
                    case "4":
                        gestor.ListarLibros();
                        break;
                    case "5":
                        return;
                    default:
                        Console.WriteLine("Opción no válida.");
                        break;
                }
            }
        }
    }
}
