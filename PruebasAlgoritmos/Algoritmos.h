#pragma once
#include "coordinates.h"
class Algoritmos
{

public:
	virtual double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) = 0;
	virtual ~Algoritmos() {}
	double distanceAbsolut(double x, double y) {
		double distancia = std::abs(x - y);
		return distancia;
	}
};

