import stmeasures
import geojsonio

def see_each_trajectory(geojson, start, end):
    for i in range(start, end):
        _ = geojsonio.display(stmeasures.get_geojsonio_contents(trajectory=geojson[i]))
