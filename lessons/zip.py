"""Combining two lists into a dictionary."""
__author__ = "930690385"


def zip(string_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Takes in a list of strings as keys and a list of ints as values, creates a dictionary with the two lists."""
    i: int = 0
    zip_dict: dict[str, int] = dict()
    if len(string_list) != len(int_list):
        return zip_dict
    else:
        if len(string_list) > 0 and len(int_list) > 0:
            while i < len(string_list):
                zip_dict[string_list[i]] = int_list[i] 
                i = i + 1
            return zip_dict
        return zip_dict