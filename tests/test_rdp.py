import cppyy

cppyy.load_library('../build/librdp.so')

cppyy.include('../src/Headers/RDP.h')
cppyy.include('../src/Headers/Coordinates.h')
cppyy.include('../src/Headers/Algoritmos.h')

lib = cppyy.gbl
Rdp = lib.RDP
CoordinateSequence = lib.CoordinateSequence
Coordinate = lib.Point

def print_coordinate_sequence(sequence):
    for point in sequence.points:
        print(f"({point.latitude}, {point.longitude})")

sequence1 = CoordinateSequence()
sequence1.points.push_back(Coordinate(1.0, 2.0))
sequence1.points.push_back(Coordinate(3.0, 2.5))
sequence1.points.push_back(Coordinate(5.0, 3.5))
sequence1.points.push_back(Coordinate(7.0, 6.0))
sequence1.points.push_back(Coordinate(9.0, 7.0))
sequence1.points.push_back(Coordinate(11.0, 8.0))
sequence1.points.push_back(Coordinate(13.0, 8.5))
sequence1.points.push_back(Coordinate(15.0, 9.0))
sequence1.points.push_back(Coordinate(17.0, 9.5))
sequence1.points.push_back(Coordinate(19.0, 9.5))

sequence2 = CoordinateSequence()
sequence2.points.push_back(Coordinate(1.0, 2.0))
sequence2.points.push_back(Coordinate(3.0, 2.5))
sequence2.points.push_back(Coordinate(5.0, 3.5))
sequence2.points.push_back(Coordinate(7.0, 6.0))
sequence2.points.push_back(Coordinate(9.0, 7.0))
sequence2.points.push_back(Coordinate(11.0, 8.0))
sequence2.points.push_back(Coordinate(13.0, 8.5))
sequence2.points.push_back(Coordinate(15.0, 9.0))
sequence2.points.push_back(Coordinate(17.0, 9.5))
sequence2.points.push_back(Coordinate(1500.0, 8.0))

rdp = Rdp()

result = rdp.Execute(sequence1, 1)

print("Resulting CoordinateSequence:")
print_coordinate_sequence(result)