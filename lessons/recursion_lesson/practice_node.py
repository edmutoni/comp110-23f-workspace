"""Node Class for a linked list."""

from __future__ import annotations

class Node:
    data: int
    next: Node | None

    def __init__(self, data, next: Node | None):
        """Constructor."""
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        # base case
        if self.next is None:
            return str(self.data)
        else: 
            # recusive step
            return str(self.data) + " -> " + str(self.next)