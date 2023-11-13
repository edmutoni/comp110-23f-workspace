"""Testing my zip function."""
__author__ = "930690385"

from zip import zip


def test_dict() -> None:
    """Testing if the code returns a proper dict of strings as keys and ints as values."""
    test_int: list[int] = [1, 2, 3]
    test_str: list[str] = ["january", "february", "march"]
    assert zip(test_str, test_int) == {"january": 1, "february": 2, "march": 3}


def test_dict_1() -> None:
    """Testing if the code returns a proper dict with a len of strings and ints of 1."""
    test_int: list[int] = [1]
    test_str: list[str] = ["happy"]
    assert zip(test_str, test_int) == {"happy": 1}


def test_diff_len() -> None:
    """Testing if the code returns an empty dict when the lists are two different lengths."""
    test_int: list[int] = [1, 2, 3]
    test_str: list[str] = ["monday", "tuesday"]
    assert zip(test_str, test_int) == {}