# dtw.pyx

from libcpp.vector cimport vector
from cython.operator cimport dereference
cimport dtw

# Estructuras de datos importadas de C++
cdef extern from "Coordinates.h":
    cdef struct Point:
        double latitude
        double longitude

    cdef struct CoordinateSequence:
        vector[Point] points

# Prototipos de funciones importadas de C++
cdef extern from "dtw.h":
    double ExecuteDTW(const CoordinateSequence& seq1, const CoordinateSequence& seq2)

# Función para calcular DTW en Python
def calculate_dtw(list seq1, list seq2):
    cdef vector[Point] vec_seq1
    cdef vector[Point] vec_seq2
    cdef Point pt
    cdef CoordinateSequence cseq1, cseq2

    # Convertir listas de Python a vector[Point]
    for s1 in seq1:
        pt.latitude = s1[0]
        pt.longitude = s1[1]
        vec_seq1.push_back(pt)

    for s2 in seq2:
        pt.latitude = s2[0]
        pt.longitude = s2[1]
        vec_seq2.push_back(pt)

    # Asignar puntos al CoordinateSequence
    cseq1.points = vec_seq1
    cseq2.points = vec_seq2

    # Llamada a la función ExecuteDTW de C++
    return ExecuteDTW(cseq1, cseq2)

