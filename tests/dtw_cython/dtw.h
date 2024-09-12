// dtw.h
#ifndef DTW_H
#define DTW_H

#include <iostream>
#include <vector>
#include "Coordinates.h"

// Prototipos de funciones DTW
double ExecuteDTW(const CoordinateSequence& seq1, const CoordinateSequence& seq2);
std::vector<std::vector<double>> CalculateDTWMatrix(const CoordinateSequence& seq1, const CoordinateSequence& seq2);
std::vector<std::pair<int, int>> CalculateOptimalPath(const std::vector<std::vector<double>>& accumulatedCost);
double CalculateCostFromOptimalPath(const std::vector<std::vector<double>>& accumulatedCost, const std::vector<std::pair<int, int>>& optimalPath);

#endif

