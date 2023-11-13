"""Test functions for dictionary.py."""
__author__ = "930690385"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
import pytest


# Testing invert.
def test_import() -> None:
    """Testing to see if codes properyly inverts the keys and values of an input dictionary."""
    test_dict: dict[str, str] = {"Monday": "1", "Tuesday": "2", "Wednesday": "3"}
    assert invert(test_dict) == {"1": "Monday", "2": "Tuesday", "3": "Wednesday"}


def test_dupes() -> None:
    """Testing to see if code raises the KeyError when an inverted dictionary will have duplicate keys."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {"Python": "Snake", "Cobra": "Snake"}
        invert(test_dict)


def test_short() -> None:
    """Testing to see if codes inverts given dictionary with only one key-value pair."""
    test_dict: dict[str, str] = {"Hello": "World"}
    assert invert(test_dict) == {"World": "Hello"}


# Testing favorite_color.
def test_favcolor() -> None:
    """Testing to see if code returns the most popular color when there is a max color."""
    test_dict: dict[str, str] = {"A": "Blue", "B": "Blue", "C": "Pink"}
    assert favorite_color(test_dict) == "Blue"


def test_one_favcolor() -> None:
    """Testing favcolor when there is only one key-value pair."""
    test_dict: dict[str, str] = {"A": "Blue"}
    assert favorite_color(test_dict) == "Blue"


def test_tie() -> None:
    """Testing to see if code returns that color that is written first in the dictionary when there is a tie for popular colors."""
    test_dict: dict[str, str] = {"A": "Blue", "B": "Blue", "C": "Pink", "D": "Pink"}
    assert favorite_color(test_dict) == "Blue"


# Testing count.
def test_unique_count() -> None:
    """Testing to see if the proper dictionary is returned when all items in the inp_list are unique values."""
    test_list: list[str] = ["Pepper", "Green Beans", "Tomatos", "Potatos"]
    assert count(test_list) == {"Pepper": 1, "Green Beans": 1, "Tomatos": 1, "Potatos": 1}


def test_multi_count() -> None:
    """Testing to see if the dict value updates the count when there's duplicate items in the list."""
    test_list: list[str] = ["Apple", "Banana", "Orange", "Apple"]
    assert count(test_list) == {"Apple": 2, "Banana": 1, "Orange": 1}


def test_all_same_count() -> None:
    """Testing to see if the dictionary returns only one key-value pair when the list only has a duplicate item."""
    test_list: list[str] = ["Apples", "Apples", "Apples", "Apples"]
    assert count(test_list) == {"Apples": 4}


# Testing alphabetize. 
def test_unique_alpha() -> None:
    """Testing if the function returns a proper dictionary when there are words that start with all different letters."""
    test_list: list[str] = ["Apple", "Banana", "Cherry", "Durian"]
    assert alphabetizer(test_list) == {"a": ['Apple'], "b": ['Banana'], "c": ['Cherry'], "d": ['Durian']}


def test_dupe_alpha() -> None:
    """Testing if the function returns the correct dictionary when there are multiple words that start with the same letter."""
    test_list: list[str] = ["Apple", "Ant", "Awesome", "Boo", "Bear", "Chocolate"]
    assert alphabetizer(test_list) == {"a": ['Apple', 'Ant', 'Awesome'], "b": ['Boo', 'Bear'], "c": ['Chocolate']}


def test_empty() -> None:
    """Testing if function returns empty dict when given an empty list."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


# Testing update_attendance
def test_new_day() -> None:
    """Testing if the dict creates a new key-value pair when there's a different day."""
    test_dict: dict[str, str] = {"Monday": ["Emilie"], "Tuesday": ["Angela"]}
    assert update_attendance(test_dict, "Wednesday", "Ifeoma") == {"Monday": ["Emilie"], "Tuesday": ["Angela"], "Wednesday": ["Ifeoma"]}


def test_dup_day() -> None:
    """Testing if a dict doesn't update when the same day and name is inputted."""
    test_dict: dict[str, str] = {"Monday": ["Emilie"], "Tuesday": ["Angela"]}
    assert update_attendance(test_dict, "Monday", "Emilie") == {"Monday": ["Emilie"], "Tuesday": ["Angela"]}


def test_new_name() -> None:
    """Testing if the dict adds a new name to an existing day."""
    test_dict: dict[str, str] = {"Monday": ["Emilie"], "Tuesday": ["Angela"]}
    assert update_attendance(test_dict, "Monday", "Ifeoma") == {"Monday": ["Emilie", "Ifeoma"], "Tuesday": ["Angela"]}