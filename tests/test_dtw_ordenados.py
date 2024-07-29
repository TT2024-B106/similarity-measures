import json
import cppyy
import time
import matplotlib.pyplot as plt
import random
import numpy as np
import mplcursors
from collections import defaultdict

# ------------------------------------------------------------
# Script para medir y graficar tiempos de ejecución de DTW
# ------------------------------------------------------------
# Este script realiza lo siguiente:
# 1. Carga datos de secuencias de coordenadas desde un archivo JSON.
# 2. Utiliza el algoritmo Dynamic Time Warping (DTW) para comparar
#    secuencias de coordenadas.
# 3. Mide los tiempos de ejecución de las comparaciones.
# 4. Calcula los tiempos de ejecución promedio para distintas
#    longitudes de secuencias de coordenadas.
# 5. Grafica los resultados, mostrando el tiempo de ejecución promedio
#    en función del número de coordenadas.
# ------------------------------------------------------------
# Diferencias con el script anterior:
# - Este script utiliza una función `load_sequence` para cargar
#   secuencias de coordenadas de manera individual, en lugar de 
#   cargarlas todas al inicio.
# - Calcula los tiempos de ejecución promedio agrupados por el
#   número de coordenadas en las secuencias.
# - Grafica los tiempos de ejecución promedio en función del número
#   de coordenadas, en lugar de hacerlo por índice de objeto.
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
total_sequences = sum(len(item['features']) for item in data['data'])
print(total_sequences)

def load_sequence(index):
    for item in data['data']:
        for feature in item['features']:
            if index == 0:
                coordinates = feature['geometry']['coordinates']
                sequence = CoordinateSequence()
                for coord in coordinates:
                    sequence.points.push_back(Coordinate(coord[1], coord[0]))  
                return sequence
            index -= 1

max_coords = 0
max_coords_index = 0
for i in range(total_sequences):
    sequence = load_sequence(i)
    num_coords = len(sequence.points)
    if num_coords > max_coords:
        max_coords = num_coords
        max_coords_index = i

num_objects = 10
num_comparisons = 1000
if total_sequences < 6000:
    raise ValueError("El archivo JSON debe contener al menos 6000 secuencias de coordenadas")

strategy = DTW()

execution_times_by_coords = defaultdict(list)

for _ in range(num_objects):
    index_to_compare = random.randint(0, total_sequences - 1)
    sequence_to_compare = load_sequence(index_to_compare)
    
    for _ in range(num_comparisons):
        index_to_compare_with = random.randint(0, total_sequences - 1)
        if index_to_compare_with == index_to_compare:
            continue
        sequence2 = load_sequence(index_to_compare_with)

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

plt.figure(figsize=(12, 6))
plt.plot(sorted_coords, avg_times, label='Average Execution Time')
plt.xlabel('Number of Coordinates')
plt.ylabel('Time (seconds)')
plt.title('Average Execution Time vs Number of Coordinates')
plt.legend()
plt.tight_layout()

mplcursors.cursor(hover=True)
plt.show()

