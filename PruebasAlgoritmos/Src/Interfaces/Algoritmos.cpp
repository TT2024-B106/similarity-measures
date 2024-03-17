#include "../../Headers/Algoritmos.h"
#include <cmath>  

Algoritmos::~Algoritmos() {}

double Algoritmos::distanceAbsolut(double x, double y) {
    return std::abs(x - y);
}
double Algoritmos::distanceBetweenPoints(const Point& point1, const Point& point2) {
    double deltaX = point2.latitude - point1.latitude;
    double deltaY = point2.longitude - point1.longitude;

    double distance = std::sqrt(deltaX * deltaX + deltaY * deltaY);

    return distance;
}
