import json
import cppyy
import time
import matplotlib.pyplot as plt
import random
import numpy as np
import mplcursors

# ------------------------------------------------------------
# Script para medir y graficar tiempos de ejecución de DTW
# ------------------------------------------------------------
# Este script realiza lo siguiente:
# 1. Carga datos de secuencias de coordenadas desde un archivo JSON.
# 2. Utiliza el algoritmo Dynamic Time Warping (DTW) para comparar
#    secuencias de coordenadas.
# 3. Mide los tiempos de ejecución de las comparaciones.
# 4. Calcula los tiempos de ejecución promedio y el número promedio
#    de coordenadas para un conjunto de secuencias.
# 5. Grafica los resultados, mostrando el tiempo de ejecución promedio
#    y el número promedio de coordenadas por objeto.
# ------------------------------------------------------------

cppyy.load_library('../build/libdtw.so')
cppyy.include('../src/Headers/DTW.h')
cppyy.include('../src/Headers/Algoritmos.h')
cppyy.include('../src/Headers/Coordinates.h')

lib = cppyy.gbl
DTW = lib.DTW
CoordinateSequence = lib.CoordinateSequence
Coordinate = lib.Point

with open('ECATEPEC.json', 'r') as f:
    data = json.load(f)

sequences = []
for item in data['data']:
    for feature in item['features']:
        coordinates = feature['geometry']['coordinates']
        sequence = CoordinateSequence()
        for coord in coordinates:
            sequence.points.push_back(Coordinate(coord[1], coord[0]))  
        sequences.append(sequence)

num_objects = 10
num_comparisons = 1000
if len(sequences) < 6000:
    raise ValueError("El archivo JSON debe contener al menos 6000 secuencias de coordenadas")

strategy = DTW()

execution_times = []
coordinate_counts = []
average_execution_times = []
average_coordinate_counts = []

for index_to_compare in range(num_objects):
    sequence_to_compare = sequences[index_to_compare]

    total_execute_time = 0
    total_coordinates = len(sequence_to_compare.points)

    for _ in range(num_comparisons):
        index_to_compare_with = random.randint(0, len(sequences) - 1)
        if index_to_compare_with == index_to_compare:
            continue  
        sequence2 = sequences[index_to_compare_with]

        start_execute_time = time.time()
        result = strategy.Execute(sequence_to_compare, sequence2)
        end_execute_time = time.time()

        execute_time = end_execute_time - start_execute_time
        total_execute_time += execute_time

        num_coords1 = len(sequence_to_compare.points)
        num_coords2 = len(sequence2.points)
        total_coordinates += num_coords2
        
        execution_times.append(execute_time)
        coordinate_counts.append(num_coords2)

    average_execute_time = total_execute_time / num_comparisons
    average_coordinates = total_coordinates / num_comparisons

    average_execution_times.append(average_execute_time)
    average_coordinate_counts.append(average_coordinates)

x = np.arange(num_objects)
z = np.polyfit(x, average_execution_times, 1)
p = np.poly1d(z)

print(f"Media del tiempo de ejecución de la estrategia (para 100 objetos): {sum(average_execution_times) / num_objects} segundos")
print(f"Media del número de coordenadas (para 100 objetos): {sum(average_coordinate_counts) / num_objects}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
execution_time_plot, = plt.plot(average_execution_times, label='Average Execution Time')
plt.scatter(x, average_execution_times)
plt.plot(x, p(x), "r--", label='Trend Line')
plt.xlabel('Object Index')
plt.ylabel('Time (seconds)')
plt.title('Average Execution Time per Object')
plt.legend()

plt.subplot(1, 2, 2)
coordinate_count_plot, = plt.plot(average_coordinate_counts, label='Average Coordinate Count', color='orange')
plt.scatter(x, average_coordinate_counts, color='orange')
plt.xlabel('Object Index')
plt.ylabel('Number of Coordinates')
plt.title('Average Number of Coordinates per Object')
plt.legend()

plt.tight_layout()

mplcursors.cursor(execution_time_plot, hover=True)
mplcursors.cursor(coordinate_count_plot, hover=True)

plt.show()
