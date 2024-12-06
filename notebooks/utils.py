import json
import random
import timeit
import stmeasures
import geojsonio
import shapely
import numpy as np
import matplotlib.pyplot as plt

def see_each_trajectory(geojson, start, end):
    for i in range(start, end):
        _ = geojsonio.display(stmeasures.geojsonio_contents(trajectory=geojson[i], indexes=[i]))

def get_trajectories(geojson, indexes):
    return [geojson[i] for i in indexes]

def see_trajectories(geojson, indexes):
    _ = geojsonio.display(
        stmeasures.geojsonio_contents(trajectories=get_trajectories(geojson, indexes), indexes=indexes)
    )

def calculate_all(t1, t2, convert=False, visualize=True):
    euclidean, hausdorff, frechet, dtw, lcss, erp, ers = -1, -1, -1, -1, -1, -1, -1

    if convert: t1, t2 = convert_to_same_size(t1, t2)
    
    try: euclidean = stmeasures.distance(t1, t2, stmeasures.Algorithms.EUCLIDEAN)
    except: print(f"Algoritmo euclideano no pudo ser calculado\n")
        
    try: hausdorff = stmeasures.distance(t1, t2, stmeasures.Algorithms.HAUSDORFF)
    except: print(f"Algoritmo Hausdorff no pudo ser calculado\n")
    
    try: frechet = stmeasures.distance(t1, t2, stmeasures.Algorithms.FRECHET)
    except: print(f"Algoritmo Frechet no pudo ser calculado\n")
    
    try: dtw = stmeasures.distance(t1, t2, stmeasures.Algorithms.DTW)
    except: print(f"Algoritmo DTW no pudo ser calculado\n")
    
    try: lcss = stmeasures.distance(t1, t2, stmeasures.Algorithms.LCSS)
    except: print(f"Algoritmo LCSS no pudo ser calculado\n")
    
    try: erp = stmeasures.distance(t1, t2, stmeasures.Algorithms.ERP)
    except: print(f"Algoritmo ERP no pudo ser calculado\n")
    
    try: ers = stmeasures.distance(t1, t2, stmeasures.Algorithms.ERS)
    except: print(f"Algoritmo ERS no pudo ser calculado\n")

    hausdorff = hausdorff_distance(t1, t2)
    frechet = frechet_distance(t1, t2)

    if euclidean > 0: print(f"Distancia Euclideana: {euclidean}")
    if hausdorff > 0: print(f"Distancia Hausdorff: {hausdorff}")
    if frechet > 0: print(f"Distancia Frechet: {frechet}")
    if dtw > 0: print(f"Distancia DTW: {dtw}")
    if lcss > 0: print(f"Distancia LCSS: {lcss}")
    if erp > 0: print(f"Distancia ERP: {erp}")
    if ers > 0: print(f"Distancia ERS: {ers}")

    if visualize:
        _ = geojsonio.display(stmeasures.geojsonio_contents(trajectories=[t1, t2]))

def convert_to_same_size(a, b):
    len_a, len_b = len(a), len(b)
    
    if len_a < len_b:
        return a, b[:len_a]
    return a[:len_b], b
    
def euclidean_distance(a, b):
    return stmeasures.distance(*convert_to_same_size(a, b))

def _linestring(coords):
    return '{"type": "LineString", "coordinates":' + str(coords) + '}'

def to_shapely(a, b):
    l1 = shapely.from_geojson(_linestring([[lat, lon] for lat, lon in a]))
    l2 = shapely.from_geojson(_linestring([[lat, lon] for lat, lon in b]))
    
    return l1, l2

def hausdorff_distance(a, b):
    return float(shapely.hausdorff_distance(*to_shapely(a, b)))

def frechet_distance(a, b):
    return float(shapely.frechet_distance(*to_shapely(a, b)))

def read_file(file_path):
    with open(file_path) as f:
        return json.load(f)

def populate_linestring(n: int) -> shapely.LineString:
    arr = []

    for _ in range(n):
        arr.append([random.uniform(-99.0, -99.5), random.uniform(19.3, 19.5)])

    return shapely.LineString(arr)

def populate_trajectory(n: int) -> list[tuple[float, float]]:
    return [
        (random.uniform(19.0, 19.5), random.uniform(-99.0, -99.5))
        for _ in range(n)
    ]

def plot_timecomplexity_shapely_vs_stmeasures(
        shapelyfn,
        stmeasuresfn,
        maxsize: int,
        *args
    ):
    params = [
        (shapelyfn, populate_linestring, "Shapely"),
        (stmeasuresfn, populate_trajectory, "stmeasures")
    ]

    _, axs = plt.subplots(1, 2, figsize=(20, 10))

    for ax, (fn, populatefn, plottitle) in zip(axs, params):
        times = []
        for i in range(2, maxsize):
            t1 = populatefn(i)
            t2 = populatefn(i)

            start = timeit.default_timer()
            if plottitle == "stmeasures":
                fn(t1, t2, *args)
            else:
                fn(t1, t2)
            end = timeit.default_timer() - start

            times.append(end)

        ax.plot(times)
        ax.set_title(plottitle)
        ax.set_xlabel("Tamaño de datos de entrada")
        ax.set_ylabel("Tiempo de ejecución")

    plt.tight_layout()
    plt.show()

def get_only_trajectories(geojson, n):
    i = 0
    dataset = []
    len_geojson = len(geojson)
    
    while len(dataset) < n:
        if i >= len_geojson or n >= len_geojson:
            raise ValueError("Number of trajectories greater than dataset length")
        
        if len(geojson[i]) > 1:
            dataset.append(geojson[i])
        
        i += 1

    return dataset

def compute_distance_matrix(trajectories, distance_function, *args):
    """
    Computes a pairwise distance matrix for a list of trajectories.

    :param trajectories: List of trajectories, where each trajectory is a list of (x, y) coordinates.
    :param distance_function: The distance function to use (e.g., hausdorff, dtw).
    :return: A 2D numpy array representing the distance matrix.
    """
    n = len(trajectories)
    distance_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            distance = distance_function(trajectories[i], trajectories[j], *args)
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance  # Symmetric matrix

    return distance_matrix

def plot_clusters(trajectories, labels, plottitle="Trajectory Clustering"):
    unique_labels = set(labels)
    colors = plt.cm.tab10(np.linspace(0, 1, len(unique_labels)))

    for trajectory, label in zip(trajectories, labels):
        color = colors[label] if label >= 0 else "k"  # Black for noise
        x, y = zip(*trajectory)
        plt.plot(x, y, color=color)

    plt.title(plottitle)
    plt.show()

def euclidean_distance1(a, b):
    return stmeasures.euclidean_distance(*convert_to_same_size(a, b))

def euclidean_distance2(a, b):
    return shapely.distance(*to_shapely(a, b))

def hausdorff_distance(a, b):
    return shapely.hausdorff_distance(*to_shapely(a, b))

def frechet_distance(a, b):
    return shapely.frechet_distance(*to_shapely(a, b))
