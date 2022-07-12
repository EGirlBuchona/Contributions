// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Algoritmo de Dijkstra en Java

import java.util.*;

class DijkstraAlgorithm {

    static class Nodo implements Comparable<Nodo> {
        int id;
        int distancia;

        Nodo(int id, int distancia) {
            this.id = id;
            this.distancia = distancia;
        }

        @Override
        public int compareTo(Nodo otro) {
            return Integer.compare(this.distancia, otro.distancia);
        }
    }

    public static void encontrarRutaMasCorta(int[][] grafo, int origen) {
        int n = grafo.length;
        int[] distancias = new int[n];
        boolean[] visitados = new boolean[n];

        Arrays.fill(distancias, Integer.MAX_VALUE);
        distancias[origen] = 0;

        PriorityQueue<Nodo> colaPrioridad = new PriorityQueue<>();
        colaPrioridad.add(new Nodo(origen, 0));

        while (!colaPrioridad.isEmpty()) {
            Nodo actual = colaPrioridad.poll();

            if (visitados[actual.id]) continue;
            visitados[actual.id] = true;

            for (int vecino = 0; vecino < n; vecino++) {
                if (grafo[actual.id][vecino] != 0 && !visitados[vecino]) {
                    int nuevaDistancia = distancias[actual.id] + grafo[actual.id][vecino];
                    if (nuevaDistancia < distancias[vecino]) {
                        distancias[vecino] = nuevaDistancia;
                        colaPrioridad.add(new Nodo(vecino, nuevaDistancia));
                    }
                }
            }
        }

        mostrarResultados(origen, distancias);
    }

    private static void mostrarResultados(int origen, int[] distancias) {
        System.out.println("Distancias desde el nodo " + origen + ":");
        for (int i = 0; i < distancias.length; i++) {
            System.out.println("Hasta nodo " + i + ": " + (distancias[i] == Integer.MAX_VALUE ? "Inalcanzable" : distancias[i]));
        }
    }

    public static void main(String[] args) {
        int[][] grafo = {
            {0, 10, 0, 0, 0, 0},
            {10, 0, 5, 0, 0, 0},
            {0, 5, 0, 20, 1, 0},
            {0, 0, 20, 0, 2, 2},
            {0, 0, 1, 2, 0, 3},
            {0, 0, 0, 2, 3, 0}
        };

        int origen = 0;
        encontrarRutaMasCorta(grafo, origen);
    }
}
