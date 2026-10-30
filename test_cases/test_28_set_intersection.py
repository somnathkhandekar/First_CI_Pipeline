from codes.set_intersection_28 import set_intersection


def test_common_elements():
    assert set_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_no_common_elements():
    assert set_intersection([1, 2], [3, 4]) == []


def test_duplicate_elements():
    assert set_intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]


def test_empty_lists():
    assert set_intersection([], []) == []


def test_one_empty_list():
    assert set_intersection([1, 2, 3], []) == []


def test_negative_numbers():
    assert set_intersection([-3, -1, 0, 2], [-1, 0, 5]) == [-1, 0]