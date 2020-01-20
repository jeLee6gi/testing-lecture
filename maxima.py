from typing import Sequence


def find_maxima(x: Sequence[float]):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    for i in range(len(x)):
        # `i` is a local maximum if the signal decreases before and after it
        if (
            (i == 0 and x[i + 1] < x[i])
            or (i == len(x)-1 and x[i - 1] < x[i])
            or (0 < i < len(x)-1 and x[i - 1] < x[i] and x[i + 1] < x[i])
        ):
            idx.append(i)

    return idx
