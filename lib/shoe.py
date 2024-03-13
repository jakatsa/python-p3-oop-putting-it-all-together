#!/usr/bin/env python3

class Shoe:
    """Represents a shoe with a brand and size."""

    def __init__(self, brand: str, size: int):
        self.brand = brand
        self._size = None  # Initialize _size attribute

        # Set size using property setter
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"