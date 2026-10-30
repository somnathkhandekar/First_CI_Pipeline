from codes.rotate_list_27 import rotate_list


def test_rotate_by_two():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_by_one():
    assert rotate_list([1, 2, 3], 1) == [3, 1, 2]


def test_rotate_by_list_length():
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]


def test_rotate_by_more_than_list_length():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]


def test_empty_list():
    assert rotate_list([], 2) == []


def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]