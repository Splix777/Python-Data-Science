# tester.py

import pytest

from ft_filter import ft_filter
from filterstring import ft_filterstring


def test_ft_filterstring():
    for i in range(10):
        assert ft_filterstring("Hello World! 123", i) == list(
            filter(lambda x: len(x) >= i, "Hello World! 123".split())
        )


def test_ft_filter():
    assert list(ft_filter(str.isalpha, "Hello, World! 123")) == list(
        filter(str.isalpha, "Hello, World! 123")
    )
    assert list(ft_filter(None, "Hello, World! 123")) == list(
        filter(None, "Hello, World! 123")
    )