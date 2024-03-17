#pragma once
#include <iostream>
#include "Algoritmos.h"


class Hausdorff : public Algoritmos
{
public:
	double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2);

private:
	double HausdorffDistance(const CoordinateSequence& setA, const CoordinateSequence& setB);
};

