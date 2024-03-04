# tester.py

import sys
import pytest

from whatis import odd_or_even


def test_odd_number():
    assert odd_or_even(5) == "I'm Odd."


def test_even_number():
    assert odd_or_even(8) == "I'm Even."


def test_string_input():
    with pytest.raises(ValueError, match="AssertionError: argument is not an integer"):
        odd_or_even("invalid")


def test_float_input():
    with pytest.raises(ValueError, match="AssertionError: argument is not an integer"):
        odd_or_even(3.14)


def test_empty_input():
    with pytest.raises(ValueError, match="AssertionError: argument is not an integer"):
        odd_or_even("")


def test_boolean_input():
    with pytest.raises(ValueError, match="AssertionError: argument is not an integer"):
        odd_or_even(True)


def test_list_input():
    with pytest.raises(ValueError, match="AssertionError: argument is not an integer"):
        odd_or_even([1, 2, 3])