def square(x: int | float) -> int | float:
    """
    A function that squares a number.

    Args:
        x (int | float): A number to be squared

    Returns:
        int | float: The squared number
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    A function that raises a number to the power of itself.

    Args:
        x (int | float): A number to be raised to the power of itself

    Returns:
        int | float: The number raised to the power of itself
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    A function that takes a number and a function and returns a function that
    takes no arguments and returns the result of the original function called
    with the original number.

    Args:
        x (int | float): A number
        function: A function that takes a number and returns a number

    Returns:
        object: A function that takes no arguments and returns a number
    """
    count = 0
    result = function(x)

    def inner() -> float:
        """
        A function that takes no arguments and returns the result of the
        original function called with the original number.

        Returns:
            float: The result of the original function called with the original
            number
        """
        nonlocal count, result
        if count:
            result = function(result)
        count += 1
        print(f'Result: {result}, Times called: {count}')
        return result

    return inner


if __name__ == '__main__':
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
