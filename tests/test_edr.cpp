#include <iostream>
#include <cstring>

#include "../src/edit_distance.h"

/*
 * To run this:
 * > make test-edr
*/

int main(int argc, char* argv[]) {
	// std::vector<double> p = {1.0, 2.0}; // (x_1, y_1)
	// std::vector<double> q = {3.0, 4.0}; // (x_2, y_2)

	if (argc > 1 && strcmp(argv[1], "-d") == 0) {
		debug_enabled = true;
	}

	std::vector<double> p = {2, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6};
	std::vector<double> q = {1, 2, 2, 3, 3, 4, 4, 5, 5, 6};

	double res = edr_distance(p, q);
	if (res >= 0.0) {
		std::cout << "Edit Distance on Real sequence (EDR): "
			<< res << std::endl;
	}

	return 0;
}
