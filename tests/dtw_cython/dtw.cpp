// dtw.cpp

#include "dtw.h"
#include <limits>
#include "algoritmos.h" // Incluimos las funciones de algoritmo

double ExecuteDTW(const CoordinateSequence& seq1, const CoordinateSequence& seq2) {
    std::vector<std::vector<double>> matrizCostos = CalculateDTWMatrix(seq1, seq2);
    std::vector<std::pair<int, int>> rutaOptima = CalculateOptimalPath(matrizCostos);
    double costDTW = CalculateCostFromOptimalPath(matrizCostos, rutaOptima);

    return costDTW;
}

std::vector<std::vector<double>> CalculateDTWMatrix(const CoordinateSequence& seq1, const CoordinateSequence& seq2) {
    int m = seq1.points.size();
    int n = seq2.points.size();
    std::vector<std::vector<double>> accumulatedCost(m, std::vector<double>(n, 0.0));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            accumulatedCost[i][j] = distanceBetweenPoints(seq1.points[i], seq2.points[j]);

            if (i == 0 && j == 0) {
                continue;
            } else if (i == 0) {
                accumulatedCost[i][j] += accumulatedCost[i][j - 1];
            } else if (j == 0) {
                accumulatedCost[i][j] += accumulatedCost[i - 1][j];
            } else {
                accumulatedCost[i][j] += std::min(
                    accumulatedCost[i - 1][j],          // Movimiento hacia abajo
                    std::min(
                        accumulatedCost[i][j - 1],      // Movimiento hacia la izquierda
                        accumulatedCost[i - 1][j - 1]   // Movimiento diagonal
                    )
                );
            }
        }
    }

    return accumulatedCost;
}

std::vector<std::pair<int, int>> CalculateOptimalPath(const std::vector<std::vector<double>>& accumulatedCost) {
    std::vector<std::pair<int, int>> optimalPath;

    int i = accumulatedCost.size() - 1;
    int j = accumulatedCost[0].size() - 1;

    while (i > 0 || j > 0) {
        optimalPath.emplace_back(i, j);

        double minCost = std::numeric_limits<double>::infinity();

        if (i > 0 && j > 0) {
            minCost = std::min(
                accumulatedCost[i - 1][j],          // Movimiento hacia abajo
                std::min(
                    accumulatedCost[i][j - 1],      // Movimiento hacia la izquierda
                    accumulatedCost[i - 1][j - 1]   // Movimiento diagonal
                )
            );
        }
        if (i > 0 && j <= 0) {
            minCost = std::min(minCost, accumulatedCost[i - 1][j]);     // Movimiento hacia abajo
        }
        if (j > 0 && i <= 0) {
            minCost = std::min(minCost, accumulatedCost[i][j - 1]);     // Movimiento hacia la izquierda
        }

        // Actualizamos las coordenadas según el movimiento con el costo mínimo
        if (i > 0 && j > 0 && accumulatedCost[i - 1][j - 1] == minCost) {
            i--;
            j--;
        } else if (i > 0 && accumulatedCost[i - 1][j] == minCost) {
            i--;
        } else {
            j--;
        }
    }

    optimalPath.emplace_back(0, 0);

    return optimalPath;
}

double CalculateCostFromOptimalPath(const std::vector<std::vector<double>>& accumulatedCost, const std::vector<std::pair<int, int>>& optimalPath) {
    double cost = 0.0;

    for (const auto& index : optimalPath) {
        cost += accumulatedCost[index.first][index.second];
    }

    std::cout << "\n";

    return cost;
}

