import json
import stmeasures
import geojsonio
import shapely

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

    try: hausdorff_distance
    except NameError: _
    else: hausdorff = hausdorff_distance(t1, t2)

    try: frechet_distance
    except NameError: _
    else: frechet = frechet_distance(t1, t2)

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
