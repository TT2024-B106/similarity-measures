import cppyy

cppyy.load_library('../build/libdtw.so')

cppyy.include('../src/Headers/DTW.h')
cppyy.include('../src/Headers/Algoritmos.h')
cppyy.include('../src/Headers/Coordinates.h')

lib = cppyy.gbl
DTW = lib.DTW
CoordinateSequence = lib.CoordinateSequence
Coordinate = lib.Point  

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

strategy = DTW()

subsequenceIndices = lib.std.vector('int')()

result = strategy.Execute(sequence1, sequence2)
print(result)
