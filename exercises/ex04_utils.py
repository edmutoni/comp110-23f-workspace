"""Lists Utils Exercise"""

def all(int_list: list[int], num_input: int ) -> bool:
    """Returning T or F if all the ints in the list is the same as the int provided"""
    i: int = 0
    if len(int_list) == 0:
        return False
    while i < len(int_list):
        if int_list[i] == num_input:
            i = i + 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returning the maxmimum value given a list of integers"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    max_num: int = input[0]
    while i < len(input):
        if input[i] > max_num:
            max_num = input[i]
            i = i + 1
        else:
            i = i + 1
    return max_num


def is_equal(f_list: list[int], s_list: list[int]) -> bool:
    """Returning T or F if every element in both lists is the same at the same index"""
    i: int = 0
    if len(f_list) <= len(s_list):
        while i < len(f_list):
            if f_list[i] == s_list[i]:
                i = i + 1
            else:
                return False
    else:
        while i < len(s_list):
            if f_list[i] == s_list[i]:
                i = i + 1
            else:
                return False
    return True