import json
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import mplcursors
from collections import defaultdict
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, size
from pyspark.sql.types import DoubleType, ArrayType, StructType, StructField, FloatType


spark = SparkSession.builder.appName("DTWBenchmark").getOrCreate()

with open('ECATEPEC.json', 'r') as f:
    data = json.load(f)

sequences = []
for item in data['data']:
    for feature in item['features']:
        coordinates = feature['geometry']['coordinates']
        sequences.append([coordinates])

schema = StructType([
    StructField("coordinates", ArrayType(ArrayType(FloatType())), True)
])

df = spark.createDataFrame(sequences, schema)

# Función para convertir lista de coordenadas en secuencia de coordenadas
def coordinates_to_sequence(coords):
    return [(coord[1], coord[0]) for coord in coords]

convert_to_sequence_udf = udf(coordinates_to_sequence, ArrayType(StructType([
    StructField("lat", DoubleType(), True),
    StructField("lon", DoubleType(), True)
])))

df = df.withColumn("sequence", convert_to_sequence_udf(df.coordinates)).drop("coordinates")

# Encontrar el máximo número de coordenadas en las secuencias
max_coords = df.select(size(col("sequence")).alias("size")).agg({"size": "max"}).collect()[0][0]

# Implementar DTW en PySpark
def dtw_distance(seq1, seq2):
    n, m = len(seq1), len(seq2)
    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = float('inf')
    dtw_matrix[0, 0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = np.sqrt((seq1[i-1][0] - seq2[j-1][0])**2 + (seq1[i-1][1] - seq2[j-1][1])**2)
            dtw_matrix[i, j] = cost + min(dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1])
    return float(dtw_matrix[n, m])

dtw_udf = udf(dtw_distance, DoubleType())

# Medir tiempos de ejecución
execution_times_by_coords = defaultdict(list)

total_sequences = df.count()
num_objects = 10
num_comparisons = 1000

# Crear una lista con las secuencias para evitar múltiples llamadas a collect()
sequences_list = df.select("sequence").rdd.map(lambda row: row.sequence).collect()

for _ in range(num_objects):
    index_to_compare = random.randint(0, total_sequences - 1)
    sequence_to_compare = sequences_list[index_to_compare]
    
    for _ in range(num_comparisons):
        index_to_compare_with = random.randint(0, total_sequences - 1)
        if index_to_compare_with == index_to_compare:
            continue
        sequence2 = sequences_list[index_to_compare_with]
        
        start_execute_time = time.time()
        distance = dtw_distance(sequence_to_compare, sequence2)
        end_execute_time = time.time()
        
        execute_time = end_execute_time - start_execute_time
        num_coords2 = len(sequence2)
        
        if num_coords2 <= max_coords:
            execution_times_by_coords[num_coords2].append(execute_time)

# Calcular tiempos promedio
avg_execution_times = {coords: np.mean(times) for coords, times in execution_times_by_coords.items()}
sorted_coords = sorted(avg_execution_times.keys())
avg_times = [avg_execution_times[coords] for coords in sorted_coords]


plt.figure(figsize=(12, 6))
plt.plot(sorted_coords, avg_times, label='Average Execution Time')
plt.xlabel('Number of Coordinates')
plt.ylabel('Time (seconds)')
plt.title('Average Execution Time vs Number of Coordinates (PySpark)')
plt.legend()
plt.tight_layout()

mplcursors.cursor(hover=True)
plt.show()
spark.stop()

