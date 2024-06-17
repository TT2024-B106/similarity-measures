#include <vector>
#include "Headers/Hausdorff.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
#include <thread>
#include <mutex>

double Hausdorff::Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) {
	return HausdorffDistance(seq1,seq2);

}

double Hausdorff::HausdorffDistance(const CoordinateSequence& setA, const CoordinateSequence& setB) {
    double maxDistanceAB = 0.0;
    std::mutex mtx;

    // Vector para almacenar las distancias m�nimas calculadas por cada hilo
    std::vector<double> minDistances(setA.points.size(), std::numeric_limits<double>::infinity());

    // Funci�n para calcular la distancia m�nima de un punto de setA a todos los puntos de setB
    auto calculateMinDistanceB = [&](int index) {
        double minDistanceB = std::numeric_limits<double>::infinity();
        for (const auto& pointB : setB.points) {
            double distance = distanceBetweenPoints(setA.points[index], pointB);
            minDistanceB = std::min(minDistanceB, distance);
        }
        minDistances[index] = minDistanceB;
        };

    std::vector<std::thread> threads;
    for (int i = 0; i < setA.points.size(); ++i) {
        threads.emplace_back(calculateMinDistanceB, i);
    }

    for (auto& t : threads) {
        t.join();
    }

    for (double distance : minDistances) {
        maxDistanceAB = std::max(maxDistanceAB, distance);
    }

    return maxDistanceAB;
}
