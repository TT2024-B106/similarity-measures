import math

def distance(p: list[float], q: list[float]) -> float:
    """
    Calculate euclidean distance of two vectors of whatever size.

    A zero-padding will take effect if one of the vectors is of different
    size.

    :param p: First float vector.
    :param q: Second float vector.
    :return: The result of the euclidean distance calculation.
    """
    # If diff is 0 the vectors are equal
    # If diff is +, q is greater and we have to add 0s to p
    # If diff is -, p is greater and we have to add 0s to q
    len_p = len(p)
    len_q = len(q)
    len_diff = len_q - len_p

    # Zero-padding
    i = 0
    while i != len_diff:
        if len_diff > 0:
            p.append(0)
            i += 1
        else:
            q.append(0)
            i -= 1

    # Euclidean distance calculation
    final_len = len_p if len_p > len_q else len_q
    sum_of_squares = 0.0
    for i in range(final_len):
        diff = p[i] - q[i]
        sum_of_squares += diff * diff
    
    return math.sqrt(sum_of_squares)
