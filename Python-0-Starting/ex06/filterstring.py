# filterstring.py

import sys


def ft_filterstring(string: str = "", n: int = 0) -> list[str]:
    """
    - Words are separated from each other by space characters.
    - Strings do not contain any special characters.
      (Punctuation or invisible)
    - The program must contain at least one list comprehension
      expression and one lambda.
    - If the number of argument is different from 2, or if the type
      of any argument is wrong, the program prints an AssertionError.
    """
    if not isinstance(string, str) or not isinstance(n, int):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    s = string
    n = n
    return [word for word in s.split() if (lambda x: len(x) >= n)(word)]


def main():
    try:
        string = sys.argv[1] if len(sys.argv) > 1 else "Hello World! 123"
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        print(ft_filterstring(string, n))
    except (ValueError, AssertionError):
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
