# dtw.pxd
from libcpp.vector cimport vector

cdef extern from "dtw.h":
    double dtw(const vector[double]& s1, const vector[double]& s2)

