# ft_filter.py

import sys


def ft_filter(function, iterable):
    """
    This function is a copy of the built-in filter function.
    It returns an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))

def main():
    print(ft_filter.__doc__)
    print(filter.__doc__)


if __name__ == '__main__':
    main()