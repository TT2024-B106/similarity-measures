#pragma once
#include "Coordinates.h"

class Algoritmos {
public:
    virtual double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) = 0;
    virtual ~Algoritmos();
    double distanceAbsolut(double x, double y);
    double distanceBetweenPoints(const Point& point1, const Point& point2);
};
