import cppyy

cppyy.include('src/manhattan.h')
cppyy.load_library('libmanhattan.so')
lib = cppyy.gbl

def test_integers():
    assert lib.distance([1,2], [3,4]) == 4

def test_floats():
    assert lib.distance([1.4231, 2.123], [10.213, 11.123]) == 17.7899
