# stmeasures/read.py
import json
from stmeasures.abstractions.geojson import GeoJSON

def file(filepath: str) -> GeoJSON:
    with open(filepath, 'r') as f:
        data = json.load(f)
    return GeoJSON(data)
