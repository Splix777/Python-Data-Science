# building.py

import sys
import string

def count_characters(text):
    char_count = len(text)
    
    upper_count = sum(bool(char.isupper()) for char in text)
    lower_count = sum(bool(char.islower()) for char in text)
    punct_count = sum(char in string.punctuation for char in text)
    space_count = sum(bool(char.isspace()) for char in text)
    digit_count = sum(bool(char.isdigit()) for char in text)

    print(f"The text contains {char_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

if __name__ == "__main__":
    try:
        text = sys.argv[1]
    except IndexError:
        try:
            print("What is the text to count?")
            text = sys.stdin.readline()
            if not text:
                sys.exit(0)
            count_characters(text)
        except KeyboardInterrupt as e:
            print(f'KeyboardInterrupt: {e}')
            sys.exit(1)
    else:
        count_characters(text)
        sys.exit(0)
    
    