"""Defining a Class"""
from __future__ import annotations 

"""
Think of a class def as a "roadmap" for objects that belong to a class
you are defining the underlying structure every instance of this class 
will have
"""


class Pizza:
    #attributes
    #think of htese as the variables
    #<name>: <type>
    size: str
    toppings: int
    gluten_free: bool
    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """Constructor"""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf
        #returns a pizza object
        
    def price(self) -> float:
        """Calculate price of pizza"""
        if self.size == "large":
            price: float = 6.23
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    def add_toppings(self, num_toppings: int):
        # add toppings to the existing pizza
        self.toppings += num_toppings
    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    def __str__(self) -> str:
        pizza_info: str = f"PIZZA ORDER: size {self.size} toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info


my_pizza: Pizza = Pizza("medium", 3, False)
print(my_pizza)
sals_pizza: Pizza = Pizza("large", 1, True)
print(sals_pizza)