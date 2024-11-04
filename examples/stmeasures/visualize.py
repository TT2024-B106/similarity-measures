import geojsonio
import json

def swap_coordinates(coords):
    return [[lon, lat] for lat, lon in coords]

def trajectory(trajectory):
    geojson = {
        "type": "LineString",
        "coordinates": trajectory['coordinates']
    }
    geojsonio.display(json.dumps(geojson))

def visualize_trajectory_by_index(geojson_obj, index):
    if 0 <= index < len(geojson_obj.trajectories):
        trajectory(geojson_obj.trajectories[index])
    else:
        print(f"Invalid index: {index}. Please choose an index between 0 and {len(geojson_obj.trajectories) - 1}.")

def trajectories(geojson_obj):
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for trajectory in geojson_obj.trajectories:
        geojson['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": trajectory['coordinates']
            },
            "properties": {
                "id": trajectory['id'],
                "timestamp": trajectory['timestamp']
            }
        })
    geojsonio.display(json.dumps(geojson))
