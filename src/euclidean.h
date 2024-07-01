#ifndef DISTANCE_H
#define DISTANCE_H

#include <cmath>
#include <cstddef>

// Function to calculate Euclidean distance between two double vectors
double distance(double* p, double* q, size_t size);

// C euclidean distance function
extern "C" {
  double euclidean_distance(double* p, double* q, size_t size);
}

#endif  // DISTANCE_H
