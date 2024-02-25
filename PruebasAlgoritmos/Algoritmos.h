#pragma once
#include "coordinates.h"
class Algoritmos
{

public:
	virtual double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) = 0;
	virtual ~Algoritmos() {}
	double EuclideanDistance(Point p1, Point p2)
	{
		return sqrt(pow(p1.latitude - p2.latitude, 2) + pow(p1.longitude - p2.longitude, 2));
	}
	double distanceAbsolut(double x, double y) {
		double distancia = std::abs(x - y);
		return distancia;
	}
};

