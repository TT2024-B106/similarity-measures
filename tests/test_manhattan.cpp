#include <iostream>

#include "../src/manhattan.h"

/*
 * To run this:
 * > make
 * > mv libmanhattan.so build/
 * > export LD_LIBRARY_PATH=./build:$LD_LIBRARY_PATH
 * > g++ tests/test_manhattan.cpp -L./build -lmanhattan
 * > ./a.out
*/

int main() {
	// Sample arrays
	std::vector<double> p = {1.0, 2.0}; // (x_1, y_1)
	std::vector<double> q = {3.0, 4.0}; // (x_2, y_2)

	double res = distance(p, q);
	if (res >= 0.0) {
		std::cout << "Manhattan Distance: " << res << std::endl;
	}

	return 0;
}
