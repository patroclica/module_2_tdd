# tests/tests_add.py
import pytest # import pytest

import calculator # import calculator

def test_two_plus_two():
    """
    Asserts that given the parameters 2 and 2, the add
    function should return 4.
    """
    assert calculator.add(2, 2) == 4

def test_five_plus_seven():
    """
    test 5 + 7
    """
    assert calculator.add(5, 7) == 12

def test_no_parameters():
    """
    Asserts that when no parameters are provided,
    0 should be returned.
    """
    assert calculator.add() == 0

def test_with_three_arguments():
    """
    test with three
    """
    assert calculator.add(1, 2, 3) == 6

def test_with_5_arguments():
    """
    test with 5
    """
    assert calculator.add(1, 2, 3, 4, 5) == 15

def test_zero_division():
    """
    test zero division
    """
    with pytest.raises(ZeroDivisionError):
        1/0
def test_negative_values():
    """ Assert that negative values work. """
    assert calculator.add(-1, -1, -1, -1, -1) == -5

def test_floating_point_precision():
    """Assert floating point precision. """
    assert calculator.add(0.1, 0.2, 0.3) == pytest.approx(0.6)

def test_subtract_two_arguments():
    """ Assert for subtract two arguments """
    assert calculator.subtract(9, 1) == 8

def test_multiply_values():
    """
    test multiply
    """
    assert calculator.multiply (3, 12) == 36

# for testing divide there is another test_divide.py
def test_divide_arguments():
    """
    test divide
    """
    assert calculator.divide(1, 1) == 1
