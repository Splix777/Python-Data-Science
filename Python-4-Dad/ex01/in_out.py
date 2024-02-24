def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0
    result = function(x)

    def inner() -> float:
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
