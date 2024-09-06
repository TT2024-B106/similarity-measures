# Existing imports and setup code
import json
import cppyy
import time
import matplotlib.pyplot as plt
import random
import numpy as np
import mplcursors
from collections import defaultdict

# Load shared libraries and include headers
cppyy.load_library('../build/libdtw.so')
cppyy.include('../src/DTW.h')
cppyy.include('../src/Algoritmos.h')
cppyy.include('../src/Coordinates.h')

lib = cppyy.gbl
DTW = lib.DTW
CoordinateSequence = lib.CoordinateSequence
Coordinate = lib.Point

def load_sequence(index, data):
    for item in data['data']:
        for feature in item['features']:
            if index == 0:
                coordinates = feature['geometry']['coordinates']
                sequence = CoordinateSequence()
                for coord in coordinates:
                    sequence.points.push_back(Coordinate(coord[1], coord[0]))  
                return sequence
            index -= 1

def main():
    with open('ECATEPEC.json', 'r') as f:
        data = json.load(f)
    
    total_sequences = sum(len(item['features']) for item in data['data'])

    max_coords = 0
    for i in range(total_sequences):
        sequence = load_sequence(i, data)
        num_coords = len(sequence.points)
        if num_coords > max_coords:
            max_coords = num_coords

    num_objects = 10
    num_comparisons = 1000

    strategy = DTW()
    execution_times_by_coords = defaultdict(list)

    for _ in range(num_objects):
        index_to_compare = random.randint(0, total_sequences - 1)
        sequence_to_compare = load_sequence(index_to_compare, data)
        
        for _ in range(num_comparisons):
            index_to_compare_with = random.randint(0, total_sequences - 1)
            if index_to_compare_with == index_to_compare:
                continue
            sequence2 = load_sequence(index_to_compare_with, data)

            start_execute_time = time.time()
            result = strategy.Execute(sequence_to_compare, sequence2)
            end_execute_time = time.time()

            execute_time = end_execute_time - start_execute_time
            num_coords2 = len(sequence2.points)

            if num_coords2 <= max_coords:
                execution_times_by_coords[num_coords2].append(execute_time)

    avg_execution_times = {coords: np.mean(times) for coords, times in execution_times_by_coords.items()}
    sorted_coords = sorted(avg_execution_times.keys())
    avg_times = [avg_execution_times[coords] for coords in sorted_coords]

    overall_avg_time_cpp = np.mean([time for times in execution_times_by_coords.values() for time in times])
    print(f"{overall_avg_time_cpp:.6f}")

    plt.figure(figsize=(12, 6))
    plt.plot(sorted_coords, avg_times, label='Average Execution Time (C++)')
    plt.xlabel('Number of Coordinates')
    plt.ylabel('Time (seconds)')
    # Updated title to include overall average execution time
    plt.title(f'Average Execution Time vs Number of Coordinates (C++)\nOverall Average Time: {overall_avg_time_cpp:.6f} seconds')
    plt.legend()
    plt.tight_layout()
    mplcursors.cursor(hover=True)
    plt.show()

if __name__ == "__main__":
    main()

