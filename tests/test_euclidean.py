import json
import cppyy
import time
import matplotlib.pyplot as plt
import random
import numpy as np
import mplcursors

# Cargar la biblioteca C++
cppyy.load_library('../build/libeuclidean.so')
cppyy.include('../src/Headers/euclidean.h')

lib = cppyy.gbl
euclidean_distance = lib.distance


with open('ECATEPEC.json', 'r') as f:
    data = json.load(f)
total_sequences = sum(len(item['features']) for item in data['data'])


def load_sequence(index):
    for item in data['data']:
        for feature in item['features']:
            if index == 0:
                coordinates = feature['geometry']['coordinates']
                sequence = [coord for coord in coordinates]  
                return sequence
            index -= 1


n = 9000


random_index = random.randint(0, total_sequences - 1)
sequence = load_sequence(random_index)
random_coord = random.choice(sequence)


all_coordinates = []
for i in range(total_sequences):
    if i != random_index:  
        sequence = load_sequence(i)
        all_coordinates.extend(sequence)
    if len(all_coordinates) >= n:
        break


if len(all_coordinates) < n:
    raise ValueError(f"No hay suficientes coordenadas disponibles para seleccionar {n} coordenadas")


random.shuffle(all_coordinates)
selected_coordinates = all_coordinates[:n]

# Variables para acumular tiempos
execution_times = []


for k in range(1, n + 1):
    coord1 = [random_coord[0]]  
    coord2 = [selected_coordinates[k-1][0]]  

    start_execute_time = time.time()
    result = euclidean_distance(coord1, coord2)
    end_execute_time = time.time()

    execute_time = end_execute_time - start_execute_time
    execution_times.append(execute_time)


average_execution_time = np.mean(execution_times)

print(f"Media del tiempo de ejecución para {n} comparaciones: {average_execution_time} segundos")


plt.figure(figsize=(12, 6))


plt.plot(range(200, n + 1), execution_times[199:], label='Execution Time per Comparison')
plt.xlabel('Number of Comparisons')
plt.ylabel('Time (seconds)')
plt.title(f'Execution Time for 1 to {n} Comparisons')
plt.legend()

plt.tight_layout()


mplcursors.cursor(hover=True)

plt.show()

