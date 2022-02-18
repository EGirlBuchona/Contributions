// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Implementación de Búsqueda Secuencial en C++

#include <iostream>
using namespace std;

int busquedaSecuencial(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == x)
        {
            return i; // Retorna el índice donde se encuentra el elemento
        }
    }
    return -1; // Retorna -1 si el elemento no se encuentra
}

int main()
{
    int arr[] = {10, 23, 35, 40, 55};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x;

    cout << "Ingrese el valor a buscar: ";
    cin >> x;

    int resultado = busquedaSecuencial(arr, n, x);
    if (resultado != -1)
    {
        cout << "Elemento encontrado en el índice: " << resultado << endl;
    }
    else
    {
        cout << "Elemento no encontrado en el array." << endl;
    }

    return 0;
}
