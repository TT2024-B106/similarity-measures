#include "euclidean.h"

double distance(double* p, double* q, size_t size)
{
	double sum_of_squares = 0.0;

	for (size_t i = 0; i < size; ++i) {
		double diff = p[i] - q[i];
		sum_of_squares += diff * diff;
	}

	return sqrt(sum_of_squares);
}

extern "C" {
	double euclidean_distance(double* p, double* q, size_t size)
	{
		return distance(p, q, size);
	}
}
