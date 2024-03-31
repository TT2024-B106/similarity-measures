#pragma once
#include "Coordinates.h"

class Algoritmo {
public:
    virtual double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) = 0;
    virtual ~Algoritmo();
    double distanceAbsolut(double x, double y);
    double distanceBetweenPoints(const Point& point1, const Point& point2);
};
