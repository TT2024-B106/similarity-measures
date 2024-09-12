# dtw_module.pyx

from libcpp.vector cimport vector
from cython.operator cimport dereference
cimport dtw


cdef extern from "coordinates.h":
    cdef struct Point:
        double latitude
        double longitude

    cdef struct CoordinateSequence:
        vector[Point] points


cdef extern from "dtw.h":
    double ExecuteDTW(const CoordinateSequence& seq1, const CoordinateSequence& seq2)


def calculate_dtw(list seq1, list seq2):
    cdef vector[Point] vec_seq1
    cdef vector[Point] vec_seq2
    cdef Point pt
    cdef CoordinateSequence cseq1, cseq2


    for s1 in seq1:
        pt.latitude = s1[0]
        pt.longitude = s1[1]
        vec_seq1.push_back(pt)

    for s2 in seq2:
        pt.latitude = s2[0]
        pt.longitude = s2[1]
        vec_seq2.push_back(pt)


    cseq1.points = vec_seq1
    cseq2.points = vec_seq2


    return ExecuteDTW(cseq1, cseq2)

