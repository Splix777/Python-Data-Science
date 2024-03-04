import string
import sys


def count_characters(text: str) -> None:
    char_types = {
        'upper letters': sum(bool(char.isupper()) for char in text),
        'lower letters': sum(bool(char.islower()) for char in text),
        'punctuation marks': sum(char in string.punctuation for char in text),
        'spaces': sum(bool(char.isspace()) for char in text),
        'digits': sum(bool(char.isdigit()) for char in text),
    }

    char_count = len(text)

    print(f"The text contains {char_count} characters:")
    for char_type, count in char_types.items():
        print(f"{count} {char_type}")


def main():
    text = ""
    if len(sys.argv) == 2:
        text = sys.argv[1]
    elif len(sys.argv) == 1:
        try:
            print("What is the text to count?")
            text = sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit(1)
        except EOFError:
            text.strip()

    else:
        raise AssertionError("More than one argument is provided.")

    count_characters(text)


if __name__ == "__main__":
    main()
