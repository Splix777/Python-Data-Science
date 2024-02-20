# test_count_characters.py

import pytest
from building import count_characters

# Parametrized test for happy path scenarios
@pytest.mark.parametrize("test_input,expected_output", [
    ("", {"upper letters": 0, "lower letters": 0, "punctuation marks": 0, "spaces": 0, "digits": 0}),
    ("hello", {"upper letters": 0, "lower letters": 5, "punctuation marks": 0, "spaces": 0, "digits": 0}),
    ("HELLO", {"upper letters": 5, "lower letters": 0, "punctuation marks": 0, "spaces": 0, "digits": 0}),
    ("12345", {"upper letters": 0, "lower letters": 0, "punctuation marks": 0, "spaces": 0, "digits": 5}),
    ("!@#$%", {"upper letters": 0, "lower letters": 0, "punctuation marks": 5, "spaces": 0, "digits": 0}),
    ("     ", {"upper letters": 0, "lower letters": 0, "punctuation marks": 0, "spaces": 5, "digits": 0}),
    ("Hello, World! 123", {"upper letters": 2, "lower letters": 8, "punctuation marks": 2, "spaces": 2, "digits": 3}),
])
def test_count_characters_happy_path(capsys, test_input, expected_output):
    '''
    Test count_characters function with happy path scenarios
    '''
    # Act
    count_characters(test_input)
    captured = capsys.readouterr()
    output = captured.out

    # Print captured output and expected output
    print("Captured Output:")
    print(output)
    print("Expected Output:")
    print(expected_output)

    # Assert
    # sourcery skip: no-loop-in-tests
    for char_type, count in expected_output.items():
        assert f"{count} {char_type}" in output

    assert f"The text contains {len(test_input)} characters:" in output
