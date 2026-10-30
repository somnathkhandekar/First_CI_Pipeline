from codes.find_max_min_25 import find_max_min


def test_positive_numbers():
    assert find_max_min([3, 8, 1, 9, 4]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -9, -1]) == (-1, -9)


def test_single_element():
    assert find_max_min([7]) == (7, 7)


def test_duplicate_numbers():
    assert find_max_min([4, 2, 4, 2]) == (4, 2)


def test_empty_list():
    assert find_max_min([]) == (None, None)


def test_mixed_numbers():
    assert find_max_min([-10, 0, 15, 5]) == (15, -10)