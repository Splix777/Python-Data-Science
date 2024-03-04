# whatis.py

import sys


def valid_integer(func):
    def wrapper(arg):
        if isinstance(arg, str):
            try:
                arg = int(arg)
            except ValueError:
                raise ValueError("AssertionError: argument is not an integer")
        if not isinstance(arg, int) or isinstance(arg, bool):
            raise ValueError("AssertionError: argument is not an integer")
        return func(arg)

    return wrapper


@valid_integer
def odd_or_even(number: int) -> str:
    try:
        print("I'm Even." if number % 2 == 0 else "I'm Odd.")
        return "I'm Even." if number % 2 == 0 else "I'm Odd."
    except ValueError as e:
        raise ValueError(e) from e


def main(number: any) -> None:
    odd_or_even(number)


# if __name__ == '__main__':
#     if len(sys.argv) != 2:
#         print('AssertionError: invalid number of arguments')
#         sys.exit(1)
#
#     try:
#         main(sys.argv[1])
#     except ValueError as e:
#         print(e)
#         sys.exit(1)

if __name__ == '__main__':
    try:
        main(5)
    except ValueError as e:
        print(e)
        sys.exit(1)