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
	// std::vector<double> p = {1.0, 2.0}; // (x_1, y_1)
	// std::vector<double> q = {3.0, 4.0}; // (x_2, y_2)

	std::vector<double> p = {1.4231, 2.123}; // (x_1, y_1)
	std::vector<double> q = {10.213, 11.123}; // (x_2, y_2)

	double res = manhattan_distance(p, q);
	if (res >= 0.0) {
		std::cout << "Manhattan Distance: " << res << std::endl;
	}

	return 0;
}
