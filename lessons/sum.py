"""Summing the elements of a list using different loops."""
__author__ = "930690385"


def w_sum(sum_list: list[float]) -> float:
    """Takes in the floats in the list and sums them togehter using a while loop."""
    sum: float = 0.0
    i: int = 0
    while i < len(sum_list):
        sum += sum_list[i]
        i += 1
    return sum
    

def f_sum(sum_list: list[float]) -> float:
    """Takes in the floats in the list and sums them together using a for loop."""
    sum: float = 0.0
    for flt in sum_list:
        sum += flt
    return sum


def f_range_sum(sum_list: list[float]) -> float:
    """Takes in the floats in the list and sums them together using through indexing using range."""
    sum: float = 0.0
    for i in range(0, len(sum_list)):
        sum += sum_list[i]
    return sum