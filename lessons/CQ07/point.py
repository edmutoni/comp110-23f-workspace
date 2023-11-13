"""OOP Exercise."""

from __future__ import annotations

__author__ = "930690385"


class Point:
    """Defining variables."""

    x: float
    y: float

    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        """Constructor."""
        self.x = init_x
        self.y = init_y

    def scale_by(self, factor: int) -> None:
        """Method to mutate the point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Method to scale a point and deliver a new one."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Printing out points in a readable way."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Overloading the * operator."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, additive: int | float) -> Point:
        """Overloading the addition operator."""
        return Point(self.x + additive, self.y + additive)