# stmeasures/abstractions/geojson.py
class GeoJSON:
    def __init__(self, data):
        self.data = data
        self.trajectories = self._extract_trajectories()

    def _extract_trajectories(self):
        def swap_coordinates(coords):
            return [[lon, lat] for lat, lon in coords]

        trajectories = []
        for item in self.data:
            features = item.get('features', [])
            for feature in features:
                if feature['geometry']['type'] == 'LineString':
                    coordinates = swap_coordinates(feature['geometry']['coordinates'])
                    trajectories.append({
                        'id': feature['properties'].get('name'),
                        'timestamp': feature['properties'].get('tiempo'),
                        'coordinates': coordinates
                    })
        return trajectories

    def find_similar(self, trajectory):
        similar_trajectories = []
        # Lógica para encontrar trayectorias similares (placeholder)
        return similar_trajectories
