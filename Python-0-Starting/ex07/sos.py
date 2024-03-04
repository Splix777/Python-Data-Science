# sos.py

import sys


def create_morse_code_dict() -> dict[str, str]:
    """
    Creates a dictionary of alphanumeric keys and
    their corresponding morse code translation as a value.
    """
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


def text_to_morse(input_string: str) -> str | None:
    """
    Takes in a input string and prints out its corresponding
    morse code.

    If there are non-alphanumeric values in the string it
    returns an AssertionError.
    """
    morse_code_dict = create_morse_code_dict()

    if not all(
        char.isalnum() or char.isspace() for char in input_string
    ):
        raise AssertionError

    morse = " ".join(
            morse_code_dict[char.upper()] if char.upper() in morse_code_dict else char
            for char in input_string
        )
    print(morse)
    return morse


if __name__ == "__main__":
    try:
        string = "".join(sys.argv[1:]) if len(sys.argv) > 1 else "help me@"
        text_to_morse(string)
    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
