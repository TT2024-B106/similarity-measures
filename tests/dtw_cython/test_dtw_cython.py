import json
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import mplcursors
from collections import defaultdict
import dtw_module  # Importar el módulo Cython

def load_sequence(index, data):
    for item in data['data']:
        for feature in item['features']:
            if index == 0:
                coordinates = feature['geometry']['coordinates']
                return [(coord[1], coord[0]) for coord in coordinates]
            index -= 1

def main():
    with open('ECATEPEC.json', 'r') as f:
        data = json.load(f)

    total_sequences = sum(len(item['features']) for item in data['data'])

    max_coords = 0
    for i in range(total_sequences):
        sequence = load_sequence(i, data)
        num_coords = len(sequence)
        if num_coords > max_coords:
            max_coords = num_coords

    num_objects = 10
    num_comparisons = 1000
    execution_times_by_coords_cython = defaultdict(list)

    for _ in range(num_objects):
        index_to_compare = random.randint(0, total_sequences - 1)
        sequence_to_compare = load_sequence(index_to_compare, data)
        
        for _ in range(num_comparisons):
            index_to_compare_with = random.randint(0, total_sequences - 1)
            if index_to_compare_with == index_to_compare:
                continue
            sequence2 = load_sequence(index_to_compare_with, data)

            start_execute_time = time.time()
            dtw_module.calculate_dtw(sequence_to_compare, sequence2)  # Llamada a la función de Cython
            end_execute_time = time.time()

            execute_time = end_execute_time - start_execute_time
            num_coords2 = len(sequence2)

            if num_coords2 <= max_coords:
                execution_times_by_coords_cython[num_coords2].append(execute_time)

    avg_execution_times_cython = {coords: np.mean(times) for coords, times in execution_times_by_coords_cython.items()}
    sorted_coords = sorted(avg_execution_times_cython.keys())
    avg_times_cython = [avg_execution_times_cython[coords] for coords in sorted_coords]

    overall_avg_time_cython = np.mean([time for times in execution_times_by_coords_cython.values() for time in times])
    print(f"{overall_avg_time_cython:.6f}")

    plt.figure(figsize=(12, 6))
    plt.plot(sorted_coords, avg_times_cython, label='Cython Average Execution Time')
    plt.xlabel('Number of Coordinates')
    plt.ylabel('Time (seconds)')
    plt.title('Average Execution Time vs Number of Coordinates (Cython)')
    plt.legend()
    plt.tight_layout()
    mplcursors.cursor(hover=True)
    plt.show()

if __name__ == "__main__":
    main()
