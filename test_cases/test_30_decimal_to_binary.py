import pytest

from codes.decimal_to_binary_30 import decimal_to_binary


def test_decimal_10():
    assert decimal_to_binary(10) == "1010"


def test_decimal_5():
    assert decimal_to_binary(5) == "101"


def test_decimal_0():
    assert decimal_to_binary(0) == "0"


def test_decimal_1():
    assert decimal_to_binary(1) == "1"


def test_large_number():
    assert decimal_to_binary(255) == "11111111"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)