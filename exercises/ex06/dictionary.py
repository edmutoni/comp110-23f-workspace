"""Dictionary functions."""
__author__ = "930690385"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key-value pairs of an input dictionary and returns a new dictionary of the new key-value pairs."""
    out_dict: dict[str, str] = {}
    for key in inp_dict:
        for item in out_dict:
            if inp_dict[key] == item:
                raise KeyError("A dictionary cannot have duplicate keys.")
        out_dict[inp_dict[key]] = key
    return out_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Finds the str color that is mentioned the most times in a dictionary and returns it."""
    color_dict: dict[str, int] = {}
    fav_color: str = ""
    max: int = 0
    for key in inp_dict:
        if inp_dict[key] in color_dict:
            color_dict[inp_dict[key]] += 1
        else:
            color_dict[inp_dict[key]] = 1
    for item in color_dict:
        if color_dict[item] > max:
            max = color_dict[item]
            fav_color = item
    return fav_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Produces a dict that has unique values per each key."""
    out_dict: dict[str, int] = {}
    i: int = 0
    while i < len(inp_list):
        if inp_list[i] in out_dict:
            out_dict[inp_list[i]] = out_dict[inp_list[i]] + 1
        else:
            out_dict[inp_list[i]] = 1
        i = i + 1
    return out_dict


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Takes in a given lists of words and returns a dictionary where the key is a letter and the values are the words in the list that start with that letter."""
    out_dict: dict[str, list[str]] = {}
    for word in inp_list:
        start_chr = word[0].lower()
        if start_chr not in out_dict:
            out_dict[start_chr] = [word] 
        else:
            out_dict[start_chr].append(word)
    return out_dict  


def update_attendance(inp_dict: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Given the day and name of a student, update the attendance log of the existing dictionary."""
    if day not in inp_dict:
        inp_dict[day] = [name]
    else:
        if name not in inp_dict[day]:
            inp_dict[day].append(name)
    return inp_dict