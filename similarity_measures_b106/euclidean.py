"""
The implementation of the euclidean algorithm.

Currently it is just a placeholder, it does not actually calculate.
"""

def distance(p: list[float], q: list[float]) -> float:
    """Calculate euclidean distance.

    Test and example for handling euclidean distance of 2 trajectories for
    whatever length provided. If the lengths are different a zero-padding is
    done.

    :param p: Vector that contains the elements of the first trajectory.
    :param q: Vector that contains the elements of the second trajectory.
    :return: The euclidean distance of the 2 trajectories.
    """
    len_p, len_q = len(p), len(q)

    if len_p == len_q:
        return max(p)

    # Padding with zeros
    while len_p != len_q:
        p.append(0) if len_p < len_q else q.append(0)
        len_p, len_q = len(p), len(q)

    return max(p)
