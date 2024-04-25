import cppyy

cppyy.include('src/edit_distance.h')
cppyy.load_library('libeditdist.so')
cppyy.load_library('libmanhattan.so')
lib = cppyy.gbl

def test_simple():
    assert lib.edr_distance([1,2], [3,4]) == 1

def test_vectors_different_length():
    # Vectors in the form of V={vx_1, vy_1, vx_2, ... vx_n, vy_n}
    r = [2, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    s = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

    assert lib.edr_distance(r, s) == 1
