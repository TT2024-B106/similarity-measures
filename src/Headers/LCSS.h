#pragma once
#include <iostream>
#include "Algoritmos.h"

class LCSS : public Algoritmo {
public:
    int Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2, std::vector<int>& subsequenceIndices);
    double Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2);

private:
    void CalculateLCSSMatrix(const CoordinateSequence& seq1, const CoordinateSequence& seq2, std::vector<std::vector<int>>& lcssMatrix);
    void BuildLCSS (const CoordinateSequence& seq1, const CoordinateSequence& seq2, const std::vector<std::vector<int>>& lcssMatrix, std::vector<int>& subsequenceIndices);
    int GetLCSS(const CoordinateSequence& seq1, const CoordinateSequence& seq2, std::vector<int>& subsequenceIndices);
};
