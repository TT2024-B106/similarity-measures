#ifndef DTW_H
#define DTW_H
#include <iostream>
#include "Algoritmos.h"

class DTW : public Algoritmo
{
public:
	double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2);

private:
	std::vector<std::vector<double>> CalculateDTWMatrix(const CoordinateSequence& seq1, const CoordinateSequence& seq2);
	std::vector<std::pair<int, int>> CalculateOptimalPath(const std::vector<std::vector<double>>& accumulatedCost);
	double CalculateCostFromOptimalPath(const std::vector<std::vector<double>>& accumulatedCost, const std::vector<std::pair<int, int>>& optimalPath);
};
#endif
