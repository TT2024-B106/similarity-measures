#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <fstream>

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

int main() {
	using namespace std::chrono;

	std::ofstream outfile("distance_times.txt");  // Open output file

	if (!outfile.is_open()) {
		std::cerr << "Error: Could not open output file." << std::endl;
		return 1;
	}

	for (size_t input_size = 2; input_size <= 10000; ++input_size) {
		std::vector<double> p(input_size, 1.0);
		std::vector<double> q(input_size, 2.0);

		auto start = high_resolution_clock::now();
		distance(p, q);
		auto stop = high_resolution_clock::now();

		auto duration = duration_cast<nanoseconds>(stop - start);
		long long timens = duration.count();
		outfile << input_size << " " << timens << std::endl;
	}

	outfile.close();

	return 0;
}
