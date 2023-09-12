"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730670385"

indices: int = 0
user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_letter: str = input("Enter a single character: ")
if len(user_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + user_letter + " in " + user_word)                
if user_letter == user_word[0]:
    print(user_letter + " found at index 0")
    indices = indices + 1
if user_letter == user_word[1]:
    print(user_letter + " found at index 1")
    indices = indices + 1
if user_letter == user_word[2]:
    print(user_letter + " found at index 2")
    indices = indices + 1
if user_letter == user_word[3]:
    print(user_letter + " found at index 3")
    indices = indices + 1
if user_letter == user_word[4]:
    print(user_letter + " found at index 4")
    indices = indices + 1
if indices == 1:
    print("1 instance of " + user_letter + " found in " + user_word)
    exit()
if indices > 1:
    print(str(indices) + " instances of " + user_letter + " found in " + user_word)
else: 
    print("No instances of " + user_letter + " found in " + user_word)