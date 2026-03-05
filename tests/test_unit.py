import pytest
from calculator.core import add, subtract, multiply, divide, clear

def test_addition():
    assert add(5, 3) == 8

def test_subtraction():
    assert subtract(10, 4) == 6

def test_multiplication():
    assert multiply(6, 7) == 42

def test_division():
    assert divide(8, 2) == 4

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_negative_numbers():
    assert add(-2, -3) == -5

def test_decimal_numbers():
    assert multiply(2.5, 2) == 5.0

def test_clear():
    assert clear() == 0