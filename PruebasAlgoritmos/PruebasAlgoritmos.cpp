#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>  
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include "coordinates.h"
#include "Algoritmos.h"
#include "DTW.h"

using namespace rapidjson;
using namespace std;




int main() {


	CoordinateSequence sequence1{ {{1.0, 2.0} ,{3.0, 2.0}, {4.0, 3.0}, {9.0, 4.5}, {8.0, 4.5}, {2.0, 4.5}, {1.0, 4.5}, {5.0, 4.5}, {7.0, 4.5}, {3.0, 4.5}} };
	//CoordinateSequence sequence2{ {{1.0, 2.0} ,{3.0, 2.0}, {4.0, 3.0}, {9.0, 4.5}, {8.0, 4.5}, {2.0, 4.5}, {1.0, 4.5}, {5.0, 4.5}, {7.0, 4.5}, {3.0, 4.5}} };
	CoordinateSequence sequence2{ {{1.0, 2.0} ,{6.0, 2.5}, {2.0, 3.5}, {3.0, 4.5}, {0.0, 4.5},{9.0, 4.5},{4.0, 4.5},{3.0, 4.5}, {6.0, 4.5}, {3.0, 4.5}} };
	

	Algoritmos* strategy = new DTW();

	double result = strategy->Execute(sequence1, sequence2);
	
	delete strategy;



	std::cout << "Distancia DTW: " << result << std::endl;

	return 0;
}