// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Búsqueda Binaria Mejorada en C++

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Función para verificar si el array está ordenado
bool estaOrdenado(const vector<int> &arr)
{
    for (size_t i = 1; i < arr.size(); i++)
    {
        if (arr[i] < arr[i - 1])
        {
            return false;
        }
    }
    return true;
}

// Función de búsqueda binaria
int busquedaBinaria(const vector<int> &arr, int valor)
{
    int izquierda = 0;
    int derecha = arr.size() - 1;

    while (izquierda <= derecha)
    {
        int medio = izquierda + (derecha - izquierda) / 2;

        if (arr[medio] == valor)
        {
            return medio;
        }
        if (arr[medio] < valor)
        {
            izquierda = medio + 1;
        }
        else
        {
            derecha = medio - 1;
        }
    }

    return -1; // Valor no encontrado
}

int main()
{
    vector<int> arr;
    int n, valor;

    cout << "Ingrese el número de elementos: ";
    cin >> n;

    cout << "Ingrese los elementos del array:\n";
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }

    // Verificar si el array está ordenado
    if (!estaOrdenado(arr))
    {
        char opcion;
        cout << "El array no está ordenado. ¿Desea ordenarlo? (s/n): ";
        cin >> opcion;
        if (opcion == 's' || opcion == 'S')
        {
            sort(arr.begin(), arr.end());
            cout << "Array ordenado.\n";
        }
        else
        {
            cout << "Operación cancelada. El array debe estar ordenado para la búsqueda binaria.\n";
            return 0;
        }
    }

    cout << "Ingrese el valor a buscar: ";
    cin >> valor;

    int resultado = busquedaBinaria(arr, valor);
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
