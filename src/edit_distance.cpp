#include "edit_distance.h"

#include <iostream>

bool debug_enabled = false;

void print_matrix(const std::vector<std::vector<double>>& matrix) {
	for (const std::vector<double>& row : matrix) {
		for (const double& value : row) {
      			std::cout << value << "\t";
		}
		std::cout << std::endl;
	}
}

void print_vector(const std::vector<double>& v) {
	std::cout << "[ ";

	for (const double& element : v) {
		std::cout << element << " ";
	}

	std::cout << "]" << std::endl;
}

void debug_mahnhattan_distance(
	const std::vector<double>& r, const std::vector<double>& s,
	int irx, int iry, int jsx, int jsy,
	double mdx, double mdy, double subcost
){
	std::cout << "md( (" << r[irx] << "," << r[iry];
	std::cout << "),(";
	std::cout << s[jsx] << "," << s[jsy] << ") )";

	std::cout << " => ";

	std::cout << "mdx(" << r[irx] << "," << s[jsx] << ")=";
	std::cout << mdx << "; ";

	std::cout << "mdy(" << r[iry] << "," << s[jsy] << ")=";
	std::cout << mdy;

	std::cout << " | subcost=" << subcost;

	std::cout << std::endl;
}

double edr_distance(
	const std::vector<double>& r, const std::vector<double>& s,
	double sigma, double cost_del, double cost_ins
){
	size_t m = r.size();
	size_t n = s.size();
	
	if (debug_enabled) {
		std::cout << "Vector r of size m=" << m << ":" << std::endl;
		print_vector(r);
		std::cout << "Vector s of size n=" << n << ":" << std::endl;
		print_vector(s);
	}

	// Dynamic Programming table
	int rows = ((m + 1) / 2) + 1;
	int cols = ((n + 1) / 2) + 1;
	std::vector<std::vector<double>> dp(
		rows, std::vector<double>(
			cols, std::numeric_limits<double>::infinity()
		)
	);

	// Base cases
	dp[0][0] = 0;

	// m == 0
	for (int i = 1; i < rows; i++) {
		dp[i][0] = n;
		// dp[i][0] = i; // Papers define: n if m = 0
	}
	// n == 0
	for (int i = 1; i < cols; i++) {
		dp[0][i] = m;
		// dp[0][i] = i; // Papers define: m if n = 0
	}

	// Filling the DP
	for (int i = 1; i < rows; i++) {
		for (int j = 1; j < cols; j++) {
			int irx = 2*(i-1)+0, iry = 2*(i-1)+1;
			int jsx = 2*(j-1)+0, jsy = 2*(j-1)+1;

			double mdx = manhattan_distance(r[irx], s[jsx]);
			double mdy = manhattan_distance(r[iry], s[jsy]);

			double subcost = (mdx<=sigma && mdy<=sigma) ? 0.0 : 1.0;

			double min_cost = std::numeric_limits<double>::infinity();
			min_cost = std::min(min_cost, dp[i - 1][j - 1] + subcost);

			// Deletion from R
			min_cost = std::min(min_cost, dp[i - 1][j] + cost_del);

			// Insertion into S
			min_cost = std::min(min_cost, dp[i][j - 1] + cost_ins);

			dp[i][j] = min_cost;

			if (debug_enabled) {
				debug_mahnhattan_distance(
					r, s, irx, iry, jsx, jsy, mdx, mdy, subcost
				);
			}
		}
	}

	if (debug_enabled) print_matrix(dp);

	return dp[rows-1][cols-1];
}
