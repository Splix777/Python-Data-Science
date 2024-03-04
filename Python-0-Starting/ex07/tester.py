# tester.py

import pytest

from sos import text_to_morse


def test_text_to_morse():
    assert text_to_morse("SOS") == "... --- ..."
    assert text_to_morse("SOS1") == "... --- ... .----"
    assert text_to_morse("SOS 1") == "... --- ... / .----"


def test_text_to_morse_non_alphanumeric():
    with pytest.raises(AssertionError):
        text_to_morse("SOS!")
        text_to_morse("SOS@")
        text_to_morse("SOS#")
        text_to_morse("SOS$")


def test_text_to_morse_empty_string():
    assert text_to_morse("") == ""
    assert text_to_morse(" ") == "/"
    assert text_to_morse("  ") == "/ /"
