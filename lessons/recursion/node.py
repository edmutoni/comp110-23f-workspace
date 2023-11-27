"""Node Class."""

from __future__ import annotations

__author__ = "930690385"


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns the data attribute for the first element in the linked list."""
        if self.next is None:
            return int(self.data)
        else:
            return int(self.data)
    
    def tail(self) -> Node | None:
        """Returns a linnked list of all elems minus the head."""
        if self.next is None:
            return None
        elif self.next.next is None:
            return self
        else:
            return self.next
    
    def last(self) -> int: 
        """Returns the data of the last element in the linked list."""
        if self.next is None:
            return int(self.data)
        elif self.next is not None:
            return self.next.last()