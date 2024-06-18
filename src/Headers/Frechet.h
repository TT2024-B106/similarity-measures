#pragma once
#include <iostream>
#include "Algoritmos.h"

class Frechet : public Algoritmo
{
public:
	double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2);

private:
	double frechetDistance(const CoordinateSequence& seq1, const CoordinateSequence& seq2);
};