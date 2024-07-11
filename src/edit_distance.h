#ifndef ED_H
#define ED_H

#include "manhattan.h"
#include <limits>
#include <algorithm>

extern bool debug_enabled;

double edr_distance(
	const std::vector<double>& r, const std::vector<double>& s,
	double sigma = 1.0, double cost_del = 1.0, double cost_ins = 1.0
);

#endif  // ED_H
