// algoritmo.cpp

#include "algoritmos.h"
#include <cmath>

double distanceAbsolut(double x, double y) {
    return std::abs(x - y);
}

double distanceBetweenPoints(const Point& point1, const Point& point2) {
    double latDistance = distanceAbsolut(point1.latitude, point2.latitude);
    double longDistance = distanceAbsolut(point1.longitude, point2.longitude);
    return std::sqrt(latDistance * latDistance + longDistance * longDistance);
}

