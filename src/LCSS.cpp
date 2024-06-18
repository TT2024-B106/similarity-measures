#include <vector>
#include "Headers/LCSS.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
#include <thread>
#include <mutex>


void LCSS::CalculateLCSSMatrix(const CoordinateSequence& seq1, const CoordinateSequence& seq2, std::vector<std::vector<int>>& lcssMatrix) {
    int m = seq1.points.size(); 
    int n = seq2.points.size(); 

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (seq1.points[i - 1].latitude == seq2.points[j - 1].latitude &&
                seq1.points[i - 1].longitude == seq2.points[j - 1].longitude) {
                lcssMatrix[i][j] = 1 + lcssMatrix[i - 1][j - 1];
            }
            else {
                lcssMatrix[i][j] = std::max(lcssMatrix[i - 1][j], lcssMatrix[i][j - 1]);
            }
        }
    }
}

void LCSS::BuildLCSS(const CoordinateSequence& seq1, const CoordinateSequence& seq2, const std::vector<std::vector<int>>& lcssMatrix, std::vector<int>& subsequenceIndices) {
    int i = seq1.points.size(), j = seq2.points.size(); 
    while (i > 0 && j > 0) {
        if (seq1.points[i - 1].latitude == seq2.points[j - 1].latitude &&
            seq1.points[i - 1].longitude == seq2.points[j - 1].longitude) {
            subsequenceIndices.push_back(i - 1); 
            --i;
            --j;
        }
        else if (lcssMatrix[i - 1][j] > lcssMatrix[i][j - 1]) {
            --i;
        }
        else {
            --j;
        }
    }


    std::reverse(subsequenceIndices.begin(), subsequenceIndices.end());
}

int LCSS::GetLCSS(const CoordinateSequence& seq1, const CoordinateSequence& seq2, std::vector<int>& subsequenceIndices) {
    int m = seq1.points.size(); 
    int n = seq2.points.size(); 

    std::vector<std::vector<int>> lcssMatrix(m + 1, std::vector<int>(n + 1, 0));

    CalculateLCSSMatrix(seq1, seq2, lcssMatrix);

    BuildLCSS(seq1, seq2, lcssMatrix, subsequenceIndices);

    return lcssMatrix[m][n];
}

int LCSS::Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2, std::vector<int>& subsequenceIndices) {
    int lcssValue = GetLCSS(seq1, seq2, subsequenceIndices);
    return lcssValue;
}
double LCSS::Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) {
 
    return 0;
}