#include <vector>
#include "Headers/RDP.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
#include <thread>
#include <mutex>


double RDP::perpendicularDistance(const Point& p, const Point& lineStart, const Point& lineEnd) {
    double dx = lineEnd.longitude - lineStart.longitude;
    double dy = lineEnd.latitude - lineStart.latitude;

    if (dx == 0 && dy == 0) {
        return std::sqrt(std::pow(p.longitude - lineStart.longitude, 2) + std::pow(p.latitude - lineStart.latitude, 2));
    }

    double u = ((p.longitude - lineStart.longitude) * dx + (p.latitude - lineStart.latitude) * dy) / (dx * dx + dy * dy);

    if (u < 0) {
        return std::sqrt(std::pow(p.longitude - lineStart.longitude, 2) + std::pow(p.latitude - lineStart.latitude, 2));
    }
    if (u > 1) {
        return std::sqrt(std::pow(p.longitude - lineEnd.longitude, 2) + std::pow(p.latitude - lineEnd.latitude, 2));
    }

    double x = lineStart.longitude + u * dx;
    double y = lineStart.latitude + u * dy;
    return std::sqrt(std::pow(p.longitude - x, 2) + std::pow(p.latitude - y, 2));
}

void RDP::simplifyLine(const CoordinateSequence& input, double tolerance, CoordinateSequence& output) {
    if (input.points.size() < 2) {
        output = input;
        return;
    }

    // Encontrar el punto con la mayor distancia perpendicular
    double maxDistance = 0;
    size_t maxIndex = 0;
    const Point& start = input.points.front();
    const Point& end = input.points.back();

    for (size_t i = 1; i < input.points.size() - 1; ++i) {
        double distance = perpendicularDistance(input.points[i], start, end);
        if (distance > maxDistance) {
            maxDistance = distance;
            maxIndex = i;
        }
    }

    // Si la distancia máxima es mayor que la tolerancia, recursivamente simplificar
    if (maxDistance > tolerance) {
        CoordinateSequence leftSubsequence{ std::vector<Point>(input.points.begin(), input.points.begin() + maxIndex + 1) };
        CoordinateSequence rightSubsequence{ std::vector<Point>(input.points.begin() + maxIndex, input.points.end()) };
        CoordinateSequence simplifiedLeft;
        CoordinateSequence simplifiedRight;
        simplifyLine(leftSubsequence, tolerance, simplifiedLeft);
        simplifyLine(rightSubsequence, tolerance, simplifiedRight);
        output.points = simplifiedLeft.points;
        output.points.insert(output.points.end(), simplifiedRight.points.begin() + 1, simplifiedRight.points.end());
    }
    else {
        output.points = { start, end };
    }
}

CoordinateSequence RDP::Execute(const CoordinateSequence& input, double tolerance) {
    CoordinateSequence output;
    simplifyLine(input, tolerance, output);
    return output;
}

double RDP::Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) {
    return 0;
}
