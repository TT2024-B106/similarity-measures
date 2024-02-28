#include <iostream>

#include "../src/euclidean.h"

/*
 * To run this:
 * > export LD_LIBRARY_PATH=./build:$LD_LIBRARY_PATH
 * > g++ tests/test_euclidean.cpp -L./build -leuclidean
 * > ./a.out
*/

int main() {
	// Sample arrays
	std::vector<double> p = {1.0, 2.0}; // (x_1, y_1)
	std::vector<double> q = {3.0, 4.0}; // (x_2, y_2)

	double res = distance(p, q);
	if (res >= 0.0) {
		std::cout << "Distance: " << res << std::endl;
	}

	return 0;
}
