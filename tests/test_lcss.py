import cppyy

# Añadir la carpeta build al PATH
cppyy.load_library('../build/liblcss.so')

# Incluir los encabezados necesarios
cppyy.include('../src/Headers/LCSS.h')
cppyy.include('../src/Headers/Coordinates.h')
cppyy.include('../src/Headers/Algoritmos.h')

# Acceder a los espacios de nombres globales de C++
lib = cppyy.gbl
Lcss = lib.LCSS
CoordinateSequence = lib.CoordinateSequence
Coordinate = lib.Point

# Crear las secuencias de coordenadas
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

# Crear una instancia de Hausdorff
lcss = Lcss()

# Ejecutar el algoritmo Hausdorff
result = lcss.Execute(sequence1, sequence2)
print("Lcss distance:", result)