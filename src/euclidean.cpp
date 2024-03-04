#include <iostream>

#include "euclidean.h"

double distance(const std::vector<double>& p,
		const std::vector<double>& q)
{
	// Check if arrays have the same size
	if (p.size() != q.size()) {
		std::cerr << "Error: Arrays must have the same size." << std::endl;
		return -1.0; // Return an error value
	}

	double sum_of_squares = 0.0;
	for (size_t i = 0; i < p.size(); ++i) {
		double diff = p[i] - q[i];
		sum_of_squares += diff * diff;
	}

	return sqrt(sum_of_squares);
}
