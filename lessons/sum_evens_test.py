"""Testing my summation function."""

from sum_evens import sum_evens_in_list
def test_empty_sum() -> None:
    """sum_evens in list of empty list should be zero."""
    assert sum_evens_in_list([]) == 0

def test_list_length_1():
    """Testing on a list with one element."""
    test_list: list[int] = [2]
    assert sum_evens_in_list(test_list) == 2

def test_list_positives():
    """Testing sum on a list of positive integers."""
    test_list: list[int] = [1,2,3,4]
    assert sum_evens_in_list(test_list) == 6

def test_list_negs_pos():
    """Testing sum of negative and positives."""
    test_list: list[int] = [1,-2,3,4]
    assert sum_evens_in_list(test_list) == 2

# def test_name() -> None:
#   assert <boolean command>

#use case: testing properties for how we expect our program to be used
#edge case: testing instances outside "typical" usage