#include "manhattan.h"

double manhattan_distance(double a, double b) {
	return std::abs(b - a);
}

double manhattan_distance(
	const std::vector<double>& p, const std::vector<double>& q
){
	if (p.size() != q.size()) {
		throw std::invalid_argument("Points must have the same dimensionality");
	}

	double distance = 0.0;
	for (size_t i = 0; i < p.size(); ++i) {
		distance += std::abs(p[i] - q[i]);
	}

	return distance;
}
