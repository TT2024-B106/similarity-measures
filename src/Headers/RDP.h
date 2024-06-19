#pragma once
#include <iostream>
#include "Algoritmos.h"

class RDP : public Algoritmo {
public:
    CoordinateSequence Execute(const CoordinateSequence& input, double tolerance);
    double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2);

private:
    double perpendicularDistance(const Point& p, const Point& lineStart, const Point& lineEnd);
    void simplifyLine(const CoordinateSequence& input, double tolerance, CoordinateSequence& output);
};
