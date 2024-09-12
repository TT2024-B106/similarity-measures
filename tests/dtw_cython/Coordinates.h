#ifndef COORDINATES_H
#define COORDINATES_H

#include <vector>

struct Point {
    double latitude;
    double longitude;
};


struct CoordinateSequence {
    std::vector<Point> points;
};

#endif 
