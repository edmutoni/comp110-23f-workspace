"""File to define Bear class."""


class Bear:
    """Initializing bear attributes."""

    age: int
    hunger_score: int

    def __init__(self, init_age: int = 0, init_hunger_score: int = 0):
        """New bear with an age and a hunger score."""
        self.age = init_age
        self.hunger_score = init_hunger_score
        return None
    
    def one_day(self):
        """Adding 1 day to bear age and reducing the hunger score."""
        self.age = self.age + 1
        self.hunger_score = self.hunger_score - 1
        return None
    
    def eat(self, num_fish: int):
        """Adding to the hunger score if the bear eats."""
        self.hunger_score = self.hunger_score + num_fish