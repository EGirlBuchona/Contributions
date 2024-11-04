// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Implementación de Búsqueda Binaria en C++

#include <iostream>
using namespace std;

int busquedaBinaria(int arr[], int izquierda, int derecha, int x)
{
    while (izquierda <= derecha)
    {
        int medio = izquierda + (derecha - izquierda) / 2;

        // Si el elemento está presente en el medio
        if (arr[medio] == x)
        {
            return medio;
        }

        // Si el elemento es mayor, ignora la mitad izquierda
        if (arr[medio] < x)
        {
            izquierda = medio + 1;
        }
        // Si el elemento es menor, ignora la mitad derecha
        else
        {
            derecha = medio - 1;
        }
    }

    // Si el elemento no está presente
    return -1;
}

int main()
{
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;

    int resultado = busquedaBinaria(arr, 0, n - 1, x);
    if (resultado == -1)
    {
        cout << "Elemento no encontrado en el array." << endl;
    }
    else
    {
        cout << "Elemento encontrado en el índice: " << resultado << endl;
    }
    return 0;
}
