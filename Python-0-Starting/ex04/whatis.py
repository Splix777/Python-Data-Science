# whatis.py

import sys


def valid_integer(func):
    def wrapper(*args, **kwargs):
        try:
            int(args[0])
        except ValueError:
            print('AssertionError: argument is not an integer')
            sys.exit(1)
        return func(*args, **kwargs)
    return wrapper


def odd_or_even(object: int) -> None:
    if object % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


@valid_integer
def main(object: any) -> None:
    odd_or_even(int(object))


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('AssertionError: more than one argument is provided')
        sys.exit(1)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        sys.exit(0)
