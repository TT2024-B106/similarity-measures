import cppyy

cppyy.include('src/euclidean.h')
cppyy.load_library('libeuclidean.so')
lib = cppyy.gbl

def distance(p: list[float], q: list[float]) -> float:
    """Calculate euclidean distance.

    Test and example for handling euclidean distance of 2 trajectories for
    whatever length provided. If the lengths are different a zero-padding is
    done.

    Args:
        - p: Vector that contains the elements of the first trajectory.
        - q: Vector that contains the elements of the second trajectory.

    Returns:
        The euclidean distance of the 2 trajectories.
    """
    len_p, len_q = len(p), len(q)

    if len_p == len_q:
        return lib.distance(p, q)

    # Padding with zeros
    while len_p != len_q:
        p.append(0) if len_p < len_q else q.append(0)
        len_p, len_q = len(p), len(q)

    return lib.distance(p, q)

def test_vectors_different_length():
    assert distance([1,2], [3,4,3,6]) == 7.280109889280518

def test_vectors_same_length():
    assert distance([1,2], [3,4]) == 2.8284271247461903
