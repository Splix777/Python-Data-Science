# ft_filter.py

def ft_filter(function, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
    return the items that are true.
    """
    if function is None:
        function = bool
    for item in iterable:
        if function(item):
            yield item


def main():
    print('ft_filter.py')
    print(ft_filter.__doc__)
    print('filter.py')
    print(filter.__doc__)

    example_string = "Hello, World! 123"

    print("\nTesting ft_filter function:")
    print(f"Original string: {example_string}")
    print(
        f"Filtered string using ft_filter: "
        f"{''.join(ft_filter(str.isalpha, example_string))}")
    print(
        f"Filtered string using ft_filter:"
        f"{''.join(ft_filter(None, example_string))}")

    print("\nTesting filter function:")
    print(f"Original string: {example_string}")
    print(
        f"Filtered string using filter:"
        f"{''.join(filter(str.isalpha, example_string))}")
    print(
        f"Filtered string using filter:"
        f"{''.join(filter(None, example_string))}")


if __name__ == '__main__':
    main()
