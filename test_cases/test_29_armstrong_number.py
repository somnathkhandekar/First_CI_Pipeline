from codes.armstrong_number_29 import is_armstrong


def test_armstrong_153():
    assert is_armstrong(153) is True


def test_armstrong_370():
    assert is_armstrong(370) is True


def test_armstrong_9474():
    assert is_armstrong(9474) is True


def test_non_armstrong_number():
    assert is_armstrong(123) is False


def test_single_digit():
    assert is_armstrong(7) is True


def test_zero():
    assert is_armstrong(0) is True


def test_negative_number():
    assert is_armstrong(-153) is False