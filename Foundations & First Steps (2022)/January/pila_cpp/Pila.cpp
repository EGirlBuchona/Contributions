// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Implementación de una Pila en C++

#include <iostream>
#include <stdexcept>
using namespace std;

#define MAX 1000 // Tamaño máximo de la pila

class Pila
{
    int tope;

public:
    int arr[MAX]; // Array que almacena los elementos de la pila

    Pila() { tope = -1; }

    bool push(int x)
    {
        if (tope >= (MAX - 1))
        {
            cout << "Overflow: La pila está llena.\n";
            return false;
        }
        else
        {
            arr[++tope] = x;
            cout << x << " añadido a la pila.\n";
            return true;
        }
    }

    int pop()
    {
        if (tope < 0)
        {
            cout << "Underflow: La pila está vacía.\n";
            return 0;
        }
        else
        {
            int x = arr[tope--];
            return x;
        }
    }

    int peek()
    {
        if (tope < 0)
        {
            cout << "La pila está vacía.\n";
            return 0;
        }
        else
        {
            int x = arr[tope];
            return x;
        }
    }

    bool estaVacia()
    {
        return (tope < 0);
    }
};

int main()
{
    Pila pila;
    pila.push(10);
    pila.push(20);
    pila.push(30);

    cout << pila.pop() << " eliminado de la pila.\n";
    cout << "Elemento superior es: " << pila.peek() << endl;

    return 0;
}
