# breakdown.py

import sys


class StringBreakdown:
    def __init__(self, user_input=None) -> None:
        """
        Initializes a StringBreakdown object with optional
        user-provided input.

        Parameters:
        - user_input (str, optional): The input string to be analyzed.

        Attributes:
        - user_input (str): The input string to be analyzed.
        - char_count (int): The total number of characters.
        - upper_count (int): The count of uppercase letters.
        - lower_count (int): The count of lowercase letters.
        - punctuation_count (int): The count of punctuation marks.
        - whitespace_count (int): The count of whitespace characters
          (space, newline, carriage return, form feed, vertical tab).
        - digits_count (int): The count of digits in the input string.
        """
        self.user_input = user_input
        self.char_count = len(user_input) if user_input else 0
        self.upper_count = 0
        self.lower_count = 0
        self.punctuation_count = 0
        self.whitespace_count = 0
        self.digits_count = 0

    def get_user_input(self) -> str:
        """
        Prompts the user to enter an input string until a "\n" is detected.
        When the user presses "Enter", the input string is returned with
        the trailing newline character included so we can count it as a
        space character. We also have to check for ctrl+D to exit the input.

        Returns:
        str: The input string entered by the user.
        """
        print("What is the text to count?")
        user_input = ""

        user_input += sys.stdin.read()
        return user_input

    def str_char_counter(self) -> None:
        """
        Analyzes the characters in the input string and counts the occurrences
        of different character types.

        The following character types are considered:
        - Uppercase letters
        - Lowercase letters
        - Punctuation marks
        - Whitespace characters
          (space, tab, newline, carriage return, form feed, vertical tab)
        - Digits

        The counts are stored in the corresponding attributes of the
        StringBreakdown object.
        """
        for char in self.user_input:
            if char.isupper():
                self.upper_count += 1
            elif char.islower():
                self.lower_count += 1
            elif char in {' ', '\t', '\n', '\r', '\f', '\v'}:
                self.whitespace_count += 1
            elif char.isdigit():
                self.digits_count += 1
            else:
                self.punctuation_count += 1

    def __str__(self) -> None:
        """
        Returns a string representation of the StringBreakdown object.

        If the user input is not provided, prompts the user to enter
        the input string.

        Returns:
        A string representing the character count of the input string.

        """
        if self.user_input is None:
            self.user_input = self.get_user_input()
            if self.user_input.endswith("\x04"):
                print("AssertionError: ctrl+D is pressed")
                sys.exit(1)
            self.char_count = len(self.user_input)
        self.str_char_counter()
        return f"The text contains {self.char_count} characters:\n" \
               f"{self.upper_count} upper letters\n" \
               f"{self.lower_count} lower letters\n" \
               f"{self.punctuation_count} punctuation marks\n" \
               f"{self.whitespace_count} spaces\n" \
               f"{self.digits_count} digits\n"
