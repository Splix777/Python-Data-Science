# filterstring.py

import sys


def main():
    '''
    - Words are separated from each other by space characters.
    - Strings do not contain any special characters.
      (Punctuation or invisible)
    - The program must contain at least one list comprehension
      expression and one lambda.
    - If the number of argument is different from 2, or if the type
      of any argument is wrong, the program prints an AssertionError.
    '''
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    s = sys.argv[1]
    n = int(sys.argv[2])
    # print(list(filter(lambda x: len(x) >= n, s.split())))
    print([word for word in s.split() if (lambda x: len(x) >= n)(word)])


if __name__ == "__main__":
    main()
