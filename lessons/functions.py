"""Demonstrates Functions"""
from random import randint

#function_name(<argument list>)

print("Hello")

x: int = (round(10.25))
#print(x)

z: int = randint(1,7)
#print(z)

#def function_name(<parameter list>) -> <return type>
"""Docstring defining function"""
    # <code part>

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    

max_number: int = my_max(1,10)
print(max_number)




def mimic(my_words: str) -> str:
    """Given the string my_words, output the same string"""
    return(my_words)


print(mimic("Hello"))

my_words: str = "hello"
response: str = mimic(my_words)
print(response)

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at the index letter_idx"""
    if letter_idx < len(my_words):
        return(my_words[letter_idx])
    else:
        return("Too high of an index")

print(mimic_letter("hello", 0))
print(mimic_letter("hello", 5))