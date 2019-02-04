# tests/tests_add.py
import calculator

def test_two_plus_two():
    """
    Asserts that given the parameters 2 and 2, the add
    function should return 4.
    """
    assert calculator.add(2, 2) == 4

def test_five_plus_seven():
    assert calculator.add(5, 7) == 12

def test_no_parameters():
    """
    Asserts that when no parameters are provided,
    0 should be returned.
    """
    assert calculator.add() == 0

def test_with_three_arguments():
    assert calculator.add(1,2,3) == 6

def test_with_5_arguments():
    assert calculator.add(1,2,3,4,5) == 15

import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
def test_negative_values():
    """ Assert that negative values work. """
    assert calculator.add(-1,-1,-1,-1,-1) == -5

def test_floating_point_precision():
    """Assert floating point precision. """
    assert calculator.add(0.1, 0.2, 0.3) == pytest.approx(0.6)

def test_subtract_two_arguments():
    """ Assert for subtract two arguments """
    assert calculator.subtract(9,1) == 8

def test_multiply_values():
    assert calculator.multiply (3, 12) == 36

def test_divide_arguments():
    assert calculator.divide(1, 1) == 1
