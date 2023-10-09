"""Lists Virtual Lesson"""
#a list is a data structure

grocery_list: list[str] = ["eggs", "milk", "bread"]
#<list name>: list[<item type>] = [<item1>, ...] 

#initialaing an emtpy list:
#<list name>: list[<item type>] = list()
#grocery_list: list[str] = list()

#adding an item to a list
grocery_list.append("bananas")

#indexing
grocery_list[0]

#modifying by index
grocery_list[1] = "eggs"

#length of a list
len(grocery_list)

#remove an item from a list
grocery_list.pop(2)

"""Randomly rolls dice and sums total"""
from random import randint
roll1: int = randint(1,6)
roll2: int = randint(1,6)
roll3: int = randint(1,6)
dice_rolls: list[int] = [roll1, roll2, roll3]
dice_sum: int = 0

dice_idx: int = 0
while dice_idx < len(dice_rolls):
    print(dice_rolls[dice_idx])
    dice_sum += dice_rolls[dice_idx]
    dice_idx += 1
print(dice_sum)

