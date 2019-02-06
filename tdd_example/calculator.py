# calculator.py
"""
def add(first_number=0, second_number=0):
    return first_number + second_number
    """
import math

def add(*numbers):
    total = 0 # initialize a total of 0
    for number in numbers: # Iterate over each param value
        total += number # Add to the total
    #return first_number + second_number

    """
    def add(*args):
    # add() returns the sum of n-parameters
    #import pdb; pdb.set_trace()
    return sum(args)
    """
    return total

def subtract(first_number, second_number):
        return first_number - second_number

def multiply(first_number, second_number):
        return first_number * second_number

def divide(*args):
    """
    Returns the result of the division of n-parameters.
    """
    if not args:
        return math.nan
    if len(args) == 1:
        return 1
    args = list(args)
    answer = args.pop(0)
    for value in args:
        try:
            answer /= value
        except ZeroDivisionError:
            return math.nan
    return answer
