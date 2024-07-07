# import math

def print_evens(values):
    """To print number of even values"""
    for val in values:
        is_even = ((val % 2) == 0)
        if is_even:
            print('Found even value %s' % val)
