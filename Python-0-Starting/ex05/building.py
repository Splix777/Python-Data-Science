# building.py

import sys
import string
from collections import Counter


def count_characters(text: str) -> None:
    '''
    This function counts the number of characters in a text.
    It also counts the number of upper and lower letters,
    punctuation marks, spaces and digits.
    '''
    char_types = {
        'upper letters': lambda c: c.isupper(),
        'lower letters': lambda c: c.islower(),
        'punctuation marks': lambda c: c in string.punctuation,
        'spaces': lambda c: c.isspace(),
        'digits': lambda c: c.isdigit(),
    }

    counts = Counter({char_type: sum(map(checker, text))
                      for char_type, checker in char_types.items()})
    char_count = len(text)

    print(f"The text contains {char_count} characters:")
    for char_type, count in counts.items():
        print(f"{count} {char_type}")


if __name__ == "__main__":
    try:
        text = sys.argv[1]
    except IndexError:
        try:
            print("What is the text to count?")
            text = sys.stdin.readline()
            if not text:
                print("No text to count. Exiting.")
                sys.exit(0)
            count_characters(text)
        except KeyboardInterrupt as e:
            print(f'KeyboardInterrupt: {e}')
            sys.exit(1)
    else:
        count_characters(text)
        sys.exit(0)
