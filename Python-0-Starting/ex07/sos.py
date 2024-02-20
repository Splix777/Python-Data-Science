# sos.py

import sys


def create_morse_code_dict() -> dict[str, str]:
    '''
    Creates a dictionary of alphanumeric keys and
    their corresponding morse code translation as a value.
    '''
    return {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }


def is_valid_input(char: str) -> bool:
    '''
    Takes a char and checks if the char in uppercase exists
    in the morse code dictionary or is a space.

    Returns a bool if the char is valid
    '''
    valid_characters = set(create_morse_code_dict().keys())
    return char.upper() in valid_characters or char.isspace()


def main(input_string: str) -> None:
    '''
    Takes in a input string and prints out its corresponding
    morse code.

    If there are non alphanumeric values in the string it
    returns an AssertionError.
    '''
    if not all(is_valid_input(char) for char in input_string):
        print("AssertionError: the input string is bad")
        sys.exit(1)

    morse_code_dict = create_morse_code_dict()

    morse_code_list = [
        morse_code_dict.get(letter.upper())
        for letter in input_string
        if letter.upper() in morse_code_dict.keys() or letter.isspace()
    ]

    result_string = ' '.join(morse_code_list)
    print(result_string)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    main(sys.argv[1])
