// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Calculadora de Impuestos en C#

using System;

namespace CalculadoraImpuestos
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Calculadora de Impuestos");
            Console.Write("Ingrese el monto sobre el cual se aplicará el impuesto: ");
            decimal monto = decimal.Parse(Console.ReadLine());

            Console.Write("Ingrese el porcentaje de impuesto (por ejemplo, 15 para 15%): ");
            decimal porcentajeImpuesto = decimal.Parse(Console.ReadLine());

            decimal montoImpuesto = CalcularImpuesto(monto, porcentajeImpuesto);
            decimal montoTotal = monto + montoImpuesto;

            Console.WriteLine($"\nMonto original: {monto:C}");
            Console.WriteLine($"Impuesto aplicado ({porcentajeImpuesto}%): {montoImpuesto:C}");
            Console.WriteLine($"Monto total con impuesto: {montoTotal:C}");
        }

        static decimal CalcularImpuesto(decimal monto, decimal porcentajeImpuesto)
        {
            return monto * (porcentajeImpuesto / 100);
        }
    }
}
