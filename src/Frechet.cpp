#include <iostream>
#include <vector>
#include <cmath>
#include "Headers/Frechet.h"



double euclideanDistance(const Point& p1, const Point& p2) {
    double dx = p1.latitude - p2.latitude;
    double dy = p1.longitude - p2.longitude;
    return sqrt(dx * dx + dy * dy);
}

double Frechet::Execute(const CoordinateSequence& seq1, const CoordinateSequence& seq2) {
    return frechetDistance(seq1, seq2);
}

double Frechet::frechetDistance(const CoordinateSequence & seq1, const CoordinateSequence & seq2) {
    int m = seq1.points.size();
    int n = seq2.points.size();

    std::vector<std::vector<double>> M(m + 1, std::vector<double>(n + 1, std::numeric_limits<double>::infinity()));

    M[0][0] = euclideanDistance(seq1.points[0], seq2.points[0]);

    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            double dist = euclideanDistance(seq1.points[i], seq2.points[j]);
            M[i][j] = std::max(dist, std::min({ M[i - 1][j], M[i][j - 1], M[i - 1][j - 1] }));
        }
    }

    return M[m - 1][n - 1]; 
}


