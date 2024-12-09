import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(3, 2) == 6

def test_divide():
    assert divide(6, 2) == 3
    with pytest.raises(ValueError):
        divide(6, 0)