# building.py

import sys
from breakdown import StringBreakdown


def main():
    """
    Main function to run the script.

    If a command-line argument is provided, it is used
    as the input string to be analyzed. If no command-line
    argument is provided, the user is prompted to enter
    an input string.

    The input string is then analyzed and the results
    are printed to the console.

    Returns:
    None
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    if len(sys.argv) == 2:
        breakdown = StringBreakdown(sys.argv[1])
    else:
        breakdown = StringBreakdown()
    print(breakdown)


if __name__ == '__main__':
    main()
