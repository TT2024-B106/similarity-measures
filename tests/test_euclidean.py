import sys
import cppyy

cppyy.include('src/euclidean.h')
cppyy.load_library('build/libeuclidean.so')
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

if __name__ == '__main__':
    # Different length
    # Distance of:
    # t1 = [(t1x_1, t1y_1)]
    # t2 = [(t2x_1, t2y_1), [(t2x_2), (t2y_2)]
    print(distance([1,2], [3,4,3,6]))

    # Same length
    print(distance([1,2], [3,4]))

    sys.exit(0)
