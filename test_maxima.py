import maxima

import pytest


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


def test_characters():
    inp = "bca"
    with pytest.raises(ValueError):
        maxima.find_maxima(inp)


def test_characters2():
    inp = ["b", "c", "a"]
    with pytest.raises(ValueError):
        maxima.find_maxima(inp)


def test_non_numeric():
    inp = [None, [], "a", 5]
    with pytest.raises(ValueError):
        maxima.find_maxima(inp)
