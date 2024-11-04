# test_visualization.ipynb
import stmeasures.read as read
import stmeasures.visualize as visualize

# Cargar el archivo GeoJSON
geojson_obj = read.file("assets/ECATEPEC.json")

# Mostrar el número total de trayectorias disponibles
print(f"Number of trajectories available: {len(geojson_obj.trajectories)}")

# Visualizar una trayectoria específica por índice
index_to_visualize = 100  # Cambia este número para visualizar una trayectoria específica
visualize.visualize_trajectory_by_index(geojson_obj, index_to_visualize)



# Visualizar todas las trayectorias
#visualize.trajectories(geojson_obj)
