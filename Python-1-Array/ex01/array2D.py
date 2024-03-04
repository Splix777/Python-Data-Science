# array2D.py

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes in a list and two indices and returns a slice of the list

    Args:
    family: list of strings
    start: integer
    end: integer

    Returns:
    list of strings

    Example:
    family = ['John', 'Paul', 'George', 'Ringo']
    start = 1
    end = 3
    print(slice_me(family, start, end))

    Output:
    ['Paul', 'George']
    """
    try:
        print(f'My shape is : {np.array(family).shape}')
        print(f'My new shape is : {np.array(family[start:end]).shape}')
        return family[start:end]
    except ValueError as e:
        print(f'Error: {e}')
        return []
