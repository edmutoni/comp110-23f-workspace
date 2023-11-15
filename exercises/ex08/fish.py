"""File to define Fish class."""


class Fish:
    """Attributes for fish."""

    age: int

    def __init__(self, init_age: int = 0):
        """Initializing a new fish."""
        self.age = init_age
        return None
    
    def one_day(self):
        """Adding one day to the fish age."""
        self.age = self.age + 1
        return None