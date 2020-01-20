import maxima


def test_left_boundary():
    inp = [1, 0]
    assert maxima.find_maxima(inp) == [0]


def test_right_boundary():
    inp = [0, 1]
    assert maxima.find_maxima(inp) == [1]


def test_both_boundaries():
    inp = [2, 0, 1]
    assert maxima.find_maxima(inp) == [0, 2]


def test_both_boundaries_oob():
    inp = [1, 0, 2]
    assert maxima.find_maxima(inp) == [0, 2]


def test_non_numeric():
    inp = "bca"
    assert maxima.find_maxima(inp) == []
