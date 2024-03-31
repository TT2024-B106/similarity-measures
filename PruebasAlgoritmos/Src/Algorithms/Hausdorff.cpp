#include <vector>
#include "Headers/Hausdorff.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

double Hausdorff::Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) {
	return HausdorffDistance(seq1,seq2);

}

double Hausdorff::HausdorffDistance(const CoordinateSequence& setA, const CoordinateSequence& setB) {
    double maxDistanceAB = 0.0;

    for (const auto& pointA : setA.points) {
        double minDistanceB = std::numeric_limits<double>::infinity();

        for (const auto& pointB : setB.points) {
            double distance = distanceBetweenPoints(pointA, pointB);
            minDistanceB = std::min(minDistanceB, distance);
        }

        maxDistanceAB = std::max(maxDistanceAB, minDistanceB);
    }

    double maxDistanceBA = 0.0;

    for (const auto& pointB : setB.points) {
        double minDistanceA = std::numeric_limits<double>::infinity();

        for (const auto& pointA : setA.points) {
            double distance = distanceBetweenPoints(pointB, pointA);
            minDistanceA = std::min(minDistanceA, distance);
        }

        maxDistanceBA = std::max(maxDistanceBA, minDistanceA);
    }

    return std::max(maxDistanceAB, maxDistanceBA);
}