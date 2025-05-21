import pytest


def add_two_numbers(a, b):
    return a + b

@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(7, 5) == 12, "The sum of 7 and 5 should be 3"


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(333,777) == 1110, "The sum of 333 and 777 should be 1110"