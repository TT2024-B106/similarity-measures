#include <iostream>

#include "../src/Headers/DTW.h"

int main() {
    CoordinateSequence sequence1{ {{1.0, 2.0}, {3.0, 2.5}, {5.0, 3.5}, {7.0, 6.0}, {9.0, 7.0}, {11.0, 8.0}, {13.0, 8.5}, {15.0, 9.0}, {17.0, 9.5}, {19.0, 9.5}} };
    CoordinateSequence sequence2{ {{1.0, 2.0}, {3.0, 2.5}, {5.0, 3.5}, {7.0, 6.0}, {9.0, 7.0}, {11.0, 8.0}, {13.0, 8.5}, {15.0, 9.0}, {17.0, 9.5}, {1500.0, 8.0}} };
    
    Algoritmo* strategy = new DTW();
    double result = strategy->Execute(sequence1, sequence2);
    std::cout << "DTW: " << result << std::endl;
    
    delete strategy; // Liberar memoria
    
    return 0;
 }

